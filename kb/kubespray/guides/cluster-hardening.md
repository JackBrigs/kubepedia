---
id: PRACTICE-CLUSTER_HARDENING
type: best_practice
title: "Cluster hardening (Kubespray hardening.yaml)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-21"
confidence: verified
aliases:
  - hardening
  - cluster hardening
  - CIS benchmark kubespray
  - PodSecurity restricted
  - encryption at rest
  - kubelet hardening
  - audit logging
tags:
  - security
  - hardening
  - best-practice
  - apiserver
  - kubelet
sources:
  - type: docs
    path: docs/operations/hardening.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/hardening.md
    note: "authoritative hardening.yaml reference (tag v2.31.0)"
  - type: code
    path: roles/kubernetes/control-plane/handlers/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/handlers/main.yml
    note: "'Control plane | Restart apiserver' removes the apiserver pod sandbox — the restart triggered by apiserver/audit/admission config changes"
  - type: code
    path: roles/kubernetes/node/handlers/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/handlers/main.yml
    note: "'Node | restart kubelet' — kubelet hardening flags restart kubelet on every node"
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "remove_anonymous_access default false (L79); docs/ansible/vars.md L318 — it removes the kubeadm:bootstrap-signer-clusterinfo rolebinding and drives kubeadm_use_file_discovery"
relations:
  - type: see_also
    target: VARIABLE-KUBE_OWNER
  - type: see_also
    target: TROUBLE-CILIUM_MOUNT_CGROUP_DENIED
  - type: see_also
    target: CONFIG-KUBELET_CONFIGURATION
  - type: see_also
    target: TROUBLE-KUBELET_SERVING_CERT_TLS
  - type: see_also
    target: PRACTICE-SECRETS_ENCRYPTION_AT_REST
---

# Cluster hardening (Kubespray hardening.yaml)

## Summary

