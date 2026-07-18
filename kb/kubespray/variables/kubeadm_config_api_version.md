---
id: VARIABLE-KUBEADM_CONFIG_API_VERSION
type: variable
title: kubeadm_config_api_version
status: active
kubespray_version: ">=v2.27.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kubeadm_config_api_version
tags:
  - kubespray-defaults
  - variable
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "default: {{ 'v1beta4' if kube_version is version('1.31.0', '>=') else 'v1bet…"
relations: []
---
<!-- generated: variable-stub -->

# kubeadm_config_api_version

## Summary

Kubespray variable `kubeadm_config_api_version` — default `{{ 'v1beta4' if kube_version is version('1.31.0', '>=') else 'v1bet…`. Defined in `roles/kubespray_defaults/defaults/main/main.yml`. Present in Kubespray
`v2.27.0`–`v2.30.0` of the indexed range. **Removed after `v2.30.0`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml` (Kubespray `v2.30.0`):

```yaml
kubeadm_config_api_version: {{ 'v1beta4' if kube_version is version('1.31.0', '>=') else 'v1bet…
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.30.0`. **Removed after `v2.30.0`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubespray_defaults/defaults/main/main.yml` (Kubespray `v2.30.0`).
