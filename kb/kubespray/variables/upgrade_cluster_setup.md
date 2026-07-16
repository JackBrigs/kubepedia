---
id: VARIABLE-UPGRADE_CLUSTER_SETUP
type: variable
title: upgrade_cluster_setup
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - upgrade_cluster_setup
tags:
  - upgrade
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Forces control-plane manifest/config refresh during upgrade: false"
relations: []
---

# upgrade_cluster_setup

## Summary
Boolean toggle that forces regeneration of control-plane static manifests and configuration during a run. Default is `false`; the upgrade playbook sets it to `true` for the control-plane role.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as `upgrade_cluster_setup: false` (line 3, unchanged across all four tags). In `playbooks/upgrade_cluster.yml` line 58 the control-plane role is invoked with `upgrade_cluster_setup: true`. In v2.29.0 and v2.29.1 that role entry carries `tags: master`; in v2.30.0 and v2.31.0 the tag was renamed to `tags: control-plane` (the `upgrade_cluster_setup: true` override itself is unchanged). The variable default `false` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Enabled automatically by `upgrade_cluster.yml`; can be set manually to force control-plane reconfiguration during `cluster.yml`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- playbooks/upgrade_cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
