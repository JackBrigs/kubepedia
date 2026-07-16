---
id: VARIABLE-ETCD_CLIENT_URL
type: variable
title: etcd_client_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_client_url
tags:
  - etcd
  - networking
  - url
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "etcd client (2379) URL derived from etcd_access_address"
relations: []
---

# etcd_client_url

## Summary
The etcd client endpoint URL. Default is the computed expression `https://{{ etcd_access_address | ansible.utils.ipwrap }}:2379`, i.e. HTTPS on the client port 2379.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `etcd_client_url: "https://{{ etcd_access_address | ansible.utils.ipwrap }}:2379"` (line 676 in v2.29.0/v2.29.1, 679 in v2.30.0, 698 in v2.31.0). The expression is **unchanged across v2.29.0-v2.31.0**; only the line number shifted.

## Compatibility
Kubespray v2.29.0-v2.31.0. Derived from `etcd_access_address`; uses the `ansible.utils.ipwrap` filter. Fixed client port 2379.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
