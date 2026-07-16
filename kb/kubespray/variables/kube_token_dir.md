---
id: VARIABLE-KUBE_TOKEN_DIR
type: variable
title: kube_token_dir
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_token_dir
tags:
  - control-plane
  - authentication
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines the token directory default \"{{ kube_config_dir }}/tokens\""
relations: []
---

# kube_token_dir

## Summary
Directory holding token-authentication files (e.g. `known_tokens.csv`) for the cluster. The default is `"{{ kube_config_dir }}/tokens"`. The apiserver static pod mounts this path and reads the token auth file from it.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
kube_token_dir: "{{ kube_config_dir }}/tokens"
```

The same value is also present in the sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml:15`. It is consumed in the kubeadm config templates for the apiserver `token-auth-file` and its `hostPath`/`mountPath` volume mount. The default value and path are unchanged across v2.29.0-v2.31.0 (only the surrounding line number in the defaults file shifts: 194 in v2.29.0/v2.29.1, 195 in v2.30.0, 192 in v2.31.0).

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Derived from `kube_config_dir`; used together with token-based static authentication of the apiserver.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
