---
id: VARIABLE-KUBELET_LOGFILES_MAX_SIZE
type: variable
title: kubelet_logfiles_max_size
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_logfiles_max_size
tags:
  - kubelet
  - logging
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Maximum size of a single kubelet container log file (containerLogMaxSize); default 10Mi"
relations: []
---

# kubelet_logfiles_max_size

## Summary
Maximum size of a single container log file before the kubelet rotates it (maps to the kubelet `containerLogMaxSize` setting). Default is `10Mi`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kubelet_logfiles_max_size: 10Mi
```

Line number: 133 (v2.29.0/v2.29.1), 130 (v2.30.0), 132 (v2.31.0). The value `10Mi` is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Related to `kubelet_logfiles_max_nr` which caps the number of retained log files.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
