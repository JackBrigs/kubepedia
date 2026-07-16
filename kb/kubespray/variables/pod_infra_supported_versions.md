---
id: VARIABLE-POD_INFRA_SUPPORTED_VERSIONS
type: variable
title: pod_infra_supported_versions
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - pod_infra_supported_versions
tags:
  - download
  - images
sources:
  - type: code
    path: roles/kubespray_defaults/vars/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/vars/main/main.yml
    note: "Maps each supported Kubernetes major version to the pause (pod infra) image version"
relations: []
---

# pod_infra_supported_versions

## Summary
Mapping from Kubernetes major version (e.g. `1.33`) to the pause / pod-infra image version to use. `pod_infra_version` indexes into this map, and the set of keys/values changes with each release as new Kubernetes versions are supported.

## Implementation
Defined in `roles/kubespray_defaults/vars/main/main.yml` (line 9). The map differs between tags:

| Tag | Contents |
| --- | --- |
| v2.29.0, v2.29.1 | `'1.33': '3.10'`, `'1.32': '3.10'`, `'1.31': '3.10'` |
| v2.30.0 | `'1.34': '3.10.1'`, `'1.33': '3.10'`, `'1.32': '3.10'` |
| v2.31.0 | `'1.35': '3.10.1'`, `'1.34': '3.10.1'`, `'1.33': '3.10'` |

## Compatibility
Kubespray v2.29.0 through v2.31.0 (values change per release). Consumed by `pod_infra_version: "{{ pod_infra_supported_versions[kube_major_version] }}"`, which in turn drives `pod_infra_image_tag`.

## References
- roles/kubespray_defaults/vars/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
