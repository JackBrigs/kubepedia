---
id: TAG-CALICO_RR
type: ansible_tag
title: "calico_rr — Ansible tag for the Calico BGP route-reflector role"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: confirmed
aliases:
  - calico_rr tag
  - calico route reflector ansible tag
  - --tags calico_rr
  - i-am-a-route-reflector
tags:
  - kubespray
  - ansible-tag
  - calico
  - bgp
sources:
  - type: code
    path: playbooks/cluster.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "role network_plugin/calico/rr tagged ['network','calico_rr'], hosts calico_rr group"
  - type: code
    path: roles/network_plugin/calico/rr/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/calico/rr/tasks/main.yml
    note: "labels calico_rr nodes i-am-a-route-reflector=true"
relations:
  - type: see_also
    target: TAG-NETWORK
  - type: see_also
    target: COMPONENT-CALICO
  - type: see_also
    target: CONFIG-CALICO_DATAPLANE
---

# calico_rr — Ansible tag for the Calico BGP route-reflector role

## Summary

`calico_rr` is the one **CNI-specific** Ansible tag in Kubespray. It scopes the
**`network_plugin/calico/rr`** role, which configures the nodes in the **`calico_rr`** inventory group
as Calico **BGP route reflectors**. Note the broader picture: Kubespray does **not** have a tag per CNI
plugin — every CNI (Cilium, Calico, Flannel, Kube-OVN, …) deploys under the single **`network`** tag
([[TAG-NETWORK]]); `calico_rr` is the only additional CNI-scoped tag, for the Calico route-reflector
topology.

## Context

- Applies to Kubespray **v2.27.0–v2.31.0**. In `playbooks/cluster.yml` the route-reflector role is
  tagged **`['network', 'calico_rr']`** and runs against the **`calico_rr`** host group, so
  `--tags calico_rr` (or `--tags network`) triggers it.
- **Why route reflectors:** in a full-mesh BGP Calico deployment, every node peers with every other —
  which doesn't scale. **Route reflectors** (RRs) let nodes peer with a small set of RRs instead,
  cutting the peering count on large clusters ([[COMPONENT-CALICO]], [[CONFIG-CALICO_DATAPLANE]]).

## Implementation

- Put the designated RR nodes in the **`calico_rr`** inventory group. The role runs pre-upgrade tasks,
  configures the node's BGP settings, and **labels** each RR node **`i-am-a-route-reflector=true`** so
  Calico treats it as a reflector.
- Run scoped: `ansible-playbook cluster.yml --tags calico_rr` reconfigures only the route-reflector
  layer; a full `--tags network` run reconfigures the whole CNI including RRs.
- Only relevant with **Calico in BGP mode** on clusters large enough to need RRs; small clusters and
  non-Calico CNIs never use this tag.

## Compatibility

- Stable across the indexed range; only meaningful when `kube_network_plugin: calico` with BGP and a
  populated `calico_rr` group. For non-Calico CNIs the tag is a no-op (empty host group).
- Do **not** expect per-plugin tags (`--tags cilium` for the CNI, `--tags flannel`, …) — they don't
  exist; use `--tags network` to reconcile the CNI and `calico_rr` for the reflector subset.

## References

- `playbooks/cluster.yml`, `roles/network_plugin/calico/rr/tasks/main.yml` (tag v2.31.0). General CNI
  tag [[TAG-NETWORK]]; Calico [[COMPONENT-CALICO]]; dataplane [[CONFIG-CALICO_DATAPLANE]].
