---
id: VARIABLE-AWS_EBS_CSI_ENABLED
type: variable
title: aws_ebs_csi_enabled
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - aws_ebs_csi_enabled
tags:
  - aws
  - csi
  - storage
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Toggles the AWS EBS CSI driver; default false"
relations: []
---

# aws_ebs_csi_enabled

## Summary
Toggles deployment of the AWS EBS CSI (Container Storage Interface) driver. Default is `false`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml`:
```yaml
aws_ebs_csi_enabled: false
```
It is also exposed (commented, `true`) as an example in `inventory/sample/group_vars/all/aws.yml`. The default value `false` is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (only the line number varies).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related to `aws_ebs_csi_plugin_image_repo`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
