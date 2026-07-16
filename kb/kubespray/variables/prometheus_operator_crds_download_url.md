---
id: VARIABLE-PROMETHEUS_OPERATOR_CRDS_DOWNLOAD_URL
type: variable
title: prometheus_operator_crds_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - prometheus_operator_crds_download_url
tags:
  - download
  - prometheus
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Computed download URL for prometheus-operator stripped-down CRDs"
relations: []
---

# prometheus_operator_crds_download_url

## Summary
Download URL for the prometheus-operator stripped-down CRDs bundle. Computed from `github_url` and `prometheus_operator_crds_version`, pointing at the release asset `stripped-down-crds.yaml`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` (line 181 in v2.29.1/v2.30.0/v2.31.0; line 179 in v2.29.0):

```yaml
prometheus_operator_crds_download_url: "{{ github_url }}/prometheus-operator/prometheus-operator/releases/download/v{{ prometheus_operator_crds_version }}/stripped-down-crds.yaml"
```

The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts). The concrete URL depends on `github_url` and the resolved `prometheus_operator_crds_version`.

## Compatibility
Kubespray v2.29.0 through v2.31.0 (unchanged expression). Related: `prometheus_operator_crds_version`, `prometheus_operator_crds_checksums`, `prometheus_operator_crds_enabled`, `github_url`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
