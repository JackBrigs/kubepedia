---
id: VARIABLE-CILIUM_AGENT_EXTRA_VOLUME_MOUNTS
type: variable
title: cilium_agent_extra_volume_mounts
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_agent_extra_volume_mounts
tags:
  - cilium
  - cni
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Defines extra volumeMounts for the cilium-agent DaemonSet; default []"
relations: []
---

# cilium_agent_extra_volume_mounts

## Summary
Provides a list of extra `volumeMounts` to inject into the cilium-agent container. Defaults to an empty list `[]`, meaning no additional volume mounts are added.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as:

```yaml
cilium_agent_extra_volume_mounts: []
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts: 220 in v2.29.0/v2.29.1, 218 in v2.30.0, 203 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Cilium CNI only. Paired with `cilium_agent_extra_volumes`, which declares the corresponding `volumes`.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
