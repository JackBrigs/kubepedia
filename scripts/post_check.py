#!/usr/bin/env python3
"""Post-upgrade verification (Kubepedia handle — pairs with upgrade_diff.py).

After a Kubespray upgrade, checks that the cluster and every managed component
actually took the upgrade: each component is at the **expected version for the
target tag** (catches the "component stuck on old version" class, e.g. a pinned
`cilium_version`), nodes/pods are healthy, and etcd is healthy.

Expected state comes from the KB (the RELEASE table for the target tag). Live state
comes from the cluster — gather it read-only and feed it in as JSON:

    scripts/post_check.py --version v2.31.0 --print-gather   # prints the commands to run
    # run those on the cluster, save the JSON, then:
    scripts/post_check.py --version v2.31.0 --facts facts.json

facts.json shape (all fields optional; missing => "not gathered"):
    {
      "components": {"Cilium": "1.18.4", "etcd": "3.6.10", "Kubernetes": "1.35.4"},
      "nodes":      [{"name": "n1", "ready": true, "kubelet": "v1.35.4"}],
      "pods_bad":   ["kube-system/cilium-abcde"],
      "etcd_healthy": true
    }
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "index", "documents.jsonl")

# component label (normalized) -> how to read its live version on the cluster
GATHER = {
    "Kubernetes": "kubectl get nodes -o jsonpath='{.items[*].status.nodeInfo.kubeletVersion}'",
    "Cilium": "kubectl -n kube-system get ds cilium -o jsonpath='{.spec.template.spec.containers[0].image}'",
    "CoreDNS": "kubectl -n kube-system get deploy coredns -o jsonpath='{.spec.template.spec.containers[0].image}'",
    "kube-proxy": "kubectl -n kube-system get ds kube-proxy -o jsonpath='{.spec.template.spec.containers[0].image}'",
    "metrics-server": "kubectl -n kube-system get deploy metrics-server -o jsonpath='{..image}'",
    "MetalLB": "kubectl -n metallb-system get deploy controller -o jsonpath='{..image}'",
    "etcd": "ETCDCTL_API=3 etcdctl version | head -1   # on an etcd node",
    "containerd": "ansible -i <inv> kube_node -m shell -a 'containerd --version'   # or: crictl version",
    "runc": "ansible -i <inv> kube_node -m shell -a 'runc --version'",
}


def load_docs():
    docs = {}
    with open(INDEX) as f:
        for line in f:
            d = json.loads(line)
            docs[d["id"]] = d
    return docs


def read_sections(path):
    body = open(os.path.join(ROOT, path)).read().split("---", 2)[-1]
    sec, cur, buf = {}, None, []
    for line in body.splitlines():
        h = re.match(r"^##\s+(.*)$", line)
        if h:
            if cur:
                sec[cur] = "\n".join(buf).strip()
            cur, buf = h.group(1).strip(), []
        elif cur:
            buf.append(line)
    if cur:
        sec[cur] = "\n".join(buf).strip()
    return sec


def norm(name):
    return re.sub(r"\(.*?\)", "", name).strip().lower()


def ver_token(s):
    m = re.search(r"[0-9]+\.[0-9]+[0-9.]*", str(s))
    return m.group(0) if m else str(s).strip()


def expected_versions(docs, tag):
    rid = "RELEASE-V" + tag.lstrip("v").replace(".", "_")
    out = {}
    if rid not in docs:
        return out
    for line in read_sections(docs[rid]["path"]).get("Implementation", "").splitlines():
        m = re.match(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$", line)
        if not m:
            continue
        name, val = m.group(1).strip(), re.sub(r"\*+", "", m.group(2)).strip()
        if name.lower() in ("component", "item") or set(name) <= set("-| "):
            continue
        out[name] = val
    return out


def render(tag, expected, facts, lang):
    ru = lang == "ru"
    comps = facts.get("components", {})
    nodes = facts.get("nodes", [])
    pods_bad = facts.get("pods_bad", [])
    out = [f"# {'Проверка после апгрейда' if ru else 'Post-upgrade check'} — Kubespray {tag}\n"]

    # --- version conformance ---
    out.append(f"\n## {'Конформность версий компонентов' if ru else 'Component version conformance'}\n")
    live_by_norm = {norm(k): v for k, v in comps.items()}
    ok = bad = ungathered = 0
    rows = []
    for name, exp in expected.items():
        # a component may have several acceptable versions in one cell (etcd/coredns
        # are computed per Kubernetes minor, e.g. "3.5.29 (1.33/1.34) / 3.6.10 (1.35)").
        # Strip the "(1.33/1.34)" K8s-minor qualifiers first so they aren't mistaken
        # for acceptable component versions.
        exp_tokens = re.findall(r"[0-9]+\.[0-9]+[0-9.]*", re.sub(r"\([^)]*\)", "", exp))
        if not exp_tokens:
            continue
        exp_disp = " / ".join(exp_tokens)
        live = live_by_norm.get(norm(name))
        if live is None:
            ungathered += 1
            rows.append(("⚪", name, exp_disp, "—", "не собрано" if ru else "not gathered"))
            continue
        live_t = ver_token(live)
        if live_t in exp_tokens:
            ok += 1
            rows.append(("✅", name, exp_disp, live_t, ""))
        else:
            bad += 1
            note = ("ЗАСТРЯЛ — не доехал до целевой версии" if ru
                    else "STUCK — did not reach the target version")
            rows.append(("❌", name, exp_disp, live_t, note))
    hdr = ("| | Компонент | Ожидалось | Фактически | |" if ru
           else "| | Component | Expected | Actual | |")
    out.append(hdr)
    out.append("|---|---|---|---|---|")
    for icon, name, exp_t, live_t, note in rows:
        out.append(f"| {icon} | {name} | `{exp_t}` | `{live_t}` | {note} |")
    summ = (f"\nИтог версий: ✅ {ok} совпало, ❌ {bad} застряло, ⚪ {ungathered} не собрано." if ru
            else f"\nVersions: ✅ {ok} match, ❌ {bad} stuck, ⚪ {ungathered} not gathered.")
    out.append(summ)
    if bad:
        out.append(("\n> ❌ **Компонент застрял** — почти всегда запиненная `*_version` в инвентаре "
                    "перекрывает тег. Проверь: `grep -rn '<comp>_version' inventory/`, убери пин и "
                    "переприменить роль (`cluster.yml --tags <роль>`)." if ru else
                    "\n> ❌ **A component is stuck** — almost always a pinned `*_version` in the "
                    "inventory overriding the tag. Check `grep -rn '<comp>_version' inventory/`, "
                    "remove the pin, re-apply the role."))

    # --- node / pod health ---
    out.append(f"\n## {'Здоровье узлов и подов' if ru else 'Node & pod health'}\n")
    if nodes:
        not_ready = [n["name"] for n in nodes if not n.get("ready")]
        icon = "✅" if not not_ready else "❌"
        out.append(f"{icon} {'узлов' if ru else 'nodes'}: {len(nodes)}, "
                   f"{'не Ready' if ru else 'not Ready'}: {not_ready or ('нет' if ru else 'none')}")
        wrong_kubelet = [n["name"] for n in nodes
                         if n.get("kubelet") and ver_token(n["kubelet"]) != ver_token(
                             expected.get("Kubernetes (default / min)", expected.get("Kubernetes", "")))]
        if wrong_kubelet:
            out.append(f"⚠ {'kubelet не на целевой версии на узлах' if ru else 'kubelet off-version on'}: "
                       f"{wrong_kubelet}")
    else:
        out.append("⚪ " + ("данные по узлам не собраны" if ru else "node data not gathered"))
    icon = "✅" if not pods_bad else "❌"
    out.append(f"{icon} {'проблемных подов' if ru else 'bad pods'}: "
               f"{pods_bad or ('нет' if ru else 'none')}")

    # --- etcd ---
    eh = facts.get("etcd_healthy")
    out.append(f"\n## etcd\n")
    if eh is None:
        out.append("⚪ " + ("не собрано (`etcdctl endpoint health --cluster`)" if ru else "not gathered"))
    else:
        out.append(("✅ etcd healthy" if eh else "❌ etcd НЕ healthy — проверь кворум/лидера"))

    # --- verdict ---
    fail = bad or pods_bad or (nodes and any(not n.get("ready") for n in nodes)) or (eh is False)
    out.append(f"\n## {'Вердикт' if ru else 'Verdict'}\n")
    out.append(("❌ **Апгрейд НЕ полностью подтверждён** — разберись с пунктами выше." if (fail and ru)
                else "✅ **Всё, что собрано, — в норме.**" if ru
                else "❌ **Upgrade not fully verified** — address the items above." if fail
                else "✅ **Everything gathered checks out.**"))
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Kubepedia post-upgrade verification")
    ap.add_argument("--version", required=True, help="target Kubespray tag, e.g. v2.31.0")
    ap.add_argument("--facts", help="JSON file of gathered live cluster facts")
    ap.add_argument("--print-gather", action="store_true",
                    help="print the read-only commands to collect the facts, then exit")
    ap.add_argument("--lang", choices=["ru", "en"], default="ru")
    args = ap.parse_args()
    tag = args.version if args.version.startswith("v") else "v" + args.version

    if args.print_gather:
        print(f"# Соберите факты на кластере (read-only) в facts.json для {tag}:")
        for comp, cmd in GATHER.items():
            print(f"#  {comp}:\n#    {cmd}")
        print("# health: kubectl get nodes; kubectl get pods -A | grep -vE 'Running|Completed'")
        print("# etcd:   ETCDCTL_API=3 etcdctl endpoint health --cluster")
        return

    docs = load_docs()
    expected = expected_versions(docs, tag)
    if not expected:
        raise SystemExit(f"no RELEASE table for {tag} in the KB")
    facts = {}
    if args.facts:
        facts = json.load(open(args.facts))
    else:
        print("note: no --facts given; showing expected-only skeleton. "
              "Run --print-gather to collect live facts.", file=sys.stderr)
    sys.stdout.write(render(tag, expected, facts, args.lang))


if __name__ == "__main__":
    main()
