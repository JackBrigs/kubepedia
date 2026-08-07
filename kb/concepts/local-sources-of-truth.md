---
id: CONCEPT-LOCAL_SOURCES
type: concept
title: "Local sources of truth: team documents that outrank anything remembered"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-08-07"
confidence: verified
aliases:
  - правила разработки ansible
  - devrules
  - где лежат конвенции команды
  - как пишут роли в команде
  - соглашения репозитория плейбуков
  - team conventions
  - local documentation register
tags:
  - conventions
  - ansible
  - awx
  - consul
  - inventory
  - documentation
sources:
  - type: doc
    path: ~/Desktop/work/playbook/docs/devrules.md
    note: "125 строк: правила написания ролей, именование, переменные, meta, README"
  - type: doc
    path: ~/Desktop/work/playbook/docs/consul.md
    note: "229 строк: consul в нашей среде — серверы на front, клиенты везде, DC, регистрация, query"
  - type: doc
    path: ~/Desktop/work/playbook/docs/awx_common.md
    note: "первичная настройка сервера через AWX и через CLI"
relations:
  - type: see_also
    target: PRACTICE-ANSIBLE_ROLE_RULES
  - type: see_also
    target: PRACTICE-AWX
  - type: see_also
    target: PRACTICE-ANSIBLE
---

## Summary

Several areas of this environment are governed by documents that live in the team's
own repositories, not in upstream documentation and not in anything a model
remembers. Writing an Ansible role, a maintenance procedure or a consul change
without reading them produces work that is plausible and wrong in the specific ways
this team already decided against. This document is the register: what exists, where
it lives, and what it governs.

## Context

The failure this prevents is concrete and has happened: an Ansible role was written
from general knowledge while `docs/devrules.md` — 125 lines of explicit team rules —
sat unread in a repository already open in the same session. The result broke five
separate rules at once (no role structure, variables without the role-name prefix,
defaults in the play instead of `defaults/`, no `meta` dependency, no README).

General Ansible knowledge is not wrong; it is simply not what this team agreed to.
The distance between "correct Ansible" and "correct here" is exactly the content of
these files.

## Implementation

The register. Paths are on the operator's workstation; the repositories are the
authority, this document only points at them.

| document | governs |
|---|---|
| `playbook/docs/devrules.md` | how roles are written, named, and parameterised |
| `playbook/docs/consul.md` | consul topology, registration, DC/query mechanics |
| `playbook/docs/awx_common.md` | first-time server setup through AWX and via CLI |
| `playbook/docs/wipe_old_servers.md` | decommissioning procedure |
| `playbook/docs/clone_awx_inventory.md` | cloning an AWX inventory |
| `playbook/docs/domain_setup_auth.md` | domain join and authentication |
| `playbook/CONTRIBUTING.md` | commit subject/body conventions, sign-off, scope prefix |
| `kube-inventory/README.md` | inventory repository layout |
| GitLab wiki `ops/ansible/playbook` | the full wiki these documents are extracted from |

**The rule this register exists to enforce:** before writing a role, a playbook, a
maintenance procedure, or anything that will be committed to those repositories,
read the governing document first. The repositories are usually already open — the
cost of checking is seconds, and the cost of not checking is work that has to be
thrown away.

**Extraction, not duplication.** Rules worth surfacing through search are recorded
as their own documents in this base (see the relations). The team files stay
authoritative: when they disagree with a document here, they win and the document
here is corrected.

## Known Issues

**These documents are not versioned against anything.** `docs/consul.md` carries a
timestamp from 2019 in its original section and describes a configuration file path
(`/etc/consul.json`) that no longer matches the running fleet (`/etc/consul.d/`).
Read them for intent and conventions; verify specifics against running systems.

**The GitLab wiki is the upstream of these files.** Each begins with a link back to
it. A file in `docs/` may lag behind the wiki.

**Absence of a rule is not permission.** Where these documents are silent — error
handling, idempotence, check mode — general Ansible practice applies, but the
choice should be stated rather than assumed.

## References

- `playbook/docs/` — the documents above, extracted from the team GitLab wiki
- `playbook/CONTRIBUTING.md` — commit conventions
- GitLab wiki `ops/ansible/playbook` — authoritative upstream of `docs/`
