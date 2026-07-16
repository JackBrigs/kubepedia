---
id: VARIABLE-KUBE_VIP_RETRYPERIOD
type: variable
title: kube_vip_retryperiod
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_retryperiod
tags:
  - kube-vip
  - leader-election
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube-vip leader-election retry period, default 1"
relations:
  - type: see_also
    target: COMPONENT-KUBE_VIP
---

# kube_vip_retryperiod

## Summary
The retry period (in seconds) used by kube-vip leader election. Default is `1`.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `kube_vip_retryperiod: 1`. The value is unchanged across v2.29.0-v2.31.0; only the line number shifts (line 90 in v2.29.0/v2.29.1, line 87 in v2.30.0/v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant when kube-vip leader election is enabled. Related variables: `kube_vip_leaseduration`, `kube_vip_renewdeadline`, `kube_vip_leader_election_enabled`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
