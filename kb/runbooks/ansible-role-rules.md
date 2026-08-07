---
id: PRACTICE-ANSIBLE_ROLE_RULES
type: best_practice
title: "Writing Ansible roles here: one task per role, prefixed variables, defaults and README mandatory"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-08-07"
confidence: verified
aliases:
  - как писать роли ansible
  - правила разработки ansible
  - devrules
  - именование ролей
  - install- префикс роли
  - переменные роли префикс
  - ansible role conventions
  - написать плейбук
tags:
  - ansible
  - conventions
  - roles
  - operations
sources:
  - type: doc
    path: ~/Desktop/work/playbook/docs/devrules.md
    note: "правила команды: одна задача на роль, обезличенность, префиксы имён, meta, README, дефолты"
  - type: doc
    path: ~/Desktop/work/playbook/roles/general/install-repo-upnp
    note: "пример разделения: install-repo-* ставит репозиторий, отдельная роль ставит пакет"
  - type: doc
    path: ~/Desktop/work/playbook/consul-reg-services.yml
    note: "домашний стиль работы с consul — HTTP API через ansible.builtin.uri, не CLI"
relations:
  - type: see_also
    target: CONCEPT-LOCAL_SOURCES
  - type: see_also
    target: PRACTICE-ANSIBLE
  - type: see_also
    target: PRACTICE-AWX
---

## Summary

The team's rules for authoring Ansible, extracted so that search reaches them before
anything gets written. The authoritative text is `playbook/docs/devrules.md`; when
the two disagree, that file wins. The short version: a role does one task, is
impersonal, ships defaults and a README, declares its dependencies, and prefixes its
variables with its own name.

## Context

Applies to anything committed to the playbook repository — new roles, changes to
existing ones, and standalone playbooks. It does not apply to Kubespray's own roles,
which follow upstream conventions.

## Implementation

**Scope of a role.**

- One role does one concrete task.
- Installing software and deploying its configuration are **two** roles, never one.
- A package that needs its own repository gets a separate repository-install role,
  declared as a dependency in `meta`.
- A role is impersonal: anything that varies between projects is generated from
  variables, never hardcoded.

**Naming.**

| kind of role | convention | example |
|---|---|---|
| installs a package | `install-` prefix | `install-filebeat` |
| deploys configuration | named after the package | `filebeat` |
| installs a repository | `install-repo-` prefix | `install-repo-elastic` |

Files and directories: lowercase Latin only.

**Variables.**

- Defaults live in the role's `defaults/main.yml`, not in the play.
- Variable names carry the role name as a prefix, so two roles cannot collide.
- Variables whose values commit to something irreversible (writing into a database,
  for example) are left **empty** by default, and the README states the minimum set
  that must be declared.
- `group_vars/all` is not a place for role variables — only a role default or a
  group-scoped variable. Deviating requires a very strong reason.
- Group variables applicable to a role are split into a file named after the role,
  so they can be found.

**Mandatory parts.** `meta/main.yml` with dependencies; `README.md` describing what
the role does and the minimum variables required. Starting from `ansible-galaxy
init` gives the layout for free.

**Size.** No more than 10–20 actions in a task file; beyond that, split into
logically related files.

**Local idioms not stated in devrules but visible in the repository:** consul is
driven through its HTTP API with `ansible.builtin.uri` (see
`consul-reg-services.yml`), not through the `consul` CLI in `shell`.

## Known Issues

**A tag is not a mode switch.** Tags select a subset of tasks. Expressing "do X" and
"undo X" as two tags means a run without tags performs both — the play reports
success while the node ends up where it started. State belongs in a variable,
validated with `assert`.

**`command` does not run a shell.** Quotes written inside its argument string are
passed through literally: `command: consul maint -reason="planned"` sends the quotes
as part of the value. Either use a module, or `shell` if a shell is genuinely needed.

**`hosts: all` relying on `--limit` is a loaded gun.** A forgotten limit runs the
play against the whole inventory. Take the target as a required variable
(`hosts: "{{ target | mandatory }}"`) or name a real group.

**Presence of a binary is not a health check.** On a reinstalled node the file can
remain while the agent is dead. Probe the service, not the filesystem.

**A fixed `pause` is not verification.** Waiting a minute and hoping is weaker, and
usually slower, than polling the actual state with `until`/`retries`.

**`become: true` plus `sudo` inside the command is double escalation.** Choose one.

## References

- `playbook/docs/devrules.md` — the authoritative rules
- `playbook/CONTRIBUTING.md` — commit subject/body conventions for these repositories
- `playbook/consul-reg-services.yml` — worked example of the HTTP-API idiom
