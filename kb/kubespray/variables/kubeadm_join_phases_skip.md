---
id: VARIABLE-KUBEADM_JOIN_PHASES_SKIP
type: variable
title: kubeadm_join_phases_skip
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_join_phases_skip
tags:
  - kubeadm
  - join
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Effective list of kubeadm join phases to skip; defaults to kubeadm_join_phases_skip_default"
relations: []
---

# kubeadm_join_phases_skip

## Summary
Effective list of `kubeadm join` phases skipped when joining a new node. By default it simply resolves to `kubeadm_join_phases_skip_default` (an empty list), so no join phases are skipped unless the user overrides the default.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a folded scalar wrapping the default list:

```yaml
kubeadm_join_phases_skip: >-
 {{ kubeadm_join_phases_skip_default }}
```

Accompanying comment notes it may need to be set to `['preflight']` for air-gapped deployments to avoid failing connectivity tests. The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 67 in v2.29.x/v2.30.0, line 66 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Derives from `kubeadm_join_phases_skip_default`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
