---
id: PRACTICE-ARCHITECTURE_COMPATIBILITY
type: best_practice
title: "CPU architecture (amd64/arm64) feature compatibility"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-21"
confidence: verified
aliases:
  - architecture-compatibility
  - arm64 kubespray
  - mixed arch cluster cni
  - image_arch host_architecture
tags:
  - operations
  - arch
sources:
  - type: docs
    path: docs/advanced/arch.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/advanced/arch.md
    note: "digest of the tag doc"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "_host_architecture_groups (x86_64->amd64, aarch64->arm64, armv7l->arm) and host_architecture derived from ansible_architecture"
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "image_arch = host_architecture | default('amd64'); feeds every binary download URL and *_checksums[image_arch] lookup"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: PRACTICE-RUNBOOK_ADD_NODES
---

# CPU architecture (amd64/arm64) feature compatibility

## Summary

The node CPU architecture (amd64, arm64, or mixed) constrains which CNI plugins and features are usable. Cilium works on amd64 and arm64 but **not** on a mixed amd64+arm64 cluster; only Calico supports mixed clusters among CNIs.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- Matters when planning heterogeneous (mixed-arch) clusters or arm64 deployments.

## Implementation

The upstream table (`docs/advanced/arch.md`@v2.31.0) in full:

| `kube_network_plugin` | amd64 | arm64 | amd64 + arm64 |
|-----------------------|-------|-------|---------------|
| Calico                | Y     | Y     | **Y**         |
| Flannel               | Y     | N     | N             |
| Canal                 | Y     | N     | N             |
| Cilium                | Y     | Y     | **N**         |
| Contib                | Y     | N     | N             |
| kube-router           | Y     | N     | N             |

So Cilium (our indexed CNI) is supported on pure amd64 and pure arm64, but **not** on an
amd64+arm64 mixed cluster; Calico is the only plugin marked as mixed-capable. If you need a
mixed-arch cluster with Cilium, that combination is unsupported — use a single architecture,
or Calico for mixed.

**How architecture is decided, and why nothing stops you** (verified at v2.31.0):

- Architecture is **per host, from facts**: `host_architecture` maps `ansible_architecture`
  through `_host_architecture_groups` (`x86_64 → amd64`, `aarch64 → arm64`,
  `armv7l → arm`; anything else passes through unchanged), and
  `image_arch: "{{ host_architecture | default('amd64') }}"` then feeds every download URL
  and checksum lookup (`kubelet`/`kubectl`/`kubeadm`/`etcd` binaries and the
  `*_checksums[image_arch]` tables) — `roles/kubespray_defaults/defaults/main/main.yml`
  and `…/defaults/main/download.yml`.
- **The table is documentation, not a preflight check.** `0040-verify-settings.yml` does not
  validate the plugin against the cluster's architectures — a mixed-arch cluster with
  Cilium will simply be attempted, and fails later and less obviously (missing image
  variants, agents crash-looping on the unsupported nodes).
- Anything you pin by hand — image tags, `*_version` overrides, a private registry — must
  exist for **every** architecture in the inventory. A checksum table without a key for the
  node's `image_arch` fails the download task on that node only, which reads as a
  single-node problem rather than an architecture one.

## Service impact

None from reading this; the impact is in the decision. Architecture is fixed at node
provisioning time, so a wrong choice is not a variable flip: correcting it means
**replacing nodes** (drain, remove, re-provision, re-add — [[PRACTICE-RUNBOOK_ADD_NODES]]),
and, if the CNI itself must change, a cluster-wide CNI migration with full datapath
disruption. Decide before the first `cluster.yml`, and verify image availability for the
target architecture before mixing.

## References

- `docs/advanced/arch.md` (tag v2.31.0 `1c9add4`);
  `roles/kubespray_defaults/defaults/main/main.yml` (`_host_architecture_groups`,
  `host_architecture`), `…/defaults/main/download.yml` (`image_arch` and its use in
  download URLs / checksum lookups).
