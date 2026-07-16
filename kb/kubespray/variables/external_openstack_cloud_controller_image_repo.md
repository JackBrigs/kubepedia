---
id: VARIABLE-EXTERNAL_OPENSTACK_CLOUD_CONTROLLER_IMAGE_REPO
type: variable
title: external_openstack_cloud_controller_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - external_openstack_cloud_controller_image_repo
tags:
  - openstack
  - cloud-controller
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Defines the image repository for the OpenStack cloud controller manager, defaulting to {{ kube_image_repo }}/provider-os/openstack-cloud-controller-manager"
relations: []
---

# external_openstack_cloud_controller_image_repo

## Summary
Sets the container image repository for the OpenStack external cloud controller manager. Default: `{{ kube_image_repo }}/provider-os/openstack-cloud-controller-manager`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as:

```yaml
external_openstack_cloud_controller_image_repo: "{{ kube_image_repo }}/provider-os/openstack-cloud-controller-manager"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number shifts: 263, 265, 265, 259 respectively).

## Compatibility
Kubespray v2.29.0–v2.31.0. Used only when the external OpenStack cloud controller is deployed. Related: `external_openstack_cloud_controller_image_tag`, `kube_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
