---
id: PRACTICE-CNI_GENERIC_PLUGIN
type: best_practice
title: "The 'cni' plugin option: custom / unsupported CNI"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-21"
confidence: verified
aliases:
  - cni-generic-plugin
  - kube_network_plugin cni
  - custom cni without kubespray
  - opt/cni/bin unpack only
tags:
  - operations
  - cni
sources:
  - type: docs
    path: docs/CNI/cni.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/CNI/cni.md
    note: "digest of the tag doc"
  - type: code
    path: roles/network_plugin/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/tasks/main.yml
    note: "network_plugin/cni is included for every kube_network_plugin except none; then network_plugin/{{ kube_network_plugin }} — which for 'cni' configures nothing"
  - type: code
    path: roles/network_plugin/cni/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cni/tasks/main.yml
    note: "creates /opt/cni/bin (owner cni_bin_owner, recurse: true) and unpacks the CNI plugins archive — the only two things this value does"
relations:
  - type: see_also
    target: COMPONENT-CNI_PLUGINS
  - type: see_also
    target: VARIABLE-CNI_BIN_OWNER
  - type: see_also
    target: CONCEPT-CUSTOM_CNI
  - type: see_also
    target: TROUBLE-KUBELET_NODE_NOTREADY_CNI
---

# The 'cni' plugin option: custom / unsupported CNI

## Summary

Setting `kube_network_plugin: cni` makes Kubespray only unpack the CNI plugin binaries (`cni_version`) into `/opt/cni/bin` and point the container runtime at CNI — it does **not** configure any network. You supply the CNI config yourself.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- For custom routing/bridge/loopback setups or CNIs Kubespray does not manage.

## Implementation

With `kube_network_plugin: cni`, you must populate `/etc/cni/net.d` with a valid CNI
configuration after Kubespray runs; otherwise pods have no network. The plugin binaries come
from [[COMPONENT-CNI_PLUGINS]] (`cni_version`). This is the escape hatch for
unsupported/custom CNIs (contrast the managed [[COMPONENT-CILIUM]] path).

**What actually runs** (verified at v2.31.0):

- `roles/network_plugin/tasks/main.yml` includes **`network_plugin/cni` for every plugin
  except `none`** — so the binary-unpacking step is not specific to
  `kube_network_plugin: cni`; it is the common base for all of them. It then includes
  `network_plugin/{{ kube_network_plugin }}`, and for the value `cni` **that role does not
  exist as a configurator** — nothing writes a network config. That absence *is* the
  feature.
- The base role does exactly two things (`roles/network_plugin/cni/tasks/main.yml`):
  creates `/opt/cni/bin` (mode `0755`, `owner: {{ cni_bin_owner }}`, **`recurse: true`**)
  and unpacks the CNI plugins archive into it. Ownership therefore comes from
  [[VARIABLE-CNI_BIN_OWNER]] (default `{{ kube_owner }}`, i.e. `kube`) — relevant if your
  hand-rolled CNI runs as a pod that writes there ([[VARIABLE-KUBE_OWNER]]).
- **`/etc/cni/net.d` and `/opt/cni/bin` are *not* pre-created by preinstall for this value.**
  `roles/kubernetes/preinstall/tasks/0050-create_directories.yml` ("Create cni directories")
  is gated on `kube_network_plugin in ["calico", "flannel", "cilium", "kube-ovn",
  "kube-router", "macvlan"]` — `cni` is not in that list. `/opt/cni/bin` still appears
  (the base role creates it); `/etc/cni/net.d` is yours to create.
- **Do not confuse it with `custom_cni`.** `kube_network_plugin: custom_cni` has its own role
  that *applies your manifests* for you ([[CONCEPT-CUSTOM_CNI]]); `cni` applies nothing at
  all.

## Service impact

Choosing `cni` is a decision about what Kubespray will **not** do, and it lands as a
day-one outage until you finish the job: with binaries but no config in `/etc/cni/net.d`,
kubelet reports the node `NotReady` with a CNI-not-initialised message and no pod gets an
address ([[TROUBLE-KUBELET_NODE_NOTREADY_CNI]]). Plan the CNI configuration step as part of
the same window as the Kubespray run.

On re-runs the base role re-unpacks the plugin binaries and **re-applies ownership
recursively** to `/opt/cni/bin` — so anything you dropped there by hand survives but may be
re-owned, and binaries with the same names are overwritten by the Kubespray-shipped ones.
Keep your own plugins under a different `bin` directory, or expect them to be replaced.

## References

- `docs/CNI/cni.md` (tag v2.31.0 `1c9add4`);
  `roles/network_plugin/tasks/main.yml` (include chain),
  `roles/network_plugin/cni/{tasks,defaults}/main.yml` (unpack + `cni_bin_owner`),
  `roles/kubernetes/preinstall/tasks/0050-create_directories.yml` (plugin list that
  excludes `cni`).
