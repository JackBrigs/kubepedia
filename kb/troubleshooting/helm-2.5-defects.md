---
id: TROUBLE-HELM_2_5_DEFECTS
type: troubleshooting
title: "helm 2.5: defects fixed in the 2.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.5.0 <2.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 2.5 known issues
  - helm 2.5 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 2.5 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 2.5: defects fixed in the 2.5 line

## Summary

**44 defects** the project fixed across **2 releases** of the 2.5 line, from 2.5.0 to
2.5.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.5.0

- 2.5.1 will be the first patch release in the 2.5 tree. It will contain _only_ bug fixes
- Fix typo in command line. 8dfec4db6152f34d2be54dd83c69c1e994b5ebf2 (Julien Balestra)
- fix(helm): helm home print to stdout 985dbae2aceabc6415de1d49bec31d6b64c15f1a (Adam Reese)
- fix(tests): Fixes broken unit test 5cfb4e8cf8c00d3fc8c2634dceae2bd8c0c565f9 (Taylor Thomas)
- fix(helm): Ensures tiller pod lands on a linux node 8a0e051c1dd059f3fede4147154b40f857b7d304 (Taylor Thomas)
- fix(helm): modify `helm repo update` help info c8b8c1e6d635c55fbf2c548c465cf6eafcf18692 (willise)
- fix(tiller): track hooks in multi-def manifests 83c69a8e10dcf6e85ad7f81afdb7eb7de58fc654 (Michelle Noorali)
- fix(tiller): make GetReleaseContent return any release c9139113378b0ba7301b2a4fcc5716bc21d40c3f (Matt Butcher)
- docs(helm): fix typo af8730032a14da71870213f7ea0bfb0399ee7fd2 (willise)
- fix(helm): remove unnecessary values merge in processImportValues 40052d3e8fbdc7ad7eda830e4325c0606e5ac916 (Justin Scott)
- fix(docs): A couple spelling mistakes a2d559bd0b5b7ac4dca965f92065fa2945f36438 (Cory Smith)
- fix(docs): Updated non-working example in 'Using Helm' documentation 2b0a61285818e06e9e5da0461b9fea12c538aa19 (Nikhil Manchanda)
- fix(tiller): Adds missing import back d9c0a8b434d88ae366bf23c0a7677b9ee4b87dfe (Taylor Thomas)
- fix(plugins): exists --> exist e7a51d542415dd347a89e21b48c573da8eb1a3dc (Seth Goings)
- fix(helm): fix race conditions in flag parsing d797acbd7bb97270698ce718b2d45ecdda1dc18e (Adam Reese)
- fix(2452): sort templates before parse 8937c775a9799387d5e1b76222d197919a992ae7 (Matt Butcher)
- fix(helm): prepend repo URL to packages missing scheme 4c6a7cf7590fc354f625eb8af2fde927f05aa8e4 (Matt Butcher)
- fix(docs): Remove "no nested globals allowed" 7c7646cce2bc7b8b4f34be88d5586473ef498d6a (Justin Scott)
- fix(plugins): add error when updating modified plugins 1e8ebae249ccf9cd1b9358c6b0c7780caf95f7b6 (Adam Reese)
- fix(helm): fix setting home via `helm --home=HOME` 9832e7df96bfe19f3e0469c7b70532fd9a4e60c7 (Adam Reese)
- fixed fromYaml | toJson bb4be3333162926c8652e868ba8c1dfa371e4e05 (lead4good)
- fix(helm): fix itermittent release testing failures 19a33b3f955b30018bd052c316a13aed8c8c66a0 (Michelle Noorali)
- fix(helm): add --devel flag to allow dev releases again 28ec92355bd676c5775ea82504cde5a3465000a0 (Matt Butcher)
- fix(Dockerfile): add ca-certificates 70f6aa4c239b689100c4bc8f154f28f133197939 (Matt Butcher)
- fix(windows): Updating docker/distribution 3f1c6a1e870b8c860267c2a22895140615282a29 (Matt Farina)
- fix(lint): add KubeVersion and TillerVersion to linter d863d9a886c187cee2a5b606d146e8c0ea26a0e5 (Matt Butcher)
- minor typo fix 5408b60ad64b5580de1f2be8f52986f99ca17c35 (Kent Rancourt)
- fix(*): return non-zero exit code on test failure 488ca6fdd86d1158523db3db1bf2daccd65d0226 (Michelle Noorali)
- fix(tiller): Fixes bug with `--wait` and updated deployments d3106125262cdaebefccbbfe4fca8bd6e630ecc4 (Taylor Thomas)
- Fix minor typo in test doc ce12341bfa5997c6cf3ccf1748a6963332ec1d7e (Kent Rancourt)
- Fixes messages for plugin remove option 1c5aab8e7853e33de550cc75edb7a1e7aa88a8cc (Sushil Kumar)
- Fixed issues reported by test-style 61c3a44dc3ec96f1c4e99510a229dc5376bd3280 (Sushil Kumar)
- fix(Dockerfile): only copy tiller binary in Dockerfile fabb7208ab52516162388934bc13f02c586bd2cb (Adam Reese)
- chore(helm): fix go style issues in completion.go 9fe76d3430b6288cb667ae0d769a6d96117bbbba (Michelle Noorali)
- fix typo: ' instead of ` 267a09193be23a55ada0e76604b0afc03ed4b26c (Hoat Le)
- fix(helm): reverted upgrade of imdario/mergo 0d62c3ab56aff538efb367e8efb5741144225b86 (Rod Cloutier)
- Fix for vbom.ml bootstrap b18625092e2a225ebd75d30ca98683a6418b5cd1 (Maxim Ivanov)

### 2.5.1

- The deadlock problem with Tiller has been found and fixed. A huge thanks to the dozen community members who submitted use cases and data to help us find the problem
- fix(tiller): remove locking system from storage and rely on backend controls b6624b78ea7da2aa1ef171963d08e67664f99cd5 (Justin Scott)
- fix(helm): fix flag parsing once and for all 97857297a6da1d1d4a4df3d2e0ce3a0fa3583484 (Adam Reese)
- fix(helm): fix `helm get` subcommands e960523b3e870a85804acb77750406fe77cb04b7 (Matt Butcher)
- fix(helm): support HELM_HOME during plugin loading d68562faa245403a16d0a3c684dd329042ff7281 (Adam Reese)
- fix(helm): load home from flags during runtime 7692de7ff0b22233b32c9574690dd6ab7a9acb09 (Adam Reese)
- Fix a bug causing 'helm depndency update' to delete required charts 30a5c6c19f31acbf61591fa7beddbaf514b51a04 (Alon Lavi)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.5.1**, the newest release recorded here for this line.

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
