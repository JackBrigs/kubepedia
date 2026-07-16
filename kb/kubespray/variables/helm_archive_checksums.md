---
id: VARIABLE-HELM_ARCHIVE_CHECKSUMS
type: variable
title: helm_archive_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - helm_archive_checksums
tags:
  - helm
  - download
  - checksum
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Map of Helm archive checksums keyed by architecture then version"
relations: []
---

# helm_archive_checksums

## Summary
A nested map of SHA256 checksums for Helm release archives, keyed first by CPU architecture (`arm`, `arm64`, `amd64`, ...) and then by Helm version string. It also implicitly defines the default `helm_version` (the first key of the `amd64` map).

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml` as a `helm_archive_checksums:` dictionary, e.g. in v2.31.0:

```yaml
helm_archive_checksums:
  arm:
    3.18.4: sha256:34ea88aef15fd822e839da262176a36e865bb9cfdb89b1f723811c0cc527f981
    ...
```

It is present in all of v2.29.0-v2.31.0; the individual version/checksum entries are refreshed per tag while the structure is unchanged.

## Compatibility
Kubespray v2.29.0-v2.31.0. Related: `helm_archive_checksum`, `helm_version`, `helm_download_url`.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
