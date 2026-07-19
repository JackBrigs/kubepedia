---
id: TROUBLE-FLAGGER_CANARY
type: troubleshooting
title: "Flagger: canary stuck / rolls back — metrics provider, mesh/Gateway provider, MetricTemplate, webhooks"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.40.0"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - flagger canary not promoting
  - flagger rollback halt advancing
  - flagger no traffic canary
  - flagger metrics provider
  - canary initialization failed
tags: [troubleshooting, progressive-delivery, flagger, mesh]
sources:
  - type: external
    path: flagger troubleshooting
    url: https://docs.flagger.app/
    note: "canary advances on metric checks; needs a traffic provider (mesh/Gateway API) and a metrics provider"
relations:
  - type: see_also
    target: CONCEPT-ADDON_FLAGGER
  - type: see_also
    target: CONCEPT-OBSERVABILITY_STACK
---

# Flagger: canary stuck / rolls back — metrics provider, mesh/Gateway provider, MetricTemplate, webhooks

## Summary

Flagger advances a canary only when its **metric checks pass** and it can **shift traffic**. A canary
that never promotes (or rolls back immediately) almost always means the **metrics provider** returns no
data, the **traffic provider** (mesh / Gateway API) isn't wired, a **MetricTemplate** query is wrong, or
a **webhook** (load test / gate) fails. Flagger 1.40.0.

## Problem

- A `Canary` sits at weight 0 / "waiting", never promotes, or **rolls back** every attempt with
  "Halt advancement".

## Context

- Flagger `1.40.0` ([[CONCEPT-ADDON_FLAGGER]]). It needs (1) a **traffic provider** (Istio/Linkerd/NGINX/
  Gateway API) to shift weight, and (2) a **metrics provider** (Prometheus by default) to judge success.
- **No metrics:** if the Prometheus URL is wrong or the query returns empty, Flagger treats it as a
  failed check and halts — "no values found" is a stall, not a pass.
- **No traffic shift:** a mesh/provider mismatch means weight never moves; the canary can't gather
  metrics and stalls.
- **MetricTemplate:** a custom `MetricTemplate` with a bad PromQL/threshold fails every interval.
- **Webhooks:** pre-rollout/load-test webhooks that error (or an unreachable tester) block advancement.

## Diagnostics

```bash
kubectl -n <ns> get canary <name>                        # STATUS + WEIGHT + LASTTRANSITION
kubectl -n <ns> describe canary <name>                   # events: "Halt advancement" reason
kubectl -n flagger-system logs deploy/flagger | tail
kubectl -n <ns> get metrictemplate,alertprovider
```

## Known Issues

- **No metrics — fix:** point Flagger at the right Prometheus (`--metrics-server` / provider address);
  test the query returns data for the canary's labels ([[CONCEPT-OBSERVABILITY_STACK]]).
- **No traffic — fix:** confirm the mesh/Gateway provider matches the Canary `spec.provider` and the
  target Service/route exists.
- **MetricTemplate — fix:** validate the PromQL and threshold; loosen `interval`/`thresholdRange` while
  debugging.
- **Webhook — fix:** make the webhook endpoint reachable and return 200; a failing gate always halts.
- **Init failure:** the target Deployment must exist before the Canary; Flagger creates the
  primary/`-canary` from it.

## References

- Flagger docs. Addon [[CONCEPT-ADDON_FLAGGER]]; metrics [[CONCEPT-OBSERVABILITY_STACK]].
