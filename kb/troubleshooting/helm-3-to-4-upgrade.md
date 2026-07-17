---
id: TROUBLE-HELM_3_TO_4_UPGRADE
type: troubleshooting
title: "Helm 3→4 upgrade: CLI/SDK/plugin breaks"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=4.0.0 <=4.2.3"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - helm 4 breaking changes
  - helm 3 to 4 migration
  - helm 4 plugin broke
  - helm 4 server side apply
tags:
  - troubleshooting
  - helm
  - upgrade
sources:
  - type: docs
    path: Helm v4.0.0 release notes
    url: https://github.com/helm/helm/releases/tag/v4.0.0
    note: "first stable Helm 4 (2025-11-12); backward-incompatible CLI/SDK; SSA; plugin redesign"
relations:
  - type: see_also
    target: COMPONENT-HELM
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# Helm 3→4 upgrade: CLI/SDK/plugin breaks

## Summary

Helm **4.0.0** (stable 2025-11-12) is a major release with **backward-incompatible** CLI flags,
output and SDK changes. Most **charts** (apiVersion `v2`) keep working, but scripts that parse
CLI output, custom **plugins/post-renderers**, and SDK integrations can break. The base ships
Helm **3.18.4** (Kubespray), so this is the upgrade-horizon jump.

## Problem

- Scripts/CI that parse `helm` CLI output or rely on specific flags fail.
- Custom plugins or **post-renderers** stop working.
- Go programs embedding the Helm SDK don't compile / behave differently.
- Install/upgrade behaviour shifts because **server-side apply** is now used.

## Context

- Applies to Helm **4.0.0–4.2.3** (base: Helm 3.18.4 — [[COMPONENT-HELM]]).
- Scope is smaller than the v2→v3 jump — "the majority of workflows remain compatible."

## Diagnostics

- **CLI flags/output changed** — audit any automation that scrapes `helm` output or passes
  removed flags; re-test against 4.x.
- **Server-side apply is now supported/used** — this can change how upgrades reconcile fields
  vs 3.x client-side apply; watch for field-manager conflicts on resources also managed by
  other controllers.
- **Plugin system redesigned** (WebAssembly-based; **post-renderers are now plugins**) — old
  binary plugins and post-renderer wiring must be migrated.
- **Charts:** apiVersion `v2` charts (the majority) continue to install/upgrade — test, don't
  assume. (An experimental `v3` chart API is coming.)
- **SDK:** the Go API changed (slog logging, multiple chart API versions) — pin and update
  embedding code deliberately.

## Known Issues

- Because SSA changes field ownership, resources co-managed by operators may see field-manager
  conflicts on first 4.x upgrade — plan a test upgrade in staging.

## References

- Helm v4.0.0 release notes (above); component: [[COMPONENT-HELM]]; horizon:
  [[CONCEPT-UPGRADE_HORIZON]].
