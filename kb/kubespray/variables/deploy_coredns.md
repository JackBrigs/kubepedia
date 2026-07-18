---
id: VARIABLE-DEPLOY_COREDNS
type: variable
title: deploy_coredns
status: active
kubespray_version: ">=v2.28.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - deploy_coredns
tags:
  - kubernetes-apps
  - ansible
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/ansible/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ansible/defaults/main.yml
    note: "default: true"
relations: []
---
<!-- generated: variable-stub -->

# deploy_coredns

## Summary

Kubespray variable `deploy_coredns` — default `true`. Defined in `roles/kubernetes-apps/ansible/defaults/main.yml`. Present in Kubespray
`v2.28.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/ansible/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
deploy_coredns: true
```

## Compatibility

Present in the Kubespray tags `v2.28.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/ansible/defaults/main.yml` (Kubespray `v2.31.0`).
