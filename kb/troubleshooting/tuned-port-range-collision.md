---
id: TROUBLE-TUNED_PORT_RANGE_COLLISION
type: troubleshooting
title: "Component fails to bind after reboot: ephemeral port range lowered to 1024 covers kubelet/etcd ports"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-28"
confidence: verified
aliases:
  - bind address already in use kubelet
  - address already in use 10250
  - ip_local_port_range 1024 65535 kubernetes
  - ephemeral port conflict kubelet etcd
  - ip_local_reserved_ports kubernetes
tags:
  - os
  - sysctl
  - tuned
  - networking
  - nodes
sources:
  - type: code
    path: roles/kubernetes/node/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/tasks/main.yml
    note: "'Ensure nodePort range is reserved' sets ip_local_reserved_ports to kube_apiserver_node_port_range only"
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "kube_apiserver_node_port_range default 30000-32767"
relations:
  - type: see_also
    target: CONCEPT-TUNED_SYSCTL_OWNERSHIP
  - type: see_also
    target: PRACTICE-PORT_REQUIREMENTS
---

# Component fails to bind after reboot: ephemeral port range lowered to 1024 covers kubelet/etcd ports

## Summary

A performance profile widens the ephemeral port range —

```
net.ipv4.ip_local_port_range = 1024 65535
```

— to gain outbound ports. The kernel default starts at **32768** precisely so that service ports
below it can never be taken by an outgoing connection. Lowering the floor puts every Kubernetes port
(kubelet 10250, etcd 2379/2380, kube-proxy 10256, controller-manager 10257, scheduler 10259) inside
the range an outbound socket may claim. The result is a rare, unreproducible startup failure:
`bind: address already in use` for a component that is not running twice.

## Problem

The race needs three things at once: the port is free (component restarting or node booting), some
process opens an outbound connection, and the kernel hands it that exact port. It therefore surfaces
after reboots and rolling restarts, on one node out of many, and never reproduces on demand.

`net.ipv4.ip_local_reserved_ports` is the guard — the kernel skips those ports when allocating
ephemeral ones. Two problems in practice:

1. **The profile's list is usually incomplete.** Lists carried between fleets typically cover
   `6443`, the NodePort range and application ports, but omit `10250`, `10256`, `10257`, `10259`,
   `2379`, `2380`.
2. **Kubespray overwrites the list.** The task *Ensure nodePort range is reserved* sets it to
   `kube_apiserver_node_port_range` (default `30000-32767`) and reloads — so after any run touching
   the node role, only the NodePort range stays reserved and every other port loses its protection
   until the tuned profile is re-applied ([[CONCEPT-TUNED_SYSCTL_OWNERSHIP]]).

Note the interaction: with the **default** port range (`32768 60999`) the whole issue disappears —
Kubernetes service ports and the NodePort range both sit below 32768, out of reach of ephemeral
allocation. Kubespray's own reservation is belt-and-braces for exactly the case where someone widened
the range.

## Context

Applies to Kubespray-managed nodes v2.27.0–v2.31.0 where a tuning profile (tuned or a plain
`sysctl.d` drop-in) lowers `ip_local_port_range`. The reserved-ports task is unchanged across the
envelope, as is the `30000-32767` default.

## Diagnostics

```bash
sysctl net.ipv4.ip_local_port_range net.ipv4.ip_local_reserved_ports
grep -rn 'ip_local_port_range\|ip_local_reserved' /etc/sysctl.d/ /etc/tuned/profiles/*/tuned.conf

# after a failed start, confirm the port was taken by an ephemeral socket
ss -tanp | grep -E ':(10250|10256|10257|10259|2379|2380)\b'
journalctl -u kubelet --since -1h | grep -i 'address already in use'
```

## Known Issues

- **Preferred fix: restore the default range** — `net.ipv4.ip_local_port_range = 32768 60999`. Service
  ports become unreachable for ephemeral allocation, and the fight over the reserved list stops
  mattering. Changing the range does not disturb established connections and needs no restart.
- **If the wide range is genuinely required** (very high outbound connection churn), the reserved
  list must cover every service port on the node — add `10250`, `10256`, `10257`, `10259`, `2379`,
  `2380` plus whatever the CNI and monitoring bind — and you must accept that a Kubespray run
  narrows it again until the profile is re-applied.
- **A sysctl.d drop-in with a later filename does not protect at runtime.** Ansible reloads its own
  file directly, so lexical order only decides the outcome at boot.
- **Do not widen `kube_apiserver_node_port_range` to smuggle extra ports into the reservation.** The
  same variable feeds the apiserver's `--service-node-port-range` and Calico's
  `FELIX_KUBENODEPORTRANGES`; changing it changes Service behaviour.

## References

- `roles/kubernetes/node/tasks/main.yml`, `roles/kubernetes/node/defaults/main.yml` — read at tag
  **v2.31.0** (verified 2026-07-28). Port inventory: [[PRACTICE-PORT_REQUIREMENTS]].
