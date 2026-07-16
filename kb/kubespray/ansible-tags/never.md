---
id: TAG-NEVER
type: ansible_tag
title: never (special Ansible tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - never
tags:
  - ansible-tag
  - special
sources:
  - type: code
    path: playbooks/upgrade_cluster.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/upgrade_cluster.yml
    note: "opt-in tasks guarded by the never tag (run only when explicitly requested)"
relations:
  - type: see_also
    target: TAG-ALWAYS
---

# never (special Ansible tag)

## Summary

`never` is an Ansible built-in special tag: tasks tagged `never` are **skipped by
default** and run only when the operator explicitly requests that tag (or another
tag on the same task). Kubespray uses it to gate opt-in / potentially dangerous
tasks so they do not fire in a normal run.

## Context

- Ansible semantics, not Kubespray-specific — but relevant to how Kubespray's
  optional tasks behave.
- A `never`-tagged task runs only with `--tags never` or with a second, explicit
  tag attached to that task.

## Implementation

By default Ansible excludes `never`-tagged tasks. To run them, the operator passes
the tag explicitly. This lets Kubespray ship optional/rarely-wanted steps without
them executing during a routine `cluster.yml` / `upgrade-cluster.yml` run.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `never` gates opt-in tasks.
- **Standalone-run safety: n/a.** `never` is a gating mechanism, not a target you
  run on its own for a result. Contrast [[TAG-ALWAYS]].

## References

- Ansible tag semantics (special tags `always` / `never`).
- `playbooks/upgrade_cluster.yml` and role tasks using `never`.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
