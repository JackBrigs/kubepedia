---
id: PRACTICE-RUNBOOK_COMPONENT_UPGRADE
type: best_practice
title: "Runbook: upgrade a single component out-of-band (pin + apply)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - single component upgrade runbook
  - bump containerd version
  - pin component version kubespray
  - upgrade calico without kubespray upgrade
  - override component version
tags:
  - runbook
  - operations
  - upgrade
sources:
  - type: docs
    path: docs/operations/upgrades.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/upgrades.md
    note: "component versions pinnable (etcd_version, containerd_version, …) but must stay compatible with the release"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: depends_on
    target: UPGRADE-KUBESPRAY_SEQUENTIAL
  - type: see_also
    target: PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: PRACTICE-GRACEFUL_UPGRADE
---

# Runbook: upgrade a single component out-of-band (pin + apply)

## Summary

Sometimes you need to bump **one** component (containerd, runc, Calico, CoreDNS, etcd, an addon)
**without** moving the whole Kubespray minor — usually to pick up a CVE fix before the next release.
Kubespray lets you **pin** a component version via its `*_version` variable, but the pin **must stay
compatible** with the release you're on. This runbook is the safe pin-and-apply loop; a **full**
minor move is [[PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR]].

## Context

- **Override, don't fork.** Set the component's `*_version` (e.g. `containerd_version`,
  `calico_version`, `etcd_version`) in inventory; Kubespray uses it instead of the tag default. Its
  checksum must be known to Kubespray for the tag, or you also supply the checksum var.
- **Compatibility is on you.** The tag default was tested together; an out-of-band bump is not.
  Confirm the target version is compatible with your Kubernetes minor and the other pinned components
  ([[UPGRADE-KUBESPRAY_SEQUENTIAL]] compatibility notes) — a bad pin can break start-up.
- **Blast radius depends on the component:** a CNI or runtime bump touches every node (drain-safe,
  serial); an addon bump is usually a rolling Deployment. Prefer scoping to the relevant tag/role.
- **This is a bridge, not a destination** — carry the pin forward or drop it at the next real minor,
  or you drift from the tested set. Stable across **v2.27.0–v2.31.0**.

## Implementation

**Step 0 — Freeze, gate, back up** ([[CONCEPT-RUNBOOKS_INDEX]] spine): snapshot etcd, cluster healthy,
record the current component version (`kubectl get nodes -o wide` for runtime; the workload/DaemonSet
image for addons).

**Step 1 — Check compatibility** of the target version with your Kubernetes minor and co-installed
components. For a CVE-driven bump, confirm the fixed version in the component's CVE matrix (e.g.
[[TROUBLE-RUNC_KNOWN_CVES]], [[TROUBLE-CONTAINERD_KNOWN_CVES]]).

**Step 2 — Pin the version** in inventory:

```yaml
containerd_version: <target>     # example; use the component's own *_version var
# supply the matching *_checksums entry if the tag doesn't already know it
```

**Step 3 — Apply, scoped** to the component where possible (node-level components go serial/drained —
[[PRACTICE-GRACEFUL_UPGRADE]]):

```bash
# node-level (runtime/CNI): drain-aware, one node at a time
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/upgrade-cluster.yml -b -e serial=1
# or scope to a role/tag when the component maps to one (e.g. --tags network for CNI)
```

**Step 4 — Verify:** the component reports the new version (`crictl version`, DaemonSet image,
`etcdctl version`), all nodes `Ready`, workloads healthy, and the CVE you targeted is no longer
applicable.

**Rollback.** Set the `*_version` back to the previous value and re-apply the same way — component
version pins are reversible **if** the old version is still compatible and its data format didn't
change (most binaries) . For stateful components (etcd) a downgrade may not be supported — treat it
like [[PRACTICE-RUNBOOK_ETCD_RESTORE]] instead. The Step 0 snapshot covers the worst case.

## References

- `docs/operations/upgrades.md` (tag `v2.31.0`). Full-minor path
  [[PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR]]; sequencing/compat [[UPGRADE-KUBESPRAY_SEQUENTIAL]]; drain
  [[PRACTICE-GRACEFUL_UPGRADE]]; index [[CONCEPT-RUNBOOKS_INDEX]].
