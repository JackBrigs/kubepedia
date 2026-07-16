---
id: ROLE-KUBERNETES_PREINSTALL
type: role
title: kubernetes/preinstall
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubernetes/preinstall
tags:
  - role
sources:
  - type: code
    path: roles/kubernetes/preinstall
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/kubernetes/preinstall
    note: "kubernetes/preinstall role"
relations:
  - type: see_also
    target: TAG-PREINSTALL
---

# kubernetes/preinstall

## Summary

Prepares nodes before Kubernetes: swapoff, settings verification (asserts), directory creation, and host DNS/resolv.conf configuration.

## Implementation

Task files under `roles/kubernetes/preinstall/tasks/`. Invoked from the playbooks under the
corresponding run-tag (see [[TAG-PREINSTALL]]).

## Configuration

Driven by variables in `roles/kubespray_defaults` (see [[ROLE-KUBESPRAY_DEFAULTS]]) and the role's own `defaults/`.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.

## References

- `roles/kubernetes/preinstall/` (tag `v2.31.0` `1c9add4`).
