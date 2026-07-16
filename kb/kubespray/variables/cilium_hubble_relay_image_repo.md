---
id: VARIABLE-CILIUM_HUBBLE_RELAY_IMAGE_REPO
type: variable
title: cilium_hubble_relay_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_hubble_relay_image_repo
tags:
  - cilium
  - hubble
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Container image repository for Hubble-Relay"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_hubble_relay_image_repo

## Summary
Container image repository for the Hubble-Relay component, derived from the Quay image repo. Default is `"{{ quay_image_repo }}/cilium/hubble-relay"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `cilium_hubble_relay_image_repo: "{{ quay_image_repo }}/cilium/hubble-relay"`. The default expression is unchanged across v2.29.0-v2.31.0.

## Compatibility
Present in Kubespray v2.29.0 through v2.31.0. Depends on `quay_image_repo`; paired with `cilium_hubble_relay_image_tag`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
