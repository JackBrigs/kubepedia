---
id: VARIABLE-AUTO_RENEW_CERTIFICATES_SYSTEMD_CALENDAR
type: variable
title: auto_renew_certificates_systemd_calendar
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - auto_renew_certificates_systemd_calendar
tags:
  - certificates
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "systemd OnCalendar schedule for certificate auto-renewal"
relations: []
---

# auto_renew_certificates_systemd_calendar

## Summary
systemd `OnCalendar` expression that defines when the control plane certificate auto-renewal timer fires. Default: `Mon *-*-1,2,3,4,5,6,7 03:00:00` (first Monday of each month at 03:00).

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
auto_renew_certificates_systemd_calendar: "Mon *-*-1,2,3,4,5,6,7 03:00:00"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Only effective when `auto_renew_certificates: true`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
