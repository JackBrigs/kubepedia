---
id: UPGRADE-CILIUM_1_15_TO_1_19
type: upgrade
title: "Cilium upgrade 1.15 → 1.19 across Kubespray v2.27.0–v2.31.0 (breaking changes)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.15.9 <=1.19.3"
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - cilium upgrade breaking changes
  - cilium 1.15 to 1.19
  - cilium version jump kubespray
  - kube-proxy replacement toggles removed cilium
  - cilium clustermesh policy default local cluster
  - cilium kernel requirement 5.10
tags:
  - cilium
  - cni
  - upgrade
  - breaking-changes
sources:
  - type: docs
    path: Documentation/operations/upgrade.rst
    url: https://github.com/cilium/cilium/blob/v1.19.3/Documentation/operations/upgrade.rst
    note: "per-version breaking-change notes read at tags v1.16.19, v1.17.3, v1.18.2, v1.19.3"
  - type: code
    path: install/kubernetes/cilium/values.yaml
    url: https://github.com/cilium/cilium/blob/v1.19.3/install/kubernetes/cilium/values.yaml
    note: "Helm default changes and cilium-envoy image tags per tag"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
  - type: depends_on
    target: UPGRADE-KUBESPRAY_SEQUENTIAL
  - type: see_also
    target: PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR
  - type: see_also
    target: PRACTICE-KERNEL_REQUIREMENTS
  - type: see_also
    target: TROUBLE-CILIUM_KNOWN_CVES
  - type: see_also
    target: CONCEPT-CILIUM_LOADBALANCING
---

# Cilium upgrade 1.15 → 1.19 across Kubespray v2.27.0–v2.31.0 (breaking changes)

## Summary

Kubespray moves Cilium through **large** version jumps as you upgrade minors:
`1.15.9` (v2.27.0) → `1.17.3` (v2.28.0) → `1.18.2` (v2.29.0) → `1.18.6` (v2.30.0) → `1.19.3` (v2.31.0)
([[COMPONENT-CILIUM]]). Each jump carries breaking defaults, removed flags, and CRD migrations that
Kubespray does **not** handle for you — this doc is the per-jump checklist. **The single most
important warning:** Kubespray **v2.27.0 → v2.28.0** takes Cilium **1.15.9 → 1.17.3**, skipping
**1.16**, but Cilium only tests/supports **consecutive-minor** upgrades — so that jump is outside
Cilium's own upgrade guidance and the 1.16 notes below are **required reading**, not optional.

## Implementation

- Kubespray installs Cilium via the `network_plugin/cilium` role at the pinned `cilium_version` for
  the tag; upgrading is part of the normal cluster/upgrade run ([[PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR]]).
  It does **not** run Cilium's pre-flight/CRD migrations — you apply the per-jump actions below via
  Helm values / inventory before or during the upgrade.
- **Version → Kubespray tag map:**

  | Kubespray | Cilium | Notable |
  |-----------|--------|---------|
  | v2.27.0 | 1.15.9 | baseline |
  | v2.28.0 | 1.17.3 | **skips 1.16** (see warning) |
  | v2.29.0 | 1.18.2 | kernel ≥5.10 required |
  | v2.30.0 | 1.18.6 | patch (cilium-envoy bump only) |
  | v2.31.0 | 1.19.3 | ClusterMesh policy/auth default flips |

- Use `upgradeCompatibility` (Helm) set to your **current** minor to hold old defaults across a jump,
  then remove it once migrated — this is the safety lever for most default changes below.

## Upgrade Notes

### Jump 1.15.9 → 1.17.3 (v2.27.0 → v2.28.0) — crosses 1.16 + 1.17

**1.16 (`upgrade.rst`@v1.16.19):**
- **Envoy DaemonSet on by default** — one extra pod/node; a non-critical pod may be evicted on
  at-capacity nodes. Hold with `upgradeCompatibility=1.15`.
