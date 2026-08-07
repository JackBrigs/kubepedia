---
id: PRACTICE-RUNBOOK_ORDER_NODES
type: best_practice
title: "Runbook: order new nodes — derive the spec from the running cluster, never from memory"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-08-07"
confidence: confirmed
aliases:
  - заказ нод
  - заказать сервер
  - order new node
  - node order form
  - resource request node
  - какие параметры сервера заказать
  - спецификация новой ноды
  - имена нод придумать
tags:
  - runbook
  - operations
  - provisioning
  - capacity
  - inventory
sources:
  - type: measurement
    path: sc-lux99-x-test-5-kube-node1, sc-lux99-x-test-5-kube-node2
    note: "12 vCPU, 24 GB, 120 GB; линейно 945 MB/s, 4K QD1 19 MB/s (~4750 IOPS, 0.21 мс) — флеш, выше потолка SATA"
  - type: measurement
    path: sc-ams94-mlt-prod-sec-kube-node3..node6
    note: "физические R440: DMI-слоты и perccli дают состав; на ВМ те же поля фиктивны"
  - type: doc
    path: kubelet swap requirement
    url: https://kubernetes.io/docs/concepts/architecture/nodes/#swap-memory
    note: "swap на узле не заказывается"
relations:
  - type: see_also
    target: PRACTICE-RUNBOOK_ADD_NODES
  - type: see_also
    target: TROUBLE-ADD_NODE_GOTCHAS
---

## Summary

A new node must be a copy of the nodes it will stand beside, and the copy is taken
from the running machines — not from a wiki page and not from memory. A mixed
cluster schedules unevenly and fails in ways that are hard to attribute later. The
deliverable is a filled request form and a pair of names that fit the existing
convention exactly.

## Context

Applies when nodes are added to an existing cluster. Two facts decide everything
that follows and both are read from the running fleet:

- **Physical or virtual.** `systemd-detect-virt` distinguishes them. On a VM the
  DMI memory-slot data is fictional (QEMU reports one dummy module regardless of
  real size) and disk media flags are meaningless — the real size comes from
  `/proc/meminfo`, the real storage class from measurement.
- **Whether the existing nodes are uniform.** If they are not, there is no single
  answer to give, and the procedure below branches.

Node names are not cosmetic: inventory groups, AWX limits and monitoring rules key
off them. The convention is read from the existing hosts and continued, never
invented.

## Implementation

**1. Read the spec off the running nodes.**

```bash
nproc                                          # vCPU
awk '/MemTotal/{printf "%.0f GB\n", $2/1048576}' /proc/meminfo
lsblk -dn -o NAME,SIZE,MODEL                   # диски
grep PRETTY /etc/os-release                    # ОС
systemd-detect-virt                            # физика или ВМ
```

**2. Classify the storage by measurement, not by flags.** Inside a VM the
"non-rotational" flag is set unconditionally, and behind a RAID controller the
kernel cannot see the media at all. A read-only test settles it:

```bash
dd if=/dev/sda of=/dev/null bs=1M count=512 iflag=direct    # линейно
dd if=/dev/sda of=/dev/null bs=4k count=2000 iflag=direct skip=100000
```

Reading is safe on a live node. Interpretation at queue depth 1:

| 4K random read | class |
|---|---|
| ~0.5–1 MB/s (~150 IOPS, 5–10 ms) | spinning disk |
| >15 MB/s (>4000 IOPS, <0.5 ms) | flash |

Sequential above ~550 MB/s also rules out a single SATA device.

**3. Continue the naming convention.** Read the existing hosts from the inventory
and take the next sequence numbers. Example from a real cluster: existing
`sc-lux99-x-test-5-kube-node1` and `-node2` yield `-node3` and `-node4`, where
`lux99` is the site, `x-test-5` the cluster and the trailing digit the sequence.

**4. Answer in the form's own shape.** The request form is the deliverable; prose
around it is not. Reproduce its field names and order verbatim:

```
project, dc, name and other info

<hostname1><hostname2>

resources

OS - ubuntu 24.04vCPUs - 12RAM - 24 Gbstorage type - faststorage space - 120Gb
```

**5. Branch when the fleet is not uniform.** If the target nodes differ from each
other — different CPU, memory, disk count, or a naming scheme that does not extend
cleanly — do not average them into one answer and do not silently pick one. Present
each distinct configuration as a separate filled form and say which existing nodes
each is copied from, so the choice stays with the person placing the order.

## Known Issues

**Do not downgrade the OS minor to whatever is "current" elsewhere.** Kubespray
configures a node from its actual distribution; a node joined on an older release
diverges in kernel, containerd and systemd behaviour, and the divergence surfaces
later and elsewhere.

**Storage class is the field most often guessed wrong.** Where a catalogue offers
"normal" and "fast", asking for the cheaper tier without knowing what backs it can
drop latency by an order of magnitude on some nodes only. The result reads as
random pod timeouts on part of the cluster — an expensive thing to diagnose for the
money saved.

**Sizing is copied, not recalculated.** Utilisation of the existing nodes is worth
reporting (it justifies the number), but a new node smaller than its peers makes
the cluster heterogeneous, which costs more than the capacity saved.

**Swap is not ordered.** kubelet requires it off.

**Addresses are not part of the hardware spec** but block delivery: free addresses
in the same subnet must be confirmed by whoever owns the network before the request
is placed.

## References

- Inventory repository — source of the naming convention and of the current host list
- `systemd-detect-virt`, `/proc/meminfo`, `lsblk`, `dd` — the reading and measuring commands above
- Runbook for adding the ordered nodes to the cluster once delivered
