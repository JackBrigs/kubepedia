---
id: TROUBLE-APT_RELEASE_INFO_CHANGE
type: troubleshooting
title: "Node provisioning fails at update_cache: apt refuses a mirror whose Origin/Label changed"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-08-06"
confidence: verified
aliases:
  - Failed to update apt cache
  - changed its Origin value from
  - changed its Label value from
  - This must be accepted explicitly before updates for this repository can be applied
  - apt-secure(8) manpage for details
  - Repository InRelease changed its value
  - allow-releaseinfo-change
  - kubespray fails on apt update new node
tags:
  - apt
  - ubuntu
  - debian
  - troubleshooting
  - provisioning
  - bootstrap
  - mirror
  - node
sources:
  - type: code
    path: apt-pkg/acquire-item.cc
    url: https://github.com/Debian/apt/blob/2.7.14/apt-pkg/acquire-item.cc#L1816-L1888
    note: "the check runs only when LastMetaIndexParser != nullptr (a previous InRelease is cached); Origin, Label and Codename default to AllowInfoChange=false, Version and Suite to true"
  - type: code
    path: apt-private/private-cmndline.cc
    url: https://github.com/Debian/apt/blob/2.7.14/apt-private/private-cmndline.cc#L206-L212
    note: "--allow-releaseinfo-change maps to Acquire::AllowReleaseInfoChange; per-field variants exist for Origin, Label, Version, Codename, Suite, DefaultPin"
relations:
  - type: see_also
    target: CONCEPT-UBUNTU_24_04_K8S
  - type: see_also
    target: TROUBLE-ADD_NODE_GOTCHAS
  - type: see_also
    target: PRACTICE-RUNBOOK_ADD_NODES
---

## Summary

Adding a node fails on the first Ansible task that sets `update_cache: true`, with
`Failed to update apt cache: ... changed its 'Origin' value from '' to '<new>'`.
Nothing is wrong with the node, the playbook or the network: an internal mirror was
migrated to different repository software, the new `InRelease` carries `Origin` and
`Label` fields the old one lacked, and apt treats that as a security event it will
not act on unattended. The node still holds the pre-migration metadata, so it has
something to compare against — which is exactly why a supposedly fresh node fails
while a genuinely empty one would not.

## Problem

An organisation moves its Debian/Ubuntu mirror — for example from aptly to
Artifactory or Nexus — behind an unchanged URL. Package content is intact and the
signature verifies. But `Release`/`InRelease` now declares:

```
Origin: Artifactory
Label: Artifactory
```

where it previously declared nothing. apt compares the freshly downloaded metadata
against the copy cached in `/var/lib/apt/lists/`, sees identity fields change under
a URL the administrator once trusted, and stops. The messages are emitted as errors
(`E:`), not warnings, so the Ansible `apt` module fails the task and the play halts
before a single package is installed.

Two properties make this misleading in a provisioning context:

- It looks like a node problem. It is a fleet-wide event, deferred until each host
  next runs `apt-get update`. Hosts that updated after the migration are silent;
  hosts imaged before it fail the moment they are touched.
- It looks like a Kubespray problem. Kubespray only calls the `apt` module; the
  refusal comes from apt itself and would occur under any playbook.

## Context

The guard lives in `pkgAcqMetaBase::VerifyVendor` and is entered only when a
previous metadata parser exists:

```cpp
if (TransactionManager->LastMetaIndexParser != nullptr)
```

That single condition explains the symptom pattern. A host with an empty
`/var/lib/apt/lists/` has no `LastMetaIndexParser`, accepts whatever the mirror now
declares, and provisions cleanly. A host built from a VM template snapshotted before
the migration carries the old lists inside the image, so every node cloned from that
template fails identically on its first run — including nodes created long after the
migration.

Not all fields are guarded equally:

| field       | change permitted by default | rationale in source |
|-------------|-----------------------------|---------------------|
| `Origin`    | no                          | identity of the publisher |
| `Label`     | no                          | identity of the publisher |
| `Codename`  | no                          | identity of the release |
| `Version`   | yes                         | "numbers change all the time, that is okay" |
| `Suite`     | yes                         | — |
| `DefaultPin`| no                          | silently changing pin priority breaks apt_preferences(5) |

So a mirror migration trips the guard precisely because it changes publisher
identity, while ordinary point-release churn does not.

The Ansible `apt` module has no parameter for this. Its full argument list —
visible in the `invocation.module_args` of the failing task — contains
`allow_unauthenticated`, `allow_downgrade` and `allow_change_held_packages`, but
nothing that maps to `Acquire::AllowReleaseInfoChange`. The acceptance therefore
cannot be expressed inside the failing task and must happen before it, either as a
separate play or as part of image preparation.

## Diagnostics

Confirm the diagnosis and identify which repository moved:

```bash
# what apt currently believes about the cached metadata
grep -E '^(Origin|Label|Codename|Suite):' /var/lib/apt/lists/*_InRelease

# what the mirror now declares
curl -s https://<mirror>/dists/<suite>/InRelease | head -20

# reproduce non-destructively — same error, no changes applied
sudo apt-get update
```

Determine how many hosts are exposed, before the next mass playbook run:

```bash
ansible -i <inventory> all -b -m raw \
  -a 'apt-get update -qq 2>&1 | grep -c "changed its" || true'
```

Any host answering non-zero will fail its next `update_cache: true` task.

If the count is high and the affected hosts share an OS image, inspect the image
itself — a populated `/var/lib/apt/lists/` in a golden template reproduces this on
every future node.

## Known Issues

**Fixing it per-node hides the real defect.** Accepting the change on one host
unblocks that host and leaves the fleet, and the image, untouched. Where the
organisation owns a playbook that manages repository definitions, running that
playbook is the correct remedy: it re-establishes the intended source list, and the
fix propagates by the same route as every other configuration change instead of
living in one operator's shell history.

**A stale apt cache inside a VM template is the root cause, not the mirror.** The
migration is a legitimate, one-time event; the reason it keeps resurfacing on "new"
nodes is that the image ships pre-migration metadata. Until the template is rebuilt
with `/var/lib/apt/lists/` cleared, every node cloned from it inherits the failure.

**Blanket acceptance is not a safe permanent setting.** Writing
`Acquire::AllowReleaseInfoChange "true";` into `/etc/apt/apt.conf.d/` disables the
guard for all repositories forever, including ones whose identity changes because
they were actually hijacked. The guard exists to make publisher substitution
visible; the per-field, per-run flags exist so it can be waived deliberately.

**Manual equivalents**, when no managing playbook applies:

```bash
# accept the identity change once; subsequent runs are clean
sudo apt-get update --allow-releaseinfo-change

# or discard the pre-migration metadata entirely — preferable on a template-born node
sudo rm -rf /var/lib/apt/lists/*
sudo apt-get update
```

Narrower variants exist — `--allow-releaseinfo-change-origin` and
`--allow-releaseinfo-change-label` — and are preferable when only those two fields
moved, since they leave the `Codename` guard armed.

## References

- apt `2.7.14`, `apt-pkg/acquire-item.cc` — the `VerifyVendor` release-info guard,
  the field table and the `apt-secure(8)` confirmation message
- apt `2.7.14`, `apt-private/private-cmndline.cc` — CLI flags to
  `Acquire::AllowReleaseInfoChange` configuration mapping
- `apt-secure(8)` — repository trust model the guard defends
- `apt_preferences(5)` — why a silent `DefaultPin` change is treated as unsafe
