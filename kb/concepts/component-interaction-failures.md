---
id: CONCEPT-COMPONENT_INTERACTION_FAILURES
type: concept
title: "Cross-component interaction failures — the seams where two healthy components break together"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - component interaction failures
  - cross-component seams
  - two components break together
  - integration failure matrix
  - which components conflict
tags:
  - concept
  - troubleshooting
  - interaction
  - networking
  - index
sources:
  - type: analysis
    path: kubepedia/cross-component seams
    note: "curated from the atomic troubleshooting graph; each seam links to its dedicated doc"
relations:
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
  - type: see_also
    target: TROUBLE-METALLB_L2_STRICTARP_UNREACHABLE
  - type: see_also
    target: TROUBLE-PSA_BLOCKS_PRIVILEGED_WORKLOAD
  - type: see_also
    target: TROUBLE-WEBHOOK_CERT_MANAGER_ORDERING
  - type: see_also
    target: TROUBLE-CILIUM_KPR_TOGGLES_REMOVED
  - type: see_also
    target: TROUBLE-CONNTRACK_TABLE_FULL
  - type: see_also
    target: TROUBLE-COREDNS_RESOLUTION_LOOP
---

# Cross-component interaction failures — the seams where two healthy components break together

## Summary

Kubepedia is a graph of **atomic, per-component** documents. That structure is precise, but a whole
class of outages lives **between** two components — each is individually "healthy", yet their
combination fails. These are the hardest to diagnose because no single component's logs explain it.
This document is the **spine** for that class: a catalog of known seams in the Kubespray range
(v2.27.0–v2.31.0), each pointing to its dedicated atomic doc. When a symptom doesn't fit any single
component, look here.

## Context

**How to use:** find the two components you have configured together; the row names the failure and
links to the fix. This complements the symptom-first [[CONCEPT-TROUBLESHOOTING_MAP]].

| Component A | Component B | Failure at the seam | Doc |
|---|---|---|---|
| MetalLB (L2) | kube-proxy **IPVS** | LB IP assigned but unreachable — `kube-ipvs0` shadows ARP; needs `strictARP` | [[TROUBLE-METALLB_L2_STRICTARP_UNREACHABLE]] |
| MetalLB / kube-proxy | **Cilium kube-proxy-replacement** | kpr removes kube-proxy; old MetalLB-with-kube-proxy toggles/assumptions break; use Cilium LB-IPAM / `l2announcements` | [[TROUBLE-CILIUM_KPR_TOGGLES_REMOVED]] |
| Privileged infra DaemonSet (CNI/CSI/agent) | **Pod Security Admission** (`restricted`) | privileged pods rejected at admission — namespace needs `privileged` label / exemption | [[TROUBLE-PSA_BLOCKS_PRIVILEGED_WORKLOAD]] |
| cert-manager | ingress / any webhook-guarded resource | validating/mutating **webhook not ready** blocks resource creation until cert-manager's own webhook is up (ordering) | [[TROUBLE-WEBHOOK_CERT_MANAGER_ORDERING]] |
| Any admission webhook | apiserver / workload creation | webhook `failurePolicy: Fail` + unreachable webhook **blocks all creates** in scope | [[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]] |
| NodeLocal DNSCache | CoreDNS / upstream resolv.conf | `loop` plugin trips or resolution breaks when the DNS chain points back at itself | [[TROUBLE-COREDNS_RESOLUTION_LOOP]] |
| Cilium IPsec/encryption | host kernel / routing | encryption + host-routing kernel path (CVE-class) — kernel/module dependency at the seam | [[TROUBLE-CILIUM_IPSEC_HOST_ROUTING_CVE]] |
| kube-proxy / high connection churn | conntrack table | `nf_conntrack: table full` drops new connections cluster-wide | [[TROUBLE-CONNTRACK_TABLE_FULL]] |
| Service topology / EndpointSlice | kube-proxy routing | topology hints / EndpointSlice churn can starve a zone of endpoints or thrash routing | [[TROUBLE-KCM_ENDPOINTSLICE_CHURN]] |
| Two snapshot controllers (addon + CSI driver bundle) | external-snapshotter | duplicate snapshot controllers fight over the same CRDs | [[TROUBLE-MULTIPLE_SNAPSHOT_CONTROLLERS]] |
| Node-local storage (local-path) | scheduler / drain | a pod pinned to a node's local PV can't reschedule — drain strands it | [[TROUBLE-NODE_LOCAL_PVC_DRAIN]] |

**Why these are under-represented by design:** each atomic doc correctly describes *its* component.
The seam failure is a property of the **configuration combination**, not either component — so it needs
an explicit cross-link like this spine to be discoverable. When you add a new component or flip a
dataplane mode (kube-proxy IPVS↔iptables, add Cilium kpr, enforce PSA, add a webhook), re-check this
table for a new seam.

**Extending this list:** a new interaction failure gets a dedicated `TROUBLE-*` atomic doc plus a row
here (both A and B linked). Don't fold the seam into one component's doc — it hides it from the other
side.

## References

- Curated from the atomic troubleshooting graph. Symptom index [[CONCEPT-TROUBLESHOOTING_MAP]]; seams
  above each carry their own source-backed doc.
