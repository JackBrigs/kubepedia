---
id: VARIABLE-KUBE_APISERVER_USE_AUTHORIZATION_CONFIG_FILE
type: variable
title: kube_apiserver_use_authorization_config_file
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_use_authorization_config_file
tags:
  - apiserver
  - authorization
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggles use of a structured authorization config file for the apiserver; default false"
relations: []
---

# kube_apiserver_use_authorization_config_file

## Summary
Toggles whether kube-apiserver uses a structured authorization configuration file. Default is `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_apiserver_use_authorization_config_file: false
```

The value `false` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. In v2.31.0 it is paired with `kube_apiserver_use_authentication_config_file`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
