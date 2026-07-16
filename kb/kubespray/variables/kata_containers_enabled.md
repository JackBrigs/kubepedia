---
id: VARIABLE-KATA_CONTAINERS_ENABLED
type: variable
title: kata_containers_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kata_containers_enabled
tags:
  - kata
  - runtime
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggles installation of the Kata Containers runtime; default false"
relations: []
---

# kata_containers_enabled

## Summary
Toggle that enables installation and configuration of the Kata Containers runtime. Disabled by default.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kata_containers_enabled: false
```

Unchanged across v2.29.0-v2.31.0 (line 332 in v2.29.0/v2.29.1, line 333 in v2.30.0, line 345 in v2.31.0). The same default is mirrored in the sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` (`kata_containers_enabled: false`).

## Compatibility
Kubespray v2.29.0 through v2.31.0. When set to `true`, the Kata download/version variables (`kata_containers_version`, `kata_containers_download_url`, `kata_containers_binary_checksum`) become relevant.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
