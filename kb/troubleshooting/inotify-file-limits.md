---
id: TROUBLE-INOTIFY_FILE_LIMITS
type: troubleshooting
title: "too many open files / inotify watch exhaustion (kernel limits at scale)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - too many open files
  - inotify watch limit reached
  - fs.inotify.max_user_watches
  - fs.inotify.max_user_instances
  - no space left on device inotify
  - file descriptor limit kubernetes
  - fs.file-max
tags:
  - troubleshooting
  - kernel
  - sysctl
  - scale
  - nodes
sources:
  - type: code
    path: roles/kubernetes/preinstall/tasks/0080-system-configurations.yml
    lines: "135"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/tasks/0080-system-configurations.yml
    note: "Kubespray sets fs.inotify.max_user_instances: 8192; additional_sysctl for more"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "additional_sysctl: [] (tag v2.31.0)"
relations:
  - type: see_also
    target: TROUBLE-CONNTRACK_TABLE_FULL
  - type: see_also
    target: PRACTICE-LARGE_DEPLOYMENTS
  - type: see_also
    target: CONFIG-KUBELET_CONFIGURATION
---

# too many open files / inotify watch exhaustion (kernel limits at scale)

## Summary

At scale (many pods per node, many file watchers), pods and daemons hit **kernel
per-user/per-host limits**: `too many open files` (file descriptors) or inotify
**watch/instance** exhaustion — the latter often shows up misleadingly as
`no space left on device` even though the disk is fine. These are **sysctl/ulimit**
limits, not disk or app bugs. Kubespray raises `fs.inotify.max_user_instances` but you may
need to raise more.

## Problem

Pods/containers log `too many open files`, `inotify_add_watch … No space left on device`,
`failed to create fsnotify watcher`, or `pipe2: too many open files`; controllers/log
agents crash under load. Nodes at high pod density are the usual place.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- The relevant kernel knobs:
  - `fs.inotify.max_user_instances` — inotify instances per user (Kubespray sets **8192**).
  - `fs.inotify.max_user_watches` — total watches per user (default distro value is often
    too low for dense nodes).
  - `fs.file-max` / `fs.nr_open` — system/per-process open file descriptors.
  - `nofile` ulimit — per-process FD limit (systemd `LimitNOFILE`, container runtime).

## Diagnostics

- **Which limit:** the message distinguishes them — `too many open files` = FD/`nofile`;
  `inotify … No space left on device` = inotify watches/instances.
- **Current values:** `sysctl fs.inotify.max_user_watches fs.inotify.max_user_instances
  fs.file-max` on the node.
- **Usage:** count inotify watches per process, or `lsof | wc -l` / `cat
  /proc/sys/fs/file-nr` for FDs.
- **Correlate with density:** `kubectl get pods -A -o wide | grep <node> | wc -l` — dense
  nodes hit these first; watch-heavy workloads (log shippers, controllers, IDEs) burn
  inotify.

## Known Issues

**Fixes — raise the limits via sysctl (persist through Kubespray):**

- **inotify watches:** add to inventory
  ```yaml
  additional_sysctl:
    - { name: fs.inotify.max_user_watches, value: 524288 }
    - { name: fs.inotify.max_user_instances, value: 8192 }
  ```
  `additional_sysctl` is applied by the preinstall role, so the values survive reboots and
  re-runs (don't hand-edit `/etc/sysctl.conf` — Kubespray manages it).
- **file descriptors:** raise `fs.file-max`/`fs.nr_open` via `additional_sysctl`, and the
  runtime/systemd `LimitNOFILE` for the container engine if daemons hit it.
- **Per-pod PID limit** is separate (`kubelet_pod_pids_limit`, default `-1` unlimited —
  [[CONFIG-KUBELET_CONFIGURATION]]); a runaway pod forking processes is a different
  exhaustion (`podPidsLimit`).

**Gotchas:**

- The **`No space left on device`** from inotify is a classic red herring — the disk is
  fine; you're out of **watches**, not space.
- inotify limits are **per real user (UID)** on the host, shared across all that user's
  containers — one noisy pod can exhaust watches for others on the node.
- This is the same *class* of problem as conntrack-table exhaustion (a kernel table/limit
  full under load) — [[TROUBLE-CONNTRACK_TABLE_FULL]]; plan node sysctls for your density
  ([[PRACTICE-LARGE_DEPLOYMENTS]]).

## References

- `0080-system-configurations.yml` (`fs.inotify.max_user_instances`) and `additional_sysctl`
  at tag `v2.31.0`. Large-scale tuning: [[PRACTICE-LARGE_DEPLOYMENTS]]; PID limit:
  [[CONFIG-KUBELET_CONFIGURATION]].
