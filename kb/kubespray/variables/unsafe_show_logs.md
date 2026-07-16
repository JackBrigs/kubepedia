---
id: VARIABLE-UNSAFE_SHOW_LOGS
type: variable
title: unsafe_show_logs
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - unsafe_show_logs
tags:
  - logging
  - debug
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Toggles verbose task log output that may leak private data"
relations: []
---

# unsafe_show_logs

## Summary
Boolean toggle that enables verbose Ansible task log/verbosity output which may contain private data; the code comment recommends `false` in production. The effective default changed between v2.29.0 and v2.29.1 (see table).

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`. The default differs between tags:

| Tag | Value |
| --- | --- |
| v2.29.0 (line 8) | `false` |
| v2.29.1 (line 10) | `"{{ lookup('env', 'CI_PROJECT_URL') == 'https://gitlab.com/kargo-ci/kubernetes-sigs-kubespray' }}"` |
| v2.30.0 (line 10) | `"{{ lookup('env', 'CI_PROJECT_URL') == 'https://gitlab.com/kargo-ci/kubernetes-sigs-kubespray' }}"` |
| v2.31.0 (line 10) | `"{{ lookup('env', 'CI_PROJECT_URL') == 'https://gitlab.com/kargo-ci/kubernetes-sigs-kubespray' }}"` |

From v2.29.1 onward the default evaluates to `true` only inside the Kubespray CI environment and `false` otherwise. The sample inventory `inventory/sample/group_vars/all/all.yml:139` sets `unsafe_show_logs: false` in all four tags. In v2.29.0 the default was additionally duplicated in several roles (`bootstrap_os`, `etcd_defaults`, csi_driver/vsphere); these duplicates were consolidated by v2.29.1.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Behavior change at v2.29.1: default became CI-environment-dependent instead of a hardcoded `false`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- inventory/sample/group_vars/all/all.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
