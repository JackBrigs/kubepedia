---
id: VARIABLE-KREW_ROOT_DIR
type: variable
title: krew_root_dir
status: active
kubespray_version: ">=v2.27.0 <=v2.27.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - krew_root_dir
tags:
  - kubernetes-apps
  - krew
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/krew/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.27.1/roles/kubernetes-apps/krew/defaults/main.yml
    note: "default: /usr/local/krew"
relations: []
---
<!-- generated: variable-stub -->

# krew_root_dir

## Summary

Kubespray variable `krew_root_dir` — default `/usr/local/krew`. Defined in `roles/kubernetes-apps/krew/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.27.1` of the indexed range. **Removed after `v2.27.1`** (absent in later tags of the range). (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/krew/defaults/main.yml` (Kubespray `v2.27.1`):

```yaml
krew_root_dir: /usr/local/krew
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.27.1`. **Removed after `v2.27.1`** (absent in later tags of the range). Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/krew/defaults/main.yml` (Kubespray `v2.27.1`).
