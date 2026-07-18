---
id: TROUBLE-CILIUM_ENI_MASQUERADE_FLIP
type: troubleshooting
title: "Cilium 1.18 on AWS ENI — enableIPv4Masquerade default flips true→false, egress SNAT changes"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=1.18.2 <=1.19.3"
verified_at: "2026-07-18"
confidence: confirmed
aliases:
  - cilium eni enableIPv4Masquerade default false
  - cilium 1.18 aws egress broken
  - cilium eni masquerade upgrade
  - pod egress snat cilium eni
tags:
  - cilium
  - troubleshooting
  - aws
  - upgrade
sources:
  - type: docs
    path: Documentation/operations/upgrade.rst
    url: https://github.com/cilium/cilium/blob/v1.18.2/Documentation/operations/upgrade.rst
    note: "1.18: eni-mode enableIPv4Masquerade Helm default flips true->false; also install/kubernetes/cilium/values.yaml@v1.18.2"
relations:
  - type: see_also
    target: UPGRADE-CILIUM_1_15_TO_1_19
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: CONCEPT-CILIUM_DATAPATH
---

# Cilium 1.18 on AWS ENI — enableIPv4Masquerade default flips true→false, egress SNAT changes

## Summary

For clusters using Cilium's **AWS ENI** IPAM/datapath mode, Cilium **1.18** flips the Helm
`enableIPv4Masquerade` **default from `true` to `false`**. After Kubespray moves Cilium to **1.18.2
(v2.29.0)**, pod egress that relied on Cilium **SNAT/masquerading** may change — traffic that was
masqueraded to the node IP is now expected to route natively via ENI. On AWS this is usually correct
(ENI gives pods routable IPs), but a cluster depending on the old masquerade behavior can see **broken
egress** to destinations that only accept the node IP.

## Problem

- After the Kubespray v2.28.0 → v2.29.0 upgrade on an **AWS ENI** Cilium cluster, pod **egress to
  external endpoints** behaves differently — connections that worked via node-IP SNAT now use the pod
  ENI IP (or vice-versa), breaking IP-allow-listed destinations or NAT expectations.

## Context

- Applies to Cilium **1.18+** in **ENI mode** → Kubespray **v2.29.0** ([[UPGRADE-CILIUM_1_15_TO_1_19]]).
  Only relevant when `ipam.mode=eni` / `eni` datapath is in use (AWS); non-ENI clusters are unaffected.
- The default change is in `values.yaml@v1.18.2` and called out in `upgrade.rst@v1.18.2`: in `eni`
  mode `enableIPv4Masquerade` now defaults **false** ([[CONCEPT-CILIUM_DATAPATH]]).

## Diagnostics

- Confirm ENI mode: `cilium config view | grep -Ei "ipam|masquerade|eni"` — `ipam-mode: eni` and the
  masquerade setting.
- Test egress source IP from a pod (e.g. to an echo service that reports the source IP) before/after —
  node IP vs pod ENI IP tells you which path is active.

## Known Issues

- **Fix (keep old behavior):** set **`enableIPv4Masquerade: true`** explicitly, or use
  `upgradeCompatibility<1.18`, to retain node-IP SNAT for pod egress.
- **Fix (adopt new default):** if pods should egress with their own ENI IPs (the AWS-native model),
  leave it `false` and ensure security groups / NAT / allow-lists accept the pod ENI IPs.
- **Pre-upgrade:** decide the egress model **before** v2.29.0 on AWS ENI clusters; this is a silent
  default flip that only affects ENI mode.

## References

- Cilium `Documentation/operations/upgrade.rst`@v1.18.2 and `install/kubernetes/cilium/values.yaml`@v1.18.2
  (eni enableIPv4Masquerade default). Full jump [[UPGRADE-CILIUM_1_15_TO_1_19]]; datapath
  [[CONCEPT-CILIUM_DATAPATH]]; component [[COMPONENT-CILIUM]].
