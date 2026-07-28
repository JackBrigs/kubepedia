---
id: TROUBLE-LEFTOVER_SECONDARY_BOND
type: troubleshooting
title: "Leftover secondary bond/VLAN on a node — how to prove it is unused before removing it"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-28"
confidence: verified
aliases:
  - unused bond on kubernetes node
  - leftover vlan interface node
  - 169.254 /31 interface node
  - remove second bond safely
tags:
  - os
  - ubuntu
  - networking
  - netplan
  - nodes
sources:
  - type: docs
    path: netplan — netplan-apply (stateless)
    url: https://netplan.readthedocs.io/en/stable/netplan-apply/
    note: "removing a device from the YAML does not delete it; and leaving the YAML intact keeps apply as a rollback"
  - type: code
    path: roles/network_facts/tasks/main.yaml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_facts/tasks/main.yaml
    note: "node IP follows the default-route interface unless pinned — the reason to check before removing anything"
relations:
  - type: see_also
    target: PRACTICE-NODE_NETWORK_CHANGE
  - type: see_also
    target: CONCEPT-UBUNTU_NETPLAN
  - type: see_also
    target: CONCEPT-KUBESPRAY_NODE_IP
---

# Leftover secondary bond/VLAN on a node — how to prove it is unused before removing it

## Summary

A node carries a second bond (often named for "external") with a VLAN on top and a link-local `/31`,
left over from a test of an additional network that was never provisioned upstream. It is usually
half-broken as well — one of its two members down — and nothing depends on it. "Usually" is not
evidence, and the checks that turn it into evidence are cheap.

## Problem

The interface looks decorative, but four things can quietly depend on a secondary interface, and none
of them show up in `ip addr`:

- **BGP peering.** A `/30` or `/31` address exists almost exclusively for point-to-point router
  peering. Cilium's BGP control plane, MetalLB or FRR may hold a session on it.
- **Egress path.** A Cilium egress-gateway policy can pin egress traffic to a device or address; the
  rules only materialise when a matching pod exists, so the interface can look idle today and be
  load-bearing tomorrow.
- **Secondary pod interfaces.** A Multus attachment definition names a `master` interface. No macvlan
  device on the node right now only means no pod is using it *at this moment*.
- **The node's own identity.** If inventory does not pin `ip:`, the node address follows the default
  route ([[CONCEPT-KUBESPRAY_NODE_IP]]).

## Context

Ubuntu nodes managed by Kubespray v2.27.0–v2.31.0. The secondary bond is declared in netplan (unlike a
hand-enslaved NIC), so removal is a two-step change: runtime first, config second
([[CONCEPT-UBUNTU_NETPLAN]]).

## Diagnostics

The full evidence set, and what each answer must be:

```bash
ip route show table all | grep -E '<bond>|<prefix>'   # only the connected /31 + its local + IPv6 scaffolding
ip rule show                                          # nothing referencing it (Cilium's fwmark rule is normal)
ss -lntup | grep -F <address>                         # no listeners
ip -br addr | grep -E 'macvlan|ipvlan'                # no secondary pod NICs

kubectl -n kube-system exec ds/cilium -- cilium bgp peers          # empty
kubectl get ciliumegressgatewaypolicies -A                          # none, or none for this node
kubectl get net-attach-def -A -o custom-columns=NS:.metadata.namespace,NAME:.metadata.name,CFG:.spec.config \
  | grep -iE 'master'                                               # none naming this bond or its members
kubectl -n kube-system exec ds/cilium -- cilium status --verbose | grep -i routing
```

With Cilium in **tunnel (VXLAN)** mode the pod data path follows the default route, so an interface
with no default route and no gateway cannot be carrying pod traffic — that plus an empty route table is
most of the proof.

Careful with a `169.254.*` grep: on a Kubespray node it also matches **nodelocaldns** on
`169.254.25.10` (`node-cache` on :53 and :9254). That is not your interface.

## Known Issues

- **Removal order:** VLAN first, then the bond — deleting the bond releases its members, which become
  free DOWN interfaces (correct, not a fault).

  ```bash
  ip link del <bond>.<vlan-id>
  ip link del <bond>
  ```

- **Do not edit netplan first.** While the YAML still declares the device, `netplan apply` recreates it
  — that is the rollback. Editing the config first throws it away.
- **When you do edit the config, remove bond, VLAN and member entries in one change.** A VLAN whose
  `link:` no longer exists fails to render at boot.
- **Half-dead is not a reason to keep it.** If the extra network is genuinely wanted, the switch side
  must be fixed too — a bond running on one of two members will silently stay that way after the
  network is finally provisioned.
- **Verify per node.** Addresses differ per host (`169.254.3.1/31` on one node, `169.254.4.1/31` on the
  next), and so can the config; identical roles do not imply identical files.

## References

- netplan stateless-apply behaviour; `roles/network_facts/tasks/main.yaml` at v2.31.0 — verified
  2026-07-28.
- Procedure and verification: [[PRACTICE-NODE_NETWORK_CHANGE]].
