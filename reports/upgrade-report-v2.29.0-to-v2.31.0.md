# Upgrade & Change Report — Kubespray v2.29.0 → v2.31.0

_Generated from Kubepedia KDS docs. 3 upgrade step(s) on the path._


## Step: v2.29.0 → v2.29.1

A **patch** upgrade: same Kubernetes minor window (1.31–1.33), refreshed patch
and component versions. **Security-motivated:** it fixes the runc container-escape
CVEs present in v2.29.0.

**Version deltas**

Version deltas:

| Item | v2.29.0 | v2.29.1 |
|------|---------|---------|
| Kubernetes default / min | 1.33.5 / 1.31.0 | 1.33.7 / 1.31.0 |
| etcd | 3.5.23 | 3.5.25 |
| containerd | 2.1.4 | 2.1.5 |
| runc | 1.3.2 | **1.3.4** |
| Cilium | 1.18.2 | 1.18.4 |
| CoreDNS (default) | 1.12.0 | 1.12.0 |

**Required actions / breaking changes**

- **Security:** runc `1.3.2 → 1.3.4` fixes **CVE-2025-31133** and the coordinated
  runc container-escape CVEs (see [[TROUBLE-RUNC_CONTAINER_ESCAPE_NOV2025]]). This
  alone is a strong reason to move off v2.29.0.
- **No API removals** — same Kubernetes minor window; no breaking API changes.
- No default/behavior changes of note beyond version bumps.
- Standard graceful upgrade ([[UPGRADE-KUBESPRAY_SEQUENTIAL]]); patch upgrades are
  low-risk.

**Compatibility constraints**

- Kubernetes stays on 1.31–1.33 (patch ranges extended, default 1.33.5 → 1.33.7).


## Step: v2.29.1 → v2.30.0

A **minor** upgrade that shifts the Kubernetes support window: `1.31` is dropped,
`1.34` is added. The most important operator action is the Kubernetes `1.32` API
removal that this transition crosses.

**Version deltas**

Version deltas:

| Item | v2.29.1 | v2.30.0 |
|------|---------|---------|
| Kubernetes default / min | 1.33.7 / 1.31.0 | 1.34.3 / **1.32.0** |
| Supported minors | 1.31, 1.32, 1.33 | **1.32, 1.33, 1.34** |
| etcd | 3.5.25 | 3.5.26 |
| containerd | 2.1.5 | 2.2.1 |
| runc | 1.3.4 | 1.3.4 |
| Cilium | 1.18.4 | 1.18.6 |
| CoreDNS (default) | 1.12.0 | 1.12.1 |
| kube-vip (deployed) | v0.8.9 | **v1.0.3** |
| nerdctl | 2.1.6 | 2.2.1 |

**Required actions / breaking changes**

- **BREAKING — API removal:** crossing to Kubernetes `1.32` removes
  `flowcontrol.apiserver.k8s.io/v1beta3` (FlowSchema, PriorityLevelConfiguration)
  — migrate any such manifests to `/v1` **before** upgrading. See
  [[CONCEPT-K8S_API_REMOVALS]] / [[API-FLOWCONTROL_APISERVER]].
- **Feature gates:** the `1.32` release removes a large batch of long-GA gates;
  drop any of them from explicit `--feature-gates` (see
  [[CONCEPT-K8S_FEATURE_GATES]]).
- **Do not skip minors** — this must be a one-step Kubespray minor upgrade.
- kube-vip image tag now derives from `kube_vip_version` (`1.0.3`), fixing the
  earlier literal-tag mismatch.
- Standard graceful upgrade; snapshot etcd first ([[PRACTICE-UPGRADE_PREFLIGHT]]).

**Compatibility constraints**

- Clusters still on Kubernetes `1.31` must first move to `1.32`+; `1.31` is
  unsupported in v2.30.0.


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


## Cross-cutting (Kubernetes layer)

