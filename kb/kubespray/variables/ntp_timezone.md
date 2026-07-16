---
id: VARIABLE-NTP_TIMEZONE
type: variable
title: ntp_timezone
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ntp_timezone
tags:
  - ntp
  - preinstall
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Timezone to set on the server; default empty string means the timezone is left unchanged."
relations: []
---

# ntp_timezone

## Summary
Sets the timezone for the target hosts (e.g. `Etc/UTC`, `Etc/GMT-8`). The default is an empty string, which means the timezone is not changed.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` (line 77):

```yaml
ntp_timezone: ""
```

The accompanying comment states: "Set the timezone for your server. eg: 'Etc/UTC','Etc/GMT-8'. If not set, the timezone will not change." The default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `ntp_servers`, `ntp_manage_config`, `ntp_tinker_panic`.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
