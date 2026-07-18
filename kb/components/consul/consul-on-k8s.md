---
id: CONCEPT-CONSUL_ON_K8S
type: concept
title: "Consul on Kubernetes (consul-k8s) — overview & why it bites"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.22.7 <=2.0.2"
verified_at: "2026-07-18"
confidence: verified
aliases:
  - consul on kubernetes
  - consul-k8s
  - hashicorp consul kubernetes
  - consul service mesh k8s
  - consul helm chart
tags:
  - consul
  - service-mesh
  - concept
sources:
  - type: code
    path: charts/consul/Chart.yaml
    url: https://github.com/hashicorp/consul-k8s/blob/v2.0.2/charts/consul/Chart.yaml
    note: "chart 2.0.2 = appVersion 2.0.2; kubeVersion >=1.22.0-0"
  - type: code
    path: charts/consul/values.yaml
    url: https://github.com/hashicorp/consul-k8s/blob/v2.0.2/charts/consul/values.yaml
    note: "global.image hashicorp/consul:2.0.2; imageK8S consul-k8s-control-plane:2.0.2; dataplane 2.0.2; Envoy v1.38.3"
relations:
  - type: see_also
    target: TROUBLE-CONSUL_CONNECT_INJECT_WEBHOOK
  - type: see_also
    target: TROUBLE-CONSUL_ACL_BOOTSTRAP
  - type: see_also
    target: TROUBLE-CONSUL_SERVER_QUORUM
  - type: see_also
    target: TROUBLE-CONSUL_UPGRADE_1X_TO_2X
---

# Consul on Kubernetes (consul-k8s) — overview & why it bites

## Summary

HashiCorp **Consul** runs on Kubernetes via the **consul-k8s** Helm chart (+ its control-plane and
Consul Dataplane images). It is **operator-deployed, not Kubespray-managed** — you own its lifecycle.
It has a reputation for operational pain, and the pain concentrates in four places: a **mutating
admission webhook** (connect-inject) that can block pod scheduling cluster-wide, **ACL bootstrap**
brittleness, **Raft quorum** on the server StatefulSet (etcd-class), and a hard **1.x → 2.x** upgrade
rewrite. This doc pins the versions and routes each problem to its detail.

## Context

- **Version pinning (lockstep):** consul-k8s **chart 2.0.2 = Consul `2.0.2`** + `consul-dataplane:2.0.2`
  + control-plane `2.0.2` + Envoy `v1.38.3` (`values.yaml`@v2.0.2). The previous line **chart 1.9.10 =
  Consul `1.22.7`** (`Chart.yaml`@v1.9.10). 2.x is a **rewrite** — you cannot mix a 1.x chart's Consul
  with 2.x tooling. The full chart↔Consul↔K8s matrix lives at HashiCorp's docs (external, authoritative).
- **Kubernetes floor:** the chart refuses to render on **K8s < 1.22** (`kubeVersion: ">=1.22.0-0"`);
  the default namespace exclusions rely on the `kubernetes.io/metadata.name` label (K8s ≥1.21.1).
- **Architecture (the moving parts that break):**
  - **Consul servers** — a StatefulSet running Raft; `server.replicas` default **1** (no fault
    tolerance out of the box) — [[TROUBLE-CONSUL_SERVER_QUORUM]].
  - **connect-inject** — a Deployment + a **MutatingWebhookConfiguration on pod CREATE**
    (`failurePolicy: Fail` by default) that injects the mesh sidecar — [[TROUBLE-CONSUL_CONNECT_INJECT_WEBHOOK]].
  - **ACLs** — a `server-acl-init` Job bootstraps ACLs and writes the bootstrap token to a Secret —
    [[TROUBLE-CONSUL_ACL_BOOTSTRAP]].
  - **TLS/gossip** — `global.tls.verify: true` by default; gossip encryption off by default but breaks
    silently on a key mismatch; a `webhook-cert-manager` rotates the webhook's serving cert.
  - **Consul Dataplane + Envoy** — the sidecar data plane (2.x default; no more per-node client agent).

**Why it "creates many problems".** Two of its core components are **cluster-wide chokepoints**: the
connect-inject webhook (a down injector rejects pod creation everywhere not excluded) and the server
Raft quorum (lose it and every server goes NotReady, which cascades back into the webhook). Add ACL
bootstrap state that can't be re-created after PV loss, and TLS/`verify: true` that breaks RPC if
enabled in one shot on a running cluster, and you get the reputation.

## References

- consul-k8s `charts/consul/{Chart.yaml,values.yaml}` @v2.0.2 (versions) and @v1.9.10 (prev line).
  Problem detail: connect-inject [[TROUBLE-CONSUL_CONNECT_INJECT_WEBHOOK]], ACL
  [[TROUBLE-CONSUL_ACL_BOOTSTRAP]], quorum [[TROUBLE-CONSUL_SERVER_QUORUM]], upgrade
  [[TROUBLE-CONSUL_UPGRADE_1X_TO_2X]]. Not a Kubespray-managed component (operator-deployed).
