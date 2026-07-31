---
id: TROUBLE-ENVOY_GATEWAY_1_7_KNOWN_ISSUES
type: troubleshooting
title: "Envoy Gateway 1.7: every defect fixed in the 1.7 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.7.0 <1.8.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - envoy gateway 1.7 known issues
  - envoy gateway 1.7 bugs
  - envoy gateway 1.7 fixed in
tags:
  - troubleshooting
  - envoy
  - gateway-api
  - upgrade
sources:
  - type: code
    path: envoyproxy/gateway release-notes/v1.7.*.yaml — "bug fixes" sections
    url: https://github.com/envoyproxy/gateway/tree/main/release-notes
    note: "6 releases on this line, 64 declared fixes"
relations:
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_KNOWN_CVES
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
---

# Envoy Gateway 1.7: every defect fixed in the 1.7 line

## Summary

The **1.7** maintenance line published **6 releases** carrying **64 defect fixes**,
7 breaking changes and 22 security updates (CVE-2026-24051, CVE-2026-33186, CVE-2026-47774).
Running anything below **1.7.5** on this line means carrying the remainder of the list
below.

Use this page the way a defect database is used: before filing "Envoy Gateway does X wrong", search
here — the odds are it is already named, with the exact patch that fixes it.

## Problem

Defects are grouped by the release that fixed them; a cluster on version *N* carries everything
listed under versions greater than *N*.

## Context

### v1.7.0 — 21

- Fixed configured OIDC authorization endpoint being overridden by discovered endpoints from issuer's well-known URL.
- Fixed 500 errors caused by partially invalid BackendRefs; traffic is now correctly routed between valid backends and 500 responses according to their configured weights.
- Fixed an issue where BackendTrafficPolicy does not validate maximum value of requestBuffer limit.
- Fixed an issue where observedGeneration is missing from the EnvoyPatchPolicy status.
- Fixed a nil pointer error when applying BackendTrafficPolicy to HTTPRoutes with no backendRefs.
- Fixed ExternalTrafficPolicy not being applied to Envoy Service when ServiceType is NodePort.
- Fixed CRL ref not processed by gateway controller.
- Fixed an issue where HTTP/3 listeners could not handle multiple hostnames.
- Fixed gateway continuing with incomplete resources after unrecoverable Kubernetes discovery errors when checking optional CRDs by failing fast and propagating errors so pods restart instead of skipping optional CRDs.
- Fixed an issue where listener translation fails when it contains invalid certificate in multiple TLS certificateRefs.
- Fixed an issue where auto-detect upstream protocol breaks with multiple backends (HTTP + HTTPS).
- Fixed validation of certificates in a CA bundle when some certificates are invalid.
- Fixed an issue where route match rule order is wrong when merging with empty path match.
- Fixed wrong cluster type selection when an HTTPRoute mixes Service backends with Backend (FQDN) references, ensuring STRICT_DNS clusters are generated for the FQDN targets.
- Fixed JWT scope authorization to accept the `scp` claim in addition to `scope`.
- Fixed SecurityPolicy BasicAuth validation to reject invalid {SHA} htpasswd entries.
- Allowed single-label backend hostnames when running with the Host infrastructure, enabling Docker Compose service names for telemetry backends.
- Fixed an issue where message package didn't adopt logging level.
- Fixed issue with controller pods reporting as ready before successful cache sync.
- Fixed issue where TCPRoute was not correctly handling mTLS settings.
- Fixed validation of XListenerSet certificateRefs

### v1.7.1 — 9

- Fixed an issue where specifying Value in ConnectionLimit was not optional. It now uses the Envoy default value if absent.
- Fixed route and policy status aggregation across multiple GatewayClasses managed by the same controller, so resources preserve status from all relevant parents and ancestors instead of being overwritten by the last processed GatewayClass.
- Fixed an issue where endpoint hostname was not respected when doing an active health check.
- Fixed an issue where computeHosts did not work when both listener and route had wildcard hostnames.
- Fixed local object reference resolution from parent policy in merged BackendTrafficPolicies.
- Fixed XListenerSet not allowing xRoutes from the same namespace when configured to allow them.
- Fixed API key authentication dropping non-first client IDs when credential Secrets contain multiple keys.
- Fixed an issue where SecurityPolicy route-target status included unmanaged Gateway parents when HTTPRoute had mixed parentRefs.
- Fixed an issue where ratelimit ConfigMap and HPA were not automatically cleaned up when the parent envoy-gateway Deployment was deleted.

### v1.7.2 — 14

