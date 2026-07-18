---
id: VARIABLE-LOCAL_PATH_PROVISIONER_RECLAIM_POLICY
type: variable
title: local_path_provisioner_reclaim_policy
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - local_path_provisioner_reclaim_policy
tags:
  - kubernetes-apps
  - external-provisioner
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/external_provisioner/local_path_provisioner/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/external_provisioner/local_path_provisioner/defaults/main.yml
    note: "default: Delete"
relations: []
---
<!-- generated: variable-stub -->

# local_path_provisioner_reclaim_policy

## Summary

Kubespray variable `local_path_provisioner_reclaim_policy` — default `Delete`. Defined in `roles/kubernetes-apps/external_provisioner/local_path_provisioner/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/external_provisioner/local_path_provisioner/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
local_path_provisioner_reclaim_policy: Delete
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/external_provisioner/local_path_provisioner/defaults/main.yml` (Kubespray `v2.31.0`).
