---
id: VARIABLE-KUBEADM_UPGRADE_NODE_PHASES_SKIP
type: variable
title: kubeadm_upgrade_node_phases_skip
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_upgrade_node_phases_skip
tags:
  - kubeadm
  - upgrade
  - control-plane
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Computed list of kubeadm upgrade node phases to skip"
relations: []
---

# kubeadm_upgrade_node_phases_skip

## Summary
List of kubeadm upgrade-node phases to skip when upgrading a secondary control-plane node. For Kubernetes >= 1.32.0 it combines `kubeadm_upgrade_node_phases_skip_default` (empty) with `kubeadm_init_phases_skip`; otherwise it is just the default (empty list).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a Jinja block expression:

```yaml
kubeadm_upgrade_node_phases_skip_default: []
kubeadm_upgrade_node_phases_skip: >-
  {%- if kube_version is version('1.32.0', '>=') -%}
  {{ kubeadm_upgrade_node_phases_skip_default + kubeadm_init_phases_skip }}
  {%- else -%}
  {{ kubeadm_upgrade_node_phases_skip_default }}
  {%- endif -%}
```

The expression is byte-identical across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 72 in v2.29.0-v2.30.0, line 71 in v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Related variables: `kubeadm_upgrade_node_phases_skip_default`, `kubeadm_init_phases_skip`, `kube_version`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
