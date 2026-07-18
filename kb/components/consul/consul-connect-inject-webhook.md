---
id: TROUBLE-CONSUL_CONNECT_INJECT_WEBHOOK
type: troubleshooting
title: "Consul connect-inject webhook blocks all pod scheduling (failurePolicy: Fail)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.22.7 <=2.0.2"
verified_at: "2026-07-18"
confidence: verified
aliases:
  - consul connect-injector webhook down
  - failed calling webhook connect-injector
  - consul pods stuck pending admission
  - consul failurePolicy Fail
  - consul injector blocks pod creation
tags:
  - consul
  - troubleshooting
  - admission
  - service-mesh
sources:
  - type: code
    path: charts/consul/templates/connect-inject-mutatingwebhookconfiguration.yaml
    url: https://github.com/hashicorp/consul-k8s/blob/v2.0.2/charts/consul/templates/connect-inject-mutatingwebhookconfiguration.yaml
    note: "pods CREATE webhook with failurePolicy from values; objectSelector app NotIn consul; namespaceSelector default exclusions"
  - type: code
    path: charts/consul/values.yaml
    url: https://github.com/hashicorp/consul-k8s/blob/v2.0.2/charts/consul/values.yaml
    note: "connectInject.failurePolicy default 'Fail' (L2836); replicas default 1 (L2419); default namespace exclusions (L2858-2865)"
relations:
  - type: see_also
    target: CONCEPT-CONSUL_ON_K8S
  - type: see_also
    target: TROUBLE-ADMISSION_WEBHOOK_BLOCKING
  - type: see_also
    target: TROUBLE-CONSUL_SERVER_QUORUM
---

# Consul connect-inject webhook blocks all pod scheduling (failurePolicy: Fail)

## Summary

Consul's **connect-inject** installs a **MutatingWebhookConfiguration on pod `CREATE`** with
**`failurePolicy: "Fail"` by default**. If the connect-injector Deployment is down, unready, or
unreachable, the API server can't call the webhook and **rejects every pod creation** in any namespace
not explicitly excluded — a cluster-wide outage from a single mesh component. The default
`connectInject.replicas: 1` makes the injector a single point of failure. (Same class as any failing
admission webhook — see [[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]].)

## Problem

- New pods stuck failing admission: `failed calling webhook ...-connect-injector...` /
  `context deadline exceeded` — cluster-wide, not just mesh namespaces.
- Even system/infra workloads can't be created if their namespace isn't excluded.
- In Kind, `Fail` "may prevent volume provisioner pods from running which can lead to hangs"
  (`values.yaml`@v2.0.2 L2830-2835).

## Context

- Applies to consul-k8s **1.9.x–2.0.x** ([[CONCEPT-CONSUL_ON_K8S]]). The `pods` webhook is the last
  core webhook in `connect-inject-mutatingwebhookconfiguration.yaml`@v2.0.2 with `failurePolicy`
  templated from `connectInject.failurePolicy` — default **`"Fail"`** (`values.yaml`@v2.0.2 L2836).
- **Built-in blast-radius limiters (know these):**
  - `objectSelector` excludes Consul's own pods (`app NotIn consul`) so Consul can still self-heal.
  - `namespaceSelector` **default-excludes** `kube-system`, `local-path-storage`, `openebs`,
    `gmp-system`, `gke-managed-cim`, and namespaces labeled `openshift.io/cluster-monitoring`
    (`values.yaml`@v2.0.2 L2858-2865). **Any workload namespace NOT on that list is exposed.**
  - The OpenShift-monitoring exclusion was only added in **2.0.2** — on earlier charts those pods
    could be caught.

## Diagnostics

- `kubectl get deploy <release>-connect-injector` — replicas ready? (default 1 → single point).
- `kubectl -n <ns> describe pod <pending>` → the `failed calling webhook` message names the injector.
- `kubectl get mutatingwebhookconfiguration <release>-connect-injector -o yaml` → confirm
  `failurePolicy: Fail` and which namespaces the `namespaceSelector` excludes.
- Check the injector's own health/certs — a stale `caBundle` from a broken `webhook-cert-manager` also
  fails the call (TLS), not just a dead Deployment.

## Known Issues

- **Fix (availability):** raise `connectInject.replicas` (>1) and keep
  `connectInject.disruptionBudget.enabled: true` (auto `maxUnavailable = (n/2)-1`) so the injector
  survives node loss (`values.yaml`@v2.0.2 L2419/L2450-2461).
- **Fix (scope):** exclude infra namespaces via `namespaceSelector` / `k8sDenyNamespaces` so a webhook
  outage can't block system workloads.
- **Fix (trade-off):** set `connectInject.failurePolicy: "Ignore"` where **availability > guaranteed
  injection** (pods schedule even if the injector is down; some may miss the sidecar) — recommended
  for Kind and often for prod resilience.
- **Recover from an outage now:** delete/patch the MutatingWebhookConfiguration (or flip it to
  `Ignore`) to unblock pod creation, fix the injector, then restore.

## References

- consul-k8s `connect-inject-mutatingwebhookconfiguration.yaml` + `values.yaml` (@v2.0.2). Overview
  [[CONCEPT-CONSUL_ON_K8S]]; generic webhook block [[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]]; the quorum
  cascade that also kills the injector path [[TROUBLE-CONSUL_SERVER_QUORUM]].
