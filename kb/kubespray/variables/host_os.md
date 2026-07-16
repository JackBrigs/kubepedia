---
id: VARIABLE-HOST_OS
type: variable
title: host_os
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - host_os
tags:
  - os
  - facts
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Normalized host operating system derived from ansible_system"
relations: []
---

# host_os

## Summary
Normalized operating system of the target host. It maps `ansible_system` through `_host_os_groups` (`Linux -> linux`, `Darwin -> darwin`, `Win32NT -> windows`), falling back to the raw `ansible_system` value when no mapping exists.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a Jinja block:

```yaml
host_os: >-
  {%- if ansible_system in _host_os_groups -%}
  {{ _host_os_groups[ansible_system] }}
  {%- else -%}
  {{ ansible_system }}
  {%- endif -%}
```

The computed expression is unchanged across v2.29.0-v2.31.0 (line numbers shift: ~739 in v2.29.x, ~742 in v2.30.0, ~761 in v2.31.0).

## Compatibility
Kubespray v2.29.0-v2.31.0. Related: `_host_os_groups`, `host_architecture`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
