---
id: CONCEPT-ADDON_TBOT
type: concept
title: "tbot (Teleport Machine ID) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "18.7.4"
verified_at: "2026-07-17"
confidence: probable
aliases:
  - tbot
  - teleport machine id
  - teleport bot
tags:
  - addons
  - security
  - identity
  - teleport
sources:
  - type: code
    path: examples/chart/tbot/Chart.yaml
    url: https://raw.githubusercontent.com/gravitational/teleport/v18.7.4/examples/chart/tbot/Chart.yaml
    note: "chart version==appVersion (Teleport version); no kubeVersion"
  - type: docs
    path: Teleport upgrading overview
    url: https://goteleport.com/docs/upgrading/overview/
    note: "no major-skip; version skew rules"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# tbot (Teleport Machine ID) — addon

## Summary

`tbot` is Teleport's Machine ID agent — it issues short-lived certificates to workloads for
Teleport-brokered access. **Version caveat:** the inventory's **`18.7.3` does not exist** —
the Teleport 18.7 patch line skips it (real tags 18.7.2, 18.7.4). Confirm the deployed tag;
this doc uses the nearest real release **18.7.4** (`confidence: probable` on the exact pin).

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].

## Implementation

- The tbot chart pins `version == appVersion` (the Teleport version) via a YAML anchor. Chart
  `kubeVersion`: **none**.

## Configuration

- Version-skew rules: **Auth (newest) ≥ Proxy ≥ agents/tbot**; a server rejects clients newer
  than itself. Upgrade order: Auth → Proxy → agents/tbot last.
- You **cannot skip a major** — step through each (e.g. 16 → 17 → 18).

## Compatibility

- **Kubernetes range:** **unverified** — Teleport publishes no supported-K8s policy and the
  chart sets no `kubeVersion`. Assumed workable across 1.29–1.35.
- **CVEs:** none affecting 18.x. CVE-2025-49825 / GHSA-8cqv-pj7f-pwpc (auth bypass) caps at
  17.x → 18.x not affected.

## References

- tbot `Chart.yaml` (v18.7.4), Teleport upgrading overview (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
