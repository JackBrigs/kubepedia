---
id: VARIABLE-COREDNS_SVC_NAME
type: variable
title: coredns_svc_name
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - coredns_svc_name
tags:
  - kubernetes-apps
  - ansible
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/ansible/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ansible/defaults/main.yml
    note: "default: coredns"
relations: []
---
<!-- generated: variable-stub -->

# coredns_svc_name

## Summary

Kubespray variable `coredns_svc_name` — default `coredns`. Defined in `roles/kubernetes-apps/ansible/defaults/main.yml`. Present in Kubespray
`v2.31.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/ansible/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
coredns_svc_name: coredns
```

## Compatibility

Present in the Kubespray tags `v2.31.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/ansible/defaults/main.yml` (Kubespray `v2.31.0`).
