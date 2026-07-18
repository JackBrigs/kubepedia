---
id: VARIABLE-KUBELET_STATIC_POD_PATH
type: variable
title: kubelet_static_pod_path
status: active
kubespray_version: ">=v2.29.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kubelet_static_pod_path
tags:
  - kubernetes
  - node
  - variable
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubernetes/node/defaults/main.yml
    note: "default: {{ kube_manifest_dir }}"
relations: []
---
<!-- generated: variable-stub -->

# kubelet_static_pod_path

## Summary

Kubespray variable `kubelet_static_pod_path` — default `{{ kube_manifest_dir }}`. Defined in `roles/kubernetes/node/defaults/main.yml`. Present in Kubespray
`v2.29.0`–`v2.30.0` of the indexed range. **Removed after `v2.30.0`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes/node/defaults/main.yml` (Kubespray `v2.30.0`):

```yaml
kubelet_static_pod_path: {{ kube_manifest_dir }}
```

## Compatibility

Present in the Kubespray tags `v2.29.0`–`v2.30.0`. **Removed after `v2.30.0`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes/node/defaults/main.yml` (Kubespray `v2.30.0`).
