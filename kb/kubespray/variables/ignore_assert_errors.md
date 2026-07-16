---
id: VARIABLE-IGNORE_ASSERT_ERRORS
type: variable
title: ignore_assert_errors
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - ignore_assert_errors
tags:
  - preinstall
  - validation
sources:
  - type: code
    path: roles/kubernetes/preinstall/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/defaults/main.yml
    note: "Allow pre-check assertions to fail and continue deployment; default false"
relations: []
---

# ignore_assert_errors

## Summary
Boolean toggle that, when `true`, lets Kubespray pre-check (assert) failures pass and the deployment continue instead of aborting. Default is `false`, so failing pre-checks stop the run.

## Implementation
Defined as `ignore_assert_errors: false` in both `roles/kubernetes/preinstall/defaults/main.yml` (with the comment "Set to true to allow pre-checks to fail and continue deployment") and `roles/kubespray_defaults/defaults/main/main.yml`.

The default value `false` is unchanged across v2.29.0-v2.31.0. (Note: the molecule prepare playbook `roles/container-engine/molecule/prepare.yml` sets it to `true` for test scaffolding only.)

## Compatibility
Kubespray v2.29.0-v2.31.0. Related: the preinstall `asserts` tasks.

## References
- roles/kubernetes/preinstall/defaults/main.yml
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
