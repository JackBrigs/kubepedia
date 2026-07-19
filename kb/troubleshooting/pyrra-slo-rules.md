---
id: TROUBLE-PYRRA
type: troubleshooting
title: "Pyrra: SLO rules not generated / not evaluated — CRD errors, Prometheus not loading the rules"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "0.9.4"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - pyrra slo not working
  - servicelevelobjective crd
  - pyrra rules not generated
  - prometheus not loading pyrra rules
tags:
  - troubleshooting
  - observability
  - slo
  - pyrra
sources:
  - type: external
    path: pyrra
    url: https://github.com/pyrra-dev/pyrra
    note: "Pyrra turns ServiceLevelObjective CRs into Prometheus recording/alerting rules; Prometheus must load them"
relations:
  - type: see_also
    target: CONCEPT-ADDON_PYRRA
  - type: see_also
    target: CONCEPT-OBSERVABILITY_STACK
---

# Pyrra: SLO rules not generated / not evaluated — CRD errors, Prometheus not loading the rules

## Summary

Pyrra manages `ServiceLevelObjective` CRs and **generates Prometheus recording/alerting rules** from them. No SLO burn-rate data means either an **invalid SLO CRD** (Pyrra didn't emit rules) or **Prometheus isn't loading** the generated PrometheusRule. App `v0.9.4`.

## Problem

- The Pyrra UI/SLO shows no data, or burn-rate alerts never fire.

## Context

- Pyrra `0.9.4` ([[CONCEPT-ADDON_PYRRA]]) over Prometheus ([[CONCEPT-OBSERVABILITY_STACK]]).
- **CRD → rules:** an invalid SLO (bad indicator query/objective) makes Pyrra emit nothing.
- **Prometheus pickup:** the generated PrometheusRule must be selected by Prometheus's `ruleSelector` (Prometheus Operator label match) — otherwise the rules exist but Prometheus ignores them.

## Diagnostics

```bash
kubectl get servicelevelobjective -A
kubectl -n <ns> logs deploy/pyrra-kubernetes | tail
kubectl get prometheusrule -A | grep -i pyrra    # generated? labels match ruleSelector?
```

## Known Issues

- **No rules — fix:** `describe` the SLO CR; correct the indicator query/objective so Pyrra generates rules.
- **Not loaded — fix:** ensure the generated PrometheusRule carries the labels Prometheus's `ruleSelector` expects (Prometheus Operator), so it's loaded and evaluated.

## References

Upstream project (see `sources`). Catalog entry [[CONCEPT-ADDON_PYRRA]].
