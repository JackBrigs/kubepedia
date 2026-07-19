---
id: TROUBLE-RELEASE_WATCHER
type: troubleshooting
title: "release-watcher: no notifications — source/API rate limits, credentials, notifier config"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - release-watcher no notifications
  - release watcher github rate limit
  - release watcher notifier
tags:
  - troubleshooting
  - tooling
  - notifications
sources:
  - type: external
    path: release_watcher
    url: https://github.com/kaasops/release-watcher
    note: "release-watcher polls software sources and notifies on new releases; failures are source auth/rate-limit or notifier config"
relations:
  - type: see_also
    target: CONCEPT-ADDON_RELEASE_WATCHER
---

# release-watcher: no notifications — source/API rate limits, credentials, notifier config

## Summary

`release-watcher` polls upstream sources (GitHub, registries) and **notifies on new releases**. When it goes quiet it's almost always **source-side rate limiting / auth** (unauthenticated GitHub API is heavily throttled) or a **misconfigured notifier** (webhook/Slack). It holds little state; the failure is at one of the two edges.

## Problem

- No new-release notifications arrive though releases clearly happened.

## Context

- release-watcher ([[CONCEPT-ADDON_RELEASE_WATCHER]]); niche/effectively-undocumented — verify the running image tag.
- **Source rate limit/auth:** unauthenticated GitHub API is throttled; without a token, polling silently fails/backs off.
- **Notifier:** a wrong/blocked webhook means it detects releases but can't tell you.

## Diagnostics

```bash
kubectl -n <ns> logs deploy/release-watcher | tail   # 'rate limit' / 403 / notifier errors
kubectl -n <ns> get secret | grep -i release-watcher    # source token present?
```

## Known Issues

- **Rate limit — fix:** give it an authenticated source token (GitHub PAT) so polling isn't throttled.
- **Notifier — fix:** correct the webhook/Slack endpoint and ensure egress to it; test with a known release.

## References

Upstream project (see `sources`). Catalog entry [[CONCEPT-ADDON_RELEASE_WATCHER]].
