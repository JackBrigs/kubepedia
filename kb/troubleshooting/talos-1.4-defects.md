---
id: TROUBLE-TALOS_1_4_DEFECTS
type: troubleshooting
title: "talos 1.4: defects fixed in the 1.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.4.0 <1.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.4 known issues
  - talos 1.4 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.4 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.4: defects fixed in the 1.4 line

## Summary

**126 defects** the project fixed across **8 releases** of the 1.4 line, from 1.4.0 to
1.4.8. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.4.0

- siderolabs/talos@c2e26e9b6 fix: fix dashboard crash when a non-existent node is specified
- siderolabs/talos@be87b6529 fix: send 'STOP' event on phase end
- siderolabs/talos@1f3c849e2 fix: quote ISO kernel args for GRUB
- siderolabs/talos@3600b648a fix: correctly parse static pod phase
- siderolabs/talos@b11de0c92 fix: improve action tracking post checks
- siderolabs/talos@40c2e750a fix: rework DHCP flow
- siderolabs/talos@ddb014cfd fix: udevd rules trigger
- siderolabs/talos@aa662ff63 fix: apply small fixes on dashboard
- siderolabs/talos@188560a33 fix: add a link-scope route if the cmdline gateway is not reachable
- siderolabs/talos@45c5b47a5 feat: dhcpv4: send current hostname, fix spec compliance of renewals
- siderolabs/talos@289b41fe4 fix: output of `talosctl logs` might be corruped
- siderolabs/talos@d30cf9c86 test: fix misprint in e2e scripts
- siderolabs/talos@0d0bb31cf fix: use stripped kernel modules
- siderolabs/talos@cf2ccc521 fix: always shutdown maintenance API service
- siderolabs/talos@b246c90ab fix: add uint32 to Magic1 and Magic2
- siderolabs/talos@bec89bf6e fix: use 'no block' etcd dial with multiple endpoints
- siderolabs/talos@9933ebb6a chore: fix loaded artifacts file permission
- siderolabs/talos@a14a0aba0 fix: nil pointer exception in syncLink
- siderolabs/talos@cf101e56f fix: add `--force` flag for `talosctl gen`
- siderolabs/talos@ea2aa0611 fix: fix data race on network config read
- siderolabs/talos@6656d35ec docs: fix Talos version to use template
- siderolabs/talos@c8f8579f2 fix: upgrade-k8s to flag should not be required since there is a default
- siderolabs/talos@fda6da692 fix: successful ACPI shutdown in maintenance mode
- siderolabs/talos@e71cc6619 fix: redo assertHostnames in HostnameMergeSuite.TestMerge
- siderolabs/talos@40e69af22 fix: improve etcd leave on reset process
- siderolabs/talos@638dc9128 fix: fix "defer" leak in ResetUserDisks
- siderolabs/talos@426fe9687 fix: extension base folder permission
- siderolabs/talos@f3d3f0f26 fix: update go-smbios library with Hyper-V data fix
- siderolabs/talos@8711eea96 fix: use passed `--context` in `talosctl config` cmd
- siderolabs/talos@36ab414a1 docs: fix the endpoints in the libvirt guide
- siderolabs/talos@3d55bd80f fix: add `--force` flag to `talosctl gen config`
- siderolabs/talos@b5c03a7fa fix: docker talosctl cluster create provisioner
- siderolabs/talos@6e8f13529 fix: add support for a fallback '*' mirror configuration
- siderolabs/talos@dcd4eb1a9 fix: improve error message on single node upgrade
- siderolabs/talos@7b75cd8b9 fix: kernel module dependency tree generation
- siderolabs/talos@65d02e5ad fix: dbus shutdown when it's not initialized
- siderolabs/talos@a7079ce85 fix: quote the ampersand character in GRUB config
- siderolabs/talos@933ba2d82 fix: display correct blockdevice size
- siderolabs/talos@c449cb736 fix: talosctl reboot command passing mode in wait mode
- siderolabs/talos@1e1aa84f6 fix: kubernetes removed resource version check
- siderolabs/talos@dcbcf5a93 fix: wait for network and retry in platform get config funcs
- siderolabs/talos@e09e10666 fix: default dns domain to 'cluster.local' in local case
- siderolabs/talos@0c6c88874 fix: trackable action flag usage text. --no-wait does not exist
- siderolabs/talos@56d945326 fix: panic in talosctl cluster show
- siderolabs/talos@38a51191e fix: correctly expand parameters in the URL
- siderolabs/talos@af21860a2 fix: return proper error if download attempts time out
- siderolabs/talos@54f7d4c92 fix: correctly quote and unquote strings in GRUB config
- siderolabs/talos@54cf0672a fix: omit zero MTU in the machine config
- siderolabs/talos@0ba5e59f6 fix: drone config for renovate PR's
- siderolabs/talos@590a393de fix: udevd healthcheck
- siderolabs/talos@09aa71264 fix: renovate config
- siderolabs/talos@f0804027a fix: renovate config
- siderolabs/talos@aa9f66c1c fix: mark DigitalOcean anchor IP as scope link
- siderolabs/talos@3e0057162 fix: unwrap gRPC errors on stop/remove pods check
- siderolabs/talos@00e52ae07 fix: build correctly etcd initial cluster URL
- siderolabs/talos@18122ae73 fix: service restart (including extension services)
- siderolabs/talos@680fd5e45 fix: bump COSI runtime with the panic controller restart fix
- siderolabs/talos@0b65bbfc8 fix: handle overwriting tags in syslinux ADV
- siderolabs/talos@70d9428a1 fix: kubespan MSS clamping
- siderolabs/talos@062c7d754 test: fix integration test on cp endpoint update
- siderolabs/talos@29020cb9c fix: report fatal sequence errors as reboots
- siderolabs/talos@c6cb36cc1 docs: fix auditpolicy example typo
- siderolabs/talos@fcb19ff51 fix: implement upgrade version checks for Talos 1.4
- siderolabs/talos@f6a86ae90 fix: oralce cloud zone
- siderolabs/talos@a0c0352dd fix: send diagnostic output to stderr consistently
- siderolabs/talos@9a5f4c08a fix: default the manifest namespace if not set
- siderolabs/talos@703624c43 docs: fix the 1.3 release date
- siderolabs/talos@ff83d9fd7 fix: improve talosctl completion
- siderolabs/talos@a9643b477 fix: use proper key usage for apid client certificate
- siderolabs/talos@171aa9467 fix: disable Wireless Lan using dtoverlay
- siderolabs/talos@873bd3807 fix: redact service account key in config in RedactSecrets method
- siderolabs/talos@5b992bd86 fix: allow empty dnsDomain in machine config
- siderolabs/talos@d04970dfa fix: ignore k8s additional addresses if nil
- siderolabs/talos@1253513bd fix: fix nil pointer panic and incorrect error output
- siderolabs/talos@82e8c9e1f fix: workaround panic in the kubelet service controller
- siderolabs/talos@a505b8909 fix: update COSI and reset restart backoff on success
- siderolabs/talos@fcffc8879 fix: add ext4 filesystem detection
- siderolabs/talos@5b2960eff fix: introduce 'overridePath' setting and fix Talos resolver
- siderolabs/talos@0219d1124 fix: use only kube-apiserver endpoints for Talos API access endpoints
- siderolabs/talos@dc5e0f4af fix: report errors to Equinix Metal event API
- siderolabs/talos@d3cf06114 fix: ignore many more filesystems in IMA
- siderolabs/talos@4cd125d49 fix: correctly handle new watch event types
- siderolabs/go-blockdevice@8c7ea19 fix: blockdevice size is reported by Linux in 512 blocks always
- siderolabs/go-kmsg@7a51094 fix: exit properly on context cancel
- siderolabs/go-smbios@c526764 feat: fix reading "broken" Hyper-V DMI data
- siderolabs/pkgs@b447e04 fix: remove FB_NVIDIA drivers, Linux 6.1.23
- siderolabs/pkgs@5d77814 fix: strip kernel modules when installing
- siderolabs/pkgs@7493721 fix: sourcefourge url shasums
- siderolabs/pkgs@15fe6d8 fix: kernel module tree files missing
- siderolabs/pkgs@ccb9d39 fix: disable magic sysrq
- siderolabs/pkgs@165dff6 fix: patch ipmitool IANA URL
- siderolabs/tools@a8440a9 fix: partially revert e6c98fdf54425e6382f226e33bccca6f3875aad3a
- siderolabs/tools@cd9687b fix: renovate config
- siderolabs/tools@37612fe fix: revert enabling provenance

