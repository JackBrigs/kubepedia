---
id: TROUBLE-KYVERNO_WEBHOOK_DENIES_UNAUTHORIZED
type: troubleshooting
title: "Kyverno webhook denies every patch with \"Unauthorized\" — the webhook is up, its own API client is not"
status: active
kubespray_version: null
kubernetes_version: ">=1.31 <=1.35"
component_version: "1.18.2"
verified_at: "2026-08-04"
confidence: verified
aliases:
  - denied the request the server has asked for the client to provide credentials
  - mutate.kyverno.svc-fail denied the request
  - kyverno Unauthorized failed to list
  - kyverno blocks cilium upgrade
  - cannot patch DaemonSet admission webhook denied
  - helm upgrade denied by kyverno
tags:
  - kyverno
  - troubleshooting
  - admission
  - upgrade
  - authentication
sources:
  - type: code
    path: staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/errors/statuserror.go
    url: https://github.com/kubernetes/kubernetes/blob/release-1.34/staging/src/k8s.io/apiserver/pkg/admission/plugin/webhook/errors/statuserror.go#L28-L29
    note: "ToStatusErr formats 'admission webhook %q denied the request' — used only when the webhook answered"
  - type: code
    path: staging/src/k8s.io/apiserver/pkg/util/webhook/error.go
    url: https://github.com/kubernetes/kubernetes/blob/release-1.34/staging/src/k8s.io/apiserver/pkg/util/webhook/error.go#L34-L39
    note: "ErrCallingWebhook formats 'failed calling webhook %q: %v' — used when the call itself failed"
  - type: code
    path: pkg/controllers/webhook/utils.go
    url: https://github.com/kyverno/kyverno/blob/v1.18.2/pkg/controllers/webhook/utils.go#L180-L187
    note: "webhookNameAndPath appends -fail / -ignore per failurePolicy; base name mutate.kyverno.svc from pkg/config/config.go L55"
relations:
  - type: see_also
    target: CONCEPT-ADDON_KYVERNO
  - type: see_also
    target: TROUBLE-KYVERNO_FAILURE_POLICY_SYSTEM_NS
  - type: see_also
    target: TROUBLE-ADMISSION_WEBHOOK_BLOCKING
  - type: see_also
    target: TROUBLE-KYVERNO_WEBHOOK_HA
---

# Kyverno webhook denies every patch with "Unauthorized" — the webhook is up, its own API client is not

## Summary

A cluster-wide admission failure that looks like the familiar "Kyverno is down" outage but is a
different fault with a different fix. Kyverno's pods are **running and answering AdmissionReviews**;
what fails is Kyverno's **own client to kube-apiserver**, which gets HTTP 401 on everything. Kyverno
turns that into `allowed: false`, so every create/update in the cluster is denied — and the denial
message carries the 401 text verbatim:

```
admission webhook "mutate.kyverno.svc-fail" denied the request:
the server has asked for the client to provide credentials
```

The two states are told apart **by the wording of the API server error alone**, before any
investigation. See Context.

## Problem

Observed during a Kubespray-driven Kubernetes upgrade: the Cilium step failed because every object of
the CNI release was refused at admission.

```
Error: Unable to upgrade Cilium: cannot patch "cilium" with kind DaemonSet:
admission webhook "mutate.kyverno.svc-fail" denied the request:
the server has asked for the client to provide credentials
&& cannot patch "cilium-envoy" ... && cannot patch "cilium-operator" ...
&& cannot patch "hubble-relay" ... && cannot patch "hubble-ui" ...
```

Five different objects, one message: the refusal is not about any object. Kyverno's own logs show the
same 401 against unrelated, low-privilege resources:

```
failed to list *v1.ClusterRole: Unauthorized
failed to list *v1.Lease: Unauthorized
failed to list *v1.ConfigMap: Unauthorized
failed to list *v1.MutatingWebhookConfiguration: Unauthorized
{"logger":"setup/runtime-checks","error":"Unauthorized","message":"failed to validate certificates"}
```

`failed to validate certificates` here is a **consequence** — Kyverno cannot read its own TLS secret —
not an independent certificate problem.

## Context

**Reading the API server message.** The API server produces exactly two shapes, from two code paths:

| Message | Meaning | Code path |
|---|---|---|
| `admission webhook "X" denied the request: <msg>` | the webhook **answered** `allowed: false`; `<msg>` is the webhook's own text | `ErrWebhookRejection` → `ToStatusErr` (`statuserror.go` L28-29) |
| `failed calling webhook "X": <err>` | the call **never completed** — unreachable, TLS failure, timeout — and `failurePolicy: Fail` closed the door | `ErrCallingWebhook` (`util/webhook/error.go` L34-39) |

