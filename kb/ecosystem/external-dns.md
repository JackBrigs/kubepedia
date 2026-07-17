---
id: CONCEPT-EXTERNAL_DNS
type: concept
title: "external-dns — publishing DNS records for Services/Ingress"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - external-dns
  - automatic dns records kubernetes
  - publish service dns
  - ingress dns automation
  - route53 cloudflare kubernetes
tags:
  - dns
  - networking
  - ecosystem
sources:
  - type: docs
    path: external-dns documentation
    url: https://kubernetes-sigs.github.io/external-dns/
    note: "watches Services/Ingresses and syncs external DNS provider records (verified)"
relations:
  - type: see_also
    target: CONCEPT-SERVICE_EXPOSURE
  - type: see_also
    target: COMPONENT-COREDNS
  - type: see_also
    target: TROUBLE-DNS_EXTERNAL_RESOLUTION
---

# external-dns — publishing DNS records for Services/Ingress

## Summary

**external-dns** watches Kubernetes **Services** (type LoadBalancer) and **Ingresses** and
automatically creates/updates records in an **external DNS provider** (Route 53,
Cloudflare, Google/Azure DNS, RFC2136, …) so `myapp.example.com` points at your service's
external IP. It solves **north-south name publishing** — it is **not** cluster-internal DNS
(that's CoreDNS, `*.svc.cluster.local`) and not pod DNS resolution.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. external-dns is **not** Kubespray-managed —
  install via its Helm chart (evidence: upstream docs, `verified`).
- Runs as a controller with a provider credential; it **owns** a DNS zone (or a filtered
  subset) and reconciles records to match cluster objects.

## Implementation

- Annotate/label a **Service** (`type: LoadBalancer`) or **Ingress** with a hostname (e.g.
  `external-dns.alpha.kubernetes.io/hostname`), and external-dns creates the A/CNAME record
  pointing at the LB external IP.
- The external IP comes from your LoadBalancer implementation — MetalLB / Cilium LB /
  cloud LB / kube-vip ([[CONCEPT-SERVICE_EXPOSURE]]); external-dns just **publishes** it.
- **TXT registry:** external-dns writes companion TXT records to track ownership so it only
  manages records it created — don't hand-edit those.
- **Scope it:** `--domain-filter` / `--zone-id-filter` and a `--txt-owner-id` keep multiple
  clusters from fighting over the same zone.

## Compatibility

- **Not a replacement for CoreDNS.** CoreDNS resolves in-cluster names
  ([[COMPONENT-COREDNS]]); external-dns publishes **public/external** names for
  ingress/LoadBalancer endpoints. Different layers.
- **Needs an external IP to publish** — a `LoadBalancer` stuck `<pending>` gives
  external-dns nothing to point at ([[TROUBLE-METALLB_SERVICE_PENDING]]).
- **Provider RBAC/credentials:** the controller needs cloud/provider API credentials with
  DNS write access; least-privilege that credential.
- **Distinct from pod egress DNS problems** — if pods can't *resolve* external names, that's
  the upstream-forwarding path ([[TROUBLE-DNS_EXTERNAL_RESOLUTION]]), unrelated to
  external-dns publishing records.

## References

- external-dns docs. Service exposure (source of the external IP): [[CONCEPT-SERVICE_EXPOSURE]];
  cluster DNS: [[COMPONENT-COREDNS]]; pod DNS resolution: [[TROUBLE-DNS_EXTERNAL_RESOLUTION]].
