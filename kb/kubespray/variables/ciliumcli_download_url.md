---
id: VARIABLE-CILIUMCLI_DOWNLOAD_URL
type: variable
title: ciliumcli_download_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ciliumcli_download_url
tags:
  - cilium
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "ciliumcli_download_url: github release URL for cilium-cli (unchanged expression v2.29.0-v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# ciliumcli_download_url

## Summary

`ciliumcli_download_url` is the download URL for the Cilium CLI tarball. It is a
computed expression built from `github_url`, `cilium_cli_version`, and
`image_arch`, unchanged across `v2.29.0`-`v2.31.0`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
ciliumcli_download_url: "{{ github_url }}/cilium/cilium-cli/releases/download/v{{ cilium_cli_version }}/cilium-linux-{{ image_arch }}.tar.gz"
```

The expression is identical across all four tags (line 161 in v2.29.0, 163 in
v2.29.1/v2.30.0/v2.31.0).

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: same computed expression.
- Related: `github_url`, `cilium_cli_version`, `image_arch`,
  `ciliumcli_binary_checksum`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
