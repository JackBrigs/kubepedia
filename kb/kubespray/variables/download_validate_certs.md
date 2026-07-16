---
id: VARIABLE-DOWNLOAD_VALIDATE_CERTS
type: variable
title: download_validate_certs
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - download_validate_certs
tags:
  - download
  - tls
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Default download_validate_certs: true"
relations:
  - type: see_also
    target: TAG-DOWNLOAD
---

# download_validate_certs

## Summary
Controls SSL/TLS certificate validation of the `get_url` module when downloading files. Set to `false` to disable validation (workaround for an Ansible https-proxy bug); checksum validation is still performed. Default: `true`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `download_validate_certs: true`. The value is unchanged across v2.29.0, v2.29.1, v2.30.0 and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Affects file downloads via `get_url`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
