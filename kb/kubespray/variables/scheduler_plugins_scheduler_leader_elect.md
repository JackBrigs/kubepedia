---
id: VARIABLE-SCHEDULER_PLUGINS_SCHEDULER_LEADER_ELECT
type: variable
title: scheduler_plugins_scheduler_leader_elect
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - scheduler_plugins_scheduler_leader_elect
tags:
  - kubernetes-apps
  - scheduler-plugins
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/scheduler_plugins/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/scheduler_plugins/defaults/main.yml
    note: "default: {{ ((groups['kube_control_plane'] | length) > 1) }}"
relations: []
---
<!-- generated: variable-stub -->

# scheduler_plugins_scheduler_leader_elect

## Summary

Kubespray variable `scheduler_plugins_scheduler_leader_elect` — default `{{ ((groups['kube_control_plane'] | length) > 1) }}`. Defined in `roles/kubernetes-apps/scheduler_plugins/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/scheduler_plugins/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
scheduler_plugins_scheduler_leader_elect: {{ ((groups['kube_control_plane'] | length) > 1) }}
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/scheduler_plugins/defaults/main.yml` (Kubespray `v2.31.0`).
