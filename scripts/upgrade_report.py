#!/usr/bin/env python3
"""Upgrade & Change Report generator (Kubepedia prototype).

Given two Kubespray versions, walk the chain of KDS UPGRADE-* documents between
them and assemble a consolidated, source-linked change report. With --inventory,
personalize it: drop notes about technologies the cluster doesn't use.

Usage:
    python scripts/upgrade_report.py --from v2.29.0 --to v2.31.0
    python scripts/upgrade_report.py --from v2.30.0 --to v2.31.0 -o report.md
    python scripts/upgrade_report.py --from v2.29.0 --to v2.31.0 \
        --inventory inventory/mycluster

Data source: the verified UPGRADE-V*__V* / RELEASE-V* / CONCEPT-* docs in kb/.
This is not KDS content; it reads the KB and emits a report.
"""
import argparse
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "index", "documents.jsonl")

# --- technology relevance model (for --inventory filtering) ---
CNI_PLUGINS = ["calico", "cilium", "flannel", "kube-ovn", "kube-router",
               "weave", "canal", "macvlan", "multus"]
# runtime keyword -> canonical container_manager value
RUNTIMES = {"containerd": "containerd", "cri-o": "crio", "cri_o": "crio",
            "crio": "crio", "docker": "docker"}
# optional add-on keyword -> the inventory enable variable
ADDON_ENABLE = {
    "metallb": "metallb_enabled",
    "kube-vip": "kube_vip_enabled",
    "ingress-nginx": "ingress_nginx_enabled",
    "cert-manager": "cert_manager_enabled",
    "metrics-server": "metrics_server_enabled",
    "cinder": "cinder_csi_enabled",
    "aws-ebs": "aws_ebs_csi_enabled",
    "azure": "azure_csi_enabled",
    "gcp-pd": "gcp_pd_csi_enabled",
    "vsphere": "vsphere_csi_enabled",
    "dashboard": "dashboard_enabled",
    "netcheck": "deploy_netchecker",
}
TRUE = {"true", "yes", "1", "on"}


def load_docs():
    docs = {}
    with open(INDEX) as f:
        for line in f:
            d = json.loads(line)
            docs[d["id"]] = d
    return docs


def id_to_version(vtok):
    return "v" + vtok[1:].replace("_", ".")


def version_key(v):
    return tuple(int(x) for x in v.lstrip("v").split("."))


def parse_upgrade_edges(docs):
    edges = {}
    for did in docs:
        m = re.match(r"^UPGRADE-(V[0-9_]+)__(V[0-9_]+)$", did)
        if m:
            edges[id_to_version(m.group(1))] = (id_to_version(m.group(2)), did)
    return edges


def build_chain(frm, to, edges):
    chain, cur, guard = [], frm, 0
    while cur != to:
        if cur not in edges:
            raise SystemExit(
                f"No upgrade path continues from {cur} toward {to} "
                f"(available starts: {sorted(edges, key=version_key)})")
        nxt, did = edges[cur]
        chain.append(did)
        cur = nxt
        guard += 1
        if guard > 50:
            raise SystemExit("upgrade chain too long / cycle")
    return chain


def read_sections(path):
    body = open(os.path.join(ROOT, path)).read().split("---", 2)[-1]
    sections, cur, buf = {}, None, []
    for line in body.splitlines():
        h = re.match(r"^##\s+(.*)$", line)
        if h:
            if cur:
                sections[cur] = "\n".join(buf).strip()
            cur, buf = h.group(1).strip(), []
        elif cur:
            buf.append(line)
    if cur:
        sections[cur] = "\n".join(buf).strip()
    return sections


def wikilinks(text):
    return set(re.findall(r"\[\[([A-Z][A-Z0-9_]*-[A-Z0-9_]+)\]\]", text))


# --- inventory profile & filtering ---
def parse_inventory(inv_path):
    """Scan inventory .yml files for the settings that decide relevance.
    Light regex (no YAML dep): captures top-level `key: value` scalars."""
    prof = {}
    files = glob.glob(os.path.join(inv_path, "**", "*.yml"), recursive=True) + \
        glob.glob(os.path.join(inv_path, "**", "*.yaml"), recursive=True)
    if os.path.isfile(inv_path):
        files = [inv_path]
    wanted = ({"kube_network_plugin", "container_manager", "kube_proxy_mode"}
              | set(ADDON_ENABLE.values()))
    for fp in files:
        try:
            for line in open(fp):
                m = re.match(r"^\s*([a-z0-9_]+)\s*:\s*([^#\n]+?)\s*$", line)
                if m and m.group(1) in wanted:
                    prof[m.group(1)] = m.group(2).strip().strip('"\'')
        except OSError:
            pass
    return prof


def relevance_sets(prof):
    """Return (active_keywords, inactive_keywords) from an inventory profile."""
    cni = prof.get("kube_network_plugin", "calico").lower()
    runtime = prof.get("container_manager", "containerd").lower()
    proxy = prof.get("kube_proxy_mode", "ipvs").lower()
    active, inactive = {cni, runtime, proxy}, set()
    # CNI: everything except the selected one is inactive
    for c in CNI_PLUGINS:
        (active if c == cni else inactive).add(c)
    # runtime: keywords mapping to a non-selected canonical value are inactive
    for kw, canon in RUNTIMES.items():
        (active if canon == runtime else inactive).add(kw)
    # optional add-ons: inactive unless their enable var is truthy
    for kw, var in ADDON_ENABLE.items():
        on = str(prof.get(var, "false")).lower() in TRUE
        (active if on else inactive).add(kw)
    return active, inactive