### 1.4.1

- siderolabs/talos@726d8d984 feat: update Linux to 6.1.25, fix virtio on arm64
- siderolabs/talos@ab09baf3d fix: bump max inhibit delay to 20 min
- siderolabs/talos@e94a19602 fix: udevd rules trigger
- siderolabs/talos@0cd177524 fix: display correct number of machines on dashboard
- siderolabs/talos@254086d6d fix: support kernel userspace module loading
- siderolabs/talos@9ce238794 fix: do not show control plane status for workers on dashboard
- siderolabs/talos@b92d9965f fix: allow `talosctl cp` to handle special files in `/proc`
- siderolabs/talos@c003fce72 chore: fix container image reproducibility
- siderolabs/talos@0a00a4ea7 fix: parse errors correctly

### 1.4.2

- siderolabs/talos@2652fce90 fix: properly skip/cleanup controlplane configs for workers
- siderolabs/talos@3da5aa945 fix: don't reload control plane pods on cert SANs changes
- siderolabs/talos@447838243 fix: enforce nolock option for all NFS mounts by default
- siderolabs/talos@e2979fb4d fix: inhibit timer to follow kubelet timer
- siderolabs/talos@476dccfb0 fix: set timeout for unmount calls
- siderolabs/talos@ebca8496a fix: set the static pod priority as values
- siderolabs/talos@05f65f1d8 fix: add back required TARGETARCH for installer

