---
id: VARIABLE-GITHUB_URL
type: variable
title: github_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - github_url
tags:
  - download
  - registry
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Base URL of GitHub used to construct release/download URLs; default https://github.com"
relations: []
---

# github_url

## Summary
Base URL of GitHub used as a building block when composing download URLs for binaries and releases hosted on GitHub. Default value is `https://github.com`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
github_url: https://github.com
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Override it to fetch GitHub-hosted assets from an internal mirror in offline or air-gapped installations.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
