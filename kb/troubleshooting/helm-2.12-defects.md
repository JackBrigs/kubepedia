---
id: TROUBLE-HELM_2_12_DEFECTS
type: troubleshooting
title: "helm 2.12: defects fixed in the 2.12 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.12.0 <2.13.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 2.12 known issues
  - helm 2.12 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 2.12 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 2.12: defects fixed in the 2.12 line

## Summary

**39 defects** the project fixed across **4 releases** of the 2.12 line, from 2.12.0 to
2.12.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.12.0

- fix(helm): Fix linebreaks when printing custom resources 7247537c3dfc761f58ad03424bc598d411923b3e (Morten Torkildsen)
- fix(helm): Print details for pod resource b536c8de104f0e68c7117ca7d4bb14872f791109 (Morten Torkildsen)
- fix(helm): Allow custom resources in hooks (#4986) 55a338579a5b3150f3b9466b4fe471a6f0118f70 (Morten Torkildsen)
- Fix for existing CRDs are deleted when crd-install hook is introduced (#4709) e2a0e7fa545585a29c1e9602e6320479788eb9a6 (Michael Merrill)
- avoid kubernetes import for slice contains logic (#4963) c095b9232dfd6631f0ce02ba1cb5ff35909153d8 (Tariq Ibrahim)
- fix(storage): when pruning release versions, never delete the last deployed revision 5bf38a2d7d572c4317e18c4ecbe7023403b979bb (Matt Tucker)
- Fix doc charts indent (#4940) 8fcefd7d959ce10448507944b2418f29da532f5d (Jintao Zhang)
- fix(windows): fix unit tests on Windows (#4897) 97465abda0b6a9e9934092c6245070fd91088023 (Matthew Fisher)
- fix(helm): --set for out of order list values (#4682) e23793120b8ce3deeeede070813cd74689ed729c (Dan Winter)
- fix(docs): run `make docs` (#4924) 3a8a797eab0e1d02456c7944bf41631546ee2e47 (Matthew Fisher)
- fix(helm): Non-zero exit code on failed chart repository update (#4348) f6b1189aa201231b67133df4c75db0709465c84f (Lev Aminov)
- fix(tiller): rollback deleted release (#3722) (#4820) 9ae00bebadad9e29ca79ae9ae93486576497059b (Brent)
- fix(helm): Merge nested values correctly on upgrade (#4806) 82d01cb3124906e97caceb967a09f2941d6a392d (Morten Torkildsen)
- fix:#4873, check release name (#4883) d41ca72e425c529896632e3cf4b98e2972e3dbd2 (liaoj)
- fix(helm): fix incorrect yaml output format of get hooks command (#4684) 1801fa0074a0207f4d5724667858b53d52c486f8 (adshmh)
- fix snap install command (#4877) 833ee712b254c618fe7afc2af20fc9e8094524a1 (Mike Garuccio)
- fix(engine): Fix template rendering thread safety issue (#4828) 6635bff38faab593ee2eb50a888e8d8d4c6c15d7 (Sean Eagan)
- Small typo fix (#4887) 4a49abb81ef78a1e4c6c69fc2e29bd8b98d6ce40 (Daniel M Barlow)
- docs(release_checklist): fix changelog generation command (#4694) 8442851a5c566a01d9b4c69b368d64daa04f6a7f (Matthew Fisher)
- test(tiller): cover crash fixed by #4630 (#4853) 0522b34e056f6dda012a763b7ed2acd4ef552e1f (Matt Rasmus)
- Fix cmd/helm use tillerTunnel values (#4777) 440e79ff958becbcbd6135fd4a7fddd553de06af (masahiro)
- fix(helm): Use line breaks consistently in status output 586dc1db61d5e18921acc36933752f00904337f2 (Morten Torkildsen)
- fix(helm): Update status output to include resource details (#4791) dd9ed71429999bd267db53c9533a6224ff48e719 (Morten Torkildsen)
- Fix reference to wordpress (#4803) ea5d2bb7bdbca360eff4b730498f73815ec94cba (Marc Khouzam)
- Grammar fix (#4801) d8f38e5cee80d6e6e4ebff2f4ea48534d49647ee (mgresser)
- fix(tiller): correctly sort PodDisruptionBudget objects before pods that might use them (#4769) 147c8217c7843b53e98528f6df12890d64c696be (Matt Tucker)
- Fix Slack channel references (#4752) e7d93f231d1a53b5ed63e32aa6d7687e5715b6d2 (Martin Hickey)
- fix(helm): fix paths in the ingress template and values file written by helm create 1a54463bdb1e4cf9b6f93fa2f7452c77e68bb54e (Arash Deshmeh)
- fix(helm): fix regression with TLS flags/environment variables not being parsed (#4657) 8be42bae885a04b4acc242cf420911145b32ee1c (Matthew Fisher)
- Fix credentials not set for ResolveChartVersion default HTTP client (#4662) fbda50a452b6db58faf2016b17c206ee27ddc999 (Caleb Delnay)
- fix(helm): fix selector typo in service template for 'helm create' (#4663) 4dd9047586f0cfa8ed77a21d2f1062c382f27d3e (Qiang Li)
- fix merge conflicts/linter errors (#4653) a297a0a7fe14779e7cfdcfa15a13237a34b42af7 (Matthew Fisher)
- Fix type in Values File (#4629) 5211bfa110ab4b99ad53800098f4928711521b96 (Pratyush Verma)
- Fix race condition in `helm list` (#4620) 5b236324468ad8958c351dd3c734880c0fa5d561 (Matthew Fisher)
- Fix for checking helm version slice bounds out of range (#4609) 2b33bf6ba719e602c026d07ae483327d84da6b7c (Robert James Hernandez)

### 2.12.1

- Revert "Fix for existing CRDs are deleted when crd-install hook is introduced (#4709)" (#5067) 02a47c7249b1fc6d8fd3b94e6b4babf9d818144e (Matthew Fisher)

### 2.12.2

- fix: perform extra validation on paths in tar archives (#5165) c194e4a4016902e2ab3f06b29dc8628f27d971a4 (Matt Butcher)

### 2.12.3

- fix: ignore pax header "file"s in chart validation 940400b5a635e9e7e0028786c3d58e3ce2ca4069 (Geoff Baskwill)
- fix: use RFC 1123 subdomains for name verification (#5132) 4268e69a2a7fa69952c02dbc8ad7b77f0bbdc16a (Matthew Fisher)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.12.3**, the newest release recorded here for this line.

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
