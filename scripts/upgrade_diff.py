#!/usr/bin/env python3
"""Kubespray upgrade — inventory migration diff (Kubepedia handle #1, v2).

A focused, action-oriented report: given two Kubespray versions and your inventory,
it tells you **what to change in the inventory** to migrate:

  * component **version diff** (from -> to),
  * **variables to REMOVE** — defaults that no longer exist in the target tag, with
    the ones YOUR inventory still sets flagged loudly (they must be deleted),
  * **variables ADDED** in the target (new features / knobs to consider),
  * a short, clean action list — **no inline [[ID]] litter**; doc references live in
    a compact appendix at the end.

Version data: the KDS RELEASE-V* tables (curated). Variable data: a direct diff of the
Kubespray role **defaults** between the two tags in a local checkout (authoritative,
per-tag). Inventory resolution: **ansible-inventory** merges your group_vars folders
with real Ansible precedence — so a composite inventory (shared defaults folder +
cluster-specific folder + hosts) resolves exactly as `ansible-playbook` would.

Usage:
    scripts/upgrade_diff.py --from v2.28.1 --to v2.31.0 \
        --inventory scripts/examples/shared-defaults \
        --inventory scripts/examples/prod-cluster
    scripts/upgrade_diff.py --from v2.30.0 --to v2.31.0            # no inventory: generic diff
    scripts/upgrade_diff.py ... --lang en -o report.md

Needs a local Kubespray checkout with the tags fetched (default: ./kubespray-src) for
the variable diff, and `ansible-inventory` on PATH for inventory resolution (falls back
to a light scan if absent).
"""
import argparse
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "index", "documents.jsonl")

# ---- version diff (from the curated RELEASE-V* KDS tables) ----


def load_docs():
    docs = {}
    if os.path.exists(INDEX):
        with open(INDEX) as f:
            for line in f:
                d = json.loads(line)
                docs[d["id"]] = d
    return docs


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


def release_id(vtok):
    return "RELEASE-V" + vtok.lstrip("v").replace(".", "_")


def _norm_comp(name):
    return re.sub(r"\(.*?\)", "", name).strip().lower()


