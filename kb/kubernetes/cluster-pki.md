---
id: CONCEPT-CLUSTER_PKI
type: concept
title: "Cluster PKI and certificate lifecycle (validity, renewal, rotation)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - certificate lifecycle
  - cluster pki
  - auto_renew_certificates
  - kube_cert_validity_period
  - certificate expiry one year
  - kubeadm certs
tags:
  - certificates
  - pki
  - security
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "auto_renew_certificates, kube_cert_validity_period, kube_ca_cert_validity_period (tag v2.31.0)"
relations:
  - type: see_also
    target: PRACTICE-CERTIFICATE_EXPIRY
  - type: see_also
    target: TROUBLE-APISERVER_CERT_SAN
  - type: see_also
    target: TROUBLE-KUBELET_SERVING_CERT_TLS
---

# Cluster PKI and certificate lifecycle (validity, renewal, rotation)

## Summary

A Kubespray/kubeadm cluster runs on a PKI: a long-lived **CA** signs short-lived
**leaf** certs (apiserver, etcd, kubelet, controller-manager, scheduler). The classic
gotcha: leaf certs default to **1 year** — a cluster left un-upgraded for a year gets
**expired control-plane certs** and stops working. Kubespray can auto-renew on a timer,
but it is **off by default**.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Defaults:
  - `kube_cert_validity_period: 8760h` (**1 year**) — non-CA (leaf) certs.
  - `kube_ca_cert_validity_period: 87600h` (**10 years**) — CA certs.
  - `auto_renew_certificates: false` — enable a systemd timer to renew control-plane certs
    automatically.
  - `auto_renew_certificates_systemd_calendar: "Mon *-*-1,2,3,4,5,6,7 03:00:00"` — the
    renewal schedule (first Monday-ish of each month, 03:00) when auto-renew is on.
  - `kube_cert_dir: {kube_config_dir}/ssl`; `kube_cert_group: kube-cert` (cert file
    ownership).

## Implementation

- **Renewal happens on any Kubespray run**: re-running `cluster.yml`/`upgrade-cluster.yml`
  renews control-plane certs — so clusters upgraded regularly rarely hit expiry. It's the
  **idle** clusters that expire.
- **Enable auto-renew** (`auto_renew_certificates: true`) on clusters you don't touch
  often — the timer renews before the 1-year deadline without a full run.
- **Manual renewal / inspection** and the recovery procedure for already-expired certs are
  in the day-2 runbook [[PRACTICE-CERTIFICATE_EXPIRY]] (`kubeadm certs check-expiration`,
  `kubeadm certs renew`).
- **SANs** are baked into the apiserver cert at generation — adding an endpoint later needs
  a cert regeneration, not just renewal ([[TROUBLE-APISERVER_CERT_SAN]]).
- **kubelet certs** rotate separately: client-cert rotation is on by default
  (`kubelet_rotate_certificates`); serving-cert rotation is opt-in
  ([[TROUBLE-KUBELET_SERVING_CERT_TLS]]).

## Compatibility

- **The 1-year trap:** an idle cluster past `kube_cert_validity_period` shows
  `x509: certificate has expired` on every API call and won't self-heal — you must renew
  (runbook). Prevent it with periodic runs or `auto_renew_certificates`.
- **CA rotation is heavy** (10-year default for a reason): rotating the CA invalidates all
  leaf certs and kubeconfigs — plan it as a major operation, not routine.
- Certificate validity checks assume correct node time — clock skew makes valid certs look
  expired/not-yet-valid ([[TROUBLE-CLOCK_SKEW_TLS]]).
- Extending `kube_cert_validity_period` reduces renewal frequency but widens the window a
  compromised cert stays valid — a security trade-off.

## References

- `auto_renew_certificates` / validity-period defaults at tag `v2.31.0`. Renewal runbook:
  [[PRACTICE-CERTIFICATE_EXPIRY]]; SANs: [[TROUBLE-APISERVER_CERT_SAN]]; kubelet certs:
  [[TROUBLE-KUBELET_SERVING_CERT_TLS]].
