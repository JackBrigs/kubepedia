---
id: TROUBLE-NODE_CANNOT_REACH_APISERVER
type: troubleshooting
title: "Node can't reach the API server (localhost LB / nginx-proxy)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - kubelet cannot reach apiserver
  - nginx-proxy not up
  - localhost loadbalancer 6443
  - node connection refused 127.0.0.1:6443
  - loadbalancer_apiserver_localhost
tags:
  - troubleshooting
  - control-plane
  - networking
  - kubespray
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "loadbalancer_apiserver_localhost (default true); type nginx"
relations:
  - type: see_also
    target: TROUBLE-FIREWALL_PORTS_BLOCKED
  - type: see_also
    target: TROUBLE-KUBE_VIP_CONTROL_PLANE_VIP
---

# Node can't reach the API server (localhost LB / nginx-proxy)

## Summary

kubelet/pods on a node can't reach the API server (`connection refused`/timeout to
`127.0.0.1:6443`). When there's no external LB, Kubespray puts a **local API load balancer** on
each non-control-plane node — a `nginx-proxy` static pod that forwards `127.0.0.1:6443` to the
real control-plane endpoints. If it's down or misconfigured, the whole node loses the API.

## Problem

- `kubelet` logs `connection refused`/`i/o timeout` to the apiserver; node `NotReady`; pods
  can't reach the in-cluster API.

## Context

- Applies to Kubespray **v2.29.0–v2.31.0**. Default **`loadbalancer_apiserver_localhost: true`**
  (when no external `loadbalancer_apiserver` is defined), **`loadbalancer_apiserver_type:
  nginx`** — non-CP nodes talk to the API via the local proxy, not directly.

## Diagnostics

- **nginx-proxy static pod:** on the affected node check `crictl ps | grep nginx-proxy` and its
  config (`/etc/nginx/nginx.conf`) — it must list the current control-plane IPs. A crashlooping
  or stale-config proxy breaks API access for that node.
- **Upstream control plane:** the proxy is only as good as the CP nodes behind it — if the CPs
  are down (etcd quorum / apiserver), the proxy returns errors too ([[TROUBLE-ETCD_QUORUM_LOSS]]).
- **Firewall/routing:** the node must reach the CP nodes on **6443**
  ([[TROUBLE-FIREWALL_PORTS_BLOCKED]]).
- **VIP setups:** if you use kube-vip/HAProxy instead of the localhost proxy, that path is the
  suspect ([[TROUBLE-KUBE_VIP_CONTROL_PLANE_VIP]]).
- **kubeconfig target:** on the node, kubelet/pod kubeconfigs should point at the proxy/VIP
  address the cluster was built with — a wrong `--server` breaks it.

## Known Issues

- Adding/removing control-plane nodes changes the upstream list — the local proxies must be
  reconfigured (a Kubespray run does this); a manual CP change without re-running leaves stale
  proxy configs.

## References

- `loadbalancer_apiserver_localhost` default (v2.31.0, above); ports:
  [[TROUBLE-FIREWALL_PORTS_BLOCKED]]; VIP: [[TROUBLE-KUBE_VIP_CONTROL_PLANE_VIP]].
