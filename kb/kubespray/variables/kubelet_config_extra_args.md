---
id: VARIABLE-KUBELET_CONFIG_EXTRA_ARGS
type: variable
title: kubelet_config_extra_args
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_config_extra_args
tags:
  - kubelet
  - config
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Extra key/value settings merged into the kubelet config; defaults to an empty map"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kubelet_config_extra_args

## Summary
A user-supplied map of additional kubelet configuration settings. Defaults to an empty dict. When the cgroup driver is `cgroupfs`, kubespray merges `kubelet_config_extra_args_cgroupfs` into it at fact-setting time.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as:

```yaml
kubelet_config_extra_args: {}
```

Unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 122 in v2.29.0, line 121 in v2.31.0). In `roles/kubernetes/node/tasks/facts.yml` it is re-set when `kubelet_cgroup_driver == 'cgroupfs'`:

```yaml
kubelet_config_extra_args: "{{ kubelet_config_extra_args | combine(kubelet_config_extra_args_cgroupfs) }}"
```

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related: `kubelet_config_extra_args_cgroupfs`, `kubelet_cgroup_driver`.

## References
- roles/kubernetes/node/defaults/main.yml
- roles/kubernetes/node/tasks/facts.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
