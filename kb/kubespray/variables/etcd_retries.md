---
id: VARIABLE-ETCD_RETRIES
type: variable
title: etcd_retries
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_retries
tags:
  - etcd
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Number of loop retries used by etcd tasks; default 4"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_retries

## Summary
Number of loop retries used by etcd-related tasks (e.g. waiting for etcd/health operations). Default is `4`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as `etcd_retries: 4` (line 89 in v2.29.0/v2.29.1, line 88 in v2.30.0/v2.31.0). The value `4` is unchanged across v2.29.0-v2.31.0; only the line number shifted due to surrounding edits.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Related etcd tuning variables in the same defaults file include `etcd_max_wals`.

## References
- roles/etcd_defaults/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
