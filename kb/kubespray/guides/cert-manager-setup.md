---
id: PRACTICE-CERT_MANAGER_SETUP
type: best_practice
title: "cert-manager: enabling and CA setup"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-21"
confidence: verified
aliases:
  - cert-manager-setup
  - cert_manager_enabled
  - kubespray deletes cert-manager namespace
  - ca-key-pair secret kubespray
  - cert-manager version kubespray
tags:
  - operations
  - cert-manager
sources:
  - type: docs
    path: docs/advanced/cert_manager.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/advanced/cert_manager.md
    note: "digest of the tag doc"
  - type: code
    path: roles/kubernetes-apps/ingress_controller/cert_manager/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ingress_controller/cert_manager/tasks/main.yml
    note: "tasks tagged 'upgrade' delete the addon dir and run 'kubectl delete namespace {{ cert_manager_namespace }}' before re-applying vendored manifests with the kube module (state: latest)"
  - type: code
    path: roles/kubernetes-apps/ingress_controller/cert_manager/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ingress_controller/cert_manager/defaults/main.yml
    note: "namespace, user 1001, tolerations/affinity/nodeselector, proxy vars, leader election namespace kube-system"
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "cert_manager_version is a static pin 1.15.3, unchanged across v2.27.0-v2.31.0"
relations:
  - type: see_also
    target: CONCEPT-SECURITY_ADVISORIES
  - type: see_also
    target: CONCEPT-DESTRUCTIVE_ACTIONS
---

# cert-manager: enabling and CA setup

## Summary

cert-manager is a native Kubernetes certificate controller (issues/renews certs from Let's Encrypt, Vault, a CA key pair, or self-signed). Kubespray deploys it when `cert_manager_enabled: true`.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`; cert-manager version per [[COMPONENT-CERT_MANAGER]] context (see the addons).
- Opt-in add-on.

## Implementation

Enable in the addons inventory (`k8s_cluster/addons.yml`): `cert_manager_enabled: true`
(default `false`). To issue TLS from your own CA, create the `ca-key-pair` Secret (Root CA
cert + key) in the cluster; then configure Issuers/ClusterIssuers. For public certs, use a
Let's Encrypt ClusterIssuer. See the upstream cert-manager CA configuration docs.

**How Kubespray deploys it** (`roles/kubernetes-apps/ingress_controller/cert_manager`,
verified at v2.31.0):

- The role is a dependency of `kubernetes-apps/ingress_controller` and runs only `when:
  cert_manager_enabled`. AWX: job tag `cert-manager` (also covered by `ingress-controller`
  and `apps`).
- The manifests are **vendored Jinja templates in Kubespray**, not an upstream download:
  `cert-manager.yml.j2` and `cert-manager.crds.yml.j2` are rendered into
  `{{ kube_config_dir }}/addons/cert_manager/` and applied with the `kube` module at
  `state: latest` (a `kubectl apply`, run only on `kube_control_plane[0]`). There is no
  Helm release and **no pruning** — objects the manifests stop containing are left behind.
- **The version is a static pin that has not moved:** `cert_manager_version: 1.15.3` in
  `roles/kubespray_defaults/defaults/main/download.yml` at **every tag from v2.27.0 through
  v2.31.0**. Upgrading Kubespray does not upgrade cert-manager, and the CRDs applied are
  whatever Kubespray vendored for 1.15.3 — check that against your Kubernetes version and
  against upstream's own support window before relying on it.
- Knobs beyond the on/off switch (`…/cert_manager/defaults/main.yml`):
  `cert_manager_namespace` (default `cert-manager`), `cert_manager_user` (`1001`),
  `cert_manager_tolerations` / `_affinity` / `_nodeselector`,
  `cert_manager_controller_extra_args`, `cert_manager_dns_policy` / `_dns_config`, the
  proxy trio (`cert_manager_http_proxy` / `_https_proxy` / `_no_proxy`), and
  `cert_manager_leader_election_namespace` (default `kube-system`; upstream note: change it
  on GKE Autopilot, which forbids writes to `kube-system`).

## Service impact

**Destructive by design on re-runs — read this before running Kubespray on a cluster whose
cert-manager holds anything you care about.** The role's first two tasks are tagged
`upgrade` and, on `kube_control_plane[0]`, they (1) delete
`{{ kube_config_dir }}/addons/cert_manager` on disk and (2) run
`kubectl delete namespace {{ cert_manager_namespace }}` with `ignore_errors: true`, before
the manifests are re-rendered and re-applied. A default Ansible run selects **all** tags, so
these tasks are not opt-in — deleting the namespace takes **Issuers, Certificates,
CertificateRequests, and the `ca-key-pair` Secret stored in it** with it. Back up the
namespace (`kubectl -n cert-manager get -o yaml …`, especially the CA key pair) before any
run that touches this role, and keep issuer definitions in Git so they can be re-applied.

Beyond that: applying the manifests rolls the cert-manager Deployments (controller, webhook,
cainjector). While the **webhook** is unavailable, admission of cert-manager CRs fails —
requests to create or update Certificates/Issuers are rejected until it is ready again.
Already-issued certificates in Secrets are untouched, so ingress traffic keeps working;
renewals pause for the duration.

## References

- `docs/advanced/cert_manager.md` (tag v2.31.0 `1c9add4`);
  `roles/kubernetes-apps/ingress_controller/cert_manager/{tasks,defaults}/main.yml` and
  `templates/cert-manager{,.crds}.yml.j2`;
  `roles/kubernetes-apps/ingress_controller/meta/main.yml` (conditional include + tags);
  `cert_manager_version` in `roles/kubespray_defaults/defaults/main/download.yml`
  (`1.15.3`, unchanged v2.27.0–v2.31.0).
