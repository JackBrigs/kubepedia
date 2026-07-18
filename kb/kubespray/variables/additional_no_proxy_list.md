---
id: VARIABLE-ADDITIONAL_NO_PROXY_LIST
type: variable
title: additional_no_proxy_list
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - additional_no_proxy_list
tags:
  - network-facts
  - variable
sources:
  - type: code
    path: roles/network_facts/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_facts/defaults/main.yml
    note: "default: {{ additional_no_proxy | split(',') }}"
relations: []
---
<!-- generated: variable-stub -->

# additional_no_proxy_list

## Summary

Kubespray variable `additional_no_proxy_list` — default `{{ additional_no_proxy | split(',') }}`. Defined in `roles/network_facts/defaults/main.yml`. Present in Kubespray
`v2.31.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/network_facts/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
additional_no_proxy_list: {{ additional_no_proxy | split(',') }}
```

## Compatibility

Present in the Kubespray tags `v2.31.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/network_facts/defaults/main.yml` (Kubespray `v2.31.0`).
