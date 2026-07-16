---
id: VARIABLE-LOADBALANCER_APISERVER_LOCALHOST
type: variable
title: loadbalancer_apiserver_localhost
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - loadbalancer_apiserver_localhost
tags:
  - ha
  - load-balancer
  - apiserver
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "662 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "loadbalancer_apiserver_localhost: {{ loadbalancer_apiserver is not defined }}"
relations:
  - type: see_also
    target: TAG-NODE
  - type: see_also
    target: COMPONENT-KUBE_VIP
---

# loadbalancer_apiserver_localhost

## Summary

`loadbalancer_apiserver_localhost` controls whether each node runs a **local**
API-server load balancer (a localhost proxy such as nginx-proxy/haproxy) to reach
the control plane. It defaults to **true when no external
`loadbalancer_apiserver` is defined**, giving HA API access without external
infrastructure.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
loadbalancer_apiserver_localhost: "{{ loadbalancer_apiserver is not defined }}"
```

So it is `true` by default, and becomes `false` when the operator provides an
external `loadbalancer_apiserver` endpoint. The local load balancer is deployed by
the `kubernetes/node` role (see [[TAG-NODE]]); `kube-vip` ([[COMPONENT-KUBE_VIP]])
is an alternative control-plane VIP mechanism.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default is `true` unless
  `loadbalancer_apiserver` is set.
- With an external LB defined, per-node local balancing is turned off and nodes
  use the external endpoint.

## References

- `roles/kubespray_defaults/defaults/main/main.yml` — default (line shifts by tag:
  L640 in v2.29.0/v2.29.1, L643 in v2.30.0, L662 in v2.31.0).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
