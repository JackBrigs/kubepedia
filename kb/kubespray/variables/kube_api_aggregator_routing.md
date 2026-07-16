---
id: VARIABLE-KUBE_API_AGGREGATOR_ROUTING
type: variable
title: kube_api_aggregator_routing
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_api_aggregator_routing
tags:
  - apiserver
  - aggregation
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Controls apiserver --enable-aggregator-routing; default false"
relations: []
---

# kube_api_aggregator_routing

## Summary
Enables the kube-apiserver aggregation-layer routing (the `--enable-aggregator-routing` flag), which routes aggregated API requests to endpoint IPs rather than the cluster IP. Disabled by default.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kube_api_aggregator_routing: false
```

Unchanged across v2.29.0-v2.31.0 (line 300 in v2.29.0/v2.29.1, line 301 in v2.30.0, line 313 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Affects control-plane apiserver flags.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
