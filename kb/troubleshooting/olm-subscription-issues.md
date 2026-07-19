---
id: TROUBLE-OLM_SUBSCRIPTION
type: troubleshooting
title: "OLM: Subscription/CSV stuck — CatalogSource unhealthy, InstallPlan needs approval, OperatorGroup"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=0.32.0"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - olm subscription stuck
  - csv pending
  - installplan requires approval
  - catalogsource connecting
  - operatorgroup missing
  - olm operator not installing
tags:
  - troubleshooting
  - operators
  - olm
  - lifecycle
sources:
  - type: external
    path: OLM troubleshooting
    url: https://github.com/operator-framework/operator-lifecycle-manager/blob/v0.32.0/doc/design/architecture.md
    note: "CatalogSource -> Subscription -> InstallPlan (approval) -> CSV; OperatorGroup scopes install"
relations:
  - type: see_also
    target: CONCEPT-ADDON_OLM
  - type: see_also
    target: TROUBLE-IMAGE_PULL_RATE_LIMIT
---

# OLM: Subscription/CSV stuck — CatalogSource unhealthy, InstallPlan needs approval, OperatorGroup

## Summary

An OLM-installed operator stalls somewhere on the **CatalogSource → Subscription → InstallPlan → CSV** chain: an unhealthy catalog registry pod, an InstallPlan awaiting **manual approval**, a missing/duplicate **OperatorGroup**, or a CSV blocked on an unmet dependency. Each hop has a distinct fix.

## Problem

- An operator installed via OLM never becomes ready: the `Subscription` shows no `installedCSV`, the
  `CSV` is stuck `Pending`/`InstallReady`, or `kubectl get installplan` shows one waiting.

## Context

- OLM v0 `0.32.0` ([[CONCEPT-ADDON_OLM]]): install flows **CatalogSource → Subscription → InstallPlan →
  CSV**. A stall at any hop blocks the operator.
- **CatalogSource unhealthy:** the catalog is served by a registry **pod**; if it's `ImagePullBackOff`
  (air-gap/rate limit — [[TROUBLE-IMAGE_PULL_RATE_LIMIT]]) or crashing, the Subscription has no source
  to resolve from (`connecting`/`LastObservedState: TRANSIENT_FAILURE`).
- **InstallPlan approval:** a Subscription with `installPlanApproval: Manual` creates an InstallPlan
  that **waits for approval** — nothing installs until you approve it. Easy to miss.
- **OperatorGroup:** the target namespace needs exactly **one** OperatorGroup matching the operator's
  install mode (OwnNamespace/SingleNamespace/AllNamespaces). Missing or **multiple** OperatorGroups →
  the CSV errors (`csv created in namespace with multiple operatorgroups`).
- **CSV dependency/conflict:** an unmet required API/dependency or a conflicting existing CRD leaves the
  CSV `Pending`.

## Diagnostics

```bash
kubectl get catalogsource -A ; kubectl -n olm get pods | grep catalog     # registry pod healthy?
kubectl get subscription -A -o wide                                        # installedCSV / state
kubectl get installplan -A                                                 # APPROVED false = waiting
kubectl get csv -A ; kubectl describe csv <csv> -n <ns>                    # phase + reason
kubectl get operatorgroup -A
```

## Known Issues

- **CatalogSource — fix:** get the registry pod running (mirror the catalog image for air-gap); the
  Subscription re-resolves once the source is `READY`.
- **Manual approval — fix:** `kubectl patch installplan <ip> -n <ns> --type merge -p
  '{"spec":{"approved":true}}'` (or set `installPlanApproval: Automatic`).
- **OperatorGroup — fix:** create a single OperatorGroup with the right target namespaces; remove
  duplicates.
- **CSV Pending — fix:** `describe csv` for the unmet requirement/conflict; install the dependency or
  resolve the CRD conflict.

## References

- OLM v0.32.0 architecture. Addon [[CONCEPT-ADDON_OLM]]; pull failures [[TROUBLE-IMAGE_PULL_RATE_LIMIT]].
