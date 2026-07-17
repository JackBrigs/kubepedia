---
id: PRACTICE-RUNBOOK_SECRETS_ENCRYPTION
type: best_practice
title: "Runbook: enable secrets encryption at rest (and re-encrypt existing secrets)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: confirmed
aliases:
  - enable secrets encryption runbook
  - encrypt secrets at rest
  - kube_encrypt_secret_data
  - rewrite existing secrets
  - secretbox encryption
tags:
  - runbook
  - operations
  - security
  - secrets
sources:
  - type: docs
    path: docs/operations/encrypting-secret-data-at-rest.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/operations/encrypting-secret-data-at-rest.md
    note: "kube_encrypt_secret_data (default false); providers identity/secretbox/aesgcm/aescbc/kms; existing secrets must be rewritten"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: depends_on
    target: VARIABLE-KUBE_ENCRYPT_SECRET_DATA
  - type: depends_on
    target: PRACTICE-SECRETS_ENCRYPTION_AT_REST
  - type: see_also
    target: CONCEPT-SECRETS_MANAGEMENT
  - type: see_also
    target: CONCEPT-INSECURE_DEFAULTS
---

# Runbook: enable secrets encryption at rest (and re-encrypt existing secrets)

## Summary

By default Kubespray stores Secrets **plaintext in etcd** (`kube_encrypt_secret_data: false` —
[[CONCEPT-INSECURE_DEFAULTS]]). This runbook turns on encryption at rest and — the step operators
forget — **rewrites existing Secrets** so the ones already in etcd actually get encrypted (enabling
the provider only encrypts **future** writes). Kubespray's default provider is **secretbox**;
mechanics and provider trade-offs are in [[PRACTICE-SECRETS_ENCRYPTION_AT_REST]].

## Context

- **Enabling ≠ encrypting what's already there.** The EncryptionConfiguration applies on **write** —
  existing Secrets stay as-is until re-written (Step 3). Skipping the rewrite leaves old secrets
  plaintext in etcd forever.
- **Provider choice** ([[VARIABLE-KUBE_ENCRYPT_SECRET_DATA]] + provider vars): `secretbox` (Kubespray
  default, good general choice); `aesgcm` needs key rotation ~every 200k writes; `aescbc` not
  recommended (padding oracle); `kms` is the upstream recommendation but needs an external KMS;
  `identity` = no encryption. Pick before you start.
- **Key custody:** the encryption key lives in the EncryptionConfiguration on the control-plane
  nodes — protect and back it up; losing it while secrets are encrypted makes them unreadable.
- Stable across **v2.27.0–v2.31.0**; part of the hardening overlay.

## Implementation

**Step 0 — Snapshot etcd** ([[PRACTICE-RUNBOOK_ETCD_BACKUP]]) — you're changing how control-plane
state is written.

**Step 1 — Set the variable** in inventory ([[VARIABLE-KUBE_ENCRYPT_SECRET_DATA]]):

```yaml
kube_encrypt_secret_data: true
kube_encryption_resources: [secrets]
kube_encryption_algorithm: "secretbox"   # or aesgcm / kms
```

**Step 2 — Apply** (writes the EncryptionConfiguration and restarts the apiserver):

```bash
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/cluster.yml -b
```

**Step 3 — Re-encrypt every existing Secret** (the critical step — rewrites them through the new
provider):

```bash
kubectl get secrets -A -o json | kubectl replace -f -
```

**Step 4 — Verify** the data is encrypted in etcd (read the raw key on an etcd node — it should start
with `k8s:enc:secretbox:` not plaintext):

```bash
ETCDCTL_API=3 etcdctl get /registry/secrets/<ns>/<name> | hexdump -C | head
# expect the k8s:enc:<provider>: prefix, not readable YAML
```

**Rollback.** To disable, set the provider back so `identity` is **first** in the provider list and
re-run, then re-write Secrets again (Step 3) to decrypt them — order matters (the first provider is
used for writes, all listed providers for reads). Never remove the old provider from the read list
until every Secret has been rewritten, or you lose the ability to decrypt them. The Step 0 snapshot is
the hard backstop.

## References

- `docs/operations/encrypting-secret-data-at-rest.md` (tag `v2.31.0`). Mechanics
  [[PRACTICE-SECRETS_ENCRYPTION_AT_REST]]; variable [[VARIABLE-KUBE_ENCRYPT_SECRET_DATA]]; secrets
  strategy [[CONCEPT-SECRETS_MANAGEMENT]]; default posture [[CONCEPT-INSECURE_DEFAULTS]]; index
  [[CONCEPT-RUNBOOKS_INDEX]].
