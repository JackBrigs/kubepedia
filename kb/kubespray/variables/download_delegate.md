---
id: VARIABLE-DOWNLOAD_DELEGATE
type: variable
title: download_delegate
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - download_delegate
tags:
  - download
  - delegation
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Host used to store downloads in download_run_once mode"
relations: []
---

# download_delegate

## Summary
Selects the host that stores downloaded files/images in `download_run_once` mode: `localhost` when `download_localhost` is true, otherwise the first host in the `kube_control_plane` group.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as a computed Jinja expression:

```yaml
download_delegate: "{% if download_localhost %}localhost{% else %}{{ groups['kube_control_plane'][0] }}{% endif %}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `download_localhost` and the `kube_control_plane` inventory group; related to `download_run_once`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
