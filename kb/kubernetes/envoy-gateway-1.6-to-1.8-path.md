---
id: UPGRADE-ENVOY_GATEWAY_1_6_TO_1_8
type: upgrade
title: "Envoy Gateway 1.6 → 1.7 / 1.8: a critical CVE up front, generated config rearranged behind it"
status: active
kubespray_version: ">=v2.29.1 <=v2.31.0"
kubernetes_version: null
component_version: ">=1.6.0 <=1.8.3"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - envoy gateway 1.6 to 1.7 upgrade
  - envoy gateway 1.8 what breaks
  - should we upgrade envoy gateway
  - envoy patch policy broken after upgrade
  - envoy gateway grpc authorization bypass
tags:
  - upgrade
  - envoy
  - gateway-api
  - security
sources:
  - type: code
    path: envoyproxy/gateway release-notes/v1.7.*.yaml, v1.8.*.yaml
    url: https://github.com/envoyproxy/gateway/tree/main/release-notes
    note: "7 breaking changes on 1.7, 11 across 1.8.x; CVE fixes at 1.7.3 and 1.7.4"
relations:
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_KNOWN_CVES
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
---

# Envoy Gateway 1.6 → 1.7 / 1.8: a critical CVE up front, generated config rearranged behind it

## Summary

Two arguments pull in opposite directions here, and they should be weighed separately.

**For moving:** `CVE-2026-33186` is a **critical authorization bypass in gRPC-Go via a
non-canonical HTTP/2 `:path` header**, fixed at **1.6.7 and 1.7.3**. On a gateway terminating ~1400
routes, a large share of them gRPC, this is the single most consequential item in the whole
comparison.

**Against rushing:** 1.7 and 1.8 rearrange **generated Envoy configuration** — filter ordering, OIDC
filter shape, Lua placement, metric tag defaults. None of it breaks the Gateway API objects; all of
it can break something built on top of the generated output.

The safe reading: the CVE does **not** require leaving 1.6. It is fixed at **1.6.7**, inside the
line. Take the security fix as a patch bump, then treat 1.7/1.8 as a separate, planned change.

## Upgrade Notes

**1.7 — seven declared behaviour changes.** The ones that reach traffic:

- **Invalid filters now return 500 direct responses** for HTTPRoute and GRPCRoute, and
  `RequestMirror` combined with `DirectResponse` or `RequestRedirect` sets `Accepted: False`.
  Routes that half-worked silently start failing loudly. Audit filters before, not after.
- **Default HTTP filter ordering changed** — `envoy.filters.http.custom_response` moves to the
  front, which changes how local replies and header processing behave.
- **`Accept-Encoding` is removed from requests to backends** when compression is enabled, to avoid
  double compression. Backends that varied on that header see different requests.
- **Host rewrite with a Dynamic Resolver backend** now uses the rewritten Host for DNS resolution as
  well as for the upstream header.
- **Default `stats_tags` changed**, affecting `envoy_cluster_*_rq_time_count` and
  `envoy_cluster_*_total_match_count` — the same silent-dashboard failure mode as a renamed metric.

**1.8 — eleven across the line.** The ones that matter most:

- **Gateway API CRDs bumped to v1.5.1**, and the controller now **unconditionally starts an informer
  for ListenerSet** — apply the CRDs as part of the upgrade, and expect the extra watch.
- **`DirectResponse` bodies now support Envoy command operators**: an existing body containing `%`
  is **interpolated** rather than sent literally. Any static body with a percent sign changes
  meaning.
- **`0s` timeout in SecurityPolicy now means infinite**, where it previously meant immediate — an
  inversion, not an adjustment.
- **OIDC is generated as a single native `oauth2` filter** with route-specific configuration moved
  to `typed_per_filter_config`; merged SecurityPolicy resource names now derive from the
  contributing policy.
- **1.8.2** tightens `SecurityPolicy` `apiKeyAuth.extractFrom` admission validation and changes
  `XRateLimitHeadersOptionDisabled` from `"Disabled"` to `"Off"`.
- **1.8.3** moves `EnvoyExtensionPolicy` Lua from per-route overrides to listener-level filters,
  changing the generated xDS.

**`EnvoyPatchPolicy` is the thing most likely to break quietly.** It matches generated xDS by name
and position; 1.7 reorders filters, 1.8.0 reshapes OIDC, 1.8.3 relocates Lua. A patch policy that no
longer matches does not error — it simply stops applying.

## Implementation

Order: Gateway API CRDs, then the controller, then confirm the proxy Deployments actually rolled —
the data-plane image ships with the release but old proxy pods keep their image until restarted.

### Impact

The controller restart re-translates every route. On this estate that is the operation already
analysed in [[TROUBLE-ENVOY_GATEWAY_LEADER_LOSS_503]]: a cold cache briefly produces direct-response
503s for backends the controller has not yet loaded. Expect it, and do not read it as damage caused
by the upgrade itself.

### Rollback

Reverting the controller image is straightforward; reverting the **CRDs** is not, so treat the CRD
apply as the point of no return and take the Gateway API objects' backup before it.

## Compatibility

1.6.7 is the end of the 1.6 line and carries every advisory fix available there — including the
critical gRPC-Go bypass — without any of the generated-configuration changes above. That makes the
patch bump and the minor upgrade genuinely independent decisions, and there is no technical reason
to couple them.

## References

- Upstream release notes for 1.7.x and 1.8.x, read 2026-07-31; the full verbatim list is in
  [[TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES]].
- Advisories per line: [[TROUBLE-ENVOY_GATEWAY_KNOWN_CVES]]; add-on:
  [[CONCEPT-ADDON_ENVOY_GATEWAY]].
