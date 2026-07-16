---
id: VARIABLE-CLOUD_RESOLVER
type: variable
title: cloud_resolver
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cloud_resolver
tags:
  - dns
  - preinstall
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Defaults to an empty list []"
relations: []
---

# cloud_resolver

## Summary
List of upstream DNS resolver addresses used by the preinstall role when
generating the host `resolv.conf` (typically the cloud provider's resolvers).
Default is an empty list `[]`, meaning no cloud resolvers are added.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` as:

```yaml
cloud_resolver: []
```

The default value `[]` is unchanged across v2.29.0, v2.29.1, v2.30.0, and
v2.31.0 (located at line 7 of that file in every tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Part of the preinstall/resolvconf handling;
related variables in the same file include `nameservers` and
`disable_host_nameservers`.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
