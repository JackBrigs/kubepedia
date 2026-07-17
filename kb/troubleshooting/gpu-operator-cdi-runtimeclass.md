---
id: TROUBLE-GPU_OPERATOR_CDI_RUNTIMECLASS
type: troubleshooting
title: "GPU Operator upgrade: management pods lose GPUs (CDI default-on)"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=25.10.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - gpu-operator cdi enabled by default
  - NVIDIA_VISIBLE_DEVICES no longer works
  - gpu management pod no runtimeclass
  - gpu-operator min kubernetes 1.30
tags:
  - troubleshooting
  - gpu
  - nvidia
  - upgrade
sources:
  - type: docs
    path: gpu-operator 25.10 release notes
    url: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/25.10/release-notes.html
    note: "CDI enabled by default; NVIDIA_VISIBLE_DEVICES needs runtimeClassName; PSP removed"
  - type: docs
    path: gpu-operator platform support
    url: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/25.10/platform-support.html
    note: "minimum Kubernetes 1.30"
relations:
  - type: see_also
    target: CONCEPT-ADDON_GPU_OPERATOR
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# GPU Operator upgrade: management pods lose GPUs (CDI default-on)

## Summary

After upgrading the NVIDIA GPU Operator to the **25.10 line (and 26.x)**, GPU **management**
containers that rely on `NVIDIA_VISIBLE_DEVICES` stop seeing GPUs, or the operator won't run
on a 1.29 node. Cause: **CDI is enabled by default** now, and the **minimum Kubernetes rose to
1.30**.

## Problem

- GPU management/tooling pods using `NVIDIA_VISIBLE_DEVICES` no longer get devices injected.
- Operator/components fail to schedule or are unsupported on **K8s 1.29** nodes.
- On OpenShift, CDI is not enabled after upgrade even though it should be.

## Context

- Applies to gpu-operator **≥25.10** (owner runs 25.10.1; latest 26.3.3 —
  [[CONCEPT-ADDON_GPU_OPERATOR]]).

## Diagnostics

- **CDI enabled by default:** standard GPU workloads no longer need `runtimeClassName`, but
  containers using `NVIDIA_VISIBLE_DEVICES` (typically GPU management containers) now
  **require an explicit `runtimeClassName`** — set it on those pods.
- **Minimum Kubernetes is 1.30** in the 25.10 line — 1.29 nodes are unsupported (1.35 support
  was added in 25.10.1).
- **PodSecurityPolicy support removed** — any PSP-based config must move to PSA/other.
- **OpenShift:** OLM does not mutate existing CRs, so set **`cdi.enabled=true` manually**
  post-upgrade.

## Known Issues

- CRI-O pods stuck `Init:RunContainerError`/`CreateContainerError` on install/upgrade; the
  Container Toolkit overwrites `imports` in the top-level containerd config; on 25.10.1 with
  SELinux enforcing, MIG Manager scheduling fails via GFD permissions (use the Node Feature
  API as a workaround).

## References

- gpu-operator 25.10 release notes + platform support (above); addon:
  [[CONCEPT-ADDON_GPU_OPERATOR]]; horizon: [[CONCEPT-UPGRADE_HORIZON]].
