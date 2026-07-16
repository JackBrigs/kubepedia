---
id: CONFIG-KUBELET_CONFIGURATION
type: configuration
title: Generated kubelet configuration (Kubespray)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubelet config
  - KubeletConfiguration
  - kubelet-config.yaml
tags:
  - kubernetes
  - kubelet
  - configuration
  - node
sources:
  - type: code
    path: roles/kubernetes/node/templates/kubelet-config.v1beta1.yaml.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/templates/kubelet-config.v1beta1.yaml.j2
    note: "generated KubeletConfiguration template (tag v2.31.0)"
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "default values of the kubelet_* variables (tag v2.31.0)"
relations:
  - type: see_also
    target: VARIABLE-KUBE_VERSION
  - type: see_also
    target: CONCEPT-K8S_1_35_CHANGES
  - type: see_also
    target: CONCEPT-SAMPLE_INVENTORY_LAYOUT
---

# Generated kubelet configuration (Kubespray)

## Summary

Kubespray renders a `KubeletConfiguration` (`kubelet.config.k8s.io/v1beta1`) file on
every node from `roles/kubernetes/node/templates/kubelet-config.v1beta1.yaml.j2`. It
is written under the kubelet config dir (referenced by the kubelet systemd unit) and
is the **source of truth for node-level behaviour** — auth, eviction, reserved
resources, DNS, swap, GC, feature gates. This document lists the fields it emits and
their Kubespray defaults so you know what a stock node runs and where to override it.

## Configuration

**Fields always emitted (with Kubespray default):**

| Field | Variable | Default (v2.31.0) |
|-------|----------|-------------------|
| `nodeStatusUpdateFrequency` | `kubelet_status_update_frequency` | `10s` |
| `failSwapOn` | `kubelet_fail_swap_on` | `true` |
| `authentication.anonymous.enabled` | — (hard-coded) | `false` |
| `authentication.webhook.enabled` | `kubelet_authentication_token_webhook` | `true` |
| `authentication.x509.clientCAFile` | `kube_cert_dir`/ca.crt | cluster CA |
| `authorization.mode` | `kubelet_authorization_mode_webhook` | `Webhook` |
| `staticPodPath` | `kube_manifest_dir` | `/etc/kubernetes/manifests` |
| `cgroupDriver` | `kubelet_cgroup_driver` | `systemd` |
| `containerLogMaxFiles` / `MaxSize` | `kubelet_logfiles_max_nr` / `_max_size` | `5` / `10Mi` |
| `containerRuntimeEndpoint` | `cri_socket` | runtime socket (containerd default) |
| `maxPods` | `kubelet_max_pods` | `110` |
| `podPidsLimit` | `kubelet_pod_pids_limit` | `-1` (unlimited) |
| `address` | `kubelet_bind_address` | node main IP (`::` fallback) |
| `readOnlyPort` | `kube_read_only_port` | `0` (**disabled**) |
| `clusterDomain` | `dns_domain` | `cluster.local` |
| `resolvConf` | `kube_resolv_conf` | `/etc/resolv.conf` |
| `eventRecordQPS` | `kubelet_event_record_qps` | `50` |
| `shutdownGracePeriod` | `kubelet_shutdown_grace_period` | `60s` |
| `shutdownGracePeriodCriticalPods` | `kubelet_shutdown_grace_period_critical_pods` | `20s` |
| `maxParallelImagePulls` | `kubelet_max_parallel_image_pulls` | `1` (serial pulls) |

**Security-relevant defaults:** anonymous auth **off**; webhook authn **and** authz
**on**; `readOnlyPort: 0` (the unauthenticated read-only port is disabled);
`protectKernelDefaults: true` (`kubelet_protect_kernel_defaults`);
`rotateCertificates: true` (client cert rotation). Server-cert bootstrap
(`serverTLSBootstrap`) is **off** by default (`kubelet_rotate_server_certificates:
false`) — enable it if you want kubelet serving certs signed by the cluster.

**Conditionally emitted fields** (only when the guarding variable is set/enabled):

- `failCgroupV1` — **only for `kube_version >= 1.35.0`**, default
  `kubelet_fail_cgroup_v1: true` → nodes refuse to start on cgroup v1. Set
  `kubelet_fail_cgroup_v1: false` to keep cgroup v1 (discouraged). See
  [[CONCEPT-K8S_1_35_CHANGES]].
- `clusterDNS` — derived from DNS mode: nodelocaldns IP if `enable_nodelocaldns`,
  else `skydns_server` (coredns), dual, or manual.
- `kubeReserved` / `systemReserved` (+ optional `*Cgroup`) — emitted only when
  `kube_reserved` / `system_reserved` is `true` (both default **false**, i.e. no
  reservation unless you opt in). Each reserves `cpu`, `memory`, `ephemeral-storage`,
  `pid`.
- `evictionHard` — only when `eviction_hard` is defined.
- `memorySwap.swapBehavior` — only when `failSwapOn` is false (`kubelet_swap_behavior`,
  default `LimitedSwap`).
- `featureGates` — from `kubelet_feature_gates` (falls back to `kube_feature_gates`).
- `seccompDefault`, `makeIPTablesUtilChains`, image-GC thresholds,
  `streamingConnectionIdleTimeout`, `cpuManagerPolicy(+Options)`,
  `topologyManagerPolicy(+Scope)`, `tracing`, `tlsMinVersion`/`tlsCipherSuites` —
  each emitted only when its variable is defined.
- `kubelet_config_extra_args` — free-form map merged verbatim (escape hatch for any
  KubeletConfiguration field not exposed as a dedicated variable).

Override these in inventory `group_vars` (node-level knobs typically in
`group_vars/all/` or `k8s_cluster/`); see [[CONCEPT-SAMPLE_INVENTORY_LAYOUT]].

## Compatibility

- Template verified at tag `v2.31.0`; the field set is stable across
  `v2.29.0`–`v2.31.0` with one version-gated addition: `failCgroupV1` appears only
  when installing Kubernetes `1.35+`.
- `apiVersion` is `kubelet.config.k8s.io/v1beta1` for the whole range.
- Kubelet command-line flags (not in this file) come from
  `roles/kubernetes/node/templates/kubelet.env.v1beta1.j2`.

## References

- Template + defaults at tag `v2.31.0` (see sources).
- Kubernetes version boundary for `failCgroupV1`: [[CONCEPT-K8S_1_35_CHANGES]].
