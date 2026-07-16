---
id: VARIABLE-KUBE_SERVICE_ADDRESSES
type: variable
title: kube_service_addresses
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kube_service_addresses
tags:
  - networking
  - cidr
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "243 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_service_addresses: 10.233.0.0/18 (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: VARIABLE-KUBE_PODS_SUBNET
---

# kube_service_addresses

## Summary

`kube_service_addresses` is the CIDR from which Kubernetes allocates
`ClusterIP` Service addresses. The default is `10.233.0.0/18` across
`v2.29.0`–`v2.31.0`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml` (`10.233.0.0/18`,
unchanged across all four tags). It is passed to the API server as the service
CIDR and must not overlap with [[VARIABLE-KUBE_PODS_SUBNET]] or the node network.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `10.233.0.0/18` (~16k service IPs).
- For dual-stack, a separate `kube_service_addresses_ipv6` applies; the combined
  service subnets are derived from both.
- Changing it after install is disruptive; set it before the first deploy.

## References

- `roles/kubespray_defaults/defaults/main/main.yml` — default (L230 in v2.29.0,
  L243 in v2.31.0; shifts by tag).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
