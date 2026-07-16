---
id: VARIABLE-CILIUM_HUBBLE_ENVOY_IMAGE_TAG
type: variable
title: cilium_hubble_envoy_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_hubble_envoy_image_tag
tags:
  - cilium
  - hubble
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image tag for the Cilium/Hubble Envoy container"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_hubble_envoy_image_tag

## Summary
Sets the container image tag for the Cilium Envoy image used by Hubble. It is a pinned build-specific tag (not derived from `cilium_version`) and differs between v2.29.0 and the later tags.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`. The value is a literal pinned tag and changes between tags:

| Tag | Value |
| --- | --- |
| v2.29.0 | `v1.34.7-1757592137-1a52bb680a956879722f48c591a2ca90f7791324` |
| v2.29.1 | `v1.34.10-1762597008-ff7ae7d623be00078865cff1b0672cc5d9bfc6d5` |
| v2.30.0 | `v1.34.10-1762597008-ff7ae7d623be00078865cff1b0672cc5d9bfc6d5` |
| v2.31.0 | `v1.34.10-1762597008-ff7ae7d623be00078865cff1b0672cc5d9bfc6d5` |

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Related to the Cilium/Hubble image download variables (`cilium_hubble_relay_image_repo`, `cilium_hubble_relay_image_tag`).

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
