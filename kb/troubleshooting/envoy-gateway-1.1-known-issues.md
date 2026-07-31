---
id: TROUBLE-ENVOY_GATEWAY_1_1_KNOWN_ISSUES
type: troubleshooting
title: "Envoy Gateway 1.1: every defect fixed in the 1.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.1.0 <1.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - envoy gateway 1.1 known issues
  - envoy gateway 1.1 bugs
  - envoy gateway 1.1 fixed in
tags:
  - troubleshooting
  - envoy
  - gateway-api
  - upgrade
sources:
  - type: code
    path: envoyproxy/gateway release-notes/v1.1.*.yaml — "bug fixes" sections
    url: https://github.com/envoyproxy/gateway/tree/main/release-notes
    note: "5 releases on this line, 15 declared fixes"
relations:
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_KNOWN_CVES
  - type: see_also
    target: TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_GATEWAY
---

# Envoy Gateway 1.1: every defect fixed in the 1.1 line

## Summary

The **1.1** maintenance line published **5 releases** carrying **15 defect fixes**,
0 breaking changes and 0 security updates.
Running anything below **1.1.4** on this line means carrying the remainder of the list
below.

Use this page the way a defect database is used: before filing "Envoy Gateway does X wrong", search
here — the odds are it is already named, with the exact patch that fixes it.

## Problem

Defects are grouped by the release that fixed them; a cluster on version *N* carries everything
listed under versions greater than *N*.

## Context

### v1.1.3 — 9

- Fixed unsupported listener protocol type causing an error while updating Gateway Status
- Fixed some status updates were being discarded by the status updater
- Fixed error level logging for admin and metrics modules
- Fixed Dashboard typos
- Fixed Ratelimit Deployment ignoring pod labels and annotation merge
- Fixed the API Server receives unnecessary requests
- Fixed set invalid Listener.SupportedKinds to empty list
- Fixed losing timeout settings that originate from the route when translating the backend traffic policy
- Fixed xds translation failure when wasm http code source configured without sha

### v1.1.4 — 6

- Fixed validate proto messages before converting them to anypb.Any
- Fixed BackendTlsPolicy specify multiple targetRefs of the same service, only one will work
- Fixed Envoy rejecting TCP Listeners that have no attached TCPRoutes
- Fixed frequent 503 errors when connecting to a Service experiencing high Pod churn
- Fixed reference grant from EnvoyExtensionPolicy to referenced ext-proc backend not respected
- Fixed BackendTrafficPolicy not applying to Gateway Route when Route has a Request Timeout defined

## Diagnostics

```bash
kubectl -n <eg-ns> get deploy envoy-gateway \
  -o jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
```

Compare against **1.1.4** — the newest release of this line.

## Known Issues

Upgrading inside a maintenance line is the low-risk move, but this project ships behaviour changes
in patch releases as well; the full list is in [[TROUBLE-ENVOY_GATEWAY_BREAKING_CHANGES]] and the
security exposure in [[TROUBLE-ENVOY_GATEWAY_KNOWN_CVES]].

## References

- Upstream `release-notes/v1.1.*.yaml`, `bug fixes` sections, read at `origin/main` on 2026-07-31.
- Add-on: [[CONCEPT-ADDON_ENVOY_GATEWAY]].
