---
id: PRACTICE-RUNBOOK_CERT_ROTATION
type: best_practice
title: "Runbook: rotate / renew cluster certificates"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - certificate rotation runbook
  - renew certificates kubernetes
  - kubeadm certs renew all
  - k8s-certs-renew
  - expired apiserver certificate
  - rotate etcd certs
tags:
  - runbook
  - operations
  - certificates
  - security
sources:
  - type: docs
    path: docs/operations/upgrades.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/upgrades.md
    note: "cluster runs renew control-plane certs; k8s-certs-renew.sh runs kubeadm certs renew all"
  - type: external
    path: kubeadm certs
    url: https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-certs/
    note: "kubeadm certs check-expiration / renew all; CP certs 1y, CA 10y; static pods not auto-restarted"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: depends_on
    target: PRACTICE-CERTIFICATE_EXPIRY
  - type: see_also
    target: TROUBLE-KUBEADM_CERT_RENEWAL
  - type: see_also
    target: TROUBLE-K8S_CERTS_RENEW_BROKEN_SCRIPT
  - type: see_also
    target: CONCEPT-CLUSTER_PKI
  - type: see_also
    target: TAG-ETCD_SECRETS
---

# Runbook: rotate / renew cluster certificates

## Summary

Kubernetes control-plane certificates default to **1-year** validity (the CA is 10 years); a cluster
that **never upgrades** silently expires them and `kubectl` stops working. This runbook renews them
in order: check expiry → renew control-plane (kubeadm) → **restart the static pods** (kubeadm does
**not** — the #1 gotcha) → renew etcd certs → verify. Renewal reuses the existing CA, so nodes keep
trusting; see [[PRACTICE-CERTIFICATE_EXPIRY]] for the full inventory and
[[TROUBLE-KUBEADM_CERT_RENEWAL]] for the seam detail.

## Context

- **kubelet client certs auto-rotate** ([[VARIABLE-KUBELET_ROTATE_CERTIFICATES]] `true`) — you rarely
  touch them. **Control-plane and etcd** certs are the ones that need this runbook.
- **Upgrades renew for free:** a normal `cluster.yml` / `upgrade-cluster.yml` run renews CP certs on
  the way — a regularly-upgraded cluster never hits expiry. This runbook is for clusters that sit
  still.
- **CA unchanged:** renewal signs new leaf certs with the **existing** CA, so kubeconfigs and node
  trust keep working. A full **CA** rotation is a different, much larger operation — out of scope
  here.
- **SAN changes** (new API VIP / hostname) are **not** a renewal — you must regenerate with the new
  SAN ([[TROUBLE-APISERVER_CERT_SAN]]). Stable across **v2.27.0–v2.31.0** / K8s 1.29–1.35
  ([[CONCEPT-CLUSTER_PKI]]).

## Implementation

**Step 0 — Check expiry** (on each control-plane node):

```bash
kubeadm certs check-expiration          # every kubeadm-managed cert + expiry
```

**Step 1 — Snapshot etcd first** ([[PRACTICE-ETCD_BACKUP_RESTORE]]) — you're touching PKI on the
control plane.

**Step 2 — Renew control-plane certs**, one control-plane node at a time:

```bash
kubeadm certs renew all                 # what Kubespray's k8s-certs-renew.sh runs
```

**Step 3 — Restart the control-plane static pods** (kubeadm does **not** — without this they keep
serving the OLD cert):

```bash
# move manifests out and back, or:
crictl ps | grep -E 'kube-apiserver|kube-controller|kube-scheduler' | awk '{print $1}' | xargs crictl stop
```

Confirm apiserver is back before moving to the next control-plane node.

**Step 4 — Alternative / bulk path via Kubespray** (renews CP certs across nodes; also the way to do
it at scale):

```bash
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/cluster.yml -b   # renews on a normal run
```

**Step 5 — Renew etcd certs** if they're near expiry ([[TAG-ETCD_SECRETS]]):

```bash
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/cluster.yml -b --tags etcd-secrets
# generates missing/changed certs; to FORCE rotation, invalidate the existing cert files first.
# a cert change triggers an etcd restart in a full run.
```

**Step 6 — Verify:** `kubeadm certs check-expiration` shows fresh dates; apiserver/etcd serve without
`x509: certificate has expired`; `kubectl get nodes` works; `etcdctl endpoint health` green
([[COMPONENT-ETCD]]). If the packaged `k8s-certs-renew` cron/script misbehaves, see
[[TROUBLE-K8S_CERTS_RENEW_BROKEN_SCRIPT]].

**Rollback.** Renewal is additive (new leaves, same CA) and hard to "undo" — but the **old certs are
already expired/replaced**, so forward is the only sane direction. If a control plane won't come back
after renewal, restore the Step 1 snapshot into a rebuilt control plane
([[PRACTICE-RUNBOOK_ETCD_RESTORE]]).

## References

- `kubeadm certs`, `docs/operations/upgrades.md`, `etcd-secrets` tag (tag `v2.31.0`). Inventory
  [[PRACTICE-CERTIFICATE_EXPIRY]]; seam [[TROUBLE-KUBEADM_CERT_RENEWAL]]; PKI
  [[CONCEPT-CLUSTER_PKI]]; index [[CONCEPT-RUNBOOKS_INDEX]].
