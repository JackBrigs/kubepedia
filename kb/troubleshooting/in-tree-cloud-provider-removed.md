---
id: TROUBLE-K8S_INTREE_CLOUD_PROVIDER_REMOVED
type: troubleshooting
title: "Cloud LoadBalancers/node-init stop working — in-tree cloud providers removed, need external CCM"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - in-tree cloud provider removed
  - external cloud-controller-manager required
  - DisableCloudProviders
  - cloud-provider external
  - loadbalancer pending no cloud provider
tags:
  - kubernetes
  - troubleshooting
  - cloud-provider
  - upgrade
sources:
  - type: code
    path: keps/sig-cloud-provider/2395-removing-in-tree-cloud-providers
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-cloud-provider/2395-removing-in-tree-cloud-providers
    note: "kep.yaml: in-tree cloud provider code removal completing across 1.29–1.31; DisableCloudProviders / DisableKubeletCloudCredentialProviders"
relations:
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# Cloud LoadBalancers/node-init stop working — in-tree cloud providers removed, need external CCM

## Summary

Kubernetes finished removing the **in-tree cloud providers** (AWS, Azure, GCE, vSphere, OpenStack) from
the core binaries across **1.29–1.31**. Clusters that still relied on `--cloud-provider=<name>` built
into kube-apiserver/kubelet/controller-manager lose cloud integration — **Service type=LoadBalancer
stays Pending**, node addresses/zones aren't populated, and cloud volumes may not attach — unless an
**external cloud-controller-manager (CCM)** and the matching **CSI driver** are installed.

## Problem

- After upgrading across this range, `Service type=LoadBalancer` sits `<pending>`; nodes lack
  `topology.kubernetes.io/zone` / provider IDs; cloud disks fail to attach.
- kube-controller-manager / kubelet logs show the in-tree cloud provider is gone / `--cloud-provider`
  external expected.

## Context

- Milestone (`keps/sig-cloud-provider/2395-...` kep.yaml): in-tree provider code removal completes
  across **1.29–1.31** (`DisableCloudProviders`, `DisableKubeletCloudCredentialProviders`). The
  external CCM model has been the path for years; this range is when the in-tree fallback disappears.
- **Kubespray context:** Kubespray already deploys **external cloud providers** (external CCM + CSI) for
  the supported clouds via `cloud_provider: external` and the per-cloud roles — a standard Kubespray
  cloud deploy is **already** on the external model. The risk is a cluster pinned to the **legacy
  in-tree** setting or a hand-rolled inventory.

## Diagnostics

- Check the setting: on control-plane, look for `--cloud-provider=<name>` (in-tree) vs
  `--cloud-provider=external` on apiserver/kubelet/controller-manager static pods / config.
- Confirm the external CCM runs: `kubectl -n kube-system get pods | grep cloud-controller-manager`, and
  the cloud CSI driver is installed.
- `kubectl get nodes -o wide` — missing provider IDs / zones indicate no working cloud provider.

## Known Issues

- **Fix:** switch to `cloud_provider: external`, deploy the **external CCM** and **CSI driver** for your
  cloud (Kubespray has roles/vars for the supported clouds), and remove the in-tree `--cloud-provider=<name>`.
- **Migration order:** install the external CCM/CSI **before or with** the upgrade that removes the
  in-tree code, or you get a window with no cloud integration.
- Verify per Kubernetes version which providers were fully removed at which minor
  ([[CONCEPT-KUBERNETES_VERSION_SUPPORT]], [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]).

## References

- `keps/sig-cloud-provider/2395-removing-in-tree-cloud-providers` (kep.yaml). Version support
  [[CONCEPT-KUBERNETES_VERSION_SUPPORT]]; silent changes [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]].
