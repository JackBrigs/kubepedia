---
id: TROUBLE-DOWNLOAD_FAILS
type: troubleshooting
title: "Download fails during deploy (binary/image/checksum)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - download failed kubespray
  - checksum mismatch download
  - failed to download binary
  - download_retries
  - download_validate_certs
  - download_force_cache
  - image pull during deploy fails
tags:
  - troubleshooting
  - download
  - offline
  - deploy
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "download_retries / download_validate_certs / download_force_cache / download_run_once (tag v2.31.0)"
  - type: code
    path: inventory/sample/group_vars/all/offline.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/inventory/sample/group_vars/all/offline.yml
    note: "files_repo / registry_host / *_image_repo mirror overrides (tag v2.31.0)"
relations:
  - type: see_also
    target: PRACTICE-OFFLINE_ENVIRONMENT
  - type: see_also
    target: TROUBLE-IMAGE_PULL_RATE_LIMIT
  - type: see_also
    target: TROUBLE-CONTAINERD_REGISTRY_CONFIG
---

# Download fails during deploy (binary/image/checksum)

## Summary

During a run Kubespray downloads binaries (kubeadm/kubelet/kubectl/etcd/cni…) and
container images. A failure here — network timeout, TLS error, HTTP 403/429, or a
**checksum mismatch** — aborts the play. The cause is almost always network/mirror
reachability or a version whose checksum Kubespray doesn't know; a handful of
`download_*` knobs and the offline mirror variables control the behaviour.

## Problem

A task like `Download_file | Download item` or `Download_container | …` fails with:
connection timeout / `Failed to connect`, `certificate verify failed`,
`HTTP Error 403/429`, or `Checksum mismatch` / `does not match` for a binary or image.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Relevant defaults:
  - `download_retries: 4` — retry count for downloads.
  - `download_validate_certs: true` — verify TLS on downloads.
  - `download_force_cache: false`, `download_run_once: false`,
    `download_localhost: false` — caching/delegation behaviour.
- Binaries come from `*_download_url` (default upstream: `dl.k8s.io`, GitHub, etc.);
  images from `*_image_repo` (default `registry.k8s.io`, quay, ghcr, docker). Offline
  mirrors override these via `files_repo` / `registry_host` in
  `group_vars/all/offline.yml`.

## Diagnostics

- Read the failing task: it prints the **URL/image** and the exact error (DNS/TLS/HTTP/
  checksum). That URL tells you which repo is unreachable.
- Reachability from the target host: `curl -IL <url>` (binary) or `crictl pull <image>`
  (image) — reproduces the failure with a clearer message.
- Checksum mismatch: confirm the **version** you set is one Kubespray ships checksums for
  (a too-new/too-old `*_version` won't have a known checksum) and that a proxy/mirror
  isn't returning an error page instead of the file.
- For images behind a private/mirror registry, verify containerd registry config
  ([[TROUBLE-CONTAINERD_REGISTRY_CONFIG]]).

## Known Issues

**Fixes:**

- **Transient network / rate limit:** raise `download_retries`; for registry 429s use a
  mirror/pull-through ([[TROUBLE-IMAGE_PULL_RATE_LIMIT]]).
- **TLS interception / self-signed proxy:** point downloads at a trusted mirror, or (lab
  only) `download_validate_certs: false`.
- **Checksum mismatch:** use a version Kubespray has checksums for; if a proxy corrupts/
  replaces the file, fix the proxy. Do **not** blindly disable checksum verification —
  it protects against corrupted/tampered artifacts.
- **Air-gapped / offline:** set `files_repo`, `registry_host`, and the `*_image_repo` /
  `*_download_url` overrides to your internal mirrors — see
  [[PRACTICE-OFFLINE_ENVIRONMENT]]. `download_run_once`/`download_force_cache` help stage
  artifacts once and distribute them.
- **`download_localhost`** downloads on the Ansible host then pushes to nodes — useful
  when only the control host has egress (but not for Flatcar, per the preflight check).

**Gotchas:**

- A specific artifact can have a one-off checksum bug fixed in a later patch (e.g. a
  Gateway API tag) — check the per-artifact troubleshooting docs before assuming your
  environment is at fault.
- Mirrors must serve the **exact path layout** Kubespray expects (`files_repo` +
  `/dl.k8s.io/release/...`).

## References

- `download.yml` defaults and `offline.yml` sample at tag `v2.31.0`.
- Offline setup: [[PRACTICE-OFFLINE_ENVIRONMENT]]; registry config:
  [[TROUBLE-CONTAINERD_REGISTRY_CONFIG]].
