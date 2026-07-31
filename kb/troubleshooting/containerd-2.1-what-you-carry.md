---
id: TROUBLE-CONTAINERD_2_1_EXPOSURE
type: troubleshooting
title: "containerd 2.1.5: what a cluster on this pin is still carrying"
status: active
kubespray_version: ">=v2.29.0 <=v2.29.1"
kubernetes_version: null
component_version: ">=2.1.4 <=2.1.5"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 2.1.5 known issues
  - cni del never executed after restart
  - leaked ip addresses after node reboot
  - containerd credential leak pod events
  - should we upgrade containerd 2.1
tags:
  - troubleshooting
  - containerd
  - security
  - upgrade
sources:
  - type: docs
    path: containerd release notes 2.1.6 – 2.1.9 (bug-fix entries)
    url: https://github.com/containerd/containerd/releases
    note: "extracted 2026-07-31; only fixes released above 2.1.5 on the same maintenance line"
  - type: docs
    path: osv.dev API (github.com/containerd/containerd/v2)
    url: https://osv.dev/list?q=github.com/containerd/containerd/v2
    note: "six CVEs still open on 2.1.5; the 2.1 line's fix is 2.1.9"
relations:
  - type: see_also
    target: TROUBLE-CONTAINERD_KNOWN_CVES
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 2.1.5: what a cluster on this pin is still carrying

## Summary

Kubespray v2.29.0/v2.29.1 pin containerd **2.1.4/2.1.5**. Staying there means carrying **nine
defects** fixed later on the same 2.1 line — plus **six CVEs**, tracked separately in
[[TROUBLE-CONTAINERD_KNOWN_CVES]].

Four of the nine matter operationally, and none of them announces itself as a runtime problem:
network addresses leak after a reboot, credentials can reach pod events, mount flags are dropped in
user namespaces, and sandbox events go to the wrong topic. Each is first seen as a CNI, security or
scheduling issue.

## Problem

**`CNI DEL` was never executed after a restart (fixed in 2.1.7).** When containerd restarts, the
teardown callback for containers that ended around the restart never fires. The CNI plugin is never
told to release the address, so IPAM keeps handing out a shrinking pool while `kubectl` shows
nothing wrong. The symptom appears days later as pods failing to get an address on a node that looks
idle — and it is investigated as a CNI bug.

**Credentials could leak into pod events (fixed in 2.1.7).** An error returned over gRPC was not
sanitised before being surfaced, so registry credentials could end up in events readable by anyone
with `get events` in the namespace.

**Read-only bind mounts lost their flags in user namespaces (fixed in 2.1.7).** A mount declared
read-only could be mounted writable. With user namespaces enabled this is a containment failure, not
a performance detail; the related iteration bug in `getUnprivilegedMountFlags` was fixed in the same
release.

**Sandbox creation fields and event topics were wrong (fixed in 2.1.8).** Events published on the
wrong topic are events nobody is subscribed to — anything watching container lifecycle (monitoring,
policy engines, cleanup controllers) silently misses them.

The remainder: image volumes broken under user namespaces (2.1.7), a TOCTOU race in tar extraction
(2.1.7 — the same hardening that landed in 2.0.9 and 2.2.3), and out-of-range `USER` values causing
unexpected username lookups (2.1.8).

## Context

| Release | Fixes above 2.1.5 |
|---|---|
| 2.1.6 | none recorded |
| **2.1.7** | CNI DEL after restart; credential sanitising; read-only bind mounts in userns; mount-flag iteration; image volumes in userns; TOCTOU in tar extraction |
| **2.1.8** | sandbox create fields and event topics; out-of-range USER handling |
| 2.1.9 | no bug-fix entries; carries the CVE fixes — see the matrix |

## Diagnostics

```bash
# what is actually running, per node
kubectl get nodes -o wide | awk '{print $1, $NF}'

# address exhaustion from leaked allocations — compare in-use IPAM entries against running pods
kubectl get pods -A --field-selector spec.nodeName=<node> -o name | wc -l
# then, on the node:
ls /var/lib/cni/networks/*/ 2>/dev/null | wc -l      # host-local IPAM: files ≈ leased addresses
```

A count of leased addresses well above the number of running pods on that node is the fingerprint of
the missing `CNI DEL`, and it accumulates across restarts rather than appearing at once.

```bash
# did credentials reach events? (worth one look, cheap)
kubectl get events -A -o json | grep -iE '"message":.*(authorization|password|secret|token)' | head
```

## Known Issues

**The 2.1 line is a dead end for the CVEs.** Six advisories remain open on 2.1.5, and the fix for
most of them exists only from 2.1.9 / 2.2.5 / 2.3.2 upward. Bumping inside the line closes the
defects above; it does not close everything on the security side. Read the matrix before deciding
how far to move.

**Upgrading containerd is a node-by-node operation with a runtime restart**, so the CNI DEL defect
is worth fixing before, not during, a large maintenance window — a restart is precisely what
triggers the leak on the version being replaced.

**Kubespray computes the version from the newest checksum key**, so a pin must be explicit in
inventory, together with the matching checksum entry — the mechanism is described in
[[VARIABLE-CONTAINERD_VERSION]].

## References

- containerd release notes for 2.1.6–2.1.9, read 2026-07-31; full per-line index in
  `containerd 2.1: defects fixed in the 2.1 line`.
- Security exposure: [[TROUBLE-CONTAINERD_KNOWN_CVES]]; component: [[COMPONENT-CONTAINERD]].
