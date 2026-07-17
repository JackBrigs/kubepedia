---
id: TROUBLE-CILIUM_OPERATOR_GENERIC_OFFLINE_REGISTRY
type: troubleshooting
title: "Cilium operator image mismatch in offline registry (operator vs operator-generic)"
status: active
kubespray_version: ">=v2.30.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - cilium-operator-generic-offline
tags:
  - cilium
  - offline
  - registry
sources:
  - type: github_pr
    url: https://github.com/kubernetes-sigs/kubespray/pull/13270
    note: "Fix merged after v2.31.0: sets cilium_operator_image_repo to cilium/operator-generic and pins operator.image.override"
  - type: github_issue
    url: https://github.com/kubernetes-sigs/kubespray/issues/13252
    note: "Original issue report"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# Cilium operator image mismatch in offline registry (operator vs operator-generic)

## Summary
When deploying from an offline registry, the cilium-operator pod enters CrashLoopBackOff with `exec: "cilium-operator-generic": executable file not found in $PATH`. Kubespray syncs `quay.io/cilium/operator`, but the Cilium Helm chart appends a `-generic` suffix for non-cloud installs and requests `cilium/operator-generic`, which is absent from the registry. Workaround: also push `cilium/operator-generic` to the offline registry, or override `cilium_operator_image_repo`.

## Problem
On an offline / air-gapped deployment the `cilium-operator` pod fails to start and loops in CrashLoopBackOff because the container command `cilium-operator-generic` is not found. This happens because the image actually pulled does not contain the generic operator binary the chart expects.

## Context
- Affected Kubespray versions: v2.30.0, v2.31.0.
- Fixed versions: none released yet — the fix was merged to master after the v2.31.0 tag and will land in a future release (v2.31.1 / v2.32.0). Not fixed in v2.31.0.
- Trigger conditions: deploying Cilium from an offline registry (non-cloud install path where the Helm chart adds the `-generic` suffix).

## Diagnostics
- Inspect the operator pod: `kubectl -n kube-system get pods -l name=cilium-operator` shows CrashLoopBackOff.
- Pod logs / events show `exec: "cilium-operator-generic": executable file not found in $PATH`.
- Verify the default in the tag: `roles/kubespray_defaults/defaults/main/download.yml:237` sets `cilium_operator_image_repo: "{{ quay_image_repo }}/cilium/operator"` — the value ends with `cilium/operator` (no `-generic`), so the chart adds `-generic` and the image is not found in the registry.

## Known Issues
- Root cause: Kubespray syncs the `quay.io/cilium/operator` image into the offline registry, but the Cilium Helm chart for non-cloud installations automatically appends the `-generic` suffix and requests `cilium/operator-generic`, which was never mirrored.
- Fix: PR #13270 (merged 2026-06-22, after the v2.31.0 tag) changes `cilium_operator_image_repo` to `cilium/operator-generic` and adds `operator.image.override` to the Helm values so the chart does not append the suffix again. Related issue: #13252.
- Workaround on v2.31.0: manually push the `cilium/operator-generic` image into the offline registry (in addition to `cilium/operator`), or override `cilium_operator_image_repo`.

## References
- https://github.com/kubernetes-sigs/kubespray/pull/13270
- https://github.com/kubernetes-sigs/kubespray/issues/13252
- Migrated from Kubepedia 0.1.0 cache: cilium-operator-generic-offline-registry-v2.31.0.md
