---
id: UPGRADE-CONTAINERD_2_1_TO_2_3
type: upgrade
title: "containerd 2.1.5 → 2.2 / 2.3: the runtime upgrade that also closes the CVEs"
status: active
kubespray_version: ">=v2.29.1 <=v2.31.0"
kubernetes_version: null
component_version: ">=2.1.5 <=2.3.3"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 2.1 to 2.2 upgrade
  - should we upgrade containerd
  - containerd 2.3 what changes
  - close containerd cves upgrade path
tags:
  - upgrade
  - containerd
  - security
sources:
  - type: docs
    path: containerd release notes 2.2.x and 2.3.x
    url: https://github.com/containerd/containerd/releases
    note: "extracted 2026-07-31; 46 fixes on the 2.2 line, 14 on 2.3, one declared breaking change"
  - type: docs
    path: osv.dev API (github.com/containerd/containerd/v2)
    url: https://osv.dev/list?q=github.com/containerd/containerd/v2
    note: "the six advisories open on 2.1.5 are fixed from 2.2.5 / 2.3.2 upward"
relations:
  - type: see_also
    target: TROUBLE-CONTAINERD_2_1_EXPOSURE
  - type: see_also
    target: TROUBLE-CONTAINERD_KNOWN_CVES
  - type: see_also
    target: VARIABLE-CONTAINERD_VERSION
---

# containerd 2.1.5 → 2.2 / 2.3: the runtime upgrade that also closes the CVEs

## Summary

The runtime upgrade is the one place where the defect argument and the security argument point the
same way. Staying on **2.1.5** keeps nine known defects and **six CVEs**, including host-root command
execution triggered by pulling a crafted image. The 2.1 line never fully closes them; **2.2.5** and
**2.3.2** do.

Only **one breaking change** is declared across both lines, and it affects plugin naming, not
workloads.

## Upgrade Notes

**The single declared breaking change** — 2.3.0: OCI hook adjustments now accumulate owners and
**commas are no longer allowed in plugin names**. Relevant only with NRI plugins in use; a name
containing a comma stops being accepted.

**What the move fixes, beyond the 2.1 backports:**

- *CNI `DEL` never executed after a restart* (2.2.2) — the address-leak defect described in
  [[TROUBLE-CONTAINERD_2_1_EXPOSURE]], fixed on the 2.2 line as well;
- *mount flags dropped for read-only bind-mounts in user namespaces* (2.2.2);
- *nil-pointer dereference in container spec memory metrics* when memory constraints are partially
  configured (2.2.2) — a crash reachable from an ordinary pod spec;
- *migrated CRI image config broken with legacy registry mirrors* (2.2.2) — matters for an
  air-gapped or mirrored registry setup;
- *overlay "rebase" disabled inside a user namespace* to fix layer-extraction failures (2.2.4), and
  *mount manager enabled in diff walking* for snapshotters such as EROFS (2.2.3);
- *sandbox creation fields and event topics* (2.2.4, the same fix as 2.1.8);
- *nil-pointer in NRI `GetIPs` during pod sandbox teardown or container exit* (2.2.6 / 2.3.3) — a
  crash on the teardown path, which is the busiest path on a node that churns pods.

**On 2.3 specifically:** sandbox task API endpoints fixed for non-runc runtimes, with task fields in
runc options deprecated (2.3.1); a Windows-only race in the runtime v2 pipe reader (2.3.2).

**Security is the deciding argument.** Of the six advisories open on 2.1.5, the fixes land at
2.1.9 / 2.2.5 / 2.3.2 depending on the line. Choosing 2.2.5+ closes all six and picks up the defect
fixes above; choosing 2.1.9 closes the CVEs while leaving the 2.2-line improvements behind.

## Implementation

Kubespray computes `containerd_version` from the newest checksum key, so the target must be pinned
explicitly in inventory together with its checksum — the mechanism and the trap are described in
[[VARIABLE-CONTAINERD_VERSION]]. Checksums for 2.2.5 and newer already exist on Kubespray `master`
and can be copied from there rather than computed.

AWX: playbook `cluster.yml`, **Job Tags** `container-engine`, Limit empty, privilege escalation on.

### Impact

Upgrading the runtime restarts containerd on each node. Running containers survive a restart of the
daemon itself, but the node is briefly unable to start or stop containers, and the CRI stream is
interrupted — `kubectl exec`/`logs` against that node fail during the window.

Do it node by node. Note the ordering trap: the `CNI DEL` defect is *triggered* by a restart on the
version being replaced, so leaked addresses may appear on the way out. Check IPAM after each node
rather than at the end.

### Rollback

Re-pin the previous version and re-run the same scope. The runtime downgrade is supported; container
state on the node is not preserved across a rollback of the snapshotter format, so prefer draining a
node before reverting it.

## Compatibility

Kubespray v2.31.0 pins 2.2.3, so 2.2.x is the version line the project itself is moving to; 2.3.x is
ahead of the envelope and is a manual pin. Kubernetes 1.32.8 works with all three lines — the CRI
contract does not change across them.

## References

- containerd release notes for 2.2.x and 2.3.x, read 2026-07-31; the per-line index lives in
  `containerd 2.2: defects fixed in the 2.2 line` and its 2.3 counterpart.
- Current exposure: [[TROUBLE-CONTAINERD_2_1_EXPOSURE]]; advisories:
  [[TROUBLE-CONTAINERD_KNOWN_CVES]]; pinning: [[VARIABLE-CONTAINERD_VERSION]].
