---
id: VARIABLE-KUBE_APISERVER_PORT
type: variable
title: kube_apiserver_port
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kube_apiserver_port
tags:
  - apiserver
  - networking
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "303 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_apiserver_port: 6443 (default, unchanged v2.29.0–v2.31.0)"
relations:
  - type: see_also
    target: VARIABLE-LOADBALANCER_APISERVER_LOCALHOST
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube_apiserver_port

## Summary

`kube_apiserver_port` is the secure port the kube-apiserver listens on. The
default is `6443` across `v2.29.0`–`v2.31.0`.

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml` (`6443`, unchanged
across all four tags). It is used in the kubeadm configuration and by the node-
local API load balancer (see [[VARIABLE-LOADBALANCER_APISERVER_LOCALHOST]]) that
fronts the control plane ([[CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS]]).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `6443`.
- Changing it affects the API endpoint, the local/external load balancer, and
  kubeconfig; keep it consistent cluster-wide.

## References

- `roles/kubespray_defaults/defaults/main/main.yml` — default (L290 in v2.29.0,
  L303 in v2.31.0; shifts by tag).
- Tags: v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
