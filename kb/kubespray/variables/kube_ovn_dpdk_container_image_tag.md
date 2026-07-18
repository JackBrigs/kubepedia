---
id: VARIABLE-KUBE_OVN_DPDK_CONTAINER_IMAGE_TAG
type: variable
title: kube_ovn_dpdk_container_image_tag
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kube_ovn_dpdk_container_image_tag
tags:
  - kubespray-defaults
  - variable
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "default: {{ kube_ovn_dpdk_version }}"
relations: []
---
<!-- generated: variable-stub -->

# kube_ovn_dpdk_container_image_tag

## Summary

Kubespray variable `kube_ovn_dpdk_container_image_tag` — default `{{ kube_ovn_dpdk_version }}`. Defined in `roles/kubespray_defaults/defaults/main/download.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` (Kubespray `v2.31.0`):

```yaml
kube_ovn_dpdk_container_image_tag: {{ kube_ovn_dpdk_version }}
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubespray_defaults/defaults/main/download.yml` (Kubespray `v2.31.0`).
