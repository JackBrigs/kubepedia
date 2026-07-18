---
id: CONCEPT-CLOUD_CONTROLLER_MANAGER
type: concept
title: "External cloud-controller-manager (CCM) in Kubespray — the out-of-tree cloud integration"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: confirmed
aliases:
  - cloud-controller-manager
  - external cloud provider kubespray
  - cloud_provider external
  - external_cloud_provider
  - CCM openstack vsphere hcloud oci
  - out-of-tree cloud provider
tags:
  - kubespray
  - cloud-provider
  - concept
sources:
  - type: code
    path: roles/kubernetes-apps/external_cloud_controller
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/kubernetes-apps/external_cloud_controller
    note: "external CCM roles: hcloud, huaweicloud, oci, openstack, vsphere; cloud_provider / external_cloud_provider vars"
  - type: docs
    path: docs/cloud_controllers/
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/docs/cloud_controllers
    note: "openstack.md, vsphere.md — CCM setup"
relations:
  - type: see_also
    target: TROUBLE-K8S_INTREE_CLOUD_PROVIDER_REMOVED
  - type: see_also
    target: CONCEPT-CSI_LAYER
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# External cloud-controller-manager (CCM) in Kubespray — the out-of-tree cloud integration

## Summary

The **cloud-controller-manager (CCM)** is the component that gives a cluster its cloud integration:
node addresses/zones/providerID, `Service type=LoadBalancer` provisioning, and route management. Since
the **in-tree cloud providers were removed** from core Kubernetes across 1.29–1.31
([[TROUBLE-K8S_INTREE_CLOUD_PROVIDER_REMOVED]]), this must run as an **external (out-of-tree) CCM**.
Kubespray deploys the external CCM as a cluster app for a fixed set of clouds; it is **off by default**
(`cloud_provider: ""`).

## Context

- **Two variables:** `cloud_provider` selects the integration mode; `external_cloud_provider` names the
  out-of-tree provider to deploy. For the removed in-tree providers you set the external path (e.g.
  `cloud_provider: external` + the provider), and Kubespray applies the matching
  `roles/kubernetes-apps/external_cloud_controller/<provider>` role.
- **Providers Kubespray ships an external CCM for** (at v2.31.0): **`openstack`**, **`vsphere`**,
  **`hcloud`** (Hetzner), **`oci`** (Oracle Cloud), **`huaweicloud`**. Other clouds (AWS, Azure, GCE)
  use their own upstream CCM/CSI, deployed outside Kubespray's CCM roles.
- **CCM image versions track the cloud provider, not Kubernetes** (per-provider, at v2.31.0):
  OpenStack CCM `v1.35.0`, vSphere CCM `v1.31.0`, Oracle (OCI) CCM `v1.29.0` (Hetzner/Huawei pinned
  separately). These are the provider's own release lines — match the CCM version to your Kubernetes
  minor per the provider's compatibility guidance ([[CONCEPT-KUBERNETES_VERSION_SUPPORT]]).
- **Pairs with a CSI driver:** the CCM handles node/LB/route; **volumes** are the CSI driver's job
  ([[CONCEPT-CSI_LAYER]]). A cloud deploy needs **both** — CCM + the cloud's CSI.

## Implementation notes

- Deploy: set `cloud_provider`/`external_cloud_provider` in inventory; the CCM runs as a DaemonSet/
  Deployment with a cloud-credentials Secret and RBAC (per-provider templates under the role).
- **Migration from in-tree:** install the external CCM **before or with** the upgrade that removes the
  in-tree code, or you get a window with no cloud integration (LoadBalancers Pending, no node zones) —
  see [[TROUBLE-K8S_INTREE_CLOUD_PROVIDER_REMOVED]].
- Nodes must run with `--cloud-provider=external` so the kubelet defers cloud logic to the CCM; a
  leftover in-tree `--cloud-provider=<name>` conflicts.

## References

- `roles/kubernetes-apps/external_cloud_controller/{openstack,vsphere,hcloud,oci,huaweicloud}` and
  `docs/cloud_controllers/` (tag v2.31.0). In-tree removal
  [[TROUBLE-K8S_INTREE_CLOUD_PROVIDER_REMOVED]]; CSI [[CONCEPT-CSI_LAYER]]; version support
  [[CONCEPT-KUBERNETES_VERSION_SUPPORT]].
