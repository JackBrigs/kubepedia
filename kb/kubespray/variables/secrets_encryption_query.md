---
id: VARIABLE-SECRETS_ENCRYPTION_QUERY
type: variable
title: secrets_encryption_query
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - secrets_encryption_query
tags:
  - encryption
  - control-plane
  - security
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "JMESPath query used to read the secret from the encryption provider config"
relations: []
---

# secrets_encryption_query

## Summary
JMESPath query used to extract the encryption key secret from the secrets-encryption provider configuration. Default `"resources[*].providers[0].{{ kube_encryption_algorithm }}.keys[0].secret"`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
secrets_encryption_query: "resources[*].providers[0].{{ kube_encryption_algorithm }}.keys[0].secret"
```

The value is unchanged across v2.29.0-v2.31.0 (line 201 in v2.29.0/v2.29.1, 204 in v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Interpolates `kube_encryption_algorithm`; used in control-plane secrets-encryption handling.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
