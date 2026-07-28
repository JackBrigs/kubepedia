---
id: PRACTICE-NODE_NETWORK_CHANGE
type: best_practice
title: "Changing networking on a live Kubernetes node — prove it is unused, change runtime first, keep the rollback"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-28"
confidence: verified
aliases:
  - remove interface kubernetes node
  - delete bond vlan node safely
  - node network change procedure
  - is this interface used
tags:
  - os
  - ubuntu
  - networking
  - netplan
  - operations
  - nodes
sources:
  - type: docs
    path: netplan — netplan-apply (stateless behaviour)
    url: https://netplan.readthedocs.io/en/stable/netplan-apply/
    note: "apply does not delete virtual devices removed from the config — which is what makes it a rollback"
  - type: code
    path: roles/network_facts/tasks/main.yaml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_facts/tasks/main.yaml
    note: "node IP follows the default-route interface unless inventory pins `ip`"
relations:
  - type: see_also
    target: CONCEPT-UBUNTU_NETPLAN
  - type: see_also
    target: CONCEPT-KUBESPRAY_NODE_IP
  - type: see_also
    target: PRACTICE-CLUSTER_HEALTH_CHECKS
---

# Changing networking on a live Kubernetes node — prove it is unused, change runtime first, keep the rollback

## Summary

Removing an interface from a Kubernetes node looks trivial and is not: the thing that appears unused
may carry the node IP, a CNI device, an egress path or a secondary pod interface, and none of that is
visible from `ip addr` alone. This is the order that makes the change safe — evidence first, runtime
before config, one node at a time, with a rollback that costs one command.

## Context

Applies to Kubespray-managed nodes v2.27.0–v2.31.0 on Ubuntu with netplan. The procedure assumes the
interface is *believed* unused; if it is known to carry traffic, this is a migration, not a cleanup.

## Implementation

**1 — Prove nothing uses it.** Each check answers a different way the interface could be load-bearing;
skipping one is how "unused" turns into an incident:

```bash
IF=agge.2000        # the interface in question
ADDR=169.254.3.1

ip route show table all | grep -E "$IF|${ADDR%.*}\."   # routes in ANY table, not just main
ip rule show                                            # policy routing pointing at it
ss -lntup | grep -F "$ADDR"                             # anything bound to its address
ip -br addr                                             # macvlan/ipvlan devices = secondary pod NICs
```

Cluster side — the four things that bind an interface to Kubernetes:

```bash
kubectl -n kube-system exec ds/cilium -- cilium status --verbose | grep -iE 'routing|devices'
kubectl -n kube-system exec ds/cilium -- cilium bgp peers            # BGP over a /30 or /31 link
kubectl get ciliumegressgatewaypolicies -A                           # egress path pinned to a device
kubectl get net-attach-def -A -o custom-columns=NS:.metadata.namespace,NAME:.metadata.name,CFG:.spec.config \
  | grep -iE 'master|"'"$IF"'"'                                      # Multus attachments
```

A point-to-point `/30` or `/31` deserves particular suspicion: that addressing exists almost only for
router peering, so check BGP before concluding it is decorative.

**2 — Pin the node IP if it is not pinned.** If inventory has no `ip:` for the host, the node address
follows the default route and a network change can move it ([[CONCEPT-KUBESPRAY_NODE_IP]]). Pin it to
the current value first.

**3 — Change the running system, not the config.** Delete the VLAN before its parent bond; removing a
bond releases its slaves, which then sit idle and DOWN — that is their correct state, not a fault:

```bash
ip link del <vlan>
ip link del <bond>
ip -br link show | grep -E '<bond>|<slave1>|<slave2>'
```

Leaving the YAML untouched is deliberate: **`netplan apply` is now the rollback**, because netplan
recreates exactly what the config declares ([[CONCEPT-UBUNTU_NETPLAN]]).

**4 — Verify before touching the next node.**

```bash
NODE=<node>
kubectl get node "$NODE" -o wide                       # Ready, and the address unchanged
kubectl -n kube-system get pod -o wide --field-selector spec.nodeName="$NODE" | grep -vE 'Running|Completed'
POD=$(kubectl -n kube-system get pod -l k8s-app=cilium --field-selector spec.nodeName="$NODE" -o name | head -1)
kubectl -n kube-system exec "$POD" -- cilium status --brief
kubectl -n kube-system exec "$POD" -- cilium-health status --succinct   # reachability from every peer
systemctl is-active kubelet containerd
```

`cilium-health` is the one that answers "do the other nodes still see this one" — note its probe
interval (~3 min) and make sure the snapshot you are reading was taken *after* the change.

**5 — Make it permanent, last.** Once the node has run without the interface long enough to trust it,
remove the blocks from netplan — the bond, its VLAN and the slave entries **in one edit**, since a VLAN
whose `link:` no longer exists breaks config rendering at boot. No `netplan apply` is needed: the
running state is already correct, and the config now agrees with it.

**6 — One node at a time.** Repeat per node and re-run the pre-flight on each: identical roles do not
guarantee identical configs, and the addresses usually differ per host.

## Known Issues

- **`netplan apply` as the first move** re-initialises every declared device including the node's only
  uplink. It is the right tool after the runtime state is correct, not before.
- **Editing the config first** costs the cheap rollback: once the YAML no longer declares the device,
  `netplan apply` cannot bring it back.
- **A drained node is not required** for removing a device that carries no traffic, and drain does not
  protect against removing one that does — the evidence in step 1 is what protects you.
- **Reboot is the real test.** Until the node has rebooted, config and reality have only been checked
  by inspection.

## References

- netplan stateless-apply behaviour; `roles/network_facts/tasks/main.yaml` at v2.31.0 — verified
  2026-07-28.
- Health gate: [[PRACTICE-CLUSTER_HEALTH_CHECKS]]; netplan detail: [[CONCEPT-UBUNTU_NETPLAN]].
