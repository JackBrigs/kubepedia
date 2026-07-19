---
id: CONCEPT-ADDON_GPU_OPERATOR
type: concept
title: "NVIDIA GPU Operator — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.30 <=1.35"
component_version: "25.10.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - gpu-operator
  - nvidia gpu operator
  - gpu-operator v25.10.1
tags:
  - addons
  - gpu
  - nvidia
  - devices
sources:
  - type: docs
    path: gpu-operator platform support (25.10)
    url: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/25.10/platform-support.html
    note: "K8s 1.30–1.35; 1.35 added in v25.10.1"
  - type: code
    path: deployments/gpu-operator/values.yaml
    url: https://raw.githubusercontent.com/NVIDIA/gpu-operator/v25.10.1/deployments/gpu-operator/values.yaml
    note: "Driver 580.105.08, Toolkit v1.18.1, Device Plugin v0.18.1"
  - type: docs
    path: gpu-operator 25.10 release notes
    url: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/25.10/release-notes.html
    note: "CDI default-on, PSP removed, min K8s 1.30"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: COMPONENT-NODE_FEATURE_DISCOVERY
---

# NVIDIA GPU Operator — addon

## Summary

The NVIDIA GPU Operator automates GPU node setup — driver, container toolkit, device plugin,
feature discovery, DCGM, MIG. Chart **v25.10.1** supports Kubernetes **1.30–1.35** (1.35 was
added specifically in this patch; **1.29 is NOT supported**). Its **CDI-default-on** change is
the key behavioural item.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]]. Bundles its own NFD
  (v0.18.2) — mind overlap with a cluster-wide [[COMPONENT-NODE_FEATURE_DISCOVERY]].

## Implementation

- Chart/app **25.10.1**; components: Driver **580.105.08**, Container Toolkit **v1.18.1**,
  Device Plugin **v0.18.1**, GPU Feature Discovery **v0.18.1**, DCGM Exporter 4.4.2-4.7.0,
  MIG Manager v0.13.1, NFD v0.18.2.
- Chart `kubeVersion` in the tag is a build placeholder (`>= 1.16.0-0`) — **ignore it**; the
  effective range is the platform-support doc: **1.30–1.35**.

## Configuration

- **CDI enabled by default:** standard GPU workloads no longer need `runtimeClassName`, but
  GPU **management** containers that use `NVIDIA_VISIBLE_DEVICES` now **require an explicit
  `runtimeClassName`**.
- **PodSecurityPolicy support removed.**
- OpenShift upgrades: OLM does not mutate existing CRs, so `cdi.enabled=true` must be set
  manually post-upgrade.

## Compatibility

- **Kubernetes range:** **1.30–1.35** (min raised to 1.30 in the 25.10 line). 1.29 nodes are
  unsupported.
- **Known issues:** CRI-O pods stuck `Init:RunContainerError`/`CreateContainerError` on
  install/upgrade; Container Toolkit overwrites `imports` in top-level containerd config; on
  25.10.1 with SELinux enforcing, MIG Manager scheduling fails via GFD permissions (use the
  Node Feature API as workaround).
- **CVEs:** none affect the shipped versions. Historic Container Toolkit CVEs
  (CVE-2024-0132, CVE-2025-23266 "NVIDIAScape") predate the bundled Toolkit v1.18.1.

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context:** the line moved from **25.10.x** to **26.3.x** (2026) — check NVIDIA's release notes for driver/toolkit compatibility before jumping.

**Open upstream bugs (as of 2026-07-19):**
- **⚠ `nvidia-container-toolkit` restarting containerd wedges other DaemonSets** — a race during runtime-config updates causes pod init failures cluster-wide (#991). A real operational trap on install/upgrade.
- **nvidia-validator fails on Talos** (library path resolution) (#1687) — relevant for Talos nodes.
- missing install docs for **Amazon Linux 2023 / Bottlerocket** AMIs (#946).

## References

- Platform-support, `values.yaml`, release notes (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; NFD: [[COMPONENT-NODE_FEATURE_DISCOVERY]].
