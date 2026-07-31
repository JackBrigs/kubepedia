---
id: CONCEPT-GO_RUNTIME_CPU
type: concept
title: "Go runtime parallelism vs container CPU limits (GOMAXPROCS)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-31"
confidence: verified
aliases:
  - gomaxprocs container
  - go process uses all host cpus
  - controller cpu throttling go
  - why does the go component spawn so many threads
tags:
  - performance
  - runtime
  - control-plane
sources:
  - type: docs
    path: Go 1.25 release notes — container-aware GOMAXPROCS
    url: https://go.dev/doc/go1.25
    note: "quoted: cgroup CPU *bandwidth limit* is honoured; CPU requests are explicitly not considered"
relations:
  - type: see_also
    target: CONCEPT-SCALE_LIMITS
  - type: see_also
    target: CONFIG-CPU_ISOLATION
---

# Go runtime parallelism vs container CPU limits (GOMAXPROCS)

## Summary

Practically every control-plane component in this knowledge base is written in Go: the API server,
etcd, kubelet, the CNI agents, the Gateway API controller, cert-manager, Argo CD. How much
parallelism their runtime assumes is decided by `GOMAXPROCS`, and until Go 1.25 that number came
from the **host**, not from the container.

The failure this produces is not a crash. It is a process that runs, reports healthy, and spends a
large share of its time scheduling itself.

## Context

**Before Go 1.25.** `GOMAXPROCS` defaulted to the number of logical CPUs visible at startup
(`runtime.NumCPU`). A pod limited to 2 CPUs on a 48-core node still started 48 scheduler threads.
Under load the kernel throttles it every quota period, and latency shows up as unexplained pauses —
often blamed on the network.

**Since Go 1.25**, quoting the release notes:

> On Linux, the runtime considers the CPU bandwidth limit of the cgroup containing the process, if
> any. If the CPU bandwidth limit is lower than the number of logical CPUs available, `GOMAXPROCS`
> will default to the lower limit. […] The Go runtime does not consider the "CPU requests" option.

and

> On all OSes, the runtime periodically updates `GOMAXPROCS` if the number of logical CPUs available
> or the cgroup CPU bandwidth limit change.

**The sentence that matters operationally is the one about requests.** The runtime reads the
**limit**. A pod with `requests: cpu: 100m` and *no limit* has no cgroup bandwidth limit at all, so
even on Go 1.25 the runtime sizes itself to the whole node. Requests only decide scheduling and the
CPU share under contention — the process still believes it owns every core.

That combination — a small request, no limit, a busy node — is the worst of both: the runtime
assumes wide parallelism while the scheduler grants it a thin slice under contention. It appears as
slow reconciliation and missed deadlines, including leader-election renewals.

**Overriding.** The behaviour can be pinned with the `GOMAXPROCS` environment variable, or disabled
with `GODEBUG=containermaxprocs=0,updatemaxprocs=0`. Setting the environment variable explicitly is
the portable option across Go versions and is how a component built with an older Go is fixed
without rebuilding it.

## Known Issues

**Which Go a component was built with is not obvious.** The version in the image, not the cluster,
decides the behaviour; a 2026 release can still be built with an older toolchain. Component release
notes usually record toolchain bumps ("Bump golang to 1.25.8"), which is the practical way to find
out.

**Setting a CPU limit is not automatically the fix.** A limit makes the runtime size itself
correctly, but it also introduces throttling. For latency-sensitive control-plane components the
common recommendation is the opposite — no limit, adequate requests — and then `GOMAXPROCS` must be
set explicitly, because the runtime has nothing to read.

## References

- Go 1.25 release notes, "container-aware GOMAXPROCS" — quoted above, read 2026-07-31.
- Node-level CPU behaviour: [[CONFIG-CPU_ISOLATION]]; sizing: [[CONCEPT-SCALE_LIMITS]].
