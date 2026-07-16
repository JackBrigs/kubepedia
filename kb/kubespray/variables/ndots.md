---
id: VARIABLE-NDOTS
type: variable
title: ndots
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ndots
tags:
  - dns
  - resolv-conf
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "ndots option value used in DNS resolv.conf configuration"
relations: []
---

# ndots

## Summary
Sets the `ndots` option used in DNS resolution configuration (resolv.conf / pod dnsConfig). Default is `2`.

## Implementation
Defined as a role default in `roles/kubespray_defaults/defaults/main/main.yml` with value `ndots: 2`. It is also exposed to users in the sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` with the same value `2`. The default is unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Governs DNS search-domain resolution behavior on the cluster.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
