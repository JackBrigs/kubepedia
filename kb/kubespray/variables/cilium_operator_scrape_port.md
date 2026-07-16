---
id: VARIABLE-CILIUM_OPERATOR_SCRAPE_PORT
type: variable
title: cilium_operator_scrape_port
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_operator_scrape_port
tags:
  - cilium
  - operator
  - metrics
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_operator_scrape_port, default \"9963\""
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_operator_scrape_port

## Summary
Port on which the Cilium operator exposes its Prometheus metrics endpoint. Default is `"9963"` (a quoted string).

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_operator_scrape_port: "9963"
```

The default value `"9963"` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts between tags).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies only when `kube_network_plugin: cilium`. Relevant when operator metrics scraping is enabled (see `cilium_enable_prometheus`).

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
