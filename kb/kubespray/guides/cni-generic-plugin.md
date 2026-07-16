---
id: PRACTICE-CNI_GENERIC_PLUGIN
type: best_practice
title: "The 'cni' plugin option: custom / unsupported CNI"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - cni-generic-plugin
tags:
  - operations
  - cni
sources:
  - type: docs
    path: docs/CNI/cni.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/CNI/cni.md
    note: "digest of the tag doc"
relations:
  - type: see_also
    target: COMPONENT-CNI_PLUGINS
---

# The 'cni' plugin option: custom / unsupported CNI

## Summary

Setting `kube_network_plugin: cni` makes Kubespray only unpack the CNI plugin binaries (`cni_version`) into `/opt/cni/bin` and point the container runtime at CNI — it does **not** configure any network. You supply the CNI config yourself.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- For custom routing/bridge/loopback setups or CNIs Kubespray does not manage.

## Implementation

With `kube_network_plugin: cni`, you must populate `/etc/cni/net.d` with a valid CNI configuration after Kubespray runs; otherwise pods have no network. The plugin binaries come from [[COMPONENT-CNI_PLUGINS]] (`cni_version`). This is the escape hatch for unsupported/custom CNIs (contrast the managed [[COMPONENT-CILIUM]] path).

## References

- `docs/CNI/cni.md` (tag v2.31.0 `1c9add4`).
