---
id: CONCEPT-TALOS_OMNI
type: concept
title: "Omni — Sidero Labs' Talos management plane (SaaS/self-hosted, KubeSpan, infra providers)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-18"
confidence: verified
aliases:
  - talos omni
  - sidero omni management plane
  - omni kubespan
  - omni infrastructure provider bare-metal
  - omni self-hosted saas
  - omni sidebase
tags:
  - talos
  - omni
  - management
sources:
  - type: docs
    path: public/omni/overview/what-is-omni.mdx
    url: https://github.com/siderolabs/docs/blob/main/public/omni/overview/what-is-omni.mdx
    note: "Omni overview, SaaS/self-hosted, BUSL license (siderolabs/docs @59a5195)"
  - type: docs
    path: public/omni/infrastructure-and-extensions/infrastructure-providers.mdx
    url: https://github.com/siderolabs/docs/blob/main/public/omni/infrastructure-and-extensions/infrastructure-providers.mdx
    note: "infra providers: bare-metal (IPMI/Redfish), KubeVirt, libvirt, vSphere, Proxmox; static vs dynamic"
relations:
  - type: see_also
    target: CONCEPT-TALOS_K8S_MATRIX
  - type: see_also
    target: CONCEPT-TALOS_CLUSTER_API
  - type: see_also
    target: CONCEPT-TALOS_NETWORKING
---

# Omni — Sidero Labs' Talos management plane (SaaS/self-hosted, KubeSpan, infra providers)

## Summary

**Omni** (`siderolabs/omni`) is Sidero Labs' Kubernetes **management platform** with native Talos
integration — 100% API-driven from OS → Kubernetes → Omni. It automates cluster create/manage/upgrade,
provides a built-in **highly-available Kubernetes API endpoint**, a management UI, and ties Talos+K8s
API access to an enterprise identity provider (access-list-validated kubeconfig). It's the
"batteries-included" alternative to hand-driving `talosctl` or wiring Cluster API
([[CONCEPT-TALOS_CLUSTER_API]]).

## Context

- **Workflow:** boot machines (bare metal / VM / cloud / edge) from an **Omni Talos image** → allocate
  to a cluster in a few clicks; Omni manages the full machine lifecycle and scaling.
- **Licensing / deployment:** available as **SaaS** (operated by Sidero Labs) and **self-hosted /
  on-prem** (air-gapped, data-sovereignty). Released under **BUSL** — production needs a commercial
  license; non-production (home lab) does not. Self-hosted covers Keycloak/SAML identity, HTTPS
  exposure, workload proxy, DB backup.
- **Machine registration** via **SideroLink**: ISO, PXE/iPXE, or cloud instances (AWS EC2, GCP, Azure,
  Hetzner). Version pairing: Omni min version tracks the Talos minor (Talos 1.13 → Omni ≥1.8.0; 1.12 →
  ≥1.4.0 — [[CONCEPT-TALOS_K8S_MATRIX]]).
- **Infrastructure providers** connect compute for automated lifecycle — **static** (owned machines
  reused across clusters) and **dynamic** (VMs created/deleted on demand). First-party: **bare-metal**,
  KubeVirt, libvirt, vSphere, Proxmox (third-party: Oxide, TrueNAS). The **bare-metal** provider
  provisions physical servers via **BMC power management (IPMI / Redfish)** + the **Image Factory** —
  replacing manual media/boot and superseding the older Sidero-Metal CAPI path for new deployments. One
  Omni instance runs multiple providers across locations; a single cluster can mix manual/static/dynamic
  and even span global sites.

**KubeSpan.** Omni and Talos use **KubeSpan** — WireGuard-based full-mesh node encryption — so all
traffic to Omni is WireGuard-encrypted and inter-node traffic can be too, letting one cluster **span
untrusted networks** (edge + cloud + on-prem — [[CONCEPT-TALOS_NETWORKING]]). Peers are discovered via
an external **discovery service** and a **Kubernetes-annotation** system (each node advertises its
public key + addresses); it can optionally route Pod subnets.

**Scope note.** Omni is a Talos-ecosystem management plane, **not** Kubespray-managed — it's the
opposite operational model (immutable-OS + SaaS-style control plane vs Ansible-driven). Documented here
because Talos is a recorded alternative-OS domain in the KB.

## References

- `siderolabs/docs` `public/omni/overview/what-is-omni.mdx`,
  `.../infrastructure-and-extensions/infrastructure-providers.mdx`,
  `public/talos/v1.13/learn-more/kubespan.mdx` (@59a5195). Matrix [[CONCEPT-TALOS_K8S_MATRIX]]; CAPI
  [[CONCEPT-TALOS_CLUSTER_API]]; networking [[CONCEPT-TALOS_NETWORKING]].
