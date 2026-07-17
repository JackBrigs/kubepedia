---
id: TROUBLE-KUBEADM_PREFLIGHT
type: troubleshooting
title: "kubeadm preflight errors (upgrade / init / join)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - kubeadm preflight error
  - ignore-preflight-errors
  - kubeadm_ignore_preflight_errors
  - port 6443 in use kubeadm
  - preflight cri socket
tags:
  - troubleshooting
  - kubeadm
  - preflight
  - upgrade
sources:
  - type: code
    path: roles/kubernetes/control-plane/tasks/kubeadm-setup.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/tasks/kubeadm-setup.yml
    note: "kubeadm init --ignore-preflight-errors=<computed>"
  - type: docs
    path: kubeadm implementation details (preflight)
    url: https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-init/
relations:
  - type: see_also
    target: CONCEPT-KUBESPRAY_KUBEADM_SEAM
  - type: see_also
    target: TROUBLE-KUBEADM_INIT_RETRY_FAILS
  - type: see_also
    target: TROUBLE-KUBEADM_VERSION_SKEW
---

# kubeadm preflight errors (upgrade / init / join)

## Summary

`kubeadm` runs **preflight checks** before `init`, `join`, and `upgrade`, and aborts with
`[preflight] Some fatal errors occurred: …`. During a Kubespray run this surfaces as an Ansible
failure wrapping the kubeadm stderr. Kubespray already passes a computed
**`--ignore-preflight-errors`** list; the remaining fatal checks are real.

## Problem

- `[preflight] Some fatal errors occurred:` — e.g. `Port 6443 is in use`, `/etc/kubernetes/…
  already exists`, `unsupported ... version`, CRI-socket ambiguity, cgroup/swap, kernel module,
  or a failed connectivity check.

## Context

- Applies to Kubespray **v2.29.0–v2.31.0** / Kubernetes **1.29–1.35**. Kubespray calls
  `kubeadm init/join --ignore-preflight-errors={{ ... }}` (setup/kubeadm role) — so anything
  still fatal is not on the ignore list.

## Diagnostics

- **Read the exact check name** kubeadm prints — each maps to a concrete fix:
  - **Port in use** (`6443`/`10259`/`10257`/`2379`): a leftover component from a failed prior
    run — see [[TROUBLE-KUBEADM_INIT_RETRY_FAILS]] (leftovers from the first try).
  - **`… already exists`** (`/etc/kubernetes/manifests`, `pki`): stale files from a partial run;
    clean per the retry doc.
  - **CRI socket:** with >1 runtime installed, set the socket explicitly
    (`--cri-socket unix:///var/run/containerd/containerd.sock`).
  - **cgroup/swap/kernel:** kubelet cgroup driver ([[TROUBLE-CGROUP_DRIVER_MISMATCH]]), swap,
    or a missing kernel module.
  - **Version check:** an unsupported version / skew is a preflight failure on `upgrade` —
    [[TROUBLE-KUBEADM_VERSION_SKEW]].
- **`--ignore-preflight-errors`:** Kubespray's list is computed; to add one, use the Kubespray
  variable (`kubeadm_ignore_preflight_errors`) rather than editing tasks — but **only** ignore
  checks you understand (ignoring a real one moves the failure downstream, e.g. into the health
  check — [[TROUBLE-KUBEADM_UPGRADE_HEALTH_CHECK]]).

## Known Issues

- Preflight failures on a **re-run** are usually leftovers from a **first failed try**, not a
  new problem — [[TROUBLE-KUBEADM_INIT_RETRY_FAILS]].

## References

- `kubeadm-setup.yml` (v2.31.0) + kubeadm init reference (above); seam:
  [[CONCEPT-KUBESPRAY_KUBEADM_SEAM]]; retries: [[TROUBLE-KUBEADM_INIT_RETRY_FAILS]]; skew:
  [[TROUBLE-KUBEADM_VERSION_SKEW]].
