---
id: ROLE-KUBERNETES_NODE
type: role
title: kubernetes/node
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubernetes/node
tags:
  - role
sources:
  - type: code
    path: roles/kubernetes/node
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/kubernetes/node
    note: "kubernetes/node role"
relations:
  - type: see_also
    target: TAG-NODE
---

# kubernetes/node

## Summary

Installs kubelet and the kubelet service on every node, plus the node-local API-server load balancer (nginx-proxy/haproxy/kube-vip).

## Implementation

Task files under `roles/kubernetes/node/tasks/`. Invoked from the playbooks under the
corresponding run-tag (see [[TAG-NODE]]).

## Configuration

Driven by variables in `roles/kubespray_defaults` (see [[ROLE-KUBESPRAY_DEFAULTS]]) and the role's own `defaults/`.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.

## References

- `roles/kubernetes/node/` (tag `v2.31.0` `1c9add4`).
