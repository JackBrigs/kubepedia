---
id: VARIABLE-APISERVER_LOADBALANCER_DOMAIN_NAME
type: variable
title: apiserver_loadbalancer_domain_name
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - apiserver_loadbalancer_domain_name
tags:
  - loadbalancer
  - apiserver
  - ha
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Domain name / address of the external API server load balancer"
relations: []
---

# apiserver_loadbalancer_domain_name

## Summary
Domain name (or address) of the external load balancer fronting the Kubernetes API server, used in generated certificates and kubeconfig endpoints. The default value CHANGED between v2.29.1 and v2.30.0.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`. The default differs between tags:

| Tags | Default |
| --- | --- |
| v2.29.0, v2.29.1 | `"lb-apiserver.kubernetes.local"` |
| v2.30.0, v2.31.0 | `"{{ 'localhost' if loadbalancer_apiserver_localhost else (loadbalancer_apiserver.address \| d(undef())) }}"` |

From v2.30.0 the value is computed: it resolves to `localhost` when `loadbalancer_apiserver_localhost` is true, otherwise to the configured `loadbalancer_apiserver.address` (undefined if none).

## Compatibility
Kubespray v2.29.0 through v2.31.0. From v2.30.0 depends on `loadbalancer_apiserver_localhost` and `loadbalancer_apiserver.address`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
