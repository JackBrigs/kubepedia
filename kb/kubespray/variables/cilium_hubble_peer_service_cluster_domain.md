---
id: VARIABLE-CILIUM_HUBBLE_PEER_SERVICE_CLUSTER_DOMAIN
type: variable
title: cilium_hubble_peer_service_cluster_domain
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_hubble_peer_service_cluster_domain
tags:
  - cilium
  - hubble
  - dns
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "DNS suffix Hubble-Relay uses to resolve its peer service"
relations: []
---

# cilium_hubble_peer_service_cluster_domain

## Summary
Overrides the DNS suffix that Hubble-Relay uses to resolve its peer service. It defaults to the inventory's `dns_domain`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as `cilium_hubble_peer_service_cluster_domain: "{{ dns_domain }}"`. The default expression is unchanged across v2.29.0-v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Depends on the `dns_domain` variable; related to the Hubble-Relay image variables.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
