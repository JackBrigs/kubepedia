---
id: TROUBLE-CILIUM_MOUNT_CGROUP_DENIED
type: troubleshooting
title: "Cilium agent Init:CrashLoopBackOff — mount-cgroup 'cannot create /hostbin/cilium-mount: Permission denied'"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-20"
confidence: verified
aliases:
  - cilium mount-cgroup permission denied
  - cannot create regular file '/hostbin/cilium-mount'
  - cilium agent Init CrashLoopBackOff
  - node.cilium.io/agent-not-ready
  - cilium-envoy running but cilium agent not ready
  - kube_owner opt cni bin cilium
  - opt/cni/bin owned by kube not root
tags:
  - troubleshooting
  - cilium
  - cni
  - nodes
sources:
  - type: docs
    path: cilium/cilium mount-cgroup Permission denied
    url: https://github.com/cilium/cilium/issues/23838
    note: "canonical: since v1.12 mount-cgroup runs non-privileged; fix is securityContext.privileged=true"
  - type: docs
    path: cilium init container copy cni permission denied
    url: https://github.com/cilium/cilium/issues/24889
    note: "same class; reduced-privilege init container cannot write to host CNI bin dir"
  - type: docs
    path: kubespray Ubuntu 24.04 cilium-mount permission denied
    url: https://github.com/kubernetes-sigs/kubespray/issues/12276
    note: "exact Kubespray + Ubuntu 24.04 report (kube-proxy-replacement); open, no documented resolution"
  - type: code
    path: roles/network_plugin/cilium/tasks/install.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/network_plugin/cilium/tasks/install.yml
    note: "cilium_extra_values (defaults/main.yml) is rendered to cilium-extra-values.yaml and passed to Helm — the knob for securityContext.privileged"
  - type: code
    path: roles/kubernetes/preinstall/tasks/0050-create_directories.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/kubernetes/preinstall/tasks/0050-create_directories.yml
    note: "'Create cni directories' (L68-76) creates /opt/cni/bin with owner: {{ kube_owner }}; kube_owner defaults to 'kube' — the actual root cause"
  - type: code
    path: tests/files/debian12-cilium.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/tests/files/debian12-cilium.yml
    note: "Kubespray's Cilium CI pins kube_owner: root — so the default kube_owner: kube + Cilium combo is untested (matches issue #12276)"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: TROUBLE-KUBELET_NODE_NOTREADY_CNI
  - type: see_also
    target: TAG-CILIUM
---

# Cilium agent Init:CrashLoopBackOff — mount-cgroup 'cannot create /hostbin/cilium-mount: Permission denied'

## Summary

