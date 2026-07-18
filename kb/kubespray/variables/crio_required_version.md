---
id: VARIABLE-CRIO_REQUIRED_VERSION
type: variable
title: crio_required_version
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - crio_required_version
tags:
  - container-engine
  - cri-o
  - variable
sources:
  - type: code
    path: roles/container-engine/cri-o/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/cri-o/defaults/main.yml
    note: "default: {{ kube_version | regex_replace('^(?P<major>//d+).(?P<minor>//d+).(…"
relations: []
---
<!-- generated: variable-stub -->

# crio_required_version

## Summary

Kubespray variable `crio_required_version` — default `{{ kube_version | regex_replace('^(?P<major>//d+).(?P<minor>//d+).(…`. Defined in `roles/container-engine/cri-o/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/container-engine/cri-o/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
crio_required_version: {{ kube_version | regex_replace('^(?P<major>//d+).(?P<minor>//d+).(…
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/container-engine/cri-o/defaults/main.yml` (Kubespray `v2.31.0`).
