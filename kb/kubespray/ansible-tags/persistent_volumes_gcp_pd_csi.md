---
id: TAG-PERSISTENT_VOLUMES_GCP_PD_CSI
type: ansible_tag
title: "persistent_volumes_gcp_pd_csi (Ansible run-tag)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - persistent_volumes_gcp_pd_csi
  - "--tags persistent_volumes_gcp_pd_csi"
tags:
  - ansible-tag
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubernetes-apps/persistent_volumes/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/persistent_volumes/meta/main.yml
    note: "run-tag persistent_volumes_gcp_pd_csi"
relations: []
---

# persistent_volumes_gcp_pd_csi (Ansible run-tag)

## Summary

Создаёт объекты хранилища (StorageClass) для Google Persistent Disk через под-роль roles/kubernetes-apps/persistent_volumes/gcp-pd-csi..

## Context

- **Playbooks:** `cluster.yml`, `upgrade_cluster.yml`
- **Affected host groups:** `kube_control_plane`
- **Roles:** `kubernetes-apps/persistent_volumes/gcp-pd-csi`

## Implementation

Создаёт объекты хранилища (StorageClass) для Google Persistent Disk через под-роль roles/kubernetes-apps/persistent_volumes/gcp-pd-csi.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`.
- **Standalone-run safety: safe.** Условие включения: gcp_pd_csi_enabled. Помечен вместе с тегом gcp-pd-csi-driver. При выключенном флаге — no-op.

## References

- `roles/kubernetes-apps/persistent_volumes/meta/main.yml`
- Migrated from the Kubepedia 0.1.0 analysis (`knowledge-base/versions/v2.31.0/ansible-tags.yaml`); verified against tag `v2.31.0` `1c9add4`.
