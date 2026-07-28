---
id: CONCEPT-KUBESPRAY_NODE_IP
type: concept
title: "How Kubespray picks a node's IP — and what changing the network on a node moves with it"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-28"
confidence: verified
aliases:
  - node ip kubespray
  - kubelet node-ip
  - ansible_default_ipv4
  - access_ip
  - main_ip
  - apiserver cert SAN node ip
  - node registered with wrong ip
  - node ip changed after network change
  - wrong INTERNAL-IP on node
  - node re-registered under different address
tags:
  - kubespray
  - networking
  - nodes
  - certificates
sources:
  - type: code
    path: roles/network_facts/tasks/main.yaml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_facts/tasks/main.yaml
    note: "_ipv4 = ip | default(ansible_default_ipv4.address); main_ip / main_access_ip / main_ips are derived here"
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "kubelet_address: {{ main_ips | join(',') }} -> kubelet --node-ip"
  - type: code
    path: roles/kubernetes/control-plane/tasks/kubeadm-setup.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/tasks/kubeadm-setup.yml
    note: "apiserver SANs include main_ip, main_access_ip AND ansible_default_ipv4.address of every control-plane node"
relations:
  - type: see_also
    target: CONCEPT-UBUNTU_NETPLAN
  - type: see_also
    target: PRACTICE-NODE_NETWORK_CHANGE
  - type: see_also
    target: CONCEPT-TUNED_SYSCTL_OWNERSHIP
---

# How Kubespray picks a node's IP — and what changing the network on a node moves with it

## Summary

A node's identity in the cluster is an IP address, and unless it is pinned in inventory that address is
**derived from whichever interface holds the default route**. Adding, removing or re-routing an
interface can therefore change what the node registers as on the next Kubespray run — and on a
control-plane node it changes the API server certificate too.

## Context

**The derivation chain, read at v2.31.0** (`roles/network_facts/tasks/main.yaml`):

```
_ipv4        = ip | default(ansible_default_ipv4.address)      # inventory 'ip', else default-route iface
_access_ipv4 = access_ip | default(_ipv4)
main_ip      = _ipv4          main_ips = [_ipv4 (+ _ipv6 when dual-stack)]
main_access_ip = _access_ipv4
```

`main_ips` becomes `kubelet_address` (`roles/kubernetes/node/defaults/main.yml`), which is rendered
into the kubelet flag `--node-ip`. So:

- **`ip:` set in inventory** — the node IP is fixed and immune to interface changes.
- **`ip:` not set** — the node IP is `ansible_default_ipv4.address`, i.e. the source address of the
  default route at fact-gathering time. A second uplink that acquires a default route, or a route
  metric change, silently moves it.

The comment left in that file by upstream is worth quoting: *"ansible_default_ipv4 isn't what you
think."*

**On control-plane nodes it also lands in the certificate.** The API server SAN list in
`roles/kubernetes/control-plane/tasks/kubeadm-setup.yml` includes, for every control-plane host:
`main_access_ip`, `main_ip`, **and** `ansible_default_ipv4.address`. A default route that moved between
runs therefore produces a different SAN set, and the certificate is regenerated with it — clients
pinned to the old address stop validating.

**What this means operationally.** Before touching interfaces, bonds or routes on a node, check whether
the address is pinned:

```bash
grep -rnE '^\s*(ip|access_ip):' inventory/<cluster>/
kubectl get node <NODE> -o jsonpath='{.status.addresses}{"\n"}'
grep -r node-ip /etc/kubernetes/kubelet.env
ip route get 1.1.1.1                      # which interface currently wins
```

If it is not pinned, pin it to the current value **before** the network change, not after. That
converts "the node may re-register under a different address" into "nothing can move".

**`access_ip` is the second half.** It defaults to `ip` and is what other nodes are told to reach this
one on — relevant when nodes have a separate management network. Setting `ip` without `access_ip` is
usually right; setting `access_ip` alone is not, because the kubelet still binds by `ip`.

## References

- `roles/network_facts/tasks/main.yaml`, `roles/kubernetes/node/defaults/main.yml`,
  `roles/kubernetes/control-plane/tasks/kubeadm-setup.yml` — read at tag **v2.31.0**
  (verified 2026-07-28).
- Change procedure: [[PRACTICE-NODE_NETWORK_CHANGE]]; netplan behaviour: [[CONCEPT-UBUNTU_NETPLAN]].
