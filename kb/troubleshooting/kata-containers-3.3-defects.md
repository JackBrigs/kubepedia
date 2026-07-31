---
id: TROUBLE-KATA_CONTAINERS_3_3_DEFECTS
type: troubleshooting
title: "kata-containers 3.3: defects fixed in the 3.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.3.0 <3.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kata-containers 3.3 known issues
  - kata-containers 3.3 fixed in
  - is this kata-containers bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kata-containers
sources:
  - type: docs
    path: kata-containers/kata-containers release notes for the 3.3 line — bug-fix entries
    url: https://github.com/kata-containers/kata-containers/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kata-containers 3.3: defects fixed in the 3.3 line

## Summary

**64 defects** the project fixed across **1 releases** of the 3.3 line, from 3.3.0 to
3.3.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.3.0

- runtime-rs: fix a typo in device manager by @ZizhengBian in https://github.com/kata-containers/kata-containers/pull/8294
- utils: kata manager: Fix version checks by @jodh-intel in https://github.com/kata-containers/kata-containers/pull/8323
- network: Fix network attach for ipvlan and macvlan by @amshinde in https://github.com/kata-containers/kata-containers/pull/8334
- docs: Fix broken links by @cmaf in https://github.com/kata-containers/kata-containers/pull/8255
- kata-manager: Fix deployment of containerd on architectures other than amd64. by @brianwang12 in https://github.com/kata-containers/kata-containers/pull/7057
- Docs: Fix Dragonball link by @sazzy4o in https://github.com/kata-containers/kata-containers/pull/8285
- gha: stale: Fix typo and allow manually triggering it by @fidencio in https://github.com/kata-containers/kata-containers/pull/8368
- tests: fixes permission denied when running test by @beraldoleal in https://github.com/kata-containers/kata-containers/pull/8217
- network: Fix network hotplug for ipvlan and macvlan endpoints for qemu and add tests by @amshinde in https://github.com/kata-containers/kata-containers/pull/8367
- runtime: Fix TestCheckHostIsVMContainerCapable unstablity issue by @justxuewei in https://github.com/kata-containers/kata-containers/pull/8389
- gha: Fix regex used to get kubectl version from the k3s version by @fidencio in https://github.com/kata-containers/kata-containers/pull/8411
- runtime-rs: fix a typo in shm by @studychao in https://github.com/kata-containers/kata-containers/pull/8169
- runtime-rs: ch: Fix TDX by @jodh-intel in https://github.com/kata-containers/kata-containers/pull/8419
- metrics: Fix function that completely stops kata containers before running a test by @dborquez in https://github.com/kata-containers/kata-containers/pull/8338
- kernel: Fix vsock packets drop when the driver initializes by @alex-matei in https://github.com/kata-containers/kata-containers/pull/8431
- Fixes make check errors by @beraldoleal in https://github.com/kata-containers/kata-containers/pull/8345
- metrics: Fix result finding in tensorflow benchmark by @GabyCT in https://github.com/kata-containers/kata-containers/pull/8467
- runtime-rs on arm64: Fixes unable to Boot Container Image using Cloud… by @brianwang12 in https://github.com/kata-containers/kata-containers/pull/8422
- runtime: Fix configmap/secrets updates with FS sharing disabled by @Sumynwa in https://github.com/kata-containers/kata-containers/pull/8239
- gha: fix artefacts build on ppc64le by @Amulyam24 in https://github.com/kata-containers/kata-containers/pull/8526
- metrics: Fix iperf parallel bandwidth limit by @GabyCT in https://github.com/kata-containers/kata-containers/pull/8531
- libs:logging: Fix logger by @jodh-intel in https://github.com/kata-containers/kata-containers/pull/8547
- runtime-rs: fix panic when hypervisor mismatches with configuration by @liubogithub in https://github.com/kata-containers/kata-containers/pull/8566
- GHA: Fix kata-deploy-runtime-classes-check for kata-qemu-se by @BbolroC in https://github.com/kata-containers/kata-containers/pull/8624
- tests: k8s: Fix indentation in setup script by @GabyCT in https://github.com/kata-containers/kata-containers/pull/8676
- tests: k8s: Fix indentation in confidential common script by @GabyCT in https://github.com/kata-containers/kata-containers/pull/8699
- kata-deploy: snapshotter typo fixes by @stevenhorsman in https://github.com/kata-containers/kata-containers/pull/8721
- kata-monitor: fix Dockerfile to build image by @liubin in https://github.com/kata-containers/kata-containers/pull/8729
- kata-deploy: Fix shim check for snapshotter configuration by @fidencio in https://github.com/kata-containers/kata-containers/pull/8733
- dragonball: Fix compilation issue without all net features by @justxuewei in https://github.com/kata-containers/kata-containers/pull/8744
- agent: Fix an issue reporting OOM events by mistake by @justxuewei in https://github.com/kata-containers/kata-containers/pull/8773
- packaging: Fix indentation of build static stratovirt by @GabyCT in https://github.com/kata-containers/kata-containers/pull/8778
- gha: Fix the failure of gha metrics for StratoVirt by @WenyuanLau in https://github.com/kata-containers/kata-containers/pull/8657
- Fix backport check hub by @stevenhorsman in https://github.com/kata-containers/kata-containers/pull/8763
- genpolicy: cargo clippy fixes by @danmihai1 in https://github.com/kata-containers/kata-containers/pull/8822
- runtime-rs: fix unused driverInfo error by @yaoyinnan in https://github.com/kata-containers/kata-containers/pull/8928
- genpolicy: fix ConfigMap volume mount paths by @danmihai1 in https://github.com/kata-containers/kata-containers/pull/8924
- dragonball: fix noop-method-call warning by @kalil-pelissier in https://github.com/kata-containers/kata-containers/pull/8932
- kata-deploy: fix deprecations on kustomization files by @wainersm in https://github.com/kata-containers/kata-containers/pull/8269
- packaging: cache: Fix caching kernels which rely on extra modules by @fidencio in https://github.com/kata-containers/kata-containers/pull/8987
- packaging: Fix pushing artefacts to the registry by @fidencio in https://github.com/kata-containers/kata-containers/pull/9000
- kata-monitor: fix agentUrl from containerd shim by @deagon in https://github.com/kata-containers/kata-containers/pull/9012
- cri-containerd: fix loop in TestContainerMemoryUpdate() by @wainersm in https://github.com/kata-containers/kata-containers/pull/9025
- runtime-rs: fix assert error in `make check` by @ChengyuZhu6 in https://github.com/kata-containers/kata-containers/pull/9043
- runtime-rs: fix interoperability issues between runtime-rs and cri-o by @pmores in https://github.com/kata-containers/kata-containers/pull/8986
- runtime: fix creation of SEV confidential container on SNP enabled host. by @niteeshkd in https://github.com/kata-containers/kata-containers/pull/9037
- tools.kata-webhook: Fix lib path by @ldoktor in https://github.com/kata-containers/kata-containers/pull/9023
- runtime: fix checksum mismatch error in `make vendor` by @ChengyuZhu6 in https://github.com/kata-containers/kata-containers/pull/9112
- ci: k8s: Fix checks used to skip confidential tests by @fidencio in https://github.com/kata-containers/kata-containers/pull/9108
- gha: nydus: Fix indentation in gha run script by @GabyCT in https://github.com/kata-containers/kata-containers/pull/9088
- tests/runk: fix the "run ps command" flaky test by @wainersm in https://github.com/kata-containers/kata-containers/pull/9009
- release: Add the needed fixes for the release process by @fidencio in https://github.com/kata-containers/kata-containers/pull/9170
- releases: Second round of follow-up fixes by @fidencio in https://github.com/kata-containers/kata-containers/pull/9188
- rootfs: Fix PAUSE_IMAGE_TARBALL addition to the rootfs by @fidencio in https://github.com/kata-containers/kata-containers/pull/9180
- ci.ocp: Backport service-up detection fixes by @ldoktor in https://github.com/kata-containers/kata-containers/pull/9169
- katautils: fix panic on tracing. by @liubogithub in https://github.com/kata-containers/kata-containers/pull/9201
- tests/kata-deploy: fix checker for kata-deploy running by @wainersm in https://github.com/kata-containers/kata-containers/pull/9184
- CI: fix the issue of ci failure on crio by @lifupan in https://github.com/kata-containers/kata-containers/pull/9206
- gpu: fix build guest kernel with gpu by @Jimmy-Xu in https://github.com/kata-containers/kata-containers/pull/9155
- Dragonball: fix unit test problems when switching to new virt github machine by @studychao in https://github.com/kata-containers/kata-containers/pull/9208
- fixed - Change the deprecated module from 'io/util' to util. 'io/util… by @chungeun-choi in https://github.com/kata-containers/kata-containers/pull/9154
- tests: fix nounset error with $GITHUB_ENV by @wainersm in https://github.com/kata-containers/kata-containers/pull/9278
- kata-manager: Fix Docker install by @jodh-intel in https://github.com/kata-containers/kata-containers/pull/9293
- ocp.ci: Various fixes and improvements to the OCP pipeline by @ldoktor in https://github.com/kata-containers/kata-containers/pull/9229


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.3.0**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kata-containers/kata-containers`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kata-containers.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
