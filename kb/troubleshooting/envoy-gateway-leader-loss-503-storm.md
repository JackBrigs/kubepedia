---
id: TROUBLE-ENVOY_GATEWAY_LEADER_LOSS_503
type: troubleshooting
title: "Envoy Gateway: controller loses leader lease → cluster-wide 503/500 burst"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.0.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - grpc stopped working inside cluster
  - envoy gateway 503 no ready endpoints
  - gateway api routes return 503 suddenly
  - stopped leading envoy gateway
  - http2 client connection lost apiserver
  - all routes 503 at once
tags:
  - troubleshooting
  - envoy
  - gateway-api
  - grpc
  - control-plane
  - incident
sources:
  - type: docs
    path: live incident, Envoy Gateway v1.6.0, ~1400 routes, single controller replica
    note: "controller log `stopped leading` + `http2: client connection lost`; Lease leaseDurationSeconds=15; 61 restarts in 8 days; 503 burst 3.5 min after restart"
  - type: docs
    path: Envoy Gateway configuration — EnvoyGateway API
    url: https://gateway.envoyproxy.io/docs/api/extension_types/
    note: "provider.kubernetes.leaderElection; absent from config ⇒ controller-runtime defaults apply"
relations:
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_BACKEND_TLS_SNI
---

# Envoy Gateway: controller loses leader lease → cluster-wide 503/500 burst

## Summary

Hundreds of routes — HTTPRoute and GRPCRoute alike — are logged as answering `503` (some `500`)
within the same ~100 ms, and applications report it as "gRPC transport died inside the cluster".
The proxies did not restart and the data plane is healthy.

What happened: the **controller lost its leader-election lease**, exited (cleanly, code 0),
restarted, and re-translated every route. The trigger for losing the lease is anything that breaks
the controller's long-lived HTTP/2 connection to the API server — **most reliably, a
`kube-apiserver` restart**, which any Kubespray `cluster.yml` run or a manual edit of the static-pod
manifest produces.

**Read the burst carefully before blaming it.** A re-translation *reports* backend state; it does
not by itself break working routes. Two very different situations produce the same log flood:

- backends that were **already** dead (abandoned per-branch environments, CrashLoopBackOff pods,
  Services with no pods) — the controller merely enumerates them on every restart;
- backends that are **fine**, listed as absent only because the informer cache was not yet warm —
  this one is real damage, and it is the case worth escalating.

Telling them apart takes one check (below). In the incident this document is written from, only
per-branch environments appeared in the burst; `prod` / `release` / `develop` routes did not — so
the restart most likely surfaced pre-existing breakage rather than causing an outage. The restart
loop was still a genuine defect: 62 restarts, one every 30 minutes.

## Problem

The controller log shows hundreds of lines within ~100 ms — a bulk re-translation, not pods
failing one by one:

```
setting 503 direct response in routes due to no ready endpoints   {"routes": ["grpcroute/<ns>/<name>/rule/0/match/-1"]}
setting 500 direct response in routes due to errors in processing destinations
    {"routes": ["httproute/<ns>/<name>/..."], "error": "service <ns>/<svc> not found"}
```

Two distinct classes, and they mean different things:

| Message | Meaning |
|---|---|
| `no ready endpoints` → **503** | the Service exists, no ready pod behind it *as far as the controller currently knows* |
| `... not found` → **500** | the Service object is absent from the controller's cache |

The previous container's log names the cause:

```
Message:... stopped leading
error: Post "https://<kubernetes-svc-ip>:443/api/v1/namespaces/envoy-gateway/events":
       http2: client connection lost
```

## Context

**Why losing the lease stops everything.** The controller renews a `coordination.k8s.io/v1` Lease
to prove it is still the leader (`leaseDurationSeconds: 15` in the observed cluster — the
controller-runtime default; the client-side renew deadline is shorter). Renewals travel over the
*same* long-lived HTTP/2 connection as every watch. If the connection drops and the renewal window
expires, the controller must stop leading — otherwise two instances could push conflicting xDS
snapshots. It therefore shuts down with exit code **0**. This is correct behaviour, not a crash;
`restartCount` grows while `reason: Completed` and `exitCode: 0`.

**Why the restart hurts.** On start the controller re-translates *all* routes. Until the informer
cache is populated, backends legitimately look absent, and the translation result is a direct-response
503/500 — which is pushed to the proxies as real configuration. Blast radius scales with the object
count: in the observed cluster **1009 HTTPRoute + 402 GRPCRoute**, one replica, `requests: cpu 100m`.

**Why gRPC gets blamed.** gRPC clients surface the failure loudly (long-lived HTTP/2 streams,
`Unavailable`/`Cancelled`), while HTTP clients retry and hide it. The log proves both are affected
equally — that single fact rules out "gRPC/GRPCRoute is broken" within seconds.

**Amplifiers.** Dead per-branch environments (Services whose selector matches no pod, routes of
merged branches) make every translation heavier and enlarge the burst without adding value.

