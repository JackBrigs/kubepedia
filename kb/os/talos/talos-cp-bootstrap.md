---
id: TROUBLE-TALOS_CP_BOOTSTRAP
type: troubleshooting
title: "Talos: control plane won't come up (bootstrap / etcd)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - talos bootstrap etcd
  - talos control plane not ready
  - talos bootstrap only once
  - talos etcd not forming
tags:
  - troubleshooting
  - talos
  - control-plane
  - etcd
sources:
  - type: docs
    path: Talos troubleshooting control plane
    url: https://www.talos.dev/latest/advanced/troubleshooting-control-plane/
    note: "bootstrap, etcd, static pods, health"
relations:
  - type: see_also
    target: CONCEPT-TALOS_OS_K8S
  - type: see_also
    target: CONCEPT-TALOS_UPGRADES
  - type: see_also
    target: TROUBLE-TALOS_APID_UNREACHABLE
---

# Talos: control plane won't come up (bootstrap / etcd)

## Summary

After applying configs the control plane never becomes ready / the API doesn't answer. The
classic causes: **`talosctl bootstrap` never run** (etcd was never initialized), **bootstrap run
on more than one node** (split-brain), a wrong **endpoint/VIP**, or etcd/time problems.

## Problem

- `talosctl health` never passes; kube-apiserver static pod not up.
- `talosctl -n <cp> get members` shows no/partial etcd members.
- API VIP unreachable; workers can't join.

## Context

- Applies to Talos **1.13.x** ([[CONCEPT-TALOS_OS_K8S]]). etcd + control-plane components run as
  Talos-managed static pods.

## Diagnostics

- **Bootstrap exactly once:** after the first control-plane node has its config, run
  **`talosctl bootstrap`** on **one** CP node only — this initializes etcd. **Never run it on a
  second node** (creates a split etcd). If forgotten, the CP waits forever with no etcd.
- **Check etcd:** `talosctl -n <cp> service etcd`, `talosctl -n <cp> get members`,
  `talosctl -n <cp> etcd status`. For quorum loss, use `etcd remove-member` / restore from a
  `talosctl etcd snapshot`.
- **Endpoint/VIP:** `cluster.controlPlane.endpoint` and `certSANs` must match the reachable
  API address (VIP or LB). A wrong endpoint means kubelets/workers can't reach the API — see the
  VIP notes in [[CONCEPT-TALOS_NETWORKING]].
- **Static pods / logs:** `talosctl -n <cp> get staticpods`,
  `talosctl -n <cp> logs kubelet`, `talosctl -n <cp> dmesg` — surfaces image-pull, cert, or
  disk problems.
- **Time sync:** skewed clocks break etcd/TLS — Talos runs NTP; verify time is sane.
- **Install disk:** an install to the wrong disk / no disk leaves the node not persisting —
  verify `machine.install.disk`.

## Known Issues

- If `talosctl` itself can't connect at all, fix connectivity first
  ([[TROUBLE-TALOS_APID_UNREACHABLE]]).
- Restoring etcd from a snapshot requires the **same secrets bundle** — another reason to back
  it up.

## References

- Talos control-plane troubleshooting (above); overview: [[CONCEPT-TALOS_OS_K8S]]; networking:
  [[CONCEPT-TALOS_NETWORKING]]; connectivity: [[TROUBLE-TALOS_APID_UNREACHABLE]].
