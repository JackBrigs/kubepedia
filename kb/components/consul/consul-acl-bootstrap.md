---
id: TROUBLE-CONSUL_ACL_BOOTSTRAP
type: troubleshooting
title: "Consul ACL bootstrap brittleness (server-acl-init) — can't re-bootstrap, policies overwritten"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.22.7 <=2.0.2"
verified_at: "2026-07-18"
confidence: verified
aliases:
  - consul server-acl-init fails
  - ACL bootstrap no longer allowed
  - consul bootstrap token secret
  - consul acl permission denied loop
  - manageSystemACLs
tags:
  - consul
  - troubleshooting
  - acl
  - security
sources:
  - type: code
    path: charts/consul/values.yaml
    url: https://github.com/hashicorp/consul-k8s/blob/v2.0.2/charts/consul/values.yaml
    note: "global.acls.manageSystemACLs; bootstrapToken secret semantics (L424,L438-464); replicationToken; acls.resources default 50Mi/50m"
  - type: code
    path: charts/consul/templates/server-acl-init-job.yaml
    url: https://github.com/hashicorp/consul-k8s/blob/v2.0.2/charts/consul/templates/server-acl-init-job.yaml
    note: "hard-fails on half-set token pairs; global.bootstrapACLs removed → use manageSystemACLs"
relations:
  - type: see_also
    target: CONCEPT-CONSUL_ON_K8S
  - type: see_also
    target: TROUBLE-CONSUL_SERVER_QUORUM
---

# Consul ACL bootstrap brittleness (server-acl-init) — can't re-bootstrap, policies overwritten

## Summary

With `global.acls.manageSystemACLs: true`, a **`server-acl-init` Job** bootstraps Consul ACLs and
writes the bootstrap token to a Secret. Its behavior hinges on **Secret state**: an empty Secret →
it bootstraps and writes the token; a populated Secret → it **skips** server bootstrap. The trap: if
ACLs were already bootstrapped on the servers but the Secret is lost/empty (e.g. after PV loss), the
Job **cannot re-bootstrap** (Consul returns `ACL bootstrap no longer allowed`) → every component loops
on permission-denied. Plus, **managed ACL policies are overwritten on every `helm upgrade`**.

## Problem

- `server-acl-init` Job fails; component pods (connect-injector, sync-catalog, etc.) loop on
  `Permission denied` / ACL errors.
- After restoring servers from a snapshot or losing the bootstrap Secret: `ACL bootstrap no longer
  allowed`.
- After a `helm upgrade`: manual edits to Consul ACL policies silently reverted.

## Context

- Applies to consul-k8s **1.9.x–2.0.x** ([[CONCEPT-CONSUL_ON_K8S]]). The bootstrap token Secret default
  is `<global.name>-bootstrap-acl-token` (key `token`); its empty-vs-populated state decides whether
  the Job bootstraps (`values.yaml`@v2.0.2 L424/L438-464).
- **Template `fail` traps:** supplying only one of `bootstrapToken.secretName`/`secretKey` (or the
  `replicationToken` pair) **hard-fails** the render; the removed `global.bootstrapACLs` hard-fails
  with "use `global.acls.manageSystemACLs` instead" (`server-acl-init-job.yaml`@v2.0.2 L5-9).
- **Upgrade overwrite:** "All policies managed by consul-k8s will now be updated on upgrade. If you
  previously edited the policies after install, your changes will be overwritten" (changelog).
- **Replication/federation:** `createReplicationToken` is valid only in the **primary** DC; secondary
  DCs import via a `replicationToken` Secret. (Login timeout for ACL replication was raised to 60s to
  stop early failures.)

## Diagnostics

- `kubectl logs job/<release>-server-acl-init` → look for `Bootstrap Token`, `bootstrap no longer
  allowed`, `Permission denied`.
- `kubectl get secret <release>-bootstrap-acl-token -o jsonpath='{.data.token}'` — exists and
  non-empty? (empty after data loss = the re-bootstrap trap).
- Confirm `global.acls.manageSystemACLs` and that both parts of any token secret pair are set.

## Known Issues

- **Fix (re-bootstrap after data loss):** because a restored leader has no ACL state, you must reset
  the ACL bootstrap on the servers (write the reset index Consul reports into `acl-bootstrap-reset` on
  each server), then let the Job repopulate the Secret. The chart only supports the "empty Secret →
  bootstrap" path; the reset procedure is a Consul-server operation, not a chart value. *(Exact
  reset steps are a Consul server operation, unverified against this chart tag.)*
- **Fix (don't lose edits):** do not hand-edit consul-k8s-managed ACL policies — they're reapplied on
  upgrade. Manage extra policies out-of-band.
- **Fix (Vault backend):** with Vault you must supply `bootstrapToken`/`replicationToken` secretName;
  KV-v2 paths need the `data` path component.
- **Resource:** `acls.resources` defaults to a tiny `50Mi`/`50m` — under large ACL sets the Job can be
  starved; raise it.
- **Ties to quorum:** ACL state lives in Consul's Raft store — losing the server PVCs
  ([[TROUBLE-CONSUL_SERVER_QUORUM]]) is what triggers the re-bootstrap trap in the first place.

## References

- consul-k8s `values.yaml` + `server-acl-init-job.yaml` (@v2.0.2), changelog (policy-overwrite,
  server-IP-churn, replication timeout). Overview [[CONCEPT-CONSUL_ON_K8S]]; quorum/PV loss
  [[TROUBLE-CONSUL_SERVER_QUORUM]].
