---
id: VARIABLE-KUBE_VIP_LEADER_ELECTION_ENABLED
type: variable
title: kube_vip_leader_election_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_vip_leader_election_enabled
tags:
  - kube-vip
  - leader-election
sources:
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "Defines kube_vip_leader_election_enabled defaulting to kube_vip_arp_enabled"
relations: []
---

# kube_vip_leader_election_enabled

## Summary
Enables kube-vip leader election. Default is the value of `kube_vip_arp_enabled` (`"{{ kube_vip_arp_enabled }}"`). When truthy, leader-election env vars (lease name, duration, etc.) are rendered into the kube-vip manifest.

## Implementation
Defined in `roles/kubernetes/node/defaults/main.yml` as `kube_vip_leader_election_enabled: "{{ kube_vip_arp_enabled }}"`. Consumed by `roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2` (`{% if kube_vip_leader_election_enabled %}`). The computed expression is unchanged across v2.29.0-v2.31.0 (line moved from 75 to 73).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies only when kube-vip is deployed. Related: `kube_vip_arp_enabled`, `kube_vip_leasename`, `kube_vip_leaseduration`.

## References
- roles/kubernetes/node/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
