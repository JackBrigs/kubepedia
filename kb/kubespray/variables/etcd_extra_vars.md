---
id: VARIABLE-ETCD_EXTRA_VARS
type: variable
title: etcd_extra_vars
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_extra_vars
tags:
  - etcd
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Defines default etcd_extra_vars: {} (empty dict of extra ETCD_* env vars)"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_extra_vars

## Summary
A dictionary of extra environment variables injected into the etcd configuration, letting operators pass arbitrary `ETCD_*` settings. Default is an empty dict `{}`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as `etcd_extra_vars: {}` (also declared with the same `{}` default in `roles/kubernetes/control-plane/defaults/main/etcd.yml`). It is iterated with `{% for key, value in etcd_extra_vars.items() %}` in `roles/etcd/templates/etcd.env.j2`, `roles/etcd/templates/etcd-events.env.j2`, and the kubeadm-config templates in `roles/kubernetes/control-plane/templates/`. The default `{}` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Each key/value becomes an additional etcd environment variable; the empty default adds none.

## References
- roles/etcd_defaults/defaults/main.yml
- roles/etcd/templates/etcd.env.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
