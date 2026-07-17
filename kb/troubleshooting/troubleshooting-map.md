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
- Stuck `Terminating` (pod) → [[TROUBLE-POD_STUCK_TERMINATING]]; namespace stuck
  `Terminating` → [[TROUBLE-NAMESPACE_STUCK_TERMINATING]].
- Evicted under disk pressure → [[TROUBLE-DISK_PRESSURE_EVICTION]].
- Deployment rollout stuck / `ProgressDeadlineExceeded` → [[TROUBLE-ROLLOUT_STUCK]].
- `too many open files` / inotify watch exhaustion → [[TROUBLE-INOTIFY_FILE_LIMITS]].

### Autoscaling & metrics

- HPA not scaling / `TARGETS <unknown>` → [[TROUBLE-HPA_NOT_SCALING]].

### Networking & DNS

- Cross-node pod traffic / MTU → [[TROUBLE-VXLAN_MTU_MISMATCH]]; conntrack drops →
  [[TROUBLE-CONNTRACK_TABLE_FULL]].
- Ports blocked by firewall → [[TROUBLE-FIREWALL_PORTS_BLOCKED]].
- External DNS fails → [[TROUBLE-DNS_EXTERNAL_RESOLUTION]]; CoreDNS crashloop →
  [[TROUBLE-COREDNS_RESOLUTION_LOOP]].
- Pods can't reach the internet (egress/masquerade) → [[TROUBLE-POD_EGRESS_INTERNET]].
- `LoadBalancer` `<pending>` → [[TROUBLE-METALLB_SERVICE_PENDING]]; control-plane VIP →
  [[TROUBLE-KUBE_VIP_VIP_NOT_UP]].
- Service unreachable / no endpoints → [[TROUBLE-SERVICE_NO_ENDPOINTS]].

### Access & control-plane↔node

- `kubectl exec/logs/port-forward` fails (`error dialing backend`, x509) →
  [[TROUBLE-KUBECTL_EXEC_LOGS_FAILS]].

- admission webhook blocks creates/updates (`failed calling webhook`) →
  [[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]].

- `Error from server (Forbidden)` (RBAC) → [[TROUBLE-RBAC_FORBIDDEN]].

### Certificates & TLS

- `x509 valid for … not <addr>` (apiserver) → [[TROUBLE-APISERVER_CERT_SAN]].
- `kubectl top`/metrics x509 (kubelet serving cert) → [[TROUBLE-KUBELET_SERVING_CERT_TLS]].
- x509 expired/not-yet-valid (clock) → [[TROUBLE-CLOCK_SKEW_TLS]].

### Images & registry

- `ImagePullBackOff`/`ErrImagePull` (triage) → [[TROUBLE-IMAGEPULLBACKOFF]].
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
- **Am I exposed? What to upgrade →** the consolidated runbook [[CONCEPT-CVE_REMEDIATION]].

### Upgrade jumps (moving toward latest — see [[CONCEPT-UPGRADE_HORIZON]])

- Argo CD 2→3 access/RBAC lost → [[TROUBLE-ARGOCD_UPGRADE_3_RBAC]].
- ingress-nginx annotation rejected → [[TROUBLE-INGRESS_NGINX_ANNOTATION_REJECTED]].
- Rook-Ceph `helm upgrade` SC immutable → [[TROUBLE-ROOK_CEPH_UPGRADE_SC_IMMUTABLE]].
- GPU Operator CDI/min-K8s → [[TROUBLE-GPU_OPERATOR_CDI_RUNTIMECLASS]].
- Envoy Gateway 1.6 backend TLS → [[TROUBLE-ENVOY_GATEWAY_BACKEND_TLS_SNI]].
- Velero 1.17 CRD/sequential → [[TROUBLE-VELERO_UPGRADE_117]].
- Capsule 0.10→0.13 webhooks/CRDs → [[TROUBLE-CAPSULE_UPGRADE_013]].
- Helm 3→4 → [[TROUBLE-HELM_3_TO_4_UPGRADE]]; registry 2→3 →
  [[TROUBLE-REGISTRY_2_TO_3_MIGRATION]]; snapshot 7→8 →
  [[TROUBLE-SNAPSHOT_CONTROLLER_7_TO_8]]; MetalLB config/FRR →
  [[TROUBLE-METALLB_CONFIG_CRD_FRR]].

### Storage & data (addons)

- PVC stuck Pending → [[TROUBLE-PVC_PENDING_NO_PROVISIONER]].
- Ceph HEALTH_WARN / OSD down → [[TROUBLE-ROOK_CEPH_HEALTH_WARN_OSD]].
- Postgres cluster not ready → [[TROUBLE-POSTGRES_OPERATOR_CLUSTER_NOT_READY]].
- RabbitMQ not clustering → [[TROUBLE-RABBITMQ_CLUSTER_NOT_FORMING]].
- Multiple snapshot-controllers conflict → [[TROUBLE-MULTIPLE_SNAPSHOT_CONTROLLERS]].

### Secrets & identity (addons)

- Vault pods 0/1 sealed → [[TROUBLE-VAULT_PODS_SEALED]].
- cert-manager Certificate not-ready → [[TROUBLE-CERT_MANAGER_CERTIFICATE_NOT_READY]].
- external-secrets not syncing → [[TROUBLE-EXTERNAL_SECRETS_NOT_SYNCING]].
- Dex OIDC login fails → [[TROUBLE-DEX_OIDC_LOGIN_FAILS]].
- Webhook↔cert-manager readiness ordering → [[TROUBLE-WEBHOOK_CERT_MANAGER_ORDERING]].

### Networking & load-balancing (addons)

- ingress-nginx 502/504 → [[TROUBLE-INGRESS_NGINX_502_504]].
- MetalLB no IP (CRD config) → [[TROUBLE-METALLB_CONFIG_CRD_FRR]]; BGP session down →
  [[TROUBLE-METALLB_BGP_SESSION_DOWN]].
- kube-vip control-plane VIP → [[TROUBLE-KUBE_VIP_CONTROL_PLANE_VIP]].
- Cilium pod connectivity → [[TROUBLE-CILIUM_POD_CONNECTIVITY]].
- Spegel mirror not used → [[TROUBLE-SPEGEL_MIRROR_NOT_USED]].

### Autoscaling, runtime & observability (addons)

- KEDA ScaledObject not scaling → [[TROUBLE-KEDA_SCALEDOBJECT_NOT_SCALING]].
- containerd pull/sandbox → [[TROUBLE-CONTAINERD_IMAGE_PULL_CRI]].
- vmagent not ingesting → [[TROUBLE-VMAGENT_REMOTE_WRITE_FAILING]].
- NFD labels missing → [[TROUBLE-NFD_LABELS_MISSING]].

## References

- The `kb/troubleshooting/` layer (110+ docs). Version/upgrade context:
  [[CONCEPT-UPGRADE_HORIZON]]; addon inventory: [[CONCEPT-ADDON_CATALOG]]. Diagnostic
  runbooks live under `kb/kubespray/guides/` (cluster health, DNS debug, node NotReady).
