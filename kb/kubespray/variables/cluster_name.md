---
id: VARIABLE-CLUSTER_NAME
type: variable
title: cluster_name
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cluster_name
tags:
  - dns
  - cluster
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Cluster DNS domain, default cluster.local"
relations: []
---

# cluster_name

## Summary
The internal cluster DNS domain name. Defaults to `cluster.local`. Set both in the role defaults and mirrored in the sample inventory.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
cluster_name: cluster.local
```

The same value is also present in `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`. The value `cluster.local` is unchanged across v2.29.0-v2.31.0 (role default line 119 in v2.29.0/v2.29.1/v2.31.0, 120 in v2.30.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Used to build in-cluster DNS names for services.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
