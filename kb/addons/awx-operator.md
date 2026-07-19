---
id: CONCEPT-ADDON_AWX
type: concept
title: "AWX Operator — addon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "24.6.1"
verified_at: "2026-07-17"
confidence: verified
aliases:
  - awx
  - awx-operator
  - ansible awx
tags:
  - addons
  - ci
  - ansible
  - awx
sources:
  - type: docs
    path: awx-operator 2.19.1 release
    url: https://github.com/ansible/awx-operator/releases/tag/2.19.1
    note: "operator 2.19.1 pairs with AWX 24.6.1"
  - type: code
    path: roles/installer/defaults/main.yml
    url: https://raw.githubusercontent.com/ansible/awx-operator/2.19.1/roles/installer/defaults/main.yml
    note: "PostgreSQL 15, Redis 7 defaults"
relations:
  - type: see_also
    target: TROUBLE-AWX_OPERATOR
  - type: see_also
    target: CONCEPT-ADDON_CATALOG
---

# AWX Operator — addon

## Summary

The AWX Operator (**2.19.1**) deploys AWX (the upstream of Ansible Automation Platform).
Operator 2.19.1 pairs with **AWX v24.6.1** and defaults to **PostgreSQL 15** + Redis 7.

## Context

- Class: upstream addon; catalog row (+ local `awx-operator-awx 0.0.1`) in
  [[CONCEPT-ADDON_CATALOG]].

## Implementation

- Operator **2.19.1** → AWX **24.6.1** (both 2024-07-02). At the git tag `_image_version`
  defaults to `latest`; the concrete 24.6.1 is injected into the released operator image at
  build time.
- Chart `kubeVersion`: **none** (the `.helm/starter` chart is an operator-sdk scaffold).

## Configuration

- **`manage_replicas` became a boolean** (spec-format change since 2.19.0) — update the AWX CR.
- **PostgreSQL default is 15** (`postgresql-15-c9s`); a PG13→15 move involves a managed data
  migration whose exact skip-version procedure is **not documented upstream** (**unverified**)
  — take a DB backup before upgrading.

## Compatibility

- **Kubernetes range:** no centralized tested range is published (**unverified**); no
  kubeVersion is imposed. Works across 1.29–1.35 in practice.
- **CVEs (AWX 24.6.1):** CVE-2026-52902 / GHSA-g29c-rgq6-gxgj (path traversal in the awxkit
  CLI YAML `!include`, Moderate) — affected/patched ranges are listed "Unknown," so 24.6.1
  inclusion is **not precisely pinned**. No version-pinned GHSA for the AWX web core at
  exactly 24.6.1. AWX images accumulate downstream-dependency CVEs with no interim patch
  releases — rebuild/scan periodically.

## Upstream issues & upgrade notes (mined 2026-07-19)

**Upstream (AWX Operator 2.19.x):** 2.19.0 added **HPA for web/task**, fixed custom-CA handling across task/web/migration, and enhanced readiness checks; 2.19.1 is a maintenance release paired with AWX 24.6.1 (no DB migration, no breaking). No newer operator line in this window — verify before assuming a higher pin exists.

## Older-version CVEs & security history (mined 2026-07-19)

The AWX **Operator** has no notable code-specific CVE record; the real older-version exposure is the **AWX application** it deploys and its **bundled PostgreSQL/Redis** versions (Django/AWX web CVEs, old PG/Redis images). For older clusters, upgrade AWX itself (not just the operator) and the managed DB/cache images to stay patched.

## Guides & how-to (official)

- **Docs/upgrade:** https://ansible.readthedocs.io/projects/awx-operator/en/latest/ (install + upgrade)
- **How to upgrade:** bump the **operator** version (Helm/kustomize), which reconciles the `AWX` CR to the paired AWX app; back up the **Postgres** DB first; watch the migration job. External-DB (`postgres_configuration_secret`) avoids the managed-DB PVC dependency.
## References

- awx-operator 2.19.1 release notes, installer defaults (above).
- Catalog: [[CONCEPT-ADDON_CATALOG]].
