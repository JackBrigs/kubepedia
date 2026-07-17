---
id: CONCEPT-ADDON_CATALOG
type: concept
title: "Application-platform addon catalog (owner inventory)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-17"
confidence: verified
aliases:
  - addon catalog
  - addon inventory
  - helm chart inventory
  - platform addons
  - installed addons
tags:
  - addons
  - inventory
  - helm
  - catalog
sources:
  - type: other
    path: owner-provided inventory
    note: "chart/app versions supplied by the cluster owner (2026-07-17) — verified as deployed-environment facts, not upstream defaults"
relations:
  - type: see_also
    target: CONCEPT-KUBERNETES_VERSION_SUPPORT
  - type: see_also
    target: CONCEPT-HELM_IN_KUBESPRAY
---

# Application-platform addon catalog (owner inventory)

## Summary

This is the **inventory index** of Helm-chart addons the owner deploys on their clusters —
a distinct layer from the Kubespray-managed components (`COMPONENT-*`). These charts are
installed **independently of Kubespray**; where a name overlaps a Kubespray add-on
(cert-manager, argocd, ingress-nginx, velero) the owner runs a **newer, independent chart
version**, so the addon entry here does **not** replace the Kubespray `COMPONENT-*` doc — it
relates to it and records the divergence (decision **D-015**).

Versions below are **owner-provided facts about the deployed environment** (`verified` as
inventory), not upstream defaults. The **Doc** column is the depth tracker: `catalog` = this
index only; `CONCEPT-ADDON_<X>` = a dedicated deep doc exists.

## Context

- **Class:** `upstream` = public project (researchable: K8s-compat, breaking changes, known
  issues, CVEs). `in-house` = proprietary chart ("собственный") with no public source —
  recorded as inventory only, behaviour never fabricated.
- **Cluster range:** these run on the same Kubernetes `1.29`–`1.35` window the base covers
  ([[CONCEPT-KUBERNETES_VERSION_SUPPORT]]); per-addon Kubernetes compatibility lives in each
  deep doc.
- Deep docs are created in prioritized batches (security / storage / platform-critical
  first). This table is the completeness anchor.

## Implementation

### Secrets & identity

| Addon | Upstream | Chart | App | Class | Doc |
|-------|----------|-------|-----|-------|-----|
| vault | HashiCorp vault | 0.32.0 | 1.21.2¹ | upstream | [[CONCEPT-ADDON_VAULT]] |
| vault-secrets-webhook | bank-vaults | 1.21.4 | — | upstream | [[CONCEPT-ADDON_VAULT_SECRETS_WEBHOOK]] |
| 1password-connect | connect | 1.17.0 | 1.7.3 | upstream | [[CONCEPT-ADDON_1PASSWORD_CONNECT]] |
| dex | dex (+ userinfo-provider 0.1.0, kubectl-web 0.0.1) | 0.23.0 | — | upstream | [[CONCEPT-ADDON_DEX]] |
| cert-manager | cert-manager | — | v1.18.2 | upstream | [[CONCEPT-ADDON_CERT_MANAGER]] (overlaps [[COMPONENT-CERT_MANAGER]]) |
| talos-kms | in-house | 0.0.1 | — | in-house | catalog |

### GitOps, CI & progressive delivery

| Addon | Upstream | Chart | App | Class | Doc |
|-------|----------|-------|-----|-------|-----|
| argocd | argo-cd | 8.5.7 | — | upstream | [[CONCEPT-ADDON_ARGOCD]] |
| gitlab-agent | gitlab-agent | 2.22.1 / 2.26.0 | — | upstream | [[CONCEPT-ADDON_GITLAB_AGENT]] |
| gitlab-runner | gitlab-runner | 0.81.0 | 18.4.0 | upstream | [[CONCEPT-ADDON_GITLAB_RUNNER]] |
| gitlab-com-runner | gitlab-runner | 0.63.0 | 16.10.0 | upstream | [[CONCEPT-ADDON_GITLAB_RUNNER]] |
| gitlab-ci-control | in-house | 0.0.1 | — | in-house | catalog |
| gitlab-runners-rbac | in-house | 0.0.1 | — | in-house | catalog |
| flagger | flagger | 1.40.0 | — | upstream | [[CONCEPT-ADDON_FLAGGER]] |

### Observability

