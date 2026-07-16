---
id: VARIABLE-OPENSTACK_BLOCKSTORAGE_IGNORE_VOLUME_AZ
type: variable
title: openstack_blockstorage_ignore_volume_az
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - openstack_blockstorage_ignore_volume_az
tags:
  - openstack
  - storage
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Whether to ignore the volume availability zone for OpenStack block storage; derived from volume_cross_zone_attachment, default 'false'."
relations: []
---

# openstack_blockstorage_ignore_volume_az

## Summary
Configures the OpenStack cloud provider to ignore the availability zone of a volume when attaching block storage. The value is derived from `volume_cross_zone_attachment`, defaulting to the string `'false'`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as a computed default:

```yaml
openstack_blockstorage_ignore_volume_az: "{{ volume_cross_zone_attachment | default('false') }}"
```

The expression is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line number drifts from 470 in v2.29.0 to 478 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Applies to the OpenStack cloud provider integration. Related variables: `volume_cross_zone_attachment`, `openstack_cacert`, `openstack_lbaas_enabled`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
