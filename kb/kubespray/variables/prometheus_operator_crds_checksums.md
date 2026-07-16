---
id: VARIABLE-PROMETHEUS_OPERATOR_CRDS_CHECKSUMS
type: variable
title: prometheus_operator_crds_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - prometheus_operator_crds_checksums
tags:
  - download
  - checksums
  - prometheus
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "no_arch map of prometheus-operator CRDs versions to sha256 checksums"
relations: []
---

# prometheus_operator_crds_checksums

## Summary
A `no_arch` map from prometheus-operator CRDs release version to its sha256 checksum for the downloaded `stripped-down-crds.yaml`. The first (newest) key also drives `prometheus_operator_crds_version`. Contents grow/change per Kubespray release.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml` (line varies by tag: 1614 in v2.29.0, 1760 in v2.29.1, 1408 in v2.30.0, 1526 in v2.31.0). Shape:

```yaml
prometheus_operator_crds_checksums:
  no_arch:
    <version>: sha256:<hash>
    ...
```

The set of versions differs between tags. The newest (first) entry:

| Tag | Newest version key |
| --- | --- |
| v2.29.0 | 0.84.0 |
| v2.30.0 | 0.84.0 |
| v2.31.0 | 0.88.1 |

(v2.29.1 also present; the map is a versioned checksum list, so individual entries vary per tag.)

## Compatibility
Kubespray v2.29.0 through v2.31.0 (contents change per release). Consumed by `prometheus_operator_crds_version` (first `no_arch` key) and used to verify the CRDs download.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
