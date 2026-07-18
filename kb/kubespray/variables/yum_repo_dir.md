---
id: VARIABLE-YUM_REPO_DIR
type: variable
title: yum_repo_dir
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - yum_repo_dir
tags:
  - container-engine
  - containerd-common
  - variable
sources:
  - type: code
    path: roles/container-engine/containerd-common/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd-common/defaults/main.yml
    note: "default: /etc/yum.repos.d"
relations: []
---
<!-- generated: variable-stub -->

# yum_repo_dir

## Summary

Kubespray variable `yum_repo_dir` — default `/etc/yum.repos.d`. Defined in `roles/container-engine/containerd-common/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/container-engine/containerd-common/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
yum_repo_dir: /etc/yum.repos.d
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/container-engine/containerd-common/defaults/main.yml` (Kubespray `v2.31.0`).
