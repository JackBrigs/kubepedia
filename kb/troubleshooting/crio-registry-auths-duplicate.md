---
id: TROUBLE-CRIO_REGISTRY_AUTHS_DUPLICATE
type: troubleshooting
title: "CRI-O: duplicate top-level auths keys make registry config invalid JSON"
status: active
kubespray_version: ">=v2.29.0 <=v2.29.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - crio-registry-auths-duplicate
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/12845
    note: "fix merged in v2.30.0 (PR #12845)"
  - type: code
    path: roles/container-engine/cri-o/templates/config.json.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/container-engine/cri-o/templates/config.json.j2
    note: "fixed file"
relations:
  - type: see_also
    target: CONCEPT-CONTAINER_MANAGER
---

# CRI-O: duplicate top-level auths keys make registry config invalid JSON

## Summary

With multiple `crio_registry_auth` entries, CRI-O's registry auth file was rendered with several top-level `auths` objects, producing invalid JSON — CRI-O then failed to pull from private registries. Fixed in **v2.30.0** (PR #12845).

## Problem

The `config.json.j2` template emitted one `{"auths": {...}}` per entry instead of merging them into a single `auths` map, so the JSON had duplicate top-level keys and image pulls from authenticated registries failed.

## Context

- Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0`.
- Confirmed via the merged PR #12845 and the tag code.

## Diagnostics

```bash
# check the generated file on a node (crio)
cat /etc/crio/auth.json 2>/dev/null | python3 -m json.tool   # invalid JSON / duplicate auths?
crictl pull <private-image>                                   # auth failure?
```

## Known Issues

Root cause fixed by PR #12845 (in `roles/container-engine/cri-o/templates/config.json.j2`). Workaround before upgrading: define a single merged `crio_registry_auth` structure, or patch the auth file by hand. The
durable fix is to upgrade to `v2.30.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/12845 — fixed in `v2.30.0`.
- `roles/container-engine/cri-o/templates/config.json.j2`.
