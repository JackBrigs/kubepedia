---
id: TROUBLE-PSA_BLOCKS_PRIVILEGED_WORKLOAD
type: troubleshooting
title: "PodSecurity 'restricted' rejects a privileged CNI/CSI/agent DaemonSet — needs namespace label / exemption"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - violates PodSecurity restricted
  - privileged pod forbidden namespace
  - daemonset blocked pod security
  - hostpath hostnetwork rejected psa
  - pod-security.kubernetes.io/enforce
  - kube_pod_security exemptions
tags:
  - troubleshooting
  - security
  - pod-security
  - admission
  - interaction
sources:
  - type: external
    path: Pod Security Admission
    url: https://kubernetes.io/docs/concepts/security/pod-security-admission/
    note: "namespace labels pod-security.kubernetes.io/enforce; restricted rejects privileged/hostPath/hostNetwork"
  - type: code
    path: kube_pod_security_* exemptions
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "kube_pod_security_default_enforce, kube_pod_security_exemptions_namespaces"
relations:
  - type: see_also
    target: VARIABLE-KUBE_POD_SECURITY_DEFAULT_ENFORCE
  - type: see_also
    target: VARIABLE-KUBE_POD_SECURITY_EXEMPTIONS_NAMESPACES
  - type: see_also
    target: PRACTICE-HARDENING
  - type: see_also
    target: CONCEPT-COMPONENT_INTERACTION_FAILURES
---

# PodSecurity 'restricted' rejects a privileged CNI/CSI/agent DaemonSet — needs namespace label / exemption

## Summary

Another **two-component seam**: you harden the cluster with **Pod Security Admission** enforcing
`restricted` (cluster default or per-namespace), then a **privileged infrastructure DaemonSet** — a CNI
agent, a CSI node plugin, a log/monitoring collector that needs `hostNetwork` / `hostPath` /
`privileged` / `NET_ADMIN` — gets **rejected at admission**. The controller keeps retrying and its pods
never start. The fix is to exempt the **infra namespace** (label it `privileged`) or add it to
Kubespray's PSA exemptions — not to weaken the whole cluster.

## Problem

- A DaemonSet/Deployment shows **0 pods**; its controller events read
  `forbidden: violates PodSecurity "restricted:latest": host namespaces / privileged / hostPath ...`.
- Happens right after enabling `restricted` enforcement, or when deploying a privileged addon into a
  namespace that inherits the restricted default.

## Context

- Applies across **v2.27.0–v2.31.0**; PSA is built in (PodSecurityPolicy is long gone). Kubespray sets
  a cluster-wide default via `kube_pod_security_default_enforce`
  ([[VARIABLE-KUBE_POD_SECURITY_DEFAULT_ENFORCE]]) and exemptions via
  `kube_pod_security_exemptions_namespaces` ([[VARIABLE-KUBE_POD_SECURITY_EXEMPTIONS_NAMESPACES]]).
- **Why:** PSA enforces the level configured for the pod's **namespace** (label
  `pod-security.kubernetes.io/enforce`), falling back to the cluster default. `restricted` forbids
  privileged, host namespaces, most `hostPath`, added capabilities, running as root — exactly what
  node-level agents require. The workload isn't broken; the **namespace policy** rejects it.
- **Note:** `kube-system` is commonly exempt already; the trap is a **new** namespace or a cluster
  default that catches an infra addon.

## Diagnostics

```bash
kubectl get ns <ns> -o jsonpath='{.metadata.labels}' | tr ',' '\n' | grep pod-security  # enforce level
kubectl get events -n <ns> --field-selector reason=FailedCreate | grep -i podsecurity
kubectl -n <ns> get ds,deploy -o wide     # DESIRED vs CURRENT = 0
```

## Known Issues

- **Fix (label the infra namespace):** for a namespace that legitimately runs privileged agents, set
  `kubectl label ns <ns> pod-security.kubernetes.io/enforce=privileged --overwrite` (and
  `warn`/`audit` to match). Keep application namespaces at `restricted`.
- **Fix (Kubespray, persistent):** add the namespace to
  `kube_pod_security_exemptions_namespaces` ([[VARIABLE-KUBE_POD_SECURITY_EXEMPTIONS_NAMESPACES]]) so
  the setting survives re-converge — don't hand-label and let the next `cluster.yml` revert it.
- **Do not** drop the cluster default to `privileged` to fix one workload — that removes protection
  everywhere. Scope the exemption to the namespace ([[PRACTICE-HARDENING]]).
- **Redesign option:** run the agent under a dedicated namespace and restrict what actually needs
  privilege; some collectors have a rootless/less-privileged mode.

## References

- Upstream Pod Security Admission; Kubespray `kube_pod_security_*`. Enforce
  [[VARIABLE-KUBE_POD_SECURITY_DEFAULT_ENFORCE]]; exemptions
  [[VARIABLE-KUBE_POD_SECURITY_EXEMPTIONS_NAMESPACES]]; hardening [[PRACTICE-HARDENING]]; interaction
  spine [[CONCEPT-COMPONENT_INTERACTION_FAILURES]].
