---
id: TROUBLE-OPENEULER_METALINK_URL
type: troubleshooting
title: "openEuler: broken package metalink URL during bootstrap"
status: active
kubespray_version: "v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - openeuler-metalink-url
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/13144
    note: "fix merged in v2.31.0 (PR #13144)"
  - type: code
    path: roles/bootstrap_os/tasks/openEuler.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/bootstrap_os/tasks/openEuler.yml
    note: "fixed file"
relations:
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# openEuler: broken package metalink URL during bootstrap

## Summary

OS bootstrap on openEuler failed because the package repository metalink URL was incorrect, so package installation could not proceed. Fixed in **v2.31.0** (PR #13144).

## Problem

The openEuler bootstrap task used a broken metalink URL; the fix corrects the repo configuration. openEuler-specific.

## Context

- Affected Kubespray: `v2.30.0`. Fixed in: `v2.31.0`.
- Confirmed via merged PR #13144 and the tag code.

## Diagnostics

```bash
# on an openEuler node, dnf/yum fails to reach the repo during bootstrap-os
dnf repolist 2>&1 | tail
```

## Known Issues

Fixed by PR #13144 (in `roles/bootstrap_os/tasks/openEuler.yml`). Workaround before upgrading: fix the openEuler repo URL manually, or upgrade to v2.31.0. Durable fix: upgrade to `v2.31.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/13144 — fixed in `v2.31.0`.
- `roles/bootstrap_os/tasks/openEuler.yml`.
