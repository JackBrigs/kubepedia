---
id: TROUBLE-ENVOY_GATEWAY_RESTART_LOOP
type: troubleshooting
title: "Envoy Gateway controller restart loop: lease renewal times out, kubelet kills the container"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - envoy gateway restarts every 30 minutes
  - envoy gateway leader election lost
  - unable to start provider leader election lost
  - failed to renew lease context deadline exceeded
  - gateway controller crashloop but pod running
  - liveness probe failed 8081 connection refused
tags:
  - troubleshooting
  - envoy
  - gateway-api
  - control-plane
  - leader-election
sources:
  - type: code
    path: envoyproxy/gateway v1.6.0 internal/provider/kubernetes/kubernetes.go:228
    note: "Provider.Start blocks on manager.Start(ctx); its error ends the whole process — no re-election"
  - type: code
    path: envoyproxy/gateway v1.6.0 internal/provider/runner/runner.go:69
    note: "logs `unable to start provider` with error `leader election lost`"
  - type: code
    path: envoyproxy/gateway v1.6.0 api/v1alpha1/envoygateway_types.go:27-30
    note: "DefaultKubernetesClientQPS = 50, DefaultKubernetesClientBurst = 100"
  - type: docs
    path: live incident — 65 restarts in 25 h on an exact 30-minute cadence, 1411 routes, one replica
    note: "lease PUT/GET with ?timeout=5s exceeded; kubelet events `failed liveness probe, will be restarted` x65"
relations:
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_LEADER_LOSS_503
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
---

# Envoy Gateway controller restart loop: lease renewal times out, kubelet kills the container

## Summary

The Envoy Gateway **controller** restarts on a fixed cadence — in the observed cluster every 30
minutes, to the second, 65 times in 25 hours — while the pod stays `Running` the whole time and no
dashboard shows anything wrong. Each restart forces a full re-translation of every route, which is
what makes it worth chasing (see [[TROUBLE-ENVOY_GATEWAY_LEADER_LOSS_503]]).

The chain is: a call to the leader-election `Lease` **times out at 5 seconds** → the controller
declares leadership lost → the manager stops and closes its health port → kubelet's liveness probe
gets `connection refused` → kubelet kills the container. Nothing here is a crash: `exitCode` is 0
and `reason` is `Completed`.

## Problem

One full cycle, from the previous container's log:

```
06:03:45  started
06:32:47  Failed to update lock optimistically: Put .../leases/<id>?timeout=5s:
          net/http: request canceled (Client.Timeout exceeded while awaiting headers), falling back to slow path
06:32:52  error retrieving resource lock ...?timeout=5s: context deadline exceeded
06:32:52  failed to renew lease <ns>/<id>: context deadline exceeded
06:32:52  unable to start provider   {"error": "leader election lost"}
06:32:52  Stopping and waiting for leader election runnables   ← health port 8081 closes here
06:33:44  kubelet: Container envoy-gateway failed liveness probe, will be restarted
06:33:45  started again
```

Pod events confirm who does the killing:

```
Warning  Unhealthy  Liveness probe failed: dial tcp <podIP>:8081: connect: connection refused   (x194 / 25h)
Normal   Killing    Container envoy-gateway failed liveness probe, will be restarted            (x65  / 25h)
```

**Do not read `http2: client connection lost` as the cause.** That line appears *after* the decision
to stop, when the shutting-down process fails to write its own `stopped leading` Event into closing
connections. The real trigger is on the lines above it: a request that did not come back within its
5-second budget. Reading the tail of the log alone inverts cause and effect.

## Context

**Why one timeout kills the process.** `Provider.Start` blocks on `manager.Start(ctx)` and returns
whatever it returns (`internal/provider/kubernetes/kubernetes.go:228`); the runner then logs
`unable to start provider` (`internal/provider/runner/runner.go:69`) and the process ends. There is
no code path that re-enters the election and carries on — losing leadership once is fatal by design,
so that two instances can never program the proxies at the same time.

**Why the cadence is so exact.** The restart interval is *internal work time + probe detection
time*, and both are constants: ~29 minutes until the renewal fails, then three liveness failures at
`periodSeconds: 20` before kubelet acts — about one more minute. Hence a metronome-like 30 minutes
with identical seconds.