def filter_block(text, active, inactive):
    """Drop lines mentioning an inactive technology (and no active one).
    Returns (filtered_text, dropped_keywords)."""
    kept, dropped = [], set()
    for line in text.splitlines():
        low = line.lower()
        hit = [k for k in inactive if k in low]
        if hit and not any(a in low for a in active):
            dropped.update(hit)
            continue
        kept.append(line)
    return "\n".join(kept).strip(), dropped


def render(frm, to, chain, docs, prof=None):
    active = inactive = None
    if prof is not None:
        active, inactive = relevance_sets(prof)
    out, cited, all_dropped = [], set(), set()
    out.append(f"# Upgrade & Change Report — Kubespray {frm} → {to}\n")
    out.append(f"_Generated from Kubepedia KDS docs. {len(chain)} upgrade step(s) on the path._\n")
    if prof is not None:
        detected = {
            "CNI": prof.get("kube_network_plugin", "calico (default)"),
            "runtime": prof.get("container_manager", "containerd (default)"),
            "kube_proxy_mode": prof.get("kube_proxy_mode", "ipvs (default)"),
        }
        enabled = sorted(k for k, v in ADDON_ENABLE.items()
                         if str(prof.get(v, "false")).lower() in TRUE)
        out.append("**Personalized for your inventory** — profile: " +
                   ", ".join(f"{k}=`{v}`" for k, v in detected.items()) +
                   (f"; enabled add-ons: {', '.join(enabled) or 'none detected'}." ))
        out.append("_Notes about technologies you don't use are filtered out "
                   "(listed at the end for transparency)._\n")

    def maybe_filter(text):
        if prof is None or not text:
            return text
        f, dropped = filter_block(text, active, inactive)
        all_dropped.update(dropped)
        return f

    for did in chain:
        d = docs[did]
        sec = read_sections(d["path"])
        out.append(f"\n## Step: {d['title'].replace('Upgrade report ', '')}\n")
        if sec.get("Summary"):
            out.append(maybe_filter(sec["Summary"]) + "\n")
        if sec.get("Implementation"):
            out.append("**Version deltas**\n")
            out.append(maybe_filter(sec["Implementation"]) + "\n")
        if sec.get("Upgrade Notes"):
            out.append("**Required actions / breaking changes**\n")
            out.append(maybe_filter(sec["Upgrade Notes"]) + "\n")
        if sec.get("Compatibility"):
            out.append("**Compatibility constraints**\n")
            out.append(maybe_filter(sec["Compatibility"]) + "\n")
        cited.add(did)
        for s in sec.values():
            cited |= wikilinks(s)

    out.append("\n## Cross-cutting (Kubernetes layer)\n")
    for cid, desc in [
        ("CONCEPT-K8S_API_REMOVALS", "API removals crossing K8s minors"),
        ("CONCEPT-K8S_FEATURE_GATES", "feature-gate graduations/removals"),
        ("CONCEPT-COMPONENT_VERSION_SELECTION", "which component versions move, and why"),
        ("PRACTICE-UPGRADE_PREFLIGHT", "pre-upgrade checklist"),
        ("PRACTICE-GRACEFUL_UPGRADE", "drain/serial/pause mechanics"),
    ]:
        if cid in docs:
            out.append(f"- **{docs[cid]['title']}** — {desc}  `[{cid}]`")
            cited.add(cid)

    if prof is not None and all_dropped:
        out.append("\n## Filtered out (not in your inventory)\n")
        out.append("These technologies were mentioned in the source upgrade notes but "
                   "removed from the report above because your inventory doesn't use them:")
        out.append("`" + "`, `".join(sorted(all_dropped)) + "`")
        out.append("\n_Re-run without `--inventory` to see the full, unfiltered report._")

    out.append("\n## Sources (KDS documents)\n")
    for cid in sorted(cited):
        if cid in docs:
            out.append(f"- `{cid}` — {docs[cid]['title']}  ({docs[cid]['path']})")
        else:
            out.append(f"- `{cid}` — (referenced; resolve in kb/)")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Kubepedia Upgrade & Change Report")
    ap.add_argument("--from", dest="frm", required=True, help="from version, e.g. v2.29.0")
    ap.add_argument("--to", dest="to", required=True, help="to version, e.g. v2.31.0")
    ap.add_argument("--inventory", help="inventory dir/file to personalize (filter) the report")
    ap.add_argument("-o", "--out", help="write report to file (default: stdout)")
    args = ap.parse_args()

    frm = args.frm if args.frm.startswith("v") else "v" + args.frm
    to = args.to if args.to.startswith("v") else "v" + args.to
    if version_key(frm) >= version_key(to):
        raise SystemExit(f"--from ({frm}) must be lower than --to ({to})")

    docs = load_docs()
    edges = parse_upgrade_edges(docs)
    if not edges:
        raise SystemExit("no UPGRADE-* docs found in the index")
    chain = build_chain(frm, to, edges)

    prof = None
    if args.inventory:
        if not os.path.exists(args.inventory):
            raise SystemExit(f"inventory not found: {args.inventory}")
        prof = parse_inventory(args.inventory)
        print(f"inventory profile: {prof or '(no relevant keys found)'}", file=sys.stderr)

    report = render(frm, to, chain, docs, prof)
    if args.out:
        with open(args.out, "w") as f:
            f.write(report)
        print(f"wrote {args.out} ({len(chain)} steps)", file=sys.stderr)
    else:
        sys.stdout.write(report)


if __name__ == "__main__":
    main()
