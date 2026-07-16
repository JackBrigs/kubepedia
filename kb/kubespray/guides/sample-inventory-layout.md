---
id: CONCEPT-SAMPLE_INVENTORY_LAYOUT
type: concept
title: Sample inventory layout (where to set what)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - sample inventory
  - group_vars layout
  - where to set variables
tags:
  - inventory
  - operations
sources:
  - type: code
    path: inventory/sample/group_vars
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/inventory/sample/group_vars
    note: "sample inventory group_vars structure (verified from tag)"
relations:
  - type: see_also
    target: VARIABLE-KUBE_NETWORK_PLUGIN
  - type: see_also
    target: VARIABLE-KUBE_VERSION
---

# Sample inventory layout (where to set what)

## Summary

Kubespray configuration is set in `inventory/<cluster>/group_vars/`, copied from
`inventory/sample/`. This map shows which file holds which settings, so you know
**where to override** a given variable (all documented `VARIABLE-*` values live in
role defaults; the sample inventory is the user-facing surface for overriding
them).

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- Host groups (`inventory.ini`): `kube_control_plane`, `etcd`, `kube_node`;
  `k8s_cluster` = `kube_control_plane` + `kube_node`; plus `calico_rr` and
  `bastion` when used.

## Implementation

`group_vars/all/` — settings for every host:

- `all.yml` — general cluster-wide settings (proxies, loadbalancer, etc.).
- `offline.yml` — offline/air-gapped mirrors ([[PRACTICE-OFFLINE_ENVIRONMENT]]).
- `etcd.yml` — etcd deployment settings.
- `containerd.yml` / `cri-o.yml` / `docker.yml` — container runtime tuning (the
  active one depends on [[VARIABLE-CONTAINER_MANAGER]]).
- per-cloud: `aws.yml`, `azure.yml`, `gcp.yml`, `openstack.yml`, `vsphere.yml`,
  `oci.yml`, `hcloud.yml`, `huaweicloud.yml`, `upcloud.yml`.
- `coreos.yml` — Flatcar/CoreOS specifics.

`group_vars/k8s_cluster/` — Kubernetes cluster settings:

- `k8s-cluster.yml` — the core knobs: `kube_version`, `kube_network_plugin`,
  `kube_proxy_mode`, CIDRs, `dns_mode`, etc. (the most-edited file).
- `addons.yml` — enable/disable add-ons (`metrics_server_enabled`,
  `cert_manager_enabled`, ingress, CSI, …).
- `kube_control_plane.yml` — control-plane / API-server specifics.
- `k8s-net-<cni>.yml` — per-CNI tuning; the active one matches
  [[VARIABLE-KUBE_NETWORK_PLUGIN]] (e.g. `k8s-net-cilium.yml` for Cilium).

Precedence: `group_vars` override role `defaults`; role code is the source of
truth for the default value (see any `VARIABLE-*` doc).

## References

- `inventory/sample/group_vars/` and `inventory/sample/inventory.ini`
  (tag `v2.31.0` `1c9add4`).
