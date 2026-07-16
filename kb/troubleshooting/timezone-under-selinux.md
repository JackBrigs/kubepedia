---
id: TROUBLE-TIMEZONE_UNDER_SELINUX
type: troubleshooting
title: "Setting timezone fails under SELinux"
status: active
kubespray_version: ">=v2.29.0 <=v2.29.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - timezone-under-selinux
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/12436
    note: "fix merged in v2.30.0 (PR #12436)"
  - type: code
    path: roles/kubernetes/preinstall/tasks/0081-ntp-configurations.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubernetes/preinstall/tasks/0081-ntp-configurations.yml
    note: "fixed file"
relations: []
---

# Setting timezone fails under SELinux

## Summary

Configuring the node timezone (`ntp_timezone`) failed on SELinux-enforcing hosts because the timezone symlink operation was blocked. Fixed in **v2.30.0** (PR #12436).

## Problem

The NTP/timezone task did not account for SELinux; the fix handles SELinux context so the timezone can be set. Affects RHEL-family nodes with SELinux enforcing.

## Context

- Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0`.
- Confirmed via merged PR #12436 and the tag code.

## Diagnostics

```bash
getenforce                                  # Enforcing?
timedatectl | grep "Time zone"
journalctl | grep -i "avc: denied" | tail   # SELinux denial during timezone set
```

## Known Issues

Fixed by PR #12436 (in `roles/kubernetes/preinstall/tasks/0081-ntp-configurations.yml`). Workaround before upgrading: temporarily set SELinux permissive or set the timezone manually, or upgrade to v2.30.0. Durable fix: upgrade to `v2.30.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/12436 — fixed in `v2.30.0`.
- `roles/kubernetes/preinstall/tasks/0081-ntp-configurations.yml`.
