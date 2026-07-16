---
id: VARIABLE-KUBELET_FEATURE_GATES
type: variable
title: kubelet_feature_gates
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_feature_gates
tags:
  - kubelet
  - feature-gates
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "List of kubelet feature gates; defaults to an empty list"
relations: []
---

# kubelet_feature_gates

## Summary
A list of feature-gate settings applied specifically to kubelet (for example `RotateKubeletServerCertificate=true`). Defaults to an empty list, meaning no kubelet-specific feature gates beyond cluster-wide defaults.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:

```yaml
kubelet_feature_gates: []
```

The default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 606 in v2.29.0, line 626 in v2.31.0). The hardening docs and hardening CI inventory set it to `["RotateKubeletServerCertificate=true"]`, but the role default is `[]`.

## Compatibility
Kubespray v2.29.0 through v2.31.0.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
