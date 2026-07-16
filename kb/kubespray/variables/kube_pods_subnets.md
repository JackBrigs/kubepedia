---
id: VARIABLE-KUBE_PODS_SUBNETS
type: variable
title: kube_pods_subnets
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_pods_subnets
tags:
  - networking
  - dualstack
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/main.yml
    note: "Computed pod CIDR string selected by network stack (dual/ipv4/ipv6)."
relations:
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# kube_pods_subnets

## Summary
A computed variable that yields the effective pod subnet string for the active network stack. It combines `kube_pods_subnet` and `kube_pods_subnet_ipv6` for dual-stack, or returns just one of them for single-stack IPv4/IPv6. It is a derived `vars/` value, not a user-tunable default.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/main.yml` as a Jinja expression:

```yaml
kube_pods_subnets: >-
  {%- if ipv4_stack and ipv6_stack -%}
  {{ kube_pods_subnet }},{{ kube_pods_subnet_ipv6 }}
  {%- elif ipv4_stack -%}
  {{ kube_pods_subnet }}
  {%- else -%}
  {{ kube_pods_subnet_ipv6 }}
  {%- endif -%}
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 38 in every tag).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `ipv4_stack`, `ipv6_stack`, `kube_pods_subnet`, and `kube_pods_subnet_ipv6`.

## References
- roles/kubespray_defaults/vars/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
