---
id: VARIABLE-RBAC_ENABLED
type: variable
title: rbac_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - rbac_enabled
tags:
  - rbac
  - authorization
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Computed flag: true when RBAC authorization is active"
relations: []
---

# rbac_enabled

## Summary
Computed boolean indicating whether Kubernetes RBAC authorization is active in the cluster. It is true when `RBAC` is present in `authorization_modes` (and no authorization config file is used), or when the authorization config file is used and it declares an authorizer of type `RBAC`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a computed expression:

```yaml
rbac_enabled: "{{ ('RBAC' in authorization_modes and not kube_apiserver_use_authorization_config_file) or (kube_apiserver_use_authorization_config_file and kube_apiserver_authorization_config_authorizers | selectattr('type', 'equalto', 'RBAC') | list | length > 0) }}"
```

Unchanged across v2.29.0-v2.31.0 (line 576 in v2.29.0/v2.29.1, line 596 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Depends on `authorization_modes`, `kube_apiserver_use_authorization_config_file`, and `kube_apiserver_authorization_config_authorizers`. Not intended to be set directly.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
