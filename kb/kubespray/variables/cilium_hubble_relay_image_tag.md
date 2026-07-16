---
id: VARIABLE-CILIUM_HUBBLE_RELAY_IMAGE_TAG
type: variable
title: cilium_hubble_relay_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_hubble_relay_image_tag
tags:
  - cilium
  - hubble
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Container image tag for Hubble-Relay, derived from cilium_version"
relations: []
---

# cilium_hubble_relay_image_tag

## Summary
Container image tag for the Hubble-Relay component, derived from the Cilium version. Default is `"v{{ cilium_version }}"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `cilium_hubble_relay_image_tag: "v{{ cilium_version }}"`. The default expression is unchanged across v2.29.0-v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Depends on `cilium_version`; paired with `cilium_hubble_relay_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
