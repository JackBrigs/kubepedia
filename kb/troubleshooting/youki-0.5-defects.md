---
id: TROUBLE-YOUKI_0_5_DEFECTS
type: troubleshooting
title: "youki 0.5: defects fixed in the 0.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.5.0 <0.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - youki 0.5 known issues
  - youki 0.5 fixed in
  - is this youki bug already fixed
tags:
  - troubleshooting
  - upgrade
  - youki
sources:
  - type: docs
    path: youki-dev/youki release notes for the 0.5 line — bug-fix entries
    url: https://github.com/youki-dev/youki/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# youki 0.5: defects fixed in the 0.5 line

## Summary

**85 defects** the project fixed across **8 releases** of the 0.5 line, from 0.5.0 to
0.5.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.5.0

- Fixed ENAMETOOLONG error in setup_console_socket by @morganllewellynjones in https://github.com/youki-dev/youki/pull/2915
- fix(libcontainer) no_pivot args is not used by @xujihui1985 in https://github.com/youki-dev/youki/pull/2923
- Fix/return multi errors on create failed by @xujihui1985 in https://github.com/youki-dev/youki/pull/2998
- fix duplicate gids in container creation by @YJDoc2 in https://github.com/youki-dev/youki/pull/3019
- Fix --preserve-fds, eliminate stray FD being passed into container by @aidanhs in https://github.com/youki-dev/youki/pull/2893
- ci: update action versions to fix deprecation warnings by @YJDoc2 in https://github.com/youki-dev/youki/pull/2918
- deps: update wasmedge to 0.14.0 by @YJDoc2 in https://github.com/youki-dev/youki/pull/2928
- Bump oci-spec to 0.7.0 by @kiokuless in https://github.com/youki-dev/youki/pull/2934
- remove incorrect dependency in readme by @YJDoc2 in https://github.com/youki-dev/youki/pull/2940
- Add seccomp into feature flags of youki to be compiled in by @musaprg in https://github.com/youki-dev/youki/pull/2924
- Add unittest to expertiment seccomp programs by @sat0ken in https://github.com/youki-dev/youki/pull/2956
- print "unknown" instead of defaults if we cannot get kernel config by @YJDoc2 in https://github.com/youki-dev/youki/pull/2964
- Add test process rlimits by @sat0ken in https://github.com/youki-dev/youki/pull/2977
- Add test process user by @sat0ken in https://github.com/youki-dev/youki/pull/2978
- add test process_oom_score_adj by @saku3 in https://github.com/youki-dev/youki/pull/2987
- Add process test by @sat0ken in https://github.com/youki-dev/youki/pull/2968
- refactor(test): refine function create_container by @xujihui1985 in https://github.com/youki-dev/youki/pull/2973
- Add test root readonly by @sat0ken in https://github.com/youki-dev/youki/pull/2976
- Adding Discord link to docs by @crmejia in https://github.com/youki-dev/youki/pull/3005
- Prepare for v0.5.0 by @utam0k in https://github.com/youki-dev/youki/pull/3016
- Use later stable rust version 1.81.0 to fix the CI by @musaprg in https://github.com/youki-dev/youki/pull/3033
- Don't specify the versionFile for tagpr by @utam0k in https://github.com/youki-dev/youki/pull/3036
- selinux: fix xattr and remove anyhow by @Gekko0114 in https://github.com/youki-dev/youki/pull/2936

### 0.5.1

- Fix building the wasmedge feature by @utam0k in https://github.com/youki-dev/youki/pull/3041
- Do `cargo check` before releasing a new version by @utam0k in https://github.com/youki-dev/youki/pull/3039

### 0.5.2

- fix(libcgroup): fix disable_oom_killer in cgroup v1 by @xujihui1985 in https://github.com/youki-dev/youki/pull/3090
- Add a PR template file by @Gekko0114 in https://github.com/youki-dev/youki/pull/3049
- add process rlimits fail test by @ntkm61027 in https://github.com/youki-dev/youki/pull/3051
- Use MountOption enum to parse mount options defined in the spec by @musaprg in https://github.com/youki-dev/youki/pull/2937
- ci: Publish packages after the release flow by @utam0k in https://github.com/youki-dev/youki/pull/3064
- Make `sepc` into `&spec` in test_{outside,inside}_containe by @utam0k in https://github.com/youki-dev/youki/pull/3068
- linux_masked_paths integration test by @nayuta-ai in https://github.com/youki-dev/youki/pull/2950
- fix: compilation errors in contest by @YJDoc2 in https://github.com/youki-dev/youki/pull/3086
- Remove problematic comments between package name in apt install by @musaprg in https://github.com/youki-dev/youki/pull/3060
- Add `delete` test by @sou1118 in https://github.com/youki-dev/youki/pull/3082

### 0.5.3

- Security: Fix compromised `tj-actions/changed-files` action by @sou1118 in https://github.com/youki-dev/youki/pull/3112
- Fix the release flow by @utam0k in https://github.com/youki-dev/youki/pull/3098
- chore(ci): add cgroup v1 compatibility for tests on ubuntu-24.04 by @sou1118 in https://github.com/youki-dev/youki/pull/3102
- fix: CPU controller tests for Kernel 6.10 cgroup v2 changes by @sou1118 in https://github.com/youki-dev/youki/pull/3106
- chore(ci): Upgrade GitHub Actions workflows for `ubuntu-24.04` by @sou1118 in https://github.com/youki-dev/youki/pull/3097
- fix: release ci tests also need apparmor disable by @YJDoc2 in https://github.com/youki-dev/youki/pull/3118
- chore(ci): add criu ppa for podman-tests ci by @sou1118 in https://github.com/youki-dev/youki/pull/3120

