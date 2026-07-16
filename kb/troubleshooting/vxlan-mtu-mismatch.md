---
id: TROUBLE-VXLAN_MTU_MISMATCH
type: troubleshooting
title: "Cross-node pod traffic hangs — VXLAN/overlay MTU mismatch"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - vxlan-mtu-mismatch
tags:
  - troubleshooting
  - operations
  - networking
sources:
  - type: docs
    url: https://docs.cilium.io/en/stable/network/mtu/
    note: "Cilium MTU / overlay encapsulation"
relations:
  - type: see_also
    target: VARIABLE-CILIUM_TUNNEL_MODE
---

# Cross-node pod traffic hangs — VXLAN/overlay MTU mismatch

## Summary

Pod-to-pod traffic works on the same node but hangs or drops large packets across nodes (small pings OK, HTTPS/large payloads stall). Classic MTU/encapsulation mismatch.

## Problem

The default Cilium datapath is VXLAN (`cilium_tunnel_mode: vxlan`), which adds ~50 bytes of encapsulation. If the pod MTU is not reduced accordingly (or the underlay blocks large frames / has jumbo-frame mismatch), fragmented/large packets are dropped.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` clusters. This is a general Kubernetes/component operational issue (not tied to one Kubespray version); the relevant tunables are noted in Known Issues.

## Diagnostics

```bash
# from a pod: large pings across nodes fail, small ones work
ping -M do -s 1472 <pod-on-another-node>     # fails if MTU too small for the underlay
kubectl -n kube-system exec ds/cilium -- cilium status | grep -i mtu
```

## Known Issues

Ensure the effective pod MTU accounts for the VXLAN overhead (Cilium auto-detects, but verify), align underlay MTU/jumbo-frame settings across nodes, or use native routing instead of VXLAN. See PRACTICE-CILIUM_DIAGNOSTICS.

## References

- https://docs.cilium.io/en/stable/network/mtu/ — Cilium MTU / overlay encapsulation (verified behavior, 2026-07-16).
