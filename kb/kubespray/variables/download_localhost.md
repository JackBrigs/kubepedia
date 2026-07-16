---
id: VARIABLE-DOWNLOAD_LOCALHOST
type: variable
title: download_localhost
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - download_localhost
tags:
  - download
  - offline
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    lines: "42 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "download_localhost: false (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: VARIABLE-DOWNLOAD_RUN_ONCE
  - type: see_also
    target: TAG-DOWNLOAD
---

# download_localhost

## Summary

`download_localhost` makes the Ansible control host act as the delegate that
downloads artifacts (then distributes them), rather than a cluster node. The
default is `false`. It is typically used together with
[[VARIABLE-DOWNLOAD_RUN_ONCE]].

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/download.yml` (`false`,
unchanged across all four tags). When `true` (and `download_run_once` is set), the
control machine pulls images/binaries and pushes them to the nodes — useful when
the control host has internet access but the nodes do not.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `false`.
- Effective in combination with `download_run_once: true`; see [[TAG-DOWNLOAD]].

## References

- `roles/kubespray_defaults/defaults/main/download.yml` — default (L40 in v2.29.0,
  L42 in v2.29.1–v2.31.0).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
