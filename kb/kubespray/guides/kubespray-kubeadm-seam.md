---
id: CONCEPT-KUBESPRAY_KUBEADM_SEAM
type: concept
title: "The Kubespray↔kubeadm seam — who does the upgrade, where errors come from"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - kubespray kubeadm seam
  - who upgrades kubernetes kubespray
  - kubeadm upgrade apply kubespray
  - ansible vs kubeadm error
  - upgrade preflight seam
tags:
  - kubespray
  - kubeadm
  - upgrade
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/tasks/kubeadm-upgrade.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/tasks/kubeadm-upgrade.yml
    note: "kubeadm upgrade apply/node + init phase addon/etcd/control-plane"
  - type: code
    path: roles/kubernetes/control-plane/tasks/check-api.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/tasks/check-api.yml
    note: "Ansible-side /healthz wait (60x5s)"
relations:
  - type: see_also
    target: CONCEPT-KUBEADM_CONFIG
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
  - type: see_also
    target: TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK
---

# The Kubespray↔kubeadm seam — who does the upgrade, where errors come from

## Summary

Kubespray does **not** upgrade Kubernetes itself — it **orchestrates kubeadm**. During a
Kubespray upgrade the Ansible roles invoke `kubeadm upgrade apply/node` (and `kubeadm init
phase …`) on the control-plane nodes; the real work — component version bumps, preflight,
health checks, addon/etcd re-apply — is **kubeadm's**. So a failure that appears "in the middle
of an Ansible run" is very often a **kubeadm** error, not a Kubespray one. This doc maps the
seam so you know which layer to debug.

## Context

- The base covers both banks well — the Ansible roles/variables layer and the Kubernetes layer —
  but the **seam between them** (kubeadm invoked by Kubespray) is where upgrade/preflight/
  health-check errors actually surface. This is the anchor for that layer.
- Applies to Kubespray **v2.29.0–v2.31.0** (code-grounded at v2.31.0).

## Implementation

**The upgrade delegation map** (`roles/kubernetes/control-plane/tasks/`):

| Ansible task | kubeadm command it runs | What it does |
|--------------|-------------------------|--------------|
| `pre-upgrade.yml` | (checks / drains) | pre-flight prep before touching the CP |
| `kubeadm-upgrade.yml` (primary CP) | **`kubeadm upgrade apply -y v<kube_version>`** | the actual control-plane upgrade + kubeadm's own preflight/health checks |
| `kubeadm-upgrade.yml` (secondary CP) | **`kubeadm upgrade node`** | upgrade the other control-plane nodes |
| `kubeadm-upgrade.yml` | `kubeadm init phase upload-config all` / `addon kube-proxy` / `etcd local` / `control-plane all` | re-render config/addons/etcd/CP static pods |
| `check-api.yml` | *(none — Ansible `uri`)* | **Kubespray's own** wait: `GET https://<ip>:6443/healthz == 200`, 60×5 s |
| `kubernetes/kubeadm` `main.yml`, `control-plane/kubeadm-setup.yml` | `kubeadm join`/`init --ignore-preflight-errors=<…>` | node bring-up (init/join) |

**Reading an error — which layer?**

- **kubeadm output** (`[preflight] …`, `[upgrade/health] …`, `[upgrade/apply] …`, `field is
  immutable`, `error execution phase …`): the failure is **kubeadm's** — go to the kubeadm
  troubleshooting docs below.
- **Ansible failure** (`FAILED! => {"rc": 1, ...}` wrapping the kubeadm stderr, or a task
  `failed_when`/`until` timeout): Ansible is **reporting** the kubeadm failure. Note Kubespray
  deliberately **tolerates some kubeadm errors** — e.g. `kubeadm upgrade` is
  `failed_when: rc != 0 and "field is immutable" not in stderr` (immutable-field errors are
  ignored), and several `init phase` tasks `retry`.
- **`check-api.yml` timeout** (`/healthz` never 200 after 5 min): the API didn't come healthy
  after kubeadm ran — the root cause is usually a kubeadm health-check/static-pod problem
  ([[TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK]]), not Ansible.

## Compatibility

- kubeadm enforces the **version-skew** policy (one minor at a time, kubelet within N-3) — a
  Kubespray upgrade that skips a minor fails at kubeadm, not Ansible
  ([[TROUBLE-KUBEADM_VERSION_SKEW]]).
- The kubeadm config it applies is `kubeadm-config.yaml` ([[CONCEPT-KUBEADM_CONFIG]]); the
  target version comes from `kube_version` ([[CONCEPT-KUBERNETES_VERSION_SUPPORT]]).

## References

- `kubeadm-upgrade.yml` + `check-api.yml` (v2.31.0, above). Seam troubleshooting:
  [[TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK]], [[TROUBLE-KUBEADM_PREFLIGHT]],
  [[TROUBLE-KUBEADM_UPGRADE_APPLY]], [[TROUBLE-KUBEADM_VERSION_SKEW]]. Config:
  [[CONCEPT-KUBEADM_CONFIG]]; versions: [[CONCEPT-KUBERNETES_VERSION_SUPPORT]].
