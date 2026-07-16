---
id: TROUBLE-SSH_BASTION_CONFIG_NAME_TYPO
type: troubleshooting
title: "bastion-ssh-config: misspelled variable ssh_bastion_confing__name"
status: active
kubespray_version: ">=v2.29.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ssh-bastion-config-name-typo
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/13046
    note: "fix merged in v2.31.0 (PR #13046)"
  - type: code
    path: roles/bastion-ssh-config/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/bastion-ssh-config/defaults/main.yml
    note: "fixed file"
relations: []
---

# bastion-ssh-config: misspelled variable ssh_bastion_confing__name

## Summary

Setting the bastion SSH config name had no effect because the role's variable was misspelled (`ssh_bastion_confing__name`), so user overrides did not apply. Fixed in **v2.31.0** (PR #13046).

## Problem

A typo in the variable name meant any override of the intended `ssh_bastion_config_name` was ignored. The fix renames it to `ssh_bastion_config_name`.

## Context

- Affected Kubespray: `>=v2.29.0 <=v2.30.0`. Fixed in: `v2.31.0`.
- Confirmed via merged PR #13046 and the tag code.

## Diagnostics

```bash
grep -r ssh_bastion_config inventory/    # if you set this, it had no effect before the fix
```

## Known Issues

Fixed by PR #13046 (in `roles/bastion-ssh-config/defaults/main.yml`). Workaround before upgrading: use the misspelled name to match the old code, or upgrade to v2.31.0 and use `ssh_bastion_config_name`. Durable fix: upgrade to `v2.31.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/13046 — fixed in `v2.31.0`.
- `roles/bastion-ssh-config/defaults/main.yml`.
