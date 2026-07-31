---
id: TROUBLE-CONTAINERD_1_6_DEFECTS
type: troubleshooting
title: "containerd 1.6: defects fixed in the 1.6 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.6.0 <1.7.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - containerd 1.6 known issues
  - containerd 1.6 fixed in
  - is this containerd bug already fixed
tags:
  - troubleshooting
  - upgrade
  - containerd
sources:
  - type: docs
    path: containerd/containerd release notes for the 1.6 line — bug-fix entries
    url: https://github.com/containerd/containerd/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# containerd 1.6: defects fixed in the 1.6 line

## Summary

**219 defects** the project fixed across **36 releases** of the 1.6 line, from 1.6.0 to
1.6.39. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.6.0

- cri: fix handling of ignore_rdt_not_enabled_errors config option ([#6514](https://github.com/containerd/containerd/pull/6514)) cri: fix handling of ignore_rdt_not_enabled_errors config option
- fix: .dockerignore make git working tree dirty ([#6523](https://github.com/containerd/containerd/pull/6523)) fix: .dockerignore makes git working tree dirty
- remotes: fix dockerPusher to handle abort correctly ([#6243](https://github.com/containerd/containerd/pull/6243)) remotes: fix dockerPusher to handle abort correctly
- Fix possibly incorrect media type default on import ([#6475](https://github.com/containerd/containerd/pull/6475)) Fix possibly incorrect media type default on import
- Fix acr fetch token 400 ([#6481](https://github.com/containerd/containerd/pull/6481)) fix acr fetch token 400
- Fix windows periodic workflow ([#6476](https://github.com/containerd/containerd/pull/6476)) Fix windows periodic workflow
- fix: should not send 137 code event if cmd is notfound ([#6465](https://github.com/containerd/containerd/pull/6465)) fix: should not send 137 code event if cmd is notfound
- Fix empty scopes return ([#6463](https://github.com/containerd/containerd/pull/6463)) fix empty scopes return
- services/introspection: fix plugin caching to show grpc plugins ([#6432](https://github.com/containerd/containerd/pull/6432)) Update caching logic to avoid map access services/introspection: support to show introspection grpc service
- Fix rdt build tags for go 1.16 ([#6459](https://github.com/containerd/containerd/pull/6459)) Fix rdt build tags for go 1.16
- tracing: fix OTLP tracer's initialization ([#6443](https://github.com/containerd/containerd/pull/6443)) tracing: fix OTLP tracer's initialization
- Fix wrong log message ([#6419](https://github.com/containerd/containerd/pull/6419)) Fix wrong log message
- Followup errors change ([#6414](https://github.com/containerd/containerd/pull/6414)) Fix incorrect error wrapped when closing ingest file Fix seek error used without nil check Fix followup items from errors replacement
- fix: use _ for consistency ([#6391](https://github.com/containerd/containerd/pull/6391)) fix: use _ for consistency
- fix(ctr): enable networking for Windows containers ([#6304](https://github.com/containerd/containerd/pull/6304)) fix(ctr): enable networking for Windows containers
- only test abstract uds on linux ([#6395](https://github.com/containerd/containerd/pull/6395)) fix: only test abstract unix socket on linux
- Fix restart container test ([#6390](https://github.com/containerd/containerd/pull/6390)) Expect ErrorNotFound on Windows after Kill() Replace tskill with taskkill
- fix when kernel version < 4.13rc1 by using index=off cause test error ([#6291](https://github.com/containerd/containerd/pull/6291)) fix when kernel version < 4.13rc1 by using index=off cause overlay test error
- Fix no-daemon flag for integration/client tests ([#6384](https://github.com/containerd/containerd/pull/6384)) Fix no-daemon flag for integration/client tests
- Fix flakiness on Windows for list stats ([#6385](https://github.com/containerd/containerd/pull/6385)) Fix flakiness on Windows for list stats
- cri-integration: Add Windows defaults and fix spaces issue ([#6347](https://github.com/containerd/containerd/pull/6347)) cri-integration: Add Windows default paths
- seutil: Fix setting the "container_kvm_t" label ([#6372](https://github.com/containerd/containerd/pull/6372)) seutil: Fix setting the "container_kvm_t" label
- Fix executable file not found when restoring shims ([#6278](https://github.com/containerd/containerd/pull/6278)) Fix executable file not found when restoring shims
- releases: mark 1.4 as Extended ([#6287](https://github.com/containerd/containerd/pull/6287)) docs: mark 1.4 as Extended docs: fix RELEASES.md gRPC API anchor
- Fix wrong make target on documentation ([#6276](https://github.com/containerd/containerd/pull/6276)) Fix wrong make target on documentation
- fix: server error return ([#6272](https://github.com/containerd/containerd/pull/6272)) fix: server error return
- feat:support custom callopts on client side ([#6254](https://github.com/containerd/containerd/pull/6254)) fix: make max recv/send msg size setting default feat:support custom callopts on client side
- [CRI] Fix panic when registry.mirrors use localhost ([#6258](https://github.com/containerd/containerd/pull/6258)) [CRI] Fix panic when registry.mirrors use localhost
- Allow absolute path to shim binaries ([#6206](https://github.com/containerd/containerd/pull/6206)) Fix package alias Support custom runtime path when launching tasks Add runtime path in CreateTaskRequest
- Fix wrong error returned for image index lookup ([#6237](https://github.com/containerd/containerd/pull/6237)) Fix wrong error returned for image index lookup
- Fix containerd fails to pull OCI image with non-`http(s)://` urls ([#6221](https://github.com/containerd/containerd/pull/6221)) Fix containerd fails to pull OCI image with non-`http(s)://` urls
- Decouple task manager ([#5918](https://github.com/containerd/containerd/pull/5918)) Address PR comments Fix build after rebase Migrate task directory Expose shim process interface Fix after rebase Cleanup shim loading Move shim restore to a separate file Fix backward compatibility with old task shims Add plugin dependency between shim and shim services Rework task create and cleanup flow Add task manager Rename task manager to shim manager
- fix shim reaper wait command execute blocked ([#6166](https://github.com/containerd/containerd/pull/6166)) fix shim reaper wait command execute blocked
- fix #6054 MaxConcurrentDownloads is not effect when Unpack is true ([#6109](https://github.com/containerd/containerd/pull/6109)) fix #6054 MaxConcurrentDownloads is not effect when Unpack is true
- Fix spelling mistake in Windows snapshotter ([#6132](https://github.com/containerd/containerd/pull/6132)) Fix spelling mistake in Windows snapshotter
- add runc shim support for sched core ([#6011](https://github.com/containerd/containerd/pull/6011)) fix integration client vendor add runc shim support for sched core
- Fixes Windows containers with image volumes ([#6034](https://github.com/containerd/containerd/pull/6034)) Windows: Fixes Windows containers with image volumes
- fix: import from k8s.io/utils/clock instead ([#6076](https://github.com/containerd/containerd/pull/6076)) fix: update vendor cleanup: import from k8s.io/utils/clock/testing instead cleanup: import from k8s.io/utils/clock instead
- feat: support import image for specific platform ([#6070](https://github.com/containerd/containerd/pull/6070)) fix: wrong flag type feat: support import image for specific platform
- fix: make exec-id flag required in exec command ([#6059](https://github.com/containerd/containerd/pull/6059)) fix: make exec-id flag required in exec command
- Fix main branch build is broken ([#6047](https://github.com/containerd/containerd/pull/6047)) Fix main branch build is broken
- Fix panic in metadata content writer on copy error ([#6043](https://github.com/containerd/containerd/pull/6043)) Fix panic in metadata content writer on copy error
- ctr: Fixes Windows image import ([#5916](https://github.com/containerd/containerd/pull/5916)) ctr: Fixes Windows image import
- update open go.opentelemetry.io v1.0.0 to fix import path ([#6017](https://github.com/containerd/containerd/pull/6017)) go.mod: update opentelemetry modules to v1.0.0
- fix error string format ([#5979](https://github.com/containerd/containerd/pull/5979)) fix error string format
- FreeBSD: fix tar headers & the nil check on getxattr ([#5991](https://github.com/containerd/containerd/pull/5991)) FreeBSD: fix tar headers & the nil check on getxattr
- Fixes task kill --force on Windows ([#5956](https://github.com/containerd/containerd/pull/5956)) Fixes task kill --force on Windows
- Fix content copy to not ignore unexpected EOF ([#5966](https://github.com/containerd/containerd/pull/5966)) Fix content copy to not ignore unexpected EOF
- fix document non-synchronous ([#5947](https://github.com/containerd/containerd/pull/5947)) fix document non-synchronous in crictl.md
- Fix cwd flag for `ctr tasks exec` ([#5932](https://github.com/containerd/containerd/pull/5932)) Fix cwd flag for `ctr tasks exec`
- Fix pull fails on unexpected EOF ([#5921](https://github.com/containerd/containerd/pull/5921)) Fix pull fails on unexpected EOF
- Fix dir support for devices ([#5845](https://github.com/containerd/containerd/pull/5845)) Adding testing of two devices Fix dir support for devices V3 (#4847)
- integration: fix TestContainerPids ([#5896](https://github.com/containerd/containerd/pull/5896)) integration: fix TestContainerPids
- Fix bad `make protos` failure ([#5857](https://github.com/containerd/containerd/pull/5857)) Fix bad `make protos` failure
- replace cri and point to new location ([#5851](https://github.com/containerd/containerd/pull/5851)) archive docs and point to new location fix #https://github.com/containerd/cri/issues/1624
- BUILDING.md: remove some bits about building runc ([#5850](https://github.com/containerd/containerd/pull/5850)) BUILDING.md: remove some bits about building runc BUILDING.md: markdown fixes
- Fix Linux CI Linter using Go 1.15.14 ([#5839](https://github.com/containerd/containerd/pull/5839)) Fix Linux CI Linter using go 1.15.14
- Fuzzing: Fix for OSS-fuzz issue 36825 ([#5829](https://github.com/containerd/containerd/pull/5829)) Fuzzing: Fix for OSS-fuzz issue 36825
- scripts: linting fixes, and remove support for Debian Jessie (as it's EOL) ([#5760](https://github.com/containerd/containerd/pull/5760)) scripts: declare ROOT closer to where it's used, and some DRY changes scripts: add missing quotes, and minor linting issues test/build-utils.sh: remove support for Debian Jessie
- runtime: fix the issue of create new socket with abstract address ([#5746](https://github.com/containerd/containerd/pull/5746)) runtime: fix the issue of create new socket with abstract address
- mergo: Upgrade to 0.3.12 to fix panic ([#5809](https://github.com/containerd/containerd/pull/5809)) mergo: Upgrade to 0.3.12 to fix panic
- remotes/docker/pusher.go: Fix missing Close() on push to docker remote ([#5770](https://github.com/containerd/containerd/pull/5770)) remotes/docker/pusher.go: Fix missing Close()
- remotes/docker/fetcher.go: Fix missing Close() on fetch from docker remote ([#5769](https://github.com/containerd/containerd/pull/5769)) remotes/docker/fetcher.go: Fix missing Close()
- Fix missing Body.Close() calls on push to docker remote ([#5712](https://github.com/containerd/containerd/pull/5712)) Fix missing Body.Close() calls on push to docker remote
- Fix cleanup context of teardownPodNetwork ([#5569](https://github.com/containerd/containerd/pull/5569)) Fix cleanup context of teardownPodNetwork
- fix invalid validation error checking ([#5565](https://github.com/containerd/containerd/pull/5565)) fix invalid validation error checking
- diff/walking: fix defer cleanup ([#5551](https://github.com/containerd/containerd/pull/5551)) diff/walking: fix defer cleanup
- Fix error case in Windows layer cleanup ([#5328](https://github.com/containerd/containerd/pull/5328)) Fix error case in Windows layer cleanup
- Use DeactivateLayer to unlock layers that we cannot rename ([#5422](https://github.com/containerd/containerd/pull/5422)) Small typo fix "reimporst" Use DeactivateLayer to recover layers that we cannot rename
- docs/cri: update links ([#5548](https://github.com/containerd/containerd/pull/5548)) docs/cri: update ocicrypt link docs/cri: fix broken links
- Fix incorrect UA used for registry authentication ([#5533](https://github.com/containerd/containerd/pull/5533)) Fix incorrect UA used for registry authentication
- Fix mounts for FreeBSD ([#5472](https://github.com/containerd/containerd/pull/5472)) Add ruleset=4 option Remove mountpoints not commonly mounted on FreeBSD Add copyright header & make sure compilation succeeds on all platforms Fix mounts for FreeBSD
- Fix small typo ([#5528](https://github.com/containerd/containerd/pull/5528)) Fix small typo
- Fixed typos in docs ([#5509](https://github.com/containerd/containerd/pull/5509)) fixed typos
- Fix `content.ReaderAt` close ([#5468](https://github.com/containerd/containerd/pull/5468)) Fix content.ReaderAt close
- oci: fix WithDevShmSize ([#5063](https://github.com/containerd/containerd/pull/5063)) oci: fix WithDevShmSize
- Fix different registry hosts referencing the same auth config. ([#5446](https://github.com/containerd/containerd/pull/5446)) Fix different registry hosts referencing the same auth config
- v2: Fix inotify fd leak when cgroup is deleted ([#212](https://github.com/containerd/cgroups/pull/212)) v2: add test case for Manager.EventChan() behavior v2: flip error handling for readKVStat("memory.events") to reduce indentation v2: manager: factor out memory.events parsing v2: Fix inotify leak when cgroup is deleted
- fix Implicit memory aliasing in for loop ([#214](https://github.com/containerd/cgroups/pull/214)) fix Implicit memory aliasing in for loop
- Fix potential dirfd leak. ([#210](https://github.com/containerd/cgroups/pull/210)) Fix potential dirfd leak
- Fix CI ([#55](https://github.com/containerd/console/pull/55)) Fix CI Stop using pkg/errors
- fix fmt.Errorf("%w", err) on err == nil ([#187](https://github.com/containerd/continuity/pull/187)) fix fmt.Errorf("%w", err) on err == nil
- Fix darwin issues ([#186](https://github.com/containerd/continuity/pull/186)) update AUTHORS darwin: use utimensat syscall instead of utimes fix darwin usage of du command
- cni: fix data-race on lazy init by ensureExec(). ([#82](https://github.com/containerd/go-cni/pull/82)) cni: fix data-race on lazy init by ensureExec()
- README: Fix CRI decryption document URL ([#53](https://github.com/containerd/imgcrypt/pull/53)) README: Fix CRI decryption document URL

### 1.6.2

- **Fix the inheritable capability defaults** ([GHSA-c9cp-9c75-9v8c](https://github.com/containerd/containerd/security/advisories/GHSA-c9cp-9c75-9v8c))
- Github Security Advisory [GHSA-c9cp-9c75-9v8c](https://github.com/containerd/containerd/security/advisories/GHSA-c9cp-9c75-9v8c) Fix the Inheritable capability defaults

### 1.6.3

- **Fix panic when configuring tracing plugin**
- **Fix deadlock from leaving transaction open in native snapshotter**
- [release/1.6] tracing: fix panic on startup when configured ([#6853](https://github.com/containerd/containerd/pull/6853)) [`e8da82adc`](https://github.com/containerd/containerd/commit/e8da82adcdc667d8247bd27a8b2c835d0872066b) tracing: fix panic on startup when configured
- [release/1.6] metrics/cgroups: fix deadlock issue in Add during Collect ([#6801](https://github.com/containerd/containerd/pull/6801)) [`fe6ba62ce`](https://github.com/containerd/containerd/commit/fe6ba62ceae6c4b692d4a8feb5655f59351abd05) metrics/cgroups: fix deadlock issue in Add during Collect
- [release/1.6 backport] native: fix deadlock from leaving transactions open ([#6727](https://github.com/containerd/containerd/pull/6727)) [`28b44826b`](https://github.com/containerd/containerd/commit/28b44826b004cb04a3d53820c1ba4f845d351963) native: fix deadlock from leaving transactions open
- Fix Loopback Version ([#88](https://github.com/containerd/go-cni/pull/88)) [`9ebcec1`](https://github.com/containerd/go-cni/commit/9ebcec1f5aae75ddd28394898d310212bc87c478) Update loopback version to support check

### 1.6.4

- **Fix broken SELinux relabeling for Kubernetes volume mounts**

### 1.6.5

- **Fix for older CNI plugins not reporting version**
- **Fix mount path handling for CRI plugin on Windows**
- [release/1.6] Bug fix for mount path handling ([#6929](https://github.com/containerd/containerd/pull/6929)) [`70839a344`](https://github.com/containerd/containerd/commit/70839a344033dbb86ae152b30a747f9258527c9e) Bug fix for mount path handling

### 1.6.6

- **Fix ExecSync handler to cap console output size** ([GHSA-5ffw-gxpp-mxpf](https://github.com/containerd/containerd/security/advisories/GHSA-5ffw-gxpp-mxpf))

### 1.6.7

- **Windows: Update hcsshim to v0.9.4 to fix regression with HostProcess stats**
- **Windows: Fix shim logs going to panic.log file**
- [release/1.6] Fix WWW-Authenticate parsing ([#7131](https://github.com/containerd/containerd/pull/7131)) [`37dfc5c9d`](https://github.com/containerd/containerd/commit/37dfc5c9db66afcfa47b6f40b7797763ac3fde76) [release/1.6] Fix WWW-Authenticate parsing
- [release/1.6] ctr: fix label args used in NewContainer ([#7051](https://github.com/containerd/containerd/pull/7051)) [`99c56d217`](https://github.com/containerd/containerd/commit/99c56d2175bc02f0fc4db58014b9b483021051a0) ctr: fix label args used in NewContainer

### 1.6.9

- **Fix CRI: Do not append []string{""} to command to preserve Docker compatibility**
- **Fix OCI resolver to skip TLS verification for localhost**
- **Fix createTarFile: make xattr EPERM non-fatal**
- **Fix CRI plugin to setup pod network after creating the sandbox container**
- **Fix OCI pusher to retry request on writer reset**
- **Fix archive to validate digests before use**
- **Fix CRI: PodSandboxStatus should tolerate missing task**
- **Fix io.containerd.runc.v1: Stats() shouldn't assume s.container is non-nil**
- [release/1.6] fix pusher concurrent close channel ([#7562](https://github.com/containerd/containerd/pull/7562)) [`29e2dea50`](https://github.com/containerd/containerd/commit/29e2dea5083e9b257471db5380a1b8ff32ae9219) fix pusher concurrent close channel
- [release 1.6 backport] Fix cleanup in critest ([#7274](https://github.com/containerd/containerd/pull/7274)) [`5c230ece0`](https://github.com/containerd/containerd/commit/5c230ece0fa985fbc973d1e6dea743439ca2c527) Fix cleanup in critest
- Fix wrapping errors ([#196](https://github.com/containerd/continuity/pull/196)) [`def6729`](https://github.com/containerd/continuity/commit/def67296172f65f5827e5355efac79e0c1331a48) fs: fix wrapping nil err [`b17bab4`](https://github.com/containerd/continuity/commit/b17bab433315a4936debf5c0c150d9f4e36d7088) fmt.Errorf: use %w, not %v to wrap errors

### 1.6.10

- **Bump hcsshim to 0.9.5 to fix container shutdown bug on Windows**

### 1.6.11

- **Fix nil pointer deference for Windows containers in CRI plugin**
- **Fix lease labels unexpectedly overwriting expiration**
- **Fix for simultaneous diff creation using the same parent snapshot**
- [release/1.6] fix: support simultaneous create diff for same parent snapshot ([#7756](https://github.com/containerd/containerd/pull/7756)) fix: support simultaneous create diff for same parent snapshot
- [release/1.6] cherry-pick: Fix order of operations when setting lease labels ([#7745](https://github.com/containerd/containerd/pull/7745)) Fix order of operations when setting lease labels

### 1.6.12

- **Fix goroutine leak during Exec in CRI plugin** ([GHSA-2qjp-425j-52j9](https://github.com/containerd/containerd/security/advisories/GHSA-2qjp-425j-52j9))
- Github Security Advisory [GHSA-2qjp-425j-52j9](https://github.com/containerd/containerd/security/advisories/GHSA-2qjp-425j-52j9) Prepare release notes for v1.6.12 CRI stream server: Fix goroutine leak in Exec

### 1.6.13

- **Update hcsschim to v0.9.6 to fix resource leak on exec**
- **Fix concurrent map iteration and map write in CRI port forwarding**
- [release/1.6] Cherry pick GitHub actions workflow updates 1.6 ([#7713](https://github.com/containerd/containerd/pull/7713)) update codeql-action to v2 Upgrade actions/upload-artifact from v2 to v3 Move up actions versions to prep for deprecation CI: update GHA instances from Ubuntu 18.04 to 20.04 Use global env variable to specify Go version on CI Rework permission handling in scripts fix pool_device_test.go
- [release/1.6] fix: check for tmpfs when evaluating if userxattr should be used ([#7788](https://github.com/containerd/containerd/pull/7788)) fix: check for tmpfs when evaluating if userxattr should be used

### 1.6.14

- **Fix `memory.memsw.limit_in_bytes: no such file or directory` error in CRI plugin**
- [release/1.6] cri: fix `memory.memsw.limit_in_bytes: no such file or directory` ([#7838](https://github.com/containerd/containerd/pull/7838)) [`53c733e0b`](https://github.com/containerd/containerd/commit/53c733e0bacd44d52cbe58a31dbc1ff2ca0d5403) cri: fix `memory.memsw.limit_in_bytes: no such file or directory`
- ParseCgroupFile: fix wrong comment about unified hierarchy ; add ParseCgroupFileUnified to get the unified path ([#232](https://github.com/containerd/cgroups/pull/232)) [`dd81920`](https://github.com/containerd/cgroups/commit/dd81920d1b44d7d9f75d93e40a74333e9afd4b92) add ParseCgroupFileUnified to get the unified path [`dae6735`](https://github.com/containerd/cgroups/commit/dae6735f2be5a4dbeb43eb726a26419aef9e2185) ParseCgroupFile: fix wrong comment about unified hierarchy
- Fix systemd full path ([#221](https://github.com/containerd/cgroups/pull/221)) [`aa8003c`](https://github.com/containerd/cgroups/commit/aa8003ca79589e6ab8a1d081b2d768eb9f35b5c8) Fix systemd full path
- Fix panic in NewSystemd on nil values ([#219](https://github.com/containerd/cgroups/pull/219)) [`65478b8`](https://github.com/containerd/cgroups/commit/65478b8fddda44862ebb6bb2b69122a22e61eba5) Fix panic in NewSystemd on nil values

### 1.6.15

- **Fix no CNI info for pod sandbox on restart in CRI plugin**
- [release/1.6] CRI: Fix no CNI info for pod sandbox on restart ([#7848](https://github.com/containerd/containerd/pull/7848)) [`f16447e2d`](https://github.com/containerd/containerd/commit/f16447e2d495d77c03c6644e78877cd3596ef523) CRI: Fix no CNI info for pod sandbox on restart

### 1.6.16

- **Fix slice append error with HugepageLimits for Linux**
- **Fix overlayfs error when upperdirlabel option is set**
- [release/1.6 backport] Fix tx closed error when upperdirlabel specified ([#8002](https://github.com/containerd/containerd/pull/8002)) [`8c704036a`](https://github.com/containerd/containerd/commit/8c704036a81b13b25ab7073e2715075b6ec39e94) Fix tx closed error when upperdirlabel specified
- [release/1.6 backport] assorted test-fixes ([#8000](https://github.com/containerd/containerd/pull/8000)) [`91a68edd7`](https://github.com/containerd/containerd/commit/91a68edd775bba554a9eac7e04898b22069db5aa) cri: Fix TestUpdateOCILinuxResource for host w/o swap controller [`5594f706e`](https://github.com/containerd/containerd/commit/5594f706e67462c4a29f68e6958341ba35d06826) Fix TestUpdateContainerResources_Memory* on cgroup v2 hosts
- [release/1.6 backport] Fix slice append error ([#7995](https://github.com/containerd/containerd/pull/7995)) [`ab193eb20`](https://github.com/containerd/containerd/commit/ab193eb20bade0c7fff74a33a3b91f2517af05c6) pkg/cri: optimize slice initialization [`e6cf5ec58`](https://github.com/containerd/containerd/commit/e6cf5ec58d395332985f15084527676d70b21f1c) Fix slice append error

### 1.6.18

- **Fix OCI image importer memory exhaustion** ([GHSA-259w-8hf6-59c2](https://github.com/containerd/containerd/security/advisories/GHSA-259w-8hf6-59c2))
- **Fix supplementary groups not being set up properly** ([GHSA-hmfx-3pcx-653p](https://github.com/containerd/containerd/security/advisories/GHSA-hmfx-3pcx-653p))
- Github Security Advisory [GHSA-hmfx-3pcx-653p](https://github.com/containerd/containerd/security/advisories/GHSA-hmfx-3pcx-653p) [`286a01f35`](https://github.com/containerd/containerd/commit/286a01f350a2298b4fdd7e2a0b31c04db3937ea8) oci: fix additional GIDs [`301823453`](https://github.com/containerd/containerd/commit/301823453d788ce409e222e88a27d7faf2c2093d) oci: fix loop iterator aliasing [`0070ab70f`](https://github.com/containerd/containerd/commit/0070ab70fa58045d25fc6ebab27edcae328e38f1) oci: skip checking gid for WithAppendAdditionalGroups [`16d52de64`](https://github.com/containerd/containerd/commit/16d52de64d9b0b0e4bf7e11226199281561a3d96) refactor: reduce duplicate code [`b45e30292`](https://github.com/containerd/containerd/commit/b45e30292ce9b214158fa403a6165aabbf5b23f0) add WithAdditionalGIDs test [`0a06c284a`](https://github.com/containerd/containerd/commit/0a06c284aec5860a58a803b5da83def3462dc3a0) add WithAppendAdditionalGroups helper
- [release/1.6] Fix retry logic within devmapper device deactivation ([#8088](https://github.com/containerd/containerd/pull/8088)) [`d5284157b`](https://github.com/containerd/containerd/commit/d5284157b8af78a2d85e78bd3106695a4e4c995b) Fix retry logic within devmapper device deactivation

### 1.6.19

- **Update hcsshim to v0.9.7 to include fix for graceful termination and pause containers**

### 1.6.20

- [1.6] shim: fix debug flag not working ([#8288](https://github.com/containerd/containerd/pull/8288)) [`28f1e32e3`](https://github.com/containerd/containerd/commit/28f1e32e3b1b167eeab8890d67ed57817b3da29b) shim: fix debug flag not working
- [release/1.1] server: Fix connection leak when receiving ECONNRESET ([#136](https://github.com/containerd/ttrpc/pull/136)) [`8977f59`](https://github.com/containerd/ttrpc/commit/8977f59dbda8a5a97d0801669e4c0d9f5a7088dd) server: Fix connection leak when receiving ECONNRESET

### 1.6.21

- [release/1.6] fix the task setting the runtime path ([#8454](https://github.com/containerd/containerd/pull/8454)) [`e8840f688`](https://github.com/containerd/containerd/commit/e8840f688ae402bef461963321d63cf9cf6fbb34) skip TestContainerStartWithAbsRuntimePath if the runtime is v1 [`75ab094de`](https://github.com/containerd/containerd/commit/75ab094de81b2d6806434e2f9ac94cb409e36314) integration: add container start test using abs runtime path [`f49254f0b`](https://github.com/containerd/containerd/commit/f49254f0b7e17951c1be6e8a8063eb3f47175cd5) WithRuntimePath uses the TaskInfo.RuntimePath field
- [release/1.6 ] Add ArgsEscaped support for CRI ([#8247](https://github.com/containerd/containerd/pull/8247)) [`bc2e01303`](https://github.com/containerd/containerd/commit/bc2e01303b7103d7fe81a97caadc224102db1460) Fix argsEscaped tests [`8b81d5acc`](https://github.com/containerd/containerd/commit/8b81d5acca2e6f390af99756128392253c5d0a5c) Add ArgsEscaped support for CRI

### 1.6.22

- **CRI: Fix additionalGids: it should fallback to imageConfig.User when securityContext.RunAsUser,RunAsUsername are empty**
- **Fix concurrent writes for `UpdateContainerStats`**
- **Resolve docker.NewResolver race condition**
- **Fix cpu architecture detection issue on emulated ARM platform**
- **Fix panic when remote differ returns empty result**
- [release/1.6 backport] [CRI] fix additionalGids: it should fallback to imageConfig.User when securityContext.RunAsUser,RunAsUsername are empty ([#8823](https://github.com/containerd/containerd/pull/8823)) [`cd06f23af`](https://github.com/containerd/containerd/commit/cd06f23af6bcf8c87cda625a0e78168c032a0637) capture desc variable in range variable just in case that it run in parallel mode [`30f5c6a1f`](https://github.com/containerd/containerd/commit/30f5c6a1f26bf34bbe5eaf21acc7d5b86b14e027) Use t.TempDir instead of os.MkdirTemp [`59d8363ef`](https://github.com/containerd/containerd/commit/59d8363ef33caa1a8261f472d3081f7f9d39e75e) fix userstr for dditionalGids on Linux
- [release/1.6 backport] Fix concurrent writes for UpdateContainerStats ([#8819](https://github.com/containerd/containerd/pull/8819)) [`9f650143f`](https://github.com/containerd/containerd/commit/9f650143fafb5927479ea3b5bf2b8e309c2d8265) Fix concurrent writes for UpdateContainerStats
- [release/1.6 backport] Use version 2 configuration format in docs ([#8821](https://github.com/containerd/containerd/pull/8821)) [`5b51b79e2`](https://github.com/containerd/containerd/commit/5b51b79e2c7baf8dad53e48dfddadabff08b711d) [release/1.6] fix remaining "v1 config" plugin IDs [`b7cf26d8d`](https://github.com/containerd/containerd/commit/b7cf26d8dc72f0f79946c289ac68c0f2a581c6c5) docs: Fix sample config.toml syntax [`fcdaf0966`](https://github.com/containerd/containerd/commit/fcdaf09664c006abf711ee88e26f18019643ffd9) docs: migrate config v1 to v2 [`728d5c5f0`](https://github.com/containerd/containerd/commit/728d5c5f0be709e415f72f44c52fe78233ddd97d) Use version 2 config and mention containerd config command
- [release/1.6] Fix cpu architecture detection issue on emulated ARM platform ([#8533](https://github.com/containerd/containerd/pull/8533)) [`2b16e4bfa`](https://github.com/containerd/containerd/commit/2b16e4bfa135e3242b41ae43cf2bb6f3cd3fe9b1) Add unit test to function GetCPUVariantFromArch [`106e36ec3`](https://github.com/containerd/containerd/commit/106e36ec3e7c72036b498b4ac73000d5c1a79d9d) Use uname machine field to get CPU variant if fails at /proc/cpuinfo
- [release/1.6 backport] Fix panic when remote differ returns empty result ([#8640](https://github.com/containerd/containerd/pull/8640)) [`f98122378`](https://github.com/containerd/containerd/commit/f98122378197fb5199bab1d7574288fe276293ee) Fix panic when remote differ returns empty result
- [release/1.6 backport] remotes/docker: ResolverOptions: fix deprecation comments ([#8620](https://github.com/containerd/containerd/pull/8620)) [`56ff20839`](https://github.com/containerd/containerd/commit/56ff2083957e0ca58168f50e89120bb5d0067362) remotes/docker: ResolverOptions: fix deprecation comments
- follow-up-#52: fix the order of cause in fmt.Errorf ([#53](https://github.com/containerd/zfs/pull/53)) [`b3f193d`](https://github.com/containerd/zfs/commit/b3f193d7f00753424184bfd0c584e5c56e7de659) follow-up-#52: fix the order of cause in fmt.Errorf
- README.md: fix CI badge ([#46](https://github.com/containerd/zfs/pull/46)) [`0977d81`](https://github.com/containerd/zfs/commit/0977d815b7d76b21cb861b04c0f0414d26af3046) README.md: fix CI badge

### 1.6.23

- **backport: ro option for userxattr mount check + cherry-pick: Fix ro mount option being passed
- [release/1.6] backport: ro option for userxattr mount check + cherry-pick: Fix ro mount option being passed ([#8888](https://github.com/containerd/containerd/pull/8888)) [`47d73b2de`](https://github.com/containerd/containerd/commit/47d73b2de65c806d93e19879ae86787b6f3735d6) Fix ro mount option being passed

### 1.6.24

- **CRI: fix leaked shim caused by high IO pressure**

### 1.6.25

- **Avoid potential deadlock in create handler in containerd-shim-runc-v2**
- **CRI: fix using the pinned label to pin image**
- [release/1.6] cri: fix using the pinned label to pin image ([#9382](https://github.com/containerd/containerd/pull/9382)) [`b49815300`](https://github.com/containerd/containerd/commit/b4981530050c4b8efb8cab8d41b28d81eb21462d) cri: fix update of pinned label for images [`751b0c186`](https://github.com/containerd/containerd/commit/751b0c1867b2fd52dccae7bafe5f453c99c65076) cri: fix using the pinned label to pin image
- [release/1.6] fix: shimv1 leak issue ([#9345](https://github.com/containerd/containerd/pull/9345)) [`8b51a95fb`](https://github.com/containerd/containerd/commit/8b51a95fb2b05dd3a2c00f16606656300cc8a1cf) fix: shimv1 leak issue
- [release/1.6] Fix ambiguous tls fallback ([#9300](https://github.com/containerd/containerd/pull/9300)) [`5dd64301c`](https://github.com/containerd/containerd/commit/5dd64301c89ad1e428a746f0e90d9d72b45fe1b8) Check scheme and host of request on push redirect [`51df21d09`](https://github.com/containerd/containerd/commit/51df21d09ebfac3e3470529fe1372ca22496e606) Avoid TLS fallback when protocol is not ambiguous
- [release/1.6 backport] fix protobuf aarch64 ([#9284](https://github.com/containerd/containerd/pull/9284)) [`5376afb3d`](https://github.com/containerd/containerd/commit/5376afb3dbec05541b018e361f1343f20dec3ada) fix protobuf aarch64
- [release 1.6] remotes/docker: Fix MountedFrom prefixed with target repository ([#9192](https://github.com/containerd/containerd/pull/9192)) [`2fffc344a`](https://github.com/containerd/containerd/commit/2fffc344ad661b37a3dae6102b47f887c946f105) remotes/docker: Fix MountedFrom prefixed with target repository

### 1.6.26

- [release/1.6] Windows default path overwrite fix ([#9441](https://github.com/containerd/containerd/pull/9441)) [`ede0ad5e1`](https://github.com/containerd/containerd/commit/ede0ad5e12826d574623a79b71bb1fbc49e75172) Fix windows default path overwrite issue

### 1.6.27

- [release/1.6] cri: add deprecation warnings for deprecated CRI configs ([#9547](https://github.com/containerd/containerd/pull/9547)) [`713065793`](https://github.com/containerd/containerd/commit/713065793592c0f877c81712a6f310f3d730bf07) deprecation: fix missing spaces in warnings [`de0cc92a7`](https://github.com/containerd/containerd/commit/de0cc92a793b84118356715503243a2b9664dfa5) cri: add deprecation warning for runtime_root [`833b94149`](https://github.com/containerd/containerd/commit/833b94149b6fd4faa6d4719ef7926257f5b2b098) cri: add deprecation warning for rutnime_engine [`47de3d63d`](https://github.com/containerd/containerd/commit/47de3d63df0e5ffa522dfc2b6cb5b2d472879f28) cri: add deprecation warning for default_runtime [`d421b8fda`](https://github.com/containerd/containerd/commit/d421b8fda9d0d303e1b90a13f378e6fffe7d9187) cri: add warning for untrusted_workload_runtime [`802cb64b0`](https://github.com/containerd/containerd/commit/802cb64b00aab14d0f2edb45c9b89eef0016dc1c) cri: add warning for old form of systemd_cgroup

### 1.6.28

- [release/1.6] carry #9557 - enable ARM CI ([#9636](https://github.com/containerd/containerd/pull/9636)) [`65e1656f2`](https://github.com/containerd/containerd/commit/65e1656f2755727770f2adc90df8b972e7a513f2) cri: fix integration test on cgroupsv2 system [`9cf1e1a39`](https://github.com/containerd/containerd/commit/9cf1e1a39ca17328c973a7d2ed2969e4f98993cc) *: enable ARM64 runner

### 1.6.30

- Fix image pinning when image is not pulled through cri
- Fix config import relative path glob ([#9835](https://github.com/containerd/containerd/pull/9835)) [`0f2068a70`](https://github.com/containerd/containerd/commit/0f2068a70e0824ef7fb13c3e21763428bc58ad40) Fix config import relative path glob
- Fix image pinning when image is not pulled through cri ([#9785](https://github.com/containerd/containerd/pull/9785)) [`2d43994fb`](https://github.com/containerd/containerd/commit/2d43994fb921722002a5043724c6624bfb9d87f0) bug fix: make sure cri image is pinned when it is pulled outside cri

### 1.6.31

- Fix runc shim to only defer init process exits
- Fix runc shim to only defer init process exits ([#10038](https://github.com/containerd/containerd/pull/10038)) [`5e53da4a1`](https://github.com/containerd/containerd/commit/5e53da4a1403e80339e3d2897dd41cce3842b335) runc-shim: only defer init process exits
- Fix compile from version control system (source) use case ([#10011](https://github.com/containerd/containerd/pull/10011)) [`7592f87f0`](https://github.com/containerd/containerd/commit/7592f87f040128b44e1aafef33b0b33c65334209) Fix compile from version control system (source) use case

### 1.6.32

- Prevent GC from schedule itself with 0 period
- Fix snapshotter root path when not under containerd root
- Fix CreatedAt time set to 269 years ago if create network failed
- Fix use of invalid token on retry fetching layer
- Bump hcsshim and go-winio for go1.22 compat ([#10245](https://github.com/containerd/containerd/pull/10245)) [`06724baad`](https://github.com/containerd/containerd/commit/06724baad6be5b669ca84cc236692961c221075f) Bump go-winio to fix struct alignment on go1.22 [`b2fdf63b7`](https://github.com/containerd/containerd/commit/b2fdf63b7ebd8841806d2377ebf095b15d197b3a) Update hcsshim for go1.22 fixes
- Update tooling to Go 1.21.10, 1.22.3 for net/http bug fixes ([#10208](https://github.com/containerd/containerd/pull/10208)) [`5b4facbd6`](https://github.com/containerd/containerd/commit/5b4facbd663a5ead60f20cc914014edc2a6d5a2a) Update toolchain to Go 1.21.10 and 1.22.3
- Fix snapshotter root path when not under containerd root ([#10127](https://github.com/containerd/containerd/pull/10127)) [`f3e8b2ca1`](https://github.com/containerd/containerd/commit/f3e8b2ca199ea760e5f574544ab0ec7da89c9484) CRI: "Fix" imageFSPath behavior [`68db74d19`](https://github.com/containerd/containerd/commit/68db74d191f0bb6d8bb279c6d8c336a5683f19c0) Snapshotters: Export the root path [`cd9b74640`](https://github.com/containerd/containerd/commit/cd9b7464045eb7bad9506b6579caa558c868dc95) Add exports to proxy plugin config [`83cf026b2`](https://github.com/containerd/containerd/commit/83cf026b261e83b10c1c724991669d6d298997b4) Add platform config to proxy plugins
- Fix CreatedAt time set to 269 years ago if create network failed ([#10119](https://github.com/containerd/containerd/pull/10119)) [`c809fa268`](https://github.com/containerd/containerd/commit/c809fa26864cf14b0ae2b4c842e57832c115b541) pod: CreatedAt time will be 269 years ago while creating cri network failed
- Prevent GC from schedule itself with 0 period. ([#10103](https://github.com/containerd/containerd/pull/10103)) [`6ddec44bd`](https://github.com/containerd/containerd/commit/6ddec44bd25708281e1717cf0dfae86dcc1f4710) Prevent GC from schedule itself with 0 period
- Fix use of invalid token on retry fetching layer ([#10064](https://github.com/containerd/containerd/pull/10064)) [`f1a14a12a`](https://github.com/containerd/containerd/commit/f1a14a12ac5574095a3d81bb9941971a5af0ffd2) fix bug that using invalid token to retry fetching layer
- Fix unexpected order of mounts ([#10045](https://github.com/containerd/containerd/pull/10045)) [`9701cf998`](https://github.com/containerd/containerd/commit/9701cf998f6f86d14072a44bc922e4c82aee4684) fix(cri): fix unexpected order of mounts since go 1.19
- Fix some issues in the test script ([containerd/imgcrypt#115](https://github.com/containerd/imgcrypt/pull/115)) [`aa517cc`](https://github.com/containerd/imgcrypt/commit/aa517cc77654cf517cc7bba5529b07da92f033dc) test: Fix order of parameters and remove unnecessary key parameter [`ec72311`](https://github.com/containerd/imgcrypt/commit/ec7231185e276feb10f5b4b974ade62a81d5e9ad) test: Add comments to test case [`2959ec0`](https://github.com/containerd/imgcrypt/commit/2959ec0ec47786956223715812f40eb9e7301786) test: To be able to run testLocalKeys alone add missing env variable
- README: Fix a typo ([containerd/imgcrypt#105](https://github.com/containerd/imgcrypt/pull/105)) [`12e84f5`](https://github.com/containerd/imgcrypt/commit/12e84f51fb70e1fb2bcc624206f707b48671b352) README: Fix a typo

### 1.6.33

- Update Go version to 1.21.11 ([#10299](https://github.com/containerd/containerd/pull/10299)) [`da9a04e54`](https://github.com/containerd/containerd/commit/da9a04e54cac42438c459fda6ec8f2c772c50441) Includes fix for a symlink race on remove
- Fix usage of "unknown" platform ([#10268](https://github.com/containerd/containerd/pull/10268)) [`d4d489496`](https://github.com/containerd/containerd/commit/d4d489496305e9ebab9deb78f718658d1c17579f) core/image: fix usage of "unknown" platform

### 1.6.34

- Fix HPC working directory in pkg/cri/server code
- Updating hcsshim vendoring to 0.9.12 to include an important backported fix ([#10398](https://github.com/containerd/containerd/pull/10398)) [`a0adb2933`](https://github.com/containerd/containerd/commit/a0adb29333f7d2b4b5afe389105b35a4cfcf946a) Updating hcsshim to 0.9.12
- Fix HPC working directory in pkg/cri/server code ([#10361](https://github.com/containerd/containerd/pull/10361)) [`086e1f56e`](https://github.com/containerd/containerd/commit/086e1f56e446740466b113a04f201e2040ae5a22) [release/1.7]: HPC working directory fix in pkg/cri/server code

### 1.6.35

- Revert HPC working directory fix in pkg/cri/server code
- Fix packaged runc reporting incorrect version
- Fix TestNewBinaryIOCleanup failing with gotip ([#10555](https://github.com/containerd/containerd/pull/10555)) [`4ec5cd6bd`](https://github.com/containerd/containerd/commit/4ec5cd6bd0c8d9a87ecade3812007b32e66232b2) Fix TestNewBinaryIOCleanup failing with gotip
- Fix packaged runc reporting incorrect version ([#10558](https://github.com/containerd/containerd/pull/10558)) [`9539b9b7b`](https://github.com/containerd/containerd/commit/9539b9b7b459dd01a1de6694639abd12dfe53361) script/setup/install-runc: fix runc using incorrect version
- Revert HPC working directory fix in pkg/cri/server code ([#10549](https://github.com/containerd/containerd/pull/10549)) [`c3c2b4eec`](https://github.com/containerd/containerd/commit/c3c2b4eec17844c3f3cbd7db9d9d03288ec36252) Revert "[release/1.7]: HPC working directory fix in pkg/cri/server code"
- client: fix tasks with PID 0 cannot be forced to delete ([#10524](https://github.com/containerd/containerd/pull/10524)) [`5c8818782`](https://github.com/containerd/containerd/commit/5c8818782363935285f09b9ced3933c15baadfd8) client: fix tasks with PID 0 cannot be forced to delete

### 1.6.36

- Fix memory leak with `kubectl exec` >= 1.30.0
- Fix bug where init exits were being dropped ([#10676](https://github.com/containerd/containerd/pull/10676)) [`c9617c321`](https://github.com/containerd/containerd/commit/c9617c321f016fef7678f5333075542e6e565cbb) runc-shim: handle pending execs as running [`15ad6ac67`](https://github.com/containerd/containerd/commit/15ad6ac67216a04fcf5c996e0e10b79d9a3bff6d) runc-shim: refuse to start execs after init exits [`7e6a18c24`](https://github.com/containerd/containerd/commit/7e6a18c2472b036eefbb8be6301447391722cc55) runc-shim: remove misleading comment
- Fix TestNewBinaryIOCleanup on Go 1.23 and Linux 5.4 ([#10591](https://github.com/containerd/containerd/pull/10591)) [`4fd7d4eef`](https://github.com/containerd/containerd/commit/4fd7d4eef143baadfad5f37080692bada83d7702) Fix TestNewBinaryIOCleanup on Go 1.23 and Linux 5.4

### 1.6.37

- Fix the race condition during GC of snapshots when client retries
- Fix console TTY leak in runc shim ([#11359](https://github.com/containerd/containerd/pull/11359)) [`3e6f219d7`](https://github.com/containerd/containerd/commit/3e6f219d7337db04b9d471c0d3dea22abf083748) Add integ test to check tty leak [`bc20f7457`](https://github.com/containerd/containerd/commit/bc20f74574b55fc6f7540e7ddcf491fa65ac4e0b) fix master tty leak due to leaking init container object
- Update vagrant host OS to fix Vagrant CI runs ([#11348](https://github.com/containerd/containerd/pull/11348)) [`d92457c71`](https://github.com/containerd/containerd/commit/d92457c71d825faf02ca0c0f58e5971bbd215c82) Remove vagrant scp from the install list
- Fix panic due to nil dereference cgroups v2 ([#11100](https://github.com/containerd/containerd/pull/11100)) [`db096794f`](https://github.com/containerd/containerd/commit/db096794f71ee9729c4cd1fce999c43a25e8e1e3) fix panic due to nil dereference cgroups v2
- Fix the race condition during GC of snapshots when client retries ([#10764](https://github.com/containerd/containerd/pull/10764)) [`74951d6cf`](https://github.com/containerd/containerd/commit/74951d6cf22eb1f21522229cd8e22b9c4480923d) Fix the race condition during GC of snapshots when client retries

### 1.6.38

- Fix integer overflow in User ID handling ([GHSA-265r-hfxg-fhmg](https://github.com/containerd/containerd/security/advisories/GHSA-265r-hfxg-fhmg))
- Fix fatal map concurrency error in httpstream
- Remove hashicorp/go-multierror dependency and fix CI ([#11500](https://github.com/containerd/containerd/pull/11500)) [`7cc3b3dce`](https://github.com/containerd/containerd/commit/7cc3b3dcec509f1ce2e5d52887520baa48201c54) e2e: use the shim bundled with containerd artifact [`0733895f3`](https://github.com/containerd/containerd/commit/0733895f3de3df51fe4e14563ee94a98df1be8dd) Remove unnecessary joinError unwrap [`054c4cc79`](https://github.com/containerd/containerd/commit/054c4cc79c929eecfb9724fd1c3e9f13a4cd5701) Remove hashicorp/go-multierror [`ff21be0ee`](https://github.com/containerd/containerd/commit/ff21be0ee8b274c05a542a096c1042ef63857f09) Update go to 1.20 to use its multi error support [`f63b5fd3f`](https://github.com/containerd/containerd/commit/f63b5fd3f9b4b809d94d4a3053c4d76a7753072c) update containerd/project-checks to 1.2.1
- Fix fatal map concurrency error in httpstream ([#11319](https://github.com/containerd/containerd/pull/11319)) [`abd1692cf`](https://github.com/containerd/containerd/commit/abd1692cf27bcff4590207bdd8a827b06657c446) fix fatal error: concurrent map iteration and map write

### 1.6.39

- Fix close container io not closed when runtime create failed
- Backport windows test fixes ([#12122](https://github.com/containerd/containerd/pull/12122)) [`9cc952fb0`](https://github.com/containerd/containerd/commit/9cc952fb0b8e092b40c6187209dc9624377cb6cd) Fix intermittent test failures on Windows CIs [`555a34af0`](https://github.com/containerd/containerd/commit/555a34af0511f64eafcc1141b5a0a0e996f2751e) Remove WS2025 from CIs due to regression
- Fix close container io not closed when runtime create failed ([#12052](https://github.com/containerd/containerd/pull/12052)) [`22f669a7c`](https://github.com/containerd/containerd/commit/22f669a7c0bc30beaa7337a02646ec882d3f2174) bugfix:close container io when runtime create failed
- Fix CI ([#11804](https://github.com/containerd/containerd/pull/11804)) [`57250c719`](https://github.com/containerd/containerd/commit/57250c7197b60b6a06d65f2c1a9b07b0b8605a83) Skip criu on Arms [`9d350bbbd`](https://github.com/containerd/containerd/commit/9d350bbbdabb45ea248cd5266322965874290ed2) Address cgroup mountpoint does not exist [`78cbefc95`](https://github.com/containerd/containerd/commit/78cbefc954ec04caa26e7e09b8d8de12960988a0) ci: update GitHub Actions release runner to ubuntu-24.04
- Fix `error: implicit declaration of function ‘memcpy’` ([containerd/btrfs#44](https://github.com/containerd/btrfs/pull/44)) [`3fb5c91`](https://github.com/containerd/btrfs/commit/3fb5c91f016ebdfc72a0c64e81889defdb1dd51d) CI: update (Go 1.23, etc.) [`cab79ec`](https://github.com/containerd/btrfs/commit/cab79ec9ea7e1b910e9aef01afbf87efb57ee674) CI: enable jobs for release/1.0 [`12b3998`](https://github.com/containerd/btrfs/commit/12b3998bdd04e4c8b36d69faf5e65d8157be94c8) Fix `error: implicit declaration of function ‘memcpy’`


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.6.39**, the newest release recorded here for this line.

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
