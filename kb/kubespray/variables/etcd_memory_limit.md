---
id: VARIABLE-ETCD_MEMORY_LIMIT
type: variable
title: etcd_memory_limit
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_memory_limit
tags:
  - etcd
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Memory limit for the etcd container/service; computed from host RAM"
relations: []
---

# etcd_memory_limit

## Summary
Memory limit applied to the etcd deployment. Computed from the host's total memory: `512M` on hosts with less than 4096 MB RAM, otherwise `0` (unlimited).

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as:

```yaml
etcd_memory_limit: "{% if ansible_memtotal_mb < 4096 %}512M{% else %}0{% endif %}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0 (present in every tag inspected). Depends on the Ansible fact `ansible_memtotal_mb`.

## References
- roles/etcd_defaults/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