- **tcx BPF links** default on kernel ≥6.6 (`bpf.enableTCX=false` to opt out).
- **`toFQDNs` overhaul** — must run **≥1.15.6 before upgrading** or hit temporary drops.
- **KVStoreMesh on by default** in ClusterMesh; **LB-IPAM `allowFirstLastIPs` default → yes**;
  `CiliumLoadBalancerIPPool.spec.cidrs` **removed** → use `.blocks` ([[CONCEPT-CILIUM_LOADBALANCING]]).
- **Policy semantics:** empty non-nil `fromEndpoints/fromCIDR/...` now selects nothing (default-deny);
  `cidrGroupRef` to only-nonexistent groups flips allow-all → **deny-all**.
- **IPsec per-tunnel keys mandatory** ([[CONCEPT-CILIUM_ENCRYPTION]]).
- **Flags removed:** `enable-remote-node-identity`, `endpoint-status`, `ip-allocation-timeout`,
  `sidecar-istio-proxy-image`, `install-egress-gateway-routes`. **Helm removed:** `encryption.{keyFile,
  mountPath,secretName,interface}` → `encryption.ipsec.*`; `proxy.prometheus.*` → `envoy.prometheus.*`;
  `remoteNodeIdentity`, `endpointStatus`, `etcd.managed`, `containerRuntime.integration`.

**1.17 (`upgrade.rst`@v1.17.3):**
- **Removed:** Consul support; Cilium-managed **etcd in pod network**; `metallb-bgp` (use Cilium BGP
  control plane — Helm `bgp.*` removed); L7 `policy.cilium.io/proxy-visibility` annotation; IPsec
  single-key.
- **Service protocol differentiation on by default** (`--bpf-lb-proto-diff`) — downgrade recreates
  protocol-set services (disruption).
- **MTU auto-detect** now uses the **lowest** MTU of all external interfaces.
- **TLS visibility/SDS:** `tls.secretsBackend` deprecated → `tls.readSecretsOnlyFromSecretsNamespace`
  (+ `tls.secretSync`); new clusters enable SDS, upgraded (`upgradeCompatibility=v1.16`) do not.
- **Helm default:** `hubble.tls.auto.certValidityDuration` 1095 → **365** days.

### Jump 1.17.3 → 1.18.2 (v2.28.0 → v2.29.0)

`upgrade.rst`@v1.18.2:
- **Kernel ≥ v5.10 now REQUIRED** — verify node kernels before v2.29.0 ([[PRACTICE-KERNEL_REQUIREMENTS]]).
- **ENI `enableIPv4Masquerade` default flips `true` → `false`** — set explicitly or
  `upgradeCompatibility<1.18`.
- **`serviceaccount` identity label** added to default identity-relevant set → transient identity
  growth / drops during upgrade (exclude with `!io\.cilium\.k8s\.policy\.serviceaccount`).
- **BGP CRDs `v2alpha1` → `v2`** (`CiliumBGPClusterConfig`, `...PeerConfig`, `...Advertisement`,
  `...NodeConfig[Override]`); `CiliumCIDRGroup` `v2alpha1`→`v2`.
- **KPR toggles deprecated** (removed in 1.19): `--enable-node-port/-host-port/-external-ips`,
  `--enable-session-affinity`, `--enable-internal-traffic-policy`, `--enable-svc-source-range-check`,
  `--enable-k8s-endpoint-slice` — features become unconditional or gated on `--kube-proxy-replacement=true`.
- **Flags renamed:** `k8s-api-server` → `k8s-api-server-urls`; `kvstore-connectivity-timeout` →
  `identity-allocation-timeout`. **L2 neigh discovery default → false.** **Operator tolerations
  narrowed** — operator no longer runs on drained nodes. Removed: External Workloads,
  `--datapath-mode=lb-only`, ipcache high-scale, all `ces-*` rate-limit flags.
- **Forward notice:** new `policy-default-local-cluster` flag (default keeps all-cluster in 1.18) —
  **becomes default in 1.19**; review before the v2.31.0 jump.

### Jump 1.18.2 → 1.18.6 (v2.29.0 → v2.30.0) — patch only

