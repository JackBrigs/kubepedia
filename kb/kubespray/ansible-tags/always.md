---
id: TAG-ALWAYS
type: ansible_tag
title: always (special Ansible tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - always
tags:
  - ansible-tag
  - special
sources:
  - type: code
    path: playbooks/boilerplate.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/boilerplate.yml
    note: "boilerplate/fact tasks tagged always so they run regardless of --tags"
relations:
  - type: see_also
    target: TAG-NEVER
---

# always (special Ansible tag)

## Summary

`always` is an Ansible built-in special tag: tasks tagged `always` run on **every**
invocation, regardless of which `--tags` are selected, unless explicitly excluded
with `--skip-tags always`. Kubespray uses it for boilerplate that must always run
(common tasks, fact gathering) so that targeted `--tags X` runs still have the
context they need.

## Context

- Not a Kubespray-specific behavior — it is Ansible semantics — but it matters
  when running Kubespray with `--tags`, because `always` tasks still execute.
- Applied to setup/boilerplate plays (e.g. `boilerplate.yml`,
  `internal_facts.yml`) and other must-run tasks.

## Implementation

Ansible runs an `always`-tagged task whenever the play runs, even if the user
passes `--tags something_else`. To skip them, the operator must pass
`--skip-tags always`. Kubespray relies on this so that fact-gathering and common
preparation are present for any tag-scoped run.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: `always` is used on boilerplate/fact tasks.
- **Standalone-run safety: n/a.** `always` is not something you target on its own;
  it modifies how other `--tags` runs behave. Contrast [[TAG-NEVER]].

## References

- Ansible tag semantics (special tags `always` / `never`).
- `playbooks/boilerplate.yml`, `playbooks/internal_facts.yml` — `always` usage.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
