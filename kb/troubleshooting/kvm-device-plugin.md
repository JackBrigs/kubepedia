---
id: TROUBLE-KVM_DEVICE_PLUGIN
type: troubleshooting
title: "KVM device plugin: devices.kubevirt.io/kvm not schedulable — node not KVM-capable, plugin not registered"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - kvm device plugin
  - /dev/kvm not available
  - devices.kubevirt.io/kvm zero
  - nested virtualization kubevirt
tags:
  - troubleshooting
  - virtualization
  - device-plugin
sources:
  - type: external
    path: kvm_device_plugin
    url: https://github.com/kubevirt/kubernetes-device-plugins
    note: "advertises /dev/kvm as devices.kubevirt.io/kvm; needs a KVM-capable node and a registered device plugin"
relations:
  - type: see_also
    target: CONCEPT-ADDON_KVM_DEVICE_PLUGIN
---

# KVM device plugin: devices.kubevirt.io/kvm not schedulable — node not KVM-capable, plugin not registered

## Summary

The KVM device plugin advertises `/dev/kvm` as the resource **`devices.kubevirt.io/kvm`** so VM workloads schedule on KVM-capable nodes. If VM pods stay `Pending` for that resource, either the **node isn't KVM-capable** (no `/dev/kvm`, nested virt off) or the **device plugin isn't registered** on it.

## Problem

- VM pods `Pending` with `Insufficient devices.kubevirt.io/kvm`, or the resource shows `0` on nodes.

## Context

- KVM device plugin ([[CONCEPT-ADDON_KVM_DEVICE_PLUGIN]]); no fixed public Helm chart version — verify the running image.
- **Node capability:** `/dev/kvm` must exist — bare-metal with VT-x/AMD-V, or a VM with **nested virtualization** enabled. Without it the plugin advertises nothing.
- **Registration:** the plugin DaemonSet must run on the node and register with the kubelet device-plugin socket.

## Diagnostics

```bash
kubectl get nodes -o json | jq '.items[].status.allocatable["devices.kubevirt.io/kvm"]'
kubectl -n <ns> get ds | grep -i kvm ; kubectl -n <ns> logs ds/<kvm-plugin> | tail
# on the node:
ls -l /dev/kvm ; egrep -c '(vmx|svm)' /proc/cpuinfo
```

## Known Issues

- **No /dev/kvm — fix:** enable virtualization/nested-virt on the node (BIOS or cloud instance setting); `/dev/kvm` must be present.
- **Not registered — fix:** ensure the plugin DaemonSet is scheduled on KVM nodes and healthy; restart it so it re-registers with the kubelet.

## References

Upstream project (see `sources`). Catalog entry [[CONCEPT-ADDON_KVM_DEVICE_PLUGIN]].
