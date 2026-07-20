---
id: TROUBLE-CONTAINERD_TASK_V3_DOWNGRADE
type: troubleshooting
title: "containerd: 'downgrading client API version' task.v3.Task warning (shim v3 mismatch)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-20"
confidence: confirmed
aliases:
  - failed to call task.Create downgrading client API version
  - service containerd.task.v3.Task
  - unsupported shim version (3)
  - containerd task v3 downgrade
  - downgrading client API version to try again
tags:
  - troubleshooting
  - containerd
  - runtime
  - shim
sources:
  - type: docs
    path: containerd shim v3 not implemented (2.0.0)
    url: https://github.com/containerd/containerd/issues/10984
    note: "containerd 2.0.0 introduced the v3 task API; a shim that only implements v2 yields 'unsupported shim version (3): not implemented'"
  - type: docs
    path: moby/moby failed to create task for container
    url: https://github.com/moby/moby/issues/46490
    note: "same class: task-service version mismatch between client and shim after a containerd major upgrade"
  - type: code
    path: roles/container-engine/containerd/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/container-engine/containerd/defaults/main.yml
    note: "Kubespray v2.29.0 ships containerd 2.1.4 (2.x line — see CONCEPT-CONTAINERD_2X), which negotiates the v3 task API"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: CONCEPT-CONTAINERD_2X
  - type: see_also
    target: TROUBLE-CONTAINERD_SHIM_TASK_CREATE
  - type: see_also
    target: TROUBLE-CONTAINERD_RUNTIME_HANDLER
---

# containerd: 'downgrading client API version' task.v3.Task warning (shim v3 mismatch)

## Summary

The containerd warning `failed to call task.Create, downgrading client API version
to try again` / `error="service containerd.task.v3.Task"` is **benign on its own**.
containerd **2.0** added a **v3 task ttrpc service**; the client calls v3 first, and
against a shim that only implements the older **v2** service it **auto-downgrades
and retries** — the task is still created and the pod starts. The line **recurs for
containers backed by such a shim**, which is noisy but not harmful. It matters only
when paired with a hard `unsupported shim version (3): not implemented` failure
(see Problem).

## Problem

- Repeated `warning … downgrading client API version to try again … service
  containerd.task.v3.Task` in `journalctl -u containerd`, but pods actually **start
  and run**. → cosmetic; the v2 fallback succeeded.
- Or a **hard** failure at pod start: `failed to create task … unsupported shim
  version (3): not implemented` and the pod stays `RunContainerError` /
  `CreateContainerError`. → the fallback did **not** save it; the shim is too old
  or wrong for this containerd.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`, which ship **containerd 2.x**
  (`2.1.4`→`2.2.3`; see [[CONCEPT-CONTAINERD_2X]] / [[COMPONENT-CONTAINERD]]).
  containerd 2.0 is where the v3 task API landed (issue #10984).
- The "client API version" in the message is the **shim task ttrpc-service
  version** (`containerd.task.v3.Task` → `…v2.Task`) negotiated per shim — **not**
  the containerd client API module, which deliberately stayed on `1.x` across the
  2.0 major bump. So the line is about the runtime-shim protocol, not the daemon API.
- The shim that ships **with** containerd 2.x (`containerd-shim-runc-v2`) does
  implement v3, so **default `runc` pods on a clean Kubespray node should not log
  this**. Seeing it points at a **shim/runtime that predates v3**:
  - a **stale/mismatched `containerd-shim-runc-v2` binary** left on `PATH` after an
    in-place containerd upgrade without a full restart, or from a different install;
  - a **third-party RuntimeClass runtime** (Kata, gVisor/`runsc`, NVIDIA, runwasi)
    whose shim was built against containerd 1.x / early 2.x — see
    [[TROUBLE-CONTAINERD_RUNTIME_HANDLER]].

## Diagnostics

- Confirm it is only a warning: `journalctl -u containerd | grep -i "downgrading client API"`
  — if the same container id then reaches `RunPodSandbox`/`CreateContainer` success
  and the pod is `Running`, it is cosmetic.
- Identify the runtime for the affected container: `crictl inspect <id> | grep -i runtimeType`
  (or map the pod → its `runtimeClassName`). A non-default handler ⇒ a third-party shim.
- Check the shim binary vs the containerd package:
  `containerd --version` and `containerd-shim-runc-v2 --version` /
  `which -a containerd-shim-runc-v2` — a version older than the running containerd,
  or duplicate copies on `PATH`, is the usual culprit.

## Known Issues

- **Warning only (pods run): no action required.** It is expected fallback noise for
  any v2-only shim under containerd 2.x. To silence it, align the shim with
  containerd (below).
- **Fix a stale default shim:** re-run the Kubespray container-engine role so
  `containerd-shim-runc-v2` matches the running containerd, then `systemctl restart
  containerd`.
- **Fix a third-party runtime:** upgrade the Kata/gVisor/NVIDIA/runwasi shim to a
  **containerd 2.x**-compatible release (implements the v3 task service); until then
  the v2 fallback keeps those pods working, but the warning persists.
- **Hard `unsupported shim version (3)`:** the shim genuinely cannot serve this
  containerd — the fix is to **upgrade the shim/runtime**. Downgrading the containerd
  daemon to the **1.7.x** line is the upstream workaround in issue #10984, but it is
  **not a Kubespray-native path** (v2.29.0+ computes a containerd 2.x version from
  its checksums map), so treat daemon downgrade as a last resort on an unmanaged
  node only. Don't run a 2.x daemon with a 1.x-only third-party shim in production.

## References

- containerd issue #10984 (v3 task API in 2.0; *unsupported shim version (3)*),
  moby/moby #46490 (client↔shim version mismatch); containerd version in Kubespray:
  [[CONCEPT-CONTAINERD_2X]] / [[COMPONENT-CONTAINERD]].
