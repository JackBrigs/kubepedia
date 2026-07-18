---
id: VARIABLE-GCP_PD_RESTRICT_ZONE_REPLICATION
type: variable
title: gcp_pd_restrict_zone_replication
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - gcp_pd_restrict_zone_replication
tags:
  - kubernetes-apps
  - persistent-volumes
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/persistent_volumes/gcp-pd-csi/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/persistent_volumes/gcp-pd-csi/defaults/main.yml
    note: "default: false"
relations: []
---
<!-- generated: variable-stub -->

# gcp_pd_restrict_zone_replication

## Summary

Kubespray variable `gcp_pd_restrict_zone_replication` — default `false`. Defined in `roles/kubernetes-apps/persistent_volumes/gcp-pd-csi/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/persistent_volumes/gcp-pd-csi/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
gcp_pd_restrict_zone_replication: false
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/persistent_volumes/gcp-pd-csi/defaults/main.yml` (Kubespray `v2.31.0`).
