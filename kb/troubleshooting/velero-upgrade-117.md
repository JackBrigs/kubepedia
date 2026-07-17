---
id: TROUBLE-VELERO_UPGRADE_117
type: troubleshooting
title: "Velero 1.17 upgrade: CRD / sequential-version errors"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.17.0 <=1.18.2"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - velero 1.17 upgrade
  - velero crd update
  - velero must be on 1.16 first
  - velero restic kopia migration
tags:
  - troubleshooting
  - velero
  - backup
  - upgrade
sources:
  - type: docs
    path: Velero upgrade-to-1.17
    url: https://velero.io/docs/main/upgrade-to-1.17/
    note: "must be on 1.16.x first; CRD update; image sync"
relations:
  - type: see_also
    target: CONCEPT-ADDON_VELERO
  - type: see_also
    target: CONCEPT-VELERO
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# Velero 1.17 upgrade: CRD / sequential-version errors

## Summary

Upgrading Velero to **1.17** fails or behaves oddly if you jumped versions or skipped the CRD
update. You must be on **1.16.x first**, apply the **CRD schema update**, and update all Velero
images together.

## Problem

- Backups/restores fail or the controller crashloops after the chart bump to 1.17.
- New CRD fields missing / schema validation errors.
- Restores report fake "completed" notifications, or backups queue up.

## Context

- Applies to Velero **1.17.0–1.18.2** (owner runs chart 11.4.0 / app 1.17.1 —
  [[CONCEPT-ADDON_VELERO]]; operational hub [[CONCEPT-VELERO]]).

## Diagnostics

- **Be on Velero 1.16.x before upgrading to 1.17** — otherwise do sequential upgrades, do not
  skip.
- **Apply the CRD schema update:**
  `velero install --crds-only --dry-run -o yaml | kubectl apply -f -`.
- **Update the Velero deployment, plugin, and node-agent images together** — a mismatch
  causes subtle failures.
- Restic uploader is legacy — consider the optional `uploader-type` migration restic→kopia.

## Known Issues

- 1.17.1 fixes the prior failure modes: fake completion notifications from repeated
  PodVolumeRestore updates (#9365); schedule-controller queue build-up; VolumeSnapshot-field
  races in multi-threaded backups; backupPVC attaching to the source node (#9229).

## References

- Velero upgrade-to-1.17 doc (above); addon: [[CONCEPT-ADDON_VELERO]]; horizon:
  [[CONCEPT-UPGRADE_HORIZON]].
