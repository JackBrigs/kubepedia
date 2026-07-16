---
id: VARIABLE-CILIUMCLI_BINARY_CHECKSUM
type: variable
title: ciliumcli_binary_checksum
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ciliumcli_binary_checksum
tags:
  - cilium
  - download
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "ciliumcli_binary_checksum looked up from ciliumcli_binary_checksums by arch and cli version (unchanged expression v2.29.0-v2.31.0)"
relations: []
---

# ciliumcli_binary_checksum

## Summary

`ciliumcli_binary_checksum` is the expected checksum of the downloaded Cilium CLI
binary, looked up from the checksum map by architecture and CLI version. The
lookup expression is unchanged across `v2.29.0`-`v2.31.0`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
ciliumcli_binary_checksum: "{{ ciliumcli_binary_checksums[image_arch][cilium_cli_version] }}"
```

The expression is identical across all four tags (line 189 in v2.29.0, 191 in
v2.29.1/v2.30.0/v2.31.0). It indexes `ciliumcli_binary_checksums` by `image_arch`
and `cilium_cli_version`; the resolved value depends on the checksum map contents
in each tag.

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: same computed expression.
- Related: `ciliumcli_binary_checksums`, `cilium_cli_version`, `image_arch`,
  `ciliumcli_download_url`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
