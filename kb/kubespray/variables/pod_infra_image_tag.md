---
id: VARIABLE-POD_INFRA_IMAGE_TAG
type: variable
title: pod_infra_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - pod_infra_image_tag
tags:
  - download
  - images
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines pod_infra_image_tag as {{ pod_infra_version }}"
relations: []
---

# pod_infra_image_tag

## Summary
Image tag of the pause (pod infra / sandbox) container. Defaults to the resolved `pod_infra_version`, which is selected from `pod_infra_supported_versions` by the Kubernetes major version.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` (line 234 in v2.29.1/v2.30.0/v2.31.0; line 232 in v2.29.0):

```yaml
pod_infra_image_tag: "{{ pod_infra_version }}"
```

The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts). The concrete tag it resolves to depends on `pod_infra_version` / `pod_infra_supported_versions`, which do change per Kubernetes version.

## Compatibility
Kubespray v2.29.0 through v2.31.0 (unchanged expression). Related: `pod_infra_version`, `pod_infra_supported_versions`, `pod_infra_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
