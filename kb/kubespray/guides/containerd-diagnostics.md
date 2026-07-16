---
id: PRACTICE-CONTAINERD_DIAGNOSTICS
type: best_practice
title: containerd diagnostics (day-2 runbook)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - containerd debug
  - image pull failure
  - crictl
tags:
  - operations
  - containerd
  - diagnostics
sources:
  - type: docs
    path: docs/CRI/containerd.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/CRI/containerd.md
    note: "containerd config; commands are standard crictl/ctr tooling"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: PRACTICE-NODE_NOT_READY
---

# containerd diagnostics (day-2 runbook)

## Summary

containerd ([[COMPONENT-CONTAINERD]]) is the default runtime. Symptoms:
`ImagePullBackOff`/`ErrImagePull`, `CreateContainerError`, or the node going
NotReady with "runtime not responsive". This runbook covers checking the runtime
and image pulls.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`; containerd runs as a systemd service;
  config at `/etc/containerd/config.toml`.

## Diagnostics

```bash
systemctl status containerd --no-pager
journalctl -u containerd -n 60 --no-pager
crictl info | head                              # runtime + CNI config
crictl ps -a | head                             # container states
crictl images | head                            # cached images

# reproduce an image pull (shows auth/registry/mirror errors)
crictl pull <image:tag>
```

Registry/mirror config lives under `/etc/containerd/config.toml` (and, for
private registries, the auth setup — see the CRI-O/containerd registry auth
troubleshooting entries):

```bash
grep -A3 -iE "registry|mirror|auth" /etc/containerd/config.toml
```

## Implementation

Common causes → action:
- **ErrImagePull / auth** → wrong/missing registry credentials or mirror; verify
  `containerd_registries*` / auth config; test with `crictl pull`.
- **Offline clusters** → images not mirrored; see [[PRACTICE-OFFLINE_ENVIRONMENT]].
- **runtime unresponsive** → restart containerd; check disk under
  `/var/lib/containerd` (`df -h`).
- **CreateContainerError** → often runc/cgroup mismatch; check
  `containerd_use_systemd_cgroup` vs kubelet cgroup driver.

## References

- `docs/CRI/containerd.md`; standard `crictl`/`ctr` tooling.
- Component: [[COMPONENT-CONTAINERD]], [[COMPONENT-RUNC]].
