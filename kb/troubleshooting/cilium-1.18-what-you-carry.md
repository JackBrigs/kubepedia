---
id: TROUBLE-CILIUM_1_18_EXPOSURE
type: troubleshooting
title: "Cilium 1.18.4: what a cluster on this pin is still carrying"
status: active
kubespray_version: ">=v2.29.0 <=v2.29.1"
kubernetes_version: null
component_version: ">=1.18.2 <=1.18.4"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.18.4 known issues
  - endpoints stuck waiting-to-regenerate
  - cilium policy not updated with new identities
  - cilium memory leak policy updates
  - intermittent packet drops fqdn policy
  - should we upgrade cilium 1.18
tags:
  - troubleshooting
  - cilium
  - network-policy
  - upgrade
sources:
  - type: docs
    path: cilium/cilium release notes 1.18.5 – 1.18.12 (bug-fix entries)
    url: https://github.com/cilium/cilium/releases
    note: "extracted 2026-07-31; only fixes released above 1.18.4 on the same maintenance line"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: TROUBLE-CILIUM_KNOWN_CVES
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# Cilium 1.18.4: what a cluster on this pin is still carrying

## Summary

Kubespray v2.29.1 pins Cilium **1.18.4**. Eight patch releases have landed above it on the same
line, carrying roughly **90 fixes**, of which about **28 change network behaviour** rather than
cosmetics.

Three groups matter, and all three produce symptoms that get investigated as application faults:
**policies that silently stop being enforced correctly**, **endpoints that stop progressing**, and
**memory that grows with policy churn**.

## Problem

**Policies stop reflecting reality.**

- *Rare endpoint-selector policy deadlock causing policies not to be updated with new identities*
  (1.18.5). New pods get identities the policy engine never applies — traffic is allowed or denied
  by a stale picture, and nothing logs an error.
- *Policy update acknowledgement never completes after endpoint deletion* (1.18.9).
- *Incorrect policy denials for traffic to L7 load-balanced services when the remote identity
  changes* (1.18.12). Connections that worked yesterday start being denied after an unrelated
  redeploy on the other side.
- *Wildcard FQDN policy identities were not pushed to Envoy for SNI-based policies* (1.18.8).

**Endpoints stop progressing.**

- *Endpoints stuck in `waiting-to-regenerate`* (1.18.5) and a *deadlock leaving endpoints stuck
  without progressing with any updates* (1.18.6). The pod is Running, the agent is Running, and the
  datapath for that endpoint is simply frozen at an older state.
- *cilium-agent crash on a transient network error during CiliumNode update* — the agent called
  `Fatal` instead of retrying (1.18.10).

**Memory grows with policy churn.**

- *Slow memory leak triggered by incremental policy updates* and *memory leak triggered by policies
  being created and deleted* (both 1.18.9), plus a *leak in CIDR metadata consolidation* (1.18.5)
  and one *in the watch channel hash map of very large StateDB transactions* (1.18.11).

On a cluster where per-branch environments are created and destroyed all day — which is exactly the
deployment pattern in this estate — policy objects churn constantly, so these are the leaks that
actually fire.

**Service and datapath correctness, individually rarer but sharp:**

- removing an endpoint from Service A could break **all requests to Service B** when names collide
  (1.18.7);
- `loadBalancerSourceRanges` applied by default to **all service types** — a regression in the new
  services control plane (1.18.6);
- ICMP error packets mishandled for SNATed load-balanced traffic (missing checksum recalculation,
  1.18.7) — this breaks path-MTU discovery, which surfaces as large responses hanging while small
  ones work;
- removed addresses missed when several EndpointSlices share a name (1.18.8);
- `CiliumLocalRedirectPolicy` overriding an existing Service frontend while backends are not yet
  Ready (1.18.10);
- FQDN correctness issues *causing packet drops and inconsistent ipcache* (1.18.5).

## Context

| Release | Behaviour-affecting fixes |
|---|---|
| 1.18.5 | endpoints stuck regenerating; FQDN drops + ipcache inconsistency; policy deadlock vs new identities; CIDR metadata leak |
| 1.18.6 | endpoint deadlock; `loadBalancerSourceRanges` applied to all service types; proxy NOTRACK/SNAT in chaining mode |
| 1.18.7 | cross-service failure on name collision; ICMP checksum on RevNAT |
| 1.18.8 | EndpointSlice name collisions; wildcard FQDN identities to Envoy; VTEP ARP returning a zero MAC |
| 1.18.9 | two policy-related memory leaks; L7 redirect performance; Hubble Relay panic; dual-stack IPAM restart bug; policy ack after endpoint deletion |
| 1.18.10 | agent crash on transient API error; local redirect policy overriding a frontend |
| 1.18.11 | StateDB watch-channel leak |
| 1.18.12 | wrong policy denials on identity change; start failure in kvstore mode with KPR behind a Service |

## Diagnostics

```bash
# endpoints not converging — the signature of the 1.18.5/1.18.6 deadlocks
kubectl -n kube-system exec ds/cilium -- cilium-dbg endpoint list \
  | awk '$0 !~ /ready/ {print}' | head

# agent restarts that look like nothing (Fatal on a transient error, 1.18.10)
kubectl -n kube-system get pods -l k8s-app=cilium \
  -o custom-columns=POD:.metadata.name,RESTARTS:.status.containerStatuses[0].restartCount

# memory trend on the agents — the leaks are slow, so compare across days, not minutes
kubectl -n kube-system top pods -l k8s-app=cilium --sort-by=memory | head

# policy state vs identities
kubectl -n kube-system exec ds/cilium -- cilium-dbg status --verbose | grep -A3 -i policy
```

An endpoint list where entries sit outside `ready` while the agent reports healthy is the tell for
the regeneration deadlock: nothing is failing, everything has simply stopped moving.

## Known Issues

**These are not upgrade-blocking changes** — all of them are patches inside the 1.18 line, so the
Gateway API CRDs and the datapath configuration stay as they are. The cost is a rolling agent
restart across every node, which briefly disrupts the datapath per node.

**A patch bump is not a substitute for capacity planning.** The memory leaks are triggered by policy
churn; if agents are already close to their limit, fixing the leak removes the growth but not the
baseline.

**Check the CVE matrix separately** — the defect list above and the advisory list are different
questions, tracked in [[TROUBLE-CILIUM_KNOWN_CVES]].

## References

- cilium/cilium release notes 1.18.5–1.18.12, read 2026-07-31; the full per-line index is in
  `cilium 1.18: defects fixed in the 1.18 line`.
- Component: [[COMPONENT-CILIUM]]; horizon: [[CONCEPT-UPGRADE_HORIZON]].
