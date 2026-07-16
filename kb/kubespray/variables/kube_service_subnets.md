---
id: VARIABLE-KUBE_SERVICE_SUBNETS
type: variable
title: kube_service_subnets
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_service_subnets
tags:
  - networking
  - services
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/main.yml
    note: "Computed stack-aware service CIDR string derived from kube_service_addresses / kube_service_addresses_ipv6"
relations: []
---

# kube_service_subnets

## Summary
Computed service CIDR string that adapts to the IP stack (IPv4-only, IPv6-only, or dual-stack). It combines `kube_service_addresses` and/or `kube_service_addresses_ipv6` and is used wherever the cluster's service CIDR must be passed to kubeadm, the apiserver, and CNI components.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/main.yml:28` as a computed Jinja expression (not a plain literal):

```yaml
kube_service_subnets: >-
  {%- if ipv4_stack and ipv6_stack -%}
  {{ kube_service_addresses }},{{ kube_service_addresses_ipv6 }}
  {%- elif ipv4_stack -%}
  {{ kube_service_addresses }}
  {%- else -%}
  {{ kube_service_addresses_ipv6 }}
  {%- endif -%}
```

It is consumed in the kubeadm config templates (`serviceSubnet`, `service-cluster-ip-range`), in the kube-ovn CNI template (`--service-cluster-ip-range`), and in the `network_facts` role (no_proxy / network facts). The expression and the path are unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Derived from `kube_service_addresses`, `kube_service_addresses_ipv6`, `ipv4_stack`, and `ipv6_stack`; parallels `kube_pods_subnets` in the same file.

## References
- roles/kubespray_defaults/vars/main/main.yml
- roles/kubernetes/control-plane/templates/kubeadm-config.v1beta4.yaml.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
