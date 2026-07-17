---
id: TROUBLE-CONTAINERD_IMAGE_PULL_CRI
type: troubleshooting
title: "containerd: image pull / CRI sandbox failures"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.0.0 <=2.3.3"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - containerd failed to pull and unpack
  - failed to create sandbox
  - containerd registry mirror auth
  - sandbox image pause
tags:
  - troubleshooting
  - containerd
  - runtime
  - cri
sources:
  - type: docs
    path: containerd CRI registry configuration
    url: https://github.com/containerd/containerd/blob/main/docs/hosts.md
    note: "config_path / certs.d hosts.toml, mirrors, auth"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: TROUBLE-IMAGEPULLBACKOFF
---

# containerd: image pull / CRI sandbox failures

## Summary

Pods fail with image-pull errors or `failed to create sandbox` at the containerd/CRI layer.
The usual causes are registry **mirror/auth** config (the `hosts.toml` / `config_path`
mechanism), a wrong **sandbox (pause) image**, or a broken CRI config after an upgrade.

## Problem

- `kubelet` events: `failed to pull and unpack image ...`, `failed to resolve reference`.
- `RunPodSandbox` / `CreateContainer` errors; pods stuck `ContainerCreating`.
- Private-registry images fail with `401/403`.

## Context

- Applies to containerd **2.0–2.3.3** (base ≤2.2.3 — [[COMPONENT-CONTAINERD]]). General
  image-pull triage: [[TROUBLE-IMAGEPULLBACKOFF]].

## Diagnostics

- **Registry mirror/auth:** modern containerd uses `config_path = "/etc/containerd/certs.d"`
  with per-registry `hosts.toml`. Verify the path is set in `/etc/containerd/config.toml`, the
  `hosts.toml` exists for the registry, and credentials (or an `imagePullSecret`) are correct.
  Test out-of-band: `ctr -n k8s.io images pull <ref>` / `crictl pull <ref>`.
- **Sandbox (pause) image:** a wrong/unreachable `sandbox_image` in the CRI plugin config
  breaks *every* pod sandbox — confirm it points to a pullable pause image.
- **After an upgrade:** the CRI config schema/version may have changed (containerd 2.x); a
  merged/overwritten `imports` section (e.g. by the NVIDIA toolkit) can drop the CRI config —
  re-check the effective `containerd config dump`.
- **TLS to registry:** a private CA must be trusted (place the CA in the `certs.d` dir or node
  trust store); self-signed without config → x509 errors.

## Known Issues

- containerd 2.x carries known CVEs at the shipped patch levels — see the containerd CVE
  matrix. GPU nodes: the Container Toolkit overwrites top-level `imports`.

## References

- containerd registry/hosts docs (above); component: [[COMPONENT-CONTAINERD]]; image-pull:
  [[TROUBLE-IMAGEPULLBACKOFF]].
