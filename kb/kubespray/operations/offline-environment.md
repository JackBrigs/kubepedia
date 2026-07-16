---
id: PRACTICE-OFFLINE_ENVIRONMENT
type: best_practice
title: Offline / air-gapped deployment
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: verified
aliases:
  - offline environment
  - air-gapped
tags:
  - offline
  - operations
sources:
  - type: docs
    path: docs/operations/offline-environment.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/offline-environment.md
    note: "artifacts to pre-stage and mirror services required for air-gapped installs"
relations:
  - type: see_also
    target: VARIABLE-SKIP_DOWNLOADS
  - type: see_also
    target: VARIABLE-DOWNLOAD_RUN_ONCE
  - type: see_also
    target: TAG-DOWNLOAD
---

# Offline / air-gapped deployment

## Summary

When nodes have no direct internet access, the artifacts Kubespray downloads must
be pre-staged in an internet-connected environment and served from local mirrors.
Kubespray then pulls everything from those mirrors instead of upstream.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- Artifacts to obtain in advance:
  - static files (zips and binaries),
  - OS packages (rpm/deb),
  - container images used by Kubespray,
  - optional: Python packages (if the OS lacks the versions in `requirements.txt`),
  - optional: Helm chart files (only if `helm_enabled=true`).

## Implementation

Stand up these local services and point Kubespray at them:

- an **HTTP reverse proxy / mirror** (`files_repo`) for static files and binaries,
- an internal **Yum/Deb repository** for OS packages,
- an internal **container image registry** populated with all Kubespray images,
- optional: an internal **PyPI** server and an internal **Helm** registry.

Generate the artifact lists with `contrib/offline/generate_list.sh`; helper tooling
lives under `contrib/offline/`. Tip: mirror using the original domains as top-level
directories in `files_repo` (`github.com/`, `dl.k8s.io/`, `storage.googleapis.com/`,
`get.helm.sh/`). For Cilium, also mirror the Helm index and chart archive.

This works together with the download controls: [[VARIABLE-SKIP_DOWNLOADS]],
[[VARIABLE-DOWNLOAD_RUN_ONCE]], and the [[TAG-DOWNLOAD]] step.

> Security note: `files_repo` credentials can be exposed by the download task when
> `unsafe_show_logs` is true — keep it disabled in CI/automation.

## Compatibility

- Verified against `v2.31.0` docs; the offline model (pre-stage artifacts + local
  mirrors) is stable across the indexed range.

## References

- `docs/operations/offline-environment.md` (tag `v2.31.0` `1c9add4`).
- `contrib/offline/` — `generate_list.sh` and offline tooling.
