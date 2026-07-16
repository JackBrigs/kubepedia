---
id: PRACTICE-CILIUM_DIAGNOSTICS
type: best_practice
title: Cilium diagnostics (day-2 runbook)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - cilium debug
  - cilium status
  - pod networking broken
tags:
  - operations
  - cilium
  - diagnostics
sources:
  - type: docs
    path: docs/CNI/cilium.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/CNI/cilium.md
    note: "Cilium config; commands are standard Cilium tooling"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: VARIABLE-CILIUM_KUBE_PROXY_REPLACEMENT
---

# Cilium diagnostics (day-2 runbook)

## Summary

When pod-to-pod or pod-to-service networking breaks on a Cilium cluster
([[COMPONENT-CILIUM]]), use the Cilium agent status and connectivity tooling to
localize the fault (agent, datapath, kube-proxy-replacement, or policy).

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` clusters with
  `kube_network_plugin: cilium`.
- Default datapath is VXLAN ([[VARIABLE-CILIUM_TUNNEL_MODE]]); kube-proxy
  replacement is off by default ([[VARIABLE-CILIUM_KUBE_PROXY_REPLACEMENT]]).

## Diagnostics

```bash
# agent health on every node
kubectl -n kube-system get pods -l k8s-app=cilium -o wide
kubectl -n kube-system exec ds/cilium -- cilium status --verbose

# endpoints / identities on a node
kubectl -n kube-system exec ds/cilium -- cilium endpoint list

# service load-balancing map (esp. when kube-proxy-replacement is enabled)
kubectl -n kube-system exec ds/cilium -- cilium service list

# operator health
kubectl -n kube-system logs deploy/cilium-operator | tail -50
```

With the Cilium CLI (if installed):

```bash
cilium status                 # overall health
cilium connectivity test      # end-to-end datapath test (creates a test namespace)
```

If Hubble is enabled ([[VARIABLE-CILIUM_ENABLE_HUBBLE]]):

```bash
hubble observe --last 100 --verdict DROPPED   # dropped flows = policy/datapath issue
```

## Implementation

Common failure patterns:
- **Agent CrashLoopBackOff** → check `cilium status`, kernel/eBPF prerequisites,
  and the operator logs.
- **Services unreachable with kube-proxy-replacement** → verify
  `cilium service list` and that kube-proxy is actually removed/consistent
  ([[VARIABLE-KUBE_PROXY_MODE]]).
- **Cross-node pod traffic fails** → tunnel/routing mismatch
  ([[VARIABLE-CILIUM_TUNNEL_MODE]]) or underlay MTU/firewall (VXLAN uses UDP 8472).
- **Native routing** → confirm the routing CIDR is set (a known past bug left it
  null; see the troubleshooting entries).

## References

- `docs/CNI/cilium.md`; standard `cilium`/`hubble` tooling.
- Config: [[PRACTICE-CILIUM]] (guide), [[COMPONENT-CILIUM]].
