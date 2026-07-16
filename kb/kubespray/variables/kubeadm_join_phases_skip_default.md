---
id: VARIABLE-KUBEADM_JOIN_PHASES_SKIP_DEFAULT
type: variable
title: kubeadm_join_phases_skip_default
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_join_phases_skip_default
tags:
  - kubeadm
  - join
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Base list of kubeadm join phases to skip; default [] (empty)"
relations:
  - type: see_also
    target: CONFIG-KUBEADM_CONFIG_API_VERSION
---

# kubeadm_join_phases_skip_default

## Summary
Base list of `kubeadm join` phases that should be skipped when joining a new node. Default is an empty list `[]`, meaning no phases are skipped by default. It is the value that `kubeadm_join_phases_skip` resolves to unless overridden.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kubeadm_join_phases_skip_default: []
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 66 in v2.29.x/v2.30.0, line 65 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `kubeadm_join_phases_skip`; may be set to `['preflight']` for air-gapped deployments.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
