---
id: VARIABLE-ETCD_HOSTS
type: variable
title: etcd_hosts
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_hosts
tags:
  - etcd
  - inventory
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Computes etcd_hosts from the etcd inventory group, defaulting to kube_control_plane"
relations: []
---

# etcd_hosts

## Summary
The list of hosts that make up the etcd cluster. Computed from the `etcd` inventory group, falling back to the `kube_control_plane` group when no dedicated `etcd` group is defined.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
etcd_hosts: "{{ groups['etcd'] | default(groups['kube_control_plane']) }}"
```

Used later in the same file to build etcd access/peer/member address lists (the `{% for item in etcd_hosts %}` loops), and consumed in `roles/kubernetes-apps/ansible/templates/etcd_metrics-endpoints.yml.j2`. The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Derived from Ansible inventory groups `etcd` / `kube_control_plane`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
