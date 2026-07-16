---
id: VARIABLE-ETCD_EXPERIMENTAL_WATCH_PROGRESS_NOTIFY_INTERVAL
type: variable
title: etcd_experimental_watch_progress_notify_interval
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd_experimental_watch_progress_notify_interval
tags:
  - etcd
sources:
  - type: code
    path: roles/etcd_defaults/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd_defaults/defaults/main.yml
    note: "Defines default etcd_experimental_watch_progress_notify_interval: 5s"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd_experimental_watch_progress_notify_interval

## Summary
Sets the interval at which etcd sends watch progress notifications to clients. Default is `5s`.

## Implementation
Defined in `roles/etcd_defaults/defaults/main.yml` as:

```yaml
etcd_experimental_watch_progress_notify_interval: 5s
```

Consumed in `roles/etcd/templates/etcd.env.j2` where it is written as `ETCD_EXPERIMENTAL_WATCH_PROGRESS_NOTIFY_INTERVAL={{ etcd_experimental_watch_progress_notify_interval }}`. The default value `5s` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Applies to the etcd environment configuration on hosts in the `etcd` group.

## References
- roles/etcd_defaults/defaults/main.yml
- roles/etcd/templates/etcd.env.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
