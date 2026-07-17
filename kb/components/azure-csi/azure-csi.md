---
id: COMPONENT-AZURE_CSI
type: component
title: azure-csi
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "1.10.0"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - azure-csi
tags:
  - csi
  - storage
  - azure
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "azure_csi_plugin_version / azure_csi_plugin_image_repo / azure_csi_plugin_image_tag"
relations:
  - type: see_also
    target: CONCEPT-CSI_LAYER
---

# azure-csi

## Summary
`azure-csi` is the Azure Disk CSI driver, the Container Storage Interface plugin that provisions and manages Azure managed disks as Kubernetes PersistentVolumes. Kubespray can deploy it as an optional storage addon. It is disabled by default (`azure_csi_enabled: false`) and pinned to plugin version `1.10.0` across the indexed range.

## Context
This document covers Kubespray tags v2.29.0 through v2.31.0. The driver is opt-in: `azure_csi_enabled` defaults to `false` in every indexed tag. It is deployed by the `kubernetes-apps/csi_driver/azuredisk` role and generally requires `persistent_volumes_enabled` (also `false` by default) plus Azure-side configuration.

## Implementation
The version is defined as a plain literal in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
azure_csi_plugin_version: "1.10.0"
azure_csi_plugin_image_repo: "mcr.microsoft.com/k8s/csi"
azure_csi_plugin_image_tag: "v{{ azure_csi_plugin_version }}"
```

The image tag in `download.yml` is derived from the version, resolving to `v1.10.0`. Note that the role `roles/kubernetes-apps/csi_driver/azuredisk/defaults/main.yml` also defines `azure_csi_plugin_image_tag: latest` as a role-level default.

| Tag | Commit | azure_csi_plugin_version |
|-----|--------|--------------------------|
| v2.29.0 | 9991412 | 1.10.0 |
| v2.29.1 | 0c6a295 | 1.10.0 |
| v2.30.0 | f4ccdb5 | 1.10.0 |
| v2.31.0 | 1c9add4 | 1.10.0 |

The version is unchanged across the entire indexed range.

## Configuration
- Enable flag: `azure_csi_enabled` — default `false` (`roles/kubespray_defaults/defaults/main/main.yml`).
- Version var: `azure_csi_plugin_version` — default `1.10.0`.
- Image repo: `azure_csi_plugin_image_repo` = `mcr.microsoft.com/k8s/csi`.
- Image tag: `azure_csi_plugin_image_tag` = `v{{ azure_csi_plugin_version }}` (download.yml, resolves to `v1.10.0`); role default `latest` in the csi_driver role.
- Key options (`roles/kubernetes-apps/csi_driver/azuredisk/defaults/main.yml`): `azure_csi_use_instance_metadata` (default `true`), `azure_csi_controller_replicas` (default `2`), `azure_csi_controller_affinity` (default `{}`), `azure_csi_node_affinity` (default `{}`).

## Compatibility
| Tag | Version |
|-----|---------|
| v2.29.0 | 1.10.0 |
| v2.29.1 | 1.10.0 |
| v2.30.0 | 1.10.0 |
| v2.31.0 | 1.10.0 |

Applicable to the Kubernetes versions shipped by these Kubespray tags (roughly 1.31–1.35).

## References
- roles/kubespray_defaults/defaults/main/download.yml (azure_csi_plugin_version, azure_csi_plugin_image_repo, azure_csi_plugin_image_tag)
- roles/kubespray_defaults/defaults/main/main.yml (azure_csi_enabled)
- roles/kubernetes-apps/csi_driver/azuredisk/defaults/main.yml (role options, image tag)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
