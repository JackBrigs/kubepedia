---
id: ROLE-DOWNLOAD
type: role
title: download
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - download
tags:
  - role
sources:
  - type: code
    path: roles/download
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/download
    note: "download role"
relations:
  - type: see_also
    target: TAG-DOWNLOAD
---

# download

## Summary

Fetches and caches all binaries, archives and container images the cluster needs, and extracts them. Central to offline installs.

## Implementation

Task files under `roles/download/tasks/`. Invoked from the playbooks under the
corresponding run-tag (see [[TAG-DOWNLOAD]]).

## Configuration

Driven by variables in `roles/kubespray_defaults` (see [[ROLE-KUBESPRAY_DEFAULTS]]) and the role's own `defaults/`.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.

## References

- `roles/download/` (tag `v2.31.0` `1c9add4`).
