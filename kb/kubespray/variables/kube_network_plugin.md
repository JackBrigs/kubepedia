---
id: VARIABLE-KUBE_NETWORK_PLUGIN
type: variable
title: kube_network_plugin
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - kube_network_plugin
tags:
  - cni
  - networking
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_network_plugin: calico (default, unchanged v2.29.0–v2.31.0)"
  - type: docs
    path: docs/ansible/vars.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/ansible/vars.md
    note: "documents the accepted CNI values (calico, cilium, flannel, kube-ovn, ...)"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# kube_network_plugin

## Summary

`kube_network_plugin` selects the CNI network plugin Kubespray installs. The
default is `calico`, unchanged across `v2.29.0`–`v2.31.0`. All shipped plugins are
now indexed: [[COMPONENT-CALICO]] (default), [[COMPONENT-CILIUM]], [[COMPONENT-FLANNEL]],
[[COMPONENT-KUBE_OVN]], [[COMPONENT-KUBE_ROUTER]], [[COMPONENT-MACVLAN]], and the
meta-plugin [[COMPONENT-MULTUS]].

## Implementation

Defined in `roles/kubespray_defaults/defaults/main/main.yml`
(`kube_network_plugin: calico`, unchanged across all three tags). The value
selects which `roles/network_plugin/<plugin>` role runs and which manifests are
templated.

Accepted values at v2.31.0: `calico` (default), `cilium`, `flannel`, `kube-ovn`,
`kube-router`, `macvlan`, plus `cni` (custom / `custom_cni` role), `ovn4nfv`, and
`none`. `multus` is a meta-plugin layered on top of a primary CNI.

> **`weave` was removed** — there is no `roles/network_plugin/weave` at v2.31.0
> (Weave Net is EOL upstream). Don't set `kube_network_plugin: weave`.

> Indexed in Kubepedia: all of the above (calico/cilium/flannel/kube-ovn/
> kube-router/macvlan/multus). Deferred: `custom_cni`, `ovn4nfv` (niche).

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: default `calico`; `cilium` is a supported
  alternative selected with `kube_network_plugin: cilium`.
- The chosen plugin determines datapath, network policy support, and which
  component versions apply (e.g. `cilium_version` when `cilium`).

## References

- `roles/kubespray_defaults/defaults/main/main.yml` — default (tags v2.29.0
  `9991412`, v2.30.0 `f4ccdb5`, v2.31.0 `1c9add4`).
- `docs/ansible/vars.md` — accepted value set.
