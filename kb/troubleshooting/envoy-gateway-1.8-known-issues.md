---
id: TROUBLE-ENVOY_GATEWAY_1_8_KNOWN_ISSUES
type: troubleshooting
title: "Envoy Gateway 1.8: every defect fixed in the 1.8 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.8.0 <1.9.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - envoy gateway 1.8 known issues
  - envoy gateway 1.8 bugs
  - envoy gateway 1.8 fixed in
tags:
  - troubleshooting
  - envoy
  - gateway-api
  - upgrade
sources:
  - type: code
    path: envoyproxy/gateway release-notes/v1.8.*.yaml — "bug fixes" sections
    url: https://github.com/envoyproxy/gateway/tree/main/release-notes
    note: "4 releases on this line, 70 declared fixes"
relations:
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_KNOWN_CVES
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
---

# Envoy Gateway 1.8: every defect fixed in the 1.8 line

## Summary

The **1.8** maintenance line published **4 releases** carrying **70 defect fixes**,
11 breaking changes and 8 security updates.
Running anything below **1.8.3** on this line means carrying the remainder of the list
below.

Use this page the way a defect database is used: before filing "Envoy Gateway does X wrong", search
here — the odds are it is already named, with the exact patch that fixes it.

## Problem

Defects are grouped by the release that fixed them; a cluster on version *N* carries everything
listed under versions greater than *N*.

## Context

### v1.8.0 — 38

