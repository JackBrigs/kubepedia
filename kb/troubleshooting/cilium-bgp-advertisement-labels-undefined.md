---
id: TROUBLE-CILIUM_BGP_ADVERTISEMENT_LABELS
type: troubleshooting
title: "Cilium: undefined variable error for CiliumBGPAdvertisement labels"
status: active
kubespray_version: "v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium-bgp-advertisement-labels-undefined
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/13149
    note: "fix merged in v2.31.0 (PR #13149)"
  - type: code
    path: roles/network_plugin/cilium/templates/cilium/cilium-bgp-advertisement.yml.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/templates/cilium/cilium-bgp-advertisement.yml.j2
    note: "fixed file"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
---

# Cilium: undefined variable error for CiliumBGPAdvertisement labels

## Summary

Rendering the CiliumBGPAdvertisement manifest failed with an undefined-variable error when using Cilium BGP control plane, aborting the network step. Fixed in **v2.31.0** (PR #13149).

## Problem

The `cilium-bgp-advertisement.yml.j2` template referenced a label variable that could be undefined; the fix guards it. Only affects clusters using Cilium BGP.

## Context

- Affected Kubespray: `v2.30.0`. Fixed in: `v2.31.0`.
- Confirmed via merged PR #13149 and the tag code.

## Diagnostics

```bash
# network step fails with "AnsibleUndefinedVariable" while templating cilium BGP advertisement
grep cilium_enable_bgp -r inventory/
```

## Known Issues

Fixed by PR #13149 (in `roles/network_plugin/cilium/templates/cilium/cilium-bgp-advertisement.yml.j2`). Workaround before upgrading: avoid Cilium BGP advertisement config until upgrading, or define the missing labels. Durable fix: upgrade to `v2.31.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/13149 — fixed in `v2.31.0`.
- `roles/network_plugin/cilium/templates/cilium/cilium-bgp-advertisement.yml.j2`.
