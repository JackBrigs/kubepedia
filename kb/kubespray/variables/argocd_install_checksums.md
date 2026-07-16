---
id: VARIABLE-ARGOCD_INSTALL_CHECKSUMS
type: variable
title: argocd_install_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - argocd_install_checksums
tags:
  - argocd
  - checksums
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Maps ArgoCD install manifest versions to their sha256 checksums under a no_arch key."
relations: []
---

# argocd_install_checksums

## Summary
A version-keyed mapping that pins the sha256 checksum of the ArgoCD install manifest for each supported ArgoCD version. It is nested under a single `no_arch` key (the manifest is architecture-independent) and is consumed when the ArgoCD addon is enabled. It is not a scalar default but a lookup table of `<argocd_version>: sha256:<hash>` entries.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml` as `argocd_install_checksums:` with a `no_arch:` sub-mapping. The set of entries grows between tags while previously listed checksums stay identical:

| Tag | Highest ArgoCD version listed |
|-----|-------------------------------|
| v2.29.0 | 2.14.20 |
| v2.29.1 | 2.14.21 |
| v2.30.0 | 2.14.21 |
| v2.31.0 | 2.14.21 |

Example verbatim entry (present in all four tags): `2.14.20: sha256:747db8bb6d1591b49bb6266412e6dcaccf3c7bd3bd81ef7d63b0ab5bfe6af951`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. The map is keyed by ArgoCD version, so the effective checksum is selected via the configured `argocd_version`. Related variables: `argocd_version`, `argocd_install_url`, `argocd_enabled`.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
