---
id: VARIABLE-AWS_EBS_CSI_PLUGIN_IMAGE_REPO
type: variable
title: aws_ebs_csi_plugin_image_repo
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - aws_ebs_csi_plugin_image_repo
tags:
  - aws
  - csi
  - image
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Container image repository for the AWS EBS CSI driver"
relations: []
---

# aws_ebs_csi_plugin_image_repo

## Summary
Container image repository for the AWS EBS CSI driver. Default is `{{ docker_image_repo }}/amazon/aws-ebs-csi-driver`, derived from the configured `docker_image_repo`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:
```yaml
aws_ebs_csi_plugin_image_repo: "{{ docker_image_repo }}/amazon/aws-ebs-csi-driver"
```
The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number varies).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Depends on `docker_image_repo`; used when `aws_ebs_csi_enabled` is true.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
