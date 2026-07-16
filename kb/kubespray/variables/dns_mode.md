---
id: VARIABLE-DNS_MODE
type: variable
title: dns_mode
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - dns_mode
tags:
  - dns
  - coredns
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "128"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "dns_mode: coredns (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-COREDNS
  - type: see_also
    target: COMPONENT-NODELOCALDNS
---

# dns_mode

## Summary

`dns_mode` selects the cluster DNS setup Kubespray deploys. The default is
`coredns` across `v2.29.0`–`v2.31.0`, which deploys CoreDNS (see
[[COMPONENT-COREDNS]]).

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml:128`
(`dns_mode: coredns`, unchanged across all four tags). Accepted values:

- `coredns` (default) — deploy CoreDNS.
- `coredns_dual` — CoreDNS with a secondary (dual-stack) service.
- `manual` — use an externally managed DNS; Kubespray does not deploy CoreDNS.
- `none` — no cluster DNS deployed.

The value gates the DNS add-on tasks and interacts with the late `resolvconf`
pass (see [[TAG-RESOLVCONF]]) and with NodeLocal DNS
([[COMPONENT-NODELOCALDNS]]).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `coredns`; accepted `coredns` |
  `coredns_dual` | `manual` | `none`.
- `coredns_dual` is for dual-stack clusters; `manual`/`none` skip CoreDNS
  deployment.

## References

- `roles/kubespray_defaults/defaults/main/main.yml:128` — default.
- CNI/DNS role tasks branch on `dns_mode == 'coredns_dual'` / `'manual'`.
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
