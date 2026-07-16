---
id: VARIABLE-PROMETHEUS_OPERATOR_CRDS_VERSION
type: variable
title: prometheus_operator_crds_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - prometheus_operator_crds_version
tags:
  - download
  - prometheus
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Resolves the prometheus-operator CRDs version as the first no_arch checksum key"
relations: []
---

# prometheus_operator_crds_version

## Summary
The prometheus-operator CRDs release version to download, computed as the first key of the `no_arch` map in `prometheus_operator_crds_checksums` (i.e. the newest listed version).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` (line 148 in v2.29.1/v2.30.0/v2.31.0; line 146 in v2.29.0):

```yaml
prometheus_operator_crds_version: "{{ (prometheus_operator_crds_checksums.no_arch | dict2items)[0].key }}"
```

The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts). The resolved value tracks the newest entry in `prometheus_operator_crds_checksums` (e.g. `0.84.0` in v2.29.0/v2.30.0, `0.88.1` in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0 (unchanged expression). Related: `prometheus_operator_crds_checksums`, `prometheus_operator_crds_download_url`, `prometheus_operator_crds_enabled`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
