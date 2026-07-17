---
id: TROUBLE-ADMISSION_WEBHOOK_BLOCKING
type: troubleshooting
title: "Admission webhook blocks all creates/updates (failed calling webhook)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - failed calling webhook
  - admission webhook denied
  - context deadline exceeded webhook
  - webhook connection refused
  - internal error occurred admission
  - mutatingwebhookconfiguration blocking
  - validatingwebhookconfiguration failurePolicy
tags:
  - troubleshooting
  - admission
  - webhook
  - api
sources:
  - type: docs
    path: Kubernetes admission webhooks
    url: https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/
    note: "failurePolicy Fail blocks matching create/update when the webhook backend is unreachable"
relations:
  - type: see_also
    target: TROUBLE-NAMESPACE_STUCK_TERMINATING
  - type: see_also
    target: COMPONENT-CERT_MANAGER
  - type: see_also
    target: CONCEPT-TROUBLESHOOTING_MAP
---

# Admission webhook blocks all creates/updates (failed calling webhook)

## Summary

A validating/mutating **admission webhook** intercepts create/update requests for the
resources it matches. If its backend service is **unreachable** and its `failurePolicy` is
**`Fail`** (the default), the apiserver **rejects every matching request** —
`Internal error occurred: failed calling webhook …`. A dead webhook can freeze deploys,
scaling, even node/pod operations cluster-wide until you fix or remove it.

## Problem

`kubectl apply`/`create`/`scale` (or the controllers doing it) fail with
`Internal error occurred: failed calling webhook "<name>": … context deadline exceeded` /
`connection refused` / `x509`, sometimes for unrelated resources.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Webhooks come from add-ons you install
  (cert-manager, ingress admission, Kyverno/OPA, service meshes) — not from Kubespray core.
- Each `ValidatingWebhookConfiguration`/`MutatingWebhookConfiguration` has `rules` (which
  resources/verbs it intercepts), a `clientConfig` (the backend Service + `caBundle`), a
  `failurePolicy` (`Fail`/`Ignore`), a `timeoutSeconds`, and a `namespaceSelector`.

## Diagnostics

- **Read the error** — it names the exact webhook (`failed calling webhook "<name>"`).
- **Find its config:** `kubectl get validatingwebhookconfigurations,mutatingwebhookconfigurations`
  then `-o yaml <name>` — see `service`, `failurePolicy`, `rules`, `namespaceSelector`.
- **Backend health:** `kubectl -n <webhook-ns> get pods,svc` — is the webhook's Deployment
  Running and its Service reachable on the configured port?
- **Cert:** `x509` means the `caBundle` doesn't match the webhook's serving cert
  (cert-manager rotated it, or a stale bundle) — [[COMPONENT-CERT_MANAGER]].
- **Scope:** `rules` + `namespaceSelector` tell you *what* it blocks — a webhook matching
  `*` on all namespaces is why "unrelated" things fail.

## Known Issues

Fix the **cause**, then restore protection:

- **Webhook backend down** — restart/repair its Deployment; the webhook recovers once the
  Service answers. This is the usual case after a bad rollout or node drain that took the
  webhook's only replica.
- **Bad `caBundle` / `x509`** — refresh the CA bundle (cert-manager `ca-injector` normally
  does this; if it's stalled, reconcile it).
- **Blocking during outage — emergency unblock:** temporarily set `failurePolicy: Ignore`,
  or **delete** the `*WebhookConfiguration` (it's re-created when the add-on redeploys) to
  stop the bleeding. **Re-enable** it after — running with it disabled removes the
  policy/mutation it enforced.
- **Self-deadlock** — a webhook whose own backend can't schedule because *its* webhook
  blocks it; break the loop by exempting the webhook's namespace
  (`namespaceSelector`/`objectSelector`) or the `kube-system` namespace.

**Gotchas:**

- A webhook matching core resources (pods, namespaces) can even **block namespace
  deletion** or node operations — related to [[TROUBLE-NAMESPACE_STUCK_TERMINATING]].
- `failurePolicy: Fail` is safer for policy correctness but turns the webhook into a
  **single point of failure**; run webhook backends HA and exempt system namespaces.
- Kubespray doesn't install these — the offending webhook is from an add-on you deployed;
  fix it there.

## References

- Kubernetes admission webhooks reference. cert-manager (webhook certs):
  [[COMPONENT-CERT_MANAGER]]; namespace GC: [[TROUBLE-NAMESPACE_STUCK_TERMINATING]].
