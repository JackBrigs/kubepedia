---
id: VARIABLE-CONTAINERD_UBUNTU_REPO_BASE_URL
type: variable
title: containerd_ubuntu_repo_base_url
status: active
kubespray_version: ">=v2.27.0 <=v2.27.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - containerd_ubuntu_repo_base_url
tags:
  - container-engine
  - containerd-common
  - variable
sources:
  - type: code
    path: roles/container-engine/containerd-common/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.27.1/roles/container-engine/containerd-common/defaults/main.yml
    note: "default: https://download.docker.com/linux/ubuntu"
relations: []
---
<!-- generated: variable-stub -->

# containerd_ubuntu_repo_base_url

## Summary

Kubespray variable `containerd_ubuntu_repo_base_url` — default `https://download.docker.com/linux/ubuntu`. Defined in `roles/container-engine/containerd-common/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.27.1` of the indexed range. **Removed after `v2.27.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/container-engine/containerd-common/defaults/main.yml` (Kubespray `v2.27.1`):

```yaml
containerd_ubuntu_repo_base_url: https://download.docker.com/linux/ubuntu
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.27.1`. **Removed after `v2.27.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/container-engine/containerd-common/defaults/main.yml` (Kubespray `v2.27.1`).
