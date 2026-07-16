---
id: VARIABLE-IMAGE_COMMAND_TOOL_ON_LOCALHOST
type: variable
title: image_command_tool_on_localhost
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - image_command_tool_on_localhost
tags:
  - download
  - container-runtime
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image CLI tool used on the localhost/delegate, defaults to image_command_tool"
relations: []
---

# image_command_tool_on_localhost

## Summary
Specifies the image management CLI tool to use on the localhost (delegate host) when downloading images centrally. It defaults to the same value as `image_command_tool`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
image_command_tool_on_localhost: "{{ image_command_tool }}"
```

The expression is unchanged across v2.29.0–v2.31.0 (line 65 in v2.29.0, line 67 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on `image_command_tool`; feeds `image_pull_command_on_localhost` and `image_info_command_on_localhost`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
