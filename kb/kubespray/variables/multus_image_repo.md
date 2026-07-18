---
id: VARIABLE-MULTUS_IMAGE_REPO
type: variable
title: multus_image_repo
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - multus_image_repo
tags:
  - kubespray-defaults
  - variable
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "default: {{ github_image_repo }}/k8snetworkplumbingwg/multus-cni"
relations: []
---
<!-- generated: variable-stub -->

# multus_image_repo

## Summary

Kubespray variable `multus_image_repo` — default `{{ github_image_repo }}/k8snetworkplumbingwg/multus-cni`. Defined in `roles/kubespray_defaults/defaults/main/download.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` (Kubespray `v2.31.0`):

```yaml
multus_image_repo: {{ github_image_repo }}/k8snetworkplumbingwg/multus-cni
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubespray_defaults/defaults/main/download.yml` (Kubespray `v2.31.0`).
