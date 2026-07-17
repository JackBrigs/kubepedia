---
id: CONCEPT-UPGRADE_HORIZON
type: concept
title: "Upgrade horizon — latest upstream versions vs the base (future context)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - upgrade horizon
  - latest upstream versions
  - version gap
  - how far behind
  - latest component versions
tags:
  - upgrade
  - versions
  - future-context
  - components
  - addons
sources:
  - type: other
    path: git ls-remote --tags (upstream repos)
    note: "latest stable tags observed live 2026-07-17 via git protocol (avoids GitHub API rate limits)"
relations:
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: CONCEPT-COMPONENT_VERSION_SELECTION
---

# Upgrade horizon — latest upstream versions vs the base (future context)

## Summary

This is the **future-context upgrade layer**: for every tracked component and addon it
records **what the base covers** (the version Kubespray `v2.31.0` ships, or the addon version
the owner deploys) versus the **latest stable upstream release** as of **2026-07-17**. This is
`future context` — the latest versions are **NOT** what Kubespray installs and are **NOT** the
deployed addon versions; they are the **upgrade target / distance-to-latest** for planning.
Version-accuracy rule: the per-component/addon docs keep their *actual* versions; this tracker
never overwrites them.

## Context

- **Why a tracker, not per-doc edits:** the base is version-aware and bound to what Kubespray
  actually ships ([[CONCEPT-KUBERNETES_VERSION_SUPPORT]]). Bumping a `COMPONENT-*` doc to an
  unshipped upstream version would misrepresent reality, so the "latest" horizon lives here.
- **Source:** `git ls-remote --tags` on each upstream repo, latest stable semver (pre-release
  tags excluded), 2026-07-17. Kubespray itself is at its ceiling — **`v2.31.0` is the newest
  release** (2026-04-25); there is no newer Kubespray to extend to.
- **⚠ = a major-version jump** (highest upgrade risk — API/CRD/behaviour breaks likely).

## Implementation

### Kubespray-managed components (shipped by v2.31.0 → latest upstream)

| Component | In base (v2.31.0) | Latest upstream (2026-07-17) | Note |
|-----------|-------------------|------------------------------|------|
| etcd | 3.6.x (≤3.6.10) | **3.7.0** | minor jump; test defrag/downgrade path |
| containerd | 2.2.3 | **2.3.3** | CRI config `imports` care |
| runc | 1.4.2 | **1.5.1** | closes the 2025 escape CVE set |
| CRI-O | ≤1.35.0 | **1.36.2** | track K8s minor |
| crun | 1.17 | **1.27.1** | |
| youki | ≤0.5.7 | **0.6.0** | |
| cri-dockerd | ≤0.3.24 | **0.4.6** | |
| nerdctl | ≤2.2.2 | **2.3.4** | |
| skopeo | 1.16.1 | **1.23.0** | |
| cni-plugins | ≤1.9.1 | **1.9.1** | at latest |
| cilium | ≤1.19.3 | **1.19.6** | patch; closes several CVEs |
| coredns | ≤1.12.4 | **1.14.6** | |
| metallb | 0.13.9 | **0.16.1** | CRD/config changes across 0.14–0.16 |
| metrics-server | ≤0.8.1 | **0.9.0** | |
| cert-manager (KS) | 1.15.3 | **1.21.0** ⚠ | many minors; API/CRD care |
| ingress-nginx (KS) | 1.13.3 | **1.15.1** | annotation-validation defaults |
| argocd (KS) | 2.14.x | **3.4.5** ⚠ | 2.x→3.x RBAC/tracking breaks |
| helm | 3.18.4 | **4.2.3** ⚠ | **Helm 3→4 major** |
| kata-containers | 3.7.0 | **3.32.0** | large jump |
| kube-vip | ≤1.0.3 | **1.2.1** | |
| local-path-provisioner | 0.0.32 | **0.0.36** | |
| node-feature-discovery | 0.16.4 | **0.19.0** | |
| registry (distribution) | 2.8.1 | **3.1.1** ⚠ | **registry v2→v3 major** |
| snapshot-controller | 7.0.2 | **8.6.0** ⚠ | v7→v8 major |
| scheduler-plugins | (tracks K8s) | **0.34.7** | pin to K8s minor |
| aws-ebs-csi | 0.5.0 | **1.62.0** ⚠ | very old pin |
| gcp-pd-csi | 1.9.2 | **1.26.4** | |
| docker | 28.3 | (28.x line) | engine |

### Addons (deployed → latest upstream)

