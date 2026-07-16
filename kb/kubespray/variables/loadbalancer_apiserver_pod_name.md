---
id: VARIABLE-LOADBALANCER_APISERVER_POD_NAME
type: variable
title: loadbalancer_apiserver_pod_name
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - loadbalancer_apiserver_pod_name
tags:
  - loadbalancer
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Computes loadbalancer_apiserver_pod_name from loadbalancer_apiserver_type"
relations: []
---

# loadbalancer_apiserver_pod_name

## Summary
Name of the local apiserver load balancer pod. It is computed from `loadbalancer_apiserver_type`: `nginx-proxy` when the type is `nginx`, otherwise `haproxy`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
loadbalancer_apiserver_pod_name: "{% if loadbalancer_apiserver_type == 'nginx' %}nginx-proxy{% else %}haproxy{% endif %}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Depends on `loadbalancer_apiserver_type`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
