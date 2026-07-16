---
id: VARIABLE-KUBE_PROXY_MODE
type: variable
title: kube_proxy_mode
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kube_proxy_mode
tags:
  - kube-proxy
  - networking
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "31 (v2.29.0/v2.30.0), 34 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_proxy_mode: ipvs (default, unchanged v2.29.0–v2.31.0)"
  - type: docs
    path: docs/ansible/vars.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/ansible/vars.md
    note: "kube_proxy_mode changes proxy mode to iptables, ipvs, or nftables"
relations:
  - type: see_also
    target: VARIABLE-KUBE_VERSION
---

# kube_proxy_mode

## Summary

`kube_proxy_mode` sets the proxy mode kube-proxy uses. Kubespray's default is
`ipvs`, unchanged across `v2.29.0`–`v2.31.0` (note this differs from upstream
kube-proxy's own default of `iptables`).

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml`
(`kube_proxy_mode: ipvs`; line 31 in v2.29.0/v2.29.1/v2.30.0, line 34 in
v2.31.0). The
value is passed to the kube-proxy configuration and gates mode-specific tasks:

- `ipvs` (default) — requires the IPVS kernel modules; interacts with
  `kube_proxy_strict_arp` (which must be set when kube-vip ARP is enabled).
- `iptables` — the classic mode (upstream kube-proxy default).
- `nftables` — the nftables backend; mode-specific handling is present in the
  Kubernetes roles across all three tags.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `ipvs`; accepted `iptables` | `ipvs` |
  `nftables`.
- `nftables` mode depends on kube-proxy support in the selected Kubernetes
  version (available for the Kubernetes versions these releases install,
  `>=1.31`; see [[VARIABLE-KUBE_VERSION]]).
- `ipvs` requires IPVS kernel modules on the nodes.

## References

- `roles/kubespray_defaults/defaults/main/main.yml` — default (v2.29.0 `9991412`,
  v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`).
- `docs/ansible/vars.md` — documents the `iptables`/`ipvs`/`nftables` value set;
  `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` carries the sample
  `kube_proxy_mode: ipvs`.
