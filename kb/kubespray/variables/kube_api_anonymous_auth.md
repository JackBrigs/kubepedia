---
id: VARIABLE-KUBE_API_ANONYMOUS_AUTH
type: variable
title: kube_api_anonymous_auth
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_api_anonymous_auth
tags:
  - apiserver
  - auth
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Controls apiserver --anonymous-auth; default true"
relations: []
---

# kube_api_anonymous_auth

## Summary
Controls the kube-apiserver `--anonymous-auth` flag. Default `true`. If set to `"{{ undef() }}"`, the `--anonymous-auth` argument is omitted entirely (per the in-code comment).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
# if kube_api_anonymous_auth: "{{ undef() }}", remove --anonymous-auth argument
kube_api_anonymous_auth: true
```

Unchanged across v2.29.0-v2.31.0 (comment at line 14, value at line 15 in all four tags). Mirrored in the sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` (line 17, `kube_api_anonymous_auth: true`).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Affects control-plane apiserver flags.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
