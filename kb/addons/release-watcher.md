---
id: CONCEPT-ADDON_RELEASE_WATCHER
type: concept
title: "release-watcher — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: probable
aliases:
  - release-watcher
tags:
  - addons
  - tooling
sources:
  - type: docs
    path: rycus86/release-watcher (closest public match)
    url: https://github.com/rycus86/release-watcher
    note: "only public release-watcher; ships chart 0.0.2, not 0.0.9"
relations:
  - type: see_also
    target: TROUBLE-RELEASE_WATCHER
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# release-watcher — addon

## Summary

`release-watcher` (chart **0.0.9** in the inventory) watches software sources for new
releases and notifies. **Version caveat:** no public `release-watcher` chart at `0.0.9`
exists — the closest public project (`rycus86/release-watcher`) ships only chart **0.0.2**.
The inventory's `0.0.9` is therefore **likely an internal/private chart** — `confidence:
probable`; treat as inventory-level until the source repo is confirmed.

## Context

- Class: upstream tool, likely internal packaging; catalog row in [[CONCEPT-ADDON_CATALOG]].

## Implementation

- No verifiable upstream chart at 0.0.9. The closest public match is a hobby project
  (`rycus86/release-watcher`, single commit, chart 0.0.2, appVersion "1.0"). Confirm the
  actual source repo with whoever pinned `0.0.9`.

## Configuration

- Configuration is unknown without the actual chart — record the source repo and values when
  identified.

## Compatibility

- **Kubernetes range:** **unverified** (no confirmable source). Assumed workable across
  1.29–1.35 as a simple watcher/notifier.
- **CVEs:** none found for the closest public project.

## Upstream issues & upgrade notes (mined 2026-07-19)

**⚠ Version/identity caveat:** the inventory's `release-watcher` chart at **0.0.9** does **not** clearly map to a maintained upstream — the closest public project is **`rycus86/release-watcher`** ("watcher for new releases", with artifacthub/helmhub providers), which is niche/low-activity and not obviously the same packaging. **Verify what image/chart you actually deploy** before relying on it. Operationally, source-API rate-limit/auth and notifier config are the failure points ([[TROUBLE-RELEASE_WATCHER]]).

## Older-version CVEs & security history (mined 2026-07-19)

release-watcher is niche/low-activity with no notable CVE record; older-version exposure is base-image/dependency CVEs and the handling of the **source API token** (a leaked GitHub PAT is the sensitive asset). Verify the actual image (the 0.0.9 pin doesn't map to a clear maintained upstream) and scope the token minimally.

## Guides & how-to (official)

- **Repo:** https://github.com/rycus86/release-watcher
- **How to upgrade:** niche/low-activity — **verify the actual image** (the 0.0.9 pin doesn't cleanly map to this upstream) before upgrading. Provide an authenticated source token (avoid rate-limit) and scope it minimally.
## References

- rycus86/release-watcher (closest public match, above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
