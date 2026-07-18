---
id: VARIABLE-KUBERNETES_USER_MANIFESTS_PATH
type: variable
title: kubernetes_user_manifests_path
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kubernetes_user_manifests_path
tags:
  - win-nodes
  - kubernetes-patch
  - variable
sources:
  - type: code
    path: roles/win_nodes/kubernetes_patch/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/win_nodes/kubernetes_patch/defaults/main.yml
    note: "default: {{ ansible_env.HOME }}/kube-manifests"
relations: []
---
<!-- generated: variable-stub -->

# kubernetes_user_manifests_path

## Summary

Kubespray variable `kubernetes_user_manifests_path` — default `{{ ansible_env.HOME }}/kube-manifests`. Defined in `roles/win_nodes/kubernetes_patch/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/win_nodes/kubernetes_patch/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
kubernetes_user_manifests_path: {{ ansible_env.HOME }}/kube-manifests
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/win_nodes/kubernetes_patch/defaults/main.yml` (Kubespray `v2.31.0`).
