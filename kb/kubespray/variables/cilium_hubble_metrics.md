---
id: VARIABLE-CILIUM_HUBBLE_METRICS
type: variable
title: cilium_hubble_metrics
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_hubble_metrics
tags:
  - cilium
  - hubble
  - metrics
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "List of Hubble metrics to enable"
relations: []
---

# cilium_hubble_metrics

## Summary
List of Hubble metrics to enable (used when `cilium_enable_hubble_metrics` is true). Default is an empty list `[]`. Commented examples in the source include `dns`, `drop`, `tcp`, `flow`, `icmp`, and `http`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_hubble_metrics: []`. The default is unchanged across v2.29.0-v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Related to `cilium_enable_hubble_metrics` and `cilium_hubble_scrape_port`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
