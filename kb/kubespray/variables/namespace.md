---
id: VARIABLE-NAMESPACE
type: variable
title: namespace
status: active
kubespray_version: ">=v2.27.0 <=v2.28.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - namespace
tags:
  - kubernetes-apps
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.28.1/roles/kubernetes-apps/defaults/main.yml
    note: "default: kube-system"
relations: []
---
<!-- generated: variable-stub -->

# namespace

## Summary

Kubespray variable `namespace` — default `kube-system`. Defined in `roles/kubernetes-apps/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.28.1` of the indexed range. **Removed after `v2.28.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/defaults/main.yml` (Kubespray `v2.28.1`):

```yaml
namespace: kube-system
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.28.1`. **Removed after `v2.28.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/defaults/main.yml` (Kubespray `v2.28.1`).
