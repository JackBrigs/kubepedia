---
id: TAG-ETCD_SECRETS
type: ansible_tag
title: etcd-secrets (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - etcd-secrets
  - --tags etcd-secrets
tags:
  - ansible-tag
  - etcd
  - certificates
sources:
  - type: code
    path: roles/etcd/tasks/main.yml
    lines: "3-30"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.1/roles/etcd/tasks/main.yml
    note: "etcd-secrets tags check_certs.yml, gen_certs_script.yml, upd_ca_trust.yml"
  - type: code
    path: playbooks/install_etcd.yml
    lines: "24"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.1/playbooks/install_etcd.yml
    note: "role: etcd; imported by cluster.yml via playbooks/cluster.yml"
relations:
  - type: see_also
    target: COMPONENT-ETCD
  - type: see_also
    target: VARIABLE-ETCD_DEPLOYMENT_TYPE
---

# etcd-secrets (Ansible run-tag)

## Summary

`etcd-secrets` is the Kubespray run-tag that manages etcd certificates. Running
`ansible-playbook cluster.yml --tags etcd-secrets` executes the etcd
certificate check and generation tasks — this is the tag that (re)generates etcd
certificates. Verified present and stable across `v2.29.0`–`v2.31.0` (including
`v2.29.1`).

## Context

- **Playbooks:** available wherever the `etcd` role runs — `cluster.yml` (through
  `playbooks/cluster.yml` → `playbooks/install_etcd.yml`), `scale.yml`, and
  `upgrade-cluster.yml`.
- **Affected host groups:** `etcd` (server/peer certificates) and the
  `k8s_cluster` nodes that receive client certificates (the etcd play runs on
  `hosts: k8s_cluster:etcd`).
- **Role:** `etcd` (`roles/etcd/tasks/main.yml`).

## Implementation

In `roles/etcd/tasks/main.yml` the tag `etcd-secrets` is attached to three
included task files:

```yaml
- include_tasks: check_certs.yml         # tags: [etcd-secrets]
- include_tasks: gen_certs_script.yml    # tags: [etcd-secrets]  ← generates etcd certs
- include_tasks: upd_ca_trust.yml        # tags: [etcd-secrets]
```

- `check_certs.yml` — inspects existing etcd certificates and decides what must be
  (re)generated.
- `gen_certs_script.yml` — generates the etcd certificates via the certificate
  script. This is the step that produces/refreshes the cert files.
- `upd_ca_trust.yml` — updates the CA trust store.

Generation is idempotent: it creates missing or changed certificates rather than
force-rotating already-valid ones. To force regeneration of valid certificates,
remove/invalidate them first, then run the tag.

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: the tag and its tasks are unchanged (4
  `etcd-secrets` occurrences in `roles/etcd/tasks/main.yml` in every tag,
  including `v2.29.1`).
- **Standalone-run safety: risky.** The tasks require gathered facts and the
  `etcd`/`k8s_cluster` host context. Running only this tag generates/updates
  certificate files but does not itself run the etcd install/config tasks (those
  carry other tags); a certificate change in a normal full run propagates further
  (e.g. `etcd_secret_changed`). Rotate deliberately, not casually.

## References

- `roles/etcd/tasks/main.yml:3-30` — `etcd-secrets` on `check_certs.yml`,
  `gen_certs_script.yml`, `upd_ca_trust.yml`.
- `playbooks/install_etcd.yml` (`role: etcd`), imported by `cluster.yml`.
- Verified on tags v2.29.0 `9991412`, **v2.29.1 `0c6a295`**, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