| Addon | Deployed | Latest upstream (2026-07-17) | Note |
|-------|----------|------------------------------|------|
| vault | 1.21.2 | **1.23.0** | closes CVE-2026-1229 |
| vault-secrets-webhook | 1.21.4 | **1.23.1** | |
| dex | 2.42.0 | **2.45.1** | |
| argocd (addon) | 3.1.7 | **3.4.5** | closes CVE-2025-55191 |
| cert-manager (addon) | 1.18.2 | **1.21.0** | 1.18 EOL; closes DoS CVE |
| flagger | 1.40.0 | **1.44.0** | |
| vm-k8s-stack | 1.115.0 | **1.147.0** | closes Snappy DoS CVE |
| alertmanager | 0.25.0 | **0.33.1** ⚠ | closes stored-XSS; big gap |
| vector-operator | 0.3.3 | **0.4.1** | |
| otel-operator | 0.156.0 | **0.156.0** | at latest |
| pyrra | 0.9.4 | **0.10.1** | |
| headlamp | 0.43.0 | **0.43.0** | at latest |
| kubernetes-dashboard | 7.6.1 (chart) | v7 line (repo archived) | migrate → headlamp |
| rook-ceph | 1.18.9 | **1.20.2** | K8s min rises |
| ceph-csi | 3.14.2 | **3.17.0** | |
| lvm-localpv | 1.7.0 | **1.9.1** | |
| volsync | 0.15.0 | **0.16.0** | |
| k8up | 2.12.0 | **2.15.0** | |
| zalando-postgres-operator | 1.14.0 | **1.15.1** | |
| velero | 1.17.1 | **1.18.2** | |
| envoy-gateway | 1.6.0 | **1.8.2** | closes RCE CVE-2026-22771 |
| envoy-xds-controller | 0.17.1 | **0.17.1** | at latest |
| capsule | 0.13.3 | **0.13.9** | closes CVE-2026-55636 |
| gpu-operator | 25.10.1 | **26.3.3** ⚠ | calver major; min K8s rises |
| keda | 2.17.2 | **2.20.1** | closes CVE-2025-68476 |
| eck-operator | 3.1.0 | **3.4.1** | |
| olm | 0.32.0 | **0.45.0** | |
| rabbitmq-cluster-operator | 2.19.2 | **2.22.2** | broker → 4.x |
| dragonfly-operator | (op) 1.1.11 / (db) 1.28.1 | **1.6.1 / 1.39.0** | db closes 3 CVEs |
| awx-operator | 2.19.1 | **2.19.1** | at latest |
| feast | 0.64.0 | **0.64.0** | at latest |
| gigapipe/qryn | 4.1.6 | **4.3.1** | |
| karma | 0.121 | **0.131** | |
| spegel | 0.0.1 | **0.7.4** ⚠ | huge gap; needs containerd 2.1+ |
| kubernetes-mcp-server | 0.0.56 | **0.0.65** | |
| open-webui | 0.9.5 | **0.10.2** | closes CVE-2026-54017 |
| tbot / teleport | 18.7.x | **18.10.0** | no major skips |
| snapshotter (addon) | 6.3.0 | **8.6.0** ⚠ | v6→v8 major |

## Compatibility

- **Major jumps (⚠) need dedicated upgrade care** — Helm 3→4, registry v2→v3, snapshot
  controller v7→v8, argocd 2→3, cert-manager's many minors, gpu-operator calver, aws-ebs-csi
  0.5→1.62. Treat each as its own change with a migration/rollback plan; do not batch.
- **Upgrading to latest also closes documented CVEs** — most security findings in the CVE
  matrices and addon docs (runc escape set, argocd CVE-2025-55191, envoy-gateway RCE
  CVE-2026-22771, keda CVE-2025-68476, capsule CVE-2026-55636, vault CVE-2026-1229,
  open-webui CVE-2026-54017, alertmanager XSS) are fixed at the latest listed versions.
- **Kubespray-managed components can't simply be bumped** — their version is set by the
  Kubespray tag; jumping ahead of Kubespray means overriding the pin (unsupported) or waiting
  for a Kubespray release that ships it. The addon versions, by contrast, are the owner's to
  bump directly.

## References

- `git ls-remote --tags` per upstream repo (2026-07-17). Base version window:
  [[CONCEPT-KUBERNETES_VERSION_SUPPORT]]; addon inventory: [[CONCEPT-ADDON_CATALOG]];
  Kubespray selection mechanism: [[CONCEPT-COMPONENT_VERSION_SELECTION]].
