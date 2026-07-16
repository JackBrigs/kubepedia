---
id: VARIABLE-CILIUMCLI_BINARY_CHECKSUMS
type: variable
title: ciliumcli_binary_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ciliumcli_binary_checksums
tags:
  - cilium
  - checksum
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Nested map arch -> cilium_cli_version -> sha256 checksum for the cilium-cli binary"
relations: []
---

# ciliumcli_binary_checksums

## Summary
Nested mapping of SHA256 checksums for the `cilium-cli` binary, keyed by CPU architecture and then by cilium-cli version. It drives both `cilium_cli_version` (defaulted to the first `amd64` key) and `ciliumcli_binary_checksum` (`ciliumcli_binary_checksums[image_arch][cilium_cli_version]`).

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml`:

```yaml
ciliumcli_binary_checksums:
  arm64:
    ...: sha256:...
  amd64:
    ...: sha256:...
```

The structure (arch -> version -> `sha256:...`) is stable across tags, but the set of versions grows between tags as new cilium-cli releases are added. The top `amd64` key (which becomes the default `cilium_cli_version`) changes per tag:

| Tag | Top amd64 version |
|-----|-------------------|
| v2.29.0 | 1.33.0 |
| v2.29.1 | 1.33.0 |
| v2.30.0 | 1.34.0 |
| v2.31.0 | 1.35.0 |

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `cilium_cli_version` and `ciliumcli_binary_checksum` in `roles/kubespray_defaults/defaults/main/download.yml`.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- roles/kubespray_defaults/defaults/main/download.yml (consumers)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
