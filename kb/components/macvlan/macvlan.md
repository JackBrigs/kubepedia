---
id: COMPONENT-MACVLAN
type: component
title: Macvlan (CNI)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=1.8.0 <=1.9.1"
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - macvlan
  - macvlan cni
  - kube_network_plugin macvlan
  - macvlan_interface
tags:
  - cni
  - networking
  - macvlan
sources:
  - type: code
    path: roles/network_plugin/macvlan/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/macvlan/defaults/main.yml
    note: "macvlan_interface: eth0"
relations:
  - type: depends_on
    target: VARIABLE-KUBE_NETWORK_PLUGIN
  - type: see_also
    target: COMPONENT-MULTUS
  - type: see_also
    target: COMPONENT-CNI_PLUGINS
---

# Macvlan (CNI)

## Summary

Macvlan (`kube_network_plugin: macvlan`) attaches pods **directly to a host interface's L2
segment** — each pod gets its own MAC on the parent NIC's network, with **no overlay/NAT**. It
has no version of its own — the `macvlan` binary ships in the standard CNI plugins bundle
([[COMPONENT-CNI_PLUGINS]], `>=1.8.0 <=1.9.1` at these tags). It's
a niche choice (pods appear as first-class hosts on the LAN); more commonly macvlan is used as a
**secondary** interface via Multus ([[COMPONENT-MULTUS]]).

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`. Select via [[VARIABLE-KUBE_NETWORK_PLUGIN]]. Uses the
  `macvlan` plugin from [[COMPONENT-CNI_PLUGINS]].

## Implementation

- Pods get an interface in **macvlan** mode off a parent host NIC (**`macvlan_interface: eth0`**
  by default) — traffic egresses with the pod's own MAC on that L2.
- No encapsulation and no NetworkPolicy from macvlan itself.

## Configuration

- **`macvlan_interface`** — the parent host NIC; must exist and carry the intended L2 on every
  node.
- IPAM is host-network-scoped — the pod IPs live on the parent LAN; coordinate with the LAN's
  DHCP/addressing to avoid conflicts.

## Compatibility

- **Constraints:** macvlan requires the switch/NIC to permit multiple MACs per port (many clouds
  and some virtual switches **block** this — macvlan often doesn't work on cloud VMs). The host
  parent interface **can't talk to its own macvlan children** by default (a known macvlan
  limitation).
- **No policy/overlay** — use it only where flat L2 pod addressing is truly desired, or as a
  Multus secondary ([[COMPONENT-MULTUS]]).

## References

- macvlan defaults (v2.31.0, above); selection: [[VARIABLE-KUBE_NETWORK_PLUGIN]]; base plugins:
  [[COMPONENT-CNI_PLUGINS]]; meta: [[COMPONENT-MULTUS]].
