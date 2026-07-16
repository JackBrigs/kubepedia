---
id: VARIABLE-CERT_MANAGER_ENABLED
type: variable
title: cert_manager_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cert_manager_enabled
tags:
  - cert-manager
  - addons
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggles deployment of the cert-manager addon; default false"
relations: []
---

# cert_manager_enabled

## Summary
Toggles whether Kubespray deploys the cert-manager addon into the cluster. Default value is `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
cert_manager_enabled: false
```

Also exposed to users in `inventory/sample/group_vars/k8s_cluster/addons.yml` with the same value `false`. The default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray `>=v2.29.0 <=v2.31.0`. When enabled, gates the `cert_manager_*` image and version variables.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/addons.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
