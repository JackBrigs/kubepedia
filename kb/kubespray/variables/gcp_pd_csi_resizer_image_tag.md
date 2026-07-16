---
id: VARIABLE-GCP_PD_CSI_RESIZER_IMAGE_TAG
type: variable
title: gcp_pd_csi_resizer_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gcp_pd_csi_resizer_image_tag
tags:
  - csi
  - gcp
  - images
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image tag of the GCP PD CSI external-resizer sidecar; default v0.4.0-gke.0"
relations: []
---

# gcp_pd_csi_resizer_image_tag

## Summary
Sets the container image tag of the external-resizer sidecar used by the GCP Persistent Disk CSI driver deployment. Default value is `v0.4.0-gke.0`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
gcp_pd_csi_resizer_image_tag: "v0.4.0-gke.0"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Relevant only when the GCP PD CSI driver is enabled; it pairs with the other `gcp_pd_csi_*_image_tag` sidecar tags.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
