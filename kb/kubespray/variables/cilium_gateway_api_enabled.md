---
id: VARIABLE-CILIUM_GATEWAY_API_ENABLED
type: variable
title: cilium_gateway_api_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_gateway_api_enabled
tags:
  - cilium
  - gateway-api
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines cilium_gateway_api_enabled, default false"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_gateway_api_enabled

## Summary
Enables Cilium's Gateway API support for ingress/routing via Kubernetes Gateway API resources. Default is `false`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_gateway_api_enabled: false
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0-v2.31.0 when `kube_network_plugin: cilium`. Related to Cilium's Gateway API / kube-proxy replacement features.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
