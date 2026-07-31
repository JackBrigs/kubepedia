---
id: TROUBLE-HELM_3_19_DEFECTS
type: troubleshooting
title: "helm 3.19: defects fixed in the 3.19 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.19.0 <3.20.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.19 known issues
  - helm 3.19 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.19 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.19: defects fixed in the 3.19 line

## Summary

**39 defects** the project fixed across **5 releases** of the 3.19 line, from 3.19.0 to
3.19.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.19.0

- Fixed a `helm pull` regression from 3.18 - error pulling OCI charts with --password #31230
- Fixed a `helm lint` regression from Helm 3.18 - rejected JSON Schema $ref URLs that worked in 3.17.x #31166
- Fixed k8s version parsing not matching original #31091
- Fixed charts failing when using a redirect registry #31087
- Fixed missing debug logging for OCI transport
- Fixed broken legacy docker support for login #30941
- Fixed processing all hook deletions on failure #30673
- fix: use username and password if provided 9a54bf1df6245232aff6235ebc5da7616f06afa7 (Evans Mungai)
- fix(helm-lint): fmt b27802031110bcfcaf0b685f7f3efda8a309ce8c (Isaiah Lewis)
- fix(helm-lint): Add TLSClientConfig d33ac5e44b4eb884d67141b00753817b091054ca (Isaiah Lewis)
- fix(helm-lint): Add HTTP/HTTPS URL support for json schema references 854370978eb4664ed75e1918df733ecf1503e904 (Isaiah Lewis)
- fix: go mod tidy for v3 da4c583145cf4de6a291e81b499ba53785739c2b (Terry Howe)
- fix Chart.yaml handling f13afaacd6f8f9dca4ad914d87fabbe129692eda (Matt Farina)
- json schema fix 6d9509aadcfb44aaaa6fc6528443815343a551b4 (Robert Sirchia)
- fix: k8s version parsing to match original 807225ed62b2901fcbaf56923111d9d7f9204a59 (Borys Hulii)
- fix: user username password for login 2c55a4e8ce483fe1a03d7afa46a89e26852bc3c5 (Terry Howe)
- fix: add debug logging to oci transport b52bb41484bca2eab616aed83aa922cbb5ef1e3b (Terry Howe)
- fix: legacy docker support broken for login 733f94c86a98f2fc4a12eba510e26615d4b8aa59 (Terry Howe)
- fix: plugin installer test with no Internet fc360417024f4734e5b7356385512a08a31c743e (Terry Howe)
- Prevent fetching newReference again as we have in calling method c33215d765e291bc9321984d4f60a0182c738938 (Benoit Tigeot)
- Prevent failure when resolving version tags in oras memory store f552b672305a420b54a725185f98e34e51fbd7ba (Benoit Tigeot)
- fix(client): skipnode utilization for PreCopy a18a52e8982b399101f7f20e2473de8514e85226 (Brandt Keller)
- fix(client): layers now returns manifest - remove duplicate from descriptors b07ab77da3a2d20508b8e775981e233a81d4c753 (Brandt Keller)
- fix(client): return nil on non-allowed media types c225c124ac76eedc3ca6e013df40da8d2c50650d (Brandt Keller)
- Fix 3.18.0 regression: registry login with scheme c0f3ace52d974b7465f33079bbf54ed961f875f1 (Scott Rigby)
- fix: move warning to top of block eb5b6d50474842db17330b11e0db70077e1c4510 (Feng Cao)
- fix: govulncheck workflow 6b15f26bd45c2856b36bdf3e8c32b44595e4580f (Matthieu MOREL)
- fix: replace fmt warning with slog 6b5c94475db950a981523344029f0a7c620a2e32 (Feng Cao)
- fix: add warning when ignore repo flag 247bf7c2e0c591554b6cfd4c2f62cb2700b034ee (Feng Cao)

### 3.19.1

- Avoid "panic: interface conversion: interface {} is nil" 2f619be224790e7b2447b10faa3b965701177e40 (Benoit Tigeot)
- Fix `helm pull` untar dir check with repo urls 8112d47cbba491a70d84005e5a88bd0e72ef5040 (Luna Stadler)
- Fix deprecation warning 5dff7ce71b53828d36121f81ac59cf389b811ebc (Benoit Tigeot)

### 3.19.2

- [backport] fix: get-helm-3 script use helm3-latest-version 8766e718a0119851f10ddbe4577593a45fadf544 (George Jenkins)

### 3.19.3

- [backport] fix: get-helm-3 script use helm3-latest-version 8766e718a0119851f10ddbe4577593a45fadf544 (George Jenkins)

### 3.19.5

- Fixed bug where removing subchart value via override resulted in warning #31118
- Fixed bug where helm uninstall with --keep-history did not suspend previous deployed releases https://github.com/helm/helm/issues/12556
- fix(rollback): `errors.Is` instead of string comp 4a19a5b6fb912c5c28a779e73f2e0880d9e239a4 (Hidde Beydals)
- fix(uninstall): supersede deployed releases 7a00235a0622b6eae1d06fbb87c2a33b718cbd7e (Hidde Beydals)
- fix null merge 578564ee26171e5ca2ee0edd0c06cb58a72fba87 (Ben Foster)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.19.5**, the newest release recorded here for this line.

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
