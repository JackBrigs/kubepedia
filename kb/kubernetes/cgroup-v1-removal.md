---
id: CONCEPT-K8S_CGROUP_V1_REMOVAL
type: concept
title: "cgroup v1 in maintenance mode (1.31) → removal underway (beta 1.35) — migrate to cgroup v2"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - cgroup v1 maintenance mode
  - cgroup v1 removal kubernetes
  - migrate to cgroup v2
  - RemoveCgroupV1
  - cgroupv1 deprecated
tags:
  - kubernetes
  - kubelet
  - cgroups
  - node
sources:
  - type: code
    path: keps/sig-node/4569-cgroup-v1-maintenance-mode
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/4569-cgroup-v1-maintenance-mode
    note: "kep.yaml: maintenance mode 1.31; removal KEP 5573 beta 1.35"
relations:
  - type: see_also
    target: PRACTICE-CGROUPS
  - type: see_also
    target: PRACTICE-KERNEL_REQUIREMENTS
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
---

# cgroup v1 in maintenance mode (1.31) → removal underway (beta 1.35) — migrate to cgroup v2

## Summary

**cgroup v1** is on the way out: Kubernetes put it in **maintenance mode from 1.31** (bug-fixes only,
no new features — KEP 4569) and began the **removal** path with **`RemoveCgroupV1` beta in 1.35** (KEP
5573). Nodes still booting cgroup v1 are on borrowed time; features like **node swap** and **PSI
metrics** already require cgroup v2. Migrate node OSes to **cgroup v2** (unified hierarchy) before it
becomes mandatory.

## Context

- Milestones: maintenance mode **1.31** (`keps/sig-node/4569-...`); removal `RemoveCgroupV1` **beta
  1.35** (`keps/sig-node/5573-...`).
- **cgroup v2 is already the default** on modern distros (recent Ubuntu/RHEL) and is required by newer
  kubelet features. Kubespray runs on cgroup v2 by default on supported OSes ([[PRACTICE-CGROUPS]]).
- **Operator action:** verify nodes boot the **unified** cgroup hierarchy (`stat -fc %T /sys/fs/cgroup`
  → `cgroup2fs`). A node still on cgroup v1 loses access to v2-only features now and will fail once
  removal completes; migrating means an OS/kernel/boot-param change and a node reboot
  ([[PRACTICE-KERNEL_REQUIREMENTS]]).

## References

- `keps/sig-node/4569-cgroup-v1-maintenance-mode`, `keps/sig-node/5573-remove-cgroup-v1` (kep.yaml).
  cgroups [[PRACTICE-CGROUPS]]; kernel [[PRACTICE-KERNEL_REQUIREMENTS]]; silent changes
  [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]].
