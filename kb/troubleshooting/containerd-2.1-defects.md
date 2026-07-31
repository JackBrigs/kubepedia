---
id: TROUBLE-CONTAINERD_2_1_DEFECTS
type: troubleshooting
title: "containerd 2.1: defects fixed in the 2.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.1.0 <2.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 2.1 known issues
  - containerd 2.1 fixed in
  - is this containerd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes for the 2.1 line — bug-fix entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 2.1: defects fixed in the 2.1 line

## Summary

**46 defects** the project fixed across **9 releases** of the 2.1 line, from 2.1.0 to
2.1.8. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.1.0

- Fix recursive RLock() mutex acquisition ([containerd/go-cni#126](https://github.com/containerd/go-cni/pull/126))
- Fix race between serve and immediate shutdown on the server ([containerd/ttrpc#175](https://github.com/containerd/ttrpc/pull/175))

### 2.1.1

- Fix erofs media type handling ([#11855](https://github.com/containerd/containerd/pull/11855)) [`e1817a401`](https://github.com/containerd/containerd/commit/e1817a401f94698cdf8fdc01d8d0e2b4f1f463e7) docs/snapshotters/erofs.md: a tip for improved performance [`2168cb92c`](https://github.com/containerd/containerd/commit/2168cb92c9cf89aaad06be9ae49fce49ed4972d8) erofs-differ: fix EROFS native image support

### 2.1.2

- Fix check of wrapped errors in erofs snapshotter
- Fix transfer differ selection ([#11936](https://github.com/containerd/containerd/pull/11936)) [`4bcea74de`](https://github.com/containerd/containerd/commit/4bcea74decd64dcbf616f56b47cf8f5b4a2a586f) Update differ selection in transfer service to prefer default [`0c3cd8a99`](https://github.com/containerd/containerd/commit/0c3cd8a99529849ee2e3f9661ebfa937f3f9be66) Add debug log when transfer returns not implemented [`820e56765`](https://github.com/containerd/containerd/commit/820e56765083b50d0e8f4baf06f4804700f33a92) Add more error details when unpack fails to extract
- Fix check of wrapped errors in erofs snapshotter ([#11935](https://github.com/containerd/containerd/pull/11935)) [`480126f50`](https://github.com/containerd/containerd/commit/480126f5079e501228553038a584ce8542807d89) erofs-snapshotter: fix to work with wrapped errors

### 2.1.3

- Fix multipart fetch issue when the server does not return content length
- Fix multipart fetch issue when the server does not return content length ([#12003](https://github.com/containerd/containerd/pull/12003)) [`7636bd5eb`](https://github.com/containerd/containerd/commit/7636bd5eb2525babefd2983d38f6e1133843eb94) fix when multipart fetching and the server does not return content length
- Fix import for local transfer service ([#12000](https://github.com/containerd/containerd/pull/12000)) [`fb752bc8e`](https://github.com/containerd/containerd/commit/fb752bc8ed456ff40ceb516dcb72830678cae1ab) fix import for local transfer service
- Fix registry errors with transfer service ([#11979](https://github.com/containerd/containerd/pull/11979)) [`f6d926314`](https://github.com/containerd/containerd/commit/f6d92631401562eba488a986a22002025d2860c9) Register remote errors for clients to access registry errors [`7c1813345`](https://github.com/containerd/containerd/commit/7c18133453a495df7a334fde31423c56d42265c2) Decode grpc errors in the transfer client proxy
- Fix fetch always adding range to requests ([#12001](https://github.com/containerd/containerd/pull/12001)) [`babacebad`](https://github.com/containerd/containerd/commit/babacebadc0738e6b016e2f366cdf4bdf893a1a5) Fix fetch always adding range to requests

### 2.1.4

- Fix containerd panic when sandbox extension is missing
- Fix lazy gRPC connection mode waiting for connect on client creation
- Fix resolve deadlock issue in docker fetcher open
- Fix erofs filesystem UUID for tar-converted layers
- Fix close container io not closed when runtime create failed
- Fix resolve deadlock issue in docker fetcher open ([#12127](https://github.com/containerd/containerd/pull/12127)) [`add2dcf86`](https://github.com/containerd/containerd/commit/add2dcf8688019158fc1c015dddffe54c6610e24) Ensure fetcher always closes body and properly calls release [`34a1cb1dd`](https://github.com/containerd/containerd/commit/34a1cb1dd1962520f6821b7273debf06a740ed6d) fix(dockerFetcher): resolve deadlock issue in dockerFetcher open
- Backport windows test fixes ([#12119](https://github.com/containerd/containerd/pull/12119)) [`6cc2a8d77`](https://github.com/containerd/containerd/commit/6cc2a8d779e29045f279cef041bec3d0569e75db) Fix intermittent test failures on Windows CIs [`6adc69312`](https://github.com/containerd/containerd/commit/6adc69312f8f929f5e285d8fd3806c269853e850) Remove WS2025 from CIs due to regression
- Fix lazy gRPC connection mode waiting for connect on client creation ([#12079](https://github.com/containerd/containerd/pull/12079)) [`2df7175d7`](https://github.com/containerd/containerd/commit/2df7175d71d1e71c3b27f9c0879db4050b183fce) client/New: Don't unlazy the gRPC connection implicitly
- Fix containerd panic when sandbox extension is missing ([#12076](https://github.com/containerd/containerd/pull/12076)) [`02298e1a0`](https://github.com/containerd/containerd/commit/02298e1a03b92d36dba899c8aba82fc3c50422cd) cri:fix containerd panic when can't find sandbox extension
- Fix erofs filesystem UUID for tar-converted layers ([#12058](https://github.com/containerd/containerd/pull/12058)) [`583133e71`](https://github.com/containerd/containerd/commit/583133e7103145fcc338b695b2e6456c69fc52ee) erofs-differ: fix filesystem UUID for tar-converted layers
- Fix close container io not closed when runtime create failed ([#12009](https://github.com/containerd/containerd/pull/12009)) [`b74268f86`](https://github.com/containerd/containerd/commit/b74268f8674647234f6a08c005f84b38ba1adf63) bugfix:close container io when runtime create failed

### 2.1.5

- **Fix userns with container image VOLUME mounts that need copy**
- Prepare release notes for v2.1.5 ([#12483](https://github.com/containerd/containerd/pull/12483)) [`fc5bdfeac`](https://github.com/containerd/containerd/commit/fc5bdfeacefc7ff2a4f6bafaa2ed6453dbb8c472) Prepare release notes for v2.1.5 [`c578c26bf`](https://github.com/containerd/containerd/commit/c578c26bf9e9d3368e87edb837b706053c3ef30e) Update mailmap [`46a4a03fb`](https://github.com/containerd/containerd/commit/46a4a03fb4131739e948f983af8c984eb0c36d61) Merge commit from fork [`232786c90`](https://github.com/containerd/containerd/commit/232786c906a11dae0c1ef5059653d4164345401f) Fix directory permissions [`239ab877d`](https://github.com/containerd/containerd/commit/239ab877db8edf31ffb2ae63d83919d1c242e8d2) Merge commit from fork [`0766796e8`](https://github.com/containerd/containerd/commit/0766796e8e95ffdbf6d2b4fb08bda536c03d444c) fix goroutine leak of container Attach
- Fix lost container logs from quickly closing io ([#12377](https://github.com/containerd/containerd/pull/12377)) [`7d9f09ba0`](https://github.com/containerd/containerd/commit/7d9f09ba048da562cdc0a971be439641c87aedcf) bugfix:fix container logs lost because io close too quickly
- Prevent goroutine hangs during ProgressTracker shutdown ([#12336](https://github.com/containerd/containerd/pull/12336)) [`9b57a4d35`](https://github.com/containerd/containerd/commit/9b57a4d35a9728ccb99a03b1a27cca8b431e99ab) Prevent goroutine hangs during ProgressTracker shutdown
- Fix overlayfs issues related to user namespace ([#12222](https://github.com/containerd/containerd/pull/12222)) [`f40bfc46b`](https://github.com/containerd/containerd/commit/f40bfc46b0b680f07299c05623d7383cd4204bcb) core/mount: Retry unmounting idmapped directories [`1f51d2dea`](https://github.com/containerd/containerd/commit/1f51d2deada6bf493214c78069d93e94dc226091) core/mount: Test cleanup of DoPrepareIDMappedOverlay() [`8fbf8c503`](https://github.com/containerd/containerd/commit/8fbf8c503ef9ebf837f82a40b9ea54f98d9dccbe) core/mount: Properly cleanup on doPrepareIDMappedOverlay errors [`b9d678e15`](https://github.com/containerd/containerd/commit/b9d678e15e27ab45a7cfa9876a46f88afeaca90c) core/mount: Don't call nil function on errors [`583fe2d24`](https://github.com/containerd/containerd/commit/583fe2d244568d585c9b5688d42a24e2cf407709) core/mount: Only idmap once per overlayfs, not per layer
- fix: create bootstrap.json with 0644 permission ([#12183](https://github.com/containerd/containerd/pull/12183)) [`3c174cf64`](https://github.com/containerd/containerd/commit/3c174cf64e5b4e6cdae6f06e091e458120390fe7) fix: create bootstrap.json with 0644 permission
- sys: fix pidfd leak in UnshareAfterEnterUserns ([#12179](https://github.com/containerd/containerd/pull/12179)) [`5ef6ea747`](https://github.com/containerd/containerd/commit/5ef6ea7470dd18e3c93f21c2ea5004f6e72b0642) sys: fix pidfd leak in UnshareAfterEnterUserns

### 2.1.6

- Redact all query parameters in CRI error logs ([#12547](https://github.com/containerd/containerd/pull/12547)) [`b72d0dfe0`](https://github.com/containerd/containerd/commit/b72d0dfe0458e1b5f1e67ba70476fc4887ee5f08) fix: redact all query parameters in CRI error logs

### 2.1.7

- Fix image volumes when using user namespaces in CRI
- Fix issue where CNI DEL was never executed after a restart
- Fix possible panic from WithMediaTypeKeyPrefix
- Hardening: fix possible TOCTOU race bug in tar extraction
- Fix unintended dropping of mount flags for read-only bind-mounts in user namespaces
- Fix possible panic from WithMediaTypeKeyPrefix ([#13135](https://github.com/containerd/containerd/pull/13135)) [`fe316cc1f`](https://github.com/containerd/containerd/commit/fe316cc1f8cad5cd9246e2f4eadd6806b94d866d) remotes: fix possible panic from WithMediaTypeKeyPrefix
- Fix vagrant on CI ([#13065](https://github.com/containerd/containerd/pull/13065)) [`f198b7f87`](https://github.com/containerd/containerd/commit/f198b7f8775d887f93e1a024696b095805440e9d) Ignore NOCHANGE error
- Fix TOCTOU race bug in tar extraction ([#12969](https://github.com/containerd/containerd/pull/12969)) [`aecfb3dc6`](https://github.com/containerd/containerd/commit/aecfb3dc641561a46a8d7dd6d444163cbae5ff88) Fix TOCTOU race bug in tar extraction
- cri: Fix image volumes with user namespaces ([#12894](https://github.com/containerd/containerd/pull/12894)) [`8d5351929`](https://github.com/containerd/containerd/commit/8d5351929995719667e375a89a55e6463a6957bb) cri: Fix image volumes with user namespaces
- core/mount: fix getUnprivilegedMountFlags iterating over indices instead of values ([#12943](https://github.com/containerd/containerd/pull/12943)) [`74e575ce8`](https://github.com/containerd/containerd/commit/74e575ce8ce95c2616acbffd3711c684757807b5) core/mount: add test for getUnprivilegedMountFlags [`c62466642`](https://github.com/containerd/containerd/commit/c624666429168da3a308697c90e3842681a7a9e8) core/mount: fix getUnprivilegedMountFlags iterating over indices instead of values
- Fix CNI issue where CNI DEL is never executed ([#12930](https://github.com/containerd/containerd/pull/12930)) [`9710aed4a`](https://github.com/containerd/containerd/commit/9710aed4a05c964b7fbcee9a13d2ae58a6ee08c2) fix issue where cni del is never executed
- integration: Fix TestImageLoad() failure on CI ([#12907](https://github.com/containerd/containerd/pull/12907)) [`51a63212f`](https://github.com/containerd/containerd/commit/51a63212ffd7ec0ecf05bd46429561b2fc847896) integration: Fix TestImageLoad() failure on CI
- fix: sanitize error before gRPC return to prevent credential leak in pod events ([#12803](https://github.com/containerd/containerd/pull/12803)) [`b65f34e15`](https://github.com/containerd/containerd/commit/b65f34e15c8a5b00dba6f18b976bb65202edfc1b) fix: sanitize error before gRPC return to prevent credential leak in pod events

### 2.1.8

- Fix handling of out-of-range USER values in OCI spec to avoid unexpected username/group lookups
- Fix bugs in sandbox service affecting sandbox creation configuration and event publishing
- backport: sandbox: forward Create fields, fix event topics ([#13272](https://github.com/containerd/containerd/pull/13272)) [`f3b4b35c9`](https://github.com/containerd/containerd/commit/f3b4b35c94cab35c398df89800b198e94984e2f6) sandbox: forward Create fields, fix event topics


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.1.8**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `containerd/containerd`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/containerd.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
