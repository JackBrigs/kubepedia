---
id: TROUBLE-POD_EGRESS_INTERNET
type: troubleshooting
title: "Pods can't reach the internet / external IPs (egress, masquerade)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - pod cannot reach internet
  - pod egress fails
  - external connectivity from pod
  - SNAT masquerade pods
  - pod traffic not natted
  - egress network policy blocked
tags:
  - troubleshooting
  - networking
  - egress
  - cni
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "cilium_enable_bpf_masquerade / cilium_native_routing_cidr affect pod egress SNAT (tag v2.31.0)"
relations:
  - type: see_also
    target: CONCEPT-CILIUM_DATAPATH
  - type: see_also
    target: TROUBLE-DNS_EXTERNAL_RESOLUTION
  - type: see_also
    target: CONCEPT-CLUSTER_NETWORKING
---

# Pods can't reach the internet / external IPs (egress, masquerade)

## Summary

When pods can talk **inside** the cluster but not to **external** IPs, the problem is the
egress path: pod source IPs (from the pod CIDR) must be **masqueraded (SNAT)** to the
node's IP to be routable off-cluster — or an **egress NetworkPolicy / node firewall** is
dropping the traffic. (If only *names* fail but IPs work, it's DNS, not egress —
[[TROUBLE-DNS_EXTERNAL_RESOLUTION]].)

## Problem

From a pod, `wget/curl <external-ip>` or `ping 1.1.1.1` times out, while
`<service>.<ns>` / other pods work. External name resolution may or may not work
separately.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- Pod IPs come from `kube_pods_subnet` ([[CONCEPT-CLUSTER_NETWORKING]]) — **not routable**
  on your LAN. To leave the cluster they must be SNAT'd to the node IP. Which addresses get
  masqueraded depends on the CNI's masquerade config.

## Diagnostics

- **Isolate the layer:** in a pod, `curl -v <external-IP>` (bypasses DNS). IP works but
  name doesn't → DNS ([[TROUBLE-DNS_EXTERNAL_RESOLUTION]]); neither works → egress path.
- **Does the node itself reach out?** `curl <external-ip>` from the node — if the node
  can't, it's node routing/firewall, not Kubernetes.
- **Masquerade config (Cilium):** check `cilium_enable_bpf_masquerade` /
  `cilium_native_routing_cidr` — with native routing, traffic to destinations *inside*
  `native_routing_cidr` is not masqueraded; everything else should be
  ([[CONCEPT-CILIUM_DATAPATH]]).
- **NetworkPolicy:** `kubectl get networkpolicy -n <ns>` — a default-deny **egress** policy
  blocks external traffic until you allow it.
- **Packet path:** `cilium-dbg monitor` (Cilium) or node `conntrack -L` / `iptables -t nat
  -L` to see whether egress is SNAT'd.

## Known Issues

Map the cause to its fix:

- **Masquerade disabled/misconfigured** — pod IPs leave un-SNAT'd and replies never return.
  Ensure masquerade is on for external destinations; with native routing set
  `cilium_native_routing_cidr` correctly (empty/wrong = the classic mis-render,
  [[TROUBLE-CILIUM_CONFIG_VALIDATION]]).
- **Egress NetworkPolicy** — a policy selects the pod and denies egress; add an allow rule
  (and allow DNS to kube-dns, or name resolution also breaks).
- **Node-level firewall / routing / no default route** — the node can't reach the internet
  (missing route, NAT gateway, security group). Fix host networking; Kubernetes can't route
  what the node can't.
- **Asymmetric routing / wrong source IP** — multi-NIC nodes SNAT'ing to an interface with
  no return path; pin the egress interface/IP.
- **MTU** on the egress path can cause hangs on large responses ([[TROUBLE-VXLAN_MTU_MISMATCH]]).

**Gotchas:**

- **DNS vs egress** are separate — a pod can resolve names (DNS works) yet fail to connect
  (egress broken), or vice-versa. Test with a raw IP to tell them apart.
- Cluster-internal working while external fails **rules out** the CNI datapath itself —
  focus on masquerade/policy/node-routing, not pod-to-pod networking.
- Egress to your **own** internal networks may be intentionally excluded from masquerade
  (native routing CIDR / non-masquerade CIDRs) — that's config, verify it's intended.

## References

- Cilium masquerade/native-routing defaults at tag `v2.31.0`. Datapath:
  [[CONCEPT-CILIUM_DATAPATH]]; DNS leg: [[TROUBLE-DNS_EXTERNAL_RESOLUTION]]; CIDRs:
  [[CONCEPT-CLUSTER_NETWORKING]].
