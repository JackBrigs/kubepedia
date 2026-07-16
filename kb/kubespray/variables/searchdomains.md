---
id: VARIABLE-SEARCHDOMAINS
type: variable
title: searchdomains
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - searchdomains
tags:
  - dns
  - network
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "List of additional DNS search domains; empty by default"
relations: []
---

# searchdomains

## Summary
List of additional DNS search domains applied to the cluster nodes. Empty by default (`[]`).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
searchdomains: []
```

The default is unchanged across v2.29.0-v2.31.0 (line 160 in v2.29.0/v2.29.1, 161 in v2.30.0, 158 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relates to node/cluster DNS configuration alongside `nameservers` and DNS mode settings.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
