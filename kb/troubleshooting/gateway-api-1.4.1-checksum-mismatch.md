---
id: TROUBLE-GATEWAY_API_1_4_1_CHECKSUM_MISMATCH
type: troubleshooting
title: "Gateway API v1.4.1: download fails due to a checksum mismatch"
status: active
kubespray_version: "v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - gateway api 1.4.1 checksum mismatch
tags:
  - gateway-api
  - download
sources:
  - type: github_pr
    url: https://github.com/kubernetes-sigs/kubespray/pull/13006
    note: "Fix Gateway API v1.4.1 unexpected checksum change"
relations: []
---

# Gateway API v1.4.1: download fails due to a checksum mismatch

## Summary
With `gateway_api_enabled: true`, installing or upgrading to v2.30.0 fails at the `download` stage: the checksum of the Gateway API v1.4.1 `standard-install.yaml` manifest does not match. Kubespray expects `sha256:daa2999…` but the actually downloaded artifact has a different hash (`73b91b7…`). Fixed in v2.31.0.

## Problem
With `gateway_api_enabled: true`, installation or upgrade to v2.30.0 fails at the `download` stage because the pinned checksum for the Gateway API v1.4.1 `standard-install.yaml` manifest no longer matches the downloaded artifact.

## Context
- Affected versions: v2.30.0 (when `gateway_api_enabled: true`).
- Fixed versions: v2.31.0 (master). The backport merged into the release-2.30 branch (to ship in a future v2.30.1 — not yet released at time of this entry).
- Trigger: `gateway_api_enabled: true` while downloading the Gateway API v1.4.1 manifest.

## Diagnostics
- `roles/kubespray_defaults/defaults/main/download.yml:145` — `gateway_api_version` resolves to **1.4.1** (first key of `gateway_api_standard_crds_checksums.no_arch`).
- `roles/kubespray_defaults/vars/main/checksums.yml:1390` — `1.4.1: sha256:daa2999f0978ba3e43b65fec179f82a1a690649da10aa5c7c5871165477368f8` (the expected hash that stopped matching).

## Known Issues
Root cause: the upstream Gateway API v1.4.1 release artifact was rewritten AFTER the v2.30.0 tag was cut, so the checksum baked into Kubespray became invalid.

Fix: PR #13006 "Fix Gateway API v1.4.1 unexpected checksum change" (master → v2.31.0), backport to the release-2.30 branch PR #13010. Issue #13122.

Workaround on v2.30.0: pin `gateway_api_version: "1.4.0"` in inventory (the 1.4.0 artifact is unaffected), or disable `gateway_api_enabled`.

## References
- https://github.com/kubernetes-sigs/kubespray/pull/13006
- Migrated from Kubepedia 0.1.0 cache: gateway-api-1.4.1-checksum-mismatch-v2.30.0.md
