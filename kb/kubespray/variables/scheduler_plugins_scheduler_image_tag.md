---
id: VARIABLE-SCHEDULER_PLUGINS_SCHEDULER_IMAGE_TAG
type: variable
title: scheduler_plugins_scheduler_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - scheduler_plugins_scheduler_image_tag
tags:
  - scheduler-plugins
  - download
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the image tag for the scheduler-plugins kube-scheduler image"
relations: []
---

# scheduler_plugins_scheduler_image_tag

## Summary
Container image tag for the scheduler-plugins kube-scheduler image. Default is `"v{{ scheduler_plugins_version }}"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
scheduler_plugins_scheduler_image_tag: "v{{ scheduler_plugins_version }}"
```

The value is unchanged across v2.29.0-v2.31.0 (line 295 in v2.29.0, 297 in v2.29.1, 298 in v2.30.0, 292 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Derived from `scheduler_plugins_version`; paired with `scheduler_plugins_scheduler_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
