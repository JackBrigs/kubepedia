---
id: VARIABLE-NERDCTL_IMAGE_PULL_COMMAND
type: variable
title: nerdctl_image_pull_command
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nerdctl_image_pull_command
tags:
  - download
  - nerdctl
  - containerd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the command used by nerdctl to pull images into the k8s.io namespace"
relations:
  - type: see_also
    target: COMPONENT-NERDCTL
---

# nerdctl_image_pull_command

## Summary
Defines the shell command used to pull container images with `nerdctl` into the `k8s.io` containerd namespace during the download stage. Default: `{{ bin_dir }}/nerdctl -n k8s.io pull --quiet`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` with the computed default:

```yaml
nerdctl_image_pull_command: "{{ bin_dir }}/nerdctl -n k8s.io pull --quiet"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray range: `>=v2.29.0 <=v2.31.0`. Depends on `bin_dir` for the nerdctl binary location. Used when the container runtime download path relies on nerdctl.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
