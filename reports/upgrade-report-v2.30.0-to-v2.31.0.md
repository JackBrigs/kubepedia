# Upgrade & Change Report — Kubespray v2.30.0 → v2.31.0

_Generated from Kubepedia KDS docs. 1 upgrade step(s) on the path._

_Verbatim excerpts from the KB docs are in English (the KB's knowledge language); source links are at the end._


## Step: v2.30.0 → v2.31.0

A **minor** upgrade: Kubernetes window shifts (`1.32` dropped, `1.35` added).
Notable: **etcd 3.6** is introduced for Kubernetes `1.35`, the
`kubeadm_config_api_version` variable is removed, and several component CVEs are
fixed by the version bumps.

**Version deltas**

Version deltas:

| Item | v2.30.0 | v2.31.0 |
|------|---------|---------|
| Kubernetes default / min | 1.34.3 / 1.32.0 | 1.35.4 / **1.33.0** |
| Supported minors | 1.32, 1.33, 1.34 | **1.33, 1.34, 1.35** |
| etcd | 3.5.26 | 3.5.29 (1.33/1.34) / **3.6.10 (1.35)** |
| containerd | 2.2.1 | 2.2.3 |
| runc | 1.3.4 | **1.4.2** |
| Cilium | 1.18.6 | **1.19.3** |
| CoreDNS (default) | 1.12.1 | 1.12.4 |
| cni-plugins | 1.8.0 | **1.9.1** |
| nerdctl | 2.2.1 | 2.2.2 |

**Required actions / breaking changes**

- **etcd 3.6** first appears (gated to Kubernetes `1.35` via the `<3.7` ceiling;
  older minors stay on `3.5.x`). Review etcd 3.6 operational changes if you run
  `1.35`. See [[COMPONENT-ETCD]].
- **kubeadm config:** the `kubeadm_config_api_version` variable and the `v1beta3`
  fallback are **removed**; the template is pinned to `v1beta4`
  ([[CONFIG-KUBEADM_CONFIG_API_VERSION]]). Remove any override of that variable.
- **Security fixes via bumps:** cni-plugins `1.8.0 → 1.9.1` fixes
  **CVE-2025-67499**; Cilium `1.18.6 → 1.19.3` clears most Cilium CVEs; runc
  `1.3.4 → 1.4.2`. (Some CVEs remain even at these versions — see the per-component
  security docs.)
- **Feature gates / no API removals** documented for `1.33`–`1.35` (see
  [[CONCEPT-K8S_API_REMOVALS]], [[CONCEPT-K8S_FEATURE_GATES]]).
- **Managed add-ons removed:** Kubespray no longer manages **ingress-nginx**
  (`ingress_nginx_enabled` gone; only the ALB controller remains —
  [[COMPONENT-INGRESS_NGINX]]), the **Kubernetes Dashboard** (`dashboard_enabled`), or
  **netcheck** in `v2.31.0`. If you relied on any of them, take over their lifecycle
  yourself before upgrading (see [[CONCEPT-COMPONENT_VERSION_SELECTION]]).
- The legacy `master` run-tag is gone (fully renamed to `control-plane`).
- One minor at a time; snapshot etcd first ([[PRACTICE-UPGRADE_PREFLIGHT]]).

**Compatibility constraints**

- Clusters on Kubernetes `1.32` must move to `1.33`+; `1.32` is unsupported in
  v2.31.0.


## Component version changes (v2.30.0 → v2.31.0)

| Component | v2.30.0 | v2.31.0 |
|---|---|---|
| Kubernetes (default / min) | **1.34.3** / **1.32.0** | **1.35.4** / **1.33.0** |
| etcd | **3.5.26** | **3.5.29** (1.33/1.34) / **3.6.10** (1.35) |
| containerd | **2.2.1** | **2.2.3** |
| runc | 1.3.4 | **1.4.2** |
| cni-plugins | 1.8.0 | **1.9.1** |
| Cilium | **1.18.6** | **1.19.3** |
| CoreDNS (default) | **1.12.1** | **1.12.4** |
| nerdctl | 2.2.1 | **2.2.2** |
| kube-vip (deployed) | **v1.0.3** | v1.0.3 |

## Security / CVE exposure

CVE exposure per shipped version (osv.dev; counts are distinct advisories):
- **Kubernetes (default / min)** `1.34.3` (2 CVEs) → `1.35.4` (**2 CVEs**)  `[TROUBLE-KUBERNETES_KNOWN_CVES]`
    - **still exposed after the upgrade**: CVE-2024-7598, CVE-2025-1767
- **containerd** `2.2.1` (6 CVEs) → `2.2.3` (**6 CVEs**)  `[TROUBLE-CONTAINERD_KNOWN_CVES]`
    - **still exposed after the upgrade**: CVE-2026-46680, CVE-2026-47262, CVE-2026-50195, CVE-2026-53488, CVE-2026-53489, CVE-2026-53492
- **runc** `1.3.4` (1 CVE) → `1.4.2` (**1 CVE**)  `[TROUBLE-RUNC_KNOWN_CVES]`
    - **still exposed after the upgrade**: CVE-2026-41579
- **cni-plugins** `1.8.0` (1 CVE) → `1.9.1` (**0 CVEs**)  `[TROUBLE-CNI_PLUGINS_KNOWN_CVES]`
    - cleared: CVE-2025-67499
    - no CVEs recorded at the target version
- **Cilium** `1.18.6` (4 CVEs) → `1.19.3` (**1 CVE**)  `[TROUBLE-CILIUM_KNOWN_CVES]`
    - cleared: CVE-2026-33726, CVE-2026-41520, CVE-2026-49445
    - **still exposed after the upgrade**: CVE-2026-53935
- **CoreDNS (default)** `1.12.1` (10 CVEs) → `1.12.4` (**8 CVEs**)  `[TROUBLE-COREDNS_KNOWN_CVES]`
    - cleared: CVE-2025-47950, CVE-2025-58063
    - **still exposed after the upgrade**: CVE-2025-68151, CVE-2026-26017, CVE-2026-26018, CVE-2026-32934, CVE-2026-32936, CVE-2026-33190, CVE-2026-33489, CVE-2026-35579
- Consolidated *am I exposed / what to upgrade* runbook  `[CONCEPT-CVE_REMEDIATION]`.

## Kubernetes layer changes (new minors: 1.35)

Minors that enter the support window on this path — read their operator-relevant changes:
- **Kubernetes 1.35** — Kubernetes 1.35 — operator-relevant changes  `[CONCEPT-K8S_1_35_CHANGES]`

## Component deep-dive — breaking changes for your components

Your inventory uses these components; read their per-version breaking-change docs (deep upstream-mined notes at the exact versions Kubespray ships, beyond the release-delta table above):
- **Cilium upgrade 1.15 → 1.19 across Kubespray v2.27.0–v2.31.0 (breaking changes)**  `[UPGRADE-CILIUM_1_15_TO_1_19]`
- **Argo CD upgrade 2.11 → 2.14 across Kubespray v2.27.0–v2.31.0 (cumulative breaking changes)**  `[UPGRADE-ARGOCD_2_11_TO_2_14]`

## Kubernetes behavior changes on this path

Crossing Kubernetes minors changes behavior two ways — actions you MUST take, and defaults that shift silently:
- **Kubernetes Urgent Upgrade Notes 1.29→1.35 — the 'must read before you upgrade' items** — must-do actions before you upgrade (removed kubelet flags, cgroup-v1 hard error, …)  `[CONCEPT-K8S_URGENT_UPGRADE_NOTES]`
- **Silent behavior changes on Kubernetes upgrade 1.29→1.35 (feature-gate GAs, default flips, deprecations)** — behavior that changes with no config edit (feature-gate GAs, default flips, deprecations)  `[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]`

## Cross-cutting (Kubernetes layer & upgrade mechanics)

- **Kubernetes API removals across 1.29–1.35** — API removals crossing K8s minors  `[CONCEPT-K8S_API_REMOVALS]`
- **Kubernetes feature gates — graduations and removals across 1.29–1.35** — feature-gate graduations/removals  `[CONCEPT-K8S_FEATURE_GATES]`
- **Component version-selection matrix (how each version is chosen)** — which component versions move, and why  `[CONCEPT-COMPONENT_VERSION_SELECTION]`
- **Upgrade horizon — latest upstream versions vs the base (future context)** — how far the shipped versions are behind latest upstream  `[CONCEPT-UPGRADE_HORIZON]`
- **The Kubespray↔kubeadm seam — who does the upgrade, where errors come from** — who does the upgrade (kubeadm) vs Kubespray  `[CONCEPT-KUBESPRAY_KUBEADM_SEAM]`
- **kubeadm upgrade: health-check fails (static control plane won't come up)** — if the control plane won't come up mid-upgrade  `[TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK]`
- **kubeadm version skew: can't skip a minor / kubelet too old** — one-minor-at-a-time skew rule  `[TROUBLE-KUBEADM_VERSION_SKEW]`
- **Pre-upgrade checklist (Kubespray)** — pre-upgrade checklist  `[PRACTICE-UPGRADE_PREFLIGHT]`
- **Graceful upgrade mechanics (drain, serial, pause)** — drain/serial/pause mechanics  `[PRACTICE-GRACEFUL_UPGRADE]`

## Sources (KDS documents)

- `COMPONENT-ETCD` — etcd  (kb/components/etcd/etcd.md)
- `COMPONENT-INGRESS_NGINX` — ingress-nginx (managed in v2.29.0–v2.30.0, removed in v2.31.0)  (kb/components/ingress-nginx/ingress-nginx.md)
- `CONCEPT-COMPONENT_VERSION_SELECTION` — Component version-selection matrix (how each version is chosen)  (kb/components/component-version-selection.md)
- `CONCEPT-CVE_REMEDIATION` — CVE remediation runbook — am I exposed, what to upgrade  (kb/troubleshooting/cve-remediation-runbook.md)
- `CONCEPT-K8S_1_35_CHANGES` — Kubernetes 1.35 — operator-relevant changes  (kb/kubernetes/changes-1.35.md)
- `CONCEPT-K8S_API_REMOVALS` — Kubernetes API removals across 1.29–1.35  (kb/kubernetes/api-removals.md)
- `CONCEPT-K8S_FEATURE_GATES` — Kubernetes feature gates — graduations and removals across 1.29–1.35  (kb/kubernetes/feature-gates.md)
- `CONCEPT-K8S_UPGRADE_SILENT_CHANGES` — Silent behavior changes on Kubernetes upgrade 1.29→1.35 (feature-gate GAs, default flips, deprecations)  (kb/kubernetes/upgrade-silent-changes-1.29-1.35.md)
- `CONCEPT-K8S_URGENT_UPGRADE_NOTES` — Kubernetes Urgent Upgrade Notes 1.29→1.35 — the 'must read before you upgrade' items  (kb/kubernetes/urgent-upgrade-notes-1.29-1.35.md)
- `CONCEPT-KUBESPRAY_KUBEADM_SEAM` — The Kubespray↔kubeadm seam — who does the upgrade, where errors come from  (kb/kubespray/guides/kubespray-kubeadm-seam.md)
- `CONCEPT-UPGRADE_HORIZON` — Upgrade horizon — latest upstream versions vs the base (future context)  (kb/kubernetes/upgrade-horizon.md)
- `CONFIG-KUBEADM_CONFIG_API_VERSION` — kubeadm ClusterConfiguration API version generated by Kubespray  (kb/kubernetes/kubeadm-config-api-version.md)
- `PRACTICE-GRACEFUL_UPGRADE` — Graceful upgrade mechanics (drain, serial, pause)  (kb/kubespray/guides/graceful-upgrade.md)
- `PRACTICE-UPGRADE_PREFLIGHT` — Pre-upgrade checklist (Kubespray)  (kb/kubespray/guides/upgrade-preflight.md)
- `RELEASE-V2_30_0` — Kubespray v2.30.0  (kb/kubespray/releases/v2.30.0.md)
- `RELEASE-V2_31_0` — Kubespray v2.31.0  (kb/kubespray/releases/v2.31.0.md)
- `TROUBLE-CILIUM_KNOWN_CVES` — cilium: known CVEs by shipped version (osv.dev)  (kb/troubleshooting/cilium-known-cves.md)
- `TROUBLE-CNI_PLUGINS_KNOWN_CVES` — cni-plugins: known CVEs by shipped version (osv.dev)  (kb/troubleshooting/cni-plugins-known-cves.md)
- `TROUBLE-CONTAINERD_KNOWN_CVES` — containerd: known CVEs by shipped version (osv.dev)  (kb/troubleshooting/containerd-known-cves.md)
- `TROUBLE-COREDNS_KNOWN_CVES` — coredns: known CVEs by shipped version (osv.dev)  (kb/troubleshooting/coredns-known-cves.md)
- `TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK` — kubeadm upgrade: health-check fails (static control plane won't come up)  (kb/troubleshooting/kubeadm-upgrade-health-check.md)
- `TROUBLE-KUBEADM_VERSION_SKEW` — kubeadm version skew: can't skip a minor / kubelet too old  (kb/troubleshooting/kubeadm-version-skew.md)
- `TROUBLE-KUBERNETES_KNOWN_CVES` — kubernetes: known CVEs by shipped version (osv.dev)  (kb/troubleshooting/kubernetes-known-cves.md)
- `TROUBLE-RUNC_KNOWN_CVES` — runc: known CVEs by shipped version (osv.dev)  (kb/troubleshooting/runc-known-cves.md)
- `UPGRADE-ARGOCD_2_11_TO_2_14` — Argo CD upgrade 2.11 → 2.14 across Kubespray v2.27.0–v2.31.0 (cumulative breaking changes)  (kb/components/argocd/argocd-upgrade-2.11-to-2.14.md)
- `UPGRADE-CILIUM_1_15_TO_1_19` — Cilium upgrade 1.15 → 1.19 across Kubespray v2.27.0–v2.31.0 (breaking changes)  (kb/components/cilium/cilium-upgrade-1.15-to-1.19.md)
- `UPGRADE-V2_30_0__V2_31_0` — Upgrade report v2.30.0 → v2.31.0  (kb/kubespray/releases/upgrade-v2.30.0-to-v2.31.0.md)
