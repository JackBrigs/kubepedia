---
id: ROLE-RESET
type: role
title: reset
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - reset
tags:
  - role
sources:
  - type: code
    path: roles/reset
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/reset
    note: "reset role"
relations:
  - type: see_also
    target: TAG-RESET
---

# reset

## Summary

Tears a node back down: stops/removes Kubernetes, etcd, container-runtime state, CNI and Kubespray-managed configuration. Destructive.

## Implementation

Task files under `roles/reset/tasks/`. Invoked from the playbooks under the
corresponding run-tag (see [[TAG-RESET]]).

## Configuration

Driven by variables in `roles/kubespray_defaults` (see [[ROLE-KUBESPRAY_DEFAULTS]]) and the role's own `defaults/`.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.

## References

- `roles/reset/` (tag `v2.31.0` `1c9add4`).
