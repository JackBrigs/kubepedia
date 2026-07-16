---
id: VARIABLE-REDHAT_OS_FAMILY_EXTENSIONS
type: variable
title: redhat_os_family_extensions
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - redhat_os_family_extensions
tags:
  - os-detection
  - preinstall
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "List of additional distributions treated as part of the RedHat OS family"
relations: []
---

# redhat_os_family_extensions

## Summary
List of extra Linux distributions that Kubespray treats as belonging to the RedHat OS family (in addition to Ansible's own detection). Defaults to `UnionTech` and `UniontechOS`.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` at line 102:

```yaml
redhat_os_family_extensions:
  - "UnionTech"
  - "UniontechOS"
```

Unchanged across v2.29.0-v2.31.0 (line 102 in all four tags).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Used during preinstall OS-family classification so that the listed distributions receive RedHat-family handling.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
