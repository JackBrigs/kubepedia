---
id: VARIABLE-KUBE_APISERVER_IP
type: variable
title: kube_apiserver_ip
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_ip
tags:
  - apiserver
  - networking
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Computed in-cluster ClusterIP of the kubernetes service"
relations:
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_apiserver_ip

## Summary
The in-cluster ClusterIP assigned to the `kubernetes` API service. Computed as the first usable address (`.1`) of the first configured service subnet.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:
`kube_apiserver_ip: "{{ kube_service_subnets.split(',') | first | ansible.utils.ipaddr('net') | ansible.utils.ipaddr(1) | ansible.utils.ipaddr('address') }}"`.
The same expression is mirrored in `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`. The role default is authoritative and unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0–v2.31.0. Derived from `kube_service_subnets`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
