---
id: TROUBLE-CONTAINERD_REGISTRY_CONFIG
type: troubleshooting
title: "containerd can't pull from a private/mirror registry (hosts.toml / certs.d)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - containerd private registry
  - registry mirror not working
  - hosts.toml
  - certs.d
  - containerd_registries_mirrors
  - containerd_registry_auth
  - x509 unknown authority pull
  - insecure registry containerd
tags:
  - troubleshooting
  - containerd
  - registry
  - image-pull
sources:
  - type: code
    path: roles/container-engine/containerd/templates/hosts.toml.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/templates/hosts.toml.j2
    note: "per-registry hosts.toml rendering (tag v2.31.0)"
  - type: code
    path: roles/container-engine/containerd/templates/config.toml.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/templates/config.toml.j2
    note: "registry config_path = {containerd_cfg_dir}/certs.d (tag v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: TROUBLE-IMAGE_PULL_RATE_LIMIT
  - type: see_also
    target: TROUBLE-CGROUP_DRIVER_MISMATCH
---

# containerd can't pull from a private/mirror registry (hosts.toml / certs.d)

## Summary

Kubespray configures containerd's image registries using the **`config_path`**
mechanism: `config.toml` sets
`[plugins."io.containerd.cri.v1.images".registry] config_path = /etc/containerd/certs.d`,
and each registry gets a `certs.d/<registry>/hosts.toml` describing its mirrors, TLS,
and auth. Pull failures (`ImagePullBackOff`, `x509`, `401/403`, connection refused) from
a private or mirrored registry almost always mean the `hosts.toml` isn't set (or is
wrong) for that registry. You configure it through inventory, **not** by hand-editing
files that Kubespray will overwrite.

## Problem

Pods stay in `ImagePullBackOff`/`ErrImagePull` for images from a private registry or an
intended mirror; `crictl pull <image>` fails with TLS errors (`x509: certificate signed
by unknown authority`), auth errors (`401 Unauthorized`/`403`), or connection errors —
while public images pull fine.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` with `container_manager: containerd`.
- Registry config lives under `containerd_cfg_dir/certs.d` (default
  **`/etc/containerd/certs.d`**); the CRI plugin reads a per-registry `hosts.toml`.
- Kubespray renders these from inventory variables — the two you need:
  - **`containerd_registries_mirrors`** — list of `{prefix, mirrors:[{host,
    capabilities, skip_verify, override_path, ca, client, header}]}`.
  - **`containerd_registry_auth`** — list of `{registry, username, password}` for
    private-registry credentials (default `[]`).

## Diagnostics

- Reproduce the pull on the node: `crictl pull <image>` (reads the same containerd
  config as the kubelet) — its error names the exact cause (TLS / auth / network).
- Check the rendered config exists and is correct:
  `cat /etc/containerd/certs.d/<registry-host>/hosts.toml` and
  `grep config_path /etc/containerd/config.toml`.
- Inspect containerd logs: `journalctl -u containerd -e`.
- Confirm the image's registry host matches a configured `prefix`/`host` exactly
  (`docker.io` vs `registry-1.docker.io`, port, path).

## Known Issues

**Fixes (set in inventory, then re-run the `containerd` role):**

- **Self-signed / private CA (`x509`):** add `ca` (path to the CA cert on the node) to
  the mirror entry, or `skip_verify: true` for a lab (insecure — disables TLS
  verification).
- **Private registry auth (`401/403`):** add an entry to `containerd_registry_auth`
  with `registry`, `username`, `password`.
- **Mirror / pull-through cache:** add the upstream under
  `containerd_registries_mirrors` with the mirror `host` and
  `capabilities: ["pull","resolve"]`; use `override_path`/`server` for non-standard
  layouts. Also relevant for Docker Hub rate limits ([[TROUBLE-IMAGE_PULL_RATE_LIMIT]]).
- **mTLS to registry:** provide `client` cert/key pairs in the mirror entry.
- **Custom headers:** `header` map (e.g. an auth proxy token).

**Gotchas:**

- Do **not** hand-edit `/etc/containerd/certs.d/*` or `config.toml` — Kubespray
  overwrites them on the next run. Change inventory instead.
- The registry key must match the image host **exactly**; `docker.io` images resolve
  via `registry-1.docker.io` — mirror the right one.
- After changing the config, containerd must reload/restart (the role handles this on a
  full run); a manual `crictl` test won't pick up changes until then.

## References

- `hosts.toml.j2`, `config.toml.j2` (registry `config_path`) at tag `v2.31.0`.
- Component: [[COMPONENT-CONTAINERD]]; rate limits: [[TROUBLE-IMAGE_PULL_RATE_LIMIT]].
