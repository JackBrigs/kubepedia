---
id: VARIABLE-NERDCTL_IMAGE_INFO_COMMAND
type: variable
title: nerdctl_image_info_command
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nerdctl_image_info_command
tags:
  - nerdctl
  - download
  - images
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Shell command to list locally present images via nerdctl"
relations:
  - type: see_also
    target: COMPONENT-NERDCTL
---

# nerdctl_image_info_command

## Summary
Shell command used to enumerate container images already present on a node via nerdctl in the `k8s.io` namespace, producing a comma-separated `Repository:Tag` list used to decide whether images need downloading.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

`nerdctl_image_info_command: "{{ bin_dir }}/nerdctl -n k8s.io images --format '{% raw %}{{ .Repository }}:{{ .Tag }}{% endraw %}' 2>/dev/null | grep -v ^:$ | tr '\n' ','"`

The expression is unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `bin_dir`; used by the download role when the container runtime is containerd/nerdctl. Parallel to the equivalent command variables for other runtimes.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
