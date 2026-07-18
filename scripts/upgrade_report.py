#!/usr/bin/env python3
"""Upgrade & Change Report generator (Kubepedia prototype).

Given two Kubespray versions, walk the chain of KDS UPGRADE-* documents between
them and assemble a consolidated, source-linked change report. It is KB-driven:
beyond the upgrade-notes chain it derives, from the KDS graph,
  * a **component version-change** table (diffed from the RELEASE-V* docs),
  * a **CVE-exposure** section (per moving component -> its osv.dev CVE matrix
    + the consolidated remediation runbook),
  * **Kubernetes layer changes** for the minors that newly enter the support
    window (CONCEPT-K8S_1_XX_CHANGES), and
  * cross-cutting upgrade mechanics (kubeadm seam, health-check, version skew,
    upgrade horizon, preflight/graceful-upgrade practices).
With --inventory, personalize it against a real Kubespray inventory: it detects
the CNI, runtime, kube_proxy_mode, kube_version, cloud provider, and enabled
add-ons, then
  * drops notes about technologies the cluster doesn't use,
  * surfaces the **deep component version-jump** docs for the components you run
    (e.g. Cilium/Argo CD breaking-change docs — COMP_TO_UPGRADE),
  * links the **Kubernetes behavior-change** layer (urgent upgrade notes +
    silent default-flips — K8S_BEHAVIOR), and
  * adds a **cloud-controller-manager** section when a cloud provider is set.

Usage:
    python scripts/upgrade_report.py --from v2.29.0 --to v2.31.0
    python scripts/upgrade_report.py --from v2.30.0 --to v2.31.0 -o report.md
    python scripts/upgrade_report.py --from v2.28.1 --to v2.31.0 \
        --inventory scripts/examples/sample-inventory      # demo fixture

The report **framing is Russian by default** (`--lang ru`) because the operator/admin
reading it is Russian-speaking; pass `--lang en` for English. Verbatim excerpts
pulled from the KDS docs stay in **English** (the KB's knowledge language, a recorded
decision) — only the report's own headers/labels/descriptions are localized, and
every quoted fact links to its source doc.

Data source: the verified UPGRADE-* / RELEASE-V* / CONCEPT-* / TROUBLE-* docs in
kb/ (read via index/documents.jsonl). This is not KDS content; it reads the KB
and emits a report — the first consumer "handle" over the knowledge base.
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
    "argocd": "argocd_enabled",
    "helm": "helm_enabled",
}
TRUE = {"true", "yes", "1", "on"}

# active component keyword -> its deep component version-jump UPGRADE doc.
# Surfaced only when the component is in the inventory (personalized).
COMP_TO_UPGRADE = {
    "cilium": "UPGRADE-CILIUM_1_15_TO_1_19",
    "argocd": "UPGRADE-ARGOCD_2_11_TO_2_14",
}
# Kubernetes-layer behavior docs relevant to any multi-version upgrade.
K8S_BEHAVIOR = ["CONCEPT-K8S_URGENT_UPGRADE_NOTES",
                "CONCEPT-K8S_UPGRADE_SILENT_CHANGES"]


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
    wanted = ({"kube_network_plugin", "container_manager", "kube_proxy_mode",
               "kube_version", "cloud_provider", "external_cloud_provider"}
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


# --- KB-driven enrichment (RELEASE tables, CVE matrices, K8s layer) ---
def release_id(vtok):
    """v2.29.0 -> RELEASE-V2_29_0"""
    return "RELEASE-V" + vtok.lstrip("v").replace(".", "_")


def parse_release_table(docs, vtok):
    """From a RELEASE doc: ({component: version}, {k8s_minor, ...})."""
    rid = release_id(vtok)
    comps, minors = {}, set()
    if rid not in docs:
        return comps, minors
    sec = read_sections(docs[rid]["path"])
    for line in sec.get("Implementation", "").splitlines():
        m = re.match(r"^\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*$", line)
        if not m:
            continue
        name, ver = m.group(1).strip(), m.group(2).strip()
        if name.lower() == "component" or set(name) <= set("-| "):
            continue
        comps[name] = ver
    for mm in re.findall(r"1\.(3[0-9])", sec.get("Compatibility", "")):
        minors.add("1." + mm)
    return comps, minors


def _norm_comp(name):
    """Normalize a component label so it matches across RELEASE docs:
    'Cilium' == 'cilium', 'CoreDNS (default)' == 'CoreDNS'."""
    return re.sub(r"\(.*?\)", "", name).strip().lower()


def component_delta(docs, frm, to):
    """[(component, from_version, to_version)] for components that changed.
    Matches on a normalized key so label drift across RELEASE docs doesn't
    show unchanged components as new ('—')."""
    cf, _ = parse_release_table(docs, frm)
    ct, _ = parse_release_table(docs, to)
    fmap = {_norm_comp(n): v for n, v in cf.items()}
    out = []
    for n, tv in ct.items():
        fv = fmap.get(_norm_comp(n), "—")
        if fv != tv:
            out.append((n, fv, tv))
    return out


COMP_TO_CVE = {
    "runc": "TROUBLE-RUNC_KNOWN_CVES",
    "containerd": "TROUBLE-CONTAINERD_KNOWN_CVES",
    "cilium": "TROUBLE-CILIUM_KNOWN_CVES",
    "coredns": "TROUBLE-COREDNS_KNOWN_CVES",
    "cni-plugins": "TROUBLE-CNI_PLUGINS_KNOWN_CVES",
    "cert-manager": "TROUBLE-CERT_MANAGER_KNOWN_CVES",
    "helm": "TROUBLE-HELM_KNOWN_CVES",
    "kubernetes": "TROUBLE-KUBERNETES_KNOWN_CVES",
}


def cve_id_for(comp_name):
    return COMP_TO_CVE.get(comp_name.lower().split("(")[0].strip())


# --- i18n: the report framing is user-facing (default Russian for the admin).
# Verbatim excerpts pulled from KDS docs stay in English (the KB's knowledge
# language, a recorded decision) — the framing is localized, the quoted facts are
# linked to their source docs. ---
STRINGS = {
    "ru": {
        "title": "# Отчёт об апгрейде и изменениях — Kubespray {frm} → {to}",
        "generated": "_Сгенерировано из базы знаний Kubepedia (KDS). Шагов апгрейда на пути: {n}._",
        "personalized": "**Персонализировано под ваш inventory** — профиль: {profile}",
        "addons": "; включённые аддоны: {addons}.",
        "none": "не обнаружено",
        "filter_note": "_Пункты про технологии, которых у вас нет, отфильтрованы (перечислены в конце для прозрачности)._",
        "excerpt_note": "_Дословные выдержки из документов базы приведены на английском (язык знаний базы); ссылки на источники — в конце отчёта._",
        "step": "\n## Шаг: {t}\n",
        "deltas": "**Изменения версий**\n",
        "actions": "**Необходимые действия / breaking changes**\n",
        "compat": "**Ограничения совместимости**\n",
        "comp_h": "\n## Изменения версий компонентов ({frm} → {to})\n",
        "component": "Компонент",
        "cve_h": "\n## Безопасность / экспозиция CVE\n",
        "cve_intro": "Перемещение этих компонентов меняет их экспозицию к CVE (osv.dev, по конкретной поставляемой версии) — сравните строки from/to в каждой матрице:",
        "cve_line": "- **{name}** `{fv}` → `{tv}` — сравните экспозицию в матрице по версиям  `[{cid}]`.",
        "cve_runbook": "- Сводный runbook «уязвим ли я / что обновлять»  `[CONCEPT-CVE_REMEDIATION]`.",
        "k8s_h": "\n## Изменения слоя Kubernetes (новые миноры: {minors})\n",
        "k8s_intro": "Миноры, входящие в окно поддержки на этом пути — прочитайте их операторские изменения:",
        "k8s_line": "- **Kubernetes {mnr}** — {title}  `[{cid}]`",
        "deep_h": "\n## Глубокий разбор компонентов — breaking changes для ваших компонентов\n",
        "deep_intro": "Ваш inventory использует эти компоненты; прочитайте их доки breaking changes по версиям (глубокие upstream-факты на точных версиях, что ставит Kubespray — сверх таблицы release-дельт выше):",
        "behav_h": "\n## Изменения поведения Kubernetes на этом пути\n",
        "behav_intro": "Переход между минорами Kubernetes меняет поведение двумя путями — действия, которые НУЖНО выполнить, и дефолты, которые меняются молча:",
        "cloud_h": "\n## Облачный провайдер (внешний cloud-controller-manager)\n",
        "cloud_intro": "Ваш кластер использует облачный провайдер — in-tree провайдеры удалены в K8s 1.29–1.31, поэтому убедитесь, что внешний CCM + CSI на месте:",
        "cross_h": "\n## Сквозное (слой Kubernetes и механика апгрейда)\n",
        "filtered_h": "\n## Отфильтровано (нет в вашем inventory)\n",
        "filtered_text": "Эти технологии упоминались в исходных upgrade-заметках, но убраны из отчёта выше, потому что ваш inventory их не использует:",
        "filtered_rerun": "\n_Запустите без `--inventory`, чтобы увидеть полный неотфильтрованный отчёт._",
        "sources_h": "\n## Источники (документы KDS)\n",
        "source_ref": "(упомянут; ищите в kb/)",
    },
    "en": {
        "title": "# Upgrade & Change Report — Kubespray {frm} → {to}",
        "generated": "_Generated from Kubepedia KDS docs. {n} upgrade step(s) on the path._",
        "personalized": "**Personalized for your inventory** — profile: {profile}",
        "addons": "; enabled add-ons: {addons}.",
        "none": "none detected",
        "filter_note": "_Notes about technologies you don't use are filtered out (listed at the end for transparency)._",
        "excerpt_note": "_Verbatim excerpts from the KB docs are in English (the KB's knowledge language); source links are at the end._",
        "step": "\n## Step: {t}\n",
        "deltas": "**Version deltas**\n",
        "actions": "**Required actions / breaking changes**\n",
        "compat": "**Compatibility constraints**\n",
        "comp_h": "\n## Component version changes ({frm} → {to})\n",
        "component": "Component",
        "cve_h": "\n## Security / CVE exposure\n",
        "cve_intro": "Moving these components changes their CVE exposure (osv.dev, per shipped version) — compare the from/to rows in each matrix:",
        "cve_line": "- **{name}** `{fv}` → `{tv}` — compare exposure in the per-version matrix  `[{cid}]`.",
        "cve_runbook": "- Consolidated *am I exposed / what to upgrade* runbook  `[CONCEPT-CVE_REMEDIATION]`.",
        "k8s_h": "\n## Kubernetes layer changes (new minors: {minors})\n",
        "k8s_intro": "Minors that enter the support window on this path — read their operator-relevant changes:",
        "k8s_line": "- **Kubernetes {mnr}** — {title}  `[{cid}]`",
        "deep_h": "\n## Component deep-dive — breaking changes for your components\n",
        "deep_intro": "Your inventory uses these components; read their per-version breaking-change docs (deep upstream-mined notes at the exact versions Kubespray ships, beyond the release-delta table above):",
        "behav_h": "\n## Kubernetes behavior changes on this path\n",
        "behav_intro": "Crossing Kubernetes minors changes behavior two ways — actions you MUST take, and defaults that shift silently:",
        "cloud_h": "\n## Cloud provider (external cloud-controller-manager)\n",
        "cloud_intro": "Your cluster uses a cloud provider — the in-tree providers were removed across K8s 1.29–1.31, so confirm the external CCM + CSI are in place:",
        "cross_h": "\n## Cross-cutting (Kubernetes layer & upgrade mechanics)\n",
        "filtered_h": "\n## Filtered out (not in your inventory)\n",
        "filtered_text": "These technologies were mentioned in the source upgrade notes but removed from the report above because your inventory doesn't use them:",
        "filtered_rerun": "\n_Re-run without `--inventory` to see the full, unfiltered report._",
        "sources_h": "\n## Sources (KDS documents)\n",
        "source_ref": "(referenced; resolve in kb/)",
    },
}

# doc-id -> localized one-line description (cross-cutting + behavior sections)
DESC = {
    "CONCEPT-K8S_URGENT_UPGRADE_NOTES": {
        "ru": "обязательные действия перед апгрейдом (удалённые kubelet-флаги, hard-error cgroup v1, …)",
        "en": "must-do actions before you upgrade (removed kubelet flags, cgroup-v1 hard error, …)"},
    "CONCEPT-K8S_UPGRADE_SILENT_CHANGES": {
        "ru": "поведение, меняющееся без правки конфига (GA feature-gate'ов, смена дефолтов, депрекейшены)",
        "en": "behavior that changes with no config edit (feature-gate GAs, default flips, deprecations)"},
    "CONCEPT-K8S_API_REMOVALS": {
        "ru": "удаления API при переходе между минорами Kubernetes",
        "en": "API removals crossing K8s minors"},
    "CONCEPT-K8S_FEATURE_GATES": {
        "ru": "выпуск (GA) и удаление feature-gate'ов",
        "en": "feature-gate graduations/removals"},
    "CONCEPT-COMPONENT_VERSION_SELECTION": {
        "ru": "какие версии компонентов меняются и почему",
        "en": "which component versions move, and why"},
    "CONCEPT-UPGRADE_HORIZON": {
        "ru": "насколько поставляемые версии отстают от последнего upstream",
        "en": "how far the shipped versions are behind latest upstream"},
    "CONCEPT-KUBESPRAY_KUBEADM_SEAM": {
        "ru": "кто выполняет апгрейд (kubeadm) vs Kubespray",
        "en": "who does the upgrade (kubeadm) vs Kubespray"},
    "TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK": {
        "ru": "если control plane не поднимается посреди апгрейда",
        "en": "if the control plane won't come up mid-upgrade"},
    "TROUBLE-KUBEADM_VERSION_SKEW": {
        "ru": "правило «по одному минору за раз» (version skew)",
        "en": "one-minor-at-a-time skew rule"},
    "PRACTICE-UPGRADE_PREFLIGHT": {
        "ru": "пред-апгрейдный чеклист",
        "en": "pre-upgrade checklist"},
    "PRACTICE-GRACEFUL_UPGRADE": {
        "ru": "механика drain/serial/pause",
        "en": "drain/serial/pause mechanics"},
}

CROSSCUT_IDS = [
    "CONCEPT-K8S_API_REMOVALS", "CONCEPT-K8S_FEATURE_GATES",
    "CONCEPT-COMPONENT_VERSION_SELECTION", "CONCEPT-UPGRADE_HORIZON",
    "CONCEPT-KUBESPRAY_KUBEADM_SEAM", "TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK",
    "TROUBLE-KUBEADM_VERSION_SKEW", "PRACTICE-UPGRADE_PREFLIGHT",
    "PRACTICE-GRACEFUL_UPGRADE",
]


def render(frm, to, chain, docs, prof=None, lang="ru"):
    S = STRINGS[lang]
    active = inactive = None
    if prof is not None:
        active, inactive = relevance_sets(prof)
    out, cited, all_dropped = [], set(), set()
    out.append(S["title"].format(frm=frm, to=to) + "\n")
    out.append(S["generated"].format(n=len(chain)) + "\n")
    if prof is not None:
        detected = {
            "CNI": prof.get("kube_network_plugin", "calico (default)"),
            "runtime": prof.get("container_manager", "containerd (default)"),
            "kube_proxy_mode": prof.get("kube_proxy_mode", "ipvs (default)"),
        }
        if prof.get("kube_version"):
            detected["kube_version"] = prof["kube_version"]
        cloud = prof.get("external_cloud_provider") or prof.get("cloud_provider")
        if cloud:
            detected["cloud"] = cloud
        enabled = sorted(k for k, v in ADDON_ENABLE.items()
                         if str(prof.get(v, "false")).lower() in TRUE)
        profile = ", ".join(f"{k}=`{v}`" for k, v in detected.items())
        out.append(S["personalized"].format(profile=profile) +
                   S["addons"].format(addons=", ".join(enabled) or S["none"]))
        out.append(S["filter_note"])
    out.append(S["excerpt_note"] + "\n")

    def maybe_filter(text):
        if prof is None or not text:
            return text
        f, dropped = filter_block(text, active, inactive)
        all_dropped.update(dropped)
        return f

    for did in chain:
        d = docs[did]
        sec = read_sections(d["path"])
        out.append(S["step"].format(t=d['title'].replace('Upgrade report ', '')))
        if sec.get("Summary"):
            out.append(maybe_filter(sec["Summary"]) + "\n")
        if sec.get("Implementation"):
            out.append(S["deltas"])
            out.append(maybe_filter(sec["Implementation"]) + "\n")
        if sec.get("Upgrade Notes"):
            out.append(S["actions"])
            out.append(maybe_filter(sec["Upgrade Notes"]) + "\n")
        if sec.get("Compatibility"):
            out.append(S["compat"])
            out.append(maybe_filter(sec["Compatibility"]) + "\n")
        cited.add(did)
        for s in sec.values():
            cited |= wikilinks(s)

    # --- Component version deltas (from RELEASE docs) ---
    delta = component_delta(docs, frm, to)
    shown_delta = []
    if delta:
        for name, fv, tv in delta:
            row = f"| {name} | {fv} | {tv} |"
            if prof is not None:
                fl, dropped = filter_block(row, active, inactive)
                all_dropped.update(dropped)
                if not fl.strip():
                    continue
            shown_delta.append((name, fv, tv))
    if shown_delta:
        out.append(S["comp_h"].format(frm=frm, to=to))
        out.append("| " + S["component"] + " | " + frm + " | " + to + " |")
        out.append("|---|---|---|")
        for name, fv, tv in shown_delta:
            out.append(f"| {name} | {fv} | {tv} |")
        cited.add(release_id(frm))
        cited.add(release_id(to))

    # --- CVE exposure for components that move ---
    cve_lines = []
    for name, fv, tv in shown_delta:
        cid = cve_id_for(name)
        if cid and cid in docs:
            cve_lines.append(S["cve_line"].format(name=name, fv=fv, tv=tv, cid=cid))
            cited.add(cid)
    if cve_lines:
        out.append(S["cve_h"])
        out.append(S["cve_intro"])
        out.extend(cve_lines)
        if "CONCEPT-CVE_REMEDIATION" in docs:
            out.append(S["cve_runbook"])
            cited.add("CONCEPT-CVE_REMEDIATION")

    # --- Kubernetes layer changes for newly-entered minors ---
    _, mf = parse_release_table(docs, frm)
    _, mt = parse_release_table(docs, to)
    new_minors = sorted(mt - mf)
    if new_minors:
        out.append(S["k8s_h"].format(minors=", ".join(new_minors)))
        out.append(S["k8s_intro"])
        for mnr in new_minors:
            cid = "CONCEPT-K8S_" + mnr.replace(".", "_") + "_CHANGES"
            if cid in docs:
                out.append(S["k8s_line"].format(mnr=mnr, title=docs[cid]['title'], cid=cid))
                cited.add(cid)

    # --- Component deep-dive version-jump upgrade docs (personalized) ---
    comp_lines = []
    for kw, uid in COMP_TO_UPGRADE.items():
        if uid not in docs:
            continue
        if prof is not None and kw not in active:
            continue
        comp_lines.append(f"- **{docs[uid]['title']}**  `[{uid}]`")
        cited.add(uid)
    if comp_lines:
        out.append(S["deep_h"])
        out.append(S["deep_intro"])
        out.extend(comp_lines)

    # --- Kubernetes behavior changes on this path (silent + urgent) ---
    kb_lines = []
    for cid in K8S_BEHAVIOR:
        if cid in docs:
            kb_lines.append(f"- **{docs[cid]['title']}** — {DESC[cid][lang]}  `[{cid}]`")
            cited.add(cid)
    if kb_lines:
        out.append(S["behav_h"])
        out.append(S["behav_intro"])
        out.extend(kb_lines)

    # --- Cloud provider (external CCM), only if the inventory uses one ---
    if prof is not None and (prof.get("cloud_provider") or prof.get("external_cloud_provider")):
        ccm_lines = []
        for cid in ("CONCEPT-CLOUD_CONTROLLER_MANAGER",
                    "TROUBLE-K8S_INTREE_CLOUD_PROVIDER_REMOVED"):
            if cid in docs:
                ccm_lines.append(f"- **{docs[cid]['title']}**  `[{cid}]`")
                cited.add(cid)
        if ccm_lines:
            out.append(S["cloud_h"])
            out.append(S["cloud_intro"])
            out.extend(ccm_lines)

    out.append(S["cross_h"])
    for cid in CROSSCUT_IDS:
        if cid in docs:
            out.append(f"- **{docs[cid]['title']}** — {DESC[cid][lang]}  `[{cid}]`")
            cited.add(cid)

    if prof is not None and all_dropped:
        out.append(S["filtered_h"])
        out.append(S["filtered_text"])
        out.append("`" + "`, `".join(sorted(all_dropped)) + "`")
        out.append(S["filtered_rerun"])

    out.append(S["sources_h"])
    for cid in sorted(cited):
        if cid in docs:
            out.append(f"- `{cid}` — {docs[cid]['title']}  ({docs[cid]['path']})")
        else:
            out.append(f"- `{cid}` — {S['source_ref']}")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description="Kubepedia Upgrade & Change Report")
    ap.add_argument("--from", dest="frm", required=True, help="from version, e.g. v2.29.0")
    ap.add_argument("--to", dest="to", required=True, help="to version, e.g. v2.31.0")
    ap.add_argument("--inventory", help="inventory dir/file to personalize (filter) the report")
    ap.add_argument("--lang", choices=["ru", "en"], default="ru",
                    help="report framing language (default: ru — the admin reads Russian; "
                         "verbatim doc excerpts stay English, the KB's knowledge language)")
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

    report = render(frm, to, chain, docs, prof, lang=args.lang)
    if args.out:
        with open(args.out, "w") as f:
            f.write(report)
        print(f"wrote {args.out} ({len(chain)} steps)", file=sys.stderr)
    else:
        sys.stdout.write(report)


if __name__ == "__main__":
    main()
