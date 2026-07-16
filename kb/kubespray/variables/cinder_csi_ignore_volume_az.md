---
id: VARIABLE-CINDER_CSI_IGNORE_VOLUME_AZ
type: variable
title: cinder_csi_ignore_volume_az
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cinder_csi_ignore_volume_az
tags:
  - cinder
  - csi
  - openstack
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defaults to the value of volume_cross_zone_attachment, or 'false' if unset"
relations: []
---

# cinder_csi_ignore_volume_az

## Summary
Controls whether the Cinder CSI plugin ignores the volume availability zone when attaching volumes in OpenStack. Defaults to the value of `volume_cross_zone_attachment`, falling back to `'false'` when that variable is unset.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as:

```yaml
cinder_csi_ignore_volume_az: "{{ volume_cross_zone_attachment | default('false') }}"
```

This computed expression is unchanged across v2.29.0-v2.31.0 (only its line number shifts: 478 in v2.29.0/v2.29.1, 479 in v2.30.0, 486 in v2.31.0).

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Depends on `volume_cross_zone_attachment`. Relevant only for the OpenStack Cinder CSI driver.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
