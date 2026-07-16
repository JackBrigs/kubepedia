---
id: VARIABLE-LOADBALANCER_APISERVER_TYPE
type: variable
title: loadbalancer_apiserver_type
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - loadbalancer_apiserver_type
tags:
  - loadbalancer
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines loadbalancer_apiserver_type with default nginx"
relations: []
---

# loadbalancer_apiserver_type

## Summary
Selects the implementation of the local apiserver load balancer running on the nodes. Default is `nginx` (nginx-proxy); the alternative is haproxy.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
loadbalancer_apiserver_type: "nginx"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Drives `loadbalancer_apiserver_pod_name` (nginx-proxy vs haproxy).

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
