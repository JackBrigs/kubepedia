---
id: VARIABLE-COREDNS_VERSION
type: variable
title: coredns_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - coredns_version
tags:
  - coredns
  - versions
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "CoreDNS image version, derived from coredns_supported_versions[kube_major_version]"
relations:
  - type: see_also
    target: COMPONENT-COREDNS
---

# coredns_version

## Summary
The CoreDNS image version deployed by Kubespray. It is not hard-coded but
derived from the Kubernetes minor version via the `coredns_supported_versions`
map, so its effective value depends on the target Kubernetes release.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as the same
computed expression across all four tags:

```yaml
coredns_version: "{{ coredns_supported_versions[kube_major_version] }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0; the
effective value changes only because the underlying `coredns_supported_versions`
map changes between tags (see that variable's document).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Depends on `kube_major_version`
and `coredns_supported_versions`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
