---
id: VARIABLE-CRICTL_VERSION
type: variable
title: crictl_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crictl_version
tags:
  - download
  - cri
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "computed default derived from crictl_checksums and kube_major_next_version"
relations: []
---

# crictl_version

## Summary

`crictl_version` selects the version of `crictl` (the CRI command-line tool) to
download. It is not a hard-coded value: it is computed from the `crictl_checksums`
map, picking the highest known version that is lower than `kube_major_next_version`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
crictl_version: "{{ (crictl_checksums['amd64'].keys() | select('version', kube_major_next_version, '<'))[0] }}"
```

The expression is unchanged across v2.29.0-v2.31.0. The effective value depends on
the target Kubernetes version and on the entries present in `crictl_checksums`.

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: same computed expression.
- Related: `crictl_checksums`, `kube_major_next_version`, `kube_version`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
