---
id: VARIABLE-CRICTL_IMAGE_INFO_COMMAND
type: variable
title: crictl_image_info_command
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crictl_image_info_command
tags:
  - crictl
  - images
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Shell command that lists RepoTags/RepoDigests of local images via crictl"
relations: []
---

# crictl_image_info_command

## Summary
A shell command template that queries local container images through `crictl`
and extracts their `RepoTags` and `RepoDigests` as a comma-separated list. Used
by Kubespray to determine which images are already present.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as the same
literal across all four tags:

```yaml
crictl_image_info_command: "{{ bin_dir }}/crictl images --verbose | awk -F ': ' '/RepoTags|RepoDigests/ {print $2}' | tr '\n' ','"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on `bin_dir` (location of
the crictl binary).

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
