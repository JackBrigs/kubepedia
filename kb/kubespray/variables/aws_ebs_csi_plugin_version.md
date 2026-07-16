---
id: VARIABLE-AWS_EBS_CSI_PLUGIN_VERSION
type: variable
title: aws_ebs_csi_plugin_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - aws_ebs_csi_plugin_version
tags:
  - csi
  - aws
  - download
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Default aws_ebs_csi_plugin_version: \"0.5.0\""
relations: []
---

# aws_ebs_csi_plugin_version

## Summary
Version of the AWS EBS CSI driver deployed by Kubespray. Default is `0.5.0`. It also feeds `aws_ebs_csi_plugin_image_tag` via `"v{{ aws_ebs_csi_plugin_version }}"`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
aws_ebs_csi_plugin_version: "0.5.0"
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Consumed by `aws_ebs_csi_plugin_image_tag`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
