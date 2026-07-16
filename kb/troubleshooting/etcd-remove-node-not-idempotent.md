---
id: TROUBLE-ETCD_REMOVE_NODE_NOT_IDEMPOTENT
type: troubleshooting
title: "etcd: remove-node.yml is not idempotent and fails if the etcd member is already gone"
status: active
kubespray_version: ">=v2.29.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - etcd remove-node not idempotent
tags:
  - etcd
  - remove-node
  - idempotency
sources:
  - type: github_pr
    url: https://github.com/kubernetes-sigs/kubespray/pull/12949
    note: "Fixes #12947 — make etcd member removal idempotent"
relations: []
---

# etcd: remove-node.yml is not idempotent and fails if the etcd member is already gone

## Summary
Re-running (or running after the fact) node removal via `remove-node.yml` fails with a templating (undefined) error when the corresponding member is no longer in the etcd cluster. The failure occurs while computing the member ID. Affects v2.29.0, v2.29.1, and v2.30.0; the fix lands in the later patches v2.29.2 and v2.30.1.

## Problem
A repeated or "after the fact" node removal run fails with a templating (undefined) error when the corresponding member is already absent from the etcd cluster. It breaks while computing the member ID:

```
{{ '%x' | format(((etcd_members.stdout | from_json).members
   | selectattr('peerURLs.0', '==', etcd_peer_url))[0].ID) }}
```

If `etcd_peer_url` is not in the member list, `selectattr(...)` returns an empty list, the `[0]` access yields undefined, and the task aborts.

## Context
- Affected versions: v2.29.0, v2.29.1, v2.30.0.
- Fixed versions: v2.29.2 and v2.30.1. The release-2.29 backport (#12960) merged 2026-02-05, which is AFTER the v2.29.1 tag (2025-12-11) and after v2.30.0 (2026-01-30) — so the fix is NOT present in v2.29.1 or v2.30.0 themselves; it lands in the future patches v2.29.2 and v2.30.1.
- Trigger: removal run where `etcd_peer_url` is no longer present in `etcdctl member list`.

## Diagnostics
In both the v2.29.1 and v2.30.0 tags, `roles/remove-node/remove-etcd-node/tasks/main.yml` (line 24) contains the expression `selectattr('peerURLs.0', '==', etcd_peer_url))[0].ID` with no guarding `when`. The code is identical to the vulnerable v2.29.1 version, so v2.30.0 is affected. The code fully matches Issue #12947.

## Known Issues
Root cause: the "Remove member from cluster" task (`roles/remove-node/remove-etcd-node/tasks/main.yml`) does not check whether the etcd member is present in the cluster before computing its ID and calling `etcdctl member remove`. There is no `when` condition handling the already-removed-member case.

Fix: PR #12949 (merged to master, "Fixes #12947") makes etcd member removal idempotent. Backport to release-2.29 is PR #12960.

Workaround on v2.29.1 / v2.30.0: do not re-run removal for an already-removed node; if needed, remove etcd members manually and verify that `etcd_peer_url` is present in the output of `etcdctl member list` before running.

## References
- https://github.com/kubernetes-sigs/kubespray/pull/12949
- Migrated from Kubepedia 0.1.0 cache: etcd-remove-node-not-idempotent-v2.29.1.md, etcd-remove-node-not-idempotent-v2.30.0.md
