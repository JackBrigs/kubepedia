---
id: TROUBLE-CILIUM_HARDCODED_APISERVER_IP_HA
type: troubleshooting
title: Cilium hardcoded API server IP breaks HA cluster on first control-plane failure
status: active
kubespray_version: "v2.29.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - cilium hardcoded apiserver ip
tags:
  - cilium
  - ha
  - apiserver
sources:
  - type: github_pr
    url: https://github.com/kubernetes-sigs/kubespray/pull/12624
    note: "Merged PR that points k8sServiceHost/k8sServicePort at kube_apiserver_global_endpoint"
relations: []
---

# Cilium hardcoded API server IP breaks HA cluster on first control-plane failure

## Summary
In an HA cluster, Cilium pointed `k8sServiceHost` at the IP of the first control-plane node only instead of the apiserver load balancer. When the first control-plane node became unavailable, `cilium-operator` and `cilium-agent` lost API connectivity and the cluster network failed. Fixed in v2.30.0 by sourcing the host/port from `kube_apiserver_global_endpoint`.

## Problem
When the first control-plane node was shut down or unreachable, the `cilium-operator` and `cilium-agent` pods lost API access with `dial tcp <first-cp-ip>:6443: connect: no route to host`. Pods went NotReady and cluster networking failed. Working around it via `cilium_config_extra_vars` did not help, because the `KUBERNETES_SERVICE_HOST` environment variable was already baked into the running pods.

## Context
- Affected versions: v2.29.1 (and earlier; hardcoded IP of the first control-plane node).
- Fixed versions: v2.30.0.
- Triggered in HA clusters when the first control-plane node fails/becomes unreachable.

## Diagnostics
- Check `cilium-operator` / `cilium-agent` logs for `dial tcp <first-cp-ip>:6443: connect: no route to host`.
- Inspect the rendered Cilium helm-values: `k8sServiceHost` set to the first control-plane node IP rather than the apiserver load balancer / global endpoint.
- Confirm the failure correlates with taking the first control-plane node offline.

## Known Issues
Root cause: Cilium referenced the IP of only the first control-plane node (`k8sServiceHost`) instead of the local/external apiserver load balancer, so connectivity was lost when that node failed.

Fix (breaking change in v2.30.0): PR #12624 (merged 2026-01-01, Issue #12623) makes `k8sServiceHost` / `k8sServicePort` derive from `kube_apiserver_global_endpoint`. Confirmed in tag v2.30.0 `roles/network_plugin/cilium/templates/values.yaml.j2` (line 10: `k8sServiceHost: "{{ kube_apiserver_global_endpoint | urlsplit('hostname') }}"`, line 11: `k8sServicePort: "{{ kube_apiserver_global_endpoint | urlsplit('port') }}"`).

Action required on upgrade to v2.30.0: ensure `kube_apiserver_global_endpoint` is correctly configured and reachable from all nodes, otherwise Cilium cannot reach the apiserver.

## References
- https://github.com/kubernetes-sigs/kubespray/pull/12624
- Migrated from Kubepedia 0.1.0 cache: cilium-hardcoded-apiserver-ip-ha-v2.30.0.md
