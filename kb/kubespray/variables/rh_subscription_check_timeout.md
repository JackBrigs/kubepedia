---
id: VARIABLE-RH_SUBSCRIPTION_CHECK_TIMEOUT
type: variable
title: rh_subscription_check_timeout
status: active
kubespray_version: ">=v2.28.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - rh_subscription_check_timeout
tags:
  - bootstrap-os
  - variable
sources:
  - type: code
    path: roles/bootstrap_os/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/bootstrap_os/defaults/main.yml
    note: "default: 180"
relations: []
---
<!-- generated: variable-stub -->

# rh_subscription_check_timeout

## Summary

Kubespray variable `rh_subscription_check_timeout` — default `180`. Defined in `roles/bootstrap_os/defaults/main.yml`. Present in Kubespray
`v2.28.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/bootstrap_os/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
rh_subscription_check_timeout: 180
```

## Compatibility

Present in the Kubespray tags `v2.28.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/bootstrap_os/defaults/main.yml` (Kubespray `v2.31.0`).
