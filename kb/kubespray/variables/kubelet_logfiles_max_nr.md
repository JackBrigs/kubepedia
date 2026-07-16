---
id: VARIABLE-KUBELET_LOGFILES_MAX_NR
type: variable
title: kubelet_logfiles_max_nr
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet_logfiles_max_nr
tags:
  - kubelet
  - logging
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Maximum number of kubelet log files kept (containerLogMaxFiles); default 5"
relations: []
---

# kubelet_logfiles_max_nr

## Summary
Maximum number of container log files retained per container by the kubelet (maps to the kubelet `containerLogMaxFiles` setting). Default is `5`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml`:

```yaml
kubelet_logfiles_max_nr: 5
```

Line number: 130 (v2.29.0/v2.29.1), 127 (v2.30.0), 129 (v2.31.0). The value `5` is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Related to `kubelet_logfiles_max_size` which caps the size of each log file.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
