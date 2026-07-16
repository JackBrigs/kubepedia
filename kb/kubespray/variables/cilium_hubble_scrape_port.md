---
id: VARIABLE-CILIUM_HUBBLE_SCRAPE_PORT
type: variable
title: cilium_hubble_scrape_port
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_hubble_scrape_port
tags:
  - cilium
  - hubble
  - metrics
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Port used to scrape Hubble metrics"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_hubble_scrape_port

## Summary
Port on which Hubble metrics are exposed/scraped. Default is `"9965"` (a quoted string).

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_hubble_scrape_port: "9965"`. The default is unchanged across v2.29.0-v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Related to `cilium_hubble_metrics` and `cilium_enable_hubble_metrics`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
