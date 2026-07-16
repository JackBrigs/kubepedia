---
id: VARIABLE-DISABLE_FAPOLICYD
type: variable
title: disable_fapolicyd
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - disable_fapolicyd
tags:
  - preinstall
  - security
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Defines disable_fapolicyd with default true"
relations: []
---

# disable_fapolicyd

## Summary
Controls whether the fapolicyd service (file access policy daemon, present on some RHEL-family systems) is disabled during preinstall. Default is `true`, meaning Kubespray disables fapolicyd, which can otherwise block Kubernetes binaries.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` (line 111 in all four tags):

```yaml
disable_fapolicyd: true
```

The default value `true` is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Handled by the `kubernetes/preinstall` role; relevant primarily on RHEL/CentOS/Rocky-family hosts where fapolicyd may be installed.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
