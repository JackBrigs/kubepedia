---
id: COMPONENT-ARGOCD
type: component
title: argocd
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=2.14.20 <=2.14.21"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - argocd
tags:
  - gitops
  - cd
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "argocd_version computed from argocd_install_checksums.no_arch"
relations: []
---

# argocd

## Summary
Argo CD is a declarative, GitOps continuous-delivery tool for Kubernetes. In Kubespray it is deployed as an optional cluster application by applying the upstream Argo CD install manifest into the cluster. It is disabled by default (`argocd_enabled: false`). Unlike image-based add-ons, Argo CD is not pinned via an `*_image_repo`/`*_image_tag` pair; instead Kubespray downloads and applies the upstream `install.yaml` manifest for the selected version. The effective version is derived from the checksums table and ranges from `2.14.20` (v2.29.0) to `2.14.21` (v2.29.1 onward).

## Context
This document covers Kubespray tags v2.29.0, v2.29.1, v2.30.0, and v2.31.0. Argo CD is opt-in: `argocd_enabled` defaults to `false` (defined in both `roles/kubernetes-apps/argocd/defaults/main.yml` and `roles/kubespray_defaults/defaults/main/main.yml`). When enabled, the `download` definition `argocd_install` in `roles/kubespray_defaults/defaults/main/download.yml` fetches the upstream manifest and the `roles/kubernetes-apps/argocd` role applies it into the `argocd` namespace (`argocd_namespace: argocd`).

Note on version precedence: the Argo CD role default `roles/kubernetes-apps/argocd/defaults/main.yml` also declares a literal `argocd_version: 2.14.5`. That literal is not consistent with the checksums table (which only contains 2.14.18–2.14.21) and the install-checksum lookup `argocd_install_checksums.no_arch[argocd_version]` requires a key that exists in the table; therefore the effective, checksum-consistent value is the computed one from `download.yml` recorded below.

## Implementation
The version is computed as the first (newest) key of the `no_arch` checksums map:

```yaml
argocd_version: "{{ (argocd_install_checksums.no_arch | dict2items)[0].key }}"
argocd_install_url: "https://raw.githubusercontent.com/argoproj/argo-cd/v{{ argocd_version }}/manifests/install.yaml"
argocd_install_checksum: "{{ argocd_install_checksums.no_arch[argocd_version] }}"
```

The `argocd_install_checksums.no_arch` table lives in `roles/kubespray_defaults/vars/main/checksums.yml`; the first-listed key is the resolved version.

Per-tag concrete version (first key of `argocd_install_checksums.no_arch`):

| Kubespray tag | commit  | argocd_version | first checksum key |
|---------------|---------|----------------|--------------------|
| v2.29.0       | 9991412 | 2.14.20        | 2.14.20            |
| v2.29.1       | 0c6a295 | 2.14.21        | 2.14.21            |
| v2.30.0       | f4ccdb5 | 2.14.21        | 2.14.21            |
| v2.31.0       | 1c9add4 | 2.14.21        | 2.14.21            |

Argo CD has no image repo/tag variables in Kubespray; it is installed from the upstream manifest referenced by `argocd_install_url`.

## Configuration
- Enable flag: `argocd_enabled` — default `false` (`roles/kubernetes-apps/argocd/defaults/main.yml` and `roles/kubespray_defaults/defaults/main/main.yml`).
- Version variable: `argocd_version` — computed default = newest key of `argocd_install_checksums.no_arch` (`roles/kubespray_defaults/defaults/main/download.yml`). A conflicting literal `2.14.5` in the argocd role defaults is overridden/inconsistent with the checksums table.
- Namespace: `argocd_namespace` — default `argocd`.
- Install source: `argocd_install_url` = `https://raw.githubusercontent.com/argoproj/argo-cd/v{{ argocd_version }}/manifests/install.yaml` (no image_repo/image_tag vars).
- Optional: `argocd_admin_password` (commented out by default).

## Compatibility
| Kubespray tag | component version |
|---------------|-------------------|
| v2.29.0       | 2.14.20           |
| v2.29.1       | 2.14.21           |
| v2.30.0       | 2.14.21           |
| v2.31.0       | 2.14.21           |

Version changes once (2.14.20 → 2.14.21 between v2.29.0 and v2.29.1) and is stable thereafter. Applicable to the Kubernetes releases supported by these Kubespray tags (approximately 1.31–1.35).

## References
- roles/kubespray_defaults/defaults/main/download.yml (argocd_version, argocd_install_url, argocd_install_checksum)
- roles/kubespray_defaults/vars/main/checksums.yml (argocd_install_checksums)
- roles/kubernetes-apps/argocd/defaults/main.yml (argocd_enabled, argocd_namespace, literal argocd_version)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
