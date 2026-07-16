---
id: VARIABLE-KUBE_APISERVER_ENABLE_ADMISSION_PLUGINS
type: variable
title: kube_apiserver_enable_admission_plugins
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kube_apiserver_enable_admission_plugins
tags:
  - security
  - hardening
  - apiserver
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    lines: "101 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "kube_apiserver_enable_admission_plugins: [] (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: VARIABLE-KUBE_POD_SECURITY_USE_DEFAULT
---

# kube_apiserver_enable_admission_plugins

## Summary

`kube_apiserver_enable_admission_plugins` is the list of admission plugins to
enable on the API server **in addition** to the kubeadm defaults. The default is
an empty list `[]` across `v2.29.0`–`v2.31.0`.

## Implementation

Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` (`[]`,
unchanged across all four tags). Its contents become the API server's
`--enable-admission-plugins`. Common hardening additions are
`PodSecurity`, `NodeRestriction`, `EventRateLimit`, `AlwaysPullImages`.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `[]` (kubeadm defaults only).
- Pairs with [[VARIABLE-KUBE_POD_SECURITY_USE_DEFAULT]] for Pod Security
  enforcement.

## References

- `roles/kubernetes/control-plane/defaults/main/main.yml` — default (L98 in
  v2.29.0, L101 in v2.31.0; shifts by tag).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
