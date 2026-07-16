---
id: VARIABLE-NAMESERVERS
type: variable
title: nameservers
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nameservers
tags:
  - dns
  - preinstall
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "List of additional upstream DNS nameservers for node resolv.conf"
relations: []
---

# nameservers

## Summary
List of additional upstream DNS nameservers configured on nodes (used when building the host `resolv.conf` / DNS configuration). Default is an empty list `[]`.

## Implementation
Defined as a role default in `roles/kubernetes/preinstall/defaults/main.yml` with value `nameservers: []`. The default is unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the preinstall DNS/resolv.conf configuration handling.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
