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
K8S_BEHAVIOR = [
    ("CONCEPT-K8S_URGENT_UPGRADE_NOTES",
     "must-do actions before you upgrade (removed kubelet flags, cgroup-v1 hard error, …)"),
    ("CONCEPT-K8S_UPGRADE_SILENT_CHANGES",
     "behavior that changes with no config edit (feature-gate GAs, default flips, deprecations)"),
]


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
        if prof.get("kube_version"):
            detected["kube_version"] = prof["kube_version"]
        cloud = prof.get("external_cloud_provider") or prof.get("cloud_provider")
        if cloud:
            detected["cloud"] = cloud
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
        out.append(f"\n## Component version changes ({frm} → {to})\n")
        out.append("| Component | " + frm + " | " + to + " |")
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
            cve_lines.append(
                f"- **{name}** `{fv}` → `{tv}` — compare exposure in the per-version "
                f"matrix  `[{cid}]`.")
            cited.add(cid)
    if cve_lines:
        out.append("\n## Security / CVE exposure\n")
        out.append("Moving these components changes their CVE exposure (osv.dev, per shipped "
                   "version) — compare the from/to rows in each matrix:")
        out.extend(cve_lines)
        if "CONCEPT-CVE_REMEDIATION" in docs:
            out.append("- Consolidated *am I exposed / what to upgrade* runbook  "
                       "`[CONCEPT-CVE_REMEDIATION]`.")
            cited.add("CONCEPT-CVE_REMEDIATION")

    # --- Kubernetes layer changes for newly-entered minors ---
    _, mf = parse_release_table(docs, frm)
    _, mt = parse_release_table(docs, to)
    new_minors = sorted(mt - mf)
    if new_minors:
        out.append("\n## Kubernetes layer changes (new minors: " +
                   ", ".join(new_minors) + ")\n")
        out.append("Minors that enter the support window on this path — read their "
                   "operator-relevant changes:")
        for mnr in new_minors:
            cid = "CONCEPT-K8S_" + mnr.replace(".", "_") + "_CHANGES"
            if cid in docs:
                out.append(f"- **Kubernetes {mnr}** — {docs[cid]['title']}  `[{cid}]`")
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
        out.append("\n## Component deep-dive — breaking changes for your components\n")
        out.append("Your inventory uses these components; read their per-version breaking-change "
                   "docs (deep upstream-mined notes at the exact versions Kubespray ships, beyond "
                   "the release-delta table above):")
        out.extend(comp_lines)

    # --- Kubernetes behavior changes on this path (silent + urgent) ---
    kb_lines = []
    for cid, desc in K8S_BEHAVIOR:
        if cid in docs:
            kb_lines.append(f"- **{docs[cid]['title']}** — {desc}  `[{cid}]`")
            cited.add(cid)
    if kb_lines:
        out.append("\n## Kubernetes behavior changes on this path\n")
        out.append("Crossing Kubernetes minors changes behavior two ways — actions you MUST take, "
                   "and defaults that shift silently:")
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
            out.append("\n## Cloud provider (external cloud-controller-manager)\n")
            out.append("Your cluster uses a cloud provider — the in-tree providers were removed "
                       "across K8s 1.29–1.31, so confirm the external CCM + CSI are in place:")
            out.extend(ccm_lines)

    out.append("\n## Cross-cutting (Kubernetes layer & upgrade mechanics)\n")
    for cid, desc in [
        ("CONCEPT-K8S_API_REMOVALS", "API removals crossing K8s minors"),
        ("CONCEPT-K8S_FEATURE_GATES", "feature-gate graduations/removals"),
        ("CONCEPT-COMPONENT_VERSION_SELECTION", "which component versions move, and why"),
        ("CONCEPT-UPGRADE_HORIZON", "how far the shipped versions are behind latest upstream"),
        ("CONCEPT-KUBESPRAY_KUBEADM_SEAM", "who does the upgrade (kubeadm) vs Kubespray"),
        ("TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK", "if the control plane won't come up mid-upgrade"),
        ("TROUBLE-KUBEADM_VERSION_SKEW", "one-minor-at-a-time skew rule"),
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
