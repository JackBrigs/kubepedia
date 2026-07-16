---
id: VARIABLE-NODELOCALDNS_BIND_METRICS_HOST_IP
type: variable
title: nodelocaldns_bind_metrics_host_ip
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nodelocaldns_bind_metrics_host_ip
tags:
  - nodelocaldns
  - dns
  - metrics
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Whether nodelocaldns binds its metrics endpoint to the host IP"
relations:
  - type: see_also
    target: COMPONENT-NODELOCALDNS
---

# nodelocaldns_bind_metrics_host_ip

## Summary
Controls whether the nodelocaldns metrics endpoint binds to the host IP. Default: `false`.

## Implementation
The authoritative default is in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
nodelocaldns_bind_metrics_host_ip: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. The sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` sets the same value (`false`), so there is no discrepancy.

## Compatibility
Kubespray range: `>=v2.29.0 <=v2.31.0`. Relevant to nodelocaldns metrics; related to `nodelocaldns_health_port`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
