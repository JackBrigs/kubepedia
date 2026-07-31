---
id: TROUBLE-TALOS_0_10_DEFECTS
type: troubleshooting
title: "talos 0.10: defects fixed in the 0.10 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.10.0 <0.11.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 0.10 known issues
  - talos 0.10 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 0.10 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 0.10: defects fixed in the 0.10 line

## Summary

**283 defects** the project fixed across **5 releases** of the 0.10 line, from 0.10.0 to
0.10.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.10.0

- u-boot version was updated to fix the boot and USB issues on Raspberry Pi 4 8GiB version
- [`280b5940c`](https://github.com/talos-systems/talos/commit/280b5940cfa58bee696d7888de65b0a181390413) fix: update osType in OVA other3xLinux64Guest"
- [`b338628dc`](https://github.com/talos-systems/talos/commit/b338628dc8547b0fd392a841c83f48e3b32f6333) fix: check if OVF env is empty
- [`564b45ba2`](https://github.com/talos-systems/talos/commit/564b45ba200531ac9dacdccd984b22eb39acdedf) fix: update etcd client errors, print etcd join failures
- [`f0970ea7f`](https://github.com/talos-systems/talos/commit/f0970ea7ffe0dbca62caef2e343b91443a6ddfcb) fix: zero out manifest contents before setting new value
- [`3dc7b8a8a`](https://github.com/talos-systems/talos/commit/3dc7b8a8a2ec669e6aa4e7d9b74761ab281ee29e) chore: fix import path mismerge
- [`e26c977d8`](https://github.com/talos-systems/talos/commit/e26c977d85028dd58b6b7482a7dd37237982f0ea) fix: check retryable network errors by interface
- [`30f687b41`](https://github.com/talos-systems/talos/commit/30f687b417eeee2b789cfb064ed9cb4ab5a301e0) fix: document HDMI problem on RPi 4
- [`28753f6dc`](https://github.com/talos-systems/talos/commit/28753f6dcb85450965e4d4a0fb68f448e1deee23) fix: trim endpoints/nodes from arguments in talosctl config
- [`aca63b882`](https://github.com/talos-systems/talos/commit/aca63b8829ad0eebd449573120bff2d9b90ba828) docs: fix "DigitalOcean" spelling
- [`33035901f`](https://github.com/talos-systems/talos/commit/33035901ff7875bdf9eb99fb86b377318f60d74b) fix: revert mark PMBR EFI partition as bootable
- [`690eb20e9`](https://github.com/talos-systems/talos/commit/690eb20e9763d8f3036f0a1b4b9447f19c5ec05b) chore: update blockdevice library for PMBR bootable fix
- [`a8761b8e1`](https://github.com/talos-systems/talos/commit/a8761b8e1efd07a3bda3d8f706d3d7bf658955bb) fix: require leader on etcd member operations
- [`3dc84625c`](https://github.com/talos-systems/talos/commit/3dc84625cb1b323bad1dd93d89a13d3d59ea22d8) fix: make both HDMI ports work on RPi 4
- [`bd5ae1e0b`](https://github.com/talos-systems/talos/commit/bd5ae1e0b5dd303a017156ba7af733f79d3c13ef) fix: add a check for overlay mounts in installer pre-flight checks
- [`e16d6d346`](https://github.com/talos-systems/talos/commit/e16d6d3468a7a072b41e94fdc352df15b8321376) fix: publish rockpi4 image to release artifacts
- [`61b694b94`](https://github.com/talos-systems/talos/commit/61b694b94896da47e2ddf677cbf12b18007268a5) fix: create rootfs for system services via /system tmpfs
- [`a1e641540`](https://github.com/talos-systems/talos/commit/a1e6415403df9827fb486492a4b292b9aab3076b) fix: retry Kubernetes API errors on cordon/uncordon/etc
- [`063d1abe9`](https://github.com/talos-systems/talos/commit/063d1abe9cf1634f3517893977fc907dd9004c55) fix: print task failure error immediately
- [`e039172ed`](https://github.com/talos-systems/talos/commit/e039172edac115afbd5bf36a1f266e5967ca5398) fix: ignore EOF errors from Kubernetes API when converting control plane
- [`7bcb91a43`](https://github.com/talos-systems/talos/commit/7bcb91a433f14a29a0d2bbe9d70eb5a997eb9ab0) docs: fix typo for stage flag
- [`7d9125847`](https://github.com/talos-systems/talos/commit/7d9125847506dfadc7e137a30bf0c93ab9ca0b50) test: fix data race in apply config tests
- [`204caf8eb`](https://github.com/talos-systems/talos/commit/204caf8eb9c6c43a90c20ebaea8387584201e7f5) test: fix apply-config integration test, bump clusterctl version
- [`d812099df`](https://github.com/talos-systems/talos/commit/d812099df3d060ae74cd3d28405ddacbdd72ab15) fix: address several issues in TUI installer
- [`269c9ad09`](https://github.com/talos-systems/talos/commit/269c9ad0988f0f966a4e31a5ab744fed7d585385) fix: don't write to config object on access
- [`a0dcfc3d5`](https://github.com/talos-systems/talos/commit/a0dcfc3d5288e633db80bf3e32d31e41756cc90f) fix: workaround race in containerd runner with stdin pipe
- [`032851844`](https://github.com/talos-systems/talos/commit/032851844fdea4b1bde7507720025c981ee3b12c) fix: get rid of data race in encoder and fix concurrent map access
- [`4b3580aa5`](https://github.com/talos-systems/talos/commit/4b3580aa57d83358434238ad953793070cfc67a7) fix: prevent panic in validate config if `machine.install` is missing
- [`9f7d67ac7`](https://github.com/talos-systems/talos/commit/9f7d67ac717834ed428b8f13d4061db5f33c81f9) chore: fix typo
- [`672c97073`](https://github.com/talos-systems/talos/commit/672c970739971dd0c558ad0319fe9fdbd66a741b) fix: allow `convert-k8s --remove-initialized-keys` with K8s cp is down
- [`1f5a0c406`](https://github.com/talos-systems/talos/commit/1f5a0c4065e1fbd63ebe6d48c13e669bfb1dbeac) fix: resolve the issue with Kubernetes upgrade
- [`65701aa72`](https://github.com/talos-systems/talos/commit/65701aa724130645fcabe521557225ff41b359b0) fix: resolve the issue with DHCP lease not being renewed
- [`711f5b23b`](https://github.com/talos-systems/talos/commit/711f5b23be69665d6204dbb80064e0ab0d1468c0) fix: config validation: CNI should apply to cp nodes, encryption config
- [`5ff491d96`](https://github.com/talos-systems/talos/commit/5ff491d9686434a6208583dca97171bfbecf3f70) fix: allow empty list for CNI URLs
- [`ce795f1ce`](https://github.com/talos-systems/talos/commit/ce795f1cea9d78c26edbcd4a40bb5d3637fde629) fix: command `etcd remove-member` shouldn't remove etcd data directory
- [`aab49a167`](https://github.com/talos-systems/talos/commit/aab49a167b1f1cd3974e3aa1244d636ba712f678) fix: repair zsh completion
- [`fc9c416a3`](https://github.com/talos-systems/talos/commit/fc9c416a3c8425bb42892f740c910894610acd00) fix: build rockpi4 metal image as part of CI build
- [`125b86f4e`](https://github.com/talos-systems/talos/commit/125b86f4efbc2ed3e0a4bdfc945e97b05f1cb82c) fix: upgrade-k8s bug with empty config values and provision script
- [`5b14d6f2b`](https://github.com/talos-systems/talos/commit/5b14d6f2b89c5b86f9ec2cb0271c6605272269d4) chore: fix `make help` output
- [`7662d033b`](https://github.com/talos-systems/talos/commit/7662d033bfc3d6e3878e2c2a2a1ec4d71dc2502e) fix: talosctl health should not check kube-proxy when it is disabled
- [`e31790f6f`](https://github.com/talos-systems/talos/commit/e31790f6f548095fe3f1b9a5c88b47e70c197d2c) fix: properly format spec comments in the resources
- [`3c5bfbb47`](https://github.com/talos-systems/talos/commit/3c5bfbb4736c86f493a665dbfe63a6e2d20acb3d) fix: don't touch any partitions on upgrade with --preserve
- [`2e22f20bd`](https://github.com/talos-systems/talos/commit/2e22f20bd876e4972bfdebd44fee13356b70b83f) docs: minor fixes to getting started
- [`ca8a5596c`](https://github.com/talos-systems/talos/commit/ca8a5596c79f638e52601e850236b715f906e3d2) chore: fix provision tests after changes to build-container
- [`8e57fc4f5`](https://github.com/talos-systems/talos/commit/8e57fc4f526096878213048658bae50cfac4cda8) fix: move containerd CRI config files under `/var/`
- [`6f7df3da1`](https://github.com/talos-systems/talos/commit/6f7df3da1e147212e6d4b40a5de65e5ca8be84db) fix: update output of `convert-k8s` command
- [`7c529e1cb`](https://github.com/talos-systems/talos/commit/7c529e1cbd2be66d71e8496304781dd406495bdd) docs: fix links in the documentation
- [`1d830a2`](https://github.com/talos-systems/go-blockdevice/commit/1d830a25f64f6fb96a1bedd800c0b40b107dc833) fix: revert mark the EFI partition in PMBR as bootable
- [`bec914f`](https://github.com/talos-systems/go-blockdevice/commit/bec914ffdda42abcfe642bc2cdfc9fcda56a74ee) fix: mark the EFI partition in PMBR as bootable
- [`dbae83e`](https://github.com/talos-systems/pkgs/commit/dbae83e704da264066ceeca20e0fe66883b542ba) fix: do not use git-lfs for rockpi4 binaries

### 0.10.1

- u-boot version was updated to fix the boot and USB issues on Raspberry Pi 4 8GiB version
- [`194baa3d6`](https://github.com/talos-systems/talos/commit/194baa3d6b1d653edbac743bd03b88fd9f02ca05) fix: properly parse matcher expressions
- [`c613d3e22`](https://github.com/talos-systems/talos/commit/c613d3e2274b866871ff8df8b98a1831203f8202) fix: bump crypto library for the CSR verification fix
- [`801808c54`](https://github.com/talos-systems/talos/commit/801808c545209939df34da5c2d1f997f2a5b500f) fix: use both self-signed and Kubernetes CA to verify Kubelet cert
- [`280b5940c`](https://github.com/talos-systems/talos/commit/280b5940cfa58bee696d7888de65b0a181390413) fix: update osType in OVA other3xLinux64Guest"
- [`b338628dc`](https://github.com/talos-systems/talos/commit/b338628dc8547b0fd392a841c83f48e3b32f6333) fix: check if OVF env is empty
- [`564b45ba2`](https://github.com/talos-systems/talos/commit/564b45ba200531ac9dacdccd984b22eb39acdedf) fix: update etcd client errors, print etcd join failures
- [`f0970ea7f`](https://github.com/talos-systems/talos/commit/f0970ea7ffe0dbca62caef2e343b91443a6ddfcb) fix: zero out manifest contents before setting new value
- [`3dc7b8a8a`](https://github.com/talos-systems/talos/commit/3dc7b8a8a2ec669e6aa4e7d9b74761ab281ee29e) chore: fix import path mismerge
- [`e26c977d8`](https://github.com/talos-systems/talos/commit/e26c977d85028dd58b6b7482a7dd37237982f0ea) fix: check retryable network errors by interface
- [`30f687b41`](https://github.com/talos-systems/talos/commit/30f687b417eeee2b789cfb064ed9cb4ab5a301e0) fix: document HDMI problem on RPi 4
- [`28753f6dc`](https://github.com/talos-systems/talos/commit/28753f6dcb85450965e4d4a0fb68f448e1deee23) fix: trim endpoints/nodes from arguments in talosctl config
- [`aca63b882`](https://github.com/talos-systems/talos/commit/aca63b8829ad0eebd449573120bff2d9b90ba828) docs: fix "DigitalOcean" spelling
- [`33035901f`](https://github.com/talos-systems/talos/commit/33035901ff7875bdf9eb99fb86b377318f60d74b) fix: revert mark PMBR EFI partition as bootable
- [`690eb20e9`](https://github.com/talos-systems/talos/commit/690eb20e9763d8f3036f0a1b4b9447f19c5ec05b) chore: update blockdevice library for PMBR bootable fix
- [`a8761b8e1`](https://github.com/talos-systems/talos/commit/a8761b8e1efd07a3bda3d8f706d3d7bf658955bb) fix: require leader on etcd member operations
- [`3dc84625c`](https://github.com/talos-systems/talos/commit/3dc84625cb1b323bad1dd93d89a13d3d59ea22d8) fix: make both HDMI ports work on RPi 4
- [`bd5ae1e0b`](https://github.com/talos-systems/talos/commit/bd5ae1e0b5dd303a017156ba7af733f79d3c13ef) fix: add a check for overlay mounts in installer pre-flight checks
- [`e16d6d346`](https://github.com/talos-systems/talos/commit/e16d6d3468a7a072b41e94fdc352df15b8321376) fix: publish rockpi4 image to release artifacts
- [`61b694b94`](https://github.com/talos-systems/talos/commit/61b694b94896da47e2ddf677cbf12b18007268a5) fix: create rootfs for system services via /system tmpfs
- [`a1e641540`](https://github.com/talos-systems/talos/commit/a1e6415403df9827fb486492a4b292b9aab3076b) fix: retry Kubernetes API errors on cordon/uncordon/etc
- [`063d1abe9`](https://github.com/talos-systems/talos/commit/063d1abe9cf1634f3517893977fc907dd9004c55) fix: print task failure error immediately
- [`e039172ed`](https://github.com/talos-systems/talos/commit/e039172edac115afbd5bf36a1f266e5967ca5398) fix: ignore EOF errors from Kubernetes API when converting control plane
- [`7bcb91a43`](https://github.com/talos-systems/talos/commit/7bcb91a433f14a29a0d2bbe9d70eb5a997eb9ab0) docs: fix typo for stage flag
- [`7d9125847`](https://github.com/talos-systems/talos/commit/7d9125847506dfadc7e137a30bf0c93ab9ca0b50) test: fix data race in apply config tests
- [`204caf8eb`](https://github.com/talos-systems/talos/commit/204caf8eb9c6c43a90c20ebaea8387584201e7f5) test: fix apply-config integration test, bump clusterctl version
- [`d812099df`](https://github.com/talos-systems/talos/commit/d812099df3d060ae74cd3d28405ddacbdd72ab15) fix: address several issues in TUI installer
- [`269c9ad09`](https://github.com/talos-systems/talos/commit/269c9ad0988f0f966a4e31a5ab744fed7d585385) fix: don't write to config object on access
- [`a0dcfc3d5`](https://github.com/talos-systems/talos/commit/a0dcfc3d5288e633db80bf3e32d31e41756cc90f) fix: workaround race in containerd runner with stdin pipe
- [`032851844`](https://github.com/talos-systems/talos/commit/032851844fdea4b1bde7507720025c981ee3b12c) fix: get rid of data race in encoder and fix concurrent map access
- [`4b3580aa5`](https://github.com/talos-systems/talos/commit/4b3580aa57d83358434238ad953793070cfc67a7) fix: prevent panic in validate config if `machine.install` is missing
- [`9f7d67ac7`](https://github.com/talos-systems/talos/commit/9f7d67ac717834ed428b8f13d4061db5f33c81f9) chore: fix typo
- [`672c97073`](https://github.com/talos-systems/talos/commit/672c970739971dd0c558ad0319fe9fdbd66a741b) fix: allow `convert-k8s --remove-initialized-keys` with K8s cp is down
- [`1f5a0c406`](https://github.com/talos-systems/talos/commit/1f5a0c4065e1fbd63ebe6d48c13e669bfb1dbeac) fix: resolve the issue with Kubernetes upgrade
- [`65701aa72`](https://github.com/talos-systems/talos/commit/65701aa724130645fcabe521557225ff41b359b0) fix: resolve the issue with DHCP lease not being renewed
- [`711f5b23b`](https://github.com/talos-systems/talos/commit/711f5b23be69665d6204dbb80064e0ab0d1468c0) fix: config validation: CNI should apply to cp nodes, encryption config
- [`5ff491d96`](https://github.com/talos-systems/talos/commit/5ff491d9686434a6208583dca97171bfbecf3f70) fix: allow empty list for CNI URLs
- [`ce795f1ce`](https://github.com/talos-systems/talos/commit/ce795f1cea9d78c26edbcd4a40bb5d3637fde629) fix: command `etcd remove-member` shouldn't remove etcd data directory
- [`aab49a167`](https://github.com/talos-systems/talos/commit/aab49a167b1f1cd3974e3aa1244d636ba712f678) fix: repair zsh completion
- [`fc9c416a3`](https://github.com/talos-systems/talos/commit/fc9c416a3c8425bb42892f740c910894610acd00) fix: build rockpi4 metal image as part of CI build
- [`125b86f4e`](https://github.com/talos-systems/talos/commit/125b86f4efbc2ed3e0a4bdfc945e97b05f1cb82c) fix: upgrade-k8s bug with empty config values and provision script
- [`5b14d6f2b`](https://github.com/talos-systems/talos/commit/5b14d6f2b89c5b86f9ec2cb0271c6605272269d4) chore: fix `make help` output
- [`7662d033b`](https://github.com/talos-systems/talos/commit/7662d033bfc3d6e3878e2c2a2a1ec4d71dc2502e) fix: talosctl health should not check kube-proxy when it is disabled
- [`e31790f6f`](https://github.com/talos-systems/talos/commit/e31790f6f548095fe3f1b9a5c88b47e70c197d2c) fix: properly format spec comments in the resources
- [`3c5bfbb47`](https://github.com/talos-systems/talos/commit/3c5bfbb4736c86f493a665dbfe63a6e2d20acb3d) fix: don't touch any partitions on upgrade with --preserve
- [`2e22f20bd`](https://github.com/talos-systems/talos/commit/2e22f20bd876e4972bfdebd44fee13356b70b83f) docs: minor fixes to getting started
- [`ca8a5596c`](https://github.com/talos-systems/talos/commit/ca8a5596c79f638e52601e850236b715f906e3d2) chore: fix provision tests after changes to build-container
- [`8e57fc4f5`](https://github.com/talos-systems/talos/commit/8e57fc4f526096878213048658bae50cfac4cda8) fix: move containerd CRI config files under `/var/`
- [`6f7df3da1`](https://github.com/talos-systems/talos/commit/6f7df3da1e147212e6d4b40a5de65e5ca8be84db) fix: update output of `convert-k8s` command
- [`7c529e1cb`](https://github.com/talos-systems/talos/commit/7c529e1cbd2be66d71e8496304781dd406495bdd) docs: fix links in the documentation
- [`4f80b97`](https://github.com/talos-systems/crypto/commit/4f80b976b640d773fb025d981bf85bcc8190815b) fix: verify CSR signature before issuing a certificate
- [`1d830a2`](https://github.com/talos-systems/go-blockdevice/commit/1d830a25f64f6fb96a1bedd800c0b40b107dc833) fix: revert mark the EFI partition in PMBR as bootable
- [`bec914f`](https://github.com/talos-systems/go-blockdevice/commit/bec914ffdda42abcfe642bc2cdfc9fcda56a74ee) fix: mark the EFI partition in PMBR as bootable
- [`dbae83e`](https://github.com/talos-systems/pkgs/commit/dbae83e704da264066ceeca20e0fe66883b542ba) fix: do not use git-lfs for rockpi4 binaries

### 0.10.2

- u-boot version was updated to fix the boot and USB issues on Raspberry Pi 4 8GiB version
- [`747903a10`](https://github.com/talos-systems/talos/commit/747903a100d3c17360a6fe43c02ab9750d67cf22) fix: stop networkd before leaving etcd on 'reset' path
- [`6fd98d95b`](https://github.com/talos-systems/talos/commit/6fd98d95b9a2e9df7a618b609d0f056f7e775f26) fix: update the way NTP sync uses `adjtimex` syscall
- [`f1298f6e3`](https://github.com/talos-systems/talos/commit/f1298f6e3ca017490eac4485c864ff9d7a55e208) fix: avoid data race on CRI pod stop
- [`194baa3d6`](https://github.com/talos-systems/talos/commit/194baa3d6b1d653edbac743bd03b88fd9f02ca05) fix: properly parse matcher expressions
- [`c613d3e22`](https://github.com/talos-systems/talos/commit/c613d3e2274b866871ff8df8b98a1831203f8202) fix: bump crypto library for the CSR verification fix
- [`801808c54`](https://github.com/talos-systems/talos/commit/801808c545209939df34da5c2d1f997f2a5b500f) fix: use both self-signed and Kubernetes CA to verify Kubelet cert
- [`280b5940c`](https://github.com/talos-systems/talos/commit/280b5940cfa58bee696d7888de65b0a181390413) fix: update osType in OVA other3xLinux64Guest"
- [`b338628dc`](https://github.com/talos-systems/talos/commit/b338628dc8547b0fd392a841c83f48e3b32f6333) fix: check if OVF env is empty
- [`564b45ba2`](https://github.com/talos-systems/talos/commit/564b45ba200531ac9dacdccd984b22eb39acdedf) fix: update etcd client errors, print etcd join failures
- [`f0970ea7f`](https://github.com/talos-systems/talos/commit/f0970ea7ffe0dbca62caef2e343b91443a6ddfcb) fix: zero out manifest contents before setting new value
- [`3dc7b8a8a`](https://github.com/talos-systems/talos/commit/3dc7b8a8a2ec669e6aa4e7d9b74761ab281ee29e) chore: fix import path mismerge
- [`e26c977d8`](https://github.com/talos-systems/talos/commit/e26c977d85028dd58b6b7482a7dd37237982f0ea) fix: check retryable network errors by interface
- [`30f687b41`](https://github.com/talos-systems/talos/commit/30f687b417eeee2b789cfb064ed9cb4ab5a301e0) fix: document HDMI problem on RPi 4
- [`28753f6dc`](https://github.com/talos-systems/talos/commit/28753f6dcb85450965e4d4a0fb68f448e1deee23) fix: trim endpoints/nodes from arguments in talosctl config
- [`aca63b882`](https://github.com/talos-systems/talos/commit/aca63b8829ad0eebd449573120bff2d9b90ba828) docs: fix "DigitalOcean" spelling
- [`33035901f`](https://github.com/talos-systems/talos/commit/33035901ff7875bdf9eb99fb86b377318f60d74b) fix: revert mark PMBR EFI partition as bootable
- [`690eb20e9`](https://github.com/talos-systems/talos/commit/690eb20e9763d8f3036f0a1b4b9447f19c5ec05b) chore: update blockdevice library for PMBR bootable fix
- [`a8761b8e1`](https://github.com/talos-systems/talos/commit/a8761b8e1efd07a3bda3d8f706d3d7bf658955bb) fix: require leader on etcd member operations
- [`3dc84625c`](https://github.com/talos-systems/talos/commit/3dc84625cb1b323bad1dd93d89a13d3d59ea22d8) fix: make both HDMI ports work on RPi 4
- [`bd5ae1e0b`](https://github.com/talos-systems/talos/commit/bd5ae1e0b5dd303a017156ba7af733f79d3c13ef) fix: add a check for overlay mounts in installer pre-flight checks
- [`e16d6d346`](https://github.com/talos-systems/talos/commit/e16d6d3468a7a072b41e94fdc352df15b8321376) fix: publish rockpi4 image to release artifacts
- [`61b694b94`](https://github.com/talos-systems/talos/commit/61b694b94896da47e2ddf677cbf12b18007268a5) fix: create rootfs for system services via /system tmpfs
- [`a1e641540`](https://github.com/talos-systems/talos/commit/a1e6415403df9827fb486492a4b292b9aab3076b) fix: retry Kubernetes API errors on cordon/uncordon/etc
- [`063d1abe9`](https://github.com/talos-systems/talos/commit/063d1abe9cf1634f3517893977fc907dd9004c55) fix: print task failure error immediately
- [`e039172ed`](https://github.com/talos-systems/talos/commit/e039172edac115afbd5bf36a1f266e5967ca5398) fix: ignore EOF errors from Kubernetes API when converting control plane
- [`7bcb91a43`](https://github.com/talos-systems/talos/commit/7bcb91a433f14a29a0d2bbe9d70eb5a997eb9ab0) docs: fix typo for stage flag
- [`7d9125847`](https://github.com/talos-systems/talos/commit/7d9125847506dfadc7e137a30bf0c93ab9ca0b50) test: fix data race in apply config tests
- [`204caf8eb`](https://github.com/talos-systems/talos/commit/204caf8eb9c6c43a90c20ebaea8387584201e7f5) test: fix apply-config integration test, bump clusterctl version
- [`d812099df`](https://github.com/talos-systems/talos/commit/d812099df3d060ae74cd3d28405ddacbdd72ab15) fix: address several issues in TUI installer
- [`269c9ad09`](https://github.com/talos-systems/talos/commit/269c9ad0988f0f966a4e31a5ab744fed7d585385) fix: don't write to config object on access
- [`a0dcfc3d5`](https://github.com/talos-systems/talos/commit/a0dcfc3d5288e633db80bf3e32d31e41756cc90f) fix: workaround race in containerd runner with stdin pipe
- [`032851844`](https://github.com/talos-systems/talos/commit/032851844fdea4b1bde7507720025c981ee3b12c) fix: get rid of data race in encoder and fix concurrent map access
- [`4b3580aa5`](https://github.com/talos-systems/talos/commit/4b3580aa57d83358434238ad953793070cfc67a7) fix: prevent panic in validate config if `machine.install` is missing
- [`9f7d67ac7`](https://github.com/talos-systems/talos/commit/9f7d67ac717834ed428b8f13d4061db5f33c81f9) chore: fix typo
- [`672c97073`](https://github.com/talos-systems/talos/commit/672c970739971dd0c558ad0319fe9fdbd66a741b) fix: allow `convert-k8s --remove-initialized-keys` with K8s cp is down
- [`1f5a0c406`](https://github.com/talos-systems/talos/commit/1f5a0c4065e1fbd63ebe6d48c13e669bfb1dbeac) fix: resolve the issue with Kubernetes upgrade
- [`65701aa72`](https://github.com/talos-systems/talos/commit/65701aa724130645fcabe521557225ff41b359b0) fix: resolve the issue with DHCP lease not being renewed
- [`711f5b23b`](https://github.com/talos-systems/talos/commit/711f5b23be69665d6204dbb80064e0ab0d1468c0) fix: config validation: CNI should apply to cp nodes, encryption config
- [`5ff491d96`](https://github.com/talos-systems/talos/commit/5ff491d9686434a6208583dca97171bfbecf3f70) fix: allow empty list for CNI URLs
- [`ce795f1ce`](https://github.com/talos-systems/talos/commit/ce795f1cea9d78c26edbcd4a40bb5d3637fde629) fix: command `etcd remove-member` shouldn't remove etcd data directory
- [`aab49a167`](https://github.com/talos-systems/talos/commit/aab49a167b1f1cd3974e3aa1244d636ba712f678) fix: repair zsh completion
- [`fc9c416a3`](https://github.com/talos-systems/talos/commit/fc9c416a3c8425bb42892f740c910894610acd00) fix: build rockpi4 metal image as part of CI build
- [`125b86f4e`](https://github.com/talos-systems/talos/commit/125b86f4efbc2ed3e0a4bdfc945e97b05f1cb82c) fix: upgrade-k8s bug with empty config values and provision script
- [`5b14d6f2b`](https://github.com/talos-systems/talos/commit/5b14d6f2b89c5b86f9ec2cb0271c6605272269d4) chore: fix `make help` output
- [`7662d033b`](https://github.com/talos-systems/talos/commit/7662d033bfc3d6e3878e2c2a2a1ec4d71dc2502e) fix: talosctl health should not check kube-proxy when it is disabled
- [`e31790f6f`](https://github.com/talos-systems/talos/commit/e31790f6f548095fe3f1b9a5c88b47e70c197d2c) fix: properly format spec comments in the resources
- [`3c5bfbb47`](https://github.com/talos-systems/talos/commit/3c5bfbb4736c86f493a665dbfe63a6e2d20acb3d) fix: don't touch any partitions on upgrade with --preserve
- [`2e22f20bd`](https://github.com/talos-systems/talos/commit/2e22f20bd876e4972bfdebd44fee13356b70b83f) docs: minor fixes to getting started
- [`ca8a5596c`](https://github.com/talos-systems/talos/commit/ca8a5596c79f638e52601e850236b715f906e3d2) chore: fix provision tests after changes to build-container
- [`8e57fc4f5`](https://github.com/talos-systems/talos/commit/8e57fc4f526096878213048658bae50cfac4cda8) fix: move containerd CRI config files under `/var/`
- [`6f7df3da1`](https://github.com/talos-systems/talos/commit/6f7df3da1e147212e6d4b40a5de65e5ca8be84db) fix: update output of `convert-k8s` command
- [`7c529e1cb`](https://github.com/talos-systems/talos/commit/7c529e1cbd2be66d71e8496304781dd406495bdd) docs: fix links in the documentation
- [`4f80b97`](https://github.com/talos-systems/crypto/commit/4f80b976b640d773fb025d981bf85bcc8190815b) fix: verify CSR signature before issuing a certificate
- [`1d830a2`](https://github.com/talos-systems/go-blockdevice/commit/1d830a25f64f6fb96a1bedd800c0b40b107dc833) fix: revert mark the EFI partition in PMBR as bootable
- [`bec914f`](https://github.com/talos-systems/go-blockdevice/commit/bec914ffdda42abcfe642bc2cdfc9fcda56a74ee) fix: mark the EFI partition in PMBR as bootable
- [`d3a32be`](https://github.com/talos-systems/go-smbios/commit/d3a32bea731a0c2a60ce7f5eae60253300ef27e1) fix: return UUID in middle endian only on SMBIOS >= 2.6
- [`dbae83e`](https://github.com/talos-systems/pkgs/commit/dbae83e704da264066ceeca20e0fe66883b542ba) fix: do not use git-lfs for rockpi4 binaries

### 0.10.3

- u-boot version was updated to fix the boot and USB issues on Raspberry Pi 4 8GiB version
- [`70ee15b79`](https://github.com/talos-systems/talos/commit/70ee15b793fbf4a58914a5ad9b619ce4f5906c12) fix: stop networkd and pods before leaving etcd on upgrade
- [`1e9496b80`](https://github.com/talos-systems/talos/commit/1e9496b80b7e96045333a03ea1614b5929edbf71) fix: properly populate AllowSchedulingOnMasters option in gen config RPC
- [`747903a10`](https://github.com/talos-systems/talos/commit/747903a100d3c17360a6fe43c02ab9750d67cf22) fix: stop networkd before leaving etcd on 'reset' path
- [`6fd98d95b`](https://github.com/talos-systems/talos/commit/6fd98d95b9a2e9df7a618b609d0f056f7e775f26) fix: update the way NTP sync uses `adjtimex` syscall
- [`f1298f6e3`](https://github.com/talos-systems/talos/commit/f1298f6e3ca017490eac4485c864ff9d7a55e208) fix: avoid data race on CRI pod stop
- [`194baa3d6`](https://github.com/talos-systems/talos/commit/194baa3d6b1d653edbac743bd03b88fd9f02ca05) fix: properly parse matcher expressions
- [`c613d3e22`](https://github.com/talos-systems/talos/commit/c613d3e2274b866871ff8df8b98a1831203f8202) fix: bump crypto library for the CSR verification fix
- [`801808c54`](https://github.com/talos-systems/talos/commit/801808c545209939df34da5c2d1f997f2a5b500f) fix: use both self-signed and Kubernetes CA to verify Kubelet cert
- [`280b5940c`](https://github.com/talos-systems/talos/commit/280b5940cfa58bee696d7888de65b0a181390413) fix: update osType in OVA other3xLinux64Guest"
- [`b338628dc`](https://github.com/talos-systems/talos/commit/b338628dc8547b0fd392a841c83f48e3b32f6333) fix: check if OVF env is empty
- [`564b45ba2`](https://github.com/talos-systems/talos/commit/564b45ba200531ac9dacdccd984b22eb39acdedf) fix: update etcd client errors, print etcd join failures
- [`f0970ea7f`](https://github.com/talos-systems/talos/commit/f0970ea7ffe0dbca62caef2e343b91443a6ddfcb) fix: zero out manifest contents before setting new value
- [`3dc7b8a8a`](https://github.com/talos-systems/talos/commit/3dc7b8a8a2ec669e6aa4e7d9b74761ab281ee29e) chore: fix import path mismerge
- [`e26c977d8`](https://github.com/talos-systems/talos/commit/e26c977d85028dd58b6b7482a7dd37237982f0ea) fix: check retryable network errors by interface
- [`30f687b41`](https://github.com/talos-systems/talos/commit/30f687b417eeee2b789cfb064ed9cb4ab5a301e0) fix: document HDMI problem on RPi 4
- [`28753f6dc`](https://github.com/talos-systems/talos/commit/28753f6dcb85450965e4d4a0fb68f448e1deee23) fix: trim endpoints/nodes from arguments in talosctl config
- [`aca63b882`](https://github.com/talos-systems/talos/commit/aca63b8829ad0eebd449573120bff2d9b90ba828) docs: fix "DigitalOcean" spelling
- [`33035901f`](https://github.com/talos-systems/talos/commit/33035901ff7875bdf9eb99fb86b377318f60d74b) fix: revert mark PMBR EFI partition as bootable
- [`690eb20e9`](https://github.com/talos-systems/talos/commit/690eb20e9763d8f3036f0a1b4b9447f19c5ec05b) chore: update blockdevice library for PMBR bootable fix
- [`a8761b8e1`](https://github.com/talos-systems/talos/commit/a8761b8e1efd07a3bda3d8f706d3d7bf658955bb) fix: require leader on etcd member operations
- [`3dc84625c`](https://github.com/talos-systems/talos/commit/3dc84625cb1b323bad1dd93d89a13d3d59ea22d8) fix: make both HDMI ports work on RPi 4
- [`bd5ae1e0b`](https://github.com/talos-systems/talos/commit/bd5ae1e0b5dd303a017156ba7af733f79d3c13ef) fix: add a check for overlay mounts in installer pre-flight checks
- [`e16d6d346`](https://github.com/talos-systems/talos/commit/e16d6d3468a7a072b41e94fdc352df15b8321376) fix: publish rockpi4 image to release artifacts
- [`61b694b94`](https://github.com/talos-systems/talos/commit/61b694b94896da47e2ddf677cbf12b18007268a5) fix: create rootfs for system services via /system tmpfs
- [`a1e641540`](https://github.com/talos-systems/talos/commit/a1e6415403df9827fb486492a4b292b9aab3076b) fix: retry Kubernetes API errors on cordon/uncordon/etc
- [`063d1abe9`](https://github.com/talos-systems/talos/commit/063d1abe9cf1634f3517893977fc907dd9004c55) fix: print task failure error immediately
- [`e039172ed`](https://github.com/talos-systems/talos/commit/e039172edac115afbd5bf36a1f266e5967ca5398) fix: ignore EOF errors from Kubernetes API when converting control plane
- [`7bcb91a43`](https://github.com/talos-systems/talos/commit/7bcb91a433f14a29a0d2bbe9d70eb5a997eb9ab0) docs: fix typo for stage flag
- [`7d9125847`](https://github.com/talos-systems/talos/commit/7d9125847506dfadc7e137a30bf0c93ab9ca0b50) test: fix data race in apply config tests
- [`204caf8eb`](https://github.com/talos-systems/talos/commit/204caf8eb9c6c43a90c20ebaea8387584201e7f5) test: fix apply-config integration test, bump clusterctl version
- [`d812099df`](https://github.com/talos-systems/talos/commit/d812099df3d060ae74cd3d28405ddacbdd72ab15) fix: address several issues in TUI installer
- [`269c9ad09`](https://github.com/talos-systems/talos/commit/269c9ad0988f0f966a4e31a5ab744fed7d585385) fix: don't write to config object on access
- [`a0dcfc3d5`](https://github.com/talos-systems/talos/commit/a0dcfc3d5288e633db80bf3e32d31e41756cc90f) fix: workaround race in containerd runner with stdin pipe
- [`032851844`](https://github.com/talos-systems/talos/commit/032851844fdea4b1bde7507720025c981ee3b12c) fix: get rid of data race in encoder and fix concurrent map access
- [`4b3580aa5`](https://github.com/talos-systems/talos/commit/4b3580aa57d83358434238ad953793070cfc67a7) fix: prevent panic in validate config if `machine.install` is missing
- [`9f7d67ac7`](https://github.com/talos-systems/talos/commit/9f7d67ac717834ed428b8f13d4061db5f33c81f9) chore: fix typo
- [`672c97073`](https://github.com/talos-systems/talos/commit/672c970739971dd0c558ad0319fe9fdbd66a741b) fix: allow `convert-k8s --remove-initialized-keys` with K8s cp is down
- [`1f5a0c406`](https://github.com/talos-systems/talos/commit/1f5a0c4065e1fbd63ebe6d48c13e669bfb1dbeac) fix: resolve the issue with Kubernetes upgrade
- [`65701aa72`](https://github.com/talos-systems/talos/commit/65701aa724130645fcabe521557225ff41b359b0) fix: resolve the issue with DHCP lease not being renewed
- [`711f5b23b`](https://github.com/talos-systems/talos/commit/711f5b23be69665d6204dbb80064e0ab0d1468c0) fix: config validation: CNI should apply to cp nodes, encryption config
- [`5ff491d96`](https://github.com/talos-systems/talos/commit/5ff491d9686434a6208583dca97171bfbecf3f70) fix: allow empty list for CNI URLs
- [`ce795f1ce`](https://github.com/talos-systems/talos/commit/ce795f1cea9d78c26edbcd4a40bb5d3637fde629) fix: command `etcd remove-member` shouldn't remove etcd data directory
- [`aab49a167`](https://github.com/talos-systems/talos/commit/aab49a167b1f1cd3974e3aa1244d636ba712f678) fix: repair zsh completion
- [`fc9c416a3`](https://github.com/talos-systems/talos/commit/fc9c416a3c8425bb42892f740c910894610acd00) fix: build rockpi4 metal image as part of CI build
- [`125b86f4e`](https://github.com/talos-systems/talos/commit/125b86f4efbc2ed3e0a4bdfc945e97b05f1cb82c) fix: upgrade-k8s bug with empty config values and provision script
- [`5b14d6f2b`](https://github.com/talos-systems/talos/commit/5b14d6f2b89c5b86f9ec2cb0271c6605272269d4) chore: fix `make help` output
- [`7662d033b`](https://github.com/talos-systems/talos/commit/7662d033bfc3d6e3878e2c2a2a1ec4d71dc2502e) fix: talosctl health should not check kube-proxy when it is disabled
- [`e31790f6f`](https://github.com/talos-systems/talos/commit/e31790f6f548095fe3f1b9a5c88b47e70c197d2c) fix: properly format spec comments in the resources
- [`3c5bfbb47`](https://github.com/talos-systems/talos/commit/3c5bfbb4736c86f493a665dbfe63a6e2d20acb3d) fix: don't touch any partitions on upgrade with --preserve
- [`2e22f20bd`](https://github.com/talos-systems/talos/commit/2e22f20bd876e4972bfdebd44fee13356b70b83f) docs: minor fixes to getting started
- [`ca8a5596c`](https://github.com/talos-systems/talos/commit/ca8a5596c79f638e52601e850236b715f906e3d2) chore: fix provision tests after changes to build-container
- [`8e57fc4f5`](https://github.com/talos-systems/talos/commit/8e57fc4f526096878213048658bae50cfac4cda8) fix: move containerd CRI config files under `/var/`
- [`6f7df3da1`](https://github.com/talos-systems/talos/commit/6f7df3da1e147212e6d4b40a5de65e5ca8be84db) fix: update output of `convert-k8s` command
- [`7c529e1cb`](https://github.com/talos-systems/talos/commit/7c529e1cbd2be66d71e8496304781dd406495bdd) docs: fix links in the documentation
- [`4f80b97`](https://github.com/talos-systems/crypto/commit/4f80b976b640d773fb025d981bf85bcc8190815b) fix: verify CSR signature before issuing a certificate
- [`1d830a2`](https://github.com/talos-systems/go-blockdevice/commit/1d830a25f64f6fb96a1bedd800c0b40b107dc833) fix: revert mark the EFI partition in PMBR as bootable
- [`bec914f`](https://github.com/talos-systems/go-blockdevice/commit/bec914ffdda42abcfe642bc2cdfc9fcda56a74ee) fix: mark the EFI partition in PMBR as bootable
- [`d3a32be`](https://github.com/talos-systems/go-smbios/commit/d3a32bea731a0c2a60ce7f5eae60253300ef27e1) fix: return UUID in middle endian only on SMBIOS >= 2.6
- [`dbae83e`](https://github.com/talos-systems/pkgs/commit/dbae83e704da264066ceeca20e0fe66883b542ba) fix: do not use git-lfs for rockpi4 binaries

### 0.10.4

- u-boot version was updated to fix the boot and USB issues on Raspberry Pi 4 8GiB version
- [`1e19e3720`](https://github.com/talos-systems/talos/commit/1e19e3720f29eadab6f9a52be7d9d846873edde8) fix: prefer extraConfig over OVF env, skip empty config
- [`70ee15b79`](https://github.com/talos-systems/talos/commit/70ee15b793fbf4a58914a5ad9b619ce4f5906c12) fix: stop networkd and pods before leaving etcd on upgrade
- [`1e9496b80`](https://github.com/talos-systems/talos/commit/1e9496b80b7e96045333a03ea1614b5929edbf71) fix: properly populate AllowSchedulingOnMasters option in gen config RPC
- [`747903a10`](https://github.com/talos-systems/talos/commit/747903a100d3c17360a6fe43c02ab9750d67cf22) fix: stop networkd before leaving etcd on 'reset' path
- [`6fd98d95b`](https://github.com/talos-systems/talos/commit/6fd98d95b9a2e9df7a618b609d0f056f7e775f26) fix: update the way NTP sync uses `adjtimex` syscall
- [`f1298f6e3`](https://github.com/talos-systems/talos/commit/f1298f6e3ca017490eac4485c864ff9d7a55e208) fix: avoid data race on CRI pod stop
- [`194baa3d6`](https://github.com/talos-systems/talos/commit/194baa3d6b1d653edbac743bd03b88fd9f02ca05) fix: properly parse matcher expressions
- [`c613d3e22`](https://github.com/talos-systems/talos/commit/c613d3e2274b866871ff8df8b98a1831203f8202) fix: bump crypto library for the CSR verification fix
- [`801808c54`](https://github.com/talos-systems/talos/commit/801808c545209939df34da5c2d1f997f2a5b500f) fix: use both self-signed and Kubernetes CA to verify Kubelet cert
- [`280b5940c`](https://github.com/talos-systems/talos/commit/280b5940cfa58bee696d7888de65b0a181390413) fix: update osType in OVA other3xLinux64Guest"
- [`b338628dc`](https://github.com/talos-systems/talos/commit/b338628dc8547b0fd392a841c83f48e3b32f6333) fix: check if OVF env is empty
- [`564b45ba2`](https://github.com/talos-systems/talos/commit/564b45ba200531ac9dacdccd984b22eb39acdedf) fix: update etcd client errors, print etcd join failures
- [`f0970ea7f`](https://github.com/talos-systems/talos/commit/f0970ea7ffe0dbca62caef2e343b91443a6ddfcb) fix: zero out manifest contents before setting new value
- [`3dc7b8a8a`](https://github.com/talos-systems/talos/commit/3dc7b8a8a2ec669e6aa4e7d9b74761ab281ee29e) chore: fix import path mismerge
- [`e26c977d8`](https://github.com/talos-systems/talos/commit/e26c977d85028dd58b6b7482a7dd37237982f0ea) fix: check retryable network errors by interface
- [`30f687b41`](https://github.com/talos-systems/talos/commit/30f687b417eeee2b789cfb064ed9cb4ab5a301e0) fix: document HDMI problem on RPi 4
- [`28753f6dc`](https://github.com/talos-systems/talos/commit/28753f6dcb85450965e4d4a0fb68f448e1deee23) fix: trim endpoints/nodes from arguments in talosctl config
- [`aca63b882`](https://github.com/talos-systems/talos/commit/aca63b8829ad0eebd449573120bff2d9b90ba828) docs: fix "DigitalOcean" spelling
- [`33035901f`](https://github.com/talos-systems/talos/commit/33035901ff7875bdf9eb99fb86b377318f60d74b) fix: revert mark PMBR EFI partition as bootable
- [`690eb20e9`](https://github.com/talos-systems/talos/commit/690eb20e9763d8f3036f0a1b4b9447f19c5ec05b) chore: update blockdevice library for PMBR bootable fix
- [`a8761b8e1`](https://github.com/talos-systems/talos/commit/a8761b8e1efd07a3bda3d8f706d3d7bf658955bb) fix: require leader on etcd member operations
- [`3dc84625c`](https://github.com/talos-systems/talos/commit/3dc84625cb1b323bad1dd93d89a13d3d59ea22d8) fix: make both HDMI ports work on RPi 4
- [`bd5ae1e0b`](https://github.com/talos-systems/talos/commit/bd5ae1e0b5dd303a017156ba7af733f79d3c13ef) fix: add a check for overlay mounts in installer pre-flight checks
- [`e16d6d346`](https://github.com/talos-systems/talos/commit/e16d6d3468a7a072b41e94fdc352df15b8321376) fix: publish rockpi4 image to release artifacts
- [`61b694b94`](https://github.com/talos-systems/talos/commit/61b694b94896da47e2ddf677cbf12b18007268a5) fix: create rootfs for system services via /system tmpfs
- [`a1e641540`](https://github.com/talos-systems/talos/commit/a1e6415403df9827fb486492a4b292b9aab3076b) fix: retry Kubernetes API errors on cordon/uncordon/etc
- [`063d1abe9`](https://github.com/talos-systems/talos/commit/063d1abe9cf1634f3517893977fc907dd9004c55) fix: print task failure error immediately
- [`e039172ed`](https://github.com/talos-systems/talos/commit/e039172edac115afbd5bf36a1f266e5967ca5398) fix: ignore EOF errors from Kubernetes API when converting control plane
- [`7bcb91a43`](https://github.com/talos-systems/talos/commit/7bcb91a433f14a29a0d2bbe9d70eb5a997eb9ab0) docs: fix typo for stage flag
- [`7d9125847`](https://github.com/talos-systems/talos/commit/7d9125847506dfadc7e137a30bf0c93ab9ca0b50) test: fix data race in apply config tests
- [`204caf8eb`](https://github.com/talos-systems/talos/commit/204caf8eb9c6c43a90c20ebaea8387584201e7f5) test: fix apply-config integration test, bump clusterctl version
- [`d812099df`](https://github.com/talos-systems/talos/commit/d812099df3d060ae74cd3d28405ddacbdd72ab15) fix: address several issues in TUI installer
- [`269c9ad09`](https://github.com/talos-systems/talos/commit/269c9ad0988f0f966a4e31a5ab744fed7d585385) fix: don't write to config object on access
- [`a0dcfc3d5`](https://github.com/talos-systems/talos/commit/a0dcfc3d5288e633db80bf3e32d31e41756cc90f) fix: workaround race in containerd runner with stdin pipe
- [`032851844`](https://github.com/talos-systems/talos/commit/032851844fdea4b1bde7507720025c981ee3b12c) fix: get rid of data race in encoder and fix concurrent map access
- [`4b3580aa5`](https://github.com/talos-systems/talos/commit/4b3580aa57d83358434238ad953793070cfc67a7) fix: prevent panic in validate config if `machine.install` is missing
- [`9f7d67ac7`](https://github.com/talos-systems/talos/commit/9f7d67ac717834ed428b8f13d4061db5f33c81f9) chore: fix typo
- [`672c97073`](https://github.com/talos-systems/talos/commit/672c970739971dd0c558ad0319fe9fdbd66a741b) fix: allow `convert-k8s --remove-initialized-keys` with K8s cp is down
- [`1f5a0c406`](https://github.com/talos-systems/talos/commit/1f5a0c4065e1fbd63ebe6d48c13e669bfb1dbeac) fix: resolve the issue with Kubernetes upgrade
- [`65701aa72`](https://github.com/talos-systems/talos/commit/65701aa724130645fcabe521557225ff41b359b0) fix: resolve the issue with DHCP lease not being renewed
- [`711f5b23b`](https://github.com/talos-systems/talos/commit/711f5b23be69665d6204dbb80064e0ab0d1468c0) fix: config validation: CNI should apply to cp nodes, encryption config
- [`5ff491d96`](https://github.com/talos-systems/talos/commit/5ff491d9686434a6208583dca97171bfbecf3f70) fix: allow empty list for CNI URLs
- [`ce795f1ce`](https://github.com/talos-systems/talos/commit/ce795f1cea9d78c26edbcd4a40bb5d3637fde629) fix: command `etcd remove-member` shouldn't remove etcd data directory
- [`aab49a167`](https://github.com/talos-systems/talos/commit/aab49a167b1f1cd3974e3aa1244d636ba712f678) fix: repair zsh completion
- [`fc9c416a3`](https://github.com/talos-systems/talos/commit/fc9c416a3c8425bb42892f740c910894610acd00) fix: build rockpi4 metal image as part of CI build
- [`125b86f4e`](https://github.com/talos-systems/talos/commit/125b86f4efbc2ed3e0a4bdfc945e97b05f1cb82c) fix: upgrade-k8s bug with empty config values and provision script
- [`5b14d6f2b`](https://github.com/talos-systems/talos/commit/5b14d6f2b89c5b86f9ec2cb0271c6605272269d4) chore: fix `make help` output
- [`7662d033b`](https://github.com/talos-systems/talos/commit/7662d033bfc3d6e3878e2c2a2a1ec4d71dc2502e) fix: talosctl health should not check kube-proxy when it is disabled
- [`e31790f6f`](https://github.com/talos-systems/talos/commit/e31790f6f548095fe3f1b9a5c88b47e70c197d2c) fix: properly format spec comments in the resources
- [`3c5bfbb47`](https://github.com/talos-systems/talos/commit/3c5bfbb4736c86f493a665dbfe63a6e2d20acb3d) fix: don't touch any partitions on upgrade with --preserve
- [`2e22f20bd`](https://github.com/talos-systems/talos/commit/2e22f20bd876e4972bfdebd44fee13356b70b83f) docs: minor fixes to getting started
- [`ca8a5596c`](https://github.com/talos-systems/talos/commit/ca8a5596c79f638e52601e850236b715f906e3d2) chore: fix provision tests after changes to build-container
- [`8e57fc4f5`](https://github.com/talos-systems/talos/commit/8e57fc4f526096878213048658bae50cfac4cda8) fix: move containerd CRI config files under `/var/`
- [`6f7df3da1`](https://github.com/talos-systems/talos/commit/6f7df3da1e147212e6d4b40a5de65e5ca8be84db) fix: update output of `convert-k8s` command
- [`7c529e1cb`](https://github.com/talos-systems/talos/commit/7c529e1cbd2be66d71e8496304781dd406495bdd) docs: fix links in the documentation
- [`4f80b97`](https://github.com/talos-systems/crypto/commit/4f80b976b640d773fb025d981bf85bcc8190815b) fix: verify CSR signature before issuing a certificate
- [`1d830a2`](https://github.com/talos-systems/go-blockdevice/commit/1d830a25f64f6fb96a1bedd800c0b40b107dc833) fix: revert mark the EFI partition in PMBR as bootable
- [`bec914f`](https://github.com/talos-systems/go-blockdevice/commit/bec914ffdda42abcfe642bc2cdfc9fcda56a74ee) fix: mark the EFI partition in PMBR as bootable
- [`d3a32be`](https://github.com/talos-systems/go-smbios/commit/d3a32bea731a0c2a60ce7f5eae60253300ef27e1) fix: return UUID in middle endian only on SMBIOS >= 2.6
- [`dbae83e`](https://github.com/talos-systems/pkgs/commit/dbae83e704da264066ceeca20e0fe66883b542ba) fix: do not use git-lfs for rockpi4 binaries


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.10.4**, the newest release recorded here for this line.

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
