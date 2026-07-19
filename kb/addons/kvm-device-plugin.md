---
id: CONCEPT-ADDON_KVM_DEVICE_PLUGIN
type: concept
title: "kvm-device-plugin — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: probable
aliases:
  - kvm-device-plugin
  - devices.kubevirt.io/kvm
tags:
  - addons
  - devices
  - virtualization
  - kvm
sources:
  - type: docs
    path: kubevirt/kubernetes-device-plugins (KVM)
    url: https://github.com/kubevirt/kubernetes-device-plugins/blob/master/docs/README.kvm.md
    note: "advertises devices.kubevirt.io/kvm; upstream archived 2020"
  - type: docs
    path: Kubernetes device plugins
    url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
    note: "device plugin API GA since 1.26, stable through 1.35"
relations:
  - type: see_also
    target: TROUBLE-KVM_DEVICE_PLUGIN
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# kvm-device-plugin — addon

## Summary

A KVM device plugin advertises `/dev/kvm` to the kubelet (resource
`devices.kubevirt.io/kvm`) so VM workloads can schedule on KVM-capable nodes. **Version
caveat:** no public **`kvm-device-plugin` Helm chart at `1.0.0`** exists — `kubevirt/kvm-device-plugin`
is 404; the real upstream `kubevirt/kubernetes-device-plugins` is archived (2020, ships raw
DaemonSet YAML, no chart). The inventory's chart is therefore **likely an internal/fork
packaging** — `confidence: probable`.

## Context

- Class: upstream tool, internal packaging; catalog row in [[CONCEPT-ADDON_CATALOG]].

## Implementation

- Advertises resource `devices.kubevirt.io/kvm`; needs host `/dev/kvm` + a privileged pod.
  The **Device Plugin API is GA since K8s 1.26 and stable through 1.35** (the registration
  mechanism is API-stable), so the plugin mechanism itself is version-safe.

## Configuration

- Nodes must be **KVM-capable** (bare metal or nested virtualization).
- The archived upstream and community forks ship **no published images** — build-your-own.
  A counter/memory-accumulation issue exists without VM-stop detection.

## Compatibility

- **Kubernetes range:** the device-plugin mechanism is stable across 1.29–1.35; the specific
  chart `1.0.0` / images are **unverified** (no public source). Confirm the deployed
  image/manifest.
- **CVEs:** none for this plugin (its Security Overview is empty). Note: `kubevirt/kubevirt`
  CVEs are a different component.

## Upstream issues & upgrade notes (mined 2026-07-19)

**⚠⚠ Upstream unmaintained:** the referenced `kubevirt/kubernetes-device-plugins` repo is **stale/abandoned — last commit April 2020**. There is no active development, no security fixes, and (as the catalog notes) **no published Helm chart at the pinned version**. Do **not** rely on it for new clusters:
- **Alternative:** use a **maintained** KVM device plugin (e.g. the `devices.kubevirt.io/kvm` plugin shipped/maintained within current KubeVirt), or run KubeVirt itself which advertises `/dev/kvm`. Verify whatever image you actually run. Scheduling troubleshooting: [[TROUBLE-KVM_DEVICE_PLUGIN]].

## References

- kubevirt/kubernetes-device-plugins KVM doc, Kubernetes device-plugins doc (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
