---
id: VARIABLE-SUPPLEMENTARY_ADDRESSES_IN_SSL_KEYS
type: variable
title: supplementary_addresses_in_ssl_keys
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - supplementary_addresses_in_ssl_keys
tags:
  - certificates
  - apiserver
  - security
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "List of extra Subject Alternative Names added to the kube-apiserver certificate; default []"
relations: []
---

# supplementary_addresses_in_ssl_keys

## Summary
List of additional Subject Alternative Names (IPs/DNS names) added to the
kube-apiserver server certificate. Useful when the API is reached through one or
more load balancers. Default is an empty list.

## Implementation
The variable is consumed in
`roles/kubernetes/control-plane/tasks/kubeadm-setup.yml` to build the apiserver
cert SANs:

```yaml
sans_supp: "{{ supplementary_addresses_in_ssl_keys if supplementary_addresses_in_ssl_keys is defined else [] }}"
```

Per-tag definition:

| Kubespray | Explicit default | Where |
|-----------|------------------|-------|
| v2.29.0   | none (defaults to `[]` via the conditional above; only shown commented-out in sample inventory) | roles/kubernetes/control-plane/tasks/kubeadm-setup.yml |
| v2.29.1   | none (same as v2.29.0) | roles/kubernetes/control-plane/tasks/kubeadm-setup.yml |
| v2.30.0   | `supplementary_addresses_in_ssl_keys: []` | roles/kubernetes/control-plane/defaults/main/main.yml:248 |
| v2.31.0   | `supplementary_addresses_in_ssl_keys: []` | roles/kubernetes/control-plane/defaults/main/main.yml:248 |

An explicit default of `[]` was introduced in v2.30.0; in v2.29.0/v2.29.1 the
variable is optional and the effective default is an empty list.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Affects the kube-apiserver certificate SANs.
Sample inventory shows the example
`supplementary_addresses_in_ssl_keys: [10.0.0.1, 10.0.0.2, 10.0.0.3]`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- roles/kubernetes/control-plane/tasks/kubeadm-setup.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
