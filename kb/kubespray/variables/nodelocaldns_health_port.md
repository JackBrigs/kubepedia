---
id: VARIABLE-NODELOCALDNS_HEALTH_PORT
type: variable
title: nodelocaldns_health_port
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nodelocaldns_health_port
tags:
  - nodelocaldns
  - dns
  - healthcheck
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "TCP port used by the nodelocaldns health check"
relations: []
---

# nodelocaldns_health_port

## Summary
TCP port on which the nodelocaldns health-check endpoint listens. Default: `9254`.

## Implementation
The authoritative default is in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
nodelocaldns_health_port: 9254
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. The sample inventory `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` sets the same value (`9254`), so there is no discrepancy.

## Compatibility
Kubespray range: `>=v2.29.0 <=v2.31.0`. Related to nodelocaldns; paired with `nodelocaldns_bind_metrics_host_ip`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