| Addon | Upstream | Chart | App | Class | Doc |
|-------|----------|-------|-----|-------|-----|
| vm | victoria-metrics-k8s-stack (+ vmalert 0.17.0, grafana-operator v5.18.0, oauth2-proxy 8.1.0, helm-exporter 1.2.16) | 0.42.0 | — | upstream | [[CONCEPT-ADDON_VM_K8S_STACK]] |
| alertmanager | prometheus-community alertmanager | 0.28.0 | — | upstream | [[CONCEPT-ADDON_ALERTMANAGER]] |
| grafana | in-house (Grafana Operator CR) | 0.0.1 | 11.6.4 | in-house | catalog |
| karma | karma (+ oauth2-proxy 8.3.1) | 2.11.0 | v0.121 | upstream | [[CONCEPT-ADDON_KARMA]] |
| pyrra | pyrra | 1.1.0 | v0.9.4¹ | upstream | [[CONCEPT-ADDON_PYRRA]] |
| vector | vector-operator | 0.7.2 | — | upstream | [[CONCEPT-ADDON_VECTOR_OPERATOR]] |
| opentelemetry | opentelemetry | — | — | upstream | [[CONCEPT-ADDON_OTEL_OPERATOR]] |
| opentelemetry-operator | opentelemetry-operator (all versions) | — | — | upstream | [[CONCEPT-ADDON_OTEL_OPERATOR]] |
| release-watcher | release-watcher | 0.0.9 | — | upstream | [[CONCEPT-ADDON_RELEASE_WATCHER]] |
| headlamp | headlamp | 0.43.0 | — | upstream | [[CONCEPT-ADDON_HEADLAMP]] |
| dashboard | kubernetes-dashboard (+ oauth2-proxy 8.1.1) | 7.6.1 | — | upstream | [[CONCEPT-ADDON_KUBERNETES_DASHBOARD]] |

### Storage & data

| Addon | Upstream | Chart | App | Class | Doc |
|-------|----------|-------|-----|-------|-----|
| rook-operator | rook-ceph | 1.18.9 | — | upstream | [[CONCEPT-ADDON_ROOK_CEPH]] |
| rook-ceph-cluster | rook-ceph-cluster | 1.18.9 | — | upstream | [[CONCEPT-ADDON_ROOK_CEPH]] |
| csi-cephfs | ceph-csi-cephfs | 3.14.2 / 3.13.0 | — | upstream | [[CONCEPT-ADDON_CEPH_CSI_CEPHFS]] |
| cephbucket | in-house | current / v1.1.35 | 1.0.0 | in-house | catalog |
| lvm-localpv | OpenEBS lvm-localpv | 1.7.0 | — | upstream | [[CONCEPT-ADDON_LVM_LOCALPV]] |
| snapshotter | external-snapshotter (local) | v6.3.0 | — | upstream | [[CONCEPT-ADDON_SNAPSHOTTER]] (overlaps [[COMPONENT-SNAPSHOT_CONTROLLER]]) |
| volsync | volsync | 0.15.0 | 0.15.0¹ | upstream | [[CONCEPT-ADDON_VOLSYNC]] |
| k8up | k8up (+ k8upcrd 0.1.0) | 4.8.4 | — | upstream | [[CONCEPT-ADDON_K8UP]] |
| velero | velero | 11.4.0 | 1.17.1 | upstream | [[CONCEPT-ADDON_VELERO]] |
| zalando-postgres-operator | postgres-operator | 1.14.0 | — | upstream | [[CONCEPT-ADDON_ZALANDO_POSTGRES_OPERATOR]] |
| rabbitmq | rabbitmq-cluster-operator (bitnami) | 3.7.0 | — | upstream | [[CONCEPT-ADDON_RABBITMQ_BITNAMI]] |
| rabbitmq-cluster-operator | cluster-operator (kustomize) | v2.19.2 | — | upstream | [[CONCEPT-ADDON_RABBITMQ_CLUSTER_OPERATOR]] |
| dragonfly | dragonfly-operator (local) | v1.1.11 | — | upstream | [[CONCEPT-ADDON_DRAGONFLY]] |
| elastic | eck-operator | 3.1.0 | — | upstream | [[CONCEPT-ADDON_ECK_OPERATOR]] |

### Networking, gateways & ingress

