---
id: TROUBLE-INGRESS2GATEWAY
type: troubleshooting
title: "ingress2gateway: converted Gateway API objects incomplete — provider annotations not translated (one-shot CLI)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - ingress2gateway conversion
  - ingress to gateway api
  - annotations not converted
  - ingress2gateway missing routes
tags:
  - troubleshooting
  - networking
  - gateway-api
  - migration
sources:
  - type: external
    path: ingress2gateway
    url: https://github.com/kubernetes-sigs/ingress2gateway
    note: "ingress2gateway is a one-shot CLI that translates Ingress to Gateway API; provider-specific annotations may not map"
relations:
  - type: see_also
    target: CONCEPT-ADDON_INGRESS2GATEWAY
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
---

# ingress2gateway: converted Gateway API objects incomplete — provider annotations not translated (one-shot CLI)

## Summary

`ingress2gateway` is a **one-shot CLI conversion tool** (not a controller) that translates Ingress into Gateway API objects. The output is often **incomplete**: provider-specific Ingress **annotations** (rewrites, auth, timeouts) have no Gateway API equivalent and are **dropped** — you review and finish by hand. It doesn't run in-cluster, so there's nothing to 'debug' at runtime.

## Problem

- The generated `HTTPRoute`/`Gateway` lacks behavior the original Ingress had (rewrites, TLS, auth), or some Ingresses aren't converted.

## Context

- ingress2gateway ([[CONCEPT-ADDON_INGRESS2GATEWAY]]); output consumed by a Gateway API controller ([[CONCEPT-ADDON_ENVOY_GATEWAY]]).
- **Annotations don't map:** controller-specific Ingress annotations are not part of the Gateway API spec; the tool translates the standard parts and skips the rest.
- **One-shot:** it's a migration aid, not a running component — re-run it as source Ingresses change.

## Diagnostics

```bash
# it's a CLI, run and inspect the output before applying
ingress2gateway print --input-file ingress.yaml > gateway.yaml
# diff intent: what annotations existed vs what mapped
grep -i annotations -A5 ingress.yaml
```

## Known Issues

- **Incomplete output — fix:** manually add the missing behavior as Gateway API constructs (filters, policies) supported by your controller; the tool only covers the standard mapping.
- **Missing conversions — fix:** ensure the provider/IngressClass is one the tool supports; convert unsupported ones by hand.

## References

Upstream project (see `sources`). Catalog entry [[CONCEPT-ADDON_INGRESS2GATEWAY]].
