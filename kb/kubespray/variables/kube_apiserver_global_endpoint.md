---
id: VARIABLE-KUBE_APISERVER_GLOBAL_ENDPOINT
type: variable
title: kube_apiserver_global_endpoint
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_apiserver_global_endpoint
tags:
  - apiserver
  - loadbalancer
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Computed cluster-wide kube-apiserver URL"
relations: []
---

# kube_apiserver_global_endpoint

## Summary
Computed HTTPS URL used as the cluster-wide (global) kube-apiserver endpoint. It resolves to the external load balancer, `localhost`, or the first control-plane node address depending on the load-balancer configuration.

## Implementation
Defined as a Jinja2 template (`|-`) in `roles/kubespray_defaults/defaults/main/main.yml`. The expression changed between v2.29.1 and v2.30.0:

| Tags | Expression (summary) |
|------|----------------------|
| v2.29.0, v2.29.1 | If `loadbalancer_apiserver` defined → `https://{{ apiserver_loadbalancer_domain_name }}:{{ loadbalancer_apiserver.port \| default(kube_apiserver_port) }}`; elif `loadbalancer_apiserver_localhost and (loadbalancer_apiserver_port is not defined or == kube_apiserver_port)` → `https://localhost:{{ kube_apiserver_port }}`; else → `https://{{ first_kube_control_plane_address \| ansible.utils.ipwrap }}:{{ kube_apiserver_port }}` |
| v2.30.0, v2.31.0 | If `loadbalancer_apiserver` defined → `https://{{ apiserver_loadbalancer_domain_name \| ansible.utils.ipwrap }}:{{ loadbalancer_apiserver.port \| default(kube_apiserver_port) }}`; elif `loadbalancer_apiserver_localhost` → `https://localhost:{{ loadbalancer_apiserver_port \| default(kube_apiserver_port) }}`; else → `https://{{ first_kube_control_plane_address \| ansible.utils.ipwrap }}:{{ kube_apiserver_port }}` |

From v2.30.0 the domain name gains an `ansible.utils.ipwrap` filter, the localhost branch condition is simplified, and its port uses `loadbalancer_apiserver_port | default(kube_apiserver_port)`.

## Compatibility
Available in Kubespray v2.29.0–v2.31.0. Depends on `loadbalancer_apiserver`, `apiserver_loadbalancer_domain_name`, `loadbalancer_apiserver_localhost`, `loadbalancer_apiserver_port`, `kube_apiserver_port`, and `first_kube_control_plane_address`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
