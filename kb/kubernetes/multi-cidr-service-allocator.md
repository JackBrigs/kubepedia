---
id: CONCEPT-K8S_MULTI_CIDR_SERVICE_ALLOCATOR
type: concept
title: "Multiple Service CIDRs — ServiceCIDR/IPAddress allocation (on 1.31, GA 1.33)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - MultiCIDRServiceAllocator
  - ServiceCIDR object
  - IPAddress object
  - extend service cidr
  - service ip exhaustion
  - DisableAllocatorDualWrite
tags:
  - kubernetes
  - networking
  - apiserver
sources:
  - type: code
    path: keps/sig-network/1880-multiple-service-cidrs
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-network/1880-multiple-service-cidrs
    note: "kep.yaml: alpha 1.27, beta/on-by-default 1.31, stable 1.33"
relations:
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: CONCEPT-KUBE_PROXY
---

# Multiple Service CIDRs — ServiceCIDR/IPAddress allocation (on 1.31, GA 1.33)

## Summary

Service IP allocation moved from an in-memory bitmap fed by the apiserver `--service-cluster-ip-range`
flag to first-class **`ServiceCIDR`** and **`IPAddress`** API objects. `MultiCIDRServiceAllocator` is
**on by default from K8s 1.31** and **GA in 1.33** (Kubespray v2.29.0+). You can now **add Service
CIDRs** to a running cluster (to fix Service-IP exhaustion) without recreating the control plane.

## Context

- Milestone (`keps/sig-network/1880-...` kep.yaml): alpha **1.27**, beta/on **1.31**, stable **1.33**
  (plus `DisableAllocatorDualWrite` completing the transition off the legacy bitmap).
- **What changes:** the flag `--service-cluster-ip-range` still bootstraps the **default**
  `ServiceCIDR`, but additional ranges are added by **creating `ServiceCIDR` objects**; each allocated
  Service IP is an `IPAddress` object. `kubectl get servicecidr` / `kubectl get ipaddress` are new.
- **Operator impact:** (1) **Service-IP exhaustion is now fixable live** — create another `ServiceCIDR`
  instead of a disruptive range change; (2) tooling/monitoring may want to read `ServiceCIDR`/
  `IPAddress`; (3) Kubespray still sets the initial range via `kube_service_addresses` — that becomes
  the default ServiceCIDR. Deleting the default ServiceCIDR is guarded (it holds
  kubernetes.default's IP).

## References

- `keps/sig-network/1880-multiple-service-cidrs` (kep.yaml GA 1.33). Silent changes
  [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]; kube-proxy [[CONCEPT-KUBE_PROXY]].
