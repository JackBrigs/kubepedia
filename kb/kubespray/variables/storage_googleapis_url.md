---
id: VARIABLE-STORAGE_GOOGLEAPIS_URL
type: variable
title: storage_googleapis_url
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - storage_googleapis_url
tags:
  - download
  - mirror
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Base URL for Google Cloud Storage used when building download URLs"
relations: []
---

# storage_googleapis_url

## Summary
Base URL for Google Cloud Storage (`https://storage.googleapis.com`). It is used
as the host prefix when constructing download URLs for artifacts hosted on GCS.
Can be overridden to point at a mirror in offline/proxied environments.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
storage_googleapis_url: https://storage.googleapis.com
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by download-URL variables that pull
artifacts from Google Cloud Storage.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
