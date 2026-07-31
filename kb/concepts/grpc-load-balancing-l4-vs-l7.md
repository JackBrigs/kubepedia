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
# 1. the port inside the container is not the Service port — resolve it first
kubectl get svc <svc> -o jsonpath='{range .spec.ports[*]}{.name}{" port="}{.port}{" target="}{.targetPort}{"\n"}{end}'

# 2. count established connections to that target port, per replica.
#    /proc/net/* is used rather than ss/netstat: application images usually have neither.
#    Ports there are hex, and a socket bound on an IPv4-mapped address lands in tcp6, not tcp.
PORT_HEX=$(printf '%04X' <target-port>)
for p in $(kubectl get pods -l app=<server> -o name); do
  n=$(kubectl exec $p -- cat /proc/net/tcp6 2>/dev/null \
      | awk -v h=":$PORT_HEX" '$2 ~ h"$" && $4=="01"' | wc -l)
  echo "$p  established=$n"
done

# 3. distinct clients per replica — the number that actually decides whether it is pinned
kubectl exec <pod> -- cat /proc/net/tcp6 \
  | awk -v h=":$PORT_HEX" '$2 ~ h"$" && $4=="01" {split($3,a,":"); print a[1]}' | sort -u | wc -l
```

Three traps make this measurement read as "no traffic at all" when it is measured naively, and all
three were hit while writing this page: the container port differs from the Service port; the
connections live in `tcp6` because the listener binds an IPv4-mapped address; and ports in
`/proc/net/*` are hexadecimal. A confident zero is the expected result of getting any of them wrong.

One connection per client and a wildly uneven distribution across replicas confirms pinning. Many
distinct clients per replica means the opposite — with enough clients the imbalance averages out on
its own, which is why the pathology is a small-fleet problem rather than a large one.

**Rule out the other causes first.** Uneven CPU across replicas has several explanations, and
connection pinning is only one:

| Observation | Likely cause |
|---|---|
| few connections, very uneven CPU | not inbound traffic at all — a queue consumer, partition assignment, a leader-elected background job |
| even connections, uneven CPU | one replica doing extra work (scheduler, cron, cache warming) |
| one connection per client, uneven CPU | connection pinning — this page |

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
