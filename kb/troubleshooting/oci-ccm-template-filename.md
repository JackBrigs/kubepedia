---
id: TROUBLE-OCI_CCM_TEMPLATE_FILENAME
type: troubleshooting
title: "OCI external cloud controller: wrong template filename in lookup"
status: active
kubespray_version: "v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - oci-ccm-template-filename
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/13151
    note: "fix merged in v2.31.0 (PR #13151)"
  - type: code
    path: roles/kubernetes-apps/external_cloud_controller/oci/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/external_cloud_controller/oci/tasks/main.yml
    note: "fixed file"
relations: []
---

# OCI external cloud controller: wrong template filename in lookup

## Summary

Deploying the OCI (Oracle Cloud) external cloud-controller-manager failed because the role looked up an incorrect template filename. Fixed in **v2.31.0** (PR #13151).

## Problem

The OCI CCM task referenced a template name that did not match the actual file, so templating failed on OCI clusters. The fix corrects the filename.

## Context

- Affected Kubespray: `v2.30.0`. Fixed in: `v2.31.0`.
- Confirmed via merged PR #13151 and the tag code.

## Diagnostics

```bash
# task fails with a template-not-found error when external_cloud_controller is OCI
ansible-playbook cluster.yml --tags external-cloud-controller  # observe the lookup error
```

## Known Issues

Fixed by PR #13151 (in `roles/kubernetes-apps/external_cloud_controller/oci/tasks/main.yml`). Workaround before upgrading: n/a beyond upgrading — it is an internal filename fix; upgrade to v2.31.0. Durable fix: upgrade to `v2.31.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/13151 — fixed in `v2.31.0`.
- `roles/kubernetes-apps/external_cloud_controller/oci/tasks/main.yml`.
