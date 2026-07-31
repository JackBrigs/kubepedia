---
id: CONCEPT-GO_RUNTIME_MEMORY
type: concept
title: "Go runtime memory vs container limits (GOMEMLIMIT, GOGC)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-31"
confidence: verified
aliases:
  - gomemlimit
  - go component oomkilled
  - garbage collector container memory limit
  - why is my go controller oom killed
tags:
  - performance
  - runtime
  - memory
sources:
  - type: docs
    path: Go runtime — GOMEMLIMIT soft memory limit (introduced in Go 1.19)
    url: https://go.dev/doc/gc-guide
    note: "soft limit: the collector runs more often as the limit approaches; it does not cap allocation"
relations:
  - type: see_also
    target: CONCEPT-SCALE_LIMITS
  - type: see_also
    target: COMPONENT-ETCD
---

# Go runtime memory vs container limits (GOMEMLIMIT, GOGC)

## Summary

A Go process is killed by the kernel, not by its own runtime. The garbage collector decides when to
run from `GOGC` — a *ratio*, by default collecting when the heap has grown 100% since the last
cycle — and knows nothing about the container's memory limit. On a workload whose live heap grows,
the next target can sit above the limit, and the OOM killer arrives first.

## Context

**`GOGC` is relative, the limit is absolute.** That mismatch is the whole problem: doubling the live
heap doubles the collection target, whatever the cgroup allows.

**`GOMEMLIMIT` (Go 1.19+) is the bridge.** It gives the runtime an absolute ceiling to aim below:
as total memory approaches it, collection becomes more frequent and more aggressive. It is a *soft*
limit — the runtime will exceed it rather than fail an allocation, so it reduces the probability of
an OOM kill instead of removing it.

**Set it below the container limit, not equal to it.** The limit governs the whole container: the
Go heap plus stacks, plus the runtime's own bookkeeping, plus anything else in the process. A common
practice is 80–90% of the container limit, leaving headroom for the non-heap part.

**Components with large working sets are the ones to look at.** etcd holding a multi-gigabyte
database, an API server on a big cluster, a controller caching every object of a large namespace
set — all keep a live heap that grows with the cluster, which is exactly where a ratio-based
collector mis-sizes itself.

## Known Issues

**An OOM kill looks like a crash, not like memory pressure.** The container exits with code 137 and
`reason: OOMKilled`; the log usually ends mid-sentence with nothing pointing at memory. Reading only
the log leads to hunting the wrong thing — check the previous container's termination state first.

**Raising the limit is not always the fix.** If the growth is a leaked cache or an unbounded watch,
a bigger limit only postpones the kill. `GOMEMLIMIT` shortens the feedback loop: with it set, the
process starts collecting harder before it dies, and continuous high CPU in the collector is itself
the signal that the working set no longer fits.

## References

- Go GC guide — `GOMEMLIMIT` semantics (soft limit, introduced 1.19), read 2026-07-31.
- Sizing: [[CONCEPT-SCALE_LIMITS]]; the component most exposed to this: [[COMPONENT-ETCD]].
