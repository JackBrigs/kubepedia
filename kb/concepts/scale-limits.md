---
id: CONCEPT-SCALE_LIMITS
type: concept
title: "Scale limits — what breaks as nodes/pods/services grow, and the knob for each"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - what breaks at scale
  - kubernetes scale ceilings
  - large cluster failure modes
  - scale tuning knobs
  - cluster sizing limits
tags:
  - concept
  - scale
  - troubleshooting
  - index
sources:
  - type: analysis
    path: kubepedia/scale failure modes
    note: "curated from the atomic scale-related docs; each row links to its dedicated doc/knob"
  - type: docs
    path: docs/operations/large-deployments.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/large-deployments.md
    note: "Kubespray-side tuning levers for large clusters"
relations:
  - type: see_also
    target: PRACTICE-LARGE_DEPLOYMENTS
  - type: see_also
    target: TROUBLE-CONNTRACK_TABLE_FULL
  - type: see_also
    target: TROUBLE-ARP_NEIGH_TABLE_OVERFLOW
  - type: see_also
    target: TROUBLE-APISERVER_MEMORY_LISTS
  - type: see_also
    target: TROUBLE-KCM_ENDPOINTSLICE_CHURN
  - type: see_also
    target: TROUBLE-SCHEDULER_PERF
---

# Scale limits — what breaks as nodes/pods/services grow, and the knob for each

## Summary

Most defaults are tuned for small/medium clusters. As a cluster grows — more **nodes**, **pods per
node**, **services/endpoints**, or **connection churn** — you cross a series of ceilings that each show
up as a different, often intermittent failure. This is the **scale spine**: a catalog of the known
ceilings in the Kubespray range (v2.27.0–v2.31.0), the symptom, and the knob or doc that fixes it.
Pair it with Kubespray's large-deployment tuning ([[PRACTICE-LARGE_DEPLOYMENTS]]).

## Context

Grows-with axis tells you *when* to expect each: **N** = nodes, **P** = pods, **S** = services/
endpoints, **C** = connections/churn.

| Grows with | Ceiling / resource | Symptom at scale | Knob / doc |
|---|---|---|---|
| C | conntrack table | `nf_conntrack: table full`, dropped connections | [[TROUBLE-CONNTRACK_TABLE_FULL]] |
| N,P | ARP/NDP neighbour cache | `neighbour table overflow`, intermittent drops | [[TROUBLE-ARP_NEIGH_TABLE_OVERFLOW]] |
| P | inotify watches/instances | `too many open files` / watches exhausted (kubelet, apps) | [[TROUBLE-INOTIFY_FILE_LIMITS]] |
| P,C | container runtime open files | fd exhaustion in containerd | `containerd_limit_open_file_num` [[VARIABLE-CONTAINERD_LIMIT_OPEN_FILE_NUM]] |
| P,S | apiserver LIST memory | apiserver OOM / latency on large LIST/watch | [[TROUBLE-APISERVER_MEMORY_LISTS]], [[TROUBLE-APISERVER_REQUEST_LATENCY]] |
| P,S | etcd DB size / event volume | `mvcc: database space exceeded`; slow writes | [[TROUBLE-ETCD_DB_SPACE_EXCEEDED]]; split events: `etcd_events_cluster_setup` [[VARIABLE-ETCD_EVENTS_CLUSTER_SETUP]] |
| P | scheduler throughput | slow scheduling / backlog of Pending | [[TROUBLE-SCHEDULER_PERF]] |
| S | EndpointSlice churn / topology | routing thrash, zone endpoint starvation | [[TROUBLE-KCM_ENDPOINTSLICE_CHURN]] |
| S | kube-proxy dataplane | large service count → slow sync (iptables O(n)); prefer IPVS/nftables | [[CONCEPT-KUBE_PROXY]] |
| P | CoreDNS QPS | DNS latency/timeouts under load | scale replicas via `enable_dns_autoscaler` [[VARIABLE-ENABLE_DNS_AUTOSCALER]] |
| P | pod density per node (PLEG, maxPods) | `PLEG is not healthy`; pods rejected past `maxPods` | [[TROUBLE-KUBELET_PLEG_NOT_HEALTHY]]; `kubelet_max_pods` [[VARIABLE-KUBELET_MAX_PODS]] |
| N | podCIDR node-prefix block | new node gets no PodCIDR (block exhausted) | [[TROUBLE-ADD_NODE_GOTCHAS]] |
| P | image pull throughput | `ImagePullBackOff` from registry rate limits | [[TROUBLE-IMAGE_PULL_RATE_LIMIT]] |
| P,S | policy-engine report volume (Kyverno) | policy reports bloat etcd at scale | [[TROUBLE-KYVERNO_REPORTS_ETCD_SCALE]] |

**Plan ceilings up front.** Two of these can't be fixed *at* the moment they bite without a re-plan:
the **podCIDR node-prefix** caps the node count (size `kube_pods_subnet` / `kube_network_node_prefix`
before you need the nodes), and the **service/pod CIDR** caps total IPs. Everything else is a sysctl or
resource/replica bump you can apply as you grow — but watch for them *before* the outage, not after.

**kube-proxy at scale:** iptables mode rebuilds rules roughly linearly with service/endpoint count, so
sync time grows and dataplane updates lag; **IPVS** (hash-based) or **nftables** mode scales better for
large service counts ([[CONCEPT-KUBE_PROXY]]) — a dataplane choice, not just a knob.

## References

- Curated from the atomic scale docs; Kubespray large-deployment tuning
  ([[PRACTICE-LARGE_DEPLOYMENTS]]). Each row links its own source-backed doc/knob.
