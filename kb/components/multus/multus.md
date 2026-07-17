---
id: COMPONENT-MULTUS
type: component
title: Multus (meta-CNI, multiple interfaces)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "4.2.2"
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - multus
  - multus cni
  - NetworkAttachmentDefinition
  - multiple pod interfaces
  - multus_version
tags:
  - cni
  - networking
  - multus
  - meta-plugin
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "multus_version 4.2.2"
  - type: code
    path: roles/network_plugin/multus/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/multus/defaults/main.yml
    note: "conf/bin/run dirs on host"
relations:
  - type: depends_on
    target: VARIABLE-KUBE_NETWORK_PLUGIN
  - type: see_also
    target: COMPONENT-MACVLAN
  - type: see_also
    target: COMPONENT-CALICO
---

# Multus (meta-CNI, multiple interfaces)

## Summary

Multus (**4.2.2** at v2.31.0) is a **meta-plugin**: it lets a pod have **multiple network
interfaces** by chaining other CNIs. It does **not** replace the primary CNI — it runs
**alongside** one (Calico/Cilium/Flannel), which stays the default pod network. Extra interfaces
are requested via **`NetworkAttachmentDefinition`** + a pod annotation.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`. Enable it via `kube_network_plugin: multus` (with a
  primary CNI set) — see [[VARIABLE-KUBE_NETWORK_PLUGIN]]. Typical for NFV/telco, storage
  networks, or attaching macvlan/SR-IOV interfaces ([[COMPONENT-MACVLAN]]).

## Implementation

- Deploys the Multus DaemonSet; it wraps the primary CNI so the first (default) interface is the
  cluster pod network, and additional interfaces come from `NetworkAttachmentDefinition` CRs.
- Host paths (from defaults): CNI conf `/etc/cni/net.d`, bin `/opt/cni/bin`, run `/run` — Multus
  writes its delegating config there.

## Configuration

- Define a **`NetworkAttachmentDefinition`** (referencing a CNI like macvlan/ipvlan/SR-IOV),
  then annotate the pod: `k8s.v1.cni.cncf.io/networks: <nad-name>`.
- The **primary CNI must be healthy** — Multus delegates the default interface to it; a broken
  primary breaks all pods.

## Compatibility

- **Kubernetes:** Multus 4.2.x supports the base's 1.31–1.35 window.
- **Not standalone:** always pair with a primary CNI; Multus alone gives no pod network.
- The secondary interfaces' features/limits come from the delegated CNI, not Multus.

## References

- multus download vars + defaults (v2.31.0, above); selection:
  [[VARIABLE-KUBE_NETWORK_PLUGIN]]; common secondary: [[COMPONENT-MACVLAN]].
