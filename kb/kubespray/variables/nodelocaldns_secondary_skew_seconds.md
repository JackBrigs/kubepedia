---
id: VARIABLE-NODELOCALDNS_SECONDARY_SKEW_SECONDS
type: variable
title: nodelocaldns_secondary_skew_seconds
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - nodelocaldns_secondary_skew_seconds
tags:
  - dns
  - nodelocaldns
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Time skew between primary and secondary nodelocaldns instances; default 5"
relations:
  - type: see_also
    target: COMPONENT-NODELOCALDNS
---

# nodelocaldns_secondary_skew_seconds

## Summary
Time skew, in seconds, applied to the secondary nodelocaldns instance so its restarts/reloads do not coincide with the primary. Default is `5`.

## Implementation
Defined in `roles/kubespray_defaults/defaults/main/main.yml` as `nodelocaldns_secondary_skew_seconds: 5`. Value is unchanged across v2.29.0-v2.31.0 (line number only shifts). The same default is documented in `docs/advanced/dns-stack.md` and mirrored in the sample inventory.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Relevant when `enable_nodelocaldns_secondary: true`. Related: `enable_nodelocaldns_secondary`, `nodelocaldns_second_health_port`.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
