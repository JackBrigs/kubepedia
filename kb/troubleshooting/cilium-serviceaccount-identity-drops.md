---
id: TROUBLE-CILIUM_SERVICEACCOUNT_IDENTITY_DROPS
type: troubleshooting
title: "Cilium 1.18 upgrade causes transient packet drops — serviceaccount added to identity labels"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=1.18.2 <=1.19.3"
verified_at: "2026-07-18"
confidence: confirmed
aliases:
  - cilium identity churn upgrade
  - io.cilium.k8s.policy.serviceaccount identity label
  - cilium 1.18 packet drops upgrade
  - identity count spike cilium
tags:
  - cilium
  - troubleshooting
  - identity
  - upgrade
sources:
  - type: docs
    path: Documentation/operations/upgrade.rst
    url: https://github.com/cilium/cilium/blob/v1.18.2/Documentation/operations/upgrade.rst
    note: "1.18 adds io.cilium.k8s.policy.serviceaccount to default identity-relevant labels → identity count rises during upgrade"
relations:
  - type: see_also
    target: UPGRADE-CILIUM_1_15_TO_1_19
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: CONCEPT-CILIUM_DATAPATH
---

# Cilium 1.18 upgrade causes transient packet drops — serviceaccount added to identity labels

## Summary

Cilium **1.18** adds `io.cilium.k8s.policy.serviceaccount` to the **default identity-relevant label
set**. Because pod **security identities** are derived from these labels, adding one causes existing
endpoints to be assigned **new identities** during the upgrade — a temporary spike in identity count
and **brief packet drops** while policies re-resolve. This happens when Kubespray moves Cilium to
**1.18.2 (v2.29.0)**. It is transient and self-healing, but surprising if unexpected.

## Problem

- During/just after the Kubespray v2.28.0 → v2.29.0 upgrade (Cilium 1.17→1.18), you see a **spike in
  Cilium identities** and **short-lived denied/dropped** connections between policy-selected pods.
- Metrics show identity allocation churn; Hubble shows brief policy drops that clear on their own.

## Context

- Applies to Cilium **1.18+** → Kubespray **v2.29.0** ([[UPGRADE-CILIUM_1_15_TO_1_19]]). The new label
  in the identity set means pods that previously shared an identity now split by ServiceAccount, so
  every affected endpoint regenerates its identity once (`upgrade.rst`@v1.18.2).
- Identities drive policy enforcement ([[CONCEPT-CILIUM_DATAPATH]]); a mass re-identity briefly widens
  the window where an endpoint's new identity isn't yet reflected in all policy maps → drops.

## Diagnostics

- `cilium identity list | wc -l` before/after — a jump correlates with the label change.
- `hubble observe --verdict DROPPED` during the upgrade window shows policy drops that stop once
  identities settle.
- Confirm the label set: `cilium config view | grep -i identity` / the `labels`/identity-relevant config.

## Known Issues

- **Fix (accept, default):** the churn is **transient** — let identities settle; drops clear within the
  regeneration window. Schedule the upgrade in a maintenance window and expect a brief blip for
  policy-selected traffic.
- **Fix (avoid the change):** if you do **not** want ServiceAccount in identities, exclude it with a
  label filter (`!io\.cilium\.k8s\.policy\.serviceaccount`) so identities don't split — set before the
  upgrade to skip the churn entirely.
- Part of a broader "transient drops on Cilium upgrade" theme (Envoy DaemonSet at 1.16, this at 1.18) —
  plan Cilium upgrades as brief-disruption events ([[UPGRADE-CILIUM_1_15_TO_1_19]]).

## References

- Cilium `Documentation/operations/upgrade.rst`@v1.18.2 (serviceaccount identity label). Full jump
  [[UPGRADE-CILIUM_1_15_TO_1_19]]; datapath/identity [[CONCEPT-CILIUM_DATAPATH]]; component
  [[COMPONENT-CILIUM]].
