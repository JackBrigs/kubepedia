---
id: VARIABLE-CRICTL_CHECKSUMS
type: variable
title: crictl_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crictl_checksums
tags:
  - checksums
  - crictl
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "SHA256 checksum table for crictl release archives keyed by arch then version"
relations: []
---

# crictl_checksums

## Summary
Static lookup table of SHA256 checksums for crictl (CRI CLI) release archives. It is a nested dict keyed first by CPU architecture (`arm64`, `amd64`, `ppc64le`, ...) and then by crictl version, used to verify the downloaded archive. It has no scalar default.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml` (line 2 in all four tags), e.g. in v2.31.0:

```yaml
crictl_checksums:
  arm64:
    1.35.0: sha256:519071de89b64c43e2a1661bb5489c6c3fd5e9e5fcef75e50e542b0c891f1118
    ...
  amd64:
    1.35.0: sha256:2e141e5b22cb189c40365a11807d69b76b9b3caced89fac2f4ec879408ce2177
    ...
```

Present in all four tags at the same path and line. The table content grows over tags as new crictl versions and checksums are added.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Consumed together with `crictl_version`, `crictl_download_url` and `crictl_binary_checksum` (the per-version/arch selected value).

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
