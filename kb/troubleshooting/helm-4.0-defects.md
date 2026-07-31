---
id: TROUBLE-HELM_4_0_DEFECTS
type: troubleshooting
title: "helm 4.0: defects fixed in the 4.0 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=4.0.0 <4.1.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 4.0 known issues
  - helm 4.0 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 4.0 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 4.0: defects fixed in the 4.0 line

## Summary

**26 defects** the project fixed across **3 releases** of the 4.0 line, from 4.0.1 to
4.0.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 4.0.1

- fix 4b6472ffb042a2c76c5323b9bfb1e8000cb3fd1e (George Jenkins)
- fix: Use server-side apply for object create during update 9dfe3b35ec7fb16b941c5904c8b8dee716cc225a (George Jenkins)
- Fix kube client logging 861adc2f4a14e96bc5c627a6c557d80461777735 (Matt Farina)
- Fix syntax errors in the document a156195c35525cfaf404058b0f9aa61610e9e791 (Fish-pro)
- fix: correct LDFLAGS path for default Kubernetes version 2c0dcda29b56f1e65098a4a2acb3c384734721af (Benoit Tigeot)

### 4.0.2

- fix: prevent reporting fallback on version when none specified 94659f25033af6eb43fc186c24e6c07b1091800b (Benoit Tigeot)
- fix: prevent segmentation violation on empty yaml in multidoc 2dd1f662cce36de8910e925921dc9f86ec72205b (Benoit Tigeot)
- fix: Fix Helm v4 release distribtion/get-helm-3 script 0bef6bdbe6e20832dea995037c975a8631072212 (George Jenkins)

### 4.0.5

- Fixed bug where helm uninstall with --keep-history did not suspend previous deployed releases #12556
- Fixed rollback error when a manifest is removed in a failed upgrade #13437
- Fixed check to ensure CLI plugin does not load with the same name as an existing Helm command
- Fixed helm test --logs failure with hook-delete-policy "hook-failed" or "hook-succeed" #9098
- Fixed a bug where empty dependency lists were incorrectly treated as present
- Fixed a bug where the watch library did not only watch namespaces associated with the objects
- Fixed regression in downloader plugins environment variables #31612
- Fixed bug where --server-side flag is not respected with helm upgrade --install #31627
- fix(upgrade): pass --server-side flag to install when using upgrade --install 1b6053d48b51673c5581973f5ae7e104f627fcf5 (Evans Mungai)
- fix(cli): handle nil config in EnvSettings.Namespace() 1e3ee1d2ba5a421165fe053a41aa4071cf69ed62 (Zadkiel AHARONIAN)
- fix(getter): pass settings environment variables 31bd995ce201e295ff2f87e11fdf13bf55fdffd2 (Zadkiel AHARONIAN)
- fix: use namespace-scoped watching to avoid cluster-wide LIST permissions 66cab24bb95f68448a83304c6d3297ec45c8fdb7 (Mohsen Mottaghi)
- Fix linting issue 417aae9c01a79c01f3de8c2a08079fddada6078e (Benoit Tigeot)
- Fix TestCliPluginExitCode e845b68fe3ea0c91f429b384e3b78f3f853ae208 (tison)
- Fix rollback for missing resources 0fd2c418b0146c1ea6182c7f7c7676a345554156 (Feruzjon Muyassarov)
- fix: assign KUBECONFIG environment variable value to env.Kubeconfig b456e274652c84316d5bfcf06d6a8b648e3cc23b (LinPr)
- fix(rollback): `errors.Is` instead of string comp e2021f8818d2cf20c118d91fdba8fba5c472c3bb (Hidde Beydals)
- fix(uninstall): supersede deployed releases af7c15303ace3c506c5c790c41186a09df1c8a54 (Hidde Beydals)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **4.0.5**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `helm/helm`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/helm.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
