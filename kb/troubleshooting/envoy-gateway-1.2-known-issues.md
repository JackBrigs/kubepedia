---
id: TROUBLE-ENVOY_GATEWAY_1_2_KNOWN_ISSUES
type: troubleshooting
title: "Envoy Gateway 1.2: every defect fixed in the 1.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.2.0 <1.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - envoy gateway 1.2 known issues
  - envoy gateway 1.2 bugs
  - envoy gateway 1.2 fixed in
tags:
  - troubleshooting
  - envoy
  - gateway-api
  - upgrade
sources:
  - type: code
    path: envoyproxy/gateway release-notes/v1.2.*.yaml — "bug fixes" sections
    url: https://github.com/envoyproxy/gateway/tree/main/release-notes
    note: "9 releases on this line, 61 declared fixes"
relations:
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_KNOWN_CVES
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
---

# Envoy Gateway 1.2: every defect fixed in the 1.2 line

## Summary

The **1.2** maintenance line published **9 releases** carrying **61 defect fixes**,
6 breaking changes and 4 security updates (CVE-2025-24030, CVE-2025-25294, CVE-2025-30157).
Running anything below **1.2.8** on this line means carrying the remainder of the list
below.

Use this page the way a defect database is used: before filing "Envoy Gateway does X wrong", search
here — the odds are it is already named, with the exact patch that fixes it.

## Problem

Defects are grouped by the release that fixed them; a cluster on version *N* carries everything
listed under versions greater than *N*.

## Context

### v1.2.0 — 31

- Fixed xDS translation failing when the WASM HTTP code source was configured without an SHA
- Fixed unsupported listener protocol types causing errors while updating Gateway status
- Fixed unsupported listener protocol types causing errors while updating Gateway status
- Fixed invalid sectionName in BackendTLSPolicy for Backend
- Fixed Delay in SecurityPolicy change propagation for HTTPRoute when using targetSelectors
- Fixed JSONPath not being correctly translated to JSONPatch paths
- Fixed allowing an empty slowStart value when using LeastRequest
- Fixed updating the HTTPRoute status correctly when the linked Backend resource is invalid
- Fixed timeout settings originating from the route being lost when translating the backend traffic policy
- Fixed Backend resources not receiving status updates
- Fixed active health checks requiring the expectedStatuses field to function correctly
- Fixed HTTPHeaderFilter processing not correctly supporting multiple header values
- Fixed reconciling multiple ReferenceGrants within the same namespace
- Fixed unwanted / appearing in the Path when using Prefix Rewrites
- Fixed incorrect gateway being selected as the HTTPRoute parent
- Fixed override issues for EnvoyExtensionPolicy
- Fixed nil pointer error when translating hash load balancing
- Fixed nil pointer if backedtls.minVersion is set but backedtls.maxVersion is not
- Fixed empty connection limits causing xDS rejection
- Fixed rate limiting not working with both headers and CIDR matches
- Fixed EDS not updating when deployments were created after services
- Fixed RBAC issue for deleting infrastructure resources
- Fixed gateways never reaching ready/programmed status when running Envoy as a Daemonset
- Fixed rate limit deployment ignoring pod labels and annotation merges
- Fixed the API Server receives unnecessary requests
- Fixed egctl experimental translate using an incorrect namespace
- Fixed reconciliation not being triggered for Secret updates referenced by a BackendTLSPolicy
- Fixed xDS translation failure when WASM HTTP code source was configured without an SHA
- Fixed HTTPRoute status displaying only one parent when targeting multiple gateways from different GatewayClasses
- Fixed Route with multiple parents having an incorrect namespace in the parentRef status
- Fixed BackendTlsPolicy specifying multiple targetRefs for the same service, to work

### v1.2.1 — 1

- Fixed a panic in the provider goroutine when the body in the direct response configuration was nil.

### v1.2.2 — 4

- Fixed Envoy rejecting TCP Listeners that have no attached TCPRoutes.
- Fixed failed to update SecurityPolicy resources with the `backendRef` field specified.
- Fixed xDS translation failed when oidc tokenEndpoint and jwt remoteJWKS are specified in the same SecurityPolicy and using the same hostname.
- Fixed frequent 503 errors when connecting to a Service experiencing high Pod churn.

### v1.2.3 — 2

- Disabled the retry policy for the JWT provider to reduce requests sent to the JWKS endpoint. Failed async fetches will retry every 1s.
- Used a waitGroup instead of an enabled channel in the status updater.

### v1.2.4 — 5

- Fixed BackendTLSPolicy not supporting the use of a port name as the sectionName in targetRefs.
- Fixed reference grant from EnvoyExtensionPolicy to the referenced ext-proc backend not being respected.
- Fixed BackendTrafficPolicy not applying to Gateway Routes when a Route has a Request Timeout defined.
- Fixed proxies connected to the secondary Envoy Gateway not receiving xDS configuration.
- Fixed traffic splitting not working when some backends were invalid.

### v1.2.5 — 8

- Fixed a nil pointer error that occurred when a SecurityPolicy referred to a UDS backend.
- Fixed an issue where the Gateway API translator did not use the TLS configuration from the BackendTLSPolicy when connecting to the OIDC provider’s well-known endpoint.
- Fixed a validation failure that occurred when multiple HTTPRoutes referred to the same extension filter.
- Fixed a nil pointer error caused by accessing the cookie TTL without verifying if it was valid.
- Fixed unexpected port number shifting in standalone mode.
- Fixed an issue where the shutdown-manager did not respect the security context of the container spec.
- Fixed readiness checks failing for single-stack IPv6 Envoy Gateway deployments on dual-stack clusters.
- Fixed IPv6 dual-stack support not working as intended.

### v1.2.6 — 1

- Fixed a panic that occurred following update to the envoy-gateway-config ConfigMap.

### v1.2.7 — 4

- Fix translating of backendSettings for extAuth.
- Fix allowing weights to be zero on endpoints for backendRefs in TCPRoute and UDPRoute.
- Fix validation of all xDS resources before sending them to the Envoy fleet.
- Added support for Secret and ConfigMap parsing in Standalone mode.

### v1.2.8 — 5

- Added support for BackendTLSPolicy and EnvoyExtensionPolicy parsing in Standalone mode.
- Fixed endpoint updates when mirrored backend Pod IPs change.
- Fix not logging an error and returning it in the K8s Reconcile method when a GatewayClass is not accepted.
- Fixed validation of host header in RequestHeaderModifier filter.
- Fixed an OpenTelemetry access log sink failure caused by an 'otel.Text is nil' error.

## Diagnostics

```bash
kubectl -n <eg-ns> get deploy envoy-gateway \
  -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```

Compare against **1.2.8** — the newest release of this line.

## Known Issues

Upgrading inside a maintenance line is the low-risk move, but this project ships behaviour changes
in patch releases as well; the full list is in [[TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES]] and the
security exposure in [[TROUBLE-ENVOY_GATEWAY_KNOWN_CVES]].

## References

- Upstream `release-notes/v1.2.*.yaml`, `bug fixes` sections, read at `origin/main` on 2026-07-31.
- Add-on: [[CONCEPT-ADDON_ENVOY_GATEWAY]].
