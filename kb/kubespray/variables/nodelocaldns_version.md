---
id: VARIABLE-NODELOCALDNS_VERSION
type: variable
title: nodelocaldns_version
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: "1.25.0"
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nodelocaldns_version
tags:
  - dns
  - nodelocaldns
  - versions
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/download.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/download.yml
    note: "Pins the node-local-dns (k8s-dns-node-cache) image version; default 1.25.0"
relations:
  - type: see_also
    target: COMPONENT-NODELOCALDNS
---

# nodelocaldns_version

## Summary
Version of the node-local-dns (k8s-dns-node-cache) image deployed for the nodelocaldns cache. Default is `1.25.0`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/download.yml` as `nodelocaldns_version: "1.25.0"`. The value is unchanged across v2.29.0-v2.31.0 (only the line number shifts: 284 in v2.29.0, 286 in v2.29.1, 287 in v2.30.0, 281 in v2.31.0).

## Compatibility
Kubespray v2.29.0 through v2.31.0. Used to build the nodelocaldns image tag/download. Related: `nodelocaldns_ip`, `enable_nodelocaldns`.

## References
- roles/kubespray_defaults/defaults/main/download.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
