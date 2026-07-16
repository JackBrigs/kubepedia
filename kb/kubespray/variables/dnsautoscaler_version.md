---
id: VARIABLE-DNSAUTOSCALER_VERSION
type: variable
title: dnsautoscaler_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: "1.8.8"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - dnsautoscaler_version
tags:
  - dns
  - version
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Version of the DNS cluster-proportional-autoscaler, default 1.8.8"
relations: []
---

# dnsautoscaler_version

## Summary
Version of the DNS cluster-proportional-autoscaler deployed with CoreDNS. Defaults to `1.8.8`. This value feeds `dnsautoscaler_image_tag` (`v{{ dnsautoscaler_version }}`).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
dnsautoscaler_version: 1.8.8
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `dnsautoscaler_image_tag`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
