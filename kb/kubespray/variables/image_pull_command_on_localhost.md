---
id: VARIABLE-IMAGE_PULL_COMMAND_ON_LOCALHOST
type: variable
title: image_pull_command_on_localhost
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - image_pull_command_on_localhost
tags:
  - download
  - container-runtime
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image-pull command for the localhost/delegate, resolved from the localhost image tool"
relations: []
---

# image_pull_command_on_localhost

## Summary
Holds the command used to pull container images on the localhost (delegate host) during centralized downloads. It is resolved dynamically from a per-tool variable named `<image_command_tool_on_localhost>_image_pull_command`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
image_pull_command_on_localhost: "{{ lookup('vars', image_command_tool_on_localhost + '_image_pull_command') }}"
```

The expression is unchanged across v2.29.0–v2.31.0 (line 69 in v2.29.0, line 71 in v2.29.1/v2.30.0/v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on `image_command_tool_on_localhost` and the corresponding `*_image_pull_command` variable.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
