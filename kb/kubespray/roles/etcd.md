---
id: ROLE-ETCD
type: role
title: "etcd (Kubespray role)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - etcd role
  - etcd ansible role
tags:
  - role
sources:
  - type: code
    path: roles/etcd
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0/roles/etcd
    note: "etcd role"
relations:
  - type: see_also
    target: TAG-ETCD
---

# etcd

## Summary

Deploys and configures the etcd cluster: certificates (etcd-secrets), binary/image download, systemd or container setup, and health checks. Gated on etcd_deployment_type != kubeadm.

## Implementation

Task files under `roles/etcd/tasks/`. Invoked from the playbooks under the
corresponding run-tag (see [[TAG-ETCD]]).

## Configuration

Driven by variables in `roles/kubespray_defaults` (see [[ROLE-KUBESPRAY_DEFAULTS]]) and the role's own `defaults/`.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.

## References

- `roles/etcd/` (tag `v2.31.0` `1c9add4`).