So `denied the request:` proves the webhook process is alive. Any text after the colon originates
inside Kyverno, not in the API server. This is the whole diagnostic shortcut: it redirects the
investigation from "why is Kyverno down" (it isn't) to "why can Kyverno not authenticate".

**Reading the 401.** `Unauthorized` is 401, not 403. 403 would mean the identity is accepted and the
RBAC grant is missing — a specific resource would fail while others work. 401 means the **token is not
accepted at all**, which is why `ClusterRole`, `Lease` and `ConfigMap` fail together. Do not go
looking at ClusterRoleBindings: this is authentication, and RBAC is never consulted.

**The `-fail` suffix is not decoration.** Kyverno builds one webhook per failure policy and appends
the suffix accordingly — `mutate.kyverno.svc-fail` / `-ignore` (`utils.go` L180-187, base name
`mutate.kyverno.svc` from `config.go` L55). A denial arriving from the `-fail` variant means the
blocking half of the configuration is the one that fired.

**Why a CNI upgrade is the step that trips over it.** Kyverno's chart excludes only its own namespace
at `namespaceSelector`; `kube-system` appears solely in `config.resourceFilters`, which is a
policy-engine skip list evaluated *after* the request reaches Kyverno
([[TROUBLE-KYVERNO_FAILURE_POLICY_SYSTEM_NS]]). A `failurePolicy: Fail` webhook therefore sits between
the cluster and its own CNI, so any Kyverno fault stops the network upgrade.

**Candidate causes for a blanket 401**, in the order worth testing:

1. **The pod's projected service-account token went stale** and client-go kept presenting it. Plausible
   when the pod lived through control-plane work and could not refresh while API servers were cycling.
   A restart issues a fresh token and fixes it permanently.
2. **`sa.key`/`sa.pub` diverged between control-plane nodes**, so tokens minted by one API server are
   rejected by the others. Reachable by regenerating PKI on a different node — for example after
   reordering control-plane hosts in the Kubespray inventory, which moves `first_kube_control_plane`.
3. **The ServiceAccount was recreated**, leaving the token bound to a UID that no longer exists.

Cause (2) is cheaply **ruled out by evidence rather than inspection**: Kyverno reaches the API through
`kubernetes.default.svc`, which load-balances across all control-plane nodes. Divergent keys would fail
a *fraction* of requests indefinitely, so a sustained window with zero `Unauthorized` in a busy
controller's log is inconsistent with divergence. In the observed incident that window was clean, and
key comparison across nodes was not needed.

## Diagnostics

Confirm the webhook is answering rather than unreachable — that is the fork in the road:

```bash
# "denied the request:"  -> webhook alive, read on
# "failed calling webhook" -> different problem, see TROUBLE-ADMISSION_WEBHOOK_BLOCKING
kubectl -n kyverno logs deploy/kyverno-admission-controller --since=10m | grep -c Unauthorized
kubectl -n kyverno get pods
kubectl -n kyverno get sa
```

Decide between a stale pod token and divergent signing keys with one non-mutating test — the same
freshly minted token against each API server separately:

```bash
TOKEN=$(kubectl -n kyverno create token kyverno-admission-controller)
for ip in <cp1> <cp2> <cp3>; do
  curl -sk -o /dev/null -w "$ip %{http_code}\n" https://$ip:6443/api \
    -H "Authorization: Bearer $TOKEN"
done
```

Mixed codes mean the control-plane nodes disagree; uniform 401 points at the ServiceAccount; uniform
200 means only the running pod's token was bad. Confirm divergence directly when suspected:

```bash
# must be identical on every control-plane node
sudo md5sum /etc/kubernetes/pki/sa.key /etc/kubernetes/pki/sa.pub
grep -E 'service-account-(issuer|key-file|signing-key-file)' /etc/kubernetes/manifests/kube-apiserver.yaml
```

Note that `/openid/v1/jwks` cannot substitute for this: `system:service-account-issuer-discovery` is
not bound to `system:unauthenticated` by default, so an unauthenticated fetch returns an identical 403
body from every node — checksums of that body compare equal and prove nothing.

## Known Issues

- **Unblock an upgrade in progress.** Restart the admission controller first — it issues a fresh token
  and resolves cause (1) outright. If the denial persists, remove the blocking configuration for the
  duration of the work; Kyverno recreates it once healthy. Editing `failurePolicy` by hand is not
  durable while Kyverno is alive: its webhook controller reconciles the change away.

  ```bash
  kubectl -n kyverno rollout restart deploy/kyverno-admission-controller
  kubectl get mutatingwebhookconfigurations | grep kyverno
  kubectl delete mutatingwebhookconfiguration kyverno-resource-mutating-webhook-cfg
  ```

- **Check the Helm release before retrying.** The failed `helm upgrade` can leave the release in
  `pending-upgrade`, and the next Kubespray run then aborts with "another operation in progress".
  `helm -n kube-system history cilium`, and roll back if the top revision is pending.

- **If keys diverged**, `--service-account-key-file` accepts a PEM file holding **several** public
  keys. Concatenating both `sa.pub` versions on every node revalidates old and new tokens at once and
  restores the cluster without downtime; converge on a single pair afterwards, and keep
  `kube-controller-manager --service-account-private-key-file` consistent with it, since it signs with
  the same key.

- **Prevent the recurrence at the right layer.** Exclude system namespaces at `namespaceSelector`, not
  in `resourceFilters`. Until then a policy-engine fault is also a CNI-upgrade outage, and the cluster
  cannot heal itself while the block is in force.

- **Disabling Kyverno for the upgrade window works but establishes nothing.** In the observed incident
  the operator disabled Kyverno, completed the upgrade, and re-enabled it; the restart alone would have
  cleared cause (1). Because the original pod was gone, the cause could not be confirmed afterwards —
  capture the token test above **before** restarting anything if the answer matters.

## References

- Kubernetes `release-1.34`: `statuserror.go` (denial format), `util/webhook/error.go` (call-failure
  format), `mutating/dispatcher.go` L330 (rejection path). Verified 2026-08-04.
- Kyverno `v1.18.2`: `pkg/controllers/webhook/utils.go` L180-187, `pkg/config/config.go` L55.
- Webhook exclusion topology: [[TROUBLE-KYVERNO_FAILURE_POLICY_SYSTEM_NS]]; unreachable-webhook case:
  [[TROUBLE-ADMISSION_WEBHOOK_BLOCKING]]; availability: [[TROUBLE-KYVERNO_WEBHOOK_HA]].
