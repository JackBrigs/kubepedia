---
id: TROUBLE-NODE_MEMORY_TOO_SMALL
type: troubleshooting
title: Node memory below Kubespray minimum (1500/1024 MB)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - memory too small
  - minimal_master_memory_mb
  - minimal_node_memory_mb
  - not enough RAM kubespray
tags:
  - troubleshooting
  - preflight
  - resources
  - memory
sources:
  - type: code
    path: roles/kubernetes/preinstall/tasks/0040-verify-settings.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/tasks/0040-verify-settings.yml
    note: "assert memtotal_mb >= minimal_{master,node}_memory_mb (tag v2.31.0)"
relations:
  - type: see_also
    target: TROUBLE-KUBESPRAY_PREFLIGHT_FAILS
  - type: see_also
    target: CONFIG-KUBELET_CONFIGURATION
---

# Node memory below Kubespray minimum (1500/1024 MB)

## Summary

Kubespray aborts if a node reports less RAM than the required minimum: **1500 MB** for
control-plane nodes (`minimal_master_memory_mb`) and **1024 MB** for worker nodes
(`minimal_node_memory_mb`). These are floors for a working cluster, not recommendations
— real workloads need much more.

## Problem

Preinstall stops on `Stop if memory is too small for control plane nodes` or
`Stop if memory is too small for nodes` because `ansible_memtotal_mb` is below the
threshold for that host's role.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`; defaults `minimal_master_memory_mb: 1500`,
  `minimal_node_memory_mb: 1024`.
- The control-plane check runs for hosts in `kube_control_plane`; the node check for
  hosts in `kube_node`. A host in both groups must clear the higher (control-plane) bar.
- `ansible_memtotal_mb` is total physical memory as seen by Ansible facts.

## Diagnostics

- Check actual memory: `free -m` / `cat /proc/meminfo` (`MemTotal`), compare to the
  threshold for the node's role.
- Confirm which group the host is in (`kube_control_plane` vs `kube_node`).
- The failing task name states whether it hit the master or node threshold.

## Known Issues

- **Fix:** resize the VM/host to meet the floor (≥1500 MB control-plane, ≥1024 MB
  worker). Plan for real headroom — reserve capacity with `kube_reserved` /
  `system_reserved` (see [[CONFIG-KUBELET_CONFIGURATION]]).
- The thresholds are overridable (`minimal_master_memory_mb` / `minimal_node_memory_mb`)
  but lowering them only defers the problem — the control plane (etcd, apiserver) is
  memory-hungry and will OOM or thrash on undersized nodes.
- Facts must be current: a stale facts cache can report old memory after a resize —
  re-run `facts.yml` after changing node size.

## References

- `0040-verify-settings.yml` (memory asserts) at tag `v2.31.0`.
- Preflight overview: [[TROUBLE-KUBESPRAY_PREFLIGHT_FAILS]].
