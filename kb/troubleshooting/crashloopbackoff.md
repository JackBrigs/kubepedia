---
id: TROUBLE-CRASHLOOPBACKOFF
type: troubleshooting
title: "Pod in CrashLoopBackOff (container keeps restarting)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - CrashLoopBackOff
  - container keeps restarting
  - pod restarting loop
  - back-off restarting failed container
  - exit code 1 container
  - liveness probe failing restart
tags:
  - troubleshooting
  - pods
  - crashloopbackoff
  - lifecycle
sources:
  - type: docs
    path: Kubernetes debug running pods / pod lifecycle
    url: https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/
    note: "CrashLoopBackOff = container exits/killed repeatedly; kubelet backs off restarts"
relations:
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
  - type: see_also
    target: TROUBLE-OOMKILLED
  - type: see_also
    target: TROUBLE-POD_CONTAINERCREATING
---

# Pod in CrashLoopBackOff (container keeps restarting)

## Summary

`CrashLoopBackOff` means the container **starts, exits/gets killed, and the kubelet
restarts it** — repeatedly, with an increasing back-off delay. It is a *state*, not a
root cause: the container is failing and you must find *why* it exits. `kubectl describe`
+ the previous container's logs point straight at it.

## Problem

`kubectl get pod` shows `CrashLoopBackOff` with a climbing `RESTARTS` count; `describe`
shows `Back-off restarting failed container` and a `Last State: Terminated` with an exit
code.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` (this is Kubernetes-native behaviour).
- The back-off grows (10s → 20s → … capped at 5m by default). Kubernetes 1.32+ can tune
  this per node via `KubeletCrashLoopBackOffMax` (`CrashLoopBackOff.MaxContainerRestartPeriod`,
  `1s`–`300s`) — see [[CONCEPT-K8S_1_32_CHANGES]]; tuning the delay does **not** fix the
  crash, it only paces restarts.

## Diagnostics

- **The two commands that solve most cases:**
  - `kubectl logs <pod> --previous` — the **crashed** container's stdout/stderr (the actual
    error). `--previous` is essential; the current attempt may not have logged yet.
  - `kubectl describe pod <pod>` — `Last State` **exit code** + `Reason`, and probe events.
- Exit-code hints: `1`/`2` = app error; **`137`** = SIGKILL, usually **OOM**
  ([[TROUBLE-OOMKILLED]]); `139` = segfault; `143` = SIGTERM (shutdown).
- Probe events: `Liveness probe failed` in `describe` → the kubelet is killing a *running*
  container because the liveness probe fails (not an app crash).

## Known Issues

Match the cause to its fix:

- **App error / bad config** (exit 1/2, error in `--previous` logs) — fix the config
  (env vars, mounted ConfigMap/Secret values), missing files, or a bad command/entrypoint.
- **Missing dependency at start** (DB/service not reachable yet) — the container exits
  before its dependency is up. Add readiness gating / init-containers / retry, or fix the
  dependency ([[TROUBLE-DNS_EXTERNAL_RESOLUTION]] if it's name resolution).
- **OOMKilled** (exit 137) — raise the memory limit / fix the leak ([[TROUBLE-OOMKILLED]]).
- **Liveness probe too aggressive** — the app is fine but the probe fails (wrong path/port,
  `initialDelaySeconds` too small for a slow start). Relax the probe; don't just raise the
  backoff.
- **Permission / read-only FS / non-root** — under PodSecurity `restricted` the container
  may be forced non-root/read-only and crash on a write ([[CONCEPT-POD_SECURITY_STANDARDS]]).
- **Wrong image / arch / entrypoint** — `exec format error` = wrong CPU arch;
  `no such file` = bad command.

**Gotchas:**

- **`--previous` is the key** — without it you read the not-yet-crashed attempt and see
  nothing. If there's no previous log, the container dies before logging → check
  `describe` exit code and the image entrypoint.
- CrashLoopBackOff is **post-start** (container ran then died); if the container never
  starts, that's `ContainerCreating`/`ErrImagePull` instead
  ([[TROUBLE-POD_CONTAINERCREATING]]).
- A crash-looping **system** pod (CNI/kube-proxy/CoreDNS) is a cluster problem, not a
  workload one — check its logs and config specifically (e.g.
  [[TROUBLE-COREDNS_RESOLUTION_LOOP]]).

## References

- Kubernetes debug-running-pod. Related lifecycle states: [[TROUBLE-POD_CONTAINERCREATING]],
  [[TROUBLE-OOMKILLED]]; symptom map: [[CONCEPT-TROUBLESHOOTING_MAP]].
