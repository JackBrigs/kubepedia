---
id: TAG-ASSERTS
type: ansible_tag
title: asserts (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - asserts
  - --tags asserts
tags:
  - ansible-tag
  - validation
sources:
  - type: code
    path: roles/kubernetes/preinstall/tasks/main.yml
    lines: "20"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/tasks/main.yml
    note: "verify-settings included under the asserts tag"
  - type: code
    path: roles/download/tasks
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/download/tasks
    note: "check_pull_required.yml / prep_download.yml also carry asserts"
relations:
  - type: see_also
    target: TAG-PREINSTALL
---

# asserts (Ansible run-tag)

## Summary

`asserts` runs Kubespray's precondition/sanity-check tasks — the inventory and
environment `assert` tasks that fail fast on invalid configuration before anything
is changed. Running `--tags asserts` performs only these checks.

## Context

- **Roles:** `kubernetes/preinstall` (settings verification) and `download`
  (pull-requirement checks) attach the `asserts` tag to their assertion tasks.
- Useful as a dry-run-style validation pass over the inventory.

## Implementation

In `roles/kubernetes/preinstall/tasks/main.yml` the settings-verification tasks
are tagged `asserts`:

```yaml
    - asserts
```

The `download` role tags its `check_pull_required.yml` / `prep_download.yml`
precondition tasks the same way. These are `assert`-based checks (e.g. supported
versions, required variables, sane settings) that stop the run on failure.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `asserts` groups the precondition checks.
- **Standalone-run safety: safe.** Read-only assertions; a good way to validate an
  inventory without applying changes (`--tags asserts`).

## References

- `roles/kubernetes/preinstall/tasks/main.yml:20`
- `roles/download/tasks/` (`check_pull_required.yml`, `prep_download.yml`)
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
