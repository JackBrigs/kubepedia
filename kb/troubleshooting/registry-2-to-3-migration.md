---
id: TROUBLE-REGISTRY_2_TO_3_MIGRATION
type: troubleshooting
title: "Registry (distribution) 2→3: config/driver breaks"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.0.0 <=3.1.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - docker registry v3 upgrade
  - distribution 3.0 config path
  - registry oss swift driver removed
  - registry config /etc/distribution
tags:
  - troubleshooting
  - registry
  - distribution
  - upgrade
sources:
  - type: docs
    path: distribution v3.0.0 release notes
    url: https://github.com/distribution/distribution/releases/tag/v3.0.0
    note: "oss/swift drivers removed; default config path /etc/distribution/config.yml"
relations:
  - type: see_also
    target: COMPONENT-REGISTRY
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# Registry (distribution) 2→3: config/driver breaks

## Summary

The CNCF **distribution** registry **v3.0.0** (2025-04-03) changed the **default config path**
and **removed the `oss` and `swift` storage drivers**. Upgrading from v2.x (the base ships
`2.8.1`) fails to start if the config isn't found at the new path or uses a dropped driver.

## Problem

- Registry pod crashloops after the v3 image bump: config file not found.
- Startup fails because the storage backend uses the removed **oss** (Alibaba) or **swift**
  (OpenStack) driver.
- Tooling importing `manifest.Versioned` breaks (deprecated).

## Context

- Applies to distribution **3.0.0–3.1.1** (base: registry 2.8.1 — [[COMPONENT-REGISTRY]]).

## Diagnostics

- **Default config path changed to `/etc/distribution/config.yml`** — mount your config there
  (or set the explicit path flag). The old `/etc/docker/registry/config.yml` is no longer the
  default.
- **`oss` and `swift` storage drivers removed** — migrate the backend to a supported driver
  (filesystem, s3, gcs, azure) before upgrading.
- `client` is no longer a standalone package; `manifest.Versioned` is deprecated in favour of
  `oci.Versioned` — update any code depending on them.

## Known Issues

- If upgrading from a v2.x that used release candidates, review the v2.x deprecations first —
  some were finalized in v3.

## References

- distribution v3.0.0 release notes (above); component: [[COMPONENT-REGISTRY]]; horizon:
  [[CONCEPT-UPGRADE_HORIZON]].