| Addon | Upstream | Chart | App | Class | Doc |
|-------|----------|-------|-----|-------|-----|
| ingress-nginx | ingress-nginx | 4.12.0 | — | upstream | [[CONCEPT-ADDON_INGRESS_NGINX]] |
| eg (envoy gateway) | gateway-helm / gateway-addons-helm | v1.4.1→v1.6.0 | — | upstream | [[CONCEPT-ADDON_ENVOY_GATEWAY]] |
| exc (envoy-xds-controller) | envoy-xds-controller (+ dex 0.22.1) | 0.87.0 | — | upstream | [[CONCEPT-ADDON_ENVOY_XDS_CONTROLLER]] |
| exc-stage | envoy-xds-controller (+ dex 0.22.1) | 0.86.0 | — | upstream | [[CONCEPT-ADDON_ENVOY_XDS_CONTROLLER]] |
| exc-test | envoy-xds-controller (+ dex 0.22.1) | 0.84.0 | — | upstream | [[CONCEPT-ADDON_ENVOY_XDS_CONTROLLER]] |
| ingress2gateway | ingress2gateway | 0.0.6 | — | upstream | [[CONCEPT-ADDON_INGRESS2GATEWAY]] |

### Multi-tenancy, operators & platform

| Addon | Upstream | Chart | App | Class | Doc |
|-------|----------|-------|-----|-------|-----|
| capsule-system | capsule / capsule-proxy | 0.10.9→0.13.3 / 0.9.13→0.13.4 | — | upstream | [[CONCEPT-ADDON_CAPSULE]] |
| operator-lifecycle-manager | OLM (in-house packaging) | 0.32.0 | — | upstream | [[CONCEPT-ADDON_OLM]] |
| spegel | spegel (in-house packaging) | 0.0.1 | — | upstream | [[CONCEPT-ADDON_SPEGEL]] |
| etcd-defrag-controller | etcd-defrag-controller | 0.0.7 | — | upstream | [[CONCEPT-ADDON_ETCD_DEFRAG_CONTROLLER]] |
| common | in-house (helm library) | 0.0.2 | — | in-house | catalog |
| quoter | in-house | 0.1.0 | — | in-house | catalog |

### RBAC / access bundles (in-house)

| Addon | Class | Chart |
|-------|-------|-------|
| bigdata-access | in-house | 0.1.0 |
| bigdata-app-access | in-house | 0.1.0 |
| development-access | in-house | 0.1.0 |
| devops-access | in-house | 0.0.1 |
| support-access | in-house | 0.0.2 |

### Compute, devices & apps

| Addon | Upstream | Chart | App | Class | Doc |
|-------|----------|-------|-----|-------|-----|
| gpu-operator | NVIDIA gpu-operator | v25.10.1 | — | upstream | [[CONCEPT-ADDON_GPU_OPERATOR]] |
| kvm-device-plugin | kvm-device-plugin | 1.0.0 | — | upstream | [[CONCEPT-ADDON_KVM_DEVICE_PLUGIN]] |
| keda | keda | 2.17.2 | — | upstream | [[CONCEPT-ADDON_KEDA]] |
| awx | awx-operator (+ awx-operator-awx 0.0.1) | 2.19.1 | — | upstream | [[CONCEPT-ADDON_AWX]] |
| tbot | Teleport tbot | 18.7.3 | — | upstream | [[CONCEPT-ADDON_TBOT]] |
| kubernetes-mcp | kubernetes-mcp-server (+ open-webui 14.6.0) | 0.1.0 | — | upstream | [[CONCEPT-ADDON_KUBERNETES_MCP]] |
| feast-operator | feast-operator | — | — | upstream | [[CONCEPT-ADDON_FEAST_OPERATOR]] |
| gigapipe-read | gigapipe (qryn) | — | — | upstream | [[CONCEPT-ADDON_GIGAPIPE]] |
| gigapipe-write | gigapipe (qryn) | — | — | upstream | [[CONCEPT-ADDON_GIGAPIPE]] |

> ¹ App version corrected from the owner list against the chart's `Chart.yaml`/release (vault chart ships 1.21.2 not 1.21.4; volsync is 0.15.0 not 3.5.0; pyrra 1.1.0 ships v0.9.4 not v0.8.1) — see the deep doc.

## Compatibility

- **Overlaps with Kubespray-managed components:** `cert-manager`, `argocd`, `ingress-nginx`,
  `velero`, `snapshotter` — the owner runs newer independent charts than the Kubespray
  defaults. When comparing, use the addon version here, not the Kubespray `COMPONENT-*`
  version; the two are deployed by different mechanisms and must not be conflated.
- **In-house addons** carry no public source; their Kubernetes-compat is whatever their
  manifests target and can only be assessed against the actual chart.
- **Variants** (`exc` / `exc-stage` / `exc-test`; the two `rabbitmq` operators) are the same
  component at different versions/packagings — one deep doc covers the component, the catalog
  rows record each deployed version.

## References

- Owner inventory (2026-07-17). Kubernetes window: [[CONCEPT-KUBERNETES_VERSION_SUPPORT]].
- Scope/model decision: `standards/decisions.md` D-015.
