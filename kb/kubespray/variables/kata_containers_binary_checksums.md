---
id: VARIABLE-KATA_CONTAINERS_BINARY_CHECKSUMS
type: variable
title: kata_containers_binary_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kata_containers_binary_checksums
tags:
  - kata
  - download
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Map of Kata Containers static tarball checksums by arch and version"
relations: []
---

# kata_containers_binary_checksums

## Summary
A nested map of SHA-256 checksums for the Kata Containers static tarball, keyed by architecture (`amd64`, `arm64`) and then by Kata version. Consumed by `kata_containers_binary_checksum` and by `kata_containers_version` (which takes the first amd64 key as the default version).

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml`. The set of indexed versions differs between tags:

| Tag(s) | amd64 / arm64 version keys |
|--------|----------------------------|
| v2.29.0, v2.29.1 | 3.7.0, 3.6.0, 3.5.0, 3.4.0, 3.3.0, 3.2.0 |
| v2.30.0, v2.31.0 | 3.7.0, 3.6.0, 3.5.0 |

In every tag the first key is `3.7.0` (e.g. amd64 `3.7.0: sha256:bebf218cafdc082476c7dabbcc5439aee6a41d6dda24dd3cfffbe0a6ae94e23d`), so the derived default `kata_containers_version` stays `3.7.0`. v2.30.0 dropped the older 3.4.0/3.3.0/3.2.0 entries.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Backing data for `kata_containers_binary_checksum` and `kata_containers_version`. Relevant only when `kata_containers_enabled: true`.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
