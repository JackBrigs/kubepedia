---
id: VARIABLE-ARTIFACTS_DIR
type: variable
title: artifacts_dir
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - artifacts_dir
tags:
  - kubernetes
  - client
  - variable
sources:
  - type: code
    path: roles/kubernetes/client/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/client/defaults/main.yml
    note: "default: {{ inventory_dir }}/artifacts"
relations: []
---
<!-- generated: variable-stub -->

# artifacts_dir

## Summary

Kubespray variable `artifacts_dir` — default `{{ inventory_dir }}/artifacts`. Defined in `roles/kubernetes/client/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes/client/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
artifacts_dir: {{ inventory_dir }}/artifacts
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes/client/defaults/main.yml` (Kubespray `v2.31.0`).
