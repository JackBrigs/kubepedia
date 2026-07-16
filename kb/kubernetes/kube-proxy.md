---
id: CONCEPT-KUBE_PROXY
type: concept
title: "kube-proxy in Kubespray (modes, default, and kube-proxy-free)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube-proxy
  - kube_proxy_mode
  - proxy mode ipvs iptables nftables
  - kube-proxy-free
  - kube_proxy_remove
  - disable kube-proxy
tags:
  - kubernetes
  - kube-proxy
  - networking
  - service-proxy
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "34,48-58"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_proxy_mode default ipvs; addon/kube-proxy skip conditions (tag v2.31.0)"
relations:
  - type: see_also
    target: VARIABLE-KUBE_PROXY_MODE
  - type: see_also
    target: CONCEPT-K8S_CONTROL_PLANE_VERSIONS
  - type: see_also
    target: TROUBLE-NFTABLES_KERNEL_TOO_LOW
---

# kube-proxy in Kubespray (modes, default, and kube-proxy-free)

## Summary

kube-proxy implements Kubernetes Service routing on every node. Kubespray deploys it as
the kubeadm **`addon/kube-proxy`** (so its version equals `kube_version` —
[[CONCEPT-K8S_CONTROL_PLANE_VERSIONS]]) and defaults its mode to **`ipvs`** — notably
**different from upstream kube-proxy's own default of `iptables`**. In several
CNI/config scenarios kube-proxy is **not deployed at all** ("kube-proxy-free"), with the
CNI taking over Service routing.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- **Mode** (`kube_proxy_mode`, default **`ipvs`**, unchanged across the range —
  [[VARIABLE-KUBE_PROXY_MODE]]):
  - `ipvs` — Kubespray default; needs the IPVS kernel modules; uses `kube-ipvs0` (which is
    why MetalLB L2 needs `kube_proxy_strict_arp: true`).
  - `iptables` — the classic mode (upstream default).
  - `nftables` — nftables backend; **GA in Kubernetes 1.33**, and Kubespray's preflight
    requires **kernel ≥ 5.13** ([[TROUBLE-NFTABLES_KERNEL_TOO_LOW]]). `ipvs` is deprecated
    upstream from 1.35, so `nftables` is the forward path.

## Implementation

**Deployment:** kube-proxy is the kubeadm addon `addon/kube-proxy`;
`kube_proxy_deployed` is true unless that phase is in `kubeadm_init_phases_skip`.

**kube-proxy-free — the addon is skipped when any of these hold** (from `main.yml`):

1. `kube_network_plugin == kube-router` **and** `kube_router_run_service_proxy: true`.
2. `kube_network_plugin == cilium` **and** `cilium_kube_proxy_replacement` is `strict`/
   true (Cilium handles Services in eBPF).
3. `kube_network_plugin == calico` **and** `calico_bpf_enabled: true` (Calico eBPF).
4. `kube_proxy_remove: true` (explicit removal, any CNI).

In those cases no kube-proxy runs and the CNI owns Service/NodePort routing — do **not**
also expect kube-proxy behaviour (iptables/ipvs rules, `kube-ipvs0`) to be present.

**Tuning:** many `kube_proxy_*` knobs exist (sync periods, conntrack timeouts,
`kube_proxy_nodeport_addresses`, `kube_proxy_masquerade_bit`, metrics/healthz bind
addresses, `kube_proxy_strict_arp`, `kube_proxy_feature_gates`, …) — see the individual
`VARIABLE-KUBE_PROXY_*` docs.

## Compatibility

- Default mode `ipvs` is stable across `v2.29.0`–`v2.31.0`. If you switch to `nftables`,
  ensure kernel ≥ 5.13 and Kubernetes ≥ 1.33.
- Switching an existing cluster to kube-proxy-free (enabling Cilium/Calico replacement or
  `kube_proxy_remove`) must be done deliberately — leftover kube-proxy rules should be
  cleaned; a half-migrated node can double-handle Services.
- kube-proxy version is not independently pinned — it moves with `kube_version`.

## References

- `main.yml` (`kube_proxy_mode`, `addon/kube-proxy` skip logic) at tag `v2.31.0`.
- Mode variable: [[VARIABLE-KUBE_PROXY_MODE]]; version coupling:
  [[CONCEPT-K8S_CONTROL_PLANE_VERSIONS]]; nftables kernel floor:
  [[TROUBLE-NFTABLES_KERNEL_TOO_LOW]].
