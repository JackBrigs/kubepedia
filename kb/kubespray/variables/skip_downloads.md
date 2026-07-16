---
id: VARIABLE-SKIP_DOWNLOADS
type: variable
title: skip_downloads
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - skip_downloads
tags:
  - download
  - offline
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    lines: "22 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "skip_downloads: false (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: TAG-DOWNLOAD
---

# skip_downloads

## Summary

`skip_downloads` disables the download step entirely. The default is `false`. When
`true`, Kubespray does not fetch any binaries or images and expects them to be
present already — the core switch for fully offline / air-gapped runs.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` (`false`,
unchanged across all four tags). It gates the `download` role at the playbook
level (`when: "not skip_downloads"`, see [[TAG-DOWNLOAD]]).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `false`.
- Set `true` only when artifacts are pre-staged (e.g. via a local registry/mirror
  and a populated binary cache); otherwise later roles fail on missing files.

## References

- `roles/kubespray_defaults/defaults/main/download.yml` — default (line shifts by
  tag; L20 in v2.29.0, L22 in v2.29.1–v2.31.0).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
