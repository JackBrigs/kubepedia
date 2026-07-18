---
id: VARIABLE-K8S_NAMESPACE
type: variable
title: k8s_namespace
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - k8s_namespace
tags:
  - kubernetes-apps
  - utils
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/utils/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/utils/defaults/main.yml
    note: "default: kube-system"
relations: []
---
<!-- generated: variable-stub -->

# k8s_namespace

## Summary

Kubespray variable `k8s_namespace` — default `kube-system`. Defined in `roles/kubernetes-apps/utils/defaults/main.yml`. Present in Kubespray
`v2.29.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/utils/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
k8s_namespace: kube-system
```

## Compatibility

Present in the Kubespray tags `v2.29.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/utils/defaults/main.yml` (Kubespray `v2.31.0`).
