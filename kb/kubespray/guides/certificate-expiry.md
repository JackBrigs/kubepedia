---
id: PRACTICE-CERTIFICATE_EXPIRY
type: best_practice
title: Certificate expiry and rotation (day-2 runbook)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - certificate expiry
  - cert rotation
  - x509 expired
tags:
  - operations
  - certificates
  - diagnostics
sources:
  - type: code
    path: roles/etcd/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd/tasks/main.yml
    note: "etcd cert tasks (etcd-secrets); kubeadm manages control-plane certs"
relations:
  - type: see_also
    target: TAG-ETCD_SECRETS
  - type: see_also
    target: VARIABLE-KUBELET_ROTATE_CERTIFICATES
---

# Certificate expiry and rotation (day-2 runbook)

## Summary

Kubernetes/Kubespray clusters use several certificate sets: kubeadm-managed
control-plane certs, etcd peer/server/client certs, and the kubelet client cert.
Expired certs cause `x509: certificate has expired` and API/kubelet failures. This
runbook covers checking expiry and renewing.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- kubelet **client** cert auto-rotates by default
  ([[VARIABLE-KUBELET_ROTATE_CERTIFICATES]] `true`); control-plane and etcd certs
  are longer-lived and renewed via kubeadm / the etcd role.

## Diagnostics

**Control-plane certs (on a control-plane node):**

```bash
kubeadm certs check-expiration          # table of all kubeadm-managed certs + expiry
openssl x509 -enddate -noout -in /etc/kubernetes/pki/apiserver.crt
```

**etcd certs:**

```bash
# host deployment (default etcd_deployment_type): certs under the etcd cert dir
ls -l /etc/ssl/etcd/ssl/ 2>/dev/null || ls -l /etc/kubernetes/pki/etcd/
openssl x509 -enddate -noout -in /etc/ssl/etcd/ssl/member-$(hostname).pem
```

**kubelet cert:**

```bash
openssl x509 -enddate -noout -in /var/lib/kubelet/pki/kubelet-client-current.pem
```

## Implementation

**Renew control-plane certs (kubeadm):**

```bash
kubeadm certs renew all        # renew, then restart the static-pod control plane
# static pods restart by moving manifests, or reboot the node in a rolling manner
```

Kubespray also renews control-plane certs on a normal `cluster.yml` /
`upgrade-cluster.yml` run.

**Renew etcd certs:** run the etcd cert path via the `etcd-secrets` tag (see
[[TAG-ETCD_SECRETS]]): `ansible-playbook cluster.yml --tags etcd-secrets`. Note it
generates missing/changed certs; to force rotation, invalidate the existing cert
files first. A cert change triggers an etcd restart in a full run.

**kubelet:** client cert rotation is automatic; for serving-cert rotation see
[[VARIABLE-KUBELET_ROTATE_SERVER_CERTIFICATES]] (needs a CSR approver).

## References

- `kubeadm certs check-expiration` / `renew` (standard kubeadm).
- `roles/etcd/tasks/main.yml` (`etcd-secrets`); Kubespray renews certs on cluster
  runs.
