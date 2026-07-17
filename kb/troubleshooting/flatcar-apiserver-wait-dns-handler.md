---
id: TROUBLE-FLATCAR_APISERVER_WAIT_DNS
type: troubleshooting
title: "Flatcar: apiserver wait skipped after DNS handler caused flakiness"
status: active
kubespray_version: "v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - flatcar-apiserver-wait-dns-handler
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/13063
    note: "fix merged in v2.31.0 (PR #13063)"
  - type: code
    path: roles/kubernetes/preinstall/handlers/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/handlers/main.yml
    note: "fixed file"
relations:
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# Flatcar: apiserver wait skipped after DNS handler caused flakiness

## Summary

On Flatcar (and Fedora CoreOS) the API-server wait was excluded after the resolvconf/DNS handler ran, leading to flaky runs where later steps proceeded before the API server was reachable. Fixed in **v2.31.0** (PR #13063).

## Problem

The wait handler excluded Flatcar/FCOS and used a Flatcar-specific notify channel; the fix removes the exclusion and unifies the notify channel so the apiserver wait runs on those OSes too.

## Context

- Affected Kubespray: `v2.30.0`. Fixed in: `v2.31.0`.
- Confirmed via merged PR #13063 and the tag code.

## Diagnostics

```bash
# on Flatcar nodes: intermittent failures right after DNS/resolvconf changes, before apiserver is up
journalctl -u kubelet -n 40 --no-pager
```

## Known Issues

Fixed by PR #13063 (in `roles/kubernetes/preinstall/handlers/main.yml`). Workaround before upgrading: re-run the playbook (often transient), or upgrade to v2.31.0 for the consistent wait. Durable fix: upgrade to `v2.31.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/13063 — fixed in `v2.31.0`.
- `roles/kubernetes/preinstall/handlers/main.yml`.
