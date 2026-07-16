---
id: TROUBLE-CGROUP_DRIVER_MISMATCH
type: troubleshooting
title: "cgroup driver mismatch (containerd SystemdCgroup vs kubelet cgroupDriver)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cgroup driver mismatch
  - SystemdCgroup
  - kubelet cgroupDriver systemd
  - node NotReady cgroup
  - failed to get cgroup stats
  - containerd_use_systemd_cgroup
tags:
  - troubleshooting
  - containerd
  - kubelet
  - cgroups
sources:
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/defaults/main.yml
    note: "containerd_use_systemd_cgroup: true (tag v2.31.0)"
  - type: code
    path: roles/kubernetes/node/templates/kubelet-config.v1beta1.yaml.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/templates/kubelet-config.v1beta1.yaml.j2
    note: "kubelet cgroupDriver default 'systemd' (tag v2.31.0)"
relations:
  - type: see_also
    target: CONFIG-KUBELET_CONFIGURATION
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
---

# cgroup driver mismatch (containerd SystemdCgroup vs kubelet cgroupDriver)

## Summary

The kubelet and the container runtime must use the **same cgroup driver**. Kubespray
sets both to **systemd** by default (`containerd_use_systemd_cgroup: true` →
`SystemdCgroup = true`; kubelet `cgroupDriver: systemd`). If they diverge — usually
after a manual override — pods fail to start, resource accounting breaks, and nodes can
go `NotReady`. On a stock Kubespray cluster they match; the mismatch is almost always
self-inflicted by overriding one side only.

## Problem

Symptoms of a driver mismatch: pods stuck `ContainerCreating`, kubelet logs such as
`failed to get cgroup stats` / `Failed to start ContainerManager` /
`cgroup ... not found`, nodes flapping `NotReady`, or broken CPU/memory limits — after
changing cgroup-related settings or joining a node configured differently.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` with containerd.
- Defaults that keep the two in sync:
  - containerd: `containerd_use_systemd_cgroup: true` → `SystemdCgroup = true` in
    `config.toml`.
  - kubelet: `cgroupDriver: systemd` (template default; see
    [[CONFIG-KUBELET_CONFIGURATION]]).
- **cgroup v2 requires the systemd driver** — this is another reason the systemd default
  matters (and why Kubernetes `1.35` forces cgroup v2 by default, see
  [[CONCEPT-K8S_FEATURE_GATES]] / the 1.35 changes).
- Modern kubelets can auto-detect the driver from the CRI via the
  `KubeletCgroupDriverFromCRI` feature gate (Beta 1.31, GA 1.34) — where active, the
  kubelet follows containerd's driver, which shrinks (but doesn't fully remove) the
  chance of a mismatch on mixed versions.

## Diagnostics

- containerd side: `containerd config dump | grep -i SystemdCgroup` (expect `true`), or
  `grep SystemdCgroup /etc/containerd/config.toml`.
- kubelet side: `grep cgroupDriver /var/lib/kubelet/config.yaml` (or the rendered
  kubelet config) — expect `systemd`.
- Host cgroup version: `stat -fc %T /sys/fs/cgroup` (`cgroup2fs` = v2).
- kubelet logs: `journalctl -u kubelet -e` for cgroup/ContainerManager errors.

## Known Issues

- **Fix:** make both sides agree — keep `containerd_use_systemd_cgroup: true` **and**
  kubelet `cgroupDriver: systemd` (the Kubespray defaults). Don't flip only one. After
  changing, re-run the relevant roles so both configs and both services restart.
- Don't set `cgroupfs` on a cgroup v2 host — v2 needs the systemd driver; combined with
  the 1.35 cgroup-v1 removal, `systemd` is the only forward-looking choice.
- Joining a node that was pre-configured with a different driver causes a per-node
  mismatch — provision nodes through Kubespray so they inherit the same defaults.
- A mismatch often surfaces only after a reboot or kubelet restart (the runtime keeps
  running until then), so it can look unrelated to the config change that caused it.

## References

- `containerd/defaults/main.yml` (`containerd_use_systemd_cgroup`) and the kubelet
  config template at tag `v2.31.0`; kubelet config: [[CONFIG-KUBELET_CONFIGURATION]].
