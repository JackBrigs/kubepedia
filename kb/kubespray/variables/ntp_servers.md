---
id: VARIABLE-NTP_SERVERS
type: variable
title: ntp_servers
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ntp_servers
tags:
  - ntp
  - preinstall
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "List of NTP servers written to the NTP config; default is four *.pool.ntp.org entries with iburst."
relations: []
---

# ntp_servers

## Summary
Defines the list of NTP servers used when NTP configuration is managed by Kubespray. Only takes effect when `ntp_manage_config` is true. The default is a list of four public pool servers, each with the `iburst` option.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` (line 44). Default value:

```yaml
ntp_servers:
  - "0.pool.ntp.org iburst"
  - "1.pool.ntp.org iburst"
  - "2.pool.ntp.org iburst"
  - "3.pool.ntp.org iburst"
```

The same default is exposed (commented) in `inventory/sample/group_vars/all/all.yml`. The default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Only applied when `ntp_manage_config: true`. Related variables: `ntp_manage_config`, `ntp_restrict`, `ntp_timezone`, `ntp_tinker_panic`.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
