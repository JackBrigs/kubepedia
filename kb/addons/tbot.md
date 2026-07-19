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
    target: TROUBLE-TBOT
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

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** beyond pinned **18.7.4** — Teleport is at **18.10.0**; several **security fixes** landed since 18.7.4 (tbot is a security agent, so stay current):
- **18.9.2:** **SSRF in AWS app access**, AWS STS session-duration capping.
- **18.10.0:** fixed Slack-plugin credential exposure in URLs.
- **18.8.3:** tightened Device Trust signature handling; restricted symlink traversal in file transfers.
- **17.7.26 (older line):** Kubernetes API proxy access now requires a new `proxy` verb (RBAC change).
- Recommend **≥18.9.2** and tracking the 18.x patch stream. Cert-renewal troubleshooting: [[TROUBLE-TBOT]].

## Older-version CVEs & security history (mined 2026-07-19)

tbot ships as part of **Teleport**, which has a **regular security-advisory cadence (HCSEC)** — an older tbot/Teleport misses those. Concretely, versions **below 18.9.2** miss the AWS-app-access SSRF fix and other 18.x hardening (see the upgrade section); older 17.x/16.x lines carry their own Teleport CVEs. Track the supported Teleport 18.x patch stream — this is a security agent, so currency matters most here.

## Guides & how-to (official)

- **Docs:** https://goteleport.com/docs/machine-id/ ; **deploy on k8s:** https://goteleport.com/docs/machine-id/deployment/kubernetes/
- **How to upgrade:** upgrade the tbot image to match the Teleport cluster version (keep within one Teleport minor); **track the 18.x patch stream — this is a security agent** (get ≥18.9.2 for the AWS SSRF fix).
## References

- tbot `Chart.yaml` (v18.7.4), Teleport upgrading overview (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
