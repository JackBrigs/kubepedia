---
id: VARIABLE-KUBE_OIDC_AUTH
type: variable
title: kube_oidc_auth
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_oidc_auth
tags:
  - authentication
  - oidc
  - apiserver
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines kube_oidc_auth default false"
relations: []
---

# kube_oidc_auth

## Summary
Enables OpenID Connect (OIDC) authentication for the Kubernetes API server. Default is `false`. When set to `true`, the API server is configured with the OIDC flags/config supplied via the related `kube_oidc_*` variables.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml`:

```yaml
kube_oidc_auth: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. It is exposed as a commented `# kube_oidc_auth: false` in the sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `kube_oidc_url`, `kube_oidc_client_id`, `kube_oidc_username_claim`, `kube_oidc_groups_claim`, and other `kube_oidc_*` settings.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
