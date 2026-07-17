---
id: COMPONENT-CALICO
type: component
title: Calico (default CNI)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "3.31.5"
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - calico
  - calico cni
  - kube_network_plugin calico
tags:
  - cni
  - networking
  - calico
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "calicoctl_binary_checksums — first key is calico_version (3.31.5 at v2.31.0)"
  - type: code
    path: roles/network_plugin/calico_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/calico_defaults/defaults/main.yml
    note: "backend/encapsulation/BGP/Typha/eBPF defaults"
relations:
  - type: depends_on
    target: VARIABLE-KUBE_NETWORK_PLUGIN
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: CONFIG-CALICO_DATAPLANE
  - type: see_also
    target: CONCEPT-CLUSTER_NETWORKING
---

# Calico (default CNI)

## Summary

Calico is the **default** Kubespray CNI (`kube_network_plugin: calico`). At tag **v2.31.0** it
ships **v3.31.5** (`calico_version` is computed per tag as the first/highest key of
`calicoctl_binary_checksums`). Calico provides pod networking, IPAM, and NetworkPolicy; Kubespray
deploys `calico-node` (a DaemonSet), the CNI plugin, and optionally Typha and an eBPF/WireGuard
dataplane. Kubespray's default encapsulation is **VXLAN** (not BGP).

## Context

- This doc covers Kubespray `v2.29.0`–`v2.31.0`; the Calico version is **per-tag computed** from
  the shipped checksums (3.31.5 at v2.31.0; older tags ship older 3.x). Config is owned by the
  `roles/network_plugin/calico_defaults` + `roles/network_plugin/calico` roles.
- Calico is the alternative to Cilium ([[COMPONENT-CILIUM]]); pick one via
  [[VARIABLE-KUBE_NETWORK_PLUGIN]].

## Implementation

- **Components:** `calico-node` (DaemonSet: the Felix agent + BIRD/VXLAN dataplane + CNI),
  the CNI binary/config (`k8s-pod-network`), `calico-kube-controllers`, and optionally **Typha**
  (`typha_enabled: false` by default — enable it to scale to large node counts).
- **Datastore:** the **Kubernetes datastore (kdd)** — Calico stores its state as CRDs in the
  API server (no separate etcd datastore in the default path).
- **Images/version:** `calico_cni`, `calico_node`, `calico_typha`, `calico_kube_controllers`
  all track `calico_version`; `calicoctl` too.

## Configuration

- **Default dataplane/encapsulation (`calico_defaults`):** `calico_network_backend: vxlan`;
  **VXLAN on** (`calico_vxlan_mode: Always`, VNI 4096, port 4789); **IPIP off**
  (`calico_ipip_mode: Never`, `calico_ipv4pool_ipip: "Off"`); `nat_outgoing: true`; default IP
  pool `default-pool`, blocksize 26. Full mode matrix (VXLAN/BGP/IPIP/eBPF/WireGuard/nftables):
  [[CONFIG-CALICO_DATAPLANE]].
- **BGP** is opt-in (`calico_network_backend: bird`, `global_as_num: 64512`,
  `peer_with_router`/`peer_with_calico_rr`, route-reflector role under `calico/rr`).
- **Felix** tunables: `calico_felix_chaininsertmode: Insert`, Prometheus metrics off by default
  (`calico_felix_prometheusmetricsenabled: false`), `calico_iptables_backend: Auto`.
- Resource defaults: `calico-node` mem limit 500M / request 64M.

## Compatibility

- **Kubernetes:** Calico 3.31 supports recent Kubernetes minors (the base's 1.31–1.35 window);
  confirm the exact Calico↔Kubernetes matrix for the shipped 3.x patch before upgrading.
- **Upgrades:** Calico is upgraded with the Kubespray tag; a CNI change / dataplane switch
  (e.g. to eBPF, or VXLAN→BGP) is disruptive — plan it as its own change. Do **not** switch
  `kube_network_plugin` on a running cluster.
- **kube-proxy:** default Calico keeps kube-proxy (unlike Cilium's kube-proxy replacement); the
  **eBPF dataplane** can replace kube-proxy — see [[CONFIG-CALICO_DATAPLANE]].

## References

- `calicoctl_binary_checksums` + `calico_defaults/defaults/main.yml` (v2.31.0, above);
  dataplane modes: [[CONFIG-CALICO_DATAPLANE]]; troubleshooting:
  [[TROUBLE-CALICO_NODE_ISSUES]]; alternative CNI: [[COMPONENT-CILIUM]].
