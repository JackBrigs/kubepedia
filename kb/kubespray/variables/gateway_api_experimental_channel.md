---
id: VARIABLE-GATEWAY_API_EXPERIMENTAL_CHANNEL
type: variable
title: gateway_api_experimental_channel
status: active
kubespray_version: ">=v2.27.0 <=v2.27.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - gateway_api_experimental_channel
tags:
  - kubernetes-apps
  - gateway-api
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/gateway_api/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.27.1/roles/kubernetes-apps/gateway_api/defaults/main.yml
    note: "default: false"
relations: []
---
<!-- generated: variable-stub -->

# gateway_api_experimental_channel

## Summary

Kubespray variable `gateway_api_experimental_channel` — default `false`. Defined in `roles/kubernetes-apps/gateway_api/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.27.1` of the indexed range. **Removed after `v2.27.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/gateway_api/defaults/main.yml` (Kubespray `v2.27.1`):

```yaml
gateway_api_experimental_channel: false
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.27.1`. **Removed after `v2.27.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/gateway_api/defaults/main.yml` (Kubespray `v2.27.1`).
