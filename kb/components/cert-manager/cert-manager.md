---
id: COMPONENT-CERT_MANAGER
type: component
title: cert-manager
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "1.15.3"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cert-manager
tags:
  - certificates
  - ingress
  - tls
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "cert_manager_version and cert_manager_*_image_repo/tag"
relations:
  - type: see_also
    target: CONCEPT-CLUSTER_PKI
  - type: see_also
    target: CONCEPT-HELM_IN_KUBESPRAY
---

# cert-manager

## Summary
cert-manager is a Kubernetes add-on that automates the issuance and renewal of TLS certificates from various sources (ACME/Let's Encrypt, internal CA, etc.). In Kubespray it is deployed as an optional cluster application (a set of Deployments plus its CRDs) into the cluster. It is disabled by default (`cert_manager_enabled: false`) and is pinned to a fixed version. Across all indexed tags (v2.29.0 through v2.31.0) the version is `1.15.3` and does not change.

## Context
This document covers Kubespray tags v2.29.0, v2.29.1, v2.30.0, and v2.31.0. cert-manager is opt-in: the enable flag `cert_manager_enabled` defaults to `false` (defined both in `roles/kubespray_defaults/defaults/main/main.yml` and used as the download/deploy gate in `roles/kubespray_defaults/defaults/main/download.yml`). When enabled it is applied by the `roles/kubernetes-apps/ingress_controller/cert_manager` role, whose manifests (`cert-manager.yml.j2`, `cert-manager.crds.yml.j2`) template the version into the deployed objects. The container images are pulled from the Quay registry (`quay_image_repo`).

## Implementation
The version is a hard-coded literal in the kubespray_defaults download definitions:

```yaml
cert_manager_version: "1.15.3"
```

The three component images derive their tag from that variable:

```yaml
cert_manager_controller_image_repo: "{{ quay_image_repo }}/jetstack/cert-manager-controller"
cert_manager_controller_image_tag: "v{{ cert_manager_version }}"
cert_manager_cainjector_image_repo: "{{ quay_image_repo }}/jetstack/cert-manager-cainjector"
cert_manager_cainjector_image_tag: "v{{ cert_manager_version }}"
cert_manager_webhook_image_repo: "{{ quay_image_repo }}/jetstack/cert-manager-webhook"
cert_manager_webhook_image_tag: "v{{ cert_manager_version }}"
```

Per-tag concrete version (line numbers are of `cert_manager_version` in `roles/kubespray_defaults/defaults/main/download.yml`):

| Kubespray tag | commit  | cert_manager_version | line |
|---------------|---------|----------------------|------|
| v2.29.0       | 9991412 | 1.15.3               | 318  |
| v2.29.1       | 0c6a295 | 1.15.3               | 320  |
| v2.30.0       | f4ccdb5 | 1.15.3               | 321  |
| v2.31.0       | 1c9add4 | 1.15.3               | 308  |

Image tag resolves to `v1.15.3` for the controller, cainjector, and webhook images.

## Configuration
- Enable flag: `cert_manager_enabled` — default `false` (`roles/kubespray_defaults/defaults/main/main.yml`).
- Version variable: `cert_manager_version` — default `"1.15.3"` (`roles/kubespray_defaults/defaults/main/download.yml`).
- Image variables (repo / tag):
  - `cert_manager_controller_image_repo` = `{{ quay_image_repo }}/jetstack/cert-manager-controller`, tag `v{{ cert_manager_version }}`
  - `cert_manager_cainjector_image_repo` = `{{ quay_image_repo }}/jetstack/cert-manager-cainjector`, tag `v{{ cert_manager_version }}`
  - `cert_manager_webhook_image_repo` = `{{ quay_image_repo }}/jetstack/cert-manager-webhook`, tag `v{{ cert_manager_version }}`

## Compatibility
| Kubespray tag | component version |
|---------------|-------------------|
| v2.29.0       | 1.15.3            |
| v2.29.1       | 1.15.3            |
| v2.30.0       | 1.15.3            |
| v2.31.0       | 1.15.3            |

Version is unchanged across the indexed range. Applicable to the Kubernetes releases supported by these Kubespray tags (approximately 1.31–1.35).

## References
- roles/kubespray_defaults/defaults/main/download.yml (cert_manager_version, image repo/tag)
- roles/kubespray_defaults/defaults/main/main.yml (cert_manager_enabled default)
- roles/kubernetes-apps/ingress_controller/cert_manager/ (deploy role and templates)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