Kubespray ships an authoritative **hardening** recipe (`docs/operations/hardening.md`):
a `hardening.yaml` overlay you pass with `-e @hardening.yaml` that tightens the API
server, controller-manager, scheduler, etcd, and kubelet toward CIS-style defaults —
audit logging, encryption at rest, PodSecurity `restricted`, TLS floors, cert rotation,
and admission controls. None of it is on by default; you opt in per cluster.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` (Kubernetes `1.31`–`1.35`, all ≥ the `1.23.6`
  floor for `PodSecurity`).
- Apply as an inventory overlay: `ansible-playbook cluster.yml -e @hardening.yaml`
  alongside your normal vars. Verify no other var overrides these.

## Implementation

**API server:**

- `authorization_modes: ['Node', 'RBAC']`; `kube_apiserver_request_timeout: 120s`;
  `kube_apiserver_service_account_lookup: true`.
- **Audit:** `kubernetes_audit: true` + `audit_log_path`, `audit_log_maxage: 30`,
  `audit_log_maxbackups: 10`, `audit_log_maxsize: 100`.
- **TLS floor:** `tls_min_version: VersionTLS12` + a restricted `tls_cipher_suites` set
  (ECDHE + AES-128-GCM / CHACHA20).
- **Encryption at rest:** `kube_encrypt_secret_data: true`,
  `kube_encryption_resources: [secrets]`, `kube_encryption_algorithm: "secretbox"`
  ([[PRACTICE-SECRETS_ENCRYPTION_AT_REST]]) — data is encrypted before it reaches etcd.
- **Admission plugins** (`kube_apiserver_enable_admission_plugins`): `EventRateLimit`,
  `AlwaysPullImages`, `ServiceAccount`, `NamespaceLifecycle`, **`NodeRestriction`**,
  `LimitRanger`, `ResourceQuota`, `MutatingAdmissionWebhook`,
  `ValidatingAdmissionWebhook`, `PodNodeSelector`, **`PodSecurity`**;
  `kube_apiserver_admission_control_config_file: true`; `EventRateLimit` limits via
  `kube_apiserver_admission_event_rate_limits`.
- `kube_profiling: false`; `remove_anonymous_access: true`.

**Controller-manager / scheduler:**

- `kube_controller_manager_bind_address: 127.0.0.1`,
  `kube_scheduler_bind_address: 127.0.0.1` (no exposed metrics/health on public IPs);
  `kube_controller_terminated_pod_gc_threshold: 50`;
  `kube_controller_feature_gates: ["RotateKubeletServerCertificate=true"]`.

**etcd:**

- `etcd_deployment_type: host` — running etcd on **dedicated hosts outside** the cluster
  isolates it from the CNI network and pod-level attack vectors (the most secure option).

**kubelet:**

- `kubelet_authorization_mode_webhook: true`, `kubelet_authentication_token_webhook: true`,
  `kube_read_only_port: 0`.
- `kubelet_rotate_certificates: true` **and** `kubelet_rotate_server_certificates: true`
  (with `serverTLSBootstrap`; CSRs auto-approved by kubelet-csr-approver —
  [[TROUBLE-KUBELET_SERVING_CERT_TLS]]).
- `kubelet_protect_kernel_defaults: true`, `kubelet_event_record_qps: 1`,
  `kubelet_streaming_connection_idle_timeout: "5m"`, `kubelet_make_iptables_util_chains: true`,
  `kubelet_seccomp_default: true`.
- `kubelet_systemd_hardening: true` + `kubelet_secure_addresses: …` — a minimal host
  firewall around the kubelet (see [[CONFIG-KUBELET_CONFIGURATION]]).

**Pod Security & files:**

- `kube_pod_security_use_default: true`, `kube_pod_security_default_enforce: restricted`
  (deny insecure pods cluster-wide; `kube-system` exempt by default).
- `kube_owner: root`, `kube_cert_group: root` (tighten file ownership).

## Service impact

Applying `hardening.yaml` to an **existing** cluster is a full `cluster.yml` run plus a set
of behaviour changes that can reject workloads. Treat it as a change window, not a tweak.

- **Control plane restarts.** The apiserver flags, audit config, admission-control config
  and encryption config are written by the control-plane role, and each of those template
  tasks notifies `Control plane | Restart apiserver`, which removes the apiserver pod
  sandbox (`crictl stopp/rmp`). The `cluster.yml` control-plane play has **no `serial`**, so
  by default this happens on **all control-plane nodes in parallel** — with a single
  control-plane node, that is a hard API outage; with HA, limit the run or accept a
  simultaneous bounce. Running workloads are unaffected; scheduling and API access are.
- **Every node's kubelet restarts.** The kubelet hardening flags change
  `kubelet-config.yaml`, which notifies `Node | restart kubelet`
  (`roles/kubernetes/node/handlers/main.yml`). A kubelet restart does not kill running
  containers, but the node is briefly `NotReady` and no pod on it can be started, probed or
  updated meanwhile.
- **`PodSecurity` enforce `restricted` is the sharpest edge.** It does **not** evict what is
  already running — it rejects **new** pods that violate the policy. Every deployment
  rollout, node drain, or pod recreation after the change can fail cluster-wide. Audit
  namespaces in `warn`/`audit` mode first and exempt what you must; only `kube-system` is
  exempt by default.
- **`kube_owner: root` re-owns files on every node** (Kubernetes config, certs and the CNI
  directories) — see [[VARIABLE-KUBE_OWNER]]. Note this is also the setting that makes stock
  Cilium work ([[TROUBLE-CILIUM_MOUNT_CGROUP_DENIED]]), so hardened clusters do not hit that
  failure.
- **`remove_anonymous_access: true` removes the `kubeadm:bootstrap-signer-clusterinfo`
  rolebinding** and switches node joins to file discovery
  (`kubeadm_use_file_discovery`). Kubespray-driven joins keep working; anything external
  that read `cluster-info` anonymously stops working.
- **Encryption at rest applies going forward only.** `kube_encrypt_secret_data: true`
  encrypts secrets as they are written; existing secrets stay in clear text in etcd until
  rewritten — see [[PRACTICE-SECRETS_ENCRYPTION_AT_REST]]. Losing the generated encryption
  key later makes those secrets unreadable, so back it up with the PKI.
- **`kubelet_systemd_hardening` + `kubelet_secure_addresses` install a host-level
  restriction around the kubelet.** A wrong address list locks the control plane out of the
  kubelet API: `kubectl logs/exec` and metrics break on that node.
- **Audit logging costs disk.** `audit_log_maxsize: 100` × `audit_log_maxbackups: 10` is up
  to ~1 GB per control-plane node; a full partition takes the apiserver down with it.
- **Rollout order:** apply to a staging cluster first, then one production control-plane
  node at a time via a limited run. **Backout** is another `cluster.yml` run without the
  overlay — plus manual work for anything the policy already rejected.

## References

- `docs/operations/hardening.md` at tag `v2.31.0` (the `hardening.yaml` reference).
  Kubelet config: [[CONFIG-KUBELET_CONFIGURATION]]; encryption at rest:
  [[PRACTICE-SECRETS_ENCRYPTION_AT_REST]]; server-cert rotation:
  [[TROUBLE-KUBELET_SERVING_CERT_TLS]].
