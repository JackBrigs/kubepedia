---
id: PRACTICE-PORT_REQUIREMENTS
type: best_practice
title: Kubespray firewall port requirements
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - port requirements
tags:
  - firewall
  - networking
  - ports
sources:
  - type: docs
    path: docs/operations/port-requirements.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/port-requirements.md
    note: "ports that must be open for Kubespray components"
relations: []
---

# Kubespray firewall port requirements

## Summary
When the network is protected by firewall rules, Kubespray requires specific ports to be open so infrastructure components can communicate. This covers the Kubernetes control plane and worker nodes, plus CNI-specific ports for Calico and Cilium and common addon ports. Some ports are optional depending on configuration and usage.

## Context
Applies to environments with firewall rules between hosts. Ensure the ports below are open and allow access between the relevant hosts before/while running Kubespray. The exact set depends on the chosen CNI (Calico vs Cilium) and enabled addons.

## Implementation
Kubernetes control plane:
- TCP 22 — ssh for ansible
- TCP 2379 — etcd client port
- TCP 2380 — etcd peer port
- TCP 6443 — kubernetes api
- TCP 10250 — kubelet api
- TCP 10257 — kube-scheduler
- TCP 10259 — kube-controller-manager

Kubernetes worker node(s):
- TCP 22 — ssh for ansible
- TCP 10250 — kubelet api
- TCP 30000-32767 — kube nodePort range

Calico (if used):
- TCP 179 — Calico networking (BGP)
- UDP 4789 — Calico CNI with VXLAN enabled
- TCP 5473 — Calico CNI with Typha enabled
- UDP 51820 — Calico with IPv4 WireGuard enabled
- UDP 51821 — Calico with IPv6 WireGuard enabled
- IPENCAP / IPIP — Calico CNI with IPIP enabled

Cilium (if used):
- TCP 4240 — Cilium health checks (cilium-health)
- TCP 4244 — Hubble server
- TCP 4245 — Hubble Relay
- UDP 8472 — VXLAN overlay
- TCP 9962 — Cilium-agent Prometheus metrics
- TCP 9963 — Cilium-operator Prometheus metrics
- TCP 9964 — Cilium-proxy Prometheus metrics
- UDP 51871 — WireGuard encryption tunnel endpoint
- ICMP — health checks

Addons:
- TCP 9100 — node exporter
- TCP/UDP 7472 — metallb metrics ports
- TCP/UDP 7946 — metallb L2 operating mode

## References
- docs/operations/port-requirements.md (tag v2.31.0 1c9add4)
