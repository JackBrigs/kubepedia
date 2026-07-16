---
id: VARIABLE-KUBE_SCHEDULER_BIND_ADDRESS
type: variable
title: kube_scheduler_bind_address
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_scheduler_bind_address
tags:
  - control-plane
  - kube-scheduler
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
    note: "Defines the default bind address \"::\" for kube-scheduler"
relations: []
---

# kube_scheduler_bind_address

## Summary
Sets the address on which the kube-scheduler binds/serves. The default is `"::"` (all IPv6/dual-stack interfaces). The interface must be reachable by the rest of the cluster and by CLI/web clients. It feeds the scheduler `bind-address` and the health-check endpoint.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml:7` as:

```yaml
kube_scheduler_bind_address: "::"
```

Consumed in the kubeadm config templates (`kubeadm-config.v1beta3.yaml.j2` and `kubeadm-config.v1beta4.yaml.j2`) as the scheduler `bind-address`, and in `roles/kubernetes/control-plane/handlers/main.yml` where the health endpoint uses `kube_scheduler_bind_address if kube_scheduler_bind_address != '::' else 'localhost'`. The default value and path are unchanged across v2.29.0-v2.31.0 (in v2.31.0 the v1beta3 template was removed, so only the v1beta4 template consumes it).

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related to other kube-scheduler options in the same defaults file (e.g. `kube_scheduler_client_conn_extra_opts`, `kube_scheduler_config_extra_opts`).

## References
- roles/kubernetes/control-plane/defaults/main/kube-scheduler.yml
- roles/kubernetes/control-plane/handlers/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
