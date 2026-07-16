---
id: VARIABLE-ETCD_ADDRESS
type: variable
title: etcd_address
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_address
tags:
  - etcd
  - networking
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "The etcd bind/advertise IP for the current host; derived from main_ip"
relations: []
---

# etcd_address

## Summary
The IP address etcd binds to / advertises on the current host. It is a computed default derived from the host's `main_ip`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:
```yaml
etcd_address: "{{ hostvars[inventory_hostname]['main_ip'] }}"
```
The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number varies).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `etcd_access_address` (which is derived from `main_access_ip`).

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
