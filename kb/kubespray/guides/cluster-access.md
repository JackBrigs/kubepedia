---
id: PRACTICE-CLUSTER_ACCESS
type: best_practice
title: "Getting cluster access (kubeconfig / kubectl) after a Kubespray deploy"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeconfig
  - admin.conf
  - kubeconfig_localhost
  - kubectl_localhost
  - how to access the cluster
  - artifacts_dir
tags:
  - operations
  - access
  - kubeconfig
  - best-practice
sources:
  - type: code
    path: roles/kubernetes/client/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/client/tasks/main.yml
    note: "copies admin.conf and kubectl to artifacts_dir when *_localhost enabled (tag v2.31.0)"
  - type: code
    path: roles/kubernetes/client/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/client/defaults/main.yml
    note: "artifacts_dir default = {inventory_dir}/artifacts (tag v2.31.0)"
relations:
  - type: see_also
    target: CONCEPT-SAMPLE_INVENTORY_LAYOUT
  - type: see_also
    target: TROUBLE-APISERVER_CERT_SAN
---

# Getting cluster access (kubeconfig / kubectl) after a Kubespray deploy

## Summary

After a Kubespray run the admin kubeconfig lives on the control-plane nodes at
`/etc/kubernetes/admin.conf`. To use the cluster from your workstation, either copy that
file or have Kubespray drop it locally with `kubeconfig_localhost: true` (and optionally
`kubectl_localhost: true` for the matching `kubectl`). Both are **off by default**.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- On nodes: the admin credential is `{{ kube_config_dir }}/admin.conf`
  (`/etc/kubernetes/admin.conf`) — cluster-admin, treat it as a secret.
- The `kubernetes/client` role handles local artifacts.

## Implementation

**Have Kubespray fetch it (recommended):**

- `kubeconfig_localhost: true` → copies `admin.conf` to
  **`{{ artifacts_dir }}/admin.conf`** (default `{{ inventory_dir }}/artifacts/`) on the
  machine running Ansible.
- `kubectl_localhost: true` → downloads the matching `kubectl` binary to
  `{{ artifacts_dir }}/kubectl` plus a `kubectl.sh` wrapper pinned to that kubeconfig.
- Then: `export KUBECONFIG=inventory/<cluster>/artifacts/admin.conf` and use `kubectl`.

**Or copy it manually:**

- `scp root@<cp-node>:/etc/kubernetes/admin.conf ./admin.conf` and set `KUBECONFIG`.

**Reachability:** the kubeconfig's `server:` address must be one the cert is valid for. If
you reach the API through an LB/VIP/DNS name, that address must be in the apiserver
cert SANs (`supplementary_addresses_in_ssl_keys`) or TLS fails
([[TROUBLE-APISERVER_CERT_SAN]]).

## Compatibility

- `admin.conf` is **cluster-admin** — don't commit it, and prefer issuing scoped
  kubeconfigs (RBAC users/service accounts) for day-to-day use.
- The fetched kubeconfig points at `kube_apiserver_access_address` (control-plane
  reachable IP); if that's a per-node IP, consider an API VIP/LB for a stable endpoint
  (kube-vip — [[CONCEPT-SERVICE_EXPOSURE]]).
- Rotating the cluster CA or admin cert invalidates old copies — re-fetch after such
  operations.

## References

- `kubernetes/client` role (`kubeconfig_localhost`, `kubectl_localhost`, `artifacts_dir`)
  at tag `v2.31.0`. Cert SANs: [[TROUBLE-APISERVER_CERT_SAN]]; inventory:
  [[CONCEPT-SAMPLE_INVENTORY_LAYOUT]].
