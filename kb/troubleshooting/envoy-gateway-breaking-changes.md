---
id: TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES
type: troubleshooting
title: "Envoy Gateway: every breaking change, 1.2.0 → 1.8.3"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.2.0 <=1.8.3"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - envoy gateway breaking changes
  - envoy gateway upgrade broke
  - envoy gateway behaviour changed after upgrade
  - envoy patch policy broken by upgrade
  - gateway api crd bump envoy gateway
tags:
  - upgrade
  - envoy
  - gateway-api
  - breaking-change
sources:
  - type: code
    path: envoyproxy/gateway release-notes/*.yaml — "breaking changes" sections of all 62 releases
    url: https://github.com/envoyproxy/gateway/tree/main/release-notes
    note: "verbatim upstream list; 52 entries across 13 releases"
relations:
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_KNOWN_CVES
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_1_6_KNOWN_ISSUES
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
---

# Envoy Gateway: every breaking change, 1.2.0 → 1.8.3

## Summary

**52 behaviour changes** are declared across the project's history. Five of them ship in
**patch** releases (1.3.1, 1.6.4, 1.6.6, 1.8.1, 1.8.2, 1.8.3) — so "it is only a patch bump" is not
a safe assumption for this component; read the list before any upgrade, including within a line.

The changes that most often surprise operators:

- **1.5.0 — xDS listener names were renamed** to port+protocol instead of Gateway name and section
  name. This breaks existing `EnvoyPatchPolicy` objects and extension managers that match on the old
  names. Silent until traffic misbehaves.
- **1.3.0 — extension-server errors became fail-closed**: any error from an extension server now
  replaces the affected resource with an "Internal Server Error" route.
- **1.3.0 / 1.6.6 / 1.7.0 — translation failures became 500s** instead of being partially ignored:
  `ClientTrafficPolicy`, `BackendTLSPolicy` and invalid route filters now answer 500 rather than
  silently half-working.
- **1.6.0 — upstream TLS gained SNI/SAN requirements** and ALPN defaults; backends whose
  certificates lack a matching DNS SAN start failing validation.
- **1.3.0 — passive health checking (outlier detection) is off by default.**
- **1.2.0 — the CPU limit was removed** from the controller Deployment to eliminate throttling.

## Problem

A behaviour change in this component usually manifests as traffic being answered by the gateway
itself (500/503) or as a policy silently ceasing to apply, not as a failed rollout. The upgrade
succeeds; the symptom appears later, in production traffic.

## Context

Verbatim, grouped by release.

### v1.2.0 — 6

- Gateway API GRPCRoute and ReferenceGrant v1alpha2 have been removed
- Please refer to the [Gateway API v1.2.0 documentation](https://github.com/kubernetes-sigs/gateway-api/releases) for more information
- Removed default CPU limit of the Envoy Gateway deployment, to eliminate CPU throttling
- Changed default Envoy shutdown settings: drain strategy has been changed to immediate, default minDrainDuration, drainTimeout and terminationGracePeriodSeconds have been set to 10s, 60s and 360s respectively
- Set ignore_health_on_host_removal to true for clusters with static endpoints This was done to speed up removal of static endpoints by the control plane when active health check is configured
- Xds and Infra IR logs are logged at Debug level instead of Info level. They will now not be seen by default in Envoy Gateway logs. You can change the logging level to default: debug to view them

### v1.3.0 — 7

- The Container `ports` field of the gateway instance has been removed, which will cause the gateway Pod to be rebuilt when upgrading the version.
- ClientTrafficPolicy previously treated an empty TLS ALPNProtocols list as being undefined and applied Envoy Gateway defaults. An empty TLS ALPNProtocols list is now treated as user-defined disablement of the TLS ALPN extension.
- Outlier detection (passive health check) is now disabled by default. refer to https://gateway.envoyproxy.io/docs/api/extension_types/#backendtrafficpolicy for working with passive health checks.
- Envoy Gateway treats errors in calls to an extension service as fail-closed by default. Any error returned from the extension server will replace the affected resource with an "Internal Server Error" immediate response. The previous behavior can be enabled by setting the `failOpen` field to `true` in the extension service configuration.
- Envoy Gateway now return a 500 response when a ClientTrafficPolicy translation fails for HTTP/GRPC routes, and forwards client traffic to an empty cluster when a ClientTrafficPolicy translation fails for TCP routes.
- Any issues with `EnvoyProxy` reference in a `Gateway` will prevent the Envoy fleet from being created or result in the deletion of an existing Envoy fleet.
- Envoy Gateway now returns a 500 response when a BackendTLSPolicy translation fails for HTTP/GRPC/TLS routes.

### v1.3.1 — 1

- Use the envoy JSON formatter for the default access log instead of text formatter.

### v1.4.0 — 5

- Use a dedicated listener port(19003) for envoy proxy readiness
- Uses the envoy JSON formatter for the default access log instead of text formatter.
- Envoy Gateway will skip xDS snapshot updates in case of errors during xDS translation.
- When Extension Manager is configured to Fail Open, translation errors are logged and suppressed.
- When Extension Manager is configured to not Fail Open, Envoy Gateway will no longer replace affected resources. Instead, xDS snapshot update would be skipped.

### v1.5.0 — 5

- Use gateway name as proxy fleet name for gateway namespace mode.
- Endpoints that are absent from service discovery are removed even if their active health checks succeed.
- The xDS listener name are now renamed based on its listening port and protocol, instead of the Gateway name and section name. This breaks existing EnvoyPatchPolicies and ExtensionManagers as they depend on the old naming scheme. This change is guarded by the `XDSNameSchemeV2` runtime flag. This flag is disabled by default in v1.5, and it will be enabled in v1.6. We recommend users to migrate their EnvoyPatchPolicies and ExtensionManagers to use the new listener names before v1.6. Visit https://gateway.envoyproxy.io/tasks/extensibility/envoy-patch-policy/#xds-name-scheme-v2 to view the new naming scheme.
- Removed `xds-translator` and `xds-server` values from the `runner` label in `watchable_subscribe_total`. Use `xds` instead.
- Accessloggers of type ALS now have http2 enabled on the cluster by default.

### v1.6.0 — 7

- ALPNProtocols in EnvoyProxy Backend TLS settings now default to [h2, http/1.1] when not explicitly configured.
- When a Backend resource specifies TLS settings and SNI is not specified or a BackendTLSPolicy is not attached to it, the upstream TLS SNI value is now automatically determined from the HTTP Host header.
- When a Backend resource specifies TLS settings and SNI is not specified or a BackendTLSPolicy is not attached to it, upstream certificate validation now requires DNS SAN to match the SNI value that is sent.
- When a MirrorPolicy is used, the shadow host suffix is no longer automatically appended to the mirrored cluster name.
- When running `egctl experimental collect`, SDS (Secret Discovery Service) data is no longer included by default. To include SDS data, enable it by adding the `--sds true` flag.
- When setting `consecutiveGatewayFailure`, `enforcingConsecutiveGatewayFailure` is automatically set to 100.
- When the OIDC provider issues a refresh token, Envoy Gateway will now automatically use it to refresh access and ID tokens when they expire. To maintain the previous behavior (not using refresh tokens), set `refreshToken` to false in the OIDC authentication configuration. See https://gateway.envoyproxy.io/docs/api/extension_types/#securitypolicyspec for details.

### v1.6.4 — 1

- Gateway API CRD has been updated, more details could be found [here](https://github.com/kubernetes-sigs/gateway-api/issues/4490).

### v1.6.6 — 2

- Returning 500 direct responses for HTTPRoute and GRPCRoute with invalid filters.
- Set HTTPRoute Accepted status to False when RequestMirror filter is used together with DirectResponse or RequestRedirect filters.

### v1.7.0 — 7

- The SecurityPolicy name has been added to the stat prefix for oauth2 filter metrics to provide better granularity. Example: http.https-10443.securitypolicy/default/oidc-example.oauth_success: 0.
- Return 500 direct responses for HTTPRoute and GRPCRoute with invalid filters.
- When an HTTPRoute rule is configured with host-rewrite filters and routes to a Dynamic Resolver backend, the rewritten Host header is used for both DNS resolution and as the Host header in upstream requests.
- Set HTTPRoute Accepted status to False when RequestMirror filter is used together with DirectResponse or RequestRedirect filters.
- Removed Accept-Encoding header from requests to backends when compression is enabled to avoid double compression issues.
- The default value `stats_tags` has been changed to improve the prometheus metrics output. Following metrics are affected: `envoy_cluster_*_rq_time_count`, `envoy_cluster_*_total_match_count`, `envoy_cluster_circuit_breakers_*_cx_open`.
- Default HTTP filter ordering now places envoy.filters.http.custom_response at the first, which can change the behavior of local replies and header processing.

### v1.8.0 — 7

- Bumped the bundled Gateway API CRDs to [v1.5.1](https://github.com/kubernetes-sigs/gateway-api/releases/tag/v1.5.1). The controller now unconditionally starts an informer for ListenerSet, so the updated Gateway API CRDs must be installed before upgrading.
- The DirectResponse body in HTTPFilter now supports Envoy command operators for dynamic content. Existing configurations including the template syntax (%) will be interpolated.
- The `0s` timeout in SecurityPolicy is now treated as infinite timeout instead of immediate timeout.
- Fixed EnvoyProxy `samplingFraction` translation to correctly convert the Gateway API fraction into Envoy's percentage-based `random_sampling` field. Existing `samplingFraction` configurations will now sample 100x more frequently than in previous releases; divide previous values by 100 to preserve prior sampling rates.
- The controller now uses production logging encoder config by default, which provides better output when using JSON encoder.
- SecurityPolicy OIDC now generates a single native `envoy.filters.http.oauth2` HTTP filter in the HCM filter chain and moves route-specific OAuth2 configuration to route `typed_per_filter_config`. This can break existing EnvoyPatchPolicies and extension managers that depend on the previous per-route OAuth2 filter instances or on the old OAuth2 filter configuration shape in the HCM filter chain.
- Merged SecurityPolicy IR/xDS resource names (OIDC, BasicAuth, ExtAuth, JWT) now derive from the policy that contributes the field (parent or route) rather than always using the route-level policy. EnvoyPatchPolicy users who reference those generated names must update their patch targets.

### v1.8.1 — 1

- Moved the Gateway API safe-upgrades ValidatingAdmissionPolicy resources out of the CRD bundle and into the gateway-helm chart templates so tools such as Flux no longer treat them as CRDs. During upgrades, two upgrade cases require action: (1) if you install Gateway API CRDs separately (e.g. with the gateway-crds-helm chart and `helm install --skip-crds`), the safe-upgrades ValidatingAdmissionPolicy and its binding are now rendered by the gateway-helm chart, so add Helm ownership metadata (the `meta.helm.sh/release-name`, `meta.helm.sh/release-namespace` annotations and the `app.kubernetes.io/managed-by=Helm` label) to the `ValidatingAdmissionPolicy/safe-upgrades.gateway.networking.k8s.io` and `ValidatingAdmissionPolicyBinding/safe-upgrades.gateway.networking.k8s.io` resources before upgrading so Helm can manage them (see https://gateway.envoyproxy.io/v1.8/install/install-helm/#installing-crds-separately); (2) if Gateway API CRDs and safe upgrade policy resources are managed by your cloud provider (or any other mechanism outside this chart), note that `--skip-crds` does not skip chart-templated resources, so disable rendering of the safe-upgrades ValidatingAdmissionPolicy by setting `crds.gatewayAPI.safeUpgradePolicy.enabled=false` (see https://gateway.envoyproxy.io/v1.8/install/install-helm/#clusters-with-compatible-provider-managed-gateway-api-crds).

### v1.8.2 — 2

- The `XRateLimitHeadersOptionDisabled` constant in `BackendTrafficPolicy` now correctly holds the value `"Off"` to match the CRD enum (previously `"Disabled"`). Since `"Disabled"` was never a valid CRD enum value and would have been rejected by the API server, no existing manifests are affected.
- `SecurityPolicy` `spec.apiKeyAuth.extractFrom` admission validation is now stricter: the list must contain at least one entry, each entry must specify exactly one of `headers`, `params`, or `cookies`, and source names must be non-empty. SecurityPolicies that previously applied with an empty or ambiguous `extractFrom` (which produced no usable API key sources) will now be rejected and must be corrected before upgrading.

### v1.8.3 — 1

- Moved EnvoyExtensionPolicy Lua source code from per-route `LuaPerRoute` overrides to listener-level Lua filters to avoid route-count-dependent memory growth. This changes generated xDS Lua filter names and configuration layout; EnvoyPatchPolicies and extension servers matching the previous `envoy.filters.http.lua/<index>` keys must be updated.

## Diagnostics

```bash
# what is running now
kubectl -n <eg-ns> get deploy envoy-gateway \
  -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'

# objects most exposed to renames and stricter validation
kubectl get envoypatchpolicy -A
kubectl get clienttrafficpolicy,backendtlspolicy,backendtrafficpolicy -A
kubectl get httproute,grpcroute -A -o json \
  | grep -c '"type": *"RequestMirror"'
```

After any upgrade, check route status rather than pod health: a rejected route stays `Accepted:
False` while every pod is `Running`.

## Known Issues

**Patch releases carry behaviour changes.** 1.6.4 updates the Gateway API CRDs; 1.6.6 turns invalid
filters into 500 direct responses and rejects `RequestMirror` combined with `DirectResponse` or
`RequestRedirect`; 1.8.2 tightens `SecurityPolicy` admission validation; 1.8.3 moves Lua from
per-route overrides to listener-level filters, changing the generated xDS.

**`EnvoyPatchPolicy` is the fragile surface.** It matches generated xDS by name, so any release that
renames or reorders generated resources (1.5.0 listener names, 1.7.0 default filter ordering, 1.8.0
OIDC filter consolidation, 1.8.3 Lua placement) can neutralise a patch policy without an error.

**Upgrade order:** Gateway API CRDs first, then the controller, then confirm the proxy Deployments
rolled — the data-plane image ships with the release but old proxy pods keep running until
restarted.

## References

- Upstream `release-notes/*.yaml`, `breaking changes` sections of all 62 releases, read at
  `origin/main` on 2026-07-31.
- Security exposure: [[TROUBLE-ENVOY_GATEWAY_KNOWN_CVES]]; defects on the 1.6 line:
  [[TROUBLE-ENVOY_GATEWAY_1_6_KNOWN_ISSUES]]; add-on: [[CONCEPT-ADDON_ENVOY_GATEWAY]].
