---
id: TROUBLE-FIREWALL_PORTS_BLOCKED
type: troubleshooting
title: "Cluster traffic blocked by a firewall (required ports)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - firewalld blocking kubernetes
  - required ports kubespray
  - node NotReady firewall
  - kubelet 10250 timeout
  - etcd 2379 2380 blocked
  - nodeport not reachable firewall
  - disable firewall kubespray
tags:
  - troubleshooting
  - networking
  - firewall
  - ports
  - preflight
sources:
  - type: docs
    path: docs/operations/port-requirements.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/port-requirements.md
    note: "authoritative required-ports list (tag v2.31.0)"
  - type: docs
    path: docs/getting_started/setting-up-your-first-cluster.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/getting_started/setting-up-your-first-cluster.md
    note: "recommends disabling the firewall to avoid deployment issues (tag v2.31.0)"
relations:
  - type: see_also
    target: TROUBLE-KUBESPRAY_PREFLIGHT_FAILS
  - type: see_also
    target: PRACTICE-NODE_NOT_READY
  - type: see_also
    target: COMPONENT-CILIUM
---

# Cluster traffic blocked by a firewall (required ports)

## Summary

Kubespray does **not** manage host firewalls; its docs recommend **disabling** the
firewall (or explicitly opening the required ports) to avoid deployment and runtime
failures. A running `firewalld`/`ufw`/cloud security-group that blocks the control-plane,
kubelet, or CNI ports produces confusing symptoms — nodes `NotReady`, `kubectl
logs/exec` timing out, cross-node DNS failing, NodePorts unreachable — that look like
app or CNI bugs but are pure connectivity.

## Problem

Intermittent or one-directional cluster failures with no obvious app cause: nodes flap
`NotReady`; `kubectl logs`/`exec`/`port-forward` hang or `timeout` (kubelet `10250`);
API/etcd unreachable from some nodes; pods on node A can't reach pods/DNS on node B;
NodePort services unreachable; Cilium health checks / Hubble failing. Often appears only
between certain nodes or after enabling a host firewall.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Kubespray configures no firewall rules —
  the host firewall is the operator's responsibility.
- Required ports (from `docs/operations/port-requirements.md`, tag `v2.31.0`):

**Control plane (inbound):**

| Proto | Port | Purpose |
|-------|------|---------|
| TCP | 22 | SSH (Ansible) |
| TCP | 2379 | etcd client |
| TCP | 2380 | etcd peer |
| TCP | 6443 | Kubernetes API |
| TCP | 10250 | kubelet API |
| TCP | 10257 | kube-controller-manager |
| TCP | 10259 | kube-scheduler |

**Worker node (inbound):**

| Proto | Port | Purpose |
|-------|------|---------|
| TCP | 22 | SSH (Ansible) |
| TCP | 10250 | kubelet API |
| TCP | 30000–32767 | NodePort range |

**Cilium (our indexed CNI):**

| Proto | Port | Purpose |
|-------|------|---------|
| TCP | 4240 | cilium-health |
| TCP | 4244 / 4245 | Hubble server / relay |
| UDP | 8472 | VXLAN overlay |
| TCP | 9962 / 9963 / 9964 | Cilium agent / operator / proxy metrics |
| UDP | 51871 | WireGuard tunnel (if encryption) |
| ICMP | — | health checks |

**Add-ons:** `9100` node-exporter; `7472` MetalLB metrics; `7946` TCP/UDP MetalLB L2.
(Calico, if used, needs `179`/BGP, `4789`/VXLAN, `5473`/Typha, `51820-1`/WireGuard,
IPIP — Calico is deferred in this KB.)

## Diagnostics

- Test reachability node-to-node: `nc -vz <peer> 10250`, `nc -vz <cp> 6443`,
  `nc -vz <etcd> 2379`.
- Check the host firewall state: `systemctl status firewalld` / `firewall-cmd
  --list-all` (RHEL-family), `ufw status` (Debian/Ubuntu), and cloud
  security-groups/NACLs.
- Overlay path: for Cilium VXLAN confirm **UDP 8472** is open both ways (a blocked
  overlay = pods can't cross nodes while same-node works).
- `kubectl get nodes -o wide` + `journalctl -u kubelet` on a `NotReady` node — a kubelet
  the API can't reach on `10250` shows up here.

## Known Issues

- **Fix:** either disable the host firewall (Kubespray's recommendation for simplicity)
  or open the ports above between the relevant host groups. On RHEL-family this is the
  single most common cause of a partially-working cluster.
- **Direction matters:** control-plane ports must be reachable **from** worker nodes and
  vice-versa; overlay (VXLAN `8472`) must be open **both** ways between all nodes.
- Cloud environments enforce firewalls at the **security-group** layer even when the
  host firewall is off — check both.
- ICMP is used by Cilium health checks; dropping all ICMP can cause false health
  failures.
- This is a runtime counterpart to preflight checks — the deploy may even succeed, then
  break later when the firewall is (re)enabled. See [[TROUBLE-KUBESPRAY_PREFLIGHT_FAILS]]
  and [[PRACTICE-NODE_NOT_READY]].

## References

- `docs/operations/port-requirements.md` and the first-cluster guide at tag `v2.31.0`.
- Kubernetes ports reference (kubernetes.io/docs/reference/networking/ports-and-protocols).
