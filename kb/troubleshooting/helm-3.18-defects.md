---
id: TROUBLE-HELM_3_18_DEFECTS
type: troubleshooting
title: "helm 3.18: defects fixed in the 3.18 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.18.0 <3.19.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.18 known issues
  - helm 3.18 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.18 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.18: defects fixed in the 3.18 line

## Summary

**30 defects** the project fixed across **6 releases** of the 3.18 line, from 3.18.0 to
3.18.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.18.0

- 3.18.1 on June 11th, 2025 will contain only bug fixes
- fix: govulncheck workflow bf1436baf3c235cb1b689a016b7162d0cddd3947 (Matthieu MOREL)
- fix:add proxy support when mTLS configured 48377fe4515cc6a5bf5ac92ea6086090e7b82798 (Rongrong Liu)
- Fix --take-ownership 4ee3a19e9a98e3b58eb4579f019666e834408ca3 (Patrick Seidensal)
- Unarchiving fix 3ce10e4f81e064a3807098c3d466c33f2ece8a18 (Matt Farina)
- Fix typo 422c58e4a2d7a00e2275916be1bfda0b28efba82 (Benoit Tigeot)
- Fix cherry-pick helm.sh/helm/v4 -> helm.sh/helm/v3 bcb83e465f4487b481b8843f4d5dfe4f26472c55 (Scott Rigby)
- clarify fix error message 97b0e11871252ad99054d911d92666f84fdac79a (Scott Rigby)
- fix err check 2f79afb0a3c506fd41ea89f13efcfa4379f88b5f (Scott Rigby)
- Fix lint 4cb639ed4edab7729859328d443b102d05a4b32d (Chris Berry)
- Fix linter warning b39411a66829d711168de543fa823cbd5e749ca4 (Evans Mungai)
- Additional review fixes from PR 483ebf915da5ab2c2bbdb46644bca2fe22ae51f9 (Evans Mungai)
- fix: check group for resource info match 2ebce786ba295a3ca7a281c3ffd78086cf561f89 (Jiasheng Zhu)
- This commit fixes the issue where the yaml.Unmarshaller converts all int values into float64, this passes in option to decoder, which enables conversion of int into . 0a6834fdf060b4fbc4e1ea4bcb85908891539d48 (Althaf M)

### 3.18.1

- This release fixes regressions around template generation and OCI registry interaction in 3.18.0
- fix(client): skipnode utilization for PreCopy f6f8700a539c18101509434f3b59e6a21402a1b2 (Brandt Keller)
- fix(client): layers now returns manifest - remove duplicate from descriptors 4da701593f8c8a137fc36a95f9e9ecfe1d01528f (Brandt Keller)
- fix(client): return nil on non-allowed media types 1a8507fd5ad910f466accfd1c784ed0c333c343a (Brandt Keller)
- Prevent fetching newReference again as we have in calling method 015531ca4f386a6fee6c9f48eae63124d19c76a7 (Benoit Tigeot)
- Prevent failure when resolving version tags in oras memory store 9db1a120f9f7404044cc4619ea7379b430004e36 (Benoit Tigeot)
- Fix 3.18.0 regression: registry login with scheme ea04cea48bf2b312e506ae03c412c6fd95929c5c (Scott Rigby)
- Revert "fix (helm) : toToml` renders int as float [ backport to v3 ]" bec66098fdb4ac37298f46701a2d5b28e5776b72 (Matt Farina)

### 3.18.2

- fix: legacy docker support broken for login 04cad4610054e5d546aa5c5d9c1b1d5cf68ec1f8 (Terry Howe)

### 3.18.3

- fix: user username password for login 5b9e2f6b4c4e2c8e21d85dc01fbb9d8a454a1fa9 (Terry Howe)
- fix: add debug logging to oci transport 191f05c068a25a80cd206c1256c6b11a63c4068b (Terry Howe)

### 3.18.5

- fix Chart.yaml handling 7799b483f52ceb665264a4056da3d2569d60f910 (Matt Farina)
- json schema fix cb8595bc650e2ec7459427d2b0430599431a3dbe (Robert Sirchia)

### 3.18.6

- fix(helm-lint): fmt b76a950f6835474e0906b96c9ec68a2eff3a6430 (Isaiah Lewis)
- fix(helm-lint): Add TLSClientConfig b79a4212e803ad50c66f06799b8bbdb51f918603 (Isaiah Lewis)
- fix(helm-lint): Add HTTP/HTTPS URL support for json schema references b9180e674fccb57e6ea6934ed7deb4448a3c9ddb (Isaiah Lewis)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.18.6**, the newest release recorded here for this line.

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
