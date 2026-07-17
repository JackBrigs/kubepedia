---
id: TROUBLE-CRIO_SHORT_NAME_REGISTRY
type: troubleshooting
title: "CRI-O: short-name image pull fails (unqualified-search-registries)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - crio short-name resolution
  - unqualified-search-registries
  - short-name did not resolve to an alias
  - crio_registries kubespray
tags:
  - troubleshooting
  - cri-o
  - registry
  - runtime
sources:
  - type: code
    path: roles/container-engine/cri-o/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/cri-o/tasks/main.yml
    note: "crio_registries → registries.conf.d/01-unqualified.conf"
relations:
  - type: see_also
    target: COMPONENT-CRI_O
  - type: see_also
    target: TROUBLE-IMAGEPULLBACKOFF
---

# CRI-O: short-name image pull fails (unqualified-search-registries)

## Summary

On **CRI-O**, pulling an image by a **short name** (e.g. `nginx` instead of
`docker.io/library/nginx`) fails: `short-name "nginx" did not resolve to an alias and no
unqualified-search registries are defined`. CRI-O (unlike Docker) does **not** implicitly assume
`docker.io` — you must configure **unqualified-search-registries**.

## Problem

- `ErrImagePull`: `short-name ... did not resolve to an alias and no unqualified-search
  registries are defined` (or a short-name prompt in strict mode).

## Context

- Applies to Kubespray **v2.29.0–v2.31.0** with CRI-O ([[COMPONENT-CRI_O]]). Kubespray writes
  registry config to **`/etc/containers/registries.conf.d/`** from the **`crio_registries`**
  variable, including `01-unqualified.conf` for entries flagged `unqualified: true`.

## Diagnostics

- **Best fix — use fully-qualified image names** in manifests (`docker.io/library/nginx:1.27`,
  `registry.example.com/app:tag`) — explicit and unambiguous.
- **Or configure unqualified search** via Kubespray: add entries to **`crio_registries`** with
  `unqualified: true` (writes `01-unqualified.conf` = `unqualified-search-registries = [...]`),
  then re-run. Verify on the node: `cat /etc/containers/registries.conf.d/01-unqualified.conf`
  and `crictl pull nginx`.
- **Short-name mode:** CRI-O's `short-name-mode` (permissive/enforcing) governs whether an
  ambiguous short name errors — enforcing requires an alias or a single search registry.

## Known Issues

- This is a **CRI-O-vs-containerd difference** — manifests that "just worked" on containerd
  (which defaults to docker.io) break on CRI-O. Prefer fully-qualified names for portability.

## References

- CRI-O role `registries.conf.d` handling (v2.31.0, above); component: [[COMPONENT-CRI_O]];
  pull triage: [[TROUBLE-IMAGEPULLBACKOFF]].
