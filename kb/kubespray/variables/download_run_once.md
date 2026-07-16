---
id: VARIABLE-DOWNLOAD_RUN_ONCE
type: variable
title: download_run_once
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - download_run_once
tags:
  - download
  - offline
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    lines: "31 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "download_run_once: false (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: TAG-DOWNLOAD
  - type: see_also
    target: VARIABLE-DOWNLOAD_LOCALHOST
---

# download_run_once

## Summary

`download_run_once` makes Kubespray download images/binaries **once** (on the
first node or the delegate) and then distribute them to the other nodes, instead
of every node downloading independently. The default is `false`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` (`false`,
unchanged across all four tags). When `true`, downloads are performed on a single
host and pushed out; combined with [[VARIABLE-DOWNLOAD_LOCALHOST]] this supports
bastion-style and bandwidth-constrained installs.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `false`.
- Useful when nodes have limited or no direct internet access but can receive
  artifacts from a delegate; part of the download/offline story with
  [[TAG-DOWNLOAD]].

## References

- `roles/kubespray_defaults/defaults/main/download.yml` — default (L29 in v2.29.0,
  L31 in v2.29.1–v2.31.0).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
