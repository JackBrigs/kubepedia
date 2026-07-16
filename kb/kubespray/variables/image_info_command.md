---
id: VARIABLE-IMAGE_INFO_COMMAND
type: variable
title: image_info_command
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - image_info_command
tags:
  - download
  - container-runtime
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Command used to list/inspect local images, resolved from the chosen image tool"
relations: []
---

# image_info_command

## Summary
Holds the command used to query information about images already present on a target host. It is resolved dynamically from a per-tool variable named `<image_command_tool>_image_info_command`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
image_info_command: "{{ lookup('vars', image_command_tool + '_image_info_command') }}"
```

The expression is unchanged across v2.29.0–v2.31.0 (line 68 in v2.29.0, line 70 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on `image_command_tool` and the corresponding `*_image_info_command` variable.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
