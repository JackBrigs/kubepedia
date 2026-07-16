---
id: VARIABLE-KUBE_ENCRYPTION_RESOURCES
type: variable
title: kube_encryption_resources
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_encryption_resources
tags:
  - control-plane
  - encryption
  - secrets
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "List of API resources covered by encryption-at-rest; default [secrets]"
relations: []
---

# kube_encryption_resources

## Summary
The list of Kubernetes API resources covered by encryption-at-rest. Default: `[secrets]`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `kube_encryption_resources: [secrets]`. It is rendered into the EncryptionConfiguration `resources` list in `roles/kubernetes/control-plane/templates/secrets_encryption.yaml.j2` via `{{ kube_encryption_resources | to_nice_yaml | indent(4, True) }}`. The value `[secrets]` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related: `kube_encrypt_token`, `kube_encryption_algorithm`, `kube_encrypt_secret_data`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- roles/kubernetes/control-plane/templates/secrets_encryption.yaml.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
