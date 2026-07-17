---
id: COMPONENT-AWS_EBS_CSI
type: component
title: aws-ebs-csi
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "0.5.0"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - aws-ebs-csi
tags:
  - csi
  - storage
  - aws
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "aws_ebs_csi_plugin_version / aws_ebs_csi_plugin_image_repo / aws_ebs_csi_plugin_image_tag"
relations:
  - type: see_also
    target: CONCEPT-CSI_LAYER
---

# aws-ebs-csi

## Summary
`aws-ebs-csi` is the Amazon EBS CSI driver (`amazon/aws-ebs-csi-driver`), the Container Storage Interface plugin that provisions and manages Amazon Elastic Block Store volumes as Kubernetes PersistentVolumes. Kubespray can deploy it as an optional storage addon. It is disabled by default (`aws_ebs_csi_enabled: false`) and pinned to plugin version `0.5.0` across the indexed range.

## Context
This document covers Kubespray tags v2.29.0 through v2.31.0. The driver is opt-in: `aws_ebs_csi_enabled` defaults to `false` in every indexed tag. It is deployed by the `kubernetes-apps/csi_driver/aws_ebs` role and generally requires `persistent_volumes_enabled` (also `false` by default) plus AWS-side IAM/credentials configuration.

## Implementation
The version is defined as a plain literal in `roles/kubespray_defaults/defaults/main/download.yml`:

```yaml
aws_ebs_csi_plugin_version: "0.5.0"
aws_ebs_csi_plugin_image_repo: "{{ docker_image_repo }}/amazon/aws-ebs-csi-driver"
aws_ebs_csi_plugin_image_tag: "v{{ aws_ebs_csi_plugin_version }}"
```

The image tag in `download.yml` is derived from the version, resolving to `v0.5.0`. Note that the role `roles/kubernetes-apps/csi_driver/aws_ebs/defaults/main.yml` also defines `aws_ebs_csi_plugin_image_tag: latest` as a role-level default.

| Tag | Commit | aws_ebs_csi_plugin_version |
|-----|--------|----------------------------|
| v2.29.0 | 9991412 | 0.5.0 |
| v2.29.1 | 0c6a295 | 0.5.0 |
| v2.30.0 | f4ccdb5 | 0.5.0 |
| v2.31.0 | 1c9add4 | 0.5.0 |

The version is unchanged across the entire indexed range.

## Configuration
- Enable flag: `aws_ebs_csi_enabled` — default `false` (`roles/kubespray_defaults/defaults/main/main.yml`).
- Version var: `aws_ebs_csi_plugin_version` — default `0.5.0`.
- Image repo: `aws_ebs_csi_plugin_image_repo` = `{{ docker_image_repo }}/amazon/aws-ebs-csi-driver`.
- Image tag: `aws_ebs_csi_plugin_image_tag` = `v{{ aws_ebs_csi_plugin_version }}` (download.yml, resolves to `v0.5.0`); role default `latest` in the csi_driver role.
- Key options (`roles/kubernetes-apps/csi_driver/aws_ebs/defaults/main.yml`): `aws_ebs_csi_enable_volume_scheduling` (default `true`), `aws_ebs_csi_enable_volume_snapshot` (default `false`), `aws_ebs_csi_enable_volume_resizing` (default `false`), `aws_ebs_csi_controller_replicas` (default `1`).

## Compatibility
| Tag | Version |
|-----|---------|
| v2.29.0 | 0.5.0 |
| v2.29.1 | 0.5.0 |
| v2.30.0 | 0.5.0 |
| v2.31.0 | 0.5.0 |

Applicable to the Kubernetes versions shipped by these Kubespray tags (roughly 1.31–1.35).

## References
- roles/kubespray_defaults/defaults/main/download.yml (aws_ebs_csi_plugin_version, aws_ebs_csi_plugin_image_repo, aws_ebs_csi_plugin_image_tag)
- roles/kubespray_defaults/defaults/main/main.yml (aws_ebs_csi_enabled, persistent_volumes_enabled)
- roles/kubernetes-apps/csi_driver/aws_ebs/defaults/main.yml (role options, image tag)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
