---
id: COMPONENT-KUBE_VIP
type: component
title: kube-vip
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: ">=0.8.9 <=1.0.3"
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kube-vip
tags:
  - load-balancer
  - control-plane
  - kube-vip
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    lines: "64,266,267 (v2.29.0)"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "v2.29.0: kube_vip_version 0.8.0 but kube_vip_image_tag literal v0.8.9 (deployed = v0.8.9)"
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "v2.30.0/v2.31.0: kube_vip_image_tag = v{{ kube_vip_version }}; kube_vip_version 1.0.3"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_vip_enabled: false (opt-in)"
relations:
  - type: see_also
    target: COMPONENT-METALLB
  - type: see_also
    target: CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS
---

# kube-vip

## Summary

kube-vip provides a virtual IP and load balancing for the Kubernetes control
plane (and optionally for `Service` type `LoadBalancer`). It is an opt-in add-on
(`kube_vip_enabled: false` by default). The **deployed** version moved from
`v0.8.9` in `v2.29.0` to `v1.0.3` in `v2.30.0`–`v2.31.0`.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`.
- Disabled by default; enabled with `kube_vip_enabled: true`.
- An alternative/companion to [[COMPONENT-METALLB]]; often used to front the
  control plane (see [[CONCEPT-CONTROL_PLANE_COMPONENT_VERSIONS]]).

## Implementation

The image comes from `ghcr.io`
(`roles/kubespray_defaults/defaults/main/download.yml`):

```yaml
kube_vip_image_repo: "{{ github_image_repo }}/kube-vip/kube-vip{{ '-iptables' if kube_vip_lb_fwdmethod == 'masquerade' else '' }}"
# github_image_repo = ghcr.io
```

The **deployed image tag** differs from the `kube_vip_version` variable in
`v2.29.0`, which is a genuine version-tracking pitfall:

| Kubespray | kube_vip_version | kube_vip_image_tag (deployed) |
|-----------|------------------|-------------------------------|
| v2.29.0   | 0.8.0            | `v0.8.9` (literal) → **deployed v0.8.9** |
| v2.30.0   | 1.0.3            | `v{{ kube_vip_version }}` → **v1.0.3** |
| v2.31.0   | 1.0.3            | `v{{ kube_vip_version }}` → **v1.0.3** |

In `v2.29.0` the running container is `v0.8.9` (from the literal
`kube_vip_image_tag`), while `kube_vip_version` (`0.8.0`) is not used to build the
image tag. From `v2.30.0` the tag is derived from `kube_vip_version`, so the two
agree. When reasoning about "which kube-vip runs", trust the image tag.

## Configuration

- Enablement: `kube_vip_enabled` (default `false`).
- Image: `kube_vip_image_repo` = `ghcr.io/kube-vip/kube-vip` (or
  `…/kube-vip-iptables` when `kube_vip_lb_fwdmethod == 'masquerade'`), tag
  `kube_vip_image_tag`.
- Forwarding method: `kube_vip_lb_fwdmethod` selects the iptables image variant.

## Compatibility

- Kubespray `v2.29.0` → kube-vip `v0.8.9` (deployed); `v2.30.0`/`v2.31.0` →
  `v1.0.3`.
- Applies to the Kubernetes versions these releases install (`>=1.31`).

## References

- `roles/kubespray_defaults/defaults/main/download.yml` — `kube_vip_version`
  (v2.29.0:64), `kube_vip_image_repo` (v2.29.0:266), `kube_vip_image_tag`
  (v2.29.0:267, literal); derived from `kube_vip_version` in v2.30.0+.
- `roles/kubespray_defaults/defaults/main/main.yml` (`kube_vip_enabled`).
- Tags: v2.29.0 `9991412`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`.
