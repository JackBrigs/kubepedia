---
id: CONFIG-CNI_MTU
type: configuration
title: "CNI overlay MTU (Kubespray)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - calico_mtu
  - cilium_mtu
  - cni overlay mtu
  - pod mtu vxlan overhead
  - kube_ovn_mtu
tags:
  - networking
  - cni
  - configuration
  - mtu
sources:
  - type: code
    path: roles/network_plugin/calico/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/calico/defaults/main.yml
    note: "calico_mtu (commented → auto)"
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "cilium_mtu: '0' (auto-detect)"
relations:
  - type: see_also
    target: TROUBLE-VXLAN_MTU_MISMATCH
  - type: see_also
    target: CONFIG-CALICO_DATAPLANE
---

# CNI overlay MTU (Kubespray)

## Summary

Pod MTU must account for encapsulation overhead, or large packets drop intermittently.
Kubespray **auto-detects** the MTU by default (`cilium_mtu: "0"`, `calico_mtu` commented =
auto); you override it per plugin when the underlay MTU is non-standard (jumbo frames, cloud
overlays, VPN).

## Configuration

- **Cilium:** `cilium_mtu: "0"` (default) auto-detects from the device; set a number to pin it.
- **Calico:** `calico_mtu` (commented out by default → Calico auto-detects); set it to the
  underlay MTU **minus overhead** when needed.
- **kube-ovn:** `kube_ovn_mtu` (default commented).
- **Overhead to subtract from the underlay MTU:** VXLAN ≈ **50** bytes, IPIP ≈ **20**,
  WireGuard ≈ **60**. On a 1500-byte underlay, VXLAN pods want **1450**; on jumbo (9000) set the
  overlay accordingly.

## Compatibility

- **Auto-detect is usually right** on standard networks — only override when the underlay MTU
  isn't 1500 or a VPN/cloud reduces the path MTU. A **too-high** pod MTU is the classic cause of
  "small requests work, large transfers hang" ([[TROUBLE-VXLAN_MTU_MISMATCH]]).
- Keep the MTU **consistent** across nodes; a mismatch breaks only some paths.
- Calico encapsulation mode (VXLAN/IPIP) sets the overhead — pick the MTU to match
  ([[CONFIG-CALICO_DATAPLANE]]).

## References

- `calico`/`cilium` defaults (v2.31.0, above); symptom: [[TROUBLE-VXLAN_MTU_MISMATCH]]; Calico
  dataplane: [[CONFIG-CALICO_DATAPLANE]].
