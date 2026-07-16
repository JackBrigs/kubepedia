---
id: VARIABLE-CILIUM_HUBBLE_INSTALL
type: variable
title: cilium_hubble_install
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_hubble_install
tags:
  - cilium
  - hubble
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Toggle to enable Hubble installation"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_hubble_install

## Summary
Boolean toggle that enables installation of Hubble (Cilium observability) alongside Cilium. Default is `false`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_hubble_install: false`. The default is unchanged across v2.29.0-v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Related to `cilium_hubble_tls_generate` (cert auto-generation when Hubble is installed) and the other `cilium_hubble_*` variables.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
