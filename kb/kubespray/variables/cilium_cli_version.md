---
id: VARIABLE-CILIUM_CLI_VERSION
type: variable
title: cilium_cli_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_cli_version
tags:
  - cilium
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "cilium_cli_version derived from first key of ciliumcli_binary_checksums['amd64'] (unchanged v2.29.0-v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# cilium_cli_version

## Summary

`cilium_cli_version` is the version of the Cilium CLI (`cilium-cli`) Kubespray
downloads. It is not a hard-coded literal but a computed expression derived from
the checksum map. The expression is unchanged across `v2.29.0`-`v2.31.0`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
cilium_cli_version: "{{ (ciliumcli_binary_checksums['amd64'] | dict2items)[0].key }}"
```

It takes the first key of the `ciliumcli_binary_checksums['amd64']` dictionary as
the CLI version. The expression is identical across all four tags (line 118 in
v2.29.0; line 120 in v2.29.1/v2.30.0/v2.31.0); the resolved value depends on the
checksum map contents in each tag.

## Compatibility

- Kubespray `v2.29.0`-`v2.31.0`: same computed expression.
- Related: `ciliumcli_binary_checksums`, `ciliumcli_download_url`,
  `ciliumcli_binary_checksum`.

## References

- `roles/kubespray_defaults/defaults/main/download.yml`
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
