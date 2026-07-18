---
id: VARIABLE-USE_ORACLE_PUBLIC_REPO
type: variable
title: use_oracle_public_repo
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - use_oracle_public_repo
tags:
  - bootstrap-os
  - variable
sources:
  - type: code
    path: roles/bootstrap_os/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/bootstrap_os/defaults/main.yml
    note: "default: true"
relations: []
---
<!-- generated: variable-stub -->

# use_oracle_public_repo

## Summary

Kubespray variable `use_oracle_public_repo` — default `true`. Defined in `roles/bootstrap_os/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/bootstrap_os/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
use_oracle_public_repo: true
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/bootstrap_os/defaults/main.yml` (Kubespray `v2.31.0`).
