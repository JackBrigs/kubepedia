---
id: VARIABLE-ARGOCD_NAMESPACE
type: variable
title: argocd_namespace
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - argocd_namespace
tags:
  - kubernetes-apps
  - argocd
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/argocd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/argocd/defaults/main.yml
    note: "default: argocd"
relations: []
---
<!-- generated: variable-stub -->

# argocd_namespace

## Summary

Kubespray variable `argocd_namespace` — default `argocd`. Defined in `roles/kubernetes-apps/argocd/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/argocd/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
argocd_namespace: argocd
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/argocd/defaults/main.yml` (Kubespray `v2.31.0`).
