---
id: VARIABLE-PROMETHEUS_OPERATOR_CRDS_ENABLED
type: variable
title: prometheus_operator_crds_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - prometheus_operator_crds_enabled
tags:
  - addons
  - prometheus
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggle for installing prometheus-operator CRDs (default: false)"
relations: []
---

# prometheus_operator_crds_enabled

## Summary
Feature toggle that controls whether Kubespray downloads and installs the prometheus-operator CRDs. Default is `false` (disabled).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` (line 466 in v2.29.0/v2.29.1, 467 in v2.30.0, 474 in v2.31.0):

```yaml
prometheus_operator_crds_enabled: false
```

The value `false` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts).

## Compatibility
Kubespray v2.29.0 through v2.31.0 (unchanged). When set to `true`, activates the related `prometheus_operator_crds_*` download variables (`_version`, `_download_url`, `_checksums`).

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
