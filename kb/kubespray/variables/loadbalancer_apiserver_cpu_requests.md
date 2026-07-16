---
id: VARIABLE-LOADBALANCER_APISERVER_CPU_REQUESTS
type: variable
title: loadbalancer_apiserver_cpu_requests
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - loadbalancer_apiserver_cpu_requests
tags:
  - loadbalancer
  - resources
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines loadbalancer_apiserver_cpu_requests with default 25m"
relations: []
---

# loadbalancer_apiserver_cpu_requests

## Summary
CPU request for the local apiserver load balancer pod (nginx-proxy / haproxy) running on the kube_node hosts. Default is `25m`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
loadbalancer_apiserver_cpu_requests: 25m
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related to `loadbalancer_apiserver_memory_requests`, `loadbalancer_apiserver_type`, and `loadbalancer_apiserver_pod_name`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
