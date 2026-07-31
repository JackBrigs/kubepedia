---
id: TROUBLE-HELM_3_13_DEFECTS
type: troubleshooting
title: "helm 3.13: defects fixed in the 3.13 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.13.0 <3.14.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.13 known issues
  - helm 3.13 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.13 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.13: defects fixed in the 3.13 line

## Summary

**34 defects** the project fixed across **3 releases** of the 3.13 line, from 3.13.0 to
3.13.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.13.0

- Values handling had numerous issues fixed and now consistently has a priority of (1) User specified values (e.g CLI), (2) parent chart values, (3) imported values, and (4) subchart values. Additionally, null can now consistently be used to remove values. Note, there is a regression around this in 3.13.0 that's fixed in 3.13.1
- 3.13.1 is the next bug fix release and will be on October 11, 2023
- Fix leaking goroutines in Install 169561a1b381ae1a6a3974d84c303f19f324ffa0 (Michał Słapek)
- fix conflict 4944acb3410d9baf377a495f41df628115a3ce35 (Maxim Trofimov)
- fix conflict 199784f7116cd1949aacb6af0b3e1cd473227d75 (Maxim Trofimov)
- fix b786cb40f09212a2b1c2c337f233a9b9c28122d9 (Maxim Trofimov)
- fix(helm): fix GetPodLogs, the hooks should be sorted before get the logs of each hook 4e5e68d55c3d4bb385a582e633cfeaa5635981eb (Bingtan Lu)
- fix: helm rollback err tips db9460cc8710c37525e08e7d314c354108d69383 (ithrael)
- fix: precedence typo bf543d94e95557cd4cc796ec5313e4548b4d126f (guoguangwu)
- Avoid nil dereference if passing a nil resolver 3607cd7110a8e62c69ea02900139c1c54534aaa9 (Antonio Gamez Diaz)
- Fix #3352, add support for --ignore-not-found just like kubectl delete 48dbda2fa8d1e8981c271a56fe51bdf8b131fac2 (suzaku)
- Fix helm may identify achieve of the application/x-gzip as application/vnd.ms-fontobject 5c7a63138b70f2493be7ea5245791ba40091b9b2 (MR ZHAO)
- fix(main): fix basic auth for helm pull or push 4a27baaffc7ae112c2f45e3cd72dd249d9563a5a (cuisongliu)
- Fix multiple bugs in values handling 0a5148faffb7110bab58a466a52be0686a69947c (Matt Farina)
- chore: fix a typo in `manager.go` 15e6066a45cbd2b98023cf07bb1cfb45e18d2d95 (Yarden Shoham)
- fix comment grammar error. 8e1c3d0d397922313e7c3201bd3d01ec1e8747eb (wujunwei)
- pkg/engine: fix nil-dereference 2a9594c0feadf0ab637c4e4c6cf50a931ba1778c (AdamKorcz)
- pkg/chartutil: fix nil-dereference 2f13355e40ca2790bebb19b7182500d312a536de (AdamKorcz)
- pkg/action: fix nil-dereference 6fc815da5a2951cecf6805d61b25d53bfe0ab980 (AdamKorcz)
- fix: add podLabels b441f5341dd796b1ecdfcec0706a38d51cd8efb7 (genofire)
- fix typo: mountPath fc1a5a1123793691a0e6f7e339ab49448fc3be77 (Eugene Zuev)
- Avoid confusing error when passing in '--version X.Y.Z' 0d9eb1341b70955c266936295e6415c12c671280 (Justin Wood)
- Fix flaky TestSQLCreate test by making sqlmock ignore order of sql requests 28ab648d3c6d9e9ec2b611c5c2c65fba53c8cb97 (Dmitry Chepurovskiy)
- Fix broken tests for SQL storage driver c7eedbd9c583933a483917416d5c86bd6704631d (Dmitry Chepurovskiy)
- Fix broken tests for configmap and secret storage drivers 95bb77c261f0965dc4e6ecf938cc754a3006939b (Dmitry Chepurovskiy)
- fix: plugin does not load when helm base dir contains space 2b49de086072b24d7b93f9ddbb66b4a933963384 (Suresh Kumar)
- Fixes #10566 c598a226e9c69113fc7265739b92818d6a2adf37 (alexandr.danilin)
- fix(search): print repo search result in original case 488add2cfe4a4d34ce875d6f89244c6575a834db (Höhl, Lukas)

### 3.13.1

- FIX Default ServiceAccount yaml bae7b3293c4c8ce2561874cf93ebae56d490b2f6 (Lars Zimmermann)
- fix(registry): unswallow error 06e4fb10a66ea984d555905702775aab639f8790 (Hidde Beydals)
- fix(registry): address anonymous pull issue 0ac78941abfed981a47f263fa59931e9123f73a1 (Hidde Beydals)
- Fix missing run statement on release action 09012691de50da37254d1ef98d97333c4a3e35c5 (Ian Zink)

### 3.13.2

- Revert "fix(main): fix basic auth for helm pull or push" e785e6c50c622ed5019fd4020a13509c87a3022d (Matt Farina)
- Revert "fix(registry): address anonymous pull issue" 268dcedba6a231b623c8252a3dafa0052d161c6e (Matt Farina)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.13.2**, the newest release recorded here for this line.

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
