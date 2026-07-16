---
id: COMPONENT-COREDNS
type: component
title: CoreDNS
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=1.11.3 <=1.12.4"
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - coredns
tags:
  - dns
  - coredns
  - addons
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    lines: "277-279 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "coredns_supported_versions, coredns_version, coredns_image_repo/tag"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "128"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "dns_mode: coredns (default)"
relations:
  - type: depends_on
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
---

# CoreDNS

## Summary

CoreDNS is the in-cluster DNS server Kubespray deploys by default
(`dns_mode: coredns`). Its version is derived from the target Kubernetes minor
line, so — like etcd — it moves with `kube_version` and can differ between minors
within one Kubespray release.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- Deployed when `dns_mode` is `coredns` (the default) or `coredns_dual`
  (dual-stack).
- The version depends on [[CONCEPT-KUBERNETES_VERSION_SUPPORT]] via
  `kube_major_version`.

## Implementation

The version is derived
(`roles/kubespray_defaults/defaults/main/download.yml`):

```yaml
coredns_version: "{{ coredns_supported_versions[kube_major_version] }}"
coredns_image_repo: "{{ kube_image_repo }}{{ '/coredns' if coredns_version is version('1.7.1', '>=') else '' }}/coredns"
coredns_image_tag: "{{ 'v' if coredns_version is version('1.7.1', '>=') else '' }}{{ coredns_version }}"
```

`coredns_supported_versions` maps each supported Kubernetes minor to a CoreDNS
version. Resolution per tag and minor:

| Kubespray | Kubernetes minor | CoreDNS version |
|-----------|------------------|-----------------|
| v2.29.0   | 1.31             | 1.11.3          |
| v2.29.0   | 1.32             | 1.11.3          |
| v2.29.0   | 1.33             | 1.12.0          |
| v2.30.0   | 1.32             | 1.11.3          |
| v2.30.0   | 1.33             | 1.12.0          |
| v2.30.0   | 1.34             | 1.12.1          |
| v2.31.0   | 1.33             | 1.12.0          |
| v2.31.0   | 1.34             | 1.12.1          |
| v2.31.0   | 1.35             | 1.12.4          |

With each tag's default `kube_version` the deployed CoreDNS is `1.12.0`
(v2.29.0 and v2.29.1 — both default to Kubernetes minor 1.33), `1.12.1`
(v2.30.0), and `1.12.4` (v2.31.0). The patch release v2.29.1 keeps the same
`coredns_supported_versions` map as v2.29.0.

The image is `registry.k8s.io/coredns/coredns:v{{ coredns_version }}`
(`kube_image_repo` = `registry.k8s.io`; the `/coredns` path and `v` tag prefix
apply for CoreDNS `>=1.7.1`, which all these versions satisfy).

## Configuration

- Version selection: `coredns_version`, `coredns_supported_versions`
  (`kubespray_defaults`).
- Image: `coredns_image_repo` = `registry.k8s.io/coredns/coredns`,
  `coredns_image_tag` = `v{{ coredns_version }}`.
- Mode: `dns_mode` (`coredns` default; `coredns_dual` for dual-stack) selects
  whether and how CoreDNS is deployed.
- Deployed by the `roles/kubernetes-apps` DNS manifests.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: CoreDNS `1.11.3`–`1.12.4` depending on the
  Kubernetes minor.
- Because the version is keyed by `kube_major_version`, changing `kube_version`
  within a release can change the CoreDNS version (contrast the literal
  [[COMPONENT-CILIUM]]).

## References

- `roles/kubespray_defaults/defaults/main/download.yml` (`coredns_supported_versions`,
  `coredns_version`, `coredns_image_repo`, `coredns_image_tag`) — lines shift by
  tag (277–279 in v2.31.0).
- `roles/kubespray_defaults/defaults/main/main.yml` (`dns_mode`).
- Tags: v2.29.0 `9991412`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
