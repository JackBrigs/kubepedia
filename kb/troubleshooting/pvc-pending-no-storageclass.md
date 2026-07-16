---
id: TROUBLE-PVC_PENDING_NO_STORAGECLASS
type: troubleshooting
title: "PVC stuck Pending — no provisioner / no default StorageClass"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - pvc pending
  - no default storageclass
  - persistentvolumeclaim pending
  - no persistent volumes available
  - waitforfirstconsumer
  - bare metal storage kubespray
tags:
  - troubleshooting
  - storage
  - csi
  - pvc
sources:
  - type: code
    path: roles/kubernetes-apps/external_provisioner/local_path_provisioner/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/external_provisioner/local_path_provisioner/defaults/main.yml
    note: "local_path_provisioner_enabled/_storage_class/_is_default_storageclass (tag v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-LOCAL_PATH_PROVISIONER
  - type: see_also
    target: CONCEPT-CSI_LAYER
---

# PVC stuck Pending — no provisioner / no default StorageClass

## Summary

A `PersistentVolumeClaim` stays `Pending` when nothing can satisfy it: no matching
`StorageClass`, no default StorageClass for a class-less claim, or no volumes/driver to
provision from. A fresh Kubespray cluster ships **no storage provisioner by default** — so
on bare metal, dynamic provisioning simply doesn't happen until you enable one.

## Problem

`kubectl get pvc` shows `Pending`; the Pod using it stays `Pending`
(`pod has unbound immediate PersistentVolumeClaims`). `kubectl describe pvc` shows
`no persistent volumes available for this claim and no storage class is set`, or a
provisioning error.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. All storage add-ons are **off by default**:
  `local_path_provisioner_enabled: false`, `local_volume_provisioner_enabled: false`, and
  every `*_csi_enabled` flag false ([[CONCEPT-CSI_LAYER]]).
- A PVC with **no `storageClassName`** binds only if a **default** StorageClass exists; a
  PVC naming a class binds only if that class + its provisioner exist.

## Diagnostics

- `kubectl describe pvc <name>` — the Events line states the reason (no class / no
  provisioner / WaitForFirstConsumer).
- `kubectl get storageclass` — is there any class, and is one marked
  `(default)`? None → class-less PVCs can't bind.
- `kubectl -n local-path-storage get pods` (or the CSI driver namespace) — is a
  provisioner actually running?
- `WaitForFirstConsumer` volume-binding mode: the PV is created only once a Pod is
  scheduled — a PVC "Pending" with an unscheduled Pod can be normal until the Pod lands.

## Known Issues

**Fixes:**

- **Simplest on bare metal — local-path-provisioner:** set
  `local_path_provisioner_enabled: true`. It creates the `local-path` StorageClass and,
  with `local_path_provisioner_is_default_storageclass: "true"` (the default), marks it
  **default** — so class-less PVCs start binding. Storage is node-local hostPath under
  `local_path_provisioner_claim_root` (`/opt/local-path-provisioner/`).
- **Real cloud/SAN storage — a CSI driver:** enable the matching `*_csi_enabled`
  (aws-ebs/azure/cinder/gcp-pd/vsphere) and use its StorageClass
  ([[CONCEPT-CSI_LAYER]]).
- **Class mismatch:** make the PVC's `storageClassName` match an existing class, or set a
  default class (`storageclass.kubernetes.io/is-default-class: "true"`).

**Gotchas:**

- **local-path is node-local** (hostPath): a Pod rescheduled to another node does **not**
  see its data — fine for scratch/dev, not for HA stateful workloads. Use real CSI for
  those.
- Only **one** StorageClass should be default; two defaults is ambiguous and rejected.
- `WaitForFirstConsumer` is expected behaviour, not a fault — check the Pod's scheduling
  before assuming the provisioner is broken.

## References

- local-path-provisioner defaults at tag `v2.31.0`. Component:
  [[COMPONENT-LOCAL_PATH_PROVISIONER]]; CSI layer: [[CONCEPT-CSI_LAYER]].
