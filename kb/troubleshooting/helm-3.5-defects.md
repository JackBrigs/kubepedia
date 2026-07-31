---
id: TROUBLE-HELM_3_5_DEFECTS
type: troubleshooting
title: "helm 3.5: defects fixed in the 3.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.5.0 <3.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.5 known issues
  - helm 3.5 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.5 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.5: defects fixed in the 3.5 line

## Summary

**26 defects** the project fixed across **4 releases** of the 3.5 line, from 3.5.0 to
3.5.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.5.0

- 3.5.1 will contain only bug fixes and be released on February 10, 2021
- Fix dep build with OCI based charts 32c22239423b3b4ba6706d450bd044baffdcf9e6 (Matt Farina)
- Fixed bug - The flags --cert-file/--key-file where ignored when --insecure-skip-tls-verify flag is set (#9070) a202fb0c0b73a1093609251476e0d8a1b76b3b8f (Dinu Mathai)
- fix(pkg/chartutil): Remove warning for nils bed1a42a398b30a63a279d68cc7319ceb4618ec3 (Marc Khouzam)
- Fix test f30badd5709ebc1afbc809716c8aae3c9ebcc7fc (rimas)
- Fixes #9083 ce1a46899f5b1e7ba9d485d7800d0d23313d7d7b (rimas)
- [COMMENT]fix comment 7c4932c485edb49874919c2cd6bb171506497c3d (Scaat Feng)
- fix: ingress path issue 50144aad0332692059534acd574fcf141307ef2d (Salim Salaues)
- fix(helm): flag descriptions start with lowercase e16d26717b1b7588ab24fa0a87e48dc1940c80d2 (Marc Khouzam)
- fix style conformance bd03e1b5c70cffd13e740f40ef1c0e8c3a49e092 (zhangye15)
- fix test-style error c96dc48f21adbc79e410fafc63f6f6daa221c424 (zhangye15)
- Fix that the invalid version number of the helm package command will escape 2c19838295b9b1efd7fb548d047eaff53095ab52 (wawa0210)
- Fixes Error: could not find protocol handler for 882db2543c90bb6e50ffe98083963b65a47cc662 (Matt Farina)
- Fix the lint error message for valid names 5785dd6d497f3eb025a92416db19508cc9a372f0 (Martin Hickey)
- fix(test): display error message 38c964ae8134a65c1ffda13e37ac8e5573bd3de3 (Matthew Fisher)
- fix(helm): allow skipping manifests in tests directories 3d66daeb55d947c4d30d542dfb7459afc21a3c10 (Torsten Walter)

### 3.5.1

- 3.5.2 will contain only bug fixes and be released on February 10, 2021

### 3.5.2

- During an audit, Helm core maintainers discovered sanitization issues [described in a security advisory](https://github.com/helm/helm/security/advisories/GHSA-c38g-469g-cmgx). These have been fixed
- The Go team renamed a crypto library (golang.org/x/crypto/ssh/terminal to golang.org/x/term). This was NOT a security fix. But it was a breaking change to the Helm build
- 3.5.3 will contain only bug fixes and be released on March 10, 2021
- fix(*): Validate metadata semver and printable characters 2bf5c280d56e0043bf1870f84d63e82d5c5d4230 (Adam Reese)

### 3.5.3

- 3.5.4 will contain only bug fixes and be released on April 14, 2021
- Fix the example for --time-format flag 041ce5a2c17a58be0fcd5f5e16fb3e7e95fea622 (mert)
- fix(pkg/storage): If storage.Create fails to clean up recent release versions, return an error d552cb3b1d491f4a1aa170d9903a897c1e9ffc7f (Daniel Lipovetsky)
- fix release sha256 dc3971631e1032b6d79c09513a9c3741b3ea6dba (houfangdong)
- Fix-9253: Change the deprecated charts repo URL in release notes ec560e5f2b3405413a025d031a16c7f7f24ff547 (Jack Whitter-Jones)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.5.3**, the newest release recorded here for this line.

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
