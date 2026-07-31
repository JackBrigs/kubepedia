---
id: TROUBLE-ENVOY_GATEWAY_1_3_KNOWN_ISSUES
type: troubleshooting
title: "Envoy Gateway 1.3: every defect fixed in the 1.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.3.0 <1.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - envoy gateway 1.3 known issues
  - envoy gateway 1.3 bugs
  - envoy gateway 1.3 fixed in
tags:
  - troubleshooting
  - envoy
  - gateway-api
  - upgrade
sources:
  - type: code
    path: envoyproxy/gateway release-notes/v1.3.*.yaml — "bug fixes" sections
    url: https://github.com/envoyproxy/gateway/tree/main/release-notes
    note: "4 releases on this line, 43 declared fixes"
relations:
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_KNOWN_CVES
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
---

# Envoy Gateway 1.3: every defect fixed in the 1.3 line

## Summary

The **1.3** maintenance line published **4 releases** carrying **43 defect fixes**,
8 breaking changes and 2 security updates (CVE-2025-25294).
Running anything below **1.3.3** on this line means carrying the remainder of the list
below.

Use this page the way a defect database is used: before filing "Envoy Gateway does X wrong", search
here — the odds are it is already named, with the exact patch that fixes it.

## Problem

Defects are grouped by the release that fixed them; a cluster on version *N* carries everything
listed under versions greater than *N*.

## Context

### v1.3.0 — 26

- Fixed a panic in the provider goroutine when the body in the direct response configuration was nil.
- Fixed Envoy rejecting TCP Listeners that have no attached TCPRoutes.
- Fixed failed to update SecurityPolicy resources with the `backendRef` field specified.
- Fixed xDS translation failed when oidc tokenEndpoint and jwt remoteJWKS are specified in the same SecurityPolicy and using the same hostname.
- Fixed frequent 503 errors when connecting to a Service experiencing high Pod churn.
- Disabled the retry policy for the JWT provider to reduce requests sent to the JWKS endpoint. Failed async fetches will retry every 1s.
- Fixed BackendTLSPolicy not supporting the use of a port name as the sectionName in targetRefs.
- Fixed reference grant from EnvoyExtensionPolicy to the referenced ext-proc backend not being respected.
- Fixed BackendTrafficPolicy not applying to Gateway Routes when a Route has a Request Timeout defined.
- Fixed proxies connected to the secondary Envoy Gateway not receiving xDS configuration.
- Fixed traffic splitting not working when some backends were invalid.
- Fixed a nil pointer error that occurred when a SecurityPolicy referred to a UDS backend.
- Fixed an issue where the Gateway API translator did not use the TLS configuration from the BackendTLSPolicy when connecting to the OIDC provider’s well-known endpoint.
- Fixed a validation failure that occurred when multiple HTTPRoutes referred to the same extension filter.
- Fixed a nil pointer error caused by accessing the cookie TTL without verifying if it was valid.
- Fixed unexpected port number shifting in standalone mode.
- Fixed an issue where the shutdown-manager did not respect the security context of the container spec.
- Fixed readiness checks failing for single-stack IPv6 Envoy Gateway deployments on dual-stack clusters.
- Fixed IPv6 dual-stack support not working as intended.
- Fixed the ability to overwrite control plane certs with the certgen command by using a new command arg (-o).
- Fixed a panic that occurred following update to the envoy-gateway-config ConfigMap.
- Fixed prometheus format conversion of ratelimit metrics for remote address.
- Fixed limitations that prevented creation of FQDN Endpoints with a single-character subdomain in Backend.
- Fixed issue where SecurityContext of shutdown-manager container was not updated by overriding helm values.
- Fixed issue with incorrect IPFamily detection for backends.
- Fixed validation of interval values in Retry settings.

### v1.3.1 — 5

- Added support for Secret and ConfigMap parsing in Standalone mode.
- Fix translating backendSettings for extAuth.
- Fix allowing weights to be zero on endpoints for backendRefs in TCPRoute and UDPRoute.
- Fix validation of all xDS resources.
- Fix support for empty values in fields with default values in Standalone.

### v1.3.2 — 6

- Added support for BackendTLSPolicy and EnvoyExtensionPolicy parsing in Standalone mode.
- Fixed updates of endpoints when mirrored backend Pod IPs are changed.
- Fix not logging an error and returning it in the K8s Reconcile method when a GatewayClass is not accepted.
- Fix allowing empty text field for opentelemetry sink when using JSON format.
- Fixed validation of host header in RequestHeaderModifier filter.
- Retrigger reconciliation when backendRef of type ServiceImport is updated or when EndpointSlice(s) for a ServiceImport are updated.

### v1.3.3 — 6

- Fix issue where ReferenceGrant from SecurityPolicy to the referenced RemoteJWKS backend was not respected.
- Fix HTTPRoute precedence by correctly considering header and query match types.
- Fix to return an error if direct response size exceeds the limit.
- Fix to avoid adding the TLS inspector filter to QUIC listeners.
- Fix to continue processing remaining GatewayClasses after encountering an error.
- Add validation for header values.

## Diagnostics

```bash
kubectl -n <eg-ns> get deploy envoy-gateway \
  -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```

Compare against **1.3.3** — the newest release of this line.

## Known Issues

Upgrading inside a maintenance line is the low-risk move, but this project ships behaviour changes
in patch releases as well; the full list is in [[TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES]] and the
security exposure in [[TROUBLE-ENVOY_GATEWAY_KNOWN_CVES]].

## References

- Upstream `release-notes/v1.3.*.yaml`, `bug fixes` sections, read at `origin/main` on 2026-07-31.
- Add-on: [[CONCEPT-ADDON_ENVOY_GATEWAY]].
