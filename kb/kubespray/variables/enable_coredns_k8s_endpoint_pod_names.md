---
id: VARIABLE-ENABLE_COREDNS_K8S_ENDPOINT_POD_NAMES
type: variable
title: enable_coredns_k8s_endpoint_pod_names
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - enable_coredns_k8s_endpoint_pod_names
tags:
  - coredns
  - dns
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Enables the CoreDNS kubernetes endpoint_pod_names option; default false"
relations: []
---

# enable_coredns_k8s_endpoint_pod_names

## Summary
Toggles the CoreDNS `kubernetes` plugin `endpoint_pod_names` option, which uses the pod name for the endpoint's A/PTR record instead of the pod IP-derived name. Default is `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:
```yaml
enable_coredns_k8s_endpoint_pod_names: false
```
Also exposed as `false` in `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`. The default value `false` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number varies).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `enable_coredns_k8s_external` and the CoreDNS deployment.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
