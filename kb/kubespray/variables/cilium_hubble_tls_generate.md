---
id: VARIABLE-CILIUM_HUBBLE_TLS_GENERATE
type: variable
title: cilium_hubble_tls_generate
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_hubble_tls_generate
tags:
  - cilium
  - hubble
  - tls
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Toggle to auto-generate Hubble TLS certificates"
relations: []
---

# cilium_hubble_tls_generate

## Summary
Boolean toggle to auto-generate TLS certificates for Hubble (relevant when `cilium_hubble_install` is true). Default is `false`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_hubble_tls_generate: false`, preceded by the comment `### Enable auto generate certs if cilium_hubble_install: true`. The default is unchanged across v2.29.0-v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Related to `cilium_hubble_install`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
