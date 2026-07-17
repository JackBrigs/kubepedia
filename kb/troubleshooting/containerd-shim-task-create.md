---
id: TROUBLE-CONTAINERD_SHIM_TASK_CREATE
type: troubleshooting
title: "containerd: failed to create shim task (runc create failed)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - failed to create shim task
  - oci runtime create failed
  - can't get final child's PID from pipe EOF
  - lstat /proc/0/ns/ipc no such file
tags:
  - troubleshooting
  - containerd
  - runtime
  - runc
sources:
  - type: docs
    path: containerd shim PID-pipe EOF (1.7.24)
    url: https://github.com/containerd/containerd/issues/11119
    note: "regression 1.7.23→1.7.24 on shim→runc handoff"
  - type: docs
    path: containerd namespace race lstat /proc/0
    url: https://github.com/containerd/containerd/issues/9160
    note: "sandbox/shim exited before namespace resolution"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: TROUBLE-CRASHLOOPBACKOFF
---

# containerd: failed to create shim task (runc create failed)

## Summary

Pods fail at container start with `failed to create shim task: OCI runtime create failed: runc
create failed: ...`. Two distinct root causes: a **containerd 1.7.24 regression** on the
shim→runc PID handoff, and a **namespace race** under concurrent pod creation.

## Problem

- `... runc create failed: unable to start container process: can't get final child's PID from
  pipe: EOF: unknown`.
- Or (~1% under churn): `... unable to create new parent process: namespace path: lstat
  /proc/0/ns/ipc: no such file or directory: unknown`.

## Context

- Applies to Kubernetes **1.29–1.35** on containerd (Kubespray's default runtime —
  [[COMPONENT-CONTAINERD]]).

## Diagnostics

- **`can't get final child's PID from pipe: EOF`:** a **regression between containerd 1.7.23.x
  and 1.7.24.x** — runc's parent dies before returning the init PID (seen aarch64/kernel 4.19/
  runc 1.1.14). Also appears when runc init is **OOM-killed** by a tight cgroup. **Fix:**
  downgrade to **1.7.23.x** (confirmed good), verify memory limits, use a runc build known-good
  for the kernel (issue #11119).
- **`lstat /proc/0/ns/ipc: no such file`:** a **race** — the sandbox/shim that owns the shared
  IPC/NET/PID namespace **exited** before runc read `/proc/<pid>/ns/*` (`/proc/0/` = the target
  PID is already gone). Only under **concurrent creation** (seen containerd 1.6.19/runc 1.1.7).
  No upstream fix. **Fix:** reduce concurrent pod-create bursts; ensure the pause/sandbox is
  healthy before dependents; rely on kubelet retry; watch for a crash-looping sandbox
  (issue #9160).

## Known Issues

- Both surface as `CrashLoopBackOff`/`RunContainerError` at the kubelet level
  ([[TROUBLE-CRASHLOOPBACKOFF]]); check the containerd/`crictl` logs for the exact runc string.

## References

- containerd issues #11119 / #9160 (above); component: [[COMPONENT-CONTAINERD]].
