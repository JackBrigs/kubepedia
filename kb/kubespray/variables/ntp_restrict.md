---
id: VARIABLE-NTP_RESTRICT
type: variable
title: ntp_restrict
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ntp_restrict
tags:
  - ntp
  - preinstall
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "List of hosts allowed NTP access; default 127.0.0.1 and ::1"
relations:
  - type: see_also
    target: TAG-PREINSTALL
---

# ntp_restrict

## Summary
List of hosts to which NTP access is restricted in the managed NTP configuration. Default is `["127.0.0.1", "::1"]`. Only takes effect when `ntp_manage_config` is true.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` (line 51) as a list, unchanged across v2.29.0-v2.31.0:

```yaml
ntp_restrict:
  - "127.0.0.1"
  - "::1"
```

## Compatibility
Kubespray v2.29.0 through v2.31.0. Only applied when `ntp_manage_config: true`. Related: `ntp_manage_config`, `ntp_servers`, `ntp_filter_interface`.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
