---
id: TROUBLE-BOND_EXTRA_SLAVE_AGGREGATOR
type: troubleshooting
title: "Extra NIC enslaved into an LACP bond sits in a second aggregator — carries nothing, and can strand the node"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-28"
confidence: verified
aliases:
  - bond slave down aggregator 2
  - Actor Churn State churned
  - extra slave in bond
  - 802.3ad second aggregator
  - lacp slave not aggregating
tags:
  - os
  - ubuntu
  - networking
  - bonding
  - nodes
sources:
  - type: docs
    path: Linux kernel — bonding driver (802.3ad, ad_select)
    url: https://www.kernel.org/doc/Documentation/networking/bonding.rst
    note: "only one aggregator is active at a time; ad_select=stable keeps the current one until it loses all ports"
  - type: docs
    path: netplan — netplan-get
    url: https://netplan.readthedocs.io/en/stable/netplan-get/
    note: "reading the declared bond members to compare against the running state"
relations:
  - type: see_also
    target: CONCEPT-UBUNTU_NETPLAN
  - type: see_also
    target: PRACTICE-NODE_NETWORK_CHANGE
---

# Extra NIC enslaved into an LACP bond sits in a second aggregator — carries nothing, and can strand the node

## Summary

A bond has more members in `/proc/net/bonding/<bond>` than the config declares. The extra one shows
`MII Status: down`, `Speed: Unknown`, a **different Aggregator ID** than the working members, and
`Actor Churn State: churned`. It moves no traffic and looks harmless — but it is a port the switch does
not know about, sitting inside the node's uplink.

## Problem

In 802.3ad only **one** aggregator is active at a time. Ports that fail to negotiate LACP with the same
partner form their own aggregator, and the bond simply does not use it. So the symptom is quiet: no
error, no alert, no traffic impact — only a discrepancy between config and reality.

The risk is conditional and worth naming precisely. With the default `ad_select=stable` the active
aggregator is re-selected only when it loses **all** of its ports. If both real links flap at once, the
bond can move to the aggregator holding the misconfigured port — and that port is not configured on the
switch, so the node goes silent. Low probability, high cost, and it needs no human to trigger it.

Typical origin: someone tested an interface with `ip link set <if> master <bond>` and left it. Because
that is a runtime-only change, the config still shows the intended members and a reboot would clear it.

## Context

Any Ubuntu node with an 802.3ad bond; observed on Kubespray-managed nodes where the bond is the single
uplink. Kubespray does not manage the node's network configuration ([[CONCEPT-UBUNTU_NETPLAN]]), so the
discrepancy is invisible to a cluster run.

## Diagnostics

```bash
grep -E 'Slave Interface|MII Status|Aggregator ID|Speed|Churn State' /proc/net/bonding/<bond>
netplan get bonds.<bond>.interfaces        # what the config declares
```

Read it as a table: every healthy member shares one Aggregator ID with `MII Status: up` and
`Actor Churn State: none`. A member with a different Aggregator ID is not part of the working bundle,
whatever its link state says.

`Partner Mac Address: 00:00:00:00:00:00` at bond level means no LACP partner answered at all — a
different fault (switch side not configured for LACP), not this one.

## Known Issues

- **Fix, when the config does not declare it** — remove it from the bond only:

  ```bash
  ip link set <extra-if> nomaster
  grep -E 'Slave Interface|MII Status|Aggregator ID|Churn State' /proc/net/bonding/<bond>
  ```

  No `netplan apply`: the config is already correct, and apply would re-initialise the node's uplink
  for nothing. The removed NIC stays as a free DOWN interface — its normal state.
- **If the config *does* declare it**, this is a config change, not a cleanup: edit the YAML, and treat
  the apply as a risky operation on a single-uplink node ([[PRACTICE-NODE_NETWORK_CHANGE]]).
- **Do not "fix" it by bringing the port up.** If the switch side is not configured, an up port either
  stays in its own aggregator or, worse, negotiates with a different partner and gives the bond a
  second candidate bundle.
- **A down member of the *active* aggregator is a different problem** — that is a genuinely degraded
  bond (one live link instead of two) and belongs to the switch/cabling side.

## References

- Linux bonding driver documentation (802.3ad aggregator selection, `ad_select`); netplan `get`
  — verified 2026-07-28.
- Safe change procedure: [[PRACTICE-NODE_NETWORK_CHANGE]].
