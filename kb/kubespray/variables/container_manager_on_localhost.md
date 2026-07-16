---
id: VARIABLE-CONTAINER_MANAGER_ON_LOCALHOST
type: variable
title: container_manager_on_localhost
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - container_manager_on_localhost
tags:
  - container-runtime
  - localhost
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Container manager used on localhost, defaults to container_manager"
relations: []
---

# container_manager_on_localhost

## Summary
Container manager used on the localhost (control) node, e.g. for local download/image operations. Defaults to the value of `container_manager`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
container_manager_on_localhost: "{{ container_manager }}"
```

This computed expression is unchanged across v2.29.0-v2.31.0 (line 351 in v2.29.0/v2.29.1, 352 in v2.30.0, 364 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Depends on `container_manager`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
