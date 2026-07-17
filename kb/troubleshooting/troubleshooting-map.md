---
id: CONCEPT-TROUBLESHOOTING_MAP
type: concept
title: "Troubleshooting map — start here (by symptom)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - troubleshooting index
  - where to start debugging
  - symptom map
  - troubleshooting entry points
  - diagnose kubespray cluster
tags:
  - troubleshooting
  - navigation
  - index
sources:
  - type: docs
    path: kb/troubleshooting/
    url: https://github.com/kubernetes-sigs/kubespray
    note: "curated index of the KB troubleshooting layer (this repo)"
relations:
  - type: see_also
    target: TROUBLE-KUBESPRAY_PREFLIGHT_FAILS
  - type: see_also
    target: TROUBLE-POD_CONTAINERCREATING
  - type: see_also
    target: TROUBLE-ETCD_QUORUM_LOSS
---

# Troubleshooting map — start here (by symptom)

## Summary

An index into the troubleshooting layer, grouped by **what you observe**. Jump to the
symptom category, then to the specific doc. Each linked doc gives diagnostics and a
source-verified fix.

## Context

- Covers Kubespray `v2.29.0`–`v2.31.0`. This is a navigator, not the fixes themselves.
- First move for almost anything Pod-level: **`kubectl describe`** — its Events name the
  cause, which maps to a doc below.

## Implementation

### Deploy / preflight won't start

- Preflight assertion "Stop if …" → [[TROUBLE-KUBESPRAY_PREFLIGHT_FAILS]] (memory
  [[TROUBLE-NODE_MEMORY_TOO_SMALL]], nftables kernel [[TROUBLE-NFTABLES_KERNEL_TOO_LOW]]).
- Cilium config aborts deploy → [[TROUBLE-CILIUM_CONFIG_VALIDATION]].
- Download/checksum failure → [[TROUBLE-DOWNLOAD_FAILS]].

### Pod lifecycle

- `Pending` / Unschedulable (scheduler) → [[TROUBLE-POD_PENDING_UNSCHEDULABLE]].
- `ContainerCreating` (kubelet/CNI) → [[TROUBLE-POD_CONTAINERCREATING]].
- `CrashLoopBackOff` (starts then dies) → [[TROUBLE-CRASHLOOPBACKOFF]].
- `OOMKilled` / exit 137 → [[TROUBLE-OOMKILLED]].
- Stuck `Terminating` → [[TROUBLE-POD_STUCK_TERMINATING]].
- Evicted under disk pressure → [[TROUBLE-DISK_PRESSURE_EVICTION]].

### Networking & DNS

- Cross-node pod traffic / MTU → [[TROUBLE-VXLAN_MTU_MISMATCH]]; conntrack drops →
  [[TROUBLE-CONNTRACK_TABLE_FULL]].
- Ports blocked by firewall → [[TROUBLE-FIREWALL_PORTS_BLOCKED]].
- External DNS fails → [[TROUBLE-DNS_EXTERNAL_RESOLUTION]]; CoreDNS crashloop →
  [[TROUBLE-COREDNS_RESOLUTION_LOOP]].
- `LoadBalancer` `<pending>` → [[TROUBLE-METALLB_SERVICE_PENDING]]; control-plane VIP →
  [[TROUBLE-KUBE_VIP_VIP_NOT_UP]].
- Service unreachable / no endpoints → [[TROUBLE-SERVICE_NO_ENDPOINTS]].

### Access & control-plane↔node

- `kubectl exec/logs/port-forward` fails (`error dialing backend`, x509) →
  [[TROUBLE-KUBECTL_EXEC_LOGS_FAILS]].

### Certificates & TLS

- `x509 valid for … not <addr>` (apiserver) → [[TROUBLE-APISERVER_CERT_SAN]].
- `kubectl top`/metrics x509 (kubelet serving cert) → [[TROUBLE-KUBELET_SERVING_CERT_TLS]].
- x509 expired/not-yet-valid (clock) → [[TROUBLE-CLOCK_SKEW_TLS]].

### Images & registry

- Private/mirror pull fails → [[TROUBLE-CONTAINERD_REGISTRY_CONFIG]].
- `429 Too Many Requests` → [[TROUBLE-IMAGE_PULL_RATE_LIMIT]].

### Runtime & storage

- cgroup driver mismatch → [[TROUBLE-CGROUP_DRIVER_MISMATCH]].
- PVC `Pending` / no StorageClass → [[TROUBLE-PVC_PENDING_NO_STORAGECLASS]].
- `FailedMount` (ConfigMap/Secret/PVC) → [[TROUBLE-FAILEDMOUNT]].

### etcd & control plane

- Quorum loss / API down → [[TROUBLE-ETCD_QUORUM_LOSS]].
- `mvcc: database space exceeded` → [[TROUBLE-ETCD_DB_SPACE_EXCEEDED]].

### Cilium (indexed CNI)

- Helm ownership adopt error → [[TROUBLE-CILIUM_HELM_OWNERSHIP_ADOPT]].
- Config validation → [[TROUBLE-CILIUM_CONFIG_VALIDATION]].

### Security / CVEs

- Per-component CVE matrices (osv.dev): [[TROUBLE-KUBERNETES_KNOWN_CVES]],
  [[TROUBLE-RUNC_KNOWN_CVES]], [[TROUBLE-CONTAINERD_KNOWN_CVES]],
  [[TROUBLE-CILIUM_KNOWN_CVES]], [[TROUBLE-COREDNS_KNOWN_CVES]] (and cni-plugins,
  cert-manager, helm).

## References

- The `kb/troubleshooting/` layer (69 docs at time of writing). Diagnostic runbooks live
  under `kb/kubespray/guides/` (cluster health, DNS debug, node NotReady, etc.).
