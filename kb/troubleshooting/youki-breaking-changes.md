---
id: TROUBLE-YOUKI_BREAKING_CHANGES
type: troubleshooting
title: "youki: declared breaking changes by release"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.2.0 <=0.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - youki breaking changes
  - youki upgrade broke
  - youki action required upgrade
  - what breaks upgrading youki
tags:
  - upgrade
  - breaking-change
  - youki
sources:
  - type: docs
    path: youki-dev/youki release notes — entries marked breaking / action required
    url: https://github.com/youki-dev/youki/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# youki: declared breaking changes by release

## Summary

**13 behaviour changes** the project itself marked as breaking or action-required, across
6 releases from 0.2.0 to 0.6.0. These are not defects: they work as designed and still break
a configuration that worked yesterday. An upgrade crossing any of them needs a decision, not just a
rollout.

## Problem

The upgrade itself usually succeeds. The damage shows up afterwards — a setting silently ignored, a
default flipped, an API version withdrawn, a variable that must now be set explicitly.

## Context

### 0.2.0

- Use syscall type to delay the creation of syscall struct. by @yihuaf in https://github.com/containers/youki/pull/2155
- Refactor the libcgroups interface by @yihuaf in https://github.com/containers/youki/pull/2168
- refactored executor and executor manager by @yihuaf in https://github.com/containers/youki/pull/2186
- Refactored the Executor interface yet again by @yihuaf in https://github.com/containers/youki/pull/2230
- Rename the rootless struct to UserNamespaceConfig by @YJDoc2 in https://github.com/containers/youki/pull/2257
- move the validation logic into executor by @yihuaf in https://github.com/containers/youki/pull/2258

### 0.3.3

- Improve error reporting and logging by @YJDoc2 in https://github.com/containers/youki/pull/2705

### 0.4.0

- Rename to improve readability by @utam0k in https://github.com/containers/youki/pull/2818

### 0.5.0

- libcontainer: use OwnedFd as console_socket in ContainerBuilder by @abel-von in https://github.com/youki-dev/youki/pull/2966

### 0.5.6

- Upgrade to Rust 1.89 and Edition 2024 by @utam0k in https://github.com/youki-dev/youki/pull/3244

### 0.6.0

- fix hooks order by @saku3 in https://github.com/youki-dev/youki/pull/3256
- mount info provider by @CheatCodeSam in https://github.com/youki-dev/youki/pull/3280
- Use oci spec container process state for seccomp by @nayuta723 in https://github.com/youki-dev/youki/pull/3330


## Diagnostics

```bash
# which version is actually deployed
kubectl get nodes -o wide
helm list -A
```

Cross the list above against the range you are moving through, not only the target version.

## Known Issues

Entries are verbatim from upstream release notes and filtered mechanically: lines shorter than
45 characters and duplicates are dropped, because section headings and list fragments reach the
extractor looking like entries. If a release you care about appears empty here, read its notes
upstream before concluding that nothing changed.

## References

- Upstream releases of `youki-dev/youki`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/youki.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
