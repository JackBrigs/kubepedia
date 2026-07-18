---
id: VARIABLE-DNS_PREVENT_SINGLE_POINT_FAILURE
type: variable
title: dns_prevent_single_point_failure
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - dns_prevent_single_point_failure
tags:
  - kubernetes-apps
  - ansible
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/ansible/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ansible/defaults/main.yml
    note: "default: {{ 'true' if dns_min_replicas | int > 1 else 'false' }}"
relations: []
---
<!-- generated: variable-stub -->

# dns_prevent_single_point_failure

## Summary

Kubespray variable `dns_prevent_single_point_failure` — default `{{ 'true' if dns_min_replicas | int > 1 else 'false' }}`. Defined in `roles/kubernetes-apps/ansible/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/ansible/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
dns_prevent_single_point_failure: {{ 'true' if dns_min_replicas | int > 1 else 'false' }}
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/ansible/defaults/main.yml` (Kubespray `v2.31.0`).
