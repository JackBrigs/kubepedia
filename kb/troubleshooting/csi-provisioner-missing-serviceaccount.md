---
id: TROUBLE-CSI_PROVISIONER_MISSING_SA
type: troubleshooting
title: "PVC stuck at ExternalProvisioning with no Provisioning event — the CSI controller plugin never started"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "ceph-csi-operator 1.0.4"
verified_at: "2026-08-07"
confidence: verified
aliases:
  - waiting for a volume to be created by external provisioner
  - ExternalProvisioning
  - PVC Pending нет событий Provisioning
  - rook-ceph.rbd.csi.ceph.com не обрабатывает PVC
  - serviceaccount rbd-ctrlplugin-sa not found
  - ctrlplugin forbidden serviceaccount
  - csi provisioner не создаёт том
  - PVC висит Pending ceph-block
tags:
  - rook-ceph
  - ceph-csi
  - storage
  - troubleshooting
  - pvc
  - rbac
sources:
  - type: measurement
    path: кластер lux, namespace rook-ceph, 2026-08-07
    note: "события FailedCreate: serviceaccount rbd-ctrlplugin-sa not found; в кластере есть ceph-csi-rbd-ctrlplugin-sa; ceph HEALTH_OK"
  - type: measurement
    path: deploy/rook-ceph.rbd.csi.ceph.com-ctrlplugin
    note: "serviceAccountName=rbd-ctrlplugin-sa; lastUpdateTime 2026-08-07T10:07:58Z — за час до появления Pending PVC"
  - type: doc
    path: ceph-csi-operator v1.0.4
    note: "оператор рапортует 'controller plugin deployment updated successfully' — он проверяет запись спецификации, а не запуск подов"
relations:
  - type: see_also
    target: CONCEPT-ADDON_ROOK_CEPH
  - type: see_also
    target: TROUBLE-NODE_LOCAL_PVC_DRAIN
---

## Summary

A PVC sits in `Pending` with one repeating event — `ExternalProvisioning: waiting
for a volume to be created by external provisioner` — and nothing else. No
`Provisioning`, no `ProvisioningFailed`. That combination is not a storage failure
and not a permissions failure on the claim: it says the external provisioner never
looked at the claim, because it is not running. The reason is usually a level below
the pods, in the controller that cannot create them at all.

## Problem

The event grammar is the whole diagnosis and it is worth reading precisely:

| event | who emits it | what it means |
|---|---|---|
| `ExternalProvisioning` | kube-controller-manager | "this claim is somebody else's job, still waiting" |
| `Provisioning` | csi-provisioner sidecar | the provisioner has taken the claim |
| `ProvisioningFailed` | csi-provisioner sidecar | the provisioner tried and failed |

Only the first appears when the provisioner is absent, because the other two can
only be written by the process that is missing. So the absence of a failure event is
itself the signal: **nothing failed, because nothing ran**.

This misdirects investigation toward the claim (quota, StorageClass, access mode)
and toward Ceph (health, capacity, pools), where everything is invariably fine.

## Context

Observed with `ceph-csi-operator` v1.0.4 driving Rook-Ceph. The operator generates
the controller-plugin Deployment and node-plugin DaemonSet from `Driver` custom
resources and writes `serviceAccountName` into them. The ServiceAccounts themselves
are created by the Helm chart.

When the two disagree about the name, nothing recovers on its own:

```
Deployment ссылается на:   rbd-ctrlplugin-sa
в кластере существует:     ceph-csi-rbd-ctrlplugin-sa
```

The prefix that the chart applies to its objects was absent from the name the
operator generated. Kubernetes refuses to create the pod:

```
pods "rook-ceph.rbd.csi.ceph.com-ctrlplugin-…" is forbidden:
error looking up service account rook-ceph/rbd-ctrlplugin-sa:
serviceaccount "rbd-ctrlplugin-sa" not found
```

**The failure is silent in the operator's own logs.** It reported `controller plugin
deployment updated successfully` and `CSI Driver reconciliation completed
successfully` in the same reconcile that produced the broken reference — it verifies
that it wrote the spec, not that a pod came up.

**The blast radius is wider than the reported claim.** The same mismatch hit four
workloads at once: RBD and CephFS, controller plugin and node plugin. The controller
plugin provisions volumes; the node plugin mounts them. Already-mounted volumes keep
working because the mount happened earlier, so the cluster looks healthy — but every
pod restart or reschedule that needs a Ceph volume will fail to mount. It is a
cluster-wide storage outage that surfaces gradually.

## Diagnostics

Trace from the claim to the ServiceAccount. A PVC does not use a ServiceAccount —
the provisioner does, and the chain runs through the StorageClass:

```bash
# 1. StorageClass утверждённый в PVC
kubectl -n <ns> get pvc <pvc> -o jsonpath='{.spec.storageClassName}'

# 2. провижионер этого класса
kubectl get sc <class> -o jsonpath='{.provisioner}'

# 3. на какой SA ссылается контроллер драйвера
kubectl -n rook-ceph get deploy <provisioner>-ctrlplugin \
  -o jsonpath='{.spec.template.spec.serviceAccountName}'

# 4. существует ли он
kubectl -n rook-ceph get sa <имя>
```

Confirm the plugin pods are absent rather than crashing, and read the reason — it
sits on the controller, not on a pod, because no pod was ever created:

```bash
kubectl -n rook-ceph get pods | grep -E 'ctrlplugin|nodeplugin'
kubectl -n rook-ceph get events --sort-by=.lastTimestamp | grep FailedCreate
```

Establish scope and timing:

```bash
kubectl get pvc -A | grep Pending
kubectl -n rook-ceph get deploy <provisioner>-ctrlplugin \
  -o jsonpath='{.status.conditions[*].lastUpdateTime}'
```

Rule Ceph out explicitly, because it will be the first suspicion:

```bash
kubectl -n rook-ceph exec deploy/rook-ceph-tools -- ceph -s
```

## Known Issues

**Do not chase the claim.** Quota, access mode, StorageClass existence and Ceph
capacity are all consistent with this failure and all irrelevant to it. The reporter
who says "the StorageClass exists and the quota is not exhausted" is correct and has
already excluded the wrong causes.

**Creating the missing ServiceAccounts by hand restores service but diverges from
the chart.** The next `helm upgrade` can remove them again. The durable fix is to
make the operator generate the names the chart actually creates — which means
finding what changed in the `Driver` resources or the operator version.

**A successful reconcile is not evidence of a working driver.** Any check built on
this operator's logs or on `Driver` status will report health while no plugin pod
exists. Verify pods, not reconciles.

**Node plugin breakage is invisible until something moves.** Because existing mounts
survive, monitoring based on running workloads will not notice. A check that a
DaemonSet has its expected number of ready pods would.

## References

- Events on `daemonset/…-nodeplugin` and `replicaset/…-ctrlplugin` in the driver namespace — the authoritative reason
- `ceph-csi-operator` reconcile logs — useful for timing, not for health
- Kubernetes external-provisioner — emitter of `Provisioning` / `ProvisioningFailed`
- kube-controller-manager — emitter of `ExternalProvisioning`
