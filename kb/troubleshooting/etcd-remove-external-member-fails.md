---
id: TROUBLE-ETCD_REMOVE_EXTERNAL_MEMBER_FAILS
type: troubleshooting
title: "etcd: removing an external (non-stacked) member aborts the remove-node playbook"
status: active
kubespray_version: "v2.29.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - etcd remove external member fails
tags:
  - etcd
  - remove-node
sources:
  - type: github_pr
    url: https://github.com/kubernetes-sigs/kubespray/pull/12685
    note: "Fix: identify the etcd member by peerURLs from etcdctl JSON output"
relations:
  - type: see_also
    target: COMPONENT-ETCD
---

# etcd: removing an external (non-stacked) member aborts the remove-node playbook

## Summary
Removing an etcd node deployed separately from the control plane (external etcd, not a Kubernetes node) aborted the removal playbook. The task "Lookup node IP in kubernetes" failed to match a Kubernetes node and stopped execution, leaving the etcd member in place. Fixed in v2.29.1 by identifying the member via `peerURLs` from `etcdctl` JSON output.

## Problem
When removing an etcd node that is deployed standalone (external etcd, the host is not part of the Kubernetes cluster), the removal playbook fails: the "Lookup node IP in kubernetes" task aborts the whole run, and the etcd member is not removed.

## Context
- Affected versions: v2.29.0 (when removing an external-etcd node).
- Fixed versions: v2.29.1.
- Trigger: the etcd node being removed is not a Kubernetes node, so the IP-to-node match finds no correspondence.

## Diagnostics
The prior logic removed the etcd member by identifying it via IP address matched against a Kubernetes node. For a standalone etcd host (not a k8s node) that lookup found no match and aborted the playbook. The match was textual and depended on several variables. Confirm against the tag code in `roles/remove-node/remove-etcd-node/tasks/main.yml`.

## Known Issues
Root cause: the member was located by IP-to-Kubernetes-node matching, which fails for external etcd hosts. Fix: PR #12685 (original #12682, commit `59b3c686a`) changed the strategy so the etcd member is now identified by `peerURLs` from the JSON output of `etcdctl`, independent of whether the etcd host is a Kubernetes cluster member and without introducing new variables. In the v2.29.1 tag, `roles/remove-node/remove-etcd-node/tasks/main.yml`:

```yaml
command: "{{ bin_dir }}/etcdctl member list -w json"
# ...
- "{{ '%x' | format(((etcd_members.stdout | from_json).members
     | selectattr('peerURLs.0', '==', etcd_peer_url))[0].ID) }}"
```

The member is selected by `peerURLs.0 == etcd_peer_url` and its ID taken from JSON. Commit `59b3c686a` is in the `v2.29.0..v2.29.1` range.

## References
- https://github.com/kubernetes-sigs/kubespray/pull/12685
- Migrated from Kubepedia 0.1.0 cache: etcd-remove-external-member-fails-v2.29.1.md
