---
id: CONCEPT-ADDON_GITLAB_AGENT
type: concept
title: "GitLab Agent for Kubernetes (agentk) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.33 <=1.35"
component_version: "18.11.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - gitlab-agent
  - agentk
  - gitlab kas agent
tags:
  - addons
  - gitops
  - gitlab
sources:
  - type: code
    path: gitlab-agent Chart.yaml
    url: https://gitlab.com/gitlab-org/charts/gitlab-agent/-/raw/v2.26.0/Chart.yaml
    note: "no kubeVersion; chart 2.26.0 → agentk 18.11.0"
  - type: docs
    path: GitLab Agent docs (supported K8s)
    url: https://docs.gitlab.com/user/clusters/agent/
    note: "supported K8s 1.33–1.35; ≥3 production minors"
relations:
  - type: see_also
    target: TROUBLE-GITLAB_AGENT
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# GitLab Agent for Kubernetes (agentk) — addon

## Summary

The GitLab Agent (`agentk`) connects a cluster to GitLab (KAS) for pull-based GitOps, CI
access and cluster management. The inventory runs two charts: **2.22.1 → agentk 18.7.1** and
**2.26.0 → agentk 18.11.0** (chart uses an independent `2.x` scheme; `appVersion` tracks
GitLab **18.x**).

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].

## Implementation

- Chart→app (chart≠app): 2.22.1 → **18.7.1**, 2.26.0 → **18.11.0**. Chart `kubeVersion`:
  **none** at both tags.

## Configuration

- **agentk must track GitLab within ±1 minor** — an agentk↔KAS version mismatch breaks
  registration.
- Chart releases **lag** GitLab releases, so a matching chart version may not exist yet for
  the newest GitLab.
- Built-in pull-based GitOps was deprecated (16.2, removal targeted 17.0) — migrate to Flux.

## Compatibility

- **Kubernetes range:** not chart-defined; GitLab docs currently list **1.33, 1.34, 1.35** as
  supported (policy: ≥3 production minors, added ~3 months after release). Within 1.29–1.35
  only **1.33–1.35** are currently supported.
- **Breaking changes:** AutoFlow modules removed in agentk v18.7.0; 18.8–18.11 agentk
  CHANGELOG is "No changes" (passthrough bumps).
- **CVEs:** none found for agentk 18.7–18.11 (OSV empty). (Ubuntu-packaged `gitlab-agent` OSV
  hits are a different package.)

## References

- gitlab-agent Chart.yaml (2.22.1/2.26.0), GitLab Agent docs (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
