---
id: VARIABLE-SCHEDULER_PLUGINS_NAMESPACE
type: variable
title: scheduler_plugins_namespace
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - scheduler_plugins_namespace
tags:
  - kubernetes-apps
  - scheduler-plugins
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/scheduler_plugins/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/scheduler_plugins/defaults/main.yml
    note: "default: scheduler-plugins"
relations: []
---
<!-- generated: variable-stub -->

# scheduler_plugins_namespace

## Summary

Kubespray variable `scheduler_plugins_namespace` — default `scheduler-plugins`. Defined in `roles/kubernetes-apps/scheduler_plugins/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/scheduler_plugins/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
scheduler_plugins_namespace: scheduler-plugins
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/scheduler_plugins/defaults/main.yml` (Kubespray `v2.31.0`).
