---
id: TROUBLE-HELM_3_2_DEFECTS
type: troubleshooting
title: "helm 3.2: defects fixed in the 3.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.2.0 <3.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 3.2 known issues
  - helm 3.2 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 3.2 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 3.2: defects fixed in the 3.2 line

## Summary

**55 defects** the project fixed across **3 releases** of the 3.2 line, from 3.2.0 to
3.2.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.2.0

- We fixed a number of issues in the update/delete/rollback logic
- Fixed [critical vulnerability in lookup function](https://github.com/helm/helm/security/advisories/GHSA-q8q8-93cv-v6h8). **Note:** The security issue only impacts Helm 3.1.x, not 3.0.x. (The security update will be adjusted when its review period is over.)
- fix linting error with lookup function (#7969) e11b7ce3b12db2941e90399e874513fbd24bcb71 (Matt Butcher)
- fix: removed inaccurate comment (#7937) 853ba2de16a04d0715c44937162e0b58752a99d6 (Matt Butcher)
- fix: Fixed a regression that was introduced with changed nil handling (#7938) 7b89e66e0c350c7d61443ed6de647298fc9e9a2b (Matt Butcher)
- Fix nested null value overrides (#7743) a34f3115395474fbf3b8a167ef3473eb8b0952e9 (uzxmx)
- fix: rebuild chart after dependency update on install (#7897) fa5eb64f32c99a2771acf326c4b0e01481d23066 (Matt Butcher)
- fix(tests): fix broken unit tests in storage (#7928) e1d046bc43ad1ec53c4c0d38aa7723c82e2ff9d2 (Adam Reese)
- fix(storage): preserve last deployed revision (#7806) b9445616b522fe701620b18becdae3a783c054cb (Eric Bailey)
- fixed capitalization in a few help messages. (#7898) 469837b92cefa0c633397dea1e49606ba0105d56 (Matt Butcher)
- fix: fixed bug in Dependency.List() (#7852) bd13b80b12c246acf8959f510c1b21f72b2ccebd (Matt Butcher)
- Avoid downloading same chart multiple times f3350defec881dc36217f4774703f252d3c895af (Andrey Voronkov)
- fix(helm): Data race in kube/client Delete func. (#7820) c12a9aee02ec07b78dce07274e4816d9863d765e (lnattrass)
- fix: update unit test for go 1.14 error string change (#7835) 3706aa7ca666fda6d8301c55118fa1c092f124a2 (Matt Butcher)
- Fix a bug in Delete() in storage/driver/cfgmaps.go (#7367) 26830942d275b3a70edfdc32474230f3499a18e4 (tiendc)
- Fix a bug in storage/driver/secrets.go Delete() (#7348) 06bc18c624c3ce264c926632ce8bc9fe471ce6e6 (tiendc)
- fix(cli): Make upgrade check if cluster reachable 22b7562c62c2fc0cc89f568755f0c2e09106c0ab (Marc Khouzam)
- fix(install): correct append tls config. bf5c0ae7f46dce9f44633e0d7e87b933c375bf5a (James McElwain)
- Fix stray modules c8d8007c7aba5b66d185f4c82cc19a16c8246dd7 (Martin Hickey)
- fix: add new static linter and fix issues it found (#7655) 16024dc19a23e83f00a19742033031717a56be0e (Matt Butcher)
- fix(helm): polish goimport c45869c4ad8f46140f6aea0d673aa7892f3eefad (Dong Gang)
- fix(helm): respect resource policy on ungrade Don't delete a resource on upgrade if it is annotated with helm.io/resource-policy=keep. This can cause data loss for users if the annotation is ignored(e.g. for a PVC) 9744e9f619d3c1d8ddbe3af59e7d70d81c05dc5a (Dong Gang)
- fix(ADOPTERS): alphabetize org list (#7645) 8edf86a7181c16fe4089c52f7b7fe58df5b08ce7 (Matthew Fisher)
- Fixes verification output on pull command a3f92f65e26323a3f91343c29ee0c4d1b6282d21 (Matt Farina)
- fix(helm): stdin values for helm upgrade --install 1ab52fa79c100332bc8014095cf7aed6937cae8a (Matt Morrissette)
- Fix dep build to be compatiable with Helm 2 when requirements use repo alias 13e2dcfde53c735dc313d0145bca063ba3a9d121 (Song Shukun)
- fix(cmd/helm): upgrade go-shellwords c235470e59fd4f17149339757940537f95605cef (Adam Reese)
- fix(helm): add --skipCRDs flag to 'helm upgrade' When 'helm upgrade --install' is run, this will allow to skip installing CRDs Closes #7452 e92a258a9d7cc684589cb22c317eb7ddaeaf753e (akash-gautam)
- Fix output of list action when it is failed 1ff7202a9841b0a6a8d409342305ead6eb1503da (Song Shukun)
- pkg/helmpath: fix unit test for Windows eda60a59b61abc7fb20063d9dc0608fe877b3206 (Song Shukun)
- fix golint failure in pkg/action e9f40ed7a51b40966e4d91957357e6f6efc60251 (Song Shukun)
- Fix render error not being propogated 7b9dc71c25f0dea9013d2174b45f16fa202468c3 (Martin Hickey)
- fix(scripts): scrape for the latest v2/v3 release from the releases page 0087d838073abcc93fb9ea694256e0b93238ae23 (Matthew Fisher)
- fix(kube): generate k8s native scheme only once e41184a585800dd672856d422b4f8a2bd3d430e0 (Hidde Beydals)
- fix(kube): use non global Scheme to convert b55224ebb9541b690daca59f6d85867c6e275d75 (Hidde Beydals)
- fix(helm): improved logs af0007c9087c3e714aafc2bdac80bb55df6dbffd (Federico Bevione)
- Fix shasums to be usable by shasum and sha256sum applications 8e9c62b1bc3c557a1d2cc88a8e4fdc83ef498cb5 (Matt Farina)
- fix(comp): Fix broken completion for --output flag e3965e11852f908646d2c02f55fd463c4b755538 (Marc Khouzam)
- fix recursion count in templates 8528548441b826533d896ebf01b6a0c911eff6d8 (Daniel Cheng)
- Fix 'helm template' to also print invalid yaml 2a73967ca214d38ed22f5f3ecfda3d1dcc2b4773 (Reinhard Naegele)
- fixed missing bullet 9daca76f16b7b17c6ecb36b30ff7832a4b83b70f (Matt Butcher)
- fix(helm): Reworded logs for clarity 077503f17502ea2ad59d73a08897f238dc72ebb0 (Federico Bevione)
- fix(helm): Don't wait for service to be ready when external IP are set 438eaec971774b2e30e97aa640abd5cfe8b3ef40 (Federico Bevione)
- fixed dependencies processing in case of helm install or upgrade for disabled/enabled sub charts d03db32c250bc7906c9d4b0e0858b0412c55dfcf (Florian Hopfensperger)
- fix(helm): sort hooks by kind for equal weight 9a2ff7802ff84fcc260c0eff940fa0af3ea91137 (Daniel Strobusch)
- fix(install): use ca file for install (#7140) e9bf446fa8faf5fa31352aa708829a951404200e (James McElwain)

### 3.2.1

- 3.2.2 is the next patch release and will contain bug fixes
- Fix markdown table in helm command doc 8635a19660e8d79da5e70a64de64c2b18f1fde73 (Lüchinger Dominic)
- fix(pkg/plugin): copy plugins directly to the data directory (#7962) 48d09a26d2a7e5d9693e0d4f145287961b612020 (Adam Reese)
- fix(helm): allow a previously failed release to be upgraded (#7653) 56ef9ab386c771d827dc502f5f8e12929fc5ee1f (Matthew Morrissette)
- fix: write index.yaml file atomically (#7954) cb7189f6ce0ba3ce73ba564e81c379a446261216 (Raphaël)

### 3.2.2

- Fix issue with unhandled error on Stat 1da74ed1bb60b200340db95e672f2c20f7dc5596 (Matt Farina)
- Fix unit test 564044c7d0250b3ace563ca7001097f2f8cee979 (Martin Hickey)
- Fix repo cache setting 4cdc98264bb5a0817075c7287f9af609f232a514 (Martin Hickey)
- fix: upgrade using --force shoud not run patch logic (#8000) 4b91e1639745fdead179d1ddef394a657c501ed1 (小明同学)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.2.2**, the newest release recorded here for this line.

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
