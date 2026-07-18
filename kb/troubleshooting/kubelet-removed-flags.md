---
id: TROUBLE-K8S_KUBELET_REMOVED_FLAGS
type: troubleshooting
title: "kubelet fails to start after upgrade — removed flags (--keep-terminated-pod-volumes 1.31, --cloud-config 1.34, --pod-infra-container-image 1.35)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - kubelet won't start after upgrade unknown flag
  - keep-terminated-pod-volumes removed
  - pod-infra-container-image removed
  - kubelet cloud-config removed
  - kubelet flag removed crashloop
  - kubelet extra args removed flag
tags:
  - kubernetes
  - troubleshooting
  - kubelet
  - upgrade
sources:
  - type: docs
    path: CHANGELOG/CHANGELOG-1.31.md, 1.34.md, 1.35.md
    url: https://github.com/kubernetes/kubernetes/tree/master/CHANGELOG
    note: "Urgent Upgrade Notes: --keep-terminated-pod-volumes removed 1.31 (#122082); --cloud-config removed 1.34 (#130161); --pod-infra-container-image removed 1.35 (#133779)"
relations:
  - type: see_also
    target: CONCEPT-K8S_URGENT_UPGRADE_NOTES
  - type: see_also
    target: CONCEPT-ESCAPE_HATCHES
  - type: see_also
    target: PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR
---

# kubelet fails to start after upgrade — removed flags (--keep-terminated-pod-volumes 1.31, --cloud-config 1.34, --pod-infra-container-image 1.35)

## Summary

The kubelet **refuses to start** if it's passed a command-line flag that the new version **removed**.
Across the Kubespray range three long-deprecated kubelet flags were dropped:
**`--keep-terminated-pod-volumes`** (removed **1.31**), **`--cloud-config`** (removed **1.34**), and
**`--pod-infra-container-image`** (removed **1.35**). If any of these is still in the node's kubelet
args / `kubelet_custom_flags` / extra-args, the kubelet **crash-loops** with an unknown-flag error
after the upgrade — a classic "node NotReady after upgrade" cause.

## Problem

- After a Kubespray upgrade, a node goes `NotReady`; `systemctl status kubelet` / the kubelet log shows
  **`unknown flag: --<name>`** or `failed to parse kubelet flag`.
- The node's kubelet won't come up until the offending flag is removed.

## Context

- Removed flags by version (Urgent Upgrade Notes — [[CONCEPT-K8S_URGENT_UPGRADE_NOTES]]):
  - **`--keep-terminated-pod-volumes`** — removed **K8s 1.31** (Kubespray v2.29.0) (#122082).
  - **`--cloud-config`** — removed **K8s 1.34** (#130161).
  - **`--pod-infra-container-image`** — removed **K8s 1.35** (#133779). kubeadm does **not** strip it
    if it was passed as an extra kubelet arg.
- Kubespray sets kubelet flags via named vars and the `kubelet_custom_flags` / extra-args escape
  hatches ([[CONCEPT-ESCAPE_HATCHES]]); a stale inventory carrying one of these into the kubelet env
  file is the usual source.

## Diagnostics

- On the failing node: `journalctl -u kubelet -n 50` → the `unknown flag: --…` line names the culprit.
- Find where it's set: check `/etc/kubernetes/kubelet.env` / the kubelet systemd unit / drop-ins on the
  node, and grep your Kubespray inventory (`group_vars`/`host_vars`) for `keep-terminated-pod-volumes`,
  `cloud-config`, `pod-infra-container-image`, and `kubelet_custom_flags`.

## Known Issues

- **Fix:** remove the dropped flag from inventory (`kubelet_custom_flags` / any `*_extra_args`) and from
  the node's kubelet env, then restart kubelet / re-run the node. For `--pod-infra-container-image`,
  the equivalent is now the runtime's sandbox image config (containerd `sandbox_image`), not a kubelet
  flag.
- **Pre-upgrade audit (the real fix):** before crossing 1.31 / 1.34 / 1.35, grep the inventory for
  these flags and remove them ([[CONCEPT-K8S_URGENT_UPGRADE_NOTES]], [[PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR]]).
  Removed kubelet flags are the #1 "kubelet won't start after upgrade" cause across this range.

## References

- Kubernetes `CHANGELOG/CHANGELOG-{1.31,1.34,1.35}.md` Urgent Upgrade Notes (@master). Curated notes
  [[CONCEPT-K8S_URGENT_UPGRADE_NOTES]]; escape hatches [[CONCEPT-ESCAPE_HATCHES]]; upgrade runbook
  [[PRACTICE-RUNBOOK_UPGRADE_ONE_MINOR]].