def parse_release_table(docs, vtok):
    rid = release_id(vtok)
    comps = {}
    if rid not in docs:
        return comps
    sec = read_sections(docs[rid]["path"])
    for line in sec.get("Implementation", "").splitlines():
        m = re.match(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$", line)
        if not m:
            continue
        name, ver = m.group(1).strip(), m.group(2).strip()
        if name.lower() in ("component", "item") or set(name) <= set("-| "):
            continue
        comps[name] = re.sub(r"\*+", "", ver).strip()
    return comps


def component_delta(docs, frm, to):
    cf, ct = parse_release_table(docs, frm), parse_release_table(docs, to)
    fmap = {_norm_comp(n): v for n, v in cf.items()}
    out = []
    for n, tv in ct.items():
        fv = fmap.get(_norm_comp(n), "—")
        if fv != tv:
            out.append((n, fv, tv))
    return out


# ---- variable diff (from the Kubespray role defaults, per tag) ----


def git_ls_defaults(src, tag):
    p = subprocess.run(
        ["git", "-C", src, "ls-tree", "-r", "--name-only", tag],
        capture_output=True, text=True)
    return [ln for ln in p.stdout.splitlines()
            if re.search(r"roles/.*/defaults/.*\.ya?ml$", ln)]


def tag_var_names(src, tag):
    """Set of top-level default variable names defined at a tag."""
    names = set()
    for f in git_ls_defaults(src, tag):
        p = subprocess.run(["git", "-C", src, "show", f"{tag}:{f}"],
                           capture_output=True, text=True)
        for m in re.finditer(r"^([a-z][a-z0-9_]*)\s*:", p.stdout, re.M):
            names.add(m.group(1))
    return names


def group_by_prefix(names):
    """Group variable names by their leading token for a compact listing."""
    groups = {}
    for n in sorted(names):
        pfx = n.split("_")[0]
        groups.setdefault(pfx, []).append(n)
    return groups


# ---- inventory resolution (ansible-inventory: real Ansible precedence) ----

_ANS_INTERNAL = {"inventory_hostname", "inventory_hostname_short", "group_names",
                 "inventory_dir", "inventory_file", "omit", "playbook_dir",
                 "inventory_hostname_short"}


def resolve_inventory(paths):
    """Return {var: value} the (possibly composite) inventory sets, merged with
    Ansible precedence via `ansible-inventory`; plus a small profile dict and the
    method used. Falls back to a light file scan if the tool isn't available."""
    args = ["ansible-inventory"]
    for p in paths:
        args += ["-i", p]
    args += ["--list"]
    try:
        p = subprocess.run(args, capture_output=True, text=True)
        if p.returncode != 0:
            raise RuntimeError(p.stderr.strip() or "ansible-inventory failed")
        data = json.loads(p.stdout)
    except (OSError, ValueError, RuntimeError) as e:
        return _scan_inventory(paths), {}, f"scan (ansible-inventory unavailable: {e})"
    hv = data.get("_meta", {}).get("hostvars", {})
    values = {}
    # group_vars apply cluster-wide; merge every host's resolved vars (last wins)
    for _host, vars_ in hv.items():
        for k, v in vars_.items():
            if k.startswith("ansible_") or k in _ANS_INTERNAL:
                continue
            values[k] = v
    profile = {k: values[k] for k in
               ("kube_network_plugin", "container_manager", "kube_proxy_mode",
                "kube_version", "external_cloud_provider", "cloud_provider")
               if values.get(k) is not None}
    return values, profile, "ansible-inventory"


def _scan_inventory(paths):
    values = {}
    for base in paths:
        files = []
        if os.path.isfile(base):
            files = [base]
        else:
            for dp, _dn, fn in os.walk(base):
                files += [os.path.join(dp, f) for f in fn
                          if f.endswith((".yml", ".yaml"))]
        for fp in files:
            try:
                for line in open(fp):
                    m = re.match(r"^\s*([a-z][a-z0-9_]*)\s*:\s*([^#\n]*?)\s*$", line)
                    if m:
                        values[m.group(1)] = m.group(2).strip().strip('"\'') or None
            except OSError:
                pass
    return values


# ---- i18n (framing Russian by default; no ID litter in the body) ----
STR = {
    "ru": {
        "title": "# Миграция инвентаря Kubespray: {frm} → {to}",
        "gen": "_Diff версий и переменных из исходников Kubespray (по тегам). Промежуточные релизы учтены (endpoint-diff)._",
        "profile": "**Ваш кластер:** {profile}.",
        "no_prof": "Инвентарь не задан — общий diff без привязки к вашему кластеру.",
        "resolved_by": "_Инвентарь разрешён через `{how}`; переменные слиты по правилам Ansible (составной инвентарь поддержан)._",
        "vers_h": "\n## Diff версий компонентов\n",
        "vers_none": "Изменений версий компонентов между этими релизами не зафиксировано в RELEASE-таблицах.",
        "th": ("Компонент", "было", "стало"),
        "warn_h": "\n## ⚠ Деструктивные действия и известные проблемы\n",
        "warn_intro": "Специфика этого перехода и вашей конфигурации, требующая ручных действий или простоя — прочитайте до апгрейда:",
        "warn_none": "Для этого перехода и вашей конфигурации особых деструктивных действий не выявлено (но всё равно снимите snapshot etcd).",
        "must_h": "\n## ⚠ Переменные, которые надо УДАЛИТЬ из вашего инвентаря\n",
        "must_intro": "Эти переменные **заданы в вашем инвентаре**, но в `{to}` их дефолтов больше нет — уберите их, иначе они игнорируются молча (а часть — признак удалённого аддона/фичи):",
        "must_none": "✅ Ваш инвентарь не задаёт переменных, удалённых в `{to}`.",
        "rem_h": "\n## Все удалённые переменные ({n}) — справочно\n",
        "rem_intro": "Дефолты, присутствовавшие в `{frm}` и отсутствующие в `{to}` (сгруппировано по префиксу):",
        "add_h": "\n## Новые переменные в {to} ({n}) — рассмотреть\n",
        "add_intro": "Появились новые дефолты — возможно, новые фичи/ручки, которые стоит включить или проверить:",
        "actions_h": "\n## Порядок действий\n",
        "actions": [
            "Идти **по одному минору Kubespray за раз** (пропускать нельзя).",
            "**Снять snapshot etcd** и пройти пред-апгрейдный чеклист.",
            "Удалить из инвентаря переменные из раздела ⚠ выше.",
            "Проверить новые переменные (раздел выше) — включить нужные.",
            "Прогнать security-матрицы для компонентов, у которых сменилась версия.",
        ],
        "docs_h": "\n## Подробнее (документы базы)\n",
        "note_inv": "Составной инвентарь: перечислите папки через несколько `--inventory` — они сольются как в Ansible.",
    },
    "en": {
        "title": "# Kubespray inventory migration: {frm} → {to}",
        "gen": "_Version & variable diff from the Kubespray sources (per tag). Intermediate releases covered (endpoint diff)._",
        "profile": "**Your cluster:** {profile}.",
        "no_prof": "No inventory given — generic diff, not tied to your cluster.",
        "resolved_by": "_Inventory resolved via `{how}`; variables merged with Ansible precedence (composite inventory supported)._",
        "vers_h": "\n## Component version diff\n",
        "vers_none": "No component version changes recorded in the RELEASE tables for this range.",
        "th": ("Component", "from", "to"),
        "warn_h": "\n## ⚠ Destructive actions & known issues\n",
        "warn_intro": "Specifics of this transition and your config that need a manual action or cause downtime — read before upgrading:",
        "warn_none": "No special destructive actions found for this transition and your config (still snapshot etcd first).",
        "must_h": "\n## ⚠ Variables to REMOVE from your inventory\n",
        "must_intro": "These are **set in your inventory** but their defaults no longer exist in `{to}` — remove them (they're silently ignored; some mark a removed add-on/feature):",
        "must_none": "✅ Your inventory sets no variables that were removed in `{to}`.",
        "rem_h": "\n## All removed variables ({n}) — reference\n",
        "rem_intro": "Defaults present in `{frm}` and absent in `{to}` (grouped by prefix):",
        "add_h": "\n## New variables in {to} ({n}) — consider\n",
        "add_intro": "New defaults appeared — possibly new features/knobs to enable or review:",
        "actions_h": "\n## Action order\n",
        "actions": [
            "Go **one Kubespray minor at a time** (no skipping).",
            "**Snapshot etcd** and run the pre-upgrade checklist.",
            "Delete the ⚠ variables above from your inventory.",
            "Review the new variables (section above) — enable what you need.",
            "Run the security matrices for components whose version changed.",
        ],
        "docs_h": "\n## Learn more (KB documents)\n",
        "note_inv": "Composite inventory: pass several `--inventory` folders — they merge like Ansible.",
    },
}

# curated, clean doc references (id + human name), shown only in the appendix
APPENDIX = [
    ("PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR", {"ru": "Runbook: апгрейд на один минор", "en": "Runbook: upgrade one minor"}),
    ("PRACTICE-UPGRADE_PREFLIGHT", {"ru": "Пред-апгрейдный чеклист", "en": "Pre-upgrade checklist"}),
    ("CONCEPT-K8S_URGENT_UPGRADE_NOTES", {"ru": "Обязательные действия перед апгрейдом (K8s)", "en": "Kubernetes urgent upgrade notes"}),
    ("CONCEPT-K8S_UPGRADE_SILENT_CHANGES", {"ru": "Тихие изменения поведения K8s", "en": "Kubernetes silent behavior changes"}),
    ("UPGRADE-CILIUM_1_15_TO_1_19", {"ru": "Cilium: ломающие изменения по версиям", "en": "Cilium breaking changes"}),
    ("UPGRADE-ARGOCD_2_11_TO_2_14", {"ru": "Argo CD: ломающие изменения по версиям", "en": "Argo CD breaking changes"}),
    ("CONCEPT-CLOUD_CONTROLLER_MANAGER", {"ru": "Внешний cloud-controller-manager", "en": "External cloud-controller-manager"}),
]

# which appendix docs are relevant to which inventory keyword
DOC_RELEVANCE = {
    "UPGRADE-CILIUM_1_15_TO_1_19": lambda p: p.get("kube_network_plugin") == "cilium",
    "UPGRADE-ARGOCD_2_11_TO_2_14": lambda keys: "argocd_enabled" in keys,
    "CONCEPT-CLOUD_CONTROLLER_MANAGER": lambda p: bool(
        p.get("cloud_provider") or p.get("external_cloud_provider")),
}


def _comp_span(vdelta, name):
    for n, f, t in vdelta:
        if _norm_comp(n) == name:
            return f, t
    return None


def build_warnings(frm, to, vdelta, values, lang):
    """Return a list of {ru, en} warnings from inventory-value and version-transition
    rules. Every rule is grounded (a real Kubespray/kubelet behavior); extend as new
    gotchas are confirmed."""
    w = []
    cni = str(values.get("kube_network_plugin", "")).lower()

    # --- inventory value-triggered (destructive follow-ups Kubespray doesn't do) ---
    cpu = str(values.get("kubelet_cpu_manager_policy", "")).lower()
    if cpu and cpu != "none":
        w.append({
            "ru": f"**CPU Manager (`kubelet_cpu_manager_policy: {cpu}`).** При смене политики "
                  f"или несовместимом сохранённом состоянии после апгрейда **kubelet не "
                  f"стартует**, пока вручную не удалить `/var/lib/kubelet/cpu_manager_state` и "
                  f"не перезапустить kubelet — **на каждом узле**. Kubespray этого не делает. "
                  f"То же для memory/topology manager (`memory_manager_state`).",
            "en": f"**CPU Manager (`kubelet_cpu_manager_policy: {cpu}`).** On a policy change or "
                  f"incompatible saved state after upgrade, **kubelet refuses to start** until "
                  f"you delete `/var/lib/kubelet/cpu_manager_state` and restart kubelet — **on "
                  f"each node**. Kubespray doesn't do this. Same for memory/topology manager."})
    top = str(values.get("kubelet_topology_manager_policy", "")).lower()
    if top and top != "none":
        w.append({
            "ru": f"**Topology Manager (`{top}`).** Смена политики Topology/Memory Manager "
                  f"так же требует удаления соответствующего `*_manager_state` в "
                  f"`/var/lib/kubelet/` и рестарта kubelet на узлах.",
            "en": f"**Topology Manager (`{top}`).** Changing the Topology/Memory Manager policy "
                  f"likewise needs the matching `*_manager_state` in `/var/lib/kubelet/` deleted "
                  f"and kubelet restarted on the nodes."})
    if str(values.get("kube_encrypt_secret_data", "")).lower() in ("true", "yes"):
        w.append({
            "ru": "**Шифрование Secret'ов включено.** Смена провайдера/ключа не перешифровывает "
                  "существующие Secret'ы автоматически — после изменения выполните "
                  "`kubectl get secrets -A -o json | kubectl replace -f -`, соблюдая порядок "
                  "провайдеров (иначе потеряете возможность их прочитать).",
            "en": "**Secret encryption is on.** Changing provider/key does not re-encrypt existing "
                  "Secrets — after the change run `kubectl get secrets -A -o json | kubectl replace "
                  "-f -`, respecting provider order (or you lose the ability to read them)."})

    # --- version-transition-triggered ---
    cil = _comp_span(vdelta, "cilium")
    if cil and cni in ("cilium", ""):
        span = f" (`{cil[0]}` → `{cil[1]}`)"
        w.append({
            "ru": f"**Переустановка/роллаут Cilium{span}.** Kubespray переприменяет CNI при "
                  f"смене версии — DaemonSet Cilium пересоздаётся/перекатывается, что даёт "
                  f"**простой сети подов на время роллаута** (наблюдалось, напр., на переходе к "
                  f"v2.29.1). Планируйте окно, делайте по одному узлу, проверьте связность после "
                  f"(netcheck).",
            "en": f"**Cilium reinstall/rollout{span}.** Kubespray re-applies the CNI on a version "
                  f"change — the Cilium DaemonSet is recreated/rolled, causing **pod-network "
                  f"downtime during the rollout** (observed e.g. on the v2.29.1 step). Plan a "
                  f"window, go node-by-node, verify connectivity after (netcheck)."})
    etc = _comp_span(vdelta, "etcd")
    if etc and "3.6" in etc[1]:
        w.append({
            "ru": "**etcd 3.6 (для K8s 1.35).** Мажорный переход etcd `3.5 → 3.6`. **In-place "
                  "даунгрейда нет** — обязательно snapshot до апгрейда; изучите операционные "
                  "изменения etcd 3.6 перед переходом на 1.35.",
            "en": "**etcd 3.6 (for K8s 1.35).** Major etcd `3.5 → 3.6`. **No in-place downgrade** "
                  "— snapshot before, and review etcd 3.6 operational changes before moving to 1.35."})
    kube = _comp_span(vdelta, "kubernetes")
    if kube and "1.35" in kube[1]:
        w.append({
            "ru": "**cgroup v1 → жёсткая ошибка на K8s 1.35.** Preflight kubeadm/kubelet **падает** "
                  "при cgroup v1 на узлах с kubelet ≥1.35. Мигрируйте узлы на **cgroup v2** до "
                  "апгрейда, либо задайте `failCgroupV1: false` в ConfigMap `kubelet-config`.",
            "en": "**cgroup v1 → hard error on K8s 1.35.** kubeadm/kubelet preflight **fails** on "
                  "cgroup v1 with kubelet ≥1.35. Migrate nodes to **cgroup v2** before upgrading, "
                  "or set `failCgroupV1: false` in the `kubelet-config` ConfigMap."})
    return w


def render(frm, to, docs, vdelta, removed, added, set_vars, values, profile, how, lang):
    S = STR[lang]
    out = [S["title"].format(frm=frm, to=to) + "\n", S["gen"] + "\n"]
    if profile:
        prof = ", ".join(f"{k}=`{v}`" for k, v in profile.items())
        out.append(S["profile"].format(profile=prof))
    elif set_vars:
        out.append(S["resolved_by"].format(how=how))
    else:
        out.append(S["no_prof"])
    if set_vars and profile:
        out.append(S["resolved_by"].format(how=how))

    # version diff
    out.append(S["vers_h"])
    if vdelta:
        out.append(f"| {S['th'][0]} | {S['th'][1]} | {S['th'][2]} |")
        out.append("|---|---|---|")
        for n, fv, tv in vdelta:
            out.append(f"| {n} | {fv} | {tv} |")
    else:
        out.append(S["vers_none"])

    # ⚠ destructive actions & known issues (inventory-value + transition rules)
    warns = build_warnings(frm, to, vdelta, values, lang)
    out.append(S["warn_h"])
    if warns:
        out.append(S["warn_intro"])
        for wn in warns:
            out.append(f"- {wn[lang]}")
    else:
        out.append(S["warn_none"])

    # ⚠ variables to remove (set ∩ removed) — the headline
    must = sorted(set_vars & removed)
    out.append(S["must_h"])
    if must:
        out.append(S["must_intro"].format(to=to))
        for v in must:
            out.append(f"- **`{v}`**")
    else:
        out.append(S["must_none"].format(to=to))

    # all removed (grouped) — reference
    if removed:
        out.append(S["rem_h"].format(n=len(removed)))
        out.append(S["rem_intro"].format(frm=frm, to=to))
        for pfx, names in sorted(group_by_prefix(removed).items()):
            if len(names) == 1:
                out.append(f"- `{names[0]}`")
            else:
                out.append(f"- `{pfx}_*` — {len(names)}: " +
                           ", ".join(f"`{n}`" for n in names[:6]) +
                           (" …" if len(names) > 6 else ""))

    # added — consider
    if added:
        shown = sorted(added)
        out.append(S["add_h"].format(to=to, n=len(added)))
        out.append(S["add_intro"])
        for v in shown[:40]:
            out.append(f"- `{v}`")
        if len(shown) > 40:
            out.append(f"- … (+{len(shown) - 40})")

    # action order (clean, no litter)
    out.append(S["actions_h"])
    for i, a in enumerate(S["actions"], 1):
        out.append(f"{i}. {a}")

    # appendix — the only place IDs appear
    relevant = []
    for did, name in APPENDIX:
        rel = DOC_RELEVANCE.get(did)
        if rel is not None:
            arg = profile if did != "UPGRADE-ARGOCD_2_11_TO_2_14" else set_vars
            if not rel(arg):
                continue
        if not docs or did in docs:
            relevant.append((did, name[lang]))
    if relevant:
        out.append(S["docs_h"])
        for did, name in relevant:
            path = f"  ({docs[did]['path']})" if did in docs else ""
            out.append(f"- {name} — `{did}`{path}")

    out.append("\n> " + S["note_inv"])
    return "\n".join(out) + "\n"


def version_key(v):
    return tuple(int(x) for x in re.findall(r"\d+", v))


def main():
    ap = argparse.ArgumentParser(description="Kubespray inventory migration diff")
    ap.add_argument("--from", dest="frm", required=True)
    ap.add_argument("--to", dest="to", required=True)
    ap.add_argument("--inventory", action="append", default=[],
                    help="inventory dir/file (repeat for composite; merged like Ansible)")
    ap.add_argument("--src", default=os.path.join(ROOT, "kubespray-src"),
                    help="Kubespray git checkout with the tags (default ./kubespray-src)")
    ap.add_argument("--lang", choices=["ru", "en"], default="ru")
    ap.add_argument("-o", "--out")
    args = ap.parse_args()

    frm = args.frm if args.frm.startswith("v") else "v" + args.frm
    to = args.to if args.to.startswith("v") else "v" + args.to
    if version_key(frm) >= version_key(to):
        raise SystemExit(f"--from ({frm}) must be lower than --to ({to})")
    if not os.path.isdir(os.path.join(args.src, ".git")):
        raise SystemExit(f"Kubespray checkout not found at {args.src} (need it for the "
                         f"variable diff) — pass --src /path/to/kubespray")

    docs = load_docs()
    vdelta = component_delta(docs, frm, to)

    fvars = tag_var_names(args.src, frm)
    tvars = tag_var_names(args.src, to)
    if not fvars or not tvars:
        raise SystemExit(f"could not read default vars for {frm}/{to} — are the tags fetched?")
    removed, added = fvars - tvars, tvars - fvars

    values, profile, how = {}, {}, ""
    if args.inventory:
        values, profile, how = resolve_inventory(args.inventory)
        print(f"inventory: {len(values)} vars via {how}", file=sys.stderr)
    set_vars = set(values)

    report = render(frm, to, docs, vdelta, removed, added, set_vars, values,
                    profile, how, args.lang)
    if args.out:
        open(args.out, "w").write(report)
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(report)


if __name__ == "__main__":
    main()
