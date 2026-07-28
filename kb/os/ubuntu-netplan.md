---
id: CONCEPT-UBUNTU_NETPLAN
type: concept
title: "netplan on Kubespray nodes — declared vs running state, and why `netplan apply` is not a safe default"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-28"
confidence: verified
aliases:
  - netplan
  - netplan apply
  - netplan try
  - netplan get
  - ubuntu network configuration
  - bond vlan ubuntu node
tags:
  - os
  - ubuntu
  - networking
  - netplan
  - nodes
sources:
  - type: docs
    path: netplan — netplan-apply
    url: https://netplan.readthedocs.io/en/stable/netplan-apply/
    note: "netplan is stateless: apply does not remove virtual devices dropped from the config"
  - type: docs
    path: netplan — netplan-try
    url: https://netplan.readthedocs.io/en/stable/netplan-try/
    note: "applies a config and rolls it back automatically if not confirmed; default timeout 120 s"
  - type: issue
    path: Launchpad #1959706 — netplan apply does not remove defunct VLAN interfaces
    url: https://bugs.launchpad.net/bugs/1959706
    note: "confirms the stateless behaviour for VLANs specifically"
  - type: code
    path: kubespray v2.31.0 — netplan references
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.31.0
    note: "netplan appears only in contrib/terraform cloud-init templates; no role configures node networking"
relations:
  - type: see_also
    target: CONCEPT-UBUNTU_24_04_K8S
  - type: see_also
    target: CONCEPT-KUBESPRAY_NODE_IP
  - type: see_also
    target: PRACTICE-NODE_NETWORK_CHANGE
---

# netplan on Kubespray nodes — declared vs running state, and why `netplan apply` is not a safe default

## Summary

On Ubuntu nodes the network is described in `/etc/netplan/*.yaml` and rendered to systemd-networkd. Two
properties decide how a Kubernetes node behaves when that configuration is touched:

- **netplan is stateless.** `netplan apply` creates and updates what the YAML declares, but it does
  **not remove** virtual devices — bonds, bridges, VLANs — that were deleted from the config. They
  survive until they are deleted by hand or the node reboots.
- **`apply` re-applies everything, including the interface the node is reachable on.** On a node whose
  only uplink is a single bond, that is a real risk for the sake of a change that often does not need
  it.

Kubespray does not configure node networking: at v2.31.0 the only `netplan` references in the tree are
cloud-init templates under `contrib/terraform/`, used when *provisioning* VMs. On an existing host the
network config comes from the image or a separate configuration-management repo, and a cluster run
neither repairs nor breaks it.

## Context

**Reading the declared state without opening files:**

```bash
netplan get                    # everything
netplan get bonds              # one section
netplan get vlans
netplan get ethernets
netplan get bonds.aggi.interfaces
```

Compare that with the running state (`ip -br addr`, `ip -br link`, `/proc/net/bonding/<bond>`). A
difference in either direction is meaningful:

- **running has more than declared** — someone changed the live system by hand. It disappears on
  reboot, and until then it is invisible to anyone reading the config.
- **declared has more than running** — the config was edited but not applied, or a device failed to
  come up. It appears on the next reboot, which is the worst moment to discover it.

**Applying changes, from safest to riskiest:**

| Action | Effect | When |
|---|---|---|
| `ip link set <if> nomaster` / `ip link del <if>` | changes only the running system; config untouched | removing something the config never declared, or staging a removal |
| `netplan try` | applies and **auto-reverts after 120 s** unless confirmed | interactive changes on a node you can lose |
| `netplan apply` | applies immediately, no revert, re-initialises declared devices | after the runtime state is already correct, or in a maintenance window |
| reboot | full re-render from config | the definitive test that config and reality agree |

The stateless property has a useful consequence: **if you change only the running system and leave the
YAML alone, `netplan apply` is your rollback** — it recreates exactly what the config declares. That
turns an interface removal into a reversible, seconds-long operation.

**Removing a virtual device is a two-step change.** Because `apply` will not delete it, the order that
works is: delete at runtime (`ip link del <vlan>` then `ip link del <bond>`), verify the cluster is
healthy, and only then remove the blocks from the YAML so it does not come back on reboot. Deleting a
bond from the config while a VLAN still references it as `link:` leaves a config that fails to render
at boot — the one way to turn a cleanup into an outage.

**Permissions.** netplan warns when a config file is world-readable
(`Permissions for /etc/netplan/*.yaml are too open`) — these files can carry WiFi keys and other
secrets. `chmod 600 /etc/netplan/*.yaml`.

## References

- netplan documentation (`netplan-apply`, `netplan-try`) and Launchpad #1959706 — verified 2026-07-28.
- Kubespray v2.31.0 tree: `netplan` only under `contrib/terraform/` (verified 2026-07-28).
- Node-IP consequences: [[CONCEPT-KUBESPRAY_NODE_IP]]; safe procedure: [[PRACTICE-NODE_NETWORK_CHANGE]].
