---
id: CONFIG-APISERVER_AUDIT
type: configuration
title: "API server audit logging in Kubespray"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubernetes audit
  - audit logging
  - kubernetes_audit
  - audit policy file
  - apiserver audit log
tags:
  - kubernetes
  - security
  - audit
  - apiserver
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "kubernetes_audit, audit_log_*, audit_policy_file defaults (tag v2.31.0)"
relations:
  - type: see_also
    target: PRACTICE-CLUSTER_HARDENING
  - type: see_also
    target: CONCEPT-POD_SECURITY_STANDARDS
---

# API server audit logging in Kubespray

## Summary

Kubernetes audit records **who did what** on the API server. Kubespray can enable the
audit **log backend** (`kubernetes_audit`, off by default): it wires an audit policy file
and a rotating log on each control-plane node. Essential for security forensics and
compliance — without it, API activity is not recorded.

## Configuration

Defaults (`kube_config_dir` = `/etc/kubernetes`):

| Variable | Default | Purpose |
|----------|---------|---------|
| `kubernetes_audit` | `false` | master switch — enable audit logging |
| `audit_policy_file` | `{kube_config_dir}/audit-policy/apiserver-audit-policy.yaml` | the audit policy (which events, at what level) |
| `audit_log_path` | `/var/log/audit/kube-apiserver-audit.log` | log file (`-` = stdout) |
| `audit_log_maxage` | `30` | days to retain |
| `audit_log_maxbackups` | `10` | rotated files to keep |
| `audit_log_maxsize` | `100` | MB before rotation |
| `audit_log_hostpath` | `/var/log/kubernetes/audit` | host dir mounted into the apiserver pod |
| `audit_log_mountpath` | dirname of `audit_log_path` | mount point inside the pod |

- Enabling `kubernetes_audit` renders the policy file and adds the apiserver
  `--audit-policy-file` / `--audit-log-*` flags plus the hostPath mount so the static
  apiserver pod can write the log.
- The **policy file** controls verbosity: levels `None`/`Metadata`/`Request`/
  `RequestResponse` per resource/verb. Tune it — `RequestResponse` on everything is huge.
- A **webhook** backend (ship audit events to an external sink) is configurable
  separately: `kubernetes_audit_webhook: true` with `audit_webhook_config_file`,
  `audit_webhook_server_url`, `audit_webhook_mode: batch` (`audit_webhook_batch_max_size:
  100`, `audit_webhook_batch_max_wait: 1s`) — use it for centralized collection instead of
  (or alongside) local files.

## Compatibility

- Applies to Kubespray `v2.29.0`–`v2.31.0`. Enabled as part of
  [[PRACTICE-CLUSTER_HARDENING]] (which also sets retention 30/10/100).
- Audit logs live on each control-plane node under `audit_log_hostpath`; ship them off-box
  (or use the webhook backend) — local logs are lost if the node dies.
- A verbose policy adds apiserver load and disk churn; scope it to security-relevant
  events (auth, RBAC, secret access, exec) rather than everything.
- Combine with PodSecurity audit annotations ([[CONCEPT-POD_SECURITY_STANDARDS]]) for a
  fuller picture of policy violations.

## References

- `kubernetes_audit` / `audit_*` defaults at tag `v2.31.0`. Hardening context:
  [[PRACTICE-CLUSTER_HARDENING]].
