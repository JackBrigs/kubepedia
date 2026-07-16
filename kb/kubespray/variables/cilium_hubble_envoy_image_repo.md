---
id: VARIABLE-CILIUM_HUBBLE_ENVOY_IMAGE_REPO
type: variable
title: cilium_hubble_envoy_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_hubble_envoy_image_repo
tags:
  - cilium
  - hubble
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines cilium_hubble_envoy_image_repo image repository"
relations: []
---

# cilium_hubble_envoy_image_repo

## Summary
Container image repository for the Cilium Envoy proxy used with Hubble. Default is `"{{ quay_image_repo }}/cilium/cilium-envoy"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
cilium_hubble_envoy_image_repo: "{{ quay_image_repo }}/cilium/cilium-envoy"
```

The computed expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0-v2.31.0 when `kube_network_plugin: cilium`. Related to the Cilium Envoy / Hubble image set.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