The `cilium` agent DaemonSet is stuck `Init:CrashLoopBackOff` because its
**`mount-cgroup` init container** fails with `cp: cannot create regular file
'/hostbin/cilium-mount': Permission denied`. Root cause: Kubespray creates
`/opt/cni/bin` with **`owner: {{ kube_owner }}`, and `kube_owner` defaults to
`kube`** (not `root`). Since Cilium **v1.12** the `mount-cgroup` init container runs
as uid 0 but with a **reduced capability set that drops `CAP_DAC_OVERRIDE`**, so it
is treated as a plain non-owner against the `kube`-owned `0755` dir and the write is
denied — **EACCES (`Permission denied`)**, not EROFS. It is **not** an LSM problem:
Cilium annotates these init containers AppArmor `unconfined` and the pod seccomp
`Unconfined`. On a **root-owned** `/opt/cni/bin` (Kubespray's own Cilium CI sets
`kube_owner: root`) the uid-0 container is the owner and writes fine — which is why
the default `kube_owner` + Cilium is the broken, untested combo (issue #12276). The
node stays `NotReady` with the `node.cilium.io/agent-not-ready` taint and
`/etc/cni/net.d` never gets populated (→ [[TROUBLE-KUBELET_NODE_NOTREADY_CNI]]).
`cilium-envoy` keeps `Running` because it does not do this host-write — the tell.

## Problem

- `kubectl -n kube-system get pod` shows `cilium-<x>` `0/1 Init:CrashLoopBackOff`
  while `cilium-envoy-<x>` is `1/1 Running` on the same node.
- Failing init container is `mount-cgroup` (`ready=false`, `reason=Error`,
  `exitCode=1`); its log is `cp: cannot create regular file
  '/hostbin/cilium-mount': Permission denied`.
- Node `NotReady` with taint `node.cilium.io/agent-not-ready:NoSchedule`; workloads
  on it stay `ContainerCreating`.
- A `Read-only file system` variant (not `Permission denied`) is a **different**
  cause — a non-writable/wrong CNI bin path (e.g. GKE's `/home/kubernetes/bin`),
  not covered here.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`, which install **Cilium via Helm**
  (Cilium `1.18.x`; v2.29.0 ships `1.18.2`, v2.29.1 ships `1.18.4`). Kubespray does
  not force `privileged`, so the chart's reduced-privilege init containers are used
  ([[COMPONENT-CILIUM]]).
- The ownership comes from `roles/kubernetes/preinstall/tasks/0050-create_directories.yml`
  ("Create cni directories", `owner: {{ kube_owner }}`). `kube_owner` default is
  `kube` (`roles/kubespray_defaults/defaults/main/main.yml`), while the **hardening
  guide and all Cilium CI test files pin `kube_owner: root`** — so stock Cilium is
  only ever exercised with a root-owned bin dir.
- Reproduced on **Ubuntu 24.04** with kube-proxy-replacement (Kubespray issue
  #12276, open). Confirmed on a real node: `/opt/cni/bin` is `drwxr-xr-x kube root`,
  the `cni-path` volume is mounted **rw**, `lsattr` shows no immutable bit, `findmnt`
  shows it is not a separate/`ro` mount, and `journalctl -k` has no AppArmor/SELinux
  denials — leaving the `kube` ownership + dropped `CAP_DAC_OVERRIDE` as the cause.
- **Empirically verified:** `chown root:root /opt/cni/bin` on the node + deleting the
  stuck pod → the new `cilium` agent reaches `1/1 Running` and the node goes `Ready`.
  This both proves the ownership root cause and validates the durable fixes below.
- `cilium_extra_values` (Kubespray default `{}`) is rendered to
  `cilium-extra-values.yaml` and passed to Helm — the supported way to set any chart
  value, including `securityContext.privileged`.

## Diagnostics

- Confirm the failing init step and message:
  `kubectl -n kube-system get pod <cilium-pod> -o jsonpath='{range .status.initContainerStatuses[*]}{.name}{" ready="}{.ready}{" "}{.lastState.terminated.reason}{"\n"}{end}'`
  then `kubectl -n kube-system logs <cilium-pod> -c mount-cgroup`.
- **Confirm it is EACCES, not EROFS:** the message is `Permission denied`
  (privilege/DAC), *not* `Read-only file system` (wrong/RO path) — they have
  different fixes.
- **Host CNI bin dir ownership (the smoking gun):** `ls -ld /opt/cni/bin`. If it is
  **`kube …` (or any non-root owner)** with mode `0755`, that is the cause — a uid-0
  container without `CAP_DAC_OVERRIDE` is a non-owner and cannot write. A
  **`root`-owned** dir would be writable by the uid-0 container and would *not* fail.
  Also check `lsattr -d /opt/cni/bin` (immutable `+i`?) and `findmnt /opt/cni/bin`
  (a separate/`ro` mount would give EROFS instead).
- Rule out LSM quickly: Cilium already annotates these init containers
  `container.apparmor.security.beta.kubernetes.io/mount-cgroup: unconfined`; only a
  **host-level** AppArmor/SELinux policy could still deny — check
  `journalctl -k | grep -iE 'apparmor.*DENIED|avc:.*denied'` and, on Ubuntu 24.04,
  `sysctl kernel.apparmor_restrict_unprivileged_userns`.

## Known Issues

- **Immediate unblock (one node, now):** `chown root:root /opt/cni/bin` on the
  affected node, then delete the stuck pod (`kubectl -n kube-system delete pod
  cilium-<x>`). The uid-0 init container becomes the owner and the `cp` succeeds.
  This is **not durable** — a later `cluster.yml`/preinstall run re-applies
  `owner: {{ kube_owner }}` and reverts it — so pair it with a durable fix below.
- **Durable fix A — align with Kubespray's own Cilium setup: `kube_owner: root`.**
  Set `kube_owner: root` in inventory (this is what the hardening guide and every
  Cilium CI test file use), then re-run `cluster.yml`. `/opt/cni/bin` becomes
  root-owned and the non-privileged `mount-cgroup` writes as owner — no privilege
  escalation needed. Note `kube_owner` is **cluster-wide**: it re-owns many
  Kubernetes dirs/files, so apply it deliberately (ideally cluster-wide, not to one
  node).
- **Durable fix B — Cilium-side, narrow blast radius (source: cilium #23838/#24889):
  grant privilege.** In group_vars (e.g. `group_vars/k8s_cluster/k8s-net-cilium.yml`):

  ```yaml
  cilium_extra_values:
    securityContext:
      privileged: true
  ```

  then re-apply the CNI: `ansible-playbook cluster.yml -b -i <inventory>
  --tags=cilium`, and delete the stuck pod. This restores full privilege
  (`CAP_DAC_OVERRIDE`) so `mount-cgroup` writes regardless of the dir owner. Touches
  only the Cilium DaemonSet, but keeps a non-standard `/opt/cni/bin` ownership.
- **Don't confuse with `Read-only file system`** — that is a wrong/RO CNI bin path
  (e.g. GKE's `/home/kubernetes/bin`), fixed by pointing Cilium at the writable bin
  dir, not by ownership or `privileged`.

## References

- cilium/cilium #23838 (privileged fix), #24889 (init copy denied), kubespray
  #12276 (Ubuntu 24.04, open); root cause:
  `roles/kubernetes/preinstall/tasks/0050-create_directories.yml` (`/opt/cni/bin`
  `owner: {{ kube_owner }}`, default `kube`) vs Cilium CI `kube_owner: root`; Helm
  knob: `roles/network_plugin/cilium/tasks/install.yml` (`cilium_extra_values`).
  Downstream node symptom: [[TROUBLE-KUBELET_NODE_NOTREADY_CNI]]; CNI:
  [[COMPONENT-CILIUM]].
