---
id: CONCEPT-OVN4NFV
type: concept
title: "ovn4nfv (Nodus) — niche OVN-based CNI for network-function virtualization"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - ovn4nfv
  - nodus cni
  - kube_network_plugin ovn4nfv
  - ovn network function virtualization
tags:
  - kubespray
  - cni
  - networking
  - niche
sources:
  - type: code
    path: roles/network_plugin/ovn4nfv/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/ovn4nfv/tasks/main.yml
    note: "labels control-plane node ovn4nfv-k8s-plugin=ovn-control-plane; applies ovn-daemonset + ovn4nfv-k8s-plugin manifests"
relations:
  - type: see_also
    target: VARIABLE-KUBE_NETWORK_PLUGIN
  - type: see_also
    target: ROLE-NETWORK_PLUGIN
  - type: see_also
    target: CONCEPT-CUSTOM_CNI
---

# ovn4nfv (Nodus) — niche OVN-based CNI for network-function virtualization

## Summary

`kube_network_plugin: ovn4nfv` selects **OVN4NFV-K8s-Plugin** (now known as **Nodus**), an
**OVN/OVS-based** CNI aimed at **network-function virtualization (NFV)** and telco use cases —
multiple/dynamic networks, service function chaining, provider networks. It is a **niche** option in
Kubespray (edge/NFV workloads), not a general-purpose CNI; most clusters should use Cilium/Calico.

## Context

- Selected via [[VARIABLE-KUBE_NETWORK_PLUGIN]] `= ovn4nfv`; applied by the `network_plugin/ovn4nfv`
  role ([[ROLE-NETWORK_PLUGIN]]). Present across **v2.27.0–v2.31.0** but rarely used.
- **What the role does** (`roles/network_plugin/ovn4nfv/tasks/main.yml`@v2.31.0): labels the first
  control-plane node `ovn4nfv-k8s-plugin=ovn-control-plane`, then applies the **`ovn-daemonset`** (OVN
  control/DB + OVS) and the **`ovn4nfv-k8s-plugin`** manifests. OVN provides the overlay; the
  ovn4nfv/Nodus plugin adds the NFV features (dynamic networks via `Network`/`ProviderNetwork` CRDs,
  SFC).
- **Use case:** Kubernetes clusters running **VNFs / CNFs** that need multiple isolated networks and
  provider-network attachment per pod — the OVN model fits NFV better than a single flat pod network.
  For anything not NFV-specific, this is the wrong CNI.

## Implementation notes

- **Niche / lower-traffic:** validate the plugin version against your Kubernetes version yourself; the
  ovn4nfv/Nodus project moves independently of Kubespray. For a modern OVN CNI on general clusters,
  **Kube-OVN** (`COMPONENT-KUBE_OVN`) is the more mainstream managed option.
- If you need a specific/newer build, consider delivering it via [[CONCEPT-CUSTOM_CNI]] instead.

## References

- `roles/network_plugin/ovn4nfv/tasks/main.yml` (tag v2.31.0). Selector
  [[VARIABLE-KUBE_NETWORK_PLUGIN]]; role [[ROLE-NETWORK_PLUGIN]]; BYO alternative [[CONCEPT-CUSTOM_CNI]].