### 1.4.3

- siderolabs/talos@1ad8b7448 fix: set rlimit explicitly in wrapperd

### 1.4.4

- siderolabs/talos@c2220996d fix: rlimit nofile test
- siderolabs/talos@779febfb9 fix: revert: set rlimit explicitly in wrapperd

### 1.4.5

- siderolabs/talos@cdc9ad889 fix: fail quickly if upgrade-k8s is used with multiple nodes
- siderolabs/talos@b5b39f99b fix: fall back to external IP when discovering nodes in upgrade-k8s
- siderolabs/talos@a89c9d201 fix: race with `udevd` and `mountUserDisks`
- siderolabs/talos@d249b14d0 fix: refresh kubelet self-issued serving certificates
- siderolabs/talos@4393b624d fix: correct upgrade Talos version check
- siderolabs/go-kubernetes@5a3df5b fix: remove removed APIs for 1.27 upgrade

### 1.4.6

- siderolabs/talos@bb76a38d4 fix: provide stashed META values before installation
- siderolabs/talos@109a6c659 fix: allow time skew for generated kubeconfig
- siderolabs/talos@8c9f0495f fix: do not probe kernel args in dashboard if not needed
- siderolabs/talos@d759302d9 fix: skip DHCP RENEW if server IP in the lease is all zeroes
- siderolabs/talos@2b33a66d7 fix: upgrade-k8s use internal IP first, external IP fallback
- siderolabs/pkgs@15a5cba fix: bump drbd to 9.2.4

### 1.4.8

- siderolabs/talos@85b5d1ddd fix: calculate log2i properly


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.4.8**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `siderolabs/talos`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/talos.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