- **Kubernetes API removals across 1.31–1.35** — API removals crossing K8s minors  `[CONCEPT-K8S_API_REMOVALS]`
- **Kubernetes feature gates — graduations and removals across 1.31–1.35** — feature-gate graduations/removals  `[CONCEPT-K8S_FEATURE_GATES]`
- **Component version-selection matrix (how each version is chosen)** — which component versions move, and why  `[CONCEPT-COMPONENT_VERSION_SELECTION]`
- **Pre-upgrade checklist (Kubespray)** — pre-upgrade checklist  `[PRACTICE-UPGRADE_PREFLIGHT]`
- **Graceful upgrade mechanics (drain, serial, pause)** — drain/serial/pause mechanics  `[PRACTICE-GRACEFUL_UPGRADE]`

## Sources (KDS documents)

- `API-FLOWCONTROL_APISERVER` — flowcontrol.apiserver.k8s.io (FlowSchema, PriorityLevelConfiguration)  (kb/kubernetes/api-flowcontrol.md)
- `COMPONENT-ETCD` — etcd  (kb/components/etcd/etcd.md)
- `COMPONENT-INGRESS_NGINX` — ingress-nginx (managed in v2.29.0–v2.30.0, removed in v2.31.0)  (kb/components/ingress-nginx/ingress-nginx.md)
- `CONCEPT-COMPONENT_VERSION_SELECTION` — Component version-selection matrix (how each version is chosen)  (kb/components/component-version-selection.md)
- `CONCEPT-K8S_API_REMOVALS` — Kubernetes API removals across 1.31–1.35  (kb/kubernetes/api-removals.md)
- `CONCEPT-K8S_FEATURE_GATES` — Kubernetes feature gates — graduations and removals across 1.31–1.35  (kb/kubernetes/feature-gates.md)
- `CONFIG-KUBEADM_CONFIG_API_VERSION` — kubeadm ClusterConfiguration API version generated by Kubespray  (kb/kubernetes/kubeadm-config-api-version.md)
- `PRACTICE-GRACEFUL_UPGRADE` — Graceful upgrade mechanics (drain, serial, pause)  (kb/kubespray/guides/graceful-upgrade.md)
- `PRACTICE-UPGRADE_PREFLIGHT` — Pre-upgrade checklist (Kubespray)  (kb/kubespray/guides/upgrade-preflight.md)
- `RELEASE-V2_29_0` — Kubespray v2.29.0  (kb/kubespray/releases/v2.29.0.md)
- `RELEASE-V2_29_1` — Kubespray v2.29.1  (kb/kubespray/releases/v2.29.1.md)
- `RELEASE-V2_30_0` — Kubespray v2.30.0  (kb/kubespray/releases/v2.30.0.md)
- `RELEASE-V2_31_0` — Kubespray v2.31.0  (kb/kubespray/releases/v2.31.0.md)
- `TROUBLE-CILIUM_KNOWN_CVES` — cilium: known CVEs by shipped version (osv.dev)  (kb/troubleshooting/cilium-known-cves.md)
- `TROUBLE-CNI_PLUGINS_KNOWN_CVES` — cni-plugins: known CVEs by shipped version (osv.dev)  (kb/troubleshooting/cni-plugins-known-cves.md)
- `TROUBLE-RUNC_CONTAINER_ESCAPE_NOV2025` — runc container escape (CVE-2025-31133 et al.) affects Kubespray v2.29.0  (kb/troubleshooting/runc-container-escape-nov2025.md)
- `TROUBLE-RUNC_KNOWN_CVES` — runc: known CVEs by shipped version (osv.dev)  (kb/troubleshooting/runc-known-cves.md)
- `UPGRADE-KUBESPRAY_SEQUENTIAL` — Sequential Kubespray/Kubernetes upgrade procedure  (kb/kubespray/operations/upgrade-sequential.md)
- `UPGRADE-V2_29_0__V2_29_1` — Upgrade report v2.29.0 → v2.29.1  (kb/kubespray/releases/upgrade-v2.29.0-to-v2.29.1.md)
- `UPGRADE-V2_29_1__V2_30_0` — Upgrade report v2.29.1 → v2.30.0  (kb/kubespray/releases/upgrade-v2.29.1-to-v2.30.0.md)
- `UPGRADE-V2_30_0__V2_31_0` — Upgrade report v2.30.0 → v2.31.0  (kb/kubespray/releases/upgrade-v2.30.0-to-v2.31.0.md)