- Rejected ClientTrafficPolicy if invalid TLS cipher suites are configured.
- Fixed validation of XListenerSet certificateRefs
- Fixed standalone mode emitting non-actionable error logs for missing secrets and unsupported ratelimit deletion on every startup.
- Fixed xPolicy resources being processed from all namespaces when NamespaceSelector watch mode is configured in the Kubernetes provider.
- Fixed route status parent aggregation when the number of parents exceeds the Gateway API cap of 32.
- Fixed ratelimit deployment missing metrics container port (19001), which prevented PodMonitor/ServiceMonitor from targeting the metrics endpoint.
- Fixed GRPCRoute RequestMirror filter backend not being indexed, causing "service not found" errors for mirror targets that exist in the cluster.
- Fixed GRPCRoute not detecting conflicting RequestMirror and DirectResponse filters, which caused the mirror to be silently dropped.
- Fixed per-endpoint hostname override not working because the auto-generated wildcard hostname.
- Fixed Basic Authentication failing when htpasswd secrets use CRLF line endings by normalizing to LF before passing to Envoy.
- BackendTLSPolicy was ignored when configuring TLS for telemetry backends (access logs, tracing, metrics).
- Fixed client certificate secret never delivered when it is exclusively referenced by a SecurityPolicy `extAuth`/`jwt`/`oidc` Backend.
- Fixed xRoute status condition when route has mirror filter and the mirror backend has no endpoints.
- Fixed gateway-helm RBAC in GatewayNamespace mode with explicit `watch.namespaces` list by adding controller-namespace secret read permissions to infra-manager.

### v1.7.3 — 5

- Fixed a control plane panic caused by concurrent Status mutation racing with the watchable Map coalesce goroutine.
- Fixed `ws` and `wss` Backend appProtocols to force HTTP/1.1 upstream connections instead of negotiating HTTP/2, avoiding compatibility issues with WebSocket backends that do not support RFC 8441 extended CONNECT.
- Fixed status conditions not being updated when a route is rejected due to multiple errors.
- Fixed benchmark JSON report emitting `0` for p99 and p999 percentiles by using the nearest Nighthawk histogram percentiles.
- Fixed active HTTP health checks to use Backend endpoint hostnames before falling back to the effective Route hostname.

### v1.7.4 — 6

- Fixed TLS secrets with non-canonical PEM formatting (e.g. unusual line endings) being passed verbatim to Envoy, which could cause BoringSSL errors such as `BAD_END_LINE`. Cert and key PEM data is now re-encoded to a canonical form before being delivered as xDS resources.
- Fixed the xDS server in GatewayNamespaceMode serving a stale certificate after cert-manager rotation by re-reading the cert from disk on every TLS handshake.
- Fixed Gateway getting stuck at `Programmed=False` after its LoadBalancer Service IP was restored, by ignoring `LastTransitionTime` when comparing status conditions.
- Fixed HPA maxReplicas required message typo in gateway-helm chart.
- Fixed BackendTLSPolicy selection to prefer section name over wildcard match on the same backend.
- Fixed invalid listeners blocking valid ones during conflict detection by validating each listener's spec independently before running conflict resolution.

### v1.7.5 — 9

- Fixed the EnvoyProxy resource not allowing IPv6 ranges in loadBalancerSourceRanges when configuring the envoy service.
- Fixed Backend TLS `alpnProtocols: []` to disable upstream ALPN instead of inheriting EnvoyProxy BackendTLS defaults.
- Fixed API key auth credential ordering to avoid unnecessary xDS updates.
- Fixed an `ExternalName` Service referenced as a route backend producing an invalid xDS cluster (with an empty address) that failed IR validation and stalled config delivery for the whole snapshot. `ExternalName` Services are now explicitly rejected as backends with a `ResolvedRefs: False` route condition; use an Envoy Gateway `Backend` resource with an FQDN endpoint instead.
- Fixed Gateway status reporting `Programmed: False` with reason `AddressNotAssigned` when the Envoy LoadBalancer service has no load balancer ingress (e.g. bare-metal clusters without a load balancer controller) but has addresses configured in `spec.externalIPs`, such as via an EnvoyProxy service patch. The external IPs are now used as a fallback for the Gateway status addresses.
- Fixed EnvoyGateway config hot-reload to apply defaults before validation, so validators always run against a fully-defaulted struct on both the startup and reload paths.
- Fixed a nil-pointer panic when `provider.kubernetes.deploy` is configured without a `type`.
- Fixed DaemonSet pod not using the configured custom ServiceAccount name.
- Fixed the rate limit `requests` CRD field to use `format: int64` so Kubernetes 1.36 accepts the `maximum` constraint.

## Diagnostics

```bash
kubectl -n <eg-ns> get deploy envoy-gateway \
  -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```

Compare against **1.7.5** — the newest release of this line.

## Known Issues

Upgrading inside a maintenance line is the low-risk move, but this project ships behaviour changes
in patch releases as well; the full list is in [[TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES]] and the
security exposure in [[TROUBLE-ENVOY_GATEWAY_KNOWN_CVES]].

## References

- Upstream `release-notes/v1.7.*.yaml`, `bug fixes` sections, read at `origin/main` on 2026-07-31.
- Add-on: [[CONCEPT-ADDON_ENVOY_GATEWAY]].
