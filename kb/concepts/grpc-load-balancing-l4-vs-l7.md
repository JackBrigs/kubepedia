---
id: CONCEPT-GRPC_LOAD_BALANCING
type: concept
title: "gRPC and HTTP/2 are not load-balanced by a Kubernetes Service"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-31"
confidence: verified
aliases:
  - grpc load balancing kubernetes service
  - one pod gets all the grpc traffic
  - http2 single tcp connection imbalance
  - scaling replicas does not spread grpc load
  - headless service client side load balancing
  - grpc max connection age goaway
tags:
  - networking
  - grpc
  - load-balancing
sources:
  - type: docs
    path: "Don't load balance gRPC or HTTP2 using Kubernetes Service (lapwingcloud)"
    url: https://medium.com/@lapwingcloud/dont-load-balance-grpc-or-http2-using-kubernetes-service-ae71be026d7f
    note: "states the core mechanism: a Service is an L4 passthrough and sees one TCP connection, not the requests multiplexed on it"
  - type: docs
    path: google.golang.org/grpc/keepalive — ServerParameters
    url: https://pkg.go.dev/google.golang.org/grpc/keepalive
    note: "quoted: MaxConnectionAge closes the connection by sending a GoAway, with +/-10% jitter to spread out connection storms"
relations:
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
  - type: see_also
    target: COMPONENT-CILIUM
---

# gRPC and HTTP/2 are not load-balanced by a Kubernetes Service

## Summary

A Kubernetes Service balances **connections**, not requests. HTTP/2 — and therefore gRPC — opens
**one long-lived TCP connection** and multiplexes every request onto it. The two facts together mean
a client pod picks one server pod at connect time and keeps talking to it until something closes the
connection.

The result is not an error. It is a cluster where one replica runs hot, the others idle, and scaling
up changes nothing.

## Context

**Why the Service cannot help.** kube-proxy — and equally Cilium's eBPF replacement, which is the
data path in this estate — makes its decision once, when the connection is established. From that
point it forwards packets. It has no view of the HTTP/2 frames inside, so it cannot spread the
requests riding on that connection.

This is worth stating explicitly because "we replaced kube-proxy with Cilium" does not change the
outcome: the eBPF service load balancer is still L4. Cilium can balance gRPC per request only where
its **Envoy** is on the path (an L7 policy or Gateway API), not in the eBPF fast path.

**The imbalance is worst exactly where it is least expected**: few clients, many server replicas.
Ten replicas behind three client pods will see at most three of them used. Adding replicas dilutes
nothing — existing connections stay where they are.

**North-south traffic is usually fine.** A gateway that terminates HTTP/2 (Envoy Gateway,
ingress-nginx with `backend-protocol: GRPC`) is an L7 proxy: it re-balances per request across ready
endpoints. The problem lives in **service-to-service** calls that go straight to a ClusterIP.

## Implementation

Three remedies, in the order they are usually worth trying.

**1. Server-side connection ageing — the cheapest, and the one the article omits.** Configure the
gRPC server to retire connections periodically so clients reconnect and land somewhere new. Quoting
the `keepalive` package: `MaxConnectionAge` is

> a duration for the maximum amount of time a connection may exist before it will be closed by
> sending a GoAway. A random jitter of +/-10% will be added to MaxConnectionAge to spread out
> connection storms.

with `MaxConnectionAgeGrace` as the additive period before a forcible close. Both default to
infinity — which is precisely why connections pin forever by default. This requires no topology
change and no client cooperation beyond honouring GOAWAY, which every conformant client does.

**2. Headless Service plus client-side balancing.** Set `clusterIP: None`, let DNS return every pod
IP, and have the client round-robin across them. Note that the API in most write-ups is outdated:
`grpc.WithBalancerName` is deprecated. The current form is a default service config, for example
`grpc.WithDefaultServiceConfig('{"loadBalancingConfig":[{"round_robin":{}}]}')` with a `dns:///`
target. The cost is that rebalancing now depends on DNS freshness and on the client library, and
every client language has to implement it.

**3. Put an L7 proxy on the path.** A gateway or a mesh sidecar terminates HTTP/2 and balances per
request. This is the most robust and the most expensive: an extra hop, extra failure modes and, for
a mesh, a sidecar per pod.

## Known Issues

**The symptom is read as an application problem.** One replica at high CPU while the rest idle looks
like a hot partition, a slow database shard or a leak. The distinguishing check is at the connection
level, not the metric level:

```bash
# on a client pod: how many established connections to the service, and to how many distinct peers
kubectl exec <client-pod> -- ss -tn state established | awk '{print $4, $5}' | sort | uniq -c
# on the server side: connections per replica
for p in $(kubectl get pods -l app=<server> -o name); do
  echo -n "$p "; kubectl exec $p -- ss -tn state established | wc -l
done
```

A count of one connection per client and a wildly uneven distribution across replicas confirms it.

**A rollout hides the problem and then it returns.** Restarting the server pods forces every client
to reconnect, which redistributes traffic — for a while. Load looks balanced right after a deploy
and drifts back over days, which is why this is often diagnosed as "it degrades over time".

**Connection ageing interacts with long streams.** `MaxConnectionAge` closes connections while
streaming RPCs may be in flight; `MaxConnectionAgeGrace` exists exactly for that. Set the grace
period longer than the longest expected stream, or long-running calls will be cut.

## References

- lapwingcloud, "Don't load balance gRPC or HTTP2 using Kubernetes Service" — the L4 passthrough
  argument, read 2026-07-31.
- `google.golang.org/grpc/keepalive` `ServerParameters` — `MaxConnectionAge` / `MaxConnectionAgeGrace`
  semantics quoted above.
- Gateway on the north-south path: [[CONCEPT-ADDON_ENVOY_GATEWAY]]; the eBPF data path:
  [[COMPONENT-CILIUM]].
