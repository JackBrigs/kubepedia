---
id: VARIABLE-NTP_DRIFTFILE
type: variable
title: ntp_driftfile
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ntp_driftfile
tags:
  - ntp
  - preinstall
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Path to the NTP drift file; computed from ntp_package"
relations:
  - type: see_also
    target: TAG-PREINSTALL
---

# ntp_driftfile

## Summary
Filesystem path to the NTP drift file written into the managed NTP configuration. Computed from `ntp_package`: `/var/lib/ntpsec/ntp.drift` when the package is `ntpsec`, otherwise `/var/lib/ntp/ntp.drift`. Only takes effect when `ntp_manage_config` is true.

## Implementation
Defined in `roles/kubernetes/preinstall/defaults/main.yml` (line 64) as a Jinja expression, unchanged across v2.29.0-v2.31.0:

```yaml
ntp_driftfile: >-
      {% if ntp_package == "ntpsec" -%}
      /var/lib/ntpsec/ntp.drift
      {%- else -%}
      /var/lib/ntp/ntp.drift
      {%- endif -%}
```

## Compatibility
Kubespray v2.29.0 through v2.31.0. Only applied when `ntp_manage_config: true`. Related: `ntp_package`, `ntp_manage_config`, `ntp_enabled`.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
