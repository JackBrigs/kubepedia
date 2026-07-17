---
id: COMPONENT-SCHEDULER_PLUGINS
type: component
title: scheduler-plugins
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "0"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - scheduler-plugins
tags:
  - scheduler
  - kubernetes-apps
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "scheduler_plugins_version, image repo/tag vars"
  - type: code
    path: roles/kubernetes-apps/scheduler_plugins/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/scheduler_plugins/defaults/main.yml
    note: "scheduler_plugins_enabled default"
relations:
  - type: see_also
    target: CONCEPT-SAMPLE_INVENTORY_LAYOUT
---

# scheduler-plugins

## Summary

scheduler-plugins deploys the Kubernetes SIG scheduler-plugins project as a
second scheduler (a controller plus a scheduler Deployment), enabling extra
scheduling features such as Coscheduling, CapacityScheduling, and
NodeResourceTopologyMatch. It is an opt-in addon: `scheduler_plugins_enabled`
defaults to `false` in all covered tags. Its version is looked up from the
`scheduler_plugins_supported_versions` table, which in every covered tag maps the
supported Kubernetes minors to `0`.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- Opt-in: `scheduler_plugins_enabled: false` by default
  (`roles/kubernetes-apps/scheduler_plugins/defaults/main.yml` and
  `roles/kubespray_defaults/defaults/main/main.yml`).
- Deployed by the `roles/kubernetes-apps/scheduler_plugins` role via the
  `deploy-scheduler-plugins.yaml.j2` and `cm-scheduler-plugins.yaml.j2`
  templates; images are pulled from the Kubernetes image registry
  (`kube_image_repo`).
- Depends on the target Kubernetes minor via `kube_major_version` for its
  version lookup.

## Implementation

The version is derived from a lookup table
(`roles/kubespray_defaults/defaults/main/download.yml`):

```yaml
# Scheduler plugins doesn't build for K8s 1.29 yet
scheduler_plugins_supported_versions:
  '1.31': 0
  '1.30': 0
  '1.29': 0
scheduler_plugins_version: "{{ scheduler_plugins_supported_versions[kube_major_version] }}"
```

In every covered tag (v2.29.0, v2.29.1, v2.30.0, v2.31.0) this table is identical
and maps `1.29`, `1.30`, and `1.31` all to `0`, so the derived
`scheduler_plugins_version` is `0` and does not change between tags. Note that
the table only lists Kubernetes minors 1.29–1.31, while the default
`kube_version` in these tags is 1.33–1.35; the table therefore does not cover the
default Kubernetes minor, and using this addon requires supplying a matching
version. The image tags are built as `v{{ scheduler_plugins_version }}`.

Image variables (`roles/kubespray_defaults/defaults/main/download.yml`):

```yaml
scheduler_plugins_controller_image_repo: "{{ kube_image_repo }}/scheduler-plugins/controller"
scheduler_plugins_controller_image_tag: "v{{ scheduler_plugins_version }}"
scheduler_plugins_scheduler_image_repo: "{{ kube_image_repo }}/scheduler-plugins/kube-scheduler"
scheduler_plugins_scheduler_image_tag: "v{{ scheduler_plugins_version }}"
```

| Tag | commit | scheduler_plugins_supported_versions | resolved version |
|-----|--------|--------------------------------------|------------------|
| v2.29.0 | 9991412 | 1.31/1.30/1.29 → 0 | 0 |
| v2.29.1 | 0c6a295 | 1.31/1.30/1.29 → 0 | 0 |
| v2.30.0 | f4ccdb5 | 1.31/1.30/1.29 → 0 | 0 |
| v2.31.0 | 1c9add4 | 1.31/1.30/1.29 → 0 | 0 |

## Configuration

- Enable flag: `scheduler_plugins_enabled` (default `false`).
- Version var: `scheduler_plugins_version` (derived from
  `scheduler_plugins_supported_versions[kube_major_version]`).
- Image vars: `scheduler_plugins_controller_image_repo` /
  `scheduler_plugins_controller_image_tag`,
  `scheduler_plugins_scheduler_image_repo` /
  `scheduler_plugins_scheduler_image_tag`.
- Other options: `scheduler_plugins_namespace` (`scheduler-plugins`),
  `scheduler_plugins_controller_replicas` (1),
  `scheduler_plugins_scheduler_replicas` (1),
  `scheduler_plugins_enabled_plugins`
  (Coscheduling, CapacityScheduling, NodeResourceTopologyMatch,
  NodeResourcesAllocatable).

## Compatibility

- Per-tag version: `0` in all four tags (unchanged; from the identical
  supported-versions table).
- Table lists Kubernetes minors 1.29–1.31; default `kube_version` in these tags
  is 1.33–1.35, so the default minor is outside the listed table entries.

## References

- roles/kubespray_defaults/defaults/main/download.yml (scheduler_plugins_version, image vars)
- roles/kubernetes-apps/scheduler_plugins/defaults/main.yml (scheduler_plugins_enabled)
- roles/kubernetes-apps/scheduler_plugins/templates/ (deploy and configmap templates)
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
