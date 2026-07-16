---
id: ROLE-NETWORK_PLUGIN
type: role
title: network_plugin
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - network_plugin
tags:
  - role
sources:
  - type: code
    path: roles/network_plugin
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/network_plugin
    note: "network_plugin role"
relations:
  - type: see_also
    target: TAG-NETWORK
---

# network_plugin

## Summary

Installs and configures the CNI selected by kube_network_plugin (Cilium indexed) by dispatching to the CNI sub-role.

## Implementation

Task files under `roles/network_plugin/tasks/`. Invoked from the playbooks under the
corresponding run-tag (see [[TAG-NETWORK]]).

## Configuration

Driven by variables in `roles/kubespray_defaults` (see [[ROLE-KUBESPRAY_DEFAULTS]]) and the role's own `defaults/`.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.

## References

- `roles/network_plugin/` (tag `v2.31.0` `1c9add4`).
