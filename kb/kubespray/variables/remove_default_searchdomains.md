---
id: VARIABLE-REMOVE_DEFAULT_SEARCHDOMAINS
type: variable
title: remove_default_searchdomains
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - remove_default_searchdomains
tags:
  - dns
  - preinstall
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Toggle to drop default DNS search domains from resolv.conf; default false"
relations: []
---

# remove_default_searchdomains

## Summary
Boolean toggle controlling whether Kubespray removes the default DNS search domains when generating the host `resolv.conf`. Defaults to `false`.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` at line 18:

```yaml
remove_default_searchdomains: false
```

Unchanged across v2.29.0-v2.31.0 (line 18 in all four tags).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Affects DNS/resolv.conf generation in the preinstall role; related to `resolvconf_mode`.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
