---
id: VARIABLE-CILIUM_AGENT_EXTRA_ARGS
type: variable
title: cilium_agent_extra_args
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_agent_extra_args
tags:
  - cilium
  - cni
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "List of extra Cilium agent arguments, default []"
relations: []
---

# cilium_agent_extra_args

## Summary
List of extra command-line arguments passed to the Cilium agent. Default: `[]` (empty list). This is the non-deprecated replacement for `cilium_agent_custom_args`.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_agent_extra_args: []
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0 when the Cilium CNI is used. Related variables: `cilium_agent_custom_args` (deprecated), `cilium_agent_extra_env_vars`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
