---
id: PRACTICE-CERTIFICATE_EXPIRY
type: best_practice
title: Certificate expiry and rotation (day-2 runbook)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-21"
confidence: verified
aliases:
  - certificate expiry
  - cert rotation
  - x509 expired
  - auto_renew_certificates downtime
  - does cert renewal restart the control plane
tags:
  - operations
  - certificates
  - diagnostics
sources:
  - type: code
    path: roles/etcd/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd/tasks/main.yml
    note: "etcd cert tasks (etcd-secrets); kubeadm manages control-plane certs"
  - type: code
    path: roles/etcd/handlers/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd/handlers/main.yml
    note: "'Restart etcd' throttles to groups['etcd']|length // 2 to keep quorum; 'Wait for etcd up' polls /health — the etcd disruption profile"
  - type: code
    path: roles/kubernetes/control-plane/templates/k8s-certs-renew.sh.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/templates/k8s-certs-renew.sh.j2
    note: "auto-renew script: 7-day buffer check, kubeadm certs renew all, crictl rmp -f of apiserver/CM/scheduler/etcd sandboxes, waits for :6443, rewrites /root/.kube/config"
  - type: code
    path: roles/kubernetes/control-plane/tasks/kubeadm-setup.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/tasks/kubeadm-setup.yml
    note: "cluster.yml only regenerates apiserver.crt when a SAN stops matching — it is not a blanket renewal"
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "auto_renew_certificates: false, auto_renew_certificates_systemd_calendar 'Mon *-*-1,2,3,4,5,6,7 03:00:00', kubeadm_upgrade_auto_cert_renewal: true (L237-244)"
  - type: code
    path: playbooks/cluster.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "the kube_control_plane play has no serial (parallel), unlike upgrade_cluster.yml which uses serial: 1"
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

**What a Kubespray run actually renews** (this is narrower than it looks):

- A plain `cluster.yml` run does **not** blanket-renew control-plane certs. It checks
  the apiserver cert SANs (`openssl x509 -checkip/-checkhost` per SAN) and only if a SAN
  no longer matches does it delete `apiserver.crt/.key` and re-run
  `kubeadm init phase certs apiserver`
  (`roles/kubernetes/control-plane/tasks/kubeadm-setup.yml`).
- `upgrade-cluster.yml` **does** renew everything: kubeadm renews all certificates during
  the control-plane upgrade, and `kubeadm_upgrade_auto_cert_renewal` (default `true`) is
  the opt-out.
- `auto_renew_certificates` (default **`false`**) installs `k8s-certs-renew.sh` plus a
  systemd timer (`auto_renew_certificates_systemd_calendar`, default
  `Mon *-*-1,2,3,4,5,6,7 03:00:00` — first Monday of each month at 03:00). The script
  renews only if some cert expires within the next timer elapse + 7 days, then
  force-removes the control-plane pod sandboxes and waits for the API port again.

**Renew etcd certs:** run the etcd cert path via the `etcd-secrets` tag (see
[[TAG-ETCD_SECRETS]]) — in AWX, job tags `etcd-secrets` on `cluster.yml`. Note it
generates missing/changed certs; to force rotation, invalidate the existing cert
files first. A cert change triggers an etcd restart in a full run.

**kubelet:** client cert rotation is automatic; for serving-cert rotation see
[[VARIABLE-KUBELET_ROTATE_SERVER_CERTIFICATES]] (needs a CSR approver).

## Service impact

Certificate work spans the whole range from free to a control-plane outage:

- **Checking is free.** `kubeadm certs check-expiration` and the `openssl` commands above
  are read-only — run them on production at any time.
- **`kubeadm certs renew all` by itself is not disruptive** — it rewrites the files on
  disk. The running apiserver/controller-manager/scheduler keep serving the **old** certs
  until their static pods restart, so nothing changes (and nothing is fixed) until you
  restart them.
- **The restart is the outage.** Removing the control-plane pod sandboxes drops the API
  server on that node: `kubectl` fails against it, controllers and the scheduler
  re-elect, and new pods are not scheduled while no apiserver is up. **Running workloads
  keep running** — kubelet and CNI are untouched — so this is an API-plane outage, not a
  data-plane one. With an HA control plane behind a load balancer, restart **one node at
  a time** and the API stays available; on a single control-plane node it is a hard,
  minutes-long API outage.
- **`auto_renew_certificates` is the sharp edge.** The systemd timer fires on **every**
  control-plane node at the *same* calendar moment, and the script force-removes the
  apiserver, controller-manager, scheduler **and etcd** sandboxes
  (`crictl rmp -f`) before waiting for `127.0.0.1:6443`. There is no staggering across
  nodes — with an unlucky calendar all control-plane nodes bounce together. It also
  overwrites `/root/.kube/config` from `admin.conf`.
- **etcd cert rotation is rolling and quorum-safe by design.** The `Restart etcd` handler
  runs with `throttle: {{ groups['etcd'] | length // 2 }}` — the source comment states
  this keeps a majority up — and a `Wait for etcd up` step polls `/health` (60 retries)
  before moving on. Expect brief per-member unavailability, not a cluster outage. Do not
  bypass it with a manual parallel restart.
- **Beware the play topology.** In `cluster.yml` the control-plane play has **no
  `serial`**, so all control-plane nodes are processed in parallel and any handler-driven
  apiserver restart fires everywhere at once; `upgrade_cluster.yml` uses `serial: 1` for
  the control plane. If you need certificate work with one-node-at-a-time behaviour, use
  the upgrade path or limit the run to a single host.
- **Backout:** back up `/etc/kubernetes/pki` (and the etcd cert dir) before renewing —
  restoring the old files plus a restart is the only quick way back, and it only helps
  while the old certs are still valid.

## References

- `kubeadm certs check-expiration` / `renew` (standard kubeadm).
- `roles/etcd/tasks/main.yml` + `roles/etcd/handlers/main.yml` (`etcd-secrets`, quorum-safe
  throttle); `roles/kubernetes/control-plane/templates/k8s-certs-renew.sh.j2` and
  `defaults/main/main.yml` L237-244 (`auto_renew_certificates`,
  `kubeadm_upgrade_auto_cert_renewal`); `tasks/kubeadm-setup.yml` (SAN-triggered apiserver
  cert regeneration only); `playbooks/cluster.yml` (no `serial` on the control-plane play).
