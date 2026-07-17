---
id: CONCEPT-INSECURE_DEFAULTS
type: concept
title: "Insecure-by-default settings in a Kubespray cluster"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - insecure defaults
  - insecure by default kubespray
  - what is not secure out of the box
  - default security posture
  - secrets not encrypted by default
  - audit disabled by default
tags:
  - security
  - hardening
  - index
sources:
  - type: docs
    path: docs/operations/hardening.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/hardening.md
    note: "hardening overlay turns these ON; their default-off/weak state is the insecure default"
relations:
  - type: see_also
    target: CONCEPT-SECURITY_INDEX
  - type: see_also
    target: PRACTICE-CLUSTER_HARDENING
  - type: see_also
    target: TROUBLE-REGISTRY_ADDON
  - type: see_also
    target: TROUBLE-KUBELET_SERVING_CERT_TLS
  - type: see_also
    target: PRACTICE-SECRETS_ENCRYPTION_AT_REST
---

# Insecure-by-default settings in a Kubespray cluster

## Summary

Kubespray ships a **working** cluster, not a **hardened** one: most security controls are **off by
default** and enabled only via the `hardening.yaml` overlay ([[PRACTICE-CLUSTER_HARDENING]]). This
page inverts the hardening recipe into an **audit checklist** — each row is a default that is weak
out of the box, its risk, and the variable that fixes it. Every entry is source-derived from
Kubespray's own `docs/operations/hardening.md` (the overlay sets the secure value, so the default is
the insecure one). Stable across **v2.27.0–v2.31.0**.

## Context

**Data & secrets:**

| Default | Risk | Harden |
|---------|------|--------|
| `kube_encrypt_secret_data: false` | Secrets stored **plaintext in etcd** — anyone with etcd/backup access reads them | set `true` (secretbox) — [[VARIABLE-KUBE_ENCRYPT_SECRET_DATA]] / [[PRACTICE-SECRETS_ENCRYPTION_AT_REST]] |
| Registry addon open | In-cluster registry has **no auth, plain HTTP, emptyDir** (data loss) | [[TROUBLE-REGISTRY_ADDON]] — set htpasswd, TLS, storage class |

**Audit & admission:**

| Default | Risk | Harden |
|---------|------|--------|
| `kubernetes_audit: false` | **No audit trail** — no record of who did what | `true` + `audit_log_*` — [[VARIABLE-KUBERNETES_AUDIT]] |
| PodSecurity not enforced | Workloads can run **privileged / hostPath / hostNetwork** unchecked | enable `PodSecurity` admission + default policy — [[CONCEPT-POD_SECURITY_STANDARDS]], [[VARIABLE-KUBE_POD_SECURITY_USE_DEFAULT]], [[VARIABLE-KUBE_APISERVER_ENABLE_ADMISSION_PLUGINS]] |
| `remove_anonymous_access: false` | Anonymous requests reach the API/kubelet surface | `true` (hardening) |

**Exposure & TLS:**

| Default | Risk | Harden |
|---------|------|--------|
| `kubelet_rotate_server_certificates: false` | kubelet **serving cert is self-signed**; metrics-server runs with `--kubelet-insecure-tls` | enable rotation + CSR approver — [[TROUBLE-KUBELET_SERVING_CERT_TLS]] |
| `kube_read_only_port` enabled | kubelet **read-only port (10255)** exposes node/pod data unauthenticated | set `0` — [[VARIABLE-KUBE_READ_ONLY_PORT]] |
| controller-manager / scheduler bind `0.0.0.0` | metrics/health on **all interfaces** | bind `127.0.0.1` (hardening) |
| `kube_profiling: true` | **pprof debug endpoints** exposed on control-plane components | set `false` (hardening) |
| No `tls_min_version` floor | weak TLS versions/ciphers accepted | `tls_min_version: VersionTLS12` + restricted `tls_cipher_suites` (hardening) |

**How to use.** Walk each row against your inventory: anything left at the default is an accepted
risk you should be able to justify. Apply the full overlay
(`ansible-playbook cluster.yml -e @hardening.yaml`) to close the set at once — roll out PodSecurity
in `audit`/`warn` mode first so it doesn't reject running workloads. Full posture map:
[[CONCEPT-SECURITY_INDEX]].

**Not "bugs".** These are deliberate usability defaults, not defects — Kubespray documents them and
provides the overlay. The risk is leaving them at default **unknowingly**; this page exists so you
don't.

## References

- `docs/operations/hardening.md` (tag `v2.31.0`). Overlay [[PRACTICE-CLUSTER_HARDENING]]; posture
  index [[CONCEPT-SECURITY_INDEX]]; encryption [[PRACTICE-SECRETS_ENCRYPTION_AT_REST]]; registry
  [[TROUBLE-REGISTRY_ADDON]]; kubelet TLS [[TROUBLE-KUBELET_SERVING_CERT_TLS]].
