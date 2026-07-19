---
id: CONCEPT-ADDON_INGRESS_NGINX
type: concept
title: "ingress-nginx (addon chart 4.12.0) — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.28 <=1.32"
component_version: "1.12.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - ingress-nginx addon
  - ingress-nginx 4.12.0
  - ingressnightmare
tags:
  - addons
  - networking
  - ingress
  - security
sources:
  - type: code
    path: charts/ingress-nginx/Chart.yaml
    url: https://raw.githubusercontent.com/kubernetes/ingress-nginx/helm-chart-4.12.0/charts/ingress-nginx/Chart.yaml
    note: "kubeVersion >=1.21.0-0; appVersion 1.12.0"
  - type: docs
    path: IngressNightmare (CVE-2025-1974)
    url: https://kubernetes.io/blog/2025/03/24/ingress-nginx-cve-2025-1974/
    note: "controller 1.12.0 affected; fixed 1.12.1"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
  - type: see_also
    target: COMPONENT-INGRESS_NGINX
---

# ingress-nginx (addon chart 4.12.0) — addon

## Summary

The owner's independent ingress-nginx install — chart **4.12.0**, controller **1.12.0** —
newer than the Kubespray-managed [[COMPONENT-INGRESS_NGINX]]. **Security-critical:** controller
1.12.0 is affected by **IngressNightmare (CVE-2025-1974, CVSS 9.8, admission RCE)** — upgrade
to chart **4.12.1** / controller 1.12.1 immediately.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]] (overlaps Kubespray's
  ingress-nginx — different, newer chart).

## Implementation

- Chart→app: `ingress-nginx-4.12.0` → controller **1.12.0** (NGINX 1.25.5, Alpine 3.21.0).
  Chart `kubeVersion`: **`>=1.21.0-0`**.

## Configuration

- **Annotation validation on by default** (`--enable-annotation-validation`,
  `annotations-risk-level=High`) — can reject previously-accepted annotations; snippet-using
  Ingresses may break on upgrade.
- **Metrics disabled by default** now (`--enable-metrics` off); metric
  `ingress_upstream_latency_seconds` removed. Lua plugin system, memcached global rate
  limiting and the OTel init-container were removed; PSPs removed from the chart; s390x
  dropped.

## Compatibility

- **Kubernetes range:** controller 1.12.0 → **K8s 1.28–1.32**. **1.33–1.35 are NOT supported**
  by this chart line.
- **CVEs — IngressNightmare (2025), controller 1.12.0 IS affected (pre-patch):**
  **CVE-2025-1974** (9.8, admission RCE), CVE-2025-1097, CVE-2025-1098, CVE-2025-24513,
  CVE-2025-24514. Fixed in **controller 1.12.1 (chart 4.12.1)** and 1.11.5. Upgrade now; in
  the meantime restrict access to the admission webhook endpoint.

## Upstream issues & upgrade notes (mined 2026-07-19)

**⚠ Security — "IngressNightmare" CVE-2025-1974** (critical, unauthenticated RCE via the admission controller; with related CVE-2025-1097/-1098/-24514): fixed in **1.11.5 / 1.12.1**. The pinned **1.12.0 predates the fix** — you must run **≥1.12.1**. Restrict/network-policy the admission webhook.

**Future upgrade context** beyond 1.12.0: chart 4.15 / **controller 1.15.0 dropped v1.12 support** (v1.13+ required).

**Open upstream bugs (as of 2026-07-19):** `proxy-ssl-name`/`proxy-ssl-server-name` ignored unless a TLS secret is also set (#6728); can't use `$`/nginx vars in `permanent-redirect` (#11175); **app-root redirect fires before the HTTPS redirect** when `ssl-redirect` is true (#6340, security); Helm upgrade briefly **drops the LB IP from Ingress status** (label mismatch) (#10475).

## References

- `Chart.yaml`, IngressNightmare advisory + controller-v1.12.0/v1.12.1 release notes (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]]; Kubespray sibling: [[COMPONENT-INGRESS_NGINX]].
