---
id: VARIABLE-KUBE_EXTERNAL_CA_MODE
type: variable
title: kube_external_ca_mode
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_external_ca_mode
tags:
  - certificates
  - control-plane
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggles external CA mode for the control plane; default false"
relations: []
---

# kube_external_ca_mode

## Summary
Boolean flag that enables external CA mode, where the cluster CA private key is not present on the nodes and certificates are managed externally. Default: `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
kube_external_ca_mode: false
```

The default value is unchanged across v2.29.0–v2.31.0 (line ~207 in v2.29.x/v2.30.0, ~205 in v2.31.0).

## Compatibility
Kubespray v2.29.0–v2.31.0. Governs kubeadm external-CA behavior for control-plane certificate generation.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