`upgrade.rst` **unchanged** between tags — no operator-facing breaking changes.
- **cilium-envoy image `v1.34.7-…` → `v1.35.9-…`** (`install/kubernetes/cilium/values.yaml`@v1.18.6) —
  Envoy security/patch uptake; check Envoy advisories for that window.
- certgen `v0.2.4`→`v0.3.1` and other digest bumps; `kubeProxyReplacement` line uncommented (still
  default `false`).

### Jump 1.18.6 → 1.19.3 (v2.30.0 → v2.31.0)

`upgrade.rst`@v1.19.3:
- **ClusterMesh `policy-default-local-cluster` now ON by default (BIGGEST)** — network-policy selectors
  now match **local-cluster endpoints only** (was all clusters). Can break cross-cluster connectivity;
  set `=false` or update policies first. (This is the 1.18 forward-notice landing.)
- **`mesh-auth-enabled` now OFF by default** (Helm `authentication.enabled`) — re-enable if policies
  use mutual auth, else traffic forwarded unauthenticated.
- **KPR toggles REMOVED** (the 1.18 deprecations) — any inventory setting `--enable-node-port` etc.
  **breaks**; features are unconditional or gated on `--kube-proxy-replacement=true`.
- **BGPv1 fully removed** — `CiliumBGPPeeringPolicy` CRD gone; must be on `cilium.io/v2` BGP CRDs.
  `CiliumLoadBalancerIPPool` `v2alpha1` deprecated → `v2`.
- **Policy CRDs:** `FromRequires`/`ToRequires` must be empty; DNS `**` wildcard now does true extended
  subdomain matching — audit allow-lists.
- **CVE-2025-37959 (kernel):** with **IPsec + KPR + BPF masquerading**, eBPF **Host Routing
  auto-enables**, which requires a kernel bugfix — patch the kernel or set
  `--enable-host-legacy-routing=true` ([[TROUBLE-CILIUM_KNOWN_CVES]], [[CONCEPT-CILIUM_ENCRYPTION]]).
- **ClusterMesh TLS `authMode` default → `migration`**; MCS-API CRDs installed by default.
- `--unmanaged-pod-watcher-interval` type int→duration (use `15s`); `bpf.tproxy=true` incompatible with
  **netkit** (agent fails to start).

## Compatibility

- **Two-minor jump is unsupported by Cilium:** v2.27.0→v2.28.0 (1.15.9→1.17.3) skips 1.16; Cilium
  "only tests the path between consecutive minor releases" (`upgrade.rst`@v1.17.3). Treat the 1.16
  notes as mandatory; consider staging via an intermediate 1.16.x if the cluster is complex.
- **Rising kernel floor:** kernel-conditional tcx (≥6.6) / netkit (≥6.8) in 1.16, then a **hard ≥5.10**
  requirement in 1.18 — validate node kernels before v2.29.0 ([[PRACTICE-KERNEL_REQUIREMENTS]]).
- **KPR consolidation** is the biggest silent breaker: piecemeal toggles deprecated in 1.18, **removed
  in 1.19**. Migrate any Kubespray inventory that sets them individually to `kube_proxy_replacement`
  before v2.31.0.
- **ClusterMesh** users face three separate default flips (KVStoreMesh on @1.16, local-cluster policy
  @1.19, mesh-auth off @1.19) — audit multi-cluster policy/connectivity across the range.
- **BGP** users must complete the `v2alpha1`→`v2` CRD migration before v2.31.0 (BGPv1 removed @1.19).

## References

- Cilium `Documentation/operations/upgrade.rst` read at tags **v1.16.19, v1.17.3, v1.18.2, v1.19.3**;
  `install/kubernetes/cilium/values.yaml`@v1.18.6 (envoy/image bumps). Component: [[COMPONENT-CILIUM]];
  sequencing [[UPGRADE-KUBESPRAY_SEQUENTIAL]]; upgrade runbook [[PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR]];
  CVEs [[TROUBLE-CILIUM_KNOWN_CVES]]; kernel [[PRACTICE-KERNEL_REQUIREMENTS]].
