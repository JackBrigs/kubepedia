---
id: TROUBLE-TALOS_0_11_DEFECTS
type: troubleshooting
title: "talos 0.11: defects fixed in the 0.11 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.11.0 <0.12.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 0.11 known issues
  - talos 0.11 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 0.11 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 0.11: defects fixed in the 0.11 line

## Summary

**293 defects** the project fixed across **6 releases** of the 0.11 line, from 0.11.0 to
0.11.5. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.11.0

- [`673b27160`](https://github.com/talos-systems/talos/commit/673b27160d288c17886fef1b816c7b7f6ac1fc2b) fix: validate bond slaves addressing
- [`5c640cd52`](https://github.com/talos-systems/talos/commit/5c640cd52fb2827d94d7487fa2a984e521482ef2) fix: ignore DeadlineExceeded error correctly on bootstrap
- [`17edc883c`](https://github.com/talos-systems/talos/commit/17edc883cffe79c4e8fe933b8628960385f0c0f6) fix: make forfeit leadership connect to the right node
- [`f6892dba7`](https://github.com/talos-systems/talos/commit/f6892dba73c75e5754c467030184375a94c9609b) fix: close Kubernetes API client
- [`06aa24fb9`](https://github.com/talos-systems/talos/commit/06aa24fb967fb46b8997124cfadae3e9e0a29f1a) fix: ignore 'not a leader' error on forfeit leadership
- [`9075fc41c`](https://github.com/talos-systems/talos/commit/9075fc41c410fdd7508c3326db303bc988f3d0b9) fix: workaround 'Unauthorized' errors when accessing Kubernetes API
- [`8aed6c2e1`](https://github.com/talos-systems/talos/commit/8aed6c2e17645db4bbaf86c016c1a1e6acc19e1b) fix: fill uuid argument correctly in the config download URL
- [`d6c5e5004`](https://github.com/talos-systems/talos/commit/d6c5e5004cedecb7f6e36e04964e38ff7623878f) fix: make output of `upgrade-k8s` command less scary
- [`452e096e1`](https://github.com/talos-systems/talos/commit/452e096e1fa487669373b28ff8aebd4f5cd159e5) fix: restart the merge controllers on conflict
- [`79f4f1aa8`](https://github.com/talos-systems/talos/commit/79f4f1aa87fea75c602f569d3ffd2611308e50de) fix: ignore deadline exceeded errors on bootstrap
- [`7abadf726`](https://github.com/talos-systems/talos/commit/7abadf72642d1f49d455f02d3ab16231973b90cf) fix: issue worker apid certs properly on renewal
- [`33d73189e`](https://github.com/talos-systems/talos/commit/33d73189e57d070e5e90d62e9e4afb7e11a3cad8) fix: don't set bond delay options if miimon is not enabled
- [`728ad5c6f`](https://github.com/talos-systems/talos/commit/728ad5c6f06e25507f2630a19e5ed9af1d6af1a8) fix: handle cases when merged resource re-appears before being destroyed
- [`829e54f1a`](https://github.com/talos-systems/talos/commit/829e54f1a473b71acc4fe9538a1405834a6561dc) fix: limit apid access to COSI runtime resources
- [`f9e01d027`](https://github.com/talos-systems/talos/commit/f9e01d0274f9d6a2f8d6060316f102cea1ea0593) fix: ignore EINVAL on `unmount` operations
- [`b5244bf18`](https://github.com/talos-systems/talos/commit/b5244bf1827b1c7b8988ae9cb76b3053a66785d4) chore: bump go.mod dependencies, fix netaddr API changes
- [`71fff02ff`](https://github.com/talos-systems/talos/commit/71fff02ff0e120f3d05a681a101b805efa0863f0) fix: revert back resource.proto order
- [`d3f4e6006`](https://github.com/talos-systems/talos/commit/d3f4e6006f412342f1b9b71983b89d7cdc7d780a) fix: replace tabs with spaces in console output
- [`72ef48f0e`](https://github.com/talos-systems/talos/commit/72ef48f0ea1898e80977f56724e931c73d7aff94) fix: assign source address to the DHCP default gateway routes
- [`0f659622d`](https://github.com/talos-systems/talos/commit/0f659622d02260731a30d4862da99697adc7ab5c) fix: build with custom kernel/rootfs
- [`5b5089ab9`](https://github.com/talos-systems/talos/commit/5b5089ab95e2a7a345e18232520d9071180d9f10) fix: mark kube-proxy as system critical priority
- [`70ac771e0`](https://github.com/talos-systems/talos/commit/70ac771e0846247dbebf484aca20ef950d8b99c7) fix: use localhost API server endpoint for internal communication
- [`4ac9bea27`](https://github.com/talos-systems/talos/commit/4ac9bea27dc098ebdfdc0958f3000d960fad50de) fix: stop etcd client logs from going to the server console
- [`fa15a6687`](https://github.com/talos-systems/talos/commit/fa15a6687fc56820fbc5566d494bedbc1a5f600f) fix: don't enable RBAC feature in the config for Talos < 0.11
- [`2dc27d996`](https://github.com/talos-systems/talos/commit/2dc27d9964fa3df08a6ec11c0b045d7325ea0d2b) fix: do not format state partition in the initialize sequence
- [`b609f33cd`](https://github.com/talos-systems/talos/commit/b609f33cdebb0659738d4fa3802035b2b344b9b9) fix: update networking stack after Equnix Metal testing
- [`243a3b53e`](https://github.com/talos-systems/talos/commit/243a3b53e0e7591d5958a3b8373ab963990c40d6) fix: separate healthy and unknown flags in the service resource
- [`1a1378be1`](https://github.com/talos-systems/talos/commit/1a1378be16fdce45273bdc81fb72715c4766ee4b) fix: update retry package with a fix for errors.Is
- [`cb83edd7f`](https://github.com/talos-systems/talos/commit/cb83edd7fcf14bd199950a04e366fc573bcf4270) fix: wait for the network to be ready in mainteancne mode
- [`d7394457d`](https://github.com/talos-systems/talos/commit/d7394457d978d073690bec589ea78d957539e333) fix: don't treat ethtool errors as fatal
- [`caec3063c`](https://github.com/talos-systems/talos/commit/caec3063c82777f82599632ca4914a58515cb9a9) fix: do not complain about empty roles
- [`744ea8a5d`](https://github.com/talos-systems/talos/commit/744ea8a5d4b4cb4ff69c2c2fc636e499af892fee) fix: do not add bootstrap contents option if tail events is not 0
- [`5029edfb7`](https://github.com/talos-systems/talos/commit/5029edfb71990581515cabe9634d0519a9988316) fix: overwrite nodes in the gRPC metadata
- [`5aede1a83`](https://github.com/talos-systems/talos/commit/5aede1a83313152bd83891d0cae4b388a54bd9c2) fix: prefer extraConfig over OVF env, skip empty config
- [`62c702c4f`](https://github.com/talos-systems/talos/commit/62c702c4fd6e7a11654f542bbe31d1adfc896731) fix: remove conflicting etcd member on rejoin with empty data directory
- [`ff62a5998`](https://github.com/talos-systems/talos/commit/ff62a59984ef0c61dcf549ab38d39584e3630724) fix: drop into maintenance mode if config URL is `none` (metal)
- [`33db8857a`](https://github.com/talos-systems/talos/commit/33db8857aaf6e411464d08c51560473455e8e156) fix: use COSI runtime DestroyReady input type
- [`73fbb4b52`](https://github.com/talos-systems/talos/commit/73fbb4b523b41d266840eced306242d57a332b4d) fix: only fetch machine uuid if it's not set
- [`f112a540b`](https://github.com/talos-systems/talos/commit/f112a540b0e776f06820ee900d6ce9f4f2de02ec) fix: clean up stale snapshots on container start
- [`fad1b4f1f`](https://github.com/talos-systems/talos/commit/fad1b4f1fdce962b779ceb960f81d572ee5033af) chore: fix go generate for the machinery
- [`f7cf64d42`](https://github.com/talos-systems/talos/commit/f7cf64d42ec77ca68408ecb0f437ab5f86bc787a) fix: add talos.config to the vApp Properties in VMware OVA
- [`49c7276b1`](https://github.com/talos-systems/talos/commit/49c7276b16a82b7da8c83f8bd930361768f0e249) chore: fix markdown linting
- [`d3d9112f2`](https://github.com/talos-systems/talos/commit/d3d9112f288d3b0f3ebe1c8b28b1c4e2fc8512b2) docs: fix spelling/grammar in What's New for Talos 0.9
- [`a26174b54`](https://github.com/talos-systems/talos/commit/a26174b54846bdfa0b66d2f9147bfe1dc8f2eb52) fix: properly compose pattern and header in etcd members output
- [`0825cf11f`](https://github.com/talos-systems/talos/commit/0825cf11f412eef930db269b6cae02d059058101) fix: stop networkd and pods before leaving etcd on upgrade
- [`bed6b15d6`](https://github.com/talos-systems/talos/commit/bed6b15d6fcf0634a887b79797d639e221fe9387) fix: properly populate AllowSchedulingOnMasters option in gen config RPC
- [`e3f407a1d`](https://github.com/talos-systems/talos/commit/e3f407a1dff3f4ee7e024bbfb64f17b5cb5d625d) fix: properly pass disk type selector from config to matcher
- [`4ffd7c0ad`](https://github.com/talos-systems/talos/commit/4ffd7c0adf281033ac02d37ca434e7f9ad71e692) fix: stop networkd before leaving etcd on 'reset' path
- [`0e8de0469`](https://github.com/talos-systems/talos/commit/0e8de04698aac95062f3037da0a9af8b6ee916b0) fix: update go-blockdevice to fix disk type detection
- [`4d50a4edd`](https://github.com/talos-systems/talos/commit/4d50a4edd0eb413c16e899536ccdc2642e37aeaa) fix: update the way NTP sync uses `adjtimex` syscall
- [`1a85c14a5`](https://github.com/talos-systems/talos/commit/1a85c14a51fdab43ae84274563bf89b30e4e6d92) fix: avoid data race on CRI pod stop
- [`5de8dbc06`](https://github.com/talos-systems/talos/commit/5de8dbc06c7ed36c8f3af9adea8b1abedeb372b6) fix: repair pine64 support
- [`382390973`](https://github.com/talos-systems/talos/commit/3823909735859f2ac5d95bc39c051fc9c2c07685) fix: properly parse matcher expressions
- [`79d804c5b`](https://github.com/talos-systems/talos/commit/79d804c5b4af50a0fd73db17d2522d6a6b45c9ca) docs: fix typos
- [`d540a4a47`](https://github.com/talos-systems/talos/commit/d540a4a4711367a0ada203f668382e39876ba081) fix: bump crypto library for the CSR verification fix
- [`2261d7ed0`](https://github.com/talos-systems/talos/commit/2261d7ed0212c287273eac647647e4390c530a6e) fix: use both self-signed and Kubernetes CA to verify Kubelet cert
- [`7f468d350`](https://github.com/talos-systems/talos/commit/7f468d350a6f80d2815149376fa24f7d7629402c) fix: update osType in OVA other3xLinux64Guest"
- [`669a0cbdc`](https://github.com/talos-systems/talos/commit/669a0cbdc4756f0ad8f0dacc56a20f71e96fe4cd) fix: check if OVF env is empty
- [`6cb266e74`](https://github.com/talos-systems/talos/commit/6cb266e74e60d9d5423feaad550a7861dc73f11d) fix: update etcd client errors, print etcd join failures
- [`f98185408`](https://github.com/talos-systems/talos/commit/f98185408d618ebcc780247ea2c42239df27a74e) chore: fix conform with scopes
- [`7776057`](https://github.com/talos-systems/crypto/commit/7776057f5086157873f62f6a21ec23fa9fd86e05) chore: fix typos
- [`4f80b97`](https://github.com/talos-systems/crypto/commit/4f80b976b640d773fb025d981bf85bcc8190815b) fix: verify CSR signature before issuing a certificate
- [`1292574`](https://github.com/talos-systems/go-blockdevice/commit/1292574643e06512255fb0f45107e0c296eb5a3b) fix: make disk type matcher parser case insensitive
- [`b77400e`](https://github.com/talos-systems/go-blockdevice/commit/b77400e0a7261bf25da77c1f28c2f393f367bfa9) fix: properly detect nvme and sd card disk types
- [`c6d0ae2`](https://github.com/talos-systems/go-debug/commit/c6d0ae2c0ee099fa0940405401e6a02716a15bd8) fix: linters and CI
- [`c78cc95`](https://github.com/talos-systems/go-retry/commit/c78cc953d9e95992575305b4e8648392c6c9b9e6) fix: implement `errors.Is` for all errors in the set
- [`d3a32be`](https://github.com/talos-systems/go-smbios/commit/d3a32bea731a0c2a60ce7f5eae60253300ef27e1) fix: return UUID in middle endian only on SMBIOS >= 2.6
- [`b0d9cd2`](https://github.com/talos-systems/pkgs/commit/b0d9cd2c36e37190c5ce7b85acea6a51a853faaf) fix: build `zbin` utility for both amd64 and arm64

### 0.11.1

- [`27133766d`](https://github.com/talos-systems/talos/commit/27133766dfd960d6cb32ff46ea7f709e437494d3) fix: correctly pick route scope for link-local destination
- [`a7bbefe56`](https://github.com/talos-systems/talos/commit/a7bbefe562ea5def458ceca1208d48ed9f9b2b21) fix: workaround issues when IPv6 is fully or partially disabled
- [`673b27160`](https://github.com/talos-systems/talos/commit/673b27160d288c17886fef1b816c7b7f6ac1fc2b) fix: validate bond slaves addressing
- [`5c640cd52`](https://github.com/talos-systems/talos/commit/5c640cd52fb2827d94d7487fa2a984e521482ef2) fix: ignore DeadlineExceeded error correctly on bootstrap
- [`17edc883c`](https://github.com/talos-systems/talos/commit/17edc883cffe79c4e8fe933b8628960385f0c0f6) fix: make forfeit leadership connect to the right node
- [`f6892dba7`](https://github.com/talos-systems/talos/commit/f6892dba73c75e5754c467030184375a94c9609b) fix: close Kubernetes API client
- [`06aa24fb9`](https://github.com/talos-systems/talos/commit/06aa24fb967fb46b8997124cfadae3e9e0a29f1a) fix: ignore 'not a leader' error on forfeit leadership
- [`9075fc41c`](https://github.com/talos-systems/talos/commit/9075fc41c410fdd7508c3326db303bc988f3d0b9) fix: workaround 'Unauthorized' errors when accessing Kubernetes API
- [`8aed6c2e1`](https://github.com/talos-systems/talos/commit/8aed6c2e17645db4bbaf86c016c1a1e6acc19e1b) fix: fill uuid argument correctly in the config download URL
- [`d6c5e5004`](https://github.com/talos-systems/talos/commit/d6c5e5004cedecb7f6e36e04964e38ff7623878f) fix: make output of `upgrade-k8s` command less scary
- [`452e096e1`](https://github.com/talos-systems/talos/commit/452e096e1fa487669373b28ff8aebd4f5cd159e5) fix: restart the merge controllers on conflict
- [`79f4f1aa8`](https://github.com/talos-systems/talos/commit/79f4f1aa87fea75c602f569d3ffd2611308e50de) fix: ignore deadline exceeded errors on bootstrap
- [`7abadf726`](https://github.com/talos-systems/talos/commit/7abadf72642d1f49d455f02d3ab16231973b90cf) fix: issue worker apid certs properly on renewal
- [`33d73189e`](https://github.com/talos-systems/talos/commit/33d73189e57d070e5e90d62e9e4afb7e11a3cad8) fix: don't set bond delay options if miimon is not enabled
- [`728ad5c6f`](https://github.com/talos-systems/talos/commit/728ad5c6f06e25507f2630a19e5ed9af1d6af1a8) fix: handle cases when merged resource re-appears before being destroyed
- [`829e54f1a`](https://github.com/talos-systems/talos/commit/829e54f1a473b71acc4fe9538a1405834a6561dc) fix: limit apid access to COSI runtime resources
- [`f9e01d027`](https://github.com/talos-systems/talos/commit/f9e01d0274f9d6a2f8d6060316f102cea1ea0593) fix: ignore EINVAL on `unmount` operations
- [`b5244bf18`](https://github.com/talos-systems/talos/commit/b5244bf1827b1c7b8988ae9cb76b3053a66785d4) chore: bump go.mod dependencies, fix netaddr API changes
- [`71fff02ff`](https://github.com/talos-systems/talos/commit/71fff02ff0e120f3d05a681a101b805efa0863f0) fix: revert back resource.proto order
- [`d3f4e6006`](https://github.com/talos-systems/talos/commit/d3f4e6006f412342f1b9b71983b89d7cdc7d780a) fix: replace tabs with spaces in console output
- [`72ef48f0e`](https://github.com/talos-systems/talos/commit/72ef48f0ea1898e80977f56724e931c73d7aff94) fix: assign source address to the DHCP default gateway routes
- [`0f659622d`](https://github.com/talos-systems/talos/commit/0f659622d02260731a30d4862da99697adc7ab5c) fix: build with custom kernel/rootfs
- [`5b5089ab9`](https://github.com/talos-systems/talos/commit/5b5089ab95e2a7a345e18232520d9071180d9f10) fix: mark kube-proxy as system critical priority
- [`70ac771e0`](https://github.com/talos-systems/talos/commit/70ac771e0846247dbebf484aca20ef950d8b99c7) fix: use localhost API server endpoint for internal communication
- [`4ac9bea27`](https://github.com/talos-systems/talos/commit/4ac9bea27dc098ebdfdc0958f3000d960fad50de) fix: stop etcd client logs from going to the server console
- [`fa15a6687`](https://github.com/talos-systems/talos/commit/fa15a6687fc56820fbc5566d494bedbc1a5f600f) fix: don't enable RBAC feature in the config for Talos < 0.11
- [`2dc27d996`](https://github.com/talos-systems/talos/commit/2dc27d9964fa3df08a6ec11c0b045d7325ea0d2b) fix: do not format state partition in the initialize sequence
- [`b609f33cd`](https://github.com/talos-systems/talos/commit/b609f33cdebb0659738d4fa3802035b2b344b9b9) fix: update networking stack after Equnix Metal testing
- [`243a3b53e`](https://github.com/talos-systems/talos/commit/243a3b53e0e7591d5958a3b8373ab963990c40d6) fix: separate healthy and unknown flags in the service resource
- [`1a1378be1`](https://github.com/talos-systems/talos/commit/1a1378be16fdce45273bdc81fb72715c4766ee4b) fix: update retry package with a fix for errors.Is
- [`cb83edd7f`](https://github.com/talos-systems/talos/commit/cb83edd7fcf14bd199950a04e366fc573bcf4270) fix: wait for the network to be ready in mainteancne mode
- [`d7394457d`](https://github.com/talos-systems/talos/commit/d7394457d978d073690bec589ea78d957539e333) fix: don't treat ethtool errors as fatal
- [`caec3063c`](https://github.com/talos-systems/talos/commit/caec3063c82777f82599632ca4914a58515cb9a9) fix: do not complain about empty roles
- [`744ea8a5d`](https://github.com/talos-systems/talos/commit/744ea8a5d4b4cb4ff69c2c2fc636e499af892fee) fix: do not add bootstrap contents option if tail events is not 0
- [`5029edfb7`](https://github.com/talos-systems/talos/commit/5029edfb71990581515cabe9634d0519a9988316) fix: overwrite nodes in the gRPC metadata
- [`5aede1a83`](https://github.com/talos-systems/talos/commit/5aede1a83313152bd83891d0cae4b388a54bd9c2) fix: prefer extraConfig over OVF env, skip empty config
- [`62c702c4f`](https://github.com/talos-systems/talos/commit/62c702c4fd6e7a11654f542bbe31d1adfc896731) fix: remove conflicting etcd member on rejoin with empty data directory
- [`ff62a5998`](https://github.com/talos-systems/talos/commit/ff62a59984ef0c61dcf549ab38d39584e3630724) fix: drop into maintenance mode if config URL is `none` (metal)
- [`33db8857a`](https://github.com/talos-systems/talos/commit/33db8857aaf6e411464d08c51560473455e8e156) fix: use COSI runtime DestroyReady input type
- [`73fbb4b52`](https://github.com/talos-systems/talos/commit/73fbb4b523b41d266840eced306242d57a332b4d) fix: only fetch machine uuid if it's not set
- [`f112a540b`](https://github.com/talos-systems/talos/commit/f112a540b0e776f06820ee900d6ce9f4f2de02ec) fix: clean up stale snapshots on container start
- [`fad1b4f1f`](https://github.com/talos-systems/talos/commit/fad1b4f1fdce962b779ceb960f81d572ee5033af) chore: fix go generate for the machinery
- [`f7cf64d42`](https://github.com/talos-systems/talos/commit/f7cf64d42ec77ca68408ecb0f437ab5f86bc787a) fix: add talos.config to the vApp Properties in VMware OVA
- [`49c7276b1`](https://github.com/talos-systems/talos/commit/49c7276b16a82b7da8c83f8bd930361768f0e249) chore: fix markdown linting
- [`d3d9112f2`](https://github.com/talos-systems/talos/commit/d3d9112f288d3b0f3ebe1c8b28b1c4e2fc8512b2) docs: fix spelling/grammar in What's New for Talos 0.9
- [`a26174b54`](https://github.com/talos-systems/talos/commit/a26174b54846bdfa0b66d2f9147bfe1dc8f2eb52) fix: properly compose pattern and header in etcd members output
- [`0825cf11f`](https://github.com/talos-systems/talos/commit/0825cf11f412eef930db269b6cae02d059058101) fix: stop networkd and pods before leaving etcd on upgrade
- [`bed6b15d6`](https://github.com/talos-systems/talos/commit/bed6b15d6fcf0634a887b79797d639e221fe9387) fix: properly populate AllowSchedulingOnMasters option in gen config RPC
- [`e3f407a1d`](https://github.com/talos-systems/talos/commit/e3f407a1dff3f4ee7e024bbfb64f17b5cb5d625d) fix: properly pass disk type selector from config to matcher
- [`4ffd7c0ad`](https://github.com/talos-systems/talos/commit/4ffd7c0adf281033ac02d37ca434e7f9ad71e692) fix: stop networkd before leaving etcd on 'reset' path
- [`0e8de0469`](https://github.com/talos-systems/talos/commit/0e8de04698aac95062f3037da0a9af8b6ee916b0) fix: update go-blockdevice to fix disk type detection
- [`4d50a4edd`](https://github.com/talos-systems/talos/commit/4d50a4edd0eb413c16e899536ccdc2642e37aeaa) fix: update the way NTP sync uses `adjtimex` syscall
- [`1a85c14a5`](https://github.com/talos-systems/talos/commit/1a85c14a51fdab43ae84274563bf89b30e4e6d92) fix: avoid data race on CRI pod stop
- [`5de8dbc06`](https://github.com/talos-systems/talos/commit/5de8dbc06c7ed36c8f3af9adea8b1abedeb372b6) fix: repair pine64 support
- [`382390973`](https://github.com/talos-systems/talos/commit/3823909735859f2ac5d95bc39c051fc9c2c07685) fix: properly parse matcher expressions
- [`79d804c5b`](https://github.com/talos-systems/talos/commit/79d804c5b4af50a0fd73db17d2522d6a6b45c9ca) docs: fix typos
- [`d540a4a47`](https://github.com/talos-systems/talos/commit/d540a4a4711367a0ada203f668382e39876ba081) fix: bump crypto library for the CSR verification fix
- [`2261d7ed0`](https://github.com/talos-systems/talos/commit/2261d7ed0212c287273eac647647e4390c530a6e) fix: use both self-signed and Kubernetes CA to verify Kubelet cert
- [`7f468d350`](https://github.com/talos-systems/talos/commit/7f468d350a6f80d2815149376fa24f7d7629402c) fix: update osType in OVA other3xLinux64Guest"
- [`669a0cbdc`](https://github.com/talos-systems/talos/commit/669a0cbdc4756f0ad8f0dacc56a20f71e96fe4cd) fix: check if OVF env is empty
- [`6cb266e74`](https://github.com/talos-systems/talos/commit/6cb266e74e60d9d5423feaad550a7861dc73f11d) fix: update etcd client errors, print etcd join failures
- [`f98185408`](https://github.com/talos-systems/talos/commit/f98185408d618ebcc780247ea2c42239df27a74e) chore: fix conform with scopes
- [`7776057`](https://github.com/talos-systems/crypto/commit/7776057f5086157873f62f6a21ec23fa9fd86e05) chore: fix typos
- [`4f80b97`](https://github.com/talos-systems/crypto/commit/4f80b976b640d773fb025d981bf85bcc8190815b) fix: verify CSR signature before issuing a certificate
- [`1292574`](https://github.com/talos-systems/go-blockdevice/commit/1292574643e06512255fb0f45107e0c296eb5a3b) fix: make disk type matcher parser case insensitive
- [`b77400e`](https://github.com/talos-systems/go-blockdevice/commit/b77400e0a7261bf25da77c1f28c2f393f367bfa9) fix: properly detect nvme and sd card disk types
- [`c6d0ae2`](https://github.com/talos-systems/go-debug/commit/c6d0ae2c0ee099fa0940405401e6a02716a15bd8) fix: linters and CI
- [`c78cc95`](https://github.com/talos-systems/go-retry/commit/c78cc953d9e95992575305b4e8648392c6c9b9e6) fix: implement `errors.Is` for all errors in the set
- [`d3a32be`](https://github.com/talos-systems/go-smbios/commit/d3a32bea731a0c2a60ce7f5eae60253300ef27e1) fix: return UUID in middle endian only on SMBIOS >= 2.6
- [`b0d9cd2`](https://github.com/talos-systems/pkgs/commit/b0d9cd2c36e37190c5ce7b85acea6a51a853faaf) fix: build `zbin` utility for both amd64 and arm64

### 0.11.2

- [`671c00c41`](https://github.com/talos-systems/talos/commit/671c00c41aa04dd076807b69321ace3f2d417b06) fix: make ethtool optional in link status controller
- [`27133766d`](https://github.com/talos-systems/talos/commit/27133766dfd960d6cb32ff46ea7f709e437494d3) fix: correctly pick route scope for link-local destination
- [`a7bbefe56`](https://github.com/talos-systems/talos/commit/a7bbefe562ea5def458ceca1208d48ed9f9b2b21) fix: workaround issues when IPv6 is fully or partially disabled
- [`673b27160`](https://github.com/talos-systems/talos/commit/673b27160d288c17886fef1b816c7b7f6ac1fc2b) fix: validate bond slaves addressing
- [`5c640cd52`](https://github.com/talos-systems/talos/commit/5c640cd52fb2827d94d7487fa2a984e521482ef2) fix: ignore DeadlineExceeded error correctly on bootstrap
- [`17edc883c`](https://github.com/talos-systems/talos/commit/17edc883cffe79c4e8fe933b8628960385f0c0f6) fix: make forfeit leadership connect to the right node
- [`f6892dba7`](https://github.com/talos-systems/talos/commit/f6892dba73c75e5754c467030184375a94c9609b) fix: close Kubernetes API client
- [`06aa24fb9`](https://github.com/talos-systems/talos/commit/06aa24fb967fb46b8997124cfadae3e9e0a29f1a) fix: ignore 'not a leader' error on forfeit leadership
- [`9075fc41c`](https://github.com/talos-systems/talos/commit/9075fc41c410fdd7508c3326db303bc988f3d0b9) fix: workaround 'Unauthorized' errors when accessing Kubernetes API
- [`8aed6c2e1`](https://github.com/talos-systems/talos/commit/8aed6c2e17645db4bbaf86c016c1a1e6acc19e1b) fix: fill uuid argument correctly in the config download URL
- [`d6c5e5004`](https://github.com/talos-systems/talos/commit/d6c5e5004cedecb7f6e36e04964e38ff7623878f) fix: make output of `upgrade-k8s` command less scary
- [`452e096e1`](https://github.com/talos-systems/talos/commit/452e096e1fa487669373b28ff8aebd4f5cd159e5) fix: restart the merge controllers on conflict
- [`79f4f1aa8`](https://github.com/talos-systems/talos/commit/79f4f1aa87fea75c602f569d3ffd2611308e50de) fix: ignore deadline exceeded errors on bootstrap
- [`7abadf726`](https://github.com/talos-systems/talos/commit/7abadf72642d1f49d455f02d3ab16231973b90cf) fix: issue worker apid certs properly on renewal
- [`33d73189e`](https://github.com/talos-systems/talos/commit/33d73189e57d070e5e90d62e9e4afb7e11a3cad8) fix: don't set bond delay options if miimon is not enabled
- [`728ad5c6f`](https://github.com/talos-systems/talos/commit/728ad5c6f06e25507f2630a19e5ed9af1d6af1a8) fix: handle cases when merged resource re-appears before being destroyed
- [`829e54f1a`](https://github.com/talos-systems/talos/commit/829e54f1a473b71acc4fe9538a1405834a6561dc) fix: limit apid access to COSI runtime resources
- [`f9e01d027`](https://github.com/talos-systems/talos/commit/f9e01d0274f9d6a2f8d6060316f102cea1ea0593) fix: ignore EINVAL on `unmount` operations
- [`b5244bf18`](https://github.com/talos-systems/talos/commit/b5244bf1827b1c7b8988ae9cb76b3053a66785d4) chore: bump go.mod dependencies, fix netaddr API changes
- [`71fff02ff`](https://github.com/talos-systems/talos/commit/71fff02ff0e120f3d05a681a101b805efa0863f0) fix: revert back resource.proto order
- [`d3f4e6006`](https://github.com/talos-systems/talos/commit/d3f4e6006f412342f1b9b71983b89d7cdc7d780a) fix: replace tabs with spaces in console output
- [`72ef48f0e`](https://github.com/talos-systems/talos/commit/72ef48f0ea1898e80977f56724e931c73d7aff94) fix: assign source address to the DHCP default gateway routes
- [`0f659622d`](https://github.com/talos-systems/talos/commit/0f659622d02260731a30d4862da99697adc7ab5c) fix: build with custom kernel/rootfs
- [`5b5089ab9`](https://github.com/talos-systems/talos/commit/5b5089ab95e2a7a345e18232520d9071180d9f10) fix: mark kube-proxy as system critical priority
- [`70ac771e0`](https://github.com/talos-systems/talos/commit/70ac771e0846247dbebf484aca20ef950d8b99c7) fix: use localhost API server endpoint for internal communication
- [`4ac9bea27`](https://github.com/talos-systems/talos/commit/4ac9bea27dc098ebdfdc0958f3000d960fad50de) fix: stop etcd client logs from going to the server console
- [`fa15a6687`](https://github.com/talos-systems/talos/commit/fa15a6687fc56820fbc5566d494bedbc1a5f600f) fix: don't enable RBAC feature in the config for Talos < 0.11
- [`2dc27d996`](https://github.com/talos-systems/talos/commit/2dc27d9964fa3df08a6ec11c0b045d7325ea0d2b) fix: do not format state partition in the initialize sequence
- [`b609f33cd`](https://github.com/talos-systems/talos/commit/b609f33cdebb0659738d4fa3802035b2b344b9b9) fix: update networking stack after Equnix Metal testing
- [`243a3b53e`](https://github.com/talos-systems/talos/commit/243a3b53e0e7591d5958a3b8373ab963990c40d6) fix: separate healthy and unknown flags in the service resource
- [`1a1378be1`](https://github.com/talos-systems/talos/commit/1a1378be16fdce45273bdc81fb72715c4766ee4b) fix: update retry package with a fix for errors.Is
- [`cb83edd7f`](https://github.com/talos-systems/talos/commit/cb83edd7fcf14bd199950a04e366fc573bcf4270) fix: wait for the network to be ready in mainteancne mode
- [`d7394457d`](https://github.com/talos-systems/talos/commit/d7394457d978d073690bec589ea78d957539e333) fix: don't treat ethtool errors as fatal
- [`caec3063c`](https://github.com/talos-systems/talos/commit/caec3063c82777f82599632ca4914a58515cb9a9) fix: do not complain about empty roles
- [`744ea8a5d`](https://github.com/talos-systems/talos/commit/744ea8a5d4b4cb4ff69c2c2fc636e499af892fee) fix: do not add bootstrap contents option if tail events is not 0
- [`5029edfb7`](https://github.com/talos-systems/talos/commit/5029edfb71990581515cabe9634d0519a9988316) fix: overwrite nodes in the gRPC metadata
- [`5aede1a83`](https://github.com/talos-systems/talos/commit/5aede1a83313152bd83891d0cae4b388a54bd9c2) fix: prefer extraConfig over OVF env, skip empty config
- [`62c702c4f`](https://github.com/talos-systems/talos/commit/62c702c4fd6e7a11654f542bbe31d1adfc896731) fix: remove conflicting etcd member on rejoin with empty data directory
- [`ff62a5998`](https://github.com/talos-systems/talos/commit/ff62a59984ef0c61dcf549ab38d39584e3630724) fix: drop into maintenance mode if config URL is `none` (metal)
- [`33db8857a`](https://github.com/talos-systems/talos/commit/33db8857aaf6e411464d08c51560473455e8e156) fix: use COSI runtime DestroyReady input type
- [`73fbb4b52`](https://github.com/talos-systems/talos/commit/73fbb4b523b41d266840eced306242d57a332b4d) fix: only fetch machine uuid if it's not set
- [`f112a540b`](https://github.com/talos-systems/talos/commit/f112a540b0e776f06820ee900d6ce9f4f2de02ec) fix: clean up stale snapshots on container start
- [`fad1b4f1f`](https://github.com/talos-systems/talos/commit/fad1b4f1fdce962b779ceb960f81d572ee5033af) chore: fix go generate for the machinery
- [`f7cf64d42`](https://github.com/talos-systems/talos/commit/f7cf64d42ec77ca68408ecb0f437ab5f86bc787a) fix: add talos.config to the vApp Properties in VMware OVA
- [`49c7276b1`](https://github.com/talos-systems/talos/commit/49c7276b16a82b7da8c83f8bd930361768f0e249) chore: fix markdown linting
- [`d3d9112f2`](https://github.com/talos-systems/talos/commit/d3d9112f288d3b0f3ebe1c8b28b1c4e2fc8512b2) docs: fix spelling/grammar in What's New for Talos 0.9
- [`a26174b54`](https://github.com/talos-systems/talos/commit/a26174b54846bdfa0b66d2f9147bfe1dc8f2eb52) fix: properly compose pattern and header in etcd members output
- [`0825cf11f`](https://github.com/talos-systems/talos/commit/0825cf11f412eef930db269b6cae02d059058101) fix: stop networkd and pods before leaving etcd on upgrade
- [`bed6b15d6`](https://github.com/talos-systems/talos/commit/bed6b15d6fcf0634a887b79797d639e221fe9387) fix: properly populate AllowSchedulingOnMasters option in gen config RPC
- [`e3f407a1d`](https://github.com/talos-systems/talos/commit/e3f407a1dff3f4ee7e024bbfb64f17b5cb5d625d) fix: properly pass disk type selector from config to matcher
- [`4ffd7c0ad`](https://github.com/talos-systems/talos/commit/4ffd7c0adf281033ac02d37ca434e7f9ad71e692) fix: stop networkd before leaving etcd on 'reset' path
- [`0e8de0469`](https://github.com/talos-systems/talos/commit/0e8de04698aac95062f3037da0a9af8b6ee916b0) fix: update go-blockdevice to fix disk type detection
- [`4d50a4edd`](https://github.com/talos-systems/talos/commit/4d50a4edd0eb413c16e899536ccdc2642e37aeaa) fix: update the way NTP sync uses `adjtimex` syscall
- [`1a85c14a5`](https://github.com/talos-systems/talos/commit/1a85c14a51fdab43ae84274563bf89b30e4e6d92) fix: avoid data race on CRI pod stop
- [`5de8dbc06`](https://github.com/talos-systems/talos/commit/5de8dbc06c7ed36c8f3af9adea8b1abedeb372b6) fix: repair pine64 support
- [`382390973`](https://github.com/talos-systems/talos/commit/3823909735859f2ac5d95bc39c051fc9c2c07685) fix: properly parse matcher expressions
- [`79d804c5b`](https://github.com/talos-systems/talos/commit/79d804c5b4af50a0fd73db17d2522d6a6b45c9ca) docs: fix typos
- [`d540a4a47`](https://github.com/talos-systems/talos/commit/d540a4a4711367a0ada203f668382e39876ba081) fix: bump crypto library for the CSR verification fix
- [`2261d7ed0`](https://github.com/talos-systems/talos/commit/2261d7ed0212c287273eac647647e4390c530a6e) fix: use both self-signed and Kubernetes CA to verify Kubelet cert
- [`7f468d350`](https://github.com/talos-systems/talos/commit/7f468d350a6f80d2815149376fa24f7d7629402c) fix: update osType in OVA other3xLinux64Guest"
- [`669a0cbdc`](https://github.com/talos-systems/talos/commit/669a0cbdc4756f0ad8f0dacc56a20f71e96fe4cd) fix: check if OVF env is empty
- [`6cb266e74`](https://github.com/talos-systems/talos/commit/6cb266e74e60d9d5423feaad550a7861dc73f11d) fix: update etcd client errors, print etcd join failures
- [`f98185408`](https://github.com/talos-systems/talos/commit/f98185408d618ebcc780247ea2c42239df27a74e) chore: fix conform with scopes
- [`7776057`](https://github.com/talos-systems/crypto/commit/7776057f5086157873f62f6a21ec23fa9fd86e05) chore: fix typos
- [`4f80b97`](https://github.com/talos-systems/crypto/commit/4f80b976b640d773fb025d981bf85bcc8190815b) fix: verify CSR signature before issuing a certificate
- [`1292574`](https://github.com/talos-systems/go-blockdevice/commit/1292574643e06512255fb0f45107e0c296eb5a3b) fix: make disk type matcher parser case insensitive
- [`b77400e`](https://github.com/talos-systems/go-blockdevice/commit/b77400e0a7261bf25da77c1f28c2f393f367bfa9) fix: properly detect nvme and sd card disk types
- [`c6d0ae2`](https://github.com/talos-systems/go-debug/commit/c6d0ae2c0ee099fa0940405401e6a02716a15bd8) fix: linters and CI
- [`c78cc95`](https://github.com/talos-systems/go-retry/commit/c78cc953d9e95992575305b4e8648392c6c9b9e6) fix: implement `errors.Is` for all errors in the set
- [`d3a32be`](https://github.com/talos-systems/go-smbios/commit/d3a32bea731a0c2a60ce7f5eae60253300ef27e1) fix: return UUID in middle endian only on SMBIOS >= 2.6
- [`b0d9cd2`](https://github.com/talos-systems/pkgs/commit/b0d9cd2c36e37190c5ce7b85acea6a51a853faaf) fix: build `zbin` utility for both amd64 and arm64

### 0.11.3

- [`ddf63dfda`](https://github.com/talos-systems/talos/commit/ddf63dfdabfabba44756177e1911f22baa5907a4) fix: bump pkgs for new kernel 5.10.52
- [`671c00c41`](https://github.com/talos-systems/talos/commit/671c00c41aa04dd076807b69321ace3f2d417b06) fix: make ethtool optional in link status controller
- [`27133766d`](https://github.com/talos-systems/talos/commit/27133766dfd960d6cb32ff46ea7f709e437494d3) fix: correctly pick route scope for link-local destination
- [`a7bbefe56`](https://github.com/talos-systems/talos/commit/a7bbefe562ea5def458ceca1208d48ed9f9b2b21) fix: workaround issues when IPv6 is fully or partially disabled
- [`673b27160`](https://github.com/talos-systems/talos/commit/673b27160d288c17886fef1b816c7b7f6ac1fc2b) fix: validate bond slaves addressing
- [`5c640cd52`](https://github.com/talos-systems/talos/commit/5c640cd52fb2827d94d7487fa2a984e521482ef2) fix: ignore DeadlineExceeded error correctly on bootstrap
- [`17edc883c`](https://github.com/talos-systems/talos/commit/17edc883cffe79c4e8fe933b8628960385f0c0f6) fix: make forfeit leadership connect to the right node
- [`f6892dba7`](https://github.com/talos-systems/talos/commit/f6892dba73c75e5754c467030184375a94c9609b) fix: close Kubernetes API client
- [`06aa24fb9`](https://github.com/talos-systems/talos/commit/06aa24fb967fb46b8997124cfadae3e9e0a29f1a) fix: ignore 'not a leader' error on forfeit leadership
- [`9075fc41c`](https://github.com/talos-systems/talos/commit/9075fc41c410fdd7508c3326db303bc988f3d0b9) fix: workaround 'Unauthorized' errors when accessing Kubernetes API
- [`8aed6c2e1`](https://github.com/talos-systems/talos/commit/8aed6c2e17645db4bbaf86c016c1a1e6acc19e1b) fix: fill uuid argument correctly in the config download URL
- [`d6c5e5004`](https://github.com/talos-systems/talos/commit/d6c5e5004cedecb7f6e36e04964e38ff7623878f) fix: make output of `upgrade-k8s` command less scary
- [`452e096e1`](https://github.com/talos-systems/talos/commit/452e096e1fa487669373b28ff8aebd4f5cd159e5) fix: restart the merge controllers on conflict
- [`79f4f1aa8`](https://github.com/talos-systems/talos/commit/79f4f1aa87fea75c602f569d3ffd2611308e50de) fix: ignore deadline exceeded errors on bootstrap
- [`7abadf726`](https://github.com/talos-systems/talos/commit/7abadf72642d1f49d455f02d3ab16231973b90cf) fix: issue worker apid certs properly on renewal
- [`33d73189e`](https://github.com/talos-systems/talos/commit/33d73189e57d070e5e90d62e9e4afb7e11a3cad8) fix: don't set bond delay options if miimon is not enabled
- [`728ad5c6f`](https://github.com/talos-systems/talos/commit/728ad5c6f06e25507f2630a19e5ed9af1d6af1a8) fix: handle cases when merged resource re-appears before being destroyed
- [`829e54f1a`](https://github.com/talos-systems/talos/commit/829e54f1a473b71acc4fe9538a1405834a6561dc) fix: limit apid access to COSI runtime resources
- [`f9e01d027`](https://github.com/talos-systems/talos/commit/f9e01d0274f9d6a2f8d6060316f102cea1ea0593) fix: ignore EINVAL on `unmount` operations
- [`b5244bf18`](https://github.com/talos-systems/talos/commit/b5244bf1827b1c7b8988ae9cb76b3053a66785d4) chore: bump go.mod dependencies, fix netaddr API changes
- [`71fff02ff`](https://github.com/talos-systems/talos/commit/71fff02ff0e120f3d05a681a101b805efa0863f0) fix: revert back resource.proto order
- [`d3f4e6006`](https://github.com/talos-systems/talos/commit/d3f4e6006f412342f1b9b71983b89d7cdc7d780a) fix: replace tabs with spaces in console output
- [`72ef48f0e`](https://github.com/talos-systems/talos/commit/72ef48f0ea1898e80977f56724e931c73d7aff94) fix: assign source address to the DHCP default gateway routes
- [`0f659622d`](https://github.com/talos-systems/talos/commit/0f659622d02260731a30d4862da99697adc7ab5c) fix: build with custom kernel/rootfs
- [`5b5089ab9`](https://github.com/talos-systems/talos/commit/5b5089ab95e2a7a345e18232520d9071180d9f10) fix: mark kube-proxy as system critical priority
- [`70ac771e0`](https://github.com/talos-systems/talos/commit/70ac771e0846247dbebf484aca20ef950d8b99c7) fix: use localhost API server endpoint for internal communication
- [`4ac9bea27`](https://github.com/talos-systems/talos/commit/4ac9bea27dc098ebdfdc0958f3000d960fad50de) fix: stop etcd client logs from going to the server console
- [`fa15a6687`](https://github.com/talos-systems/talos/commit/fa15a6687fc56820fbc5566d494bedbc1a5f600f) fix: don't enable RBAC feature in the config for Talos < 0.11
- [`2dc27d996`](https://github.com/talos-systems/talos/commit/2dc27d9964fa3df08a6ec11c0b045d7325ea0d2b) fix: do not format state partition in the initialize sequence
- [`b609f33cd`](https://github.com/talos-systems/talos/commit/b609f33cdebb0659738d4fa3802035b2b344b9b9) fix: update networking stack after Equnix Metal testing
- [`243a3b53e`](https://github.com/talos-systems/talos/commit/243a3b53e0e7591d5958a3b8373ab963990c40d6) fix: separate healthy and unknown flags in the service resource
- [`1a1378be1`](https://github.com/talos-systems/talos/commit/1a1378be16fdce45273bdc81fb72715c4766ee4b) fix: update retry package with a fix for errors.Is
- [`cb83edd7f`](https://github.com/talos-systems/talos/commit/cb83edd7fcf14bd199950a04e366fc573bcf4270) fix: wait for the network to be ready in mainteancne mode
- [`d7394457d`](https://github.com/talos-systems/talos/commit/d7394457d978d073690bec589ea78d957539e333) fix: don't treat ethtool errors as fatal
- [`caec3063c`](https://github.com/talos-systems/talos/commit/caec3063c82777f82599632ca4914a58515cb9a9) fix: do not complain about empty roles
- [`744ea8a5d`](https://github.com/talos-systems/talos/commit/744ea8a5d4b4cb4ff69c2c2fc636e499af892fee) fix: do not add bootstrap contents option if tail events is not 0
- [`5029edfb7`](https://github.com/talos-systems/talos/commit/5029edfb71990581515cabe9634d0519a9988316) fix: overwrite nodes in the gRPC metadata
- [`5aede1a83`](https://github.com/talos-systems/talos/commit/5aede1a83313152bd83891d0cae4b388a54bd9c2) fix: prefer extraConfig over OVF env, skip empty config
- [`62c702c4f`](https://github.com/talos-systems/talos/commit/62c702c4fd6e7a11654f542bbe31d1adfc896731) fix: remove conflicting etcd member on rejoin with empty data directory
- [`ff62a5998`](https://github.com/talos-systems/talos/commit/ff62a59984ef0c61dcf549ab38d39584e3630724) fix: drop into maintenance mode if config URL is `none` (metal)
- [`33db8857a`](https://github.com/talos-systems/talos/commit/33db8857aaf6e411464d08c51560473455e8e156) fix: use COSI runtime DestroyReady input type
- [`73fbb4b52`](https://github.com/talos-systems/talos/commit/73fbb4b523b41d266840eced306242d57a332b4d) fix: only fetch machine uuid if it's not set
- [`f112a540b`](https://github.com/talos-systems/talos/commit/f112a540b0e776f06820ee900d6ce9f4f2de02ec) fix: clean up stale snapshots on container start
- [`fad1b4f1f`](https://github.com/talos-systems/talos/commit/fad1b4f1fdce962b779ceb960f81d572ee5033af) chore: fix go generate for the machinery
- [`f7cf64d42`](https://github.com/talos-systems/talos/commit/f7cf64d42ec77ca68408ecb0f437ab5f86bc787a) fix: add talos.config to the vApp Properties in VMware OVA
- [`49c7276b1`](https://github.com/talos-systems/talos/commit/49c7276b16a82b7da8c83f8bd930361768f0e249) chore: fix markdown linting
- [`d3d9112f2`](https://github.com/talos-systems/talos/commit/d3d9112f288d3b0f3ebe1c8b28b1c4e2fc8512b2) docs: fix spelling/grammar in What's New for Talos 0.9
- [`a26174b54`](https://github.com/talos-systems/talos/commit/a26174b54846bdfa0b66d2f9147bfe1dc8f2eb52) fix: properly compose pattern and header in etcd members output
- [`0825cf11f`](https://github.com/talos-systems/talos/commit/0825cf11f412eef930db269b6cae02d059058101) fix: stop networkd and pods before leaving etcd on upgrade
- [`bed6b15d6`](https://github.com/talos-systems/talos/commit/bed6b15d6fcf0634a887b79797d639e221fe9387) fix: properly populate AllowSchedulingOnMasters option in gen config RPC
- [`e3f407a1d`](https://github.com/talos-systems/talos/commit/e3f407a1dff3f4ee7e024bbfb64f17b5cb5d625d) fix: properly pass disk type selector from config to matcher
- [`4ffd7c0ad`](https://github.com/talos-systems/talos/commit/4ffd7c0adf281033ac02d37ca434e7f9ad71e692) fix: stop networkd before leaving etcd on 'reset' path
- [`0e8de0469`](https://github.com/talos-systems/talos/commit/0e8de04698aac95062f3037da0a9af8b6ee916b0) fix: update go-blockdevice to fix disk type detection
- [`4d50a4edd`](https://github.com/talos-systems/talos/commit/4d50a4edd0eb413c16e899536ccdc2642e37aeaa) fix: update the way NTP sync uses `adjtimex` syscall
- [`1a85c14a5`](https://github.com/talos-systems/talos/commit/1a85c14a51fdab43ae84274563bf89b30e4e6d92) fix: avoid data race on CRI pod stop
- [`5de8dbc06`](https://github.com/talos-systems/talos/commit/5de8dbc06c7ed36c8f3af9adea8b1abedeb372b6) fix: repair pine64 support
- [`382390973`](https://github.com/talos-systems/talos/commit/3823909735859f2ac5d95bc39c051fc9c2c07685) fix: properly parse matcher expressions
- [`79d804c5b`](https://github.com/talos-systems/talos/commit/79d804c5b4af50a0fd73db17d2522d6a6b45c9ca) docs: fix typos
- [`d540a4a47`](https://github.com/talos-systems/talos/commit/d540a4a4711367a0ada203f668382e39876ba081) fix: bump crypto library for the CSR verification fix
- [`2261d7ed0`](https://github.com/talos-systems/talos/commit/2261d7ed0212c287273eac647647e4390c530a6e) fix: use both self-signed and Kubernetes CA to verify Kubelet cert
- [`7f468d350`](https://github.com/talos-systems/talos/commit/7f468d350a6f80d2815149376fa24f7d7629402c) fix: update osType in OVA other3xLinux64Guest"
- [`669a0cbdc`](https://github.com/talos-systems/talos/commit/669a0cbdc4756f0ad8f0dacc56a20f71e96fe4cd) fix: check if OVF env is empty
- [`6cb266e74`](https://github.com/talos-systems/talos/commit/6cb266e74e60d9d5423feaad550a7861dc73f11d) fix: update etcd client errors, print etcd join failures
- [`f98185408`](https://github.com/talos-systems/talos/commit/f98185408d618ebcc780247ea2c42239df27a74e) chore: fix conform with scopes
- [`7776057`](https://github.com/talos-systems/crypto/commit/7776057f5086157873f62f6a21ec23fa9fd86e05) chore: fix typos
- [`4f80b97`](https://github.com/talos-systems/crypto/commit/4f80b976b640d773fb025d981bf85bcc8190815b) fix: verify CSR signature before issuing a certificate
- [`1292574`](https://github.com/talos-systems/go-blockdevice/commit/1292574643e06512255fb0f45107e0c296eb5a3b) fix: make disk type matcher parser case insensitive
- [`b77400e`](https://github.com/talos-systems/go-blockdevice/commit/b77400e0a7261bf25da77c1f28c2f393f367bfa9) fix: properly detect nvme and sd card disk types
- [`c6d0ae2`](https://github.com/talos-systems/go-debug/commit/c6d0ae2c0ee099fa0940405401e6a02716a15bd8) fix: linters and CI
- [`c78cc95`](https://github.com/talos-systems/go-retry/commit/c78cc953d9e95992575305b4e8648392c6c9b9e6) fix: implement `errors.Is` for all errors in the set
- [`d3a32be`](https://github.com/talos-systems/go-smbios/commit/d3a32bea731a0c2a60ce7f5eae60253300ef27e1) fix: return UUID in middle endian only on SMBIOS >= 2.6
- [`b0d9cd2`](https://github.com/talos-systems/pkgs/commit/b0d9cd2c36e37190c5ce7b85acea6a51a853faaf) fix: build `zbin` utility for both amd64 and arm64

### 0.11.4

- [`64259fd0a`](https://github.com/talos-systems/talos/commit/64259fd0ad431a6ad475f36cd655f73295493e7d) fix: preserve PMBR bootable, align partitions with minimal I/O size
- [`7776057`](https://github.com/talos-systems/crypto/commit/7776057f5086157873f62f6a21ec23fa9fd86e05) chore: fix typos
- [`4f80b97`](https://github.com/talos-systems/crypto/commit/4f80b976b640d773fb025d981bf85bcc8190815b) fix: verify CSR signature before issuing a certificate
- [`2ec0c3c`](https://github.com/talos-systems/go-blockdevice/commit/2ec0c3cc0ff5ff705ed5c910ca1bcd5d93c7b102) fix: preserve the PMBR bootable flag when opening GPT partition
- [`1292574`](https://github.com/talos-systems/go-blockdevice/commit/1292574643e06512255fb0f45107e0c296eb5a3b) fix: make disk type matcher parser case insensitive
- [`b77400e`](https://github.com/talos-systems/go-blockdevice/commit/b77400e0a7261bf25da77c1f28c2f393f367bfa9) fix: properly detect nvme and sd card disk types
- [`c6d0ae2`](https://github.com/talos-systems/go-debug/commit/c6d0ae2c0ee099fa0940405401e6a02716a15bd8) fix: linters and CI
- [`c78cc95`](https://github.com/talos-systems/go-retry/commit/c78cc953d9e95992575305b4e8648392c6c9b9e6) fix: implement `errors.Is` for all errors in the set
- [`d3a32be`](https://github.com/talos-systems/go-smbios/commit/d3a32bea731a0c2a60ce7f5eae60253300ef27e1) fix: return UUID in middle endian only on SMBIOS >= 2.6
- [`b0d9cd2`](https://github.com/talos-systems/pkgs/commit/b0d9cd2c36e37190c5ce7b85acea6a51a853faaf) fix: build `zbin` utility for both amd64 and arm64

### 0.11.5

- talos-systems/talos@218f24a1b fix: update go-blockdevice
- talos-systems/go-blockdevice@fe24303 fix: perform correct PMBR partition calculations


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.11.5**, the newest release recorded here for this line.

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
