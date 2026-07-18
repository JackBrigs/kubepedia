---
id: VARIABLE-AWS_EBS_CSI_ENABLE_VOLUME_SCHEDULING
type: variable
title: aws_ebs_csi_enable_volume_scheduling
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-18"
confidence: verified
aliases:
  - aws_ebs_csi_enable_volume_scheduling
tags:
  - kubernetes-apps
  - csi-driver
  - variable
sources:
  - type: code
    path: roles/kubernetes-apps/csi_driver/aws_ebs/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/csi_driver/aws_ebs/defaults/main.yml
    note: "default: true"
relations: []
---
<!-- generated: variable-stub -->

# aws_ebs_csi_enable_volume_scheduling

## Summary

Kubespray variable `aws_ebs_csi_enable_volume_scheduling` — default `true`. Defined in `roles/kubernetes-apps/csi_driver/aws_ebs/defaults/main.yml`. Present in Kubespray
`v2.27.0`–`v2.31.0` of the indexed range. (Source-grounded reference stub; see the file for
the exact value and surrounding context.)

## Implementation

Defined in `roles/kubernetes-apps/csi_driver/aws_ebs/defaults/main.yml` (Kubespray `v2.31.0`):

```yaml
aws_ebs_csi_enable_volume_scheduling: true
```

## Compatibility

Present in the Kubespray tags `v2.27.0`–`v2.31.0`. Read the exact per-tag value from the source
file, as defaults can change between releases.

## References

- `roles/kubernetes-apps/csi_driver/aws_ebs/defaults/main.yml` (Kubespray `v2.31.0`).
