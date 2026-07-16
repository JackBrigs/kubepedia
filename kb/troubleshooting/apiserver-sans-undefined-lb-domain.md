---
id: TROUBLE-APISERVER_SANS_UNDEFINED_LB_DOMAIN
type: troubleshooting
title: Undefined apiserver_loadbalancer_domain_name breaks apiserver_sans generation
status: active
kubespray_version: ">=v2.30.0 <v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - apiserver_sans undefined LB domain
tags:
  - control-plane
  - certificates
  - kubeadm
sources:
  - type: github_pr
    url: https://github.com/kubernetes-sigs/kubespray/pull/13009
    note: "Fix PR: undefined check for apiserver_loadbalancer_domain_name in apiserver_sans"
relations: []
---

# Undefined apiserver_loadbalancer_domain_name breaks apiserver_sans generation

## Summary
When `apiserver_loadbalancer_domain_name` is not defined, building the kube-apiserver certificate SAN list (`apiserver_sans`) fails during templating. This is common when deploying without an external load balancer, and when certificates are regenerated during an upgrade. Fixed in v2.31.0 by adding an undefined check; workaround on v2.30.0 is to explicitly set the variable.

## Problem
In the `_apiserver_sans` fact assembly, the value `apiserver_loadbalancer_domain_name` is appended to the SAN list without an `undefined` guard (unlike the neighboring `loadbalancer_apiserver.address | d('')`). If the variable is not set, templating fails before the `select` filter.

## Context
- Affected Kubespray versions: v2.30.0.
- Fixed versions: v2.31.0 (master). Backported to release-2.30 (future v2.30.1, tag not released).
- Trigger conditions: deploying without an external LB, or regenerating certificates during an upgrade, while `apiserver_loadbalancer_domain_name` is left undefined.

## Diagnostics
Inspect `roles/kubernetes/control-plane/tasks/kubeadm-setup.yml`, the `_apiserver_sans` block (lines 28-41 in the v2.30.0 tag):

```yaml
apiserver_sans: "{{ _apiserver_sans | flatten | select | unique }}"
vars:
  _apiserver_sans:
    - ...
    - "{{ apiserver_loadbalancer_domain_name }}"        # <- no | default('')
    - "{{ loadbalancer_apiserver.address | d('') }}"    # <- guard present here
```

The line with `apiserver_loadbalancer_domain_name` lacks `| default('')`; when the variable is undefined the task fails. The bug is present in v2.30.0.

## Known Issues
Root cause: `apiserver_loadbalancer_domain_name` is added to the SAN list without a `default('')` / undefined guard, so an undefined value breaks Jinja templating of `apiserver_sans`.

Workaround on v2.30.0: explicitly set `apiserver_loadbalancer_domain_name` in inventory (e.g., the domain name of the first control-plane node even without an external LB), or build the role from the release-2.30 branch.

Fix: PR [#13009](https://github.com/kubernetes-sigs/kubespray/pull/13009) "Undefined check for apiserver_loadbalancer_domain_name in apiserver_sans" (master → v2.31.0); backport to release-2.30 via PR [#13014](https://github.com/kubernetes-sigs/kubespray/pull/13014).

## References
- https://github.com/kubernetes-sigs/kubespray/pull/13009
- Migrated from Kubepedia 0.1.0 cache: apiserver-sans-undefined-lb-domain-v2.30.0.md
