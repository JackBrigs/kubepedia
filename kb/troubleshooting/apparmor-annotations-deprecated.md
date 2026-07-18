---
id: TROUBLE-K8S_APPARMOR_ANNOTATIONS_DEPRECATED
type: troubleshooting
title: "AppArmor annotations deprecated — move to securityContext.appArmorProfile (API GA 1.31)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - apparmor annotation deprecated
  - container.apparmor.security.beta.kubernetes.io
  - appArmorProfile securityContext
  - apparmor GA kubernetes 1.31
tags:
  - kubernetes
  - troubleshooting
  - security
  - node
sources:
  - type: code
    path: keps/sig-node/24-apparmor
    url: https://github.com/kubernetes/enhancements/tree/master/keps/sig-node/24-apparmor
    note: "kep.yaml: AppArmor API stable/GA 1.31; annotation form deprecated"
relations:
  - type: see_also
    target: CONCEPT-POD_SECURITY_STANDARDS
  - type: see_also
    target: CONCEPT-K8S_UPGRADE_SILENT_CHANGES
  - type: see_also
    target: PRACTICE-CLUSTER_HARDENING
---

# AppArmor annotations deprecated — move to securityContext.appArmorProfile (API GA 1.31)

## Summary

AppArmor moved from **annotations** to a **first-class API field**: the AppArmor API reached **GA in
K8s 1.31**, and the old
`container.apparmor.security.beta.kubernetes.io/<container>: <profile>` **annotation form is
deprecated**. Set the profile in **`securityContext.appArmorProfile`** (pod or container) instead.
Manifests still using the annotation keep working for now but should be migrated; the annotation will
eventually stop being honored.

## Problem

- Deprecation warnings on pods carrying `container.apparmor.security.beta.kubernetes.io/*` annotations.
- Planning forward: unsure how to declare an AppArmor profile without the annotation.
- A Pod Security / policy tool flags the annotation as outdated.

## Context

- Milestone (`keps/sig-node/24-apparmor` kep.yaml): AppArmor API **GA 1.31** (Kubespray v2.29.0+); the
  annotation is the pre-GA form and is deprecated.
- **New form:** `securityContext.appArmorProfile: { type: RuntimeDefault | Localhost | Unconfined,
  localhostProfile: <name> }` at pod or container level. Requires AppArmor-enabled nodes (kernel LSM).

## Diagnostics

- Find annotation users: `kubectl get pods -A -o json | grep -l 'container.apparmor.security.beta.kubernetes.io'`
  (or via your manifests/Helm charts).
- Check node support: AppArmor must be enabled in the kernel/LSM on the node.

## Known Issues

- **Fix:** replace the annotation with `securityContext.appArmorProfile` in pod specs / templates
  (Deployments, StatefulSets, Helm charts). A pod using `RuntimeDefault` is the common baseline.
- **PSA/hardening:** AppArmor is part of a hardened node posture ([[CONCEPT-POD_SECURITY_STANDARDS]],
  [[PRACTICE-CLUSTER_HARDENING]]); the GA field is the supported way to require it going forward.
- **Timeline:** the annotation still works across the current range but treat it as tech debt to clear
  ([[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]]).

## References

- `keps/sig-node/24-apparmor` (kep.yaml API GA 1.31). PSA [[CONCEPT-POD_SECURITY_STANDARDS]]; hardening
  [[PRACTICE-CLUSTER_HARDENING]]; silent changes [[CONCEPT-K8S_UPGRADE_SILENT_CHANGES]].