### 0.5.4

- fix: allow duplicate additionalGids by @saku3 in https://github.com/youki-dev/youki/pull/3189
- use additional gids,user,group in exec, inject path iif not given by @YJDoc2 in https://github.com/youki-dev/youki/pull/3131
- fix: mount retry and logging by @z63d in https://github.com/youki-dev/youki/pull/3157
- fix: Gracefully terminate processes after successful execution of Wasm executors by @z63d in https://github.com/youki-dev/youki/pull/3099
- fix: Running create_runtime hook after container is set to created. by @CheatCodeSam in https://github.com/youki-dev/youki/pull/3181
- fix: Ignoring CPU realtime on cgroupsv2 if set to zero by @CheatCodeSam in https://github.com/youki-dev/youki/pull/3180
- chore(docs): Fix codecov link in README by @khanhtc1202 in https://github.com/youki-dev/youki/pull/3129
- Fixed grammatical error in README by @CheatCodeSam in https://github.com/youki-dev/youki/pull/3160
- fix: protobuf bug on docs rs by @mdaffad in https://github.com/youki-dev/youki/pull/3159
- bump nix to 0.29.0 by @kemingy in https://github.com/youki-dev/youki/pull/3123
- update rust version to 1.85.0 by @YJDoc2 in https://github.com/youki-dev/youki/pull/3085
- add-test-linux_rootfs_propagation by @saku3 in https://github.com/youki-dev/youki/pull/3024
- Add a relative_network_cgroups test as one of the integration tests by @moz-sec in https://github.com/youki-dev/youki/pull/2986
- Refactor init process by @utam0k in https://github.com/youki-dev/youki/pull/3158
- add kill test by @YamasouA in https://github.com/youki-dev/youki/pull/2996
- allow running selected tests in contest.sh and justfile by @saku3 in https://github.com/youki-dev/youki/pull/3165
- fix: capet Ambient log level by @z63d in https://github.com/youki-dev/youki/pull/3150
- add test process_capabilities_fail by @kazmsk in https://github.com/youki-dev/youki/pull/3010
- fix typos and outdated typos ci action by @howjmay in https://github.com/youki-dev/youki/pull/3168
- add a system call mock for uid/gid. by @nayuta-ai in https://github.com/youki-dev/youki/pull/3173
- fix: remove println statements from contest tests by @YJDoc2 in https://github.com/youki-dev/youki/pull/3167
- Installing kubectl in dev container. by @CheatCodeSam in https://github.com/youki-dev/youki/pull/3177
- Add uid_mappings test by @moz-sec in https://github.com/youki-dev/youki/pull/3161
- fix: update devcontainer.json by @AobaIwaki123 in https://github.com/youki-dev/youki/pull/3172
- Remove oci tests that are duplicates of contest by @utam0k in https://github.com/youki-dev/youki/pull/3042
- Remove oci tests that are duplicates of contest by @saku3 in https://github.com/youki-dev/youki/pull/3184
- Fix debug logging for CPU affinity bitmask by @saku3 in https://github.com/youki-dev/youki/pull/3191
- [DNM] ci: temp disable workflows by @YJDoc2 in https://github.com/youki-dev/youki/pull/3192

### 0.5.5

- fix(3198): fix difference in how commands are passed after exec and ps by @tommady in https://github.com/youki-dev/youki/pull/3201
- Revert "[DNM] ci: temp disable workflows" by @YJDoc2 in https://github.com/youki-dev/youki/pull/3194
- Fixed Minor Spelling Errors by @CheatCodeSam in https://github.com/youki-dev/youki/pull/3205
- chore(justfile):add install recipe by @saku3 in https://github.com/youki-dev/youki/pull/3213

### 0.5.6

- fix(3197): fix youki version command Part of Enhancing Compatibility with runc by @tommady in https://github.com/youki-dev/youki/pull/3200
- Update Vagrantfile to support the ARM architecture by @bells17 in https://github.com/youki-dev/youki/pull/3222
- setup runc integration test by @saku3 in https://github.com/youki-dev/youki/pull/3182
- update runc ci to 1.3.1 by @saku3 in https://github.com/youki-dev/youki/pull/3237
- Add mdbook binary to devcontainer by @bells17 in https://github.com/youki-dev/youki/pull/3240
- Unskip runc tests after CI runc update 1.3.1 by @saku3 in https://github.com/youki-dev/youki/pull/3249
- Fix podman ci by @saku3 in https://github.com/youki-dev/youki/pull/3260
- add misc_props test by @YamasouA in https://github.com/youki-dev/youki/pull/3250
- chore(deps): bump libseccomp from 0.3.0 to 0.4.0 by @MattPatchava in https://github.com/youki-dev/youki/pull/3275

### 0.5.7

- Waiting on systemd to add intermediate process to cgroup. by @CheatCodeSam in https://github.com/youki-dev/youki/pull/3262
- Update/runc 1.3.2 by @n4mlz in https://github.com/youki-dev/youki/pull/3274


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.5.7**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `youki-dev/youki`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/youki.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
