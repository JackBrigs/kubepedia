---
id: VARIABLE-KUBE_ROUTER_RUN_FIREWALL
type: variable
title: kube_router_run_firewall
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kube_router_run_firewall
tags:
  - network-plugin
  - kube-router
  - variable
sources:
  - type: code
    path: roles/network_plugin/kube-router/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/kube-router/defaults/main.yml
    note: "default: true"
relations: []
---
<!-- generated: variable-stub -->

# kube_router_run_firewall

## Summary

Kubespray variable `kube_router_run_firewall` — default `true`. Defined in `roles/network_plugin/kube-router/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_plugin/kube-router/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
kube_router_run_firewall: true
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_plugin/kube-router/defaults/main.yml` (Kubespray `v2.31.0`).
