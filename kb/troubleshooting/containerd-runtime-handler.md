---
id: TROUBLE-CONTAINERD_RUNTIME_HANDLER
type: troubleshooting
title: "containerd: no runtime configured for RuntimeClass handler (gVisor/Kata)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - no runtime for runsc is configured
  - no runtime for kata-qemu is configured
  - runtimeclass handler not found containerd
  - gvisor kata containerd runtime
tags:
  - troubleshooting
  - containerd
  - runtimeclass
  - runtime
sources:
  - type: docs
    path: minikube gVisor no runtime configured
    url: https://github.com/kubernetes/minikube/issues/5463
    note: "handler must match containerd runtimes.<handler> block"
  - type: docs
    path: kata on k3s handler config
    url: https://github.com/kata-containers/kata-containers/issues/10914
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: COMPONENT-KATA_CONTAINERS
---

# containerd: no runtime configured for RuntimeClass handler (gVisor/Kata)

## Summary

Pods using a `RuntimeClass` (gVisor `runsc`, Kata) fail to schedule the sandbox with
`failed to get sandbox runtime: no runtime for "runsc" is configured` — the RuntimeClass
`handler` has no matching runtime block in containerd's config.

## Problem

- `no runtime for "runsc" is configured` (gVisor) / `no runtime for "kata-qemu" is configured`
  (Kata) when creating a pod with that `runtimeClassName`.

## Context

- Applies to Kubernetes **1.29–1.35** on containerd ([[COMPONENT-CONTAINERD]],
  [[COMPONENT-KATA_CONTAINERS]]). Common on k3s/minikube where the managed `config.toml` isn't
  edited by the runtime installer.

## Diagnostics

- **Cause:** the `RuntimeClass.handler` string has **no matching**
  `[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.<handler>]` block — and the key must
  match the handler **char-for-char**.
- **Fix:** add the handler block and **restart containerd**, e.g.:
  - gVisor: `...runtimes.runsc` with `runtime_type = "io.containerd.runsc.v1"`.
  - Kata: `...runtimes.kata-qemu` with `runtime_type = "io.containerd.kata-qemu.v2"`.
- **On k3s:** don't edit the managed `config.toml` directly — use a **`config.toml.tmpl`**
  override so the runtime block survives restarts (kata-deploy doesn't edit it for you).
- Verify the `RuntimeClass` object's `handler` equals the config key exactly.

## Known Issues

- A version mismatch between the shim binary and the `runtime_type` also fails here — install
  the matching shim (`containerd-shim-runsc-v1` / `containerd-shim-kata-v2`) on PATH.

## References

- minikube #5463, kata #10914 (above); component: [[COMPONENT-CONTAINERD]]; Kata:
  [[COMPONENT-KATA_CONTAINERS]].
