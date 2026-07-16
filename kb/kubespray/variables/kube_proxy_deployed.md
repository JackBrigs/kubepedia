---
id: VARIABLE-KUBE_PROXY_DEPLOYED
type: variable
title: kube_proxy_deployed
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_proxy_deployed
tags:
  - kube-proxy
  - kubeadm
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/main.yml
    note: "Computed constant: true unless the addon/kube-proxy kubeadm phase is skipped"
relations: []
---

# kube_proxy_deployed

## Summary
Computed constant that is true when kube-proxy is deployed by kubeadm, i.e. when the `addon/kube-proxy` init phase is not skipped. Derived from `kubeadm_init_phases_skip`.

## Implementation
Defined as a Kubespray constant in `roles/kubespray_defaults/vars/main/main.yml`:

```yaml
kube_proxy_deployed: "{{ 'addon/kube-proxy' not in kubeadm_init_phases_skip }}"
```

The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (same file, line 20 in each tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0. It is a `vars/` constant (not a user-facing default); its value depends on `kubeadm_init_phases_skip`.

## References
- roles/kubespray_defaults/vars/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
