---
id: VARIABLE-KUBEADM_UPGRADE_NODE_PHASES_SKIP_DEFAULT
type: variable
title: kubeadm_upgrade_node_phases_skip_default
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_upgrade_node_phases_skip_default
tags:
  - kubeadm
  - upgrade
  - control-plane
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines kubeadm_upgrade_node_phases_skip_default: []"
relations:
  - type: see_also
    target: CONFIG-KUBEADM_CONFIG_API_VERSION
---

# kubeadm_upgrade_node_phases_skip_default

## Summary
Base (default) list of kubeadm upgrade-node phases to skip when upgrading a secondary control-plane node. Default is an empty list (`[]`); it seeds the computed `kubeadm_upgrade_node_phases_skip`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
kubeadm_upgrade_node_phases_skip_default: []
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 71 in v2.29.0-v2.30.0, line 70 in v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Related variable: `kubeadm_upgrade_node_phases_skip`, which consumes this default.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
