---
id: VARIABLE-NTP_TINKER_PANIC
type: variable
title: ntp_tinker_panic
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ntp_tinker_panic
tags:
  - ntp
  - preinstall
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Controls the NTP tinker panic setting; default false."
relations:
  - type: see_also
    target: TAG-PREINSTALL
---

# ntp_tinker_panic

## Summary
Controls the NTP `tinker panic` option in the managed NTP configuration. When enabled, it keeps NTP from panicking on large time offsets (useful for virtual machines). The default is `false`. Only takes effect when `ntp_manage_config` is true.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` (line 71):

```yaml
ntp_tinker_panic: false
```

The default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Only applied when `ntp_manage_config: true`. Related variables: `ntp_manage_config`, `ntp_servers`, `ntp_timezone`.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
