---
id: VARIABLE-KUBELET_CUSTOM_FLAGS
type: variable
title: kubelet_custom_flags
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_custom_flags
tags:
  - kubelet
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Custom flags passed to kubelet; default empty list []"
relations: []
---

# kubelet_custom_flags

## Summary
List of custom flags to be passed to the kubelet. Empty by default, allowing operators to append arbitrary kubelet command-line flags.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` with the comment `## Support custom flags to be passed to kubelet`:

```yaml
kubelet_custom_flags: []
```

The default (empty list `[]`) is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 136 in v2.29.0/v2.29.1, 133 in v2.30.0, 135 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed when rendering the kubelet service/configuration.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