- Fixed local rate limit rules with identical sourceCIDR client selectors producing conflicting descriptors.
- Rejected ClientTrafficPolicy if invalid TLS cipher suites are configured.
- Fixed ClientTrafficPolicy to disable HTTP/3 and surface a warning on the policy when downstream client TLS validation is configured, instead of generating a rejected QUIC listener.
- Fixed validation of XListenerSet certificateRefs.
- Fixed XListenerSet not allowing xRoutes from the same namespace when configured to allow them.
- Fixed API key authentication dropping non-first client IDs when credential Secrets contain multiple keys.
- Fixed `X-ENVOY-ORIGINAL-HOST` not being set when `headers.enableEnvoyHeaders` is enabled and hostname rewrite is configured for DynamicResolver type of Backends.
- Fixed standalone mode emitting non-actionable error logs for missing secrets and unsupported ratelimit deletion on every startup.
- Fixed local object reference resolution from parent policy in merged BackendTrafficPolicies.
- Fixed xPolicy resources being processed from all namespaces when NamespaceSelector watch mode is configured in the Kubernetes provider.
- Fixed route and policy status aggregation across multiple GatewayClasses managed by the same controller, so resources preserve status from all relevant parents and ancestors instead of being overwritten by the last processed GatewayClass.
- Fixed route status parent aggregation when the number of parents exceeds the Gateway API cap of 32.
- Made ConnectionLimit.Value optional so users can configure MaxConnectionDuration, MaxRequestsPerConnection, or MaxStreamDuration without setting a max connections value.
- Fixed endpoint hostname not being respected during active health checks.
- Fixed ratelimit deployment missing metrics container port (19001), which prevented PodMonitor/ServiceMonitor from targeting the metrics endpoint.
- Fixed ratelimit ServiceAccount missing standard Kubernetes app labels.
- Fixed GRPCRoute RequestMirror filter backend not being indexed, causing "service not found" errors for mirror targets that exist in the cluster.
- Fixed GRPCRoute not detecting conflicting RequestMirror and DirectResponse filters, which caused the mirror to be silently dropped.
- Fixed BackendTrafficPolicy `requestBuffer` coexisting with route upgrades by disabling the default WebSocket upgrade on buffered routes and rejecting explicit `requestBuffer` + `httpUpgrade` combinations.
- Fixed per-endpoint hostname override not working due to the auto-generated wildcard hostname.
- Fixed Basic Authentication failing when htpasswd secrets use CRLF line endings by normalizing to LF before passing to Envoy.
- Fixed BackendTLSPolicy being ignored when configuring TLS for telemetry backends (access logs, tracing, metrics).
- Fixed client certificate secret never being delivered when exclusively referenced by a SecurityPolicy `extAuth`/`jwt`/`oidc` Backend.
- Fixed xRoutes being incorrectly marked unaccepted when a RequestMirror filter referenced a backend with no endpoints; the route now remains accepted with `BackendsAvailable=False`, per Gateway API conformance.
- Fixed `ws` and `wss` Backend appProtocols to force HTTP/1.1 upstream connections instead of negotiating HTTP/2, avoiding compatibility issues with WebSocket backends that do not support RFC 8441 extended CONNECT.
- Fixed gateway-helm RBAC in GatewayNamespace mode with explicit `watch.namespaces` list by adding controller-namespace secret read permissions to infra-manager.
- Fixed a control plane panic caused by concurrent Status mutation racing with the watchable Map coalesce goroutine.
- Fixed BackendTrafficPolicy rate limit `requests` values above uint32 max (4294967295) being silently truncated modulo 2^32 by the rate limit service and Envoy token bucket. The field now rejects such values at admission time with a clear schema validation error.
- Fixed status conditions not being updated when a route is rejected due to multiple errors.
- Fixed spurious development-mode panic log from the gatewayapi translator.
- Fixed SecurityPolicy merge using the wrong policy as the owner for resource references and IR generation.
- Fixed ListenerSet and its listeners incorrectly setting `Accepted: False` for InvalidCertificateRef and RefNotPermitted, inconsistent with Gateway behavior and the Gateway API spec.
- Fixed active HTTP health checks to use Backend endpoint hostnames before falling back to the effective Route hostname.
- Fixed HTTPS listeners with overlapping hostnames but disjoint certificate SANs to preserve HTTP/2 ALPN by default.
- Removed the spurious cross-namespace policy-attachment warning condition when a ReferenceGrant is missing (#8901).
- Fixed an invalid first listener winning hostname/protocol precedence and causing a later valid listener on the same hostname/port to be marked HostnameConflict (#8577).
- Increased `RateLimitSelectCondition.headers` MaxItems from 16 to 64, matching the existing `HTTPHeaderFilter` pattern (#8906).
- Fixed Gateway getting stuck at `Programmed=False` after its LoadBalancer Service IP was restored, by ignoring `LastTransitionTime` when comparing status conditions.

### v1.8.1 — 12

- Fixed the xDS server in GatewayNamespaceMode serving a stale certificate after cert-manager rotation by re-reading the cert from disk on every TLS handshake.
- Fixed controller panic when processing backend tls settings.
- Fixed BackendTLSPolicy selection to prefer section name over wildcard match on the same backend.
- Fixed ClientTrafficPolicy TLS cipher validation rejecting supported IANA/RFC cipher suite names.
- Fixed Kubernetes provider namespace-scoped watches to always include the controller namespace so Envoy Gateway can read its own infrastructure resources.
- Fixed TLS secrets with non-canonical PEM formatting (e.g. unusual line endings) being passed verbatim to Envoy, which could cause BoringSSL errors such as `BAD_END_LINE`. Cert and key PEM data is now re-encoded to a canonical form before being delivered as xDS resources.
- Fixed `MaxStreamDuration` not being set on `CommonHttpProtocolOptions` for non-route cluster.
- Fixed `egctl x status all`/`xroute`/`xpolicy` failing when a Gateway API CRD (e.g. TCPRoute) is not installed in the cluster; missing CRDs are now skipped silently, or reported on stderr with `-v`.
- Fixed Kubernetes Service and ServiceImport `appProtocol` values `kubernetes.io/ws` and `kubernetes.io/wss` to force HTTP/1.1 upstream connections instead of negotiating HTTP/2, avoiding compatibility issues with WebSocket backends that do not support RFC 8441 extended CONNECT.
- Fixed Gateway getting stuck at `Programmed=False` after its LoadBalancer Service IP was restored, by ignoring `LastTransitionTime` when comparing status conditions.
- Fixed HPA maxReplicas required message typo in gateway-helm chart.
- Fixed invalid listeners blocking valid ones during conflict detection by validating each listener's spec independently before running conflict resolution.

### v1.8.2 — 12

- Fixed API key auth credential ordering to avoid unnecessary xDS updates.
- Fixed the EnvoyProxy resource not allowing IPv6 ranges in loadBalancerSourceRanges when configuring the envoy service.
- Fixed HTTPRoute, GRPCRoute, TLSRoute, TCPRoute, and UDPRoute Accepted condition being set to False when an attached listener is not programmed due to a missing TLS certificate ref; listener programmed state is now correctly separated from route acceptance.
- Fixed Backend TLS `alpnProtocols: []` to disable upstream ALPN instead of inheriting EnvoyProxy BackendTLS defaults.
- Fixed BackendTrafficPolicy rate limit validation failing on Kubernetes 1.36, which now cross-validates integer ranges against their configured maximum, by validating the affected field as int64.
- Fixed the generated `install.yaml` creating a duplicate ValidatingAdmissionPolicy and its binding which caused `kustomize build` to fail with a duplicate resource error.
- Fixed an `ExternalName` Service referenced as a route backend producing an invalid xDS cluster (with an empty address) that failed IR validation and stalled config delivery for the whole snapshot. `ExternalName` Services are now explicitly rejected as backends with a `ResolvedRefs: False` route condition; use an Envoy Gateway `Backend` resource with an FQDN endpoint instead.
- Fixed ListenerSet hostname conflict resolution to apply listener precedence: Gateway-owned listeners win over ListenerSet listeners, and among ListenerSet listeners the first in processing order wins. Conflicted ListenerSet listeners now correctly report Accepted=False with the conflict reason. The Gateway's AttachedListenerSets count now only reflects ListenerSets with at least one accepted listener.
- Fixed Gateway status reporting `Programmed: False` with reason `AddressNotAssigned` when the Envoy LoadBalancer service has no load balancer ingress (e.g. bare-metal clusters without a load balancer controller) but has addresses configured in `spec.externalIPs`, such as via an EnvoyProxy service patch. The external IPs are now used as a fallback for the Gateway status addresses.
- Fixed EnvoyGateway config hot-reload to apply defaults before validation, so validators always run against a fully-defaulted struct on both the startup and reload paths.
- Fixed HTTPRoute per-retry timeout (derived from `rule.timeouts.backendRequest`) not being applied when no retry backoff was configured.
- Fixed shared global rate limit rules with a `cost` field not working as expected.

### v1.8.3 — 8

- Fixed backend (upstream) TLS connections being capped at TLS 1.2 by default; they now default to a max of TLS 1.3 as documented.
- Fixed TLS Secrets being pushed to Envoy and rejected by BoringSSL (KEY_VALUES_MISMATCH), which with mergeGateways enabled broke TLS for all Gateways sharing the proxy. A serving certificate chain that contains an expired (or malformed) certificate is now rejected during translation instead of having the expired member silently dropped (which corrupted the chain), and a Secret whose certificate and private key do not match is likewise rejected; both failures are isolated to the referencing listener. CA bundles used for client validation still drop expired CAs.
- Fixed a data race that could crash envoy-gateway with `panic: reflect: slice index out of range` when the watchable coalesce goroutine compared the xDS IR with `reflect.DeepEqual` while the translator concurrently mutated resource status in place; the translator now isolates status mutations by deep-copying only the status field of each resource at the start of translation.
- Fixed unreferenced Secret events triggering a full reconciliation whenever the HTTPRouteFilter CRD is installed. Every Secret write in the cluster previously enqueued a reconcile, causing sustained reconcile storms on clusters with high-frequency Secret writers (secret sync controllers, certificate rotation).
- Fixed Wasm extensions remaining permanently failed after transient errors fetching the Wasm module. Envoy's built-in behavior only retried the fetch once after ~1 second and never re-attempted it, leaving the filter failed until the next configuration update. Envoy Gateway now configures the fetch with up to 10 retries using jittered exponential backoff (1s base interval, 30s max interval).
- Fixed log timestamps regressing to Unix epoch floats (e.g. `1.784e+09`) since v1.8.0 by explicitly setting `ISO8601TimeEncoder` on the production zap encoder config, restoring the expected ISO 8601 format (e.g. `2026-07-14T17:44:06.617Z`).
- Fixed IPv6 literal hosts (e.g. `[::1]`, `[2001:db8::1]`) not being detected in OIDC token/JWKS endpoints, which caused them to be built as STRICT_DNS clusters instead of static ones and bypassed the IP-literal check on the SecurityPolicy token endpoint.
- Fixed the gateway-helm chart resolving the ratelimit image to an outdated build (`ff287602` instead of `1e50889b`) when `global.images.ratelimit.image` is set without a tag.

## Diagnostics

```bash
kubectl -n <eg-ns> get deploy envoy-gateway \
  -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```

Compare against **1.8.3** — the newest release of this line.

## Known Issues

Upgrading inside a maintenance line is the low-risk move, but this project ships behaviour changes
in patch releases as well; the full list is in [[TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES]] and the
security exposure in [[TROUBLE-ENVOY_GATEWAY_KNOWN_CVES]].

## References

- Upstream `release-notes/v1.8.*.yaml`, `bug fixes` sections, read at `origin/main` on 2026-07-31.
- Add-on: [[CONCEPT-ADDON_ENVOY_GATEWAY]].
