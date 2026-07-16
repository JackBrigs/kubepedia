---
id: VARIABLE-NODELOCALDNS_IMAGE_TAG
type: variable
title: nodelocaldns_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nodelocaldns_image_tag
tags:
  - nodelocaldns
  - dns
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Image tag for the nodelocaldns container, derived from nodelocaldns_version"
relations:
  - type: see_also
    target: COMPONENT-NODELOCALDNS
---

# nodelocaldns_image_tag

## Summary
Container image tag for nodelocaldns (k8s-dns-node-cache). It is derived from `nodelocaldns_version`. Default expression: `{{ nodelocaldns_version }}`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
nodelocaldns_image_tag: "{{ nodelocaldns_version }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0. The resolved tag depends on the value of `nodelocaldns_version` in each tag.

## Compatibility
Kubespray range: `>=v2.29.0 <=v2.31.0`. Depends on `nodelocaldns_version`. Paired with `nodelocaldns_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
