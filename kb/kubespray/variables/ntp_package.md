---
id: VARIABLE-NTP_PACKAGE
type: variable
title: ntp_package
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ntp_package
tags:
  - ntp
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "NTP package to install; computed from ansible_os_family"
relations:
  - type: see_also
    target: TAG-PREINSTALL
---

# ntp_package

## Summary
Name of the package providing NTP functionality that Kubespray installs. Computed from the OS family: `chrony` on RedHat-family systems, otherwise `ntp`. Accepted values are `ntp`, `ntpsec`, or `chrony`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a Jinja expression, unchanged across v2.29.0-v2.31.0 (line number shifts: 796 in v2.29.0/v2.29.1, 799 in v2.30.0, 818 in v2.31.0):

```yaml
ntp_package: >-
      {% if ansible_os_family == "RedHat" -%}
      chrony
      {%- else -%}
      ntp
      {%- endif -%}
```

## Compatibility
Kubespray v2.29.0 through v2.31.0. The chosen package also affects `ntp_driftfile` (ntpsec uses a different drift path). Related: `ntp_enabled`, `ntp_manage_config`, `ntp_driftfile`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
