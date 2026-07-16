---
id: VARIABLE-CILIUM_HUBBLE_CERTGEN_IMAGE_TAG
type: variable
title: cilium_hubble_certgen_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_hubble_certgen_image_tag
tags:
  - cilium
  - hubble
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines cilium_hubble_certgen_image_tag, default v0.2.4"
relations: []
---

# cilium_hubble_certgen_image_tag

## Summary
Container image tag for the Cilium Hubble certgen job. Default is `"v0.2.4"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
cilium_hubble_certgen_image_tag: "v0.2.4"
```

The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0-v2.31.0 when `kube_network_plugin: cilium` with Hubble enabled. Paired with `cilium_hubble_certgen_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
