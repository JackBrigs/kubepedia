---
id: VARIABLE-RETRY_STAGGER
type: variable
title: retry_stagger
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - retry_stagger
tags:
  - retries
  - ansible
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines retry_stagger with default 5"
relations: []
---

# retry_stagger

## Summary
Controls the stagger (randomized spread) applied when retrying failed operations, used to avoid thundering-herd retries against remote endpoints. Default value is `5`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `retry_stagger: 5`. It is also surfaced to users in the sample inventory at `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml` with the same value `5`. The default is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Present in Kubespray >=v2.29.0 <=v2.31.0. No constraints observed; the value is a plain integer default.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
