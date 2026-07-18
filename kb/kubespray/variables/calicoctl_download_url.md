---
id: VARIABLE-CALICOCTL_DOWNLOAD_URL
type: variable
title: calicoctl_download_url
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - calicoctl_download_url
tags:
  - kubespray-defaults
  - variable
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "default: {{ github_url }}/projectcalico/calico/releases/download/v{{ calico_…"
relations: []
---
<!-- generated: variable-stub -->

# calicoctl_download_url

## Summary

Kubespray variable `calicoctl_download_url` — default `{{ github_url }}/projectcalico/calico/releases/download/v{{ calico_…`. Defined in `roles/kubespray_defaults/defaults/main/download.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` (Kubespray `v2.31.0`):

```yaml
calicoctl_download_url: {{ github_url }}/projectcalico/calico/releases/download/v{{ calico_…
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubespray_defaults/defaults/main/download.yml` (Kubespray `v2.31.0`).
