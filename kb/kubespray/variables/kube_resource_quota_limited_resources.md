---
id: VARIABLE-KUBE_RESOURCE_QUOTA_LIMITED_RESOURCES
type: variable
title: kube_resource_quota_limited_resources
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_resource_quota_limited_resources
tags:
  - control-plane
  - resource-quota
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines the default empty list []; consumed by templates/resourcequota.yaml.j2"
relations: []
---

# kube_resource_quota_limited_resources

## Summary
Defines the `limitedResources` entries of the cluster-wide ResourceQuota object that Kubespray can render. The default is an empty list `[]`, which disables emitting any `limitedResources` block. When set to a non-empty list it is injected verbatim into `resourcequota.yaml.j2`.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
kube_resource_quota_limited_resources: []
```

A commented example precedes it in the same file. It is consumed in `roles/kubernetes/control-plane/templates/resourcequota.yaml.j2` via `{% if kube_resource_quota_limited_resources | d(false) -%}` and rendered with `to_nice_yaml`. The default value `[]` and the file path are unchanged across v2.29.0-v2.31.0 (only the surrounding line numbers shift: line 134 in v2.29.0/v2.29.1, line 137 in v2.30.0/v2.31.0).

## Compatibility
Kubespray `>=v2.29.0 <=v2.31.0`. Related to the ResourceQuota feature toggled via `resource_quota_enabled` and the `resourcequota.yaml.j2` template.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- roles/kubernetes/control-plane/templates/resourcequota.yaml.j2
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
