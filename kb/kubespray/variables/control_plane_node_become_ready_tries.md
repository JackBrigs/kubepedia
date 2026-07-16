---
id: VARIABLE-CONTROL_PLANE_NODE_BECOME_READY_TRIES
type: variable
title: control_plane_node_become_ready_tries
status: active
kubespray_version: ">=v2.30.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - control_plane_node_become_ready_tries
tags:
  - control-plane
  - readiness
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Number of retries waiting for a secondary control-plane node to become Ready, defaults to 24"
relations: []
---

# control_plane_node_become_ready_tries

## Summary
The number of retries used while waiting for a secondary control-plane node to reach the Ready state during the kubeadm secondary join. Default is `24`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` (line 7):

```yaml
control_plane_node_become_ready_tries: 24
```

Consumed in `roles/kubernetes/control-plane/tasks/kubeadm-secondary.yml` as `retries: "{{ control_plane_node_become_ready_tries }}"`. Value is `24` and unchanged between v2.30.0 and v2.31.0.

## Compatibility
Introduced in v2.30.0; present in v2.30.0 and v2.31.0. Not defined in v2.29.0 or v2.29.1.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- roles/kubernetes/control-plane/tasks/kubeadm-secondary.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
