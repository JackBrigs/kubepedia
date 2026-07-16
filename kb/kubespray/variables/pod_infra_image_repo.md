---
id: VARIABLE-POD_INFRA_IMAGE_REPO
type: variable
title: pod_infra_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - pod_infra_image_repo
tags:
  - download
  - images
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines pod_infra_image_repo as {{ kube_image_repo }}/pause"
relations: []
---

# pod_infra_image_repo

## Summary
Repository path of the pause (pod infra / sandbox) container image. Defaults to the `pause` image under the configured Kubernetes image repository: `{{ kube_image_repo }}/pause`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` (line 233 in v2.29.1/v2.30.0/v2.31.0; line 231 in v2.29.0):

```yaml
pod_infra_image_repo: "{{ kube_image_repo }}/pause"
```

The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts). The effective value follows whatever `kube_image_repo` resolves to.

## Compatibility
Kubespray v2.29.0 through v2.31.0 (unchanged). Related: `kube_image_repo`, `pod_infra_image_tag`, `pod_infra_version`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
