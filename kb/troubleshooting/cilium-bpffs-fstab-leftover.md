---
id: TROUBLE-CILIUM_BPFFS_FSTAB_LEFTOVER
type: troubleshooting
title: "Leftover `bpffs /sys/fs/bpf` entry in /etc/fstab after Kubespray stops managing it"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-28"
confidence: verified
aliases:
  - bpffs fstab kubespray
  - "Cilium | Ensure BPFFS mounted"
  - /sys/fs/bpf fstab entry
  - bpf mount left in fstab
tags:
  - cilium
  - cni
  - os
  - nodes
sources:
  - type: code
    path: roles/network_plugin/cilium/tasks/install.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/tasks/install.yml
    note: "task 'Cilium | Ensure BPFFS mounted' — ansible.posix.mount state: mounted, i.e. writes /etc/fstab"
  - type: pull_request
    path: kubespray PR #13377 — Unneeded bpf fstab entry added when using Cilium
    url: https://github.com/kubernetes-sigs/kubespray/pull/13377
    note: "merged 2026-07-20 into master: the task is removed entirely; unreleased"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: PRACTICE-NODE_NETWORK_CHANGE
---

# Leftover `bpffs /sys/fs/bpf` entry in /etc/fstab after Kubespray stops managing it

## Summary

Through **v2.31.0** Kubespray mounts the BPF filesystem itself when Cilium is the CNI, and does it
with a **persistent** mount — the entry lands in `/etc/fstab`. Upstream removed that task on
`master` (PR #13377, merged 2026-07-20, not in any release). Removing the task does not remove the
line it wrote: every node deployed by an earlier release keeps a Kubespray-authored `fstab` entry
that nothing owns any more.

## Problem

The task at v2.31.0 is:

```yaml
- name: Cilium | Ensure BPFFS mounted
  ansible.posix.mount:
    fstype: bpf
    path: /sys/fs/bpf
    src: bpffs
    state: mounted
```

`state: mounted` means "mount now **and** persist in `/etc/fstab`". Modern Cilium mounts the BPF
filesystem itself from its `mount-bpf-fs` init container, and systemd mounts `/sys/fs/bpf` on
current distributions, so the entry is redundant — which is exactly the reasoning behind its
removal upstream.

Nothing breaks either way. The problem is ownership: after the upgrade that drops the task, the
line stays in `/etc/fstab` looking like deliberate node configuration, with no code left in
Kubespray that would recreate, verify or remove it. The next person to audit the file has to
work out where it came from.

## Context

Applies to nodes deployed with Kubespray v2.27.0–v2.31.0 using Cilium (`kube_network_plugin:
cilium` or `cilium_deploy_additionally`). The removal is **future context**: it exists only on
`master` as of 2026-07-28 — v2.31.0 is dated 2026-04-24, the merge is 2026-07-20.

## Diagnostics

```bash
grep -n 'bpf' /etc/fstab
findmnt /sys/fs/bpf
kubectl -n kube-system get ds cilium -o jsonpath='{.spec.template.spec.initContainers[*].name}'
```

Expected on an affected node: an fstab line `bpffs /sys/fs/bpf bpf defaults 0 0`, the filesystem
mounted, and `mount-bpf-fs` present among Cilium's init containers — i.e. two mechanisms doing the
same job.

## Known Issues

- **Do not remove the line while Cilium is running until you confirm who mounts it.** If
  `mount-bpf-fs` is in the DaemonSet, Cilium mounts the filesystem itself on start and the fstab
  entry is redundant; unmounting a live `/sys/fs/bpf` is a different matter and is not part of this
  cleanup — the entry only decides what happens at the next boot.
- **The entry is not removed by the upgrade.** `ansible.posix.mount` with `state: mounted` only
  adds; the task's disappearance leaves the line. Cleaning it up is a manual, per-node action
  (`state: absent` via ad-hoc Ansible, or editing the file) and belongs to the same class as other
  leftover node artefacts ([[PRACTICE-NODE_NETWORK_CHANGE]] for the general procedure of proving an
  artefact is unused before deleting it).
- **On older kernels or minimal images the mount may still be doing real work** — check
  `findmnt /sys/fs/bpf` before assuming redundancy.

## References

- `roles/network_plugin/cilium/tasks/install.yml` at tag **v2.31.0** (task present) vs `master`
  (task removed by PR #13377, merged 2026-07-20) — verified 2026-07-28.
- CNI: [[COMPONENT-CILIUM]].
