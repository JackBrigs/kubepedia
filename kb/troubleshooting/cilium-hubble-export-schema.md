---
id: TROUBLE-CILIUM_HUBBLE_EXPORT_SCHEMA
type: troubleshooting
title: Cilium/Hubble flow export settings ignored after Cilium 1.18 schema change
status: active
kubespray_version: "v2.29.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - hubble export static schema
tags:
  - cilium
  - hubble
sources:
  - type: github_pr
    url: https://github.com/kubernetes-sigs/kubespray/pull/12718
    note: "Backport to release-2.29 aligning Hubble export values to the Cilium 1.18 hubble.export.static schema"
relations: []
---

# Cilium/Hubble flow export settings ignored after Cilium 1.18 schema change

## Summary
With Hubble flow export enabled, the static exporter settings (file rotation/size) were not applied because Cilium 1.18 moved them under the helm-values key `hubble.export.static`, while Kubespray still generated the old schema. Fixed in v2.29.1.

## Problem
When Hubble flow export was enabled, the static exporter settings (file rotation / size) did not take effect, because Cilium 1.18 relocated them into helm-values under the `hubble.export.static` key while Kubespray generated values using the old schema.

## Context
- Affected versions: v2.29.0 (Cilium 1.18 with Hubble export).
- Fixed versions: v2.29.1.
- In v2.29.1 the default Cilium version is 1.18.4, so the new schema applies.

## Diagnostics
- With Hubble export enabled, verify the rendered helm-values contain the `hubble.export.static` block.
- Confirm the exporter file rotation / max-size settings are not honored at runtime despite being configured.
- Relate to the upstream Cilium schema change cilium/cilium#36974.

## Known Issues
Root cause: Kubespray built the Hubble export helm-values using the pre-Cilium-1.18 schema, tied to the upstream schema change (cilium/cilium#36974).

Fix: PR #12665 (master) aligned the values to the new `hubble.export.static` schema. Backport into release-2.29: PR #12718, commit `a04592de1`. Confirmed in tag v2.29.1 `roles/network_plugin/cilium/templates/values.yaml.j2`, which contains the new schema:

```yaml
  export:
    static:
      fileMaxBackups: {{ cilium_hubble_export_file_max_backups }}
      fileMaxSizeMb: {{ cilium_hubble_export_file_max_size_mb }}
```

Commit `a04592de1` ("Adjust hubble export values for cilium 1.18 schema change (#12718)") falls within the `v2.29.0..v2.29.1` range.

## References
- https://github.com/kubernetes-sigs/kubespray/pull/12718
- Migrated from Kubepedia 0.1.0 cache: cilium-hubble-export-schema-v2.29.1.md
