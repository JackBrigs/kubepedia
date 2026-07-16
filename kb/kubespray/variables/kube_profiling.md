---
id: VARIABLE-KUBE_PROFILING
type: variable
title: kube_profiling
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_profiling
tags:
  - security
  - control-plane
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggles profiling (pprof) endpoints on control-plane components; defaults to false."
relations: []
---

# kube_profiling

## Summary
Controls whether Go profiling (pprof) endpoints are enabled on the Kubernetes control-plane components. Defaults to `false`, disabling profiling for a hardened posture (a common CIS-benchmark recommendation).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
kube_profiling: false
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 303 in v2.29.x, 304 in v2.30.0, 316 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies to the apiserver, controller-manager, and scheduler profiling flags.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
