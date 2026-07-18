---
id: TROUBLE-K8S_GITREPO_VOLUME_REMOVED
type: troubleshooting
title: "gitRepo volume no longer works — driver disabled by default (K8s 1.33)"
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: ">=1.33 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - gitRepo volume disabled
  - GitRepoVolumeDriver
  - gitRepo volume deprecated removed
  - pod gitRepo volume fails 1.33
tags:
  - kubernetes
  - troubleshooting
  - storage
  - security
sources:
  - type: code
    path: keps/sig-storage/5040-remove-gitrepo-driver
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-storage/5040-remove-gitrepo-driver
    note: "kep.yaml: GitRepoVolumeDriver gate off-by-default 1.33 (removal track)"
relations:
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: CONCEPT-K8S_FEATURE_GATES
---

# gitRepo volume no longer works — driver disabled by default (K8s 1.33)

## Summary

The **`gitRepo` volume** type (which cloned a Git repo into a pod volume at start) has been a security
liability for years and is now on the removal track: the `GitRepoVolumeDriver` feature gate is
**off by default from K8s 1.33** (Kubespray v2.31.0). Pods that use a `gitRepo` volume **fail** on
clusters at 1.33+ unless the gate is temporarily re-enabled. Migrate to an init container that clones
the repo instead.

## Problem

- After upgrading to Kubespray v2.31.0 (K8s 1.33+), pods with a `spec.volumes[].gitRepo` **fail to
  start** / the volume is rejected.
- Legacy manifests or charts that used `gitRepo` to seed content no longer work.

## Context

- Milestone (`keps/sig-storage/5040-...` kep.yaml): `GitRepoVolumeDriver` gate **off by default 1.33**
  (removal path). It was deprecated long ago; the driver could execute Git hooks with the kubelet's
  privileges — a real attack surface.
- Applies at **K8s 1.33+** → Kubespray **v2.31.0**; earlier tags (≤1.32) still allow it.

## Diagnostics

- Find users: `kubectl get pods -A -o json | grep -l '"gitRepo"'` (or grep your manifests/Helm charts
  for `gitRepo:`).
- Confirm the K8s minor (`kubectl version`) — ≥1.33 means the driver is off by default.

## Known Issues

- **Fix (correct):** replace the `gitRepo` volume with an **init container** that runs `git clone` into
  an `emptyDir` shared with the main container — this is the documented, safe replacement.
- **Temporary bridge:** the `GitRepoVolumeDriver` feature gate can be re-enabled to buy migration time
  ([[CONCEPT-K8S_FEATURE_GATES]]), but it is on the removal track — do not treat re-enabling as a
  durable fix.
- **Pre-upgrade audit:** grep for `gitRepo` volumes before v2.31.0 and convert them
  ([[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]).

## References

- `keps/sig-storage/5040-remove-gitrepo-driver` (kep.yaml off-by-default 1.33). Silent changes
  [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]; gates [[CONCEPT-K8S_FEATURE_GATES]].
