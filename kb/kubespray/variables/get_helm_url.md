---
id: VARIABLE-GET_HELM_URL
type: variable
title: get_helm_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - get_helm_url
tags:
  - helm
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Base URL of the official Helm download site; default https://get.helm.sh"
relations: []
---

# get_helm_url

## Summary
Base URL of the Helm distribution site used to construct the Helm binary download URL. Default value is `https://get.helm.sh`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
get_helm_url: https://get.helm.sh
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Override it to fetch the Helm binary from an internal mirror in offline or air-gapped installations.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