## Diagnostics

Order matters — the first two commands separate this failure mode from a genuine outage:

```bash
# 1. Is the data plane actually broken? (usually not)
kubectl get pods -A --field-selector status.phase=Pending          # expect: none
kubectl get events -A --field-selector reason=FailedScheduling     # expect: none

# 2. Has the controller been restarting?
kubectl -n <eg-ns> get pods                                        # RESTARTS column
kubectl -n <eg-ns> get pod <controller> -o jsonpath='{.status.containerStatuses[0].lastState.terminated}'
#    reason=Completed, exitCode=0  ⇒ leader-lease loss, not a crash

# 3. Confirm the cause in the previous instance's log
kubectl -n <eg-ns> logs <controller> --previous | grep -E "stopped leading|connection lost"

# 4. Correlate: did an apiserver restart at that moment?
kubectl -n kube-system get pods -l component=kube-apiserver \
  -o custom-columns='POD:.metadata.name,START:.status.startTime,RESTARTS:.status.containerStatuses[0].restartCount'

# 5. Measure the current burst (should fall to zero once translation completes)
kubectl -n <eg-ns> logs deploy/envoy-gateway --since=15m | grep -c 'no ready endpoints'
kubectl -n <eg-ns> logs deploy/envoy-gateway --since=15m | grep -c 'not found'

# 6. Separate transient from permanent: Services that really have no backend
kubectl get endpoints -n <app-ns> --no-headers | awk '$2=="<none>"' | wc -l
```

A `503` count that decays to 0 while endpoints stay non-empty confirms this failure mode.
Endpoints that are permanently `<none>` are a separate, application-side problem.

**The decisive check — did clients actually get a 503?** The controller log cannot answer this; the
proxy access log can. Three outcomes, distinguishable per request:

| Situation | `response_code_details` | `upstream` | response flags |
|---|---|---|---|
| normal | `via_upstream` | backend address | `-` |
| **answered from configuration** (the controller programmed a direct response) | not `via_upstream` | empty | `-` |
| backend genuinely unreachable | — | empty | `UH` / `UF` |

Search the window for `status: 503` and look at those fields. 503s confined to routes whose
backends were already dead mean the restart only reported existing breakage. 503s on routes that
normally work — with no upstream and no failure flags — mean the cold cache really did serve
errors to clients.

Proxy access logs rotate fast under load (thousands of requests per minute per proxy), so pull this
from central log storage, not from the node.

## Known Issues

**The restart loop is invisible to ordinary monitoring.** In the observed cluster the controller
had restarted **62 times in 9 days**, on an exact 30-minute cadence, while the pod stayed `Running`
the whole time — dashboards that watch pod health show nothing. Restart-count alerting is the only
thing that catches it.

**Do not assume user impact — prove it.** Whether a burst reached clients is decided in the proxy
access log, not in the controller log; see the discriminator above. Claiming an outage from the
controller log alone is the easy mistake this document exists to prevent.

**Kubespray runs trigger it.** `cluster.yml` and any hand-edit of
`/etc/kubernetes/manifests/kube-apiserver.yaml` restart the API server and break the controller's
connection. On a three-master cluster Kubespray's control-plane play has **no `serial`**, so the
restarts can land close together. Expect a 503 burst during maintenance windows and do not mistake
it for damage caused by the maintenance itself.

**Remediation, in order of value:**

1. **Run more than one controller replica.** A standby with a warm cache takes over on lease loss
   instead of a cold start — the burst shrinks to the takeover window.
2. **Give the controller real `requests`.** 100m CPU for a process translating ~1400 routes makes it
   the first victim of any CPU contention, and slow renewals lose the lease on their own.
3. **Tune leader election** via `provider.kubernetes.leaderElection` in the `EnvoyGateway` config
   (longer lease/renew windows survive short API-server outages). Verify the field names against the
   Envoy Gateway version in use — the section is absent from a default config, in which case
   controller-runtime defaults apply.
4. **Delete dead branch environments** — orphaned Services and routes inflate every translation.
5. If bursts continue without any API-server restart, look at API-server latency and etcd health
   (a multi-GB etcd database makes renewals slow); see [[CONCEPT-ADDON_ETCD_DEFRAG_CONTROLLER]].

**What is *not* the cause:** draining or removing a control-plane node does not evict application
pods — control-plane nodes carry `node-role.kubernetes.io/control-plane:NoSchedule`. Check the taint
before blaming node maintenance for missing endpoints.

## References

- Controller log (`stopped leading`, `http2: client connection lost`), `Lease`
  `leaseDurationSeconds: 15`, `lastState.terminated{reason: Completed, exitCode: 0}` — read from a
  live cluster on 2026-07-31, Envoy Gateway v1.6.0.
- Add-on: [[CONCEPT-ADDON_ENVOY_GATEWAY]]; upgrade-side pitfalls of the same component:
  [[TROUBLE-ENVOY_GATEWAY_BACKEND_TLS_SNI]].
