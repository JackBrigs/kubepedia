---
id: VARIABLE-KUBE_ENCRYPT_TOKEN
type: variable
title: kube_encrypt_token
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_encrypt_token
tags:
  - control-plane
  - encryption
  - secrets
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Secret token used for encryption-at-rest of Kubernetes secrets"
relations: []
---

# kube_encrypt_token

## Summary
The secret token used for encryption-at-rest of Kubernetes secrets. By default it is generated via a `password` lookup of length 32 (ascii letters and digits) stored under `credentials_dir`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```
kube_encrypt_token: "{{ lookup('password', credentials_dir + '/kube_encrypt_token.creds length=32 chars=ascii_letters,digits') }}"
```

At runtime `roles/kubernetes/control-plane/tasks/encrypt-at-rest.yml` may override it with a value extracted from an existing `secrets_encryption.yaml` (`kube_encrypt_token_extracted`), and `roles/kubernetes/control-plane/templates/secrets_encryption.yaml.j2` renders it (base64-encoded) into the EncryptionConfiguration. The definition is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related: `kube_encryption_algorithm`, `kube_encryption_resources`, `kube_encrypt_secret_data`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- roles/kubernetes/control-plane/tasks/encrypt-at-rest.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