**Where the 29 minutes come from.** Not from Envoy Gateway: there is no such timer anywhere in
`internal/`. It comes from the API-server side. A candidate worth testing first: `kube-apiserver`
leaves `--min-request-timeout` at its default of **1800 s**, so long-running watches are torn down
around the 30-minute mark and the client re-establishes them all at once. The controller's client is
capped at **QPS 50 / burst 100** by default (`api/v1alpha1/envoygateway_types.go:27-30`); with a
large object set that re-subscription burst can occupy the queue long enough for the lease call —
budgeted at 5 s — to expire behind it.

**Scale is part of the cause.** The observed cluster ran 1009 HTTPRoute + 402 GRPCRoute through a
single replica requesting `cpu: 100m`. Abandoned per-branch environments inflate that count without
serving anyone.

**Not an upstream defect.** A search of `envoyproxy/gateway` returns **zero** reports containing
`stopped leading`; leader election itself landed long ago (PRs #2123, #2694, nil-guard #3096, tests
#4420). Treat this as defaults meeting scale, not as a product bug.

## Diagnostics

```bash
EG_NS=envoy-gateway

# 1. Is it a loop? RESTARTS climbs while the pod stays Running
kubectl -n $EG_NS get pods

# 2. Who kills it — events name the executioner
kubectl -n $EG_NS describe pod <controller-pod> | sed -n '/Events:/,$p'
#    "failed liveness probe, will be restarted"  ⇒ kubelet, after the health port closed
#    OOMKilled / Error                           ⇒ a different problem entirely

# 3. Why leadership was lost — read the lines BEFORE the shutdown block
kubectl -n $EG_NS logs <controller-pod> --previous \
  | grep -iE "renew|resource lock|leader election lost|Client.Timeout"

# 4. Current knobs (absent section ⇒ library defaults apply)
kubectl -n $EG_NS get cm envoy-gateway-config -o jsonpath='{.data.envoy-gateway\.yaml}'

# 5. Confirm the cadence
kubectl -n $EG_NS get pod <controller-pod> \
  -o jsonpath='{.status.containerStatuses[0].restartCount}{"  "}{.status.containerStatuses[0].state.running.startedAt}{"\n"}'
```

Two samples of `restartCount` a while apart give the true rate — a single count over pod age hides
whether the loop is old or started today.

## Known Issues

**Ordinary monitoring cannot see this.** The pod never leaves `Running`, so pod-health dashboards
stay green through hundreds of restarts. The only reliable signal is the restart counter:

```promql
increase(kube_pod_container_status_restarts_total{namespace="envoy-gateway"}[1h]) > 1
```

**Remediation, in order:**

1. **Raise the client rate limit** — the defaults are the likely bottleneck:

   ```yaml
   provider:
     kubernetes:
       client:
         rateLimit:
           qps: 200
           burst: 400
   ```

2. **Give leadership renewal room to survive one slow call:**

   ```yaml
   provider:
     kubernetes:
       leaderElection:
         leaseDuration: 60s
         renewDeadline: 40s
         retryPeriod: 5s
   ```

3. **Raise the controller's `requests`.** `cpu: 100m` for a process translating >1000 routes makes
   it the first casualty of any contention on the node.

4. **Single replica? Consider `leaderElection.disable: true`.** Election buys nothing with one
   instance, and losing it is the only thing ending the process. Re-enable it before scaling to two
   replicas — otherwise both would program the proxies simultaneously.

5. **Delete dead per-branch environments.** Fewer objects, shorter translation, smaller
   re-subscription burst.

Options 1–2 are configuration only, applied by editing the `EnvoyGateway` config; both change
behaviour on controller restart, which the loop supplies on its own.

## References

- Code read at tag **v1.6.0**: `internal/provider/kubernetes/kubernetes.go:228`,
  `internal/provider/runner/runner.go:69`, `api/v1alpha1/envoygateway_types.go:27-30`.
- Consequence of each restart: [[TROUBLE-ENVOY_GATEWAY_LEADER_LOSS_503]]; add-on:
  [[CONCEPT-ADDON_ENVOY_GATEWAY]].
