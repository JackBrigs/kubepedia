---
id: CONCEPT-TALOS_CILIUM
type: concept
title: "Talos + Cilium — CNI install specifics"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - talos cilium install
  - talos cni none cilium
  - talos kube-proxy replacement
  - cilium kubeprism talos
  - talos cilium cgroup securitycontext
tags:
  - os
  - talos
  - networking
  - cilium
  - documentation
sources:
  - type: docs
    path: Talos "Deploying Cilium CNI"
    url: https://www.talos.dev/latest/kubernetes-guides/network/deploying-cilium/
    note: "cni.name none, proxy disabled, Cilium values for Talos"
relations:
  - type: see_also
    target: CONCEPT-TALOS_NETWORKING
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: TROUBLE-CILIUM_POD_CONNECTIVITY
---

# Talos + Cilium — CNI install specifics

## Summary

Running Cilium on Talos needs two things: tell Talos **not** to install its default CNI/proxy,
and give Cilium the **Talos-specific values** (KubePrism API endpoint, cgroup mount,
capabilities). Miss these and Cilium pods crash or the cluster has no working network.

## Context

- Applies to Talos **1.13.x** with Cilium ([[CONCEPT-TALOS_NETWORKING]], [[COMPONENT-CILIUM]]).
  Talos's default CNI is Flannel — Cilium replaces it.

## Implementation

**1. Disable Talos defaults (machine config).**

```yaml
cluster:
  network:
    cni:
      name: none        # don't install Flannel
  proxy:
    disabled: true      # Cilium does kube-proxy replacement
```

**2. Install Cilium with Talos-appropriate Helm values.** Key ones:

- **API endpoint without kube-proxy:** point Cilium at Talos's **KubePrism** local API balancer
  — `k8sServiceHost: localhost`, `k8sServicePort: 7445` — so the agent reaches the API before a
  service network exists (alternatively the control-plane VIP).
- **`kubeProxyReplacement: true`** (paired with `proxy.disabled` above).
- **cgroup:** Talos already mounts cgroup v2 — set `cgroup.autoMount.enabled: false` and
  `cgroup.hostRoot: /sys/fs/cgroup` so Cilium doesn't try to (re)mount it.
- **Capabilities:** Talos restricts pod capabilities, so grant the specific ones Cilium needs
  (`securityContext.capabilities.ciliumAgent` / `cleanCiliumState` lists per the Talos guide),
  rather than relying on privileged defaults.

## Compatibility

- **Do not deploy kube-proxy** — with `proxy.disabled: true` + `kubeProxyReplacement`, a stray
  kube-proxy conflicts.
- After install, validate with `cilium status` / `cilium connectivity test`; cross-node issues
  are the usual datapath class ([[TROUBLE-CILIUM_POD_CONNECTIVITY]]).
- Keep the Cilium version within its own K8s support window ([[COMPONENT-CILIUM]]); the Talos
  guide's values track current Cilium — re-check them when bumping either side.

## References

- Talos "Deploying Cilium" guide (above); Talos networking: [[CONCEPT-TALOS_NETWORKING]];
  Cilium component: [[COMPONENT-CILIUM]]; connectivity: [[TROUBLE-CILIUM_POD_CONNECTIVITY]].
