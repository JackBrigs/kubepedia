---
id: VARIABLE-KUBE_APISERVER_USE_AUTHENTICATION_CONFIG_FILE
type: variable
title: kube_apiserver_use_authentication_config_file
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_use_authentication_config_file
tags:
  - apiserver
  - authentication
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggles use of a structured authentication config file for the apiserver; default false"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_apiserver_use_authentication_config_file

## Summary
Toggles whether kube-apiserver uses a structured authentication configuration file. Default is `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_apiserver_use_authentication_config_file: false
```

Introduced in v2.31.0. Not present in v2.29.0, v2.29.1, or v2.30.0 (grep returns no definition in those tags).

## Compatibility
Available only in Kubespray v2.31.0 within the audited range. Complements `kube_apiserver_use_authorization_config_file`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
