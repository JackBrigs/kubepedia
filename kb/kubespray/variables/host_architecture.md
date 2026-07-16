---
id: VARIABLE-HOST_ARCHITECTURE
type: variable
title: host_architecture
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - host_architecture
tags:
  - architecture
  - facts
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Normalized host CPU architecture derived from ansible_architecture"
relations: []
---

# host_architecture

## Summary
Normalized CPU architecture of the target host. It maps `ansible_architecture` through `_host_architecture_groups`, falling back to the raw `ansible_architecture` value when no mapping exists.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a Jinja block:

```yaml
host_architecture: >-
  {%- if ansible_architecture in _host_architecture_groups -%}
  {{ _host_architecture_groups[ansible_architecture] }}
  {%- else -%}
  {{ ansible_architecture }}
  {%- endif -%}
```

The computed expression is unchanged across v2.29.0-v2.31.0 (line numbers shift: ~728 in v2.29.x, ~731 in v2.30.0, ~750 in v2.31.0).

## Compatibility
Kubespray v2.29.0-v2.31.0. Related: `_host_architecture_groups`, `host_os`, `image_arch`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
