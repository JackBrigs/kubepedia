---
id: UPGRADE-CILIUM_1_18_TO_1_19
type: upgrade
title: "Cilium 1.18.4 → 1.19: what the upgrade fixes and what it changes under you"
status: active
kubespray_version: ">=v2.29.1 <=v2.31.0"
kubernetes_version: null
component_version: ">=1.18.4 <=1.19.3"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.18 to 1.19 upgrade
  - should we move cilium to 1.19
  - what breaks upgrading cilium 1.19
  - cilium 1.19 what gets fixed
tags:
  - upgrade
  - cilium
  - network-policy
sources:
  - type: docs
    path: cilium/cilium release notes 1.19.0 – 1.19.3
    url: https://github.com/cilium/cilium/releases
    note: "extracted 2026-07-31; 148 fixes on the line, 47 of them behaviour-affecting"
relations:
  - type: see_also
    target: TROUBLE-CILIUM_1_18_EXPOSURE
  - type: see_also
    target: TROUBLE-CILIUM_CLUSTERMESH_LOCAL_POLICY
  - type: see_also
    target: COMPONENT-CILIUM
---

# Cilium 1.18.4 → 1.19: what the upgrade fixes and what it changes under you

## Summary

Moving from **1.18.4** (Kubespray v2.29.1) to **1.19.3** (v2.31.0) is a minor upgrade, and it is not
symmetrical: it closes most of what [[TROUBLE-CILIUM_1_18_EXPOSURE]] lists, and it flips **two
defaults that change enforcement**, silently, on clusters that relied on the old behaviour.

Decide the two defaults first. Everything else is a straight improvement.

## Upgrade Notes

**Two default flips demand a decision before the rollout** — both already analysed in this base:

- `policy-default-local-cluster` is **on** by default: cross-cluster traffic that used to be
  permitted is denied unless policies are rewritten. See
  [[TROUBLE-CILIUM_CLUSTERMESH_LOCAL_POLICY]].
- mesh authentication is **disabled** by default, so mutual-auth traffic is forwarded
  unauthenticated instead of failing closed — the dangerous direction for a security control.

Neither appears in the release body as a breaking change; both were found by reading upgrade notes,
which is why the machine-extracted list for this line shows zero breaking entries. Absence there is
not evidence of a safe upgrade.

**What the move fixes** — the 1.18 problems carried today are addressed on the way:

| Carried on 1.18.4 | Where it is fixed |
|---|---|
| policy deadlock vs new identities; endpoints stuck regenerating | 1.18.5–1.18.6, included |
| memory leaks from policy churn | 1.18.9 / 1.18.11 and again on 1.19.3 (incremental policy updates) |
| wildcard FQDN identities not pushed to Envoy (SNI policies) | 1.18.8, re-landed 1.19.2 |
| VTEP ARP returning a zero MAC | 1.18.8, re-landed 1.19.2 |
| L7 policy proxy redirect performance | 1.18.9, re-landed 1.19.3 |
| agent fails to start in kvstore mode with etcd behind a Service | 1.18.12, re-landed 1.19.3 |

**New on the 1.19 line itself**, worth knowing before you meet them:

- panic during datapath reinitialisation when a required DirectRouting device is missing (1.19.1);
- IPsec key-rotation race dropping packets while XFRM states were not ready (1.19.2);
- clustermesh: goroutine leak and a race leaving EndpointSlices uncleaned when a cluster is removed
  (1.19.2);
- MCS-API CRD install could attempt a downgrade when the version label is higher (1.19.3).

The clustermesh entries only matter with cluster mesh in use; the IPsec one only with encryption
enabled.

## Implementation

Rolling the agent is the whole operation; the decisions are the two defaults above.

### Impact

Upgrading Cilium is a rolling restart of the agent on every node. Per node the datapath is briefly
disrupted; existing connections survive, new connections during the window may not. On this estate
that is 358 nodes across four clusters, so plan it per cluster, not per fleet.

The two default flips are **not** rolled back by restarting the agent — they take effect as soon as
the new configuration is applied, which is why they are a decision and not a risk to monitor.

### Rollback

Downgrading a CNI in place is not a supported operation; the practical rollback is to re-pin the old
version and re-run, accepting another rolling restart. Verify the default flips are reverted
explicitly — the values, not just the version.

## Compatibility

Cilium 1.19.3 is what Kubespray v2.31.0 pins, against Kubernetes 1.35.4; on this estate the target
is 1.19 with Kubernetes 1.32.8, which is within Cilium's supported skew but is not the combination
Kubespray ships as a pair. Pinning `cilium_version` without moving Kubespray keeps the rest of the
envelope unchanged — see [[CONCEPT-UPGRADE_HORIZON]].

### Diagnostics

```bash
# before: confirm what the defaults are today
kubectl -n kube-system get cm cilium-config -o yaml \
  | grep -E "policy-default-local-cluster|mesh-auth|enable-mesh-auth"

# after: agents healthy and endpoints converged
kubectl -n kube-system exec ds/cilium -- cilium-dbg status --brief
kubectl -n kube-system exec ds/cilium -- cilium-dbg endpoint list | awk '$0 !~ /ready/'
```

## References

- cilium/cilium release notes 1.19.0–1.19.3, read 2026-07-31; per-line index in
  `cilium 1.19: defects fixed in the 1.19 line`.
- Current exposure: [[TROUBLE-CILIUM_1_18_EXPOSURE]]; the default flip:
  [[TROUBLE-CILIUM_CLUSTERMESH_LOCAL_POLICY]]; component: [[COMPONENT-CILIUM]].
