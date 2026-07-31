---
id: TROUBLE-HELM_2_8_DEFECTS
type: troubleshooting
title: "helm 2.8: defects fixed in the 2.8 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.8.0 <2.9.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - helm 2.8 known issues
  - helm 2.8 fixed in
  - is this helm bug already fixed
tags:
  - troubleshooting
  - upgrade
  - helm
sources:
  - type: docs
    path: helm/helm release notes for the 2.8 line — bug-fix entries
    url: https://github.com/helm/helm/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# helm 2.8: defects fixed in the 2.8 line

## Summary

**58 defects** the project fixed across **3 releases** of the 2.8 line, from 2.8.0 to
2.8.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.8.0

- Added a --wait flag for helm init which pings the Tiller server and ensures that it is ready to receive requests Fixes #2114 b29d25ef0be611cffb28c5ac8b494e2c735178b3 (Alex Johnson)
- fix(capabilities): Adding GitVersion to default set d5a865b5f4fe5392defb7aba40711aa8135933a8 (Matt Farina)
- Fix filename 9ad292b3ef701c9a7d97b5533991e476c2f9776c (Dennis Benzinger | SAP Hybris)
- fix(helm): filter helm list to print latest release (#3335) e9203b826bb4f1efb6dfaa3a566c9cc1bbac4651 (Adam Reese)
- Added notes on how to fix pulling errors fb1432264182baa52e89c1b8eb593f1074e66e06 (Andrey Chernih)
- fix a typo 270969117c620b417cdc785dfa9d0a38c4fec2bf (Pure White)
- fix typo 724b3898a4a79e247e5c8720bd214265053bdc1e (Luis Cordova)
- docs(chart_template_guide): Fix link e4274c448ce70fb683dfbd52d53bf7804efed6fd (Mitchel Humpherys)
- Fix broken bullets by Note in docs.helm.sh 9735642fe8b092da503e88c9ebca8c63ddcf7c92 (Gabriel Miretti)
- Fix command formatting 219e1075ce0441d063d9604a563e9e9a2484288f (Gabriel Miretti)
- Typo fix cfb7dfa82c5d7ebb54645ffd0727416b0ccf10a9 (Andrey Klimentyev)
- Fix package url bd8178d50b867abf0785939bb8c1c5eaf9036b12 (Nauris Sadovskis)
- fix(helm): Init not creating local-index symlink on Windows 9129188fadd62e2baf01dbc0f0c2c21638aab4bf (Pietro Menna)
- Fix helm ls in Quickstart 6029f4dc9325f436a2112fc4afa717329a2dd430 (Luk Burchard)
- Fix example and reference version matching syntax a3af75f9b607ee6f96b1c61f09e5c13f29a06538 (Tim H)
- fix(helm): Apply PR comments for tpl template name fix Modified existing unit test to verify the changed behavior. Removed debug print. 8bc7dede1864b94ced115a566c115e522b4af11b (Lukas Eichler)
- Fixed warning for missing formating parameter inside error message. 1cebc760a036f41caf8ce2207237775b0d13055b (Lukas Eichler)
- fix(helm): Set template context inside tpl function to outer function. docs(helm): Added documentation about tpl function 2c338db1bd9b8624dd908eb6ac137c913d9ec39d (Lukas Eichler)
- fix TLS default path 618094ccd2a37acb0adbdcd43885eb6aae0a712c (Matthew Fisher)
- fix(sprig): Update to v2.14.1 that fixes an issue 57f95213f356125da730aa98f09300bbebd14619 (Matt Farina)
- fix signatures 93bce130fbee835a2c136189b661c9a8ec0812cb (Federico Gimenez)
- fix(tiller): Forces close of idle gRPC connections 44e5cecdcaee14c15055d20d6b9a72e80cd4794d (Taylor Thomas)
- fix links to service_accounts.md 35616bd0df6d46b1f988bfdbb1f39c80d75fda3e (Matthew Fisher)
- fixed bad link. c20ec8fedaef10e0642d20bfe554baeb932aa0ee (Ralph Squillace)
- fix(helm): add --app-version flag to 'helm package' 9e869700c0bbb76ebec94b7b12871d6fe27b59ab (Arash Deshmeh)
- Fix a typo in install.go, update helm_install.md d81780032a167816ec2c900857c7d074b8ae267c (Igor Vuk)
- correct typo 335ea3c6ac1786aab4f3a0028d0c5bc7941d33d8 (Mark Gibaud)
- fix(helm): Fixed semantic version constraints on 'search' command (#3116) b74c21a7b291033cfe417a153eb4b455eba60696 (Morgan Parry)
- Fix helmignore for .* (#3114) d762a42168308d93a46be1d7bc37bc518eee496f (Johnny Bergström)
- fix: rename variable due to linter warning 2106766ab81b6fb881809aa25a9e35999a6170f7 (Christoph Hösler)
- fix: updated docs b45293feb006013094213d6380cb881956a4672b (Christoph Hösler)
- fix(helm): resolve relative chart paths 09313ad26c38d905b7ff87921fa5754ade0152d5 (Christoph Hösler)
- fix(helm): Tunnel closing already closed channel (#3157) fe3eeaf39d44a95aa9e7cff29647cd12ab60da5a (Matt Cholick)
- Fix/missing ssl params (#3152) e8e6ac5d7783808cc0bd1adad053bec339849647 (Matt Butcher)
- Fix incorrect line 7e0e27726df8b7b7023f78f1ed593a58bc15377a (Denis Mikhaylov)
- fix(helm): update documentation to reflect $HOME env var change 8ee89fe5dcdf35bc937508367dce8133ed08f43e (Pietro Menna)
- fix(helm): home env not set on Windows ece9486182db705923e3f04618c5f6a37e71076d (Pietro Menna)
- Fix err checking 6f6d46de06a1b580d350f3cdf9bfb78cf4de76a3 (Alexander Lukyanchenko)
- fix(tiller): upgrade last deployed release 82ef751414d9de6b64ffaf89d964ab67cb5d4766 (Adam Reese)
- fix(docs): fix code comment for ReuseValues() b8734a173ec079e9ec181b03bee44bebae8e9c2e (Matt Tucker)
- docs(templates): fix and expand config checksum example 25e851ecd03301030aa76b106520a52ec2a8f44e (Joan Rieu)
- docs(templates): fix misleading/broken examples e464479cb2bb9b7228f595e513622bef2b173946 (Joan Rieu)
- Fix typo for --service-account 3c3936fcaaf2c86d783ed87d6d1aca25d6dd5d15 (Simon Schmidt)
- Fix for relative chart path support in index.yaml 8775f632f246ff3c7746c3cc3f71d51a06101e93 (Christian Jauvin)
- fix(circleci): Fixing the glide/vendor cache so it is used by glide 4c7617a76e310fa53473b31b18b371b344da4fef (Matt Farina)
- Update install tests to use ReleaseMock and associates from the helm package. Also fix release names to match expected reponse values 2bc97cfc839a542735a798bc7c24f1921387509f (Brad Bowman)
- Review fixes applied 9a42d71898612c8bee21e6d1b417789b8167cece (Marcin Kłopotek)
- Fixes shell installation script #2977 42bc36d24093c6b1f4a6fb4c4df7a79be7e82151 (Marcin Kłopotek)

### 2.8.1

- fix(grpc): Fixes issue where message sending limited to 4mb e2f688fa0d3cead645dc6737fa236021fa740f82 (Matt Farina)
- fix(api-machinery): Fixes patching for unstructured objects 90957b905c6f8446c590a05ca43171e4e3073918 (Matt Farina)
- fix helm init --upgrade logic 2b2b994092fc7b8407dd8403c673844721ccd929 (Matthew Fisher)
- Fix 'getSelectorFromObject' 7086a16e29cfb106c272437f756b6cef628e7582 (Reinhard Nägele)
- Fix pod recreation d6dc3ded8465f177866e67e8acc1694f189064f0 (Reinhard Nägele)
- fix RELEASE_BRANCH_NAME fdbbfecb55b6cd23ea59cc668ec55cc900cd3ea4 (Matthew Fisher)

### 2.8.2

- fix protoc e647416e1e5720dd71a05c7ffd0cbaf4eeaa7127 (Matthew Fisher)
- fix helm init --wait a5394ea0fb4bcde72e34c51261767fa9abe10186 (Matthew Fisher)
- fix(helm): Don't crash in search if upper case chars are encountered. cc5a8abefd38ff98591ecbe42edcd4f9d4d7fe2d (Morgan Parry)
- fix(tiller): Supersede multiple deployments (#3539) 5847d922111ccb90beba3e6ea072bdc357355fdd (Johnny Bergström)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.8.2**, the newest release recorded here for this line.

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
