---
id: VARIABLE-AWS_EBS_CSI_PLUGIN_IMAGE_TAG
type: variable
title: aws_ebs_csi_plugin_image_tag
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - aws_ebs_csi_plugin_image_tag
tags:
  - csi
  - aws
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Effective default aws_ebs_csi_plugin_image_tag: \"v{{ aws_ebs_csi_plugin_version }}\""
relations: []
---

# aws_ebs_csi_plugin_image_tag

## Summary
Image tag for the AWS EBS CSI driver container. The effective default is derived from `aws_ebs_csi_plugin_version` as `"v{{ aws_ebs_csi_plugin_version }}"`, resolving to `v0.5.0`.

## Implementation
The authoritative value lives in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
aws_ebs_csi_plugin_image_tag: "v{{ aws_ebs_csi_plugin_version }}"
```

A separate role-local default in `roles/kubernetes-apps/csi_driver/aws_ebs/defaults/main.yml` sets `aws_ebs_csi_plugin_image_tag: latest`, but the `kubespray_defaults` value has higher precedence at play time. Both definitions are unchanged across v2.29.0-v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Tied to `aws_ebs_csi_plugin_version` (default `0.5.0`).

## References
- roles/kubespray_defaults/defaults/main/download.yml
- roles/kubernetes-apps/csi_driver/aws_ebs/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
