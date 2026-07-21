---
id: COMPONENT-INGRESS_NGINX
type: component
title: "ingress-nginx (managed in v2.29.0–v2.30.0, removed in v2.31.0)"
status: deprecated
kubespray_version: ">=v2.29.0 <=v2.30.0"
kubernetes_version: ">=1.31 <=1.34"
component_version: "1.13.3"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ingress-nginx
  - ingress_nginx_enabled
  - nginx ingress controller
  - kubespray ingress nginx removed
tags:
  - component
  - ingress
  - networking
  - deprecated
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    lines: "309-312"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "ingress_nginx_version 1.13.3 at v2.29.0/v2.30.0"
  - type: code
    path: roles/kubernetes-apps/ingress_controller/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ingress_controller/meta/main.yml
    note: "v2.31.0 ingress_controller depends only on cert_manager + alb_ingress_controller — no nginx"
relations:
  - type: see_also
    target: PRACTICE-RUNBOOK_INGRESS_NGINX_DETACH
  - type: see_also
    target: TAG-INGRESS_CONTROLLER
  - type: see_also
    target: UPGRADE-V2_30_0__V2_31_0
  - type: see_also
    target: COMPONENT-METALLB
---

# ingress-nginx (managed in v2.29.0–v2.30.0, removed in v2.31.0)

## Summary

Kubespray shipped the **ingress-nginx** controller as an optional managed add-on in
`v2.29.0`–`v2.30.0` (`ingress_nginx_enabled`, controller `1.13.3`), and **removed** it in
`v2.31.0`. If you relied on Kubespray to deploy ingress-nginx, note that after upgrading
to `v2.31.0` the cluster will **no longer manage it** — you must install/maintain it
yourself (Helm/manifests). The only in-tree ingress controller left in `v2.31.0` is the
AWS ALB controller (`ingress_alb_enabled`).

## Context

- **Managed range:** Kubespray `v2.29.0`–`v2.30.0` (Kubernetes `1.31`–`1.34`).
- **Removed:** `v2.31.0` — `ingress_nginx_enabled` and `ingress_nginx_version` are gone
  from defaults, and `ingress_controller/meta` no longer references an nginx sub-role
  (only `cert_manager` and `alb_ingress_controller`).
- Deployed via the `ingress-controller` run-tag ([[TAG-INGRESS_CONTROLLER]]) on
  `kube_control_plane`.

## Implementation

- Enabled with `ingress_nginx_enabled: true` (default `false`) in the managed range.
- Controller image version pinned by `ingress_nginx_version` (**`1.13.3`** in both
  `v2.29.0` and `v2.30.0`); image tag `v{{ ingress_nginx_version }}`.
- Rendered and applied by `roles/kubernetes-apps/ingress_controller` under the
  `ingress-controller` tag.

## Configuration

Common knobs (managed range only): `ingress_nginx_host_network`,
`ingress_nginx_namespace`, `ingress_nginx_insecure_port` / `_secure_port`,
`ingress_nginx_nodeselector`, `ingress_nginx_class`. Set these in inventory
(`group_vars/k8s_cluster/addons.yml`) alongside `ingress_nginx_enabled`.

## Compatibility

- **`v2.31.0`: not available.** Do not set `ingress_nginx_enabled` on `v2.31.0` — it is
  no longer honored. Migrate to a self-managed ingress-nginx (upstream Helm chart) or a
  different ingress solution **before/around** the `v2.30.0 → v2.31.0` upgrade
  ([[UPGRADE-V2_30_0__V2_31_0]]). Ordered procedure with rollback:
  [[PRACTICE-RUNBOOK_INGRESS_NGINX_DETACH]].
- For LoadBalancer-type exposure (not HTTP ingress), MetalLB remains available
  ([[COMPONENT-METALLB]]).
- Controller `1.13.3` corresponds to the ingress-nginx project's `1.13.x` line; consult
  its own compatibility matrix for the Kubernetes versions it supports.

## References

- `ingress_nginx_version` (download.yml:309-312) at `v2.29.0`/`v2.30.0`; absence +
  `ingress_controller/meta` at `v2.31.0`. Run-tag: [[TAG-INGRESS_CONTROLLER]].
