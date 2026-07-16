---
id: VARIABLE-AZURE_CSI_ENABLED
type: variable
title: azure_csi_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - azure_csi_enabled
tags:
  - csi
  - azure
  - toggle
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Default azure_csi_enabled: false"
relations: []
---

# azure_csi_enabled

## Summary
Toggle that controls whether the Azure Disk CSI driver is deployed. Default is `false` (disabled).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
azure_csi_enabled: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line number shifts: 452 in v2.29.0/v2.29.1, 453 in v2.30.0, 461 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. When enabled, gates deployment using the related `azure_csi_*` image and version variables.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
