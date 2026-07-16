---
id: VARIABLE-CILIUM_AGENT_SCRAPE_PORT
type: variable
title: cilium_agent_scrape_port
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_agent_scrape_port
tags:
  - cilium
  - cni
  - metrics
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Prometheus scrape port for the cilium-agent; default \"9962\""
relations: []
---

# cilium_agent_scrape_port

## Summary
Sets the port that Prometheus scrapes for cilium-agent metrics. Defaults to `"9962"` (a quoted string).

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_agent_scrape_port: "9962"
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line number shifts: 339 in v2.29.0/v2.29.1, 337 in v2.30.0, 319 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Cilium CNI only; relevant when Cilium metrics/Prometheus scraping is enabled.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
