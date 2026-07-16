---
id: VARIABLE-IMAGE_COMMAND_TOOL
type: variable
title: image_command_tool
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - image_command_tool
tags:
  - download
  - container-runtime
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Selects the CLI tool used to manage/pull images based on container_manager"
relations: []
---

# image_command_tool

## Summary
Chooses the command-line tool used to manage container images on target hosts, derived from `container_manager`. It resolves to `nerdctl` for containerd, `crictl` for CRI-O, and otherwise the value of `container_manager` itself (e.g. `docker`).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
image_command_tool: "{%- if container_manager == 'containerd' -%}nerdctl{%- elif container_manager == 'crio' -%}crictl{%- else -%}{{ container_manager }}{%- endif -%}"
```

The expression is unchanged across v2.29.0–v2.31.0 (line 64 in v2.29.0, line 66 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on `container_manager`; feeds `image_pull_command` and `image_info_command`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
