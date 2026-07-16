---
id: VARIABLE-GATEWAY_API_STANDARD_CRDS_CHECKSUMS
type: variable
title: gateway_api_standard_crds_checksums
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - gateway_api_standard_crds_checksums
tags:
  - gateway-api
  - checksums
  - crds
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/checksums.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/checksums.yml
    note: "Maps Gateway API standard-channel CRD versions to their sha256 checksums under a no_arch key."
relations: []
---

# gateway_api_standard_crds_checksums

## Summary
A version-keyed mapping that pins the sha256 checksum of the Gateway API standard-channel CRD manifest for each supported version. It is nested under a single `no_arch` key (the manifest is architecture-independent). From v2.30.0 its first (highest) key also determines the effective `gateway_api_version`.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/checksums.yml` as `gateway_api_standard_crds_checksums:` with a `no_arch:` sub-mapping. The set of entries grows between tags while previously listed checksums stay identical:

| Tag | Highest version listed |
|-----|------------------------|
| v2.29.0 | 1.2.1 |
| v2.29.1 | 1.2.1 |
| v2.30.0 | 1.4.1 |
| v2.31.0 | 1.5.1 |

Example verbatim entry (present in all four tags): `1.2.1: sha256:97598bf6ab3b33b9b5c5432bdd24de091e4e9c3aa0575ebb0710a2a19cd64d64`.

## Compatibility
Kubespray v2.29.0 through v2.31.0. The effective checksum is selected via the configured `gateway_api_version`. Related variables: `gateway_api_version`, `gateway_api_experimental_crds_checksums`, `gateway_api_enabled`, `gateway_api_channel`.

## References
- roles/kubespray_defaults/vars/main/checksums.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
