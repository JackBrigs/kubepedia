---
id: COMPONENT-METALLB
type: component
title: MetalLB
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "0.13.9"
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - metallb
tags:
  - load-balancer
  - metallb
  - addons
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    lines: "366-369 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "metallb_version, metallb_speaker/controller_image_repo, metallb_image_tag"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    lines: "470 (v2.31.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "metallb_enabled: false (opt-in)"
relations:
  - type: see_also
    target: COMPONENT-KUBE_VIP
---

# MetalLB

## Summary

MetalLB is a bare-metal load-balancer implementation for Kubernetes `Service`
type `LoadBalancer`. It is an opt-in add-on in Kubespray (`metallb_enabled:
false` by default). The pinned version is `0.13.9`, unchanged across
`v2.29.0`–`v2.31.0`.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- Disabled by default; enabled with `metallb_enabled: true`.
- Provides `LoadBalancer` addresses on bare metal; an alternative to
  [[COMPONENT-KUBE_VIP]] for service load balancing.

## Implementation

The version is a literal
(`roles/kubespray_defaults/defaults/main/download.yml`):

```yaml
metallb_version: 0.13.9
metallb_speaker_image_repo: "{{ quay_image_repo }}/metallb/speaker"       # quay.io/metallb/speaker
metallb_controller_image_repo: "{{ quay_image_repo }}/metallb/controller" # quay.io/metallb/controller
metallb_image_tag: "v{{ metallb_version }}"                               # v0.13.9
```

The version does not vary by tag or by `kube_version`:

| Kubespray | metallb_version | Images |
|-----------|-----------------|--------|
| v2.29.0   | 0.13.9          | quay.io/metallb/{speaker,controller}:v0.13.9 |
| v2.29.1   | 0.13.9          | quay.io/metallb/{speaker,controller}:v0.13.9 |
| v2.30.0   | 0.13.9          | quay.io/metallb/{speaker,controller}:v0.13.9 |
| v2.31.0   | 0.13.9          | quay.io/metallb/{speaker,controller}:v0.13.9 |

## Configuration

- Enablement: `metallb_enabled` (default `false`).
- Version: `metallb_version` (literal).
- Images: `metallb_speaker_image_repo`, `metallb_controller_image_repo`, tag
  `metallb_image_tag` = `v{{ metallb_version }}`.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: MetalLB `0.13.9`.
- Applies to the Kubernetes versions these releases install (`>=1.31`).

## References

- `roles/kubespray_defaults/defaults/main/download.yml:366-369` (`metallb_version`,
  image repos, tag).
- `roles/kubespray_defaults/defaults/main/main.yml` (`metallb_enabled`).
- Tags: v2.29.0 `9991412`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
