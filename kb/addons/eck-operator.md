---
id: CONCEPT-ADDON_ECK_OPERATOR
type: concept
title: "Elastic ECK Operator — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.33"
component_version: "3.1.0"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - eck-operator
  - elastic cloud on kubernetes
  - elastic
tags:
  - addons
  - data
  - elastic
sources:
  - type: code
    path: deploy/eck-operator/Chart.yaml
    url: https://raw.githubusercontent.com/elastic/cloud-on-k8s/v3.1.0/deploy/eck-operator/Chart.yaml
    note: "kubeVersion >=1.21.0-0; appVersion 3.1.0"
  - type: docs
    path: ECK v3.1.0 README (supported versions)
    url: https://raw.githubusercontent.com/elastic/cloud-on-k8s/v3.1.0/README.md
    note: "K8s 1.29–1.33, OpenShift 4.15–4.19"
relations:
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# Elastic ECK Operator — addon

## Summary

ECK (Elastic Cloud on Kubernetes) orchestrates Elasticsearch, Kibana, APM, Beats, Agent,
Logstash and Enterprise Search. Chart/app **3.1.0**, supporting Kubernetes **1.29–1.33**.
The operator **orchestrates** the Elastic Stack — it does not bundle a fixed Stack version.

## Context

- Class: upstream addon; catalog row in [[CONCEPT-ADDON_CATALOG]].

## Implementation

- Chart→app: `eck-operator` 3.1.0. Chart `kubeVersion`: **`>=1.21.0-0`** (looser than the
  README's tested range).
- Managed Stack per README: Elasticsearch/Kibana/APM/Beats/Agent/Maps 7.17+/8+/9+,
  Logstash 8.12+/9+, Enterprise Search 7.7+/8+.

## Configuration

- Pin Elastic Stack versions per CR; mind the operator↔Stack ordering rules (below) before
  bumping major Stack versions.

## Compatibility

- **Kubernetes range:** **1.29–1.33** (ECK v3.1.0 README), OpenShift 4.15–4.19.
- **Upgrade ordering:** ECK 3.0.0 removed support for Elastic Stack 6.x; Stack **9.0.0
  requires ECK ≥3.0.0**; **Enterprise Search cannot upgrade to Stack 9.0.0** (no 9.x image) —
  migrate/delete it before upgrading. **No breaking changes for ECK 3.1** specifically (3.1.0
  adds metadata propagation to child resources; UBI base image minimal→micro).
- **CVEs:** none affecting the 3.x operator (only historic CVE-2020-7010, fixed ECK 1.1.0).

## Upstream issues & upgrade notes (mined 2026-07-19)

**Future upgrade context** beyond pinned **3.1.0** (from upstream releases):
- **⚠ 3.3.0 breaking:** **Elasticsearch 6.x support removed** and **Stack 7.17 support ended** — verify your managed stacks aren't on those before upgrading the operator.
- **3.4.0 upgrade note:** upgrades to **Elasticsearch 9.0 must go through 8.18** (no direct jump); adds client-cert auth, rolling restart, cosign image signing.

**Open upstream bugs (as of 2026-07-19):** `is_managed` doesn't correctly update agent policies (#8709); **ECK gets `401 Unauthorized` setting up Fleet Server** via Kibana API (#6144); ES-9.0 log-autodiscovery annotation issue (#8680).

## Older-version CVEs & security history (mined 2026-07-19)

The ECK GitHub advisories endpoint was not retrievable in this pass (rate-limited); Elastic tracks CVEs on the **Elastic Security site**. The dominant older-version exposure is **not the ECK operator code** but the **Elasticsearch/Kibana Stack version** it manages — older managed stacks (e.g. 7.17 / 8.x below current) carry their own CVEs. Keep both the operator and the managed Stack patched, and remember 3.3.0 removed ES 6.x / Stack 7.17 support.

## Guides & how-to (official)

- **Upgrade ECK:** https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-upgrading-eck.html ; **upgrade the Stack:** https://www.elastic.co/guide/en/cloud-on-k8s/current/k8s-upgrading-stack.html
- **How to upgrade:** upgrade the **operator** first, then managed Stacks (rolling, orchestrated by ECK). **3.3 removed ES 6.x / Stack 7.17**; **ES 9.0 must go through 8.18** — plan the Stack path accordingly.
## References

- `Chart.yaml`, ECK 3.1.0 README, Elastic release/breaking-changes notes (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
