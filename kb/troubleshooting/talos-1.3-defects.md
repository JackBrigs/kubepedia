---
id: TROUBLE-TALOS_1_3_DEFECTS
type: troubleshooting
title: "talos 1.3: defects fixed in the 1.3 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.3.0 <1.4.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.3 known issues
  - talos 1.3 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.3 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.3: defects fixed in the 1.3 line

## Summary

**190 defects** the project fixed across **8 releases** of the 1.3 line, from 1.3.0 to
1.3.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.3.0

- siderolabs/talos@c9c15b6dd fix: allow empty dnsDomain in machine config
- siderolabs/talos@c48856a6c fix: ignore k8s additional addresses if nil
- siderolabs/talos@66feeeccd fix: don't report link name in route statuses
- siderolabs/talos@0bdec81ca fix: fix nil pointer panic and incorrect error output
- siderolabs/talos@bce132f14 fix: workaround panic in the kubelet service controller
- siderolabs/talos@e47e74452 fix: add ext4 filesystem detection
- siderolabs/talos@810a550f1 fix: report errors to Equinix Metal event API
- siderolabs/talos@1f382d8f7 fix: use only kube-apiserver endpoints for Talos API access endpoints
- siderolabs/talos@89882dd2d fix: introduce 'overridePath' setting and fix Talos resolver
- siderolabs/talos@1e520afbb fix: ignore many more filesystems in IMA
- siderolabs/talos@2964b9327 fix: correctly handle new watch event types
- siderolabs/talos@4a052eadf fix: disable kexec on upgrades from pre-BTF kernel
- siderolabs/talos@732c459ec fix: parse and apply DHCP settings properly from cmdline
- siderolabs/talos@a9e9d71b2 fix: parse correctly upgrade cmd force flag
- siderolabs/talos@c54bea128 fix: don't publish external IPs as affiliate addresses
- siderolabs/talos@54d9032ce test: fix log streaming for conformance tests
- siderolabs/talos@6430ce1ef fix: limit SideroLink Wireguard link MTU to 1280
- siderolabs/talos@5bfd7dbfa test: fix assertion on reboot test
- siderolabs/talos@e1590ba7b fix: lifecycle action tracking
- siderolabs/talos@03a20da9d fix: filter up duplicate IPs out of NodeAddresses
- siderolabs/talos@0301bbe93 fix: check if processes is nil to avoid panic
- siderolabs/talos@0b41923c3 fix: restore the StaticPodStatus resource
- siderolabs/talos@3333cd93c fix: generate correct Flannel config for IPv6-only clusters
- siderolabs/talos@8b4ae08d1 fix: etcd snapshot command on Windows
- siderolabs/talos@7e50e24c0 fix: properly cleanup legacy static pod manifests directory
- siderolabs/talos@6ee47bcc6 fix: support serving config for qemu launcher on IPv6
- siderolabs/talos@4ea3b99b5 fix: serve static pod files on 127.0.0.1 instead of localhost
- siderolabs/talos@aa3d9b4ca fix: regenerate cert on node labeling retry
- siderolabs/talos@021c73c35 fix: lowercase nodename
- siderolabs/talos@dc70d892a fix: support setting KubeSpan link MTU
- siderolabs/talos@d210338e3 fix: skip protobuf full unmarshaling for some talosctl commands
- siderolabs/talos@993743f63 fix: skip hostname via DHCP on OpenStack platform
- siderolabs/talos@63de93722 fix: update go-smbios to v0.3.1
- siderolabs/talos@1c43c72ae docs: fix talos required kernel params
- siderolabs/talos@23c9ea46b fix: raspberry pi install
- siderolabs/talos@8b2235c3b fix: lookup Equinix Metal bond slaves using 'permanent addr'
- siderolabs/talos@c90e20251 fix: kubeconfig permission
- siderolabs/talos@357b770cb fix: cryptsetup delete slot
- siderolabs/talos@711128839 fix: continue applying bootstrap manifests on some errors
- siderolabs/talos@18e041f1e docs: fix typo in patching example
- siderolabs/talos@13fdfaffc test: fix up default branch name
- siderolabs/talos@aade73643 docs: fix missing variable in OpenEBS docs
- siderolabs/talos@015535d90 fix: update discovery client with the redirect fix
- siderolabs/talos@94b088f02 fix: set etcd options consistently
- siderolabs/talos@92ae7ef4b fix: fix protoenc encoding for enums and types with custom encoders
- siderolabs/talos@7b270ff33 test: fix api controller test
- siderolabs/talos@2dadcd669 fix: stop worker nodes from acting as apid routers
- siderolabs/talos@9eaf33f3f fix: never sign client certificate requests in trustd
- siderolabs/talos@f424e5340 fix: stop containers more thoroughly
- siderolabs/talos@3a67c42cb fix: kill the task processes when cleaning up stale task
- siderolabs/talos@9beee92e7 docs: fix double vv in Kubernetes version
- siderolabs/talos@688272515 fix: use different username for Talos Kubernetes API access
- siderolabs/talos@9dadc4a59 fix: include all node addresses into etcd cert SANs
- siderolabs/talos@9df8f1ff1 fix: list COSI APIs for the apid authenticator
- siderolabs/talos@31462450f fix: pass a pointer to specs.Mount into protoenc.Marshal
- siderolabs/talos@6472ae00b fix: automatically discard VIPs for etcd advertised addresses
- siderolabs/talos@36c1f1d6e fix: flip the client-server version check
- siderolabs/talos@0847400f7 fix: prevent panic on health check if a member has no IPs
- siderolabs/talos@353154281 fix: drop kube-system SA default binding
- siderolabs/talos@b2fec3c97 fix: properly handle `configContext` being `nil` in Talos client
- siderolabs/talos@1c0977b3a fix: change the type of returned gRPC connection object from the client
- siderolabs/talos@41848e421 fix: expose Talos client gRPC connection via the function `Conn`
- siderolabs/talos@d283aba3a test: fix cli reboot test
- siderolabs/talos@072349812 fix: update COSI to the version with gRPC Wait fix
- siderolabs/talos@89d57aa81 fix: always abort the maintenance service
- siderolabs/talos@f6fa74619 fix: limit apid backoff max delay
- siderolabs/talos@d7ef346db fix: get command in the case 'nodes' are not set in the context
- siderolabs/talos@4e9c32256 fix: correctly render hosts.toml with multiple endpoints
- siderolabs/talos@053af1d59 fix: update etcd certificates when node addresses changes
- siderolabs/talos@361e85b74 fix: properly read kexec disabled sysctl
- siderolabs/talos@2f2d97b6b fix: don't wait for the hostname in maintenance mode
- siderolabs/talos@a0d94be30 fix: stable default hostname bias
- siderolabs/talos@7d43fc79b fix: make 'ca', 'crt' and 'key' flags optional for 'talosctl config add'
- siderolabs/talos@fd467e02c fix: handle grub config being empty in the `Revert` function
- siderolabs/talos@9492aca65 fix: clean up `cancelCtxMu` leftovers in PriorityLock
- siderolabs/talos@61e3eb2ea fix: talosctl edit mc loop
- siderolabs/talos@32db7a7f5 fix: surround `cancelCtx` with the mutex
- siderolabs/crypto@6fa2d93 fix: deepcopy nil fields as `nil`
- siderolabs/crypto@9a63cba fix: add back support for generating ECDSA keys with P-256 and SHA512
- siderolabs/crypto@893bc66 fix: use SHA256 for ECDSA-P256
- siderolabs/crypto@4f80b97 fix: verify CSR signature before issuing a certificate
- siderolabs/crypto@cf75519 fix: function NewKeyPair should create certificate with proper subject
- siderolabs/crypto@d0c3eef fix: implement NewKeyPair
- siderolabs/discovery-client@230f317 fix: reconnect the client on update failure
- siderolabs/gen@b3b6db8 fix: fix Copy documentation and implementation
- siderolabs/gen@726e066 fix: rename tuples.go to pair.go and set proper package name
- siderolabs/go-blockdevice@9c4af49 fix: cryptsetup remove slot
- siderolabs/go-blockdevice@fccee8b chore: rekres the source, fix issues
- siderolabs/go-blockdevice@b374eb4 fix: align partition to 1M boundary by default
- siderolabs/go-blockdevice@ec428fe fix: lookup filesystem labels on the actual device path
- siderolabs/go-blockdevice@15b182d fix: return partition table not exist when trying to read an empty dev
- siderolabs/go-blockdevice@b9517d5 fix: resize partition
- siderolabs/go-blockdevice@70d2865 fix: try to find cdrom disks
- siderolabs/go-blockdevice@667bf53 fix: revert gpt partition not found
- siderolabs/go-blockdevice@d7d4cdd fix: gpt partition not found
- siderolabs/go-blockdevice@33afba3 fix: also open in readonly mode when running `All` lookup method
- siderolabs/go-blockdevice@d981156 fix: allow Build for Windows
- siderolabs/go-blockdevice@fe24303 fix: perform correct PMBR partition calculations
- siderolabs/go-blockdevice@2ec0c3c fix: preserve the PMBR bootable flag when opening GPT partition
- siderolabs/go-blockdevice@1292574 fix: make disk type matcher parser case insensitive
- siderolabs/go-blockdevice@b77400e fix: properly detect nvme and sd card disk types
- siderolabs/go-blockdevice@1d830a2 fix: revert mark the EFI partition in PMBR as bootable
- siderolabs/go-blockdevice@bec914f fix: mark the EFI partition in PMBR as bootable
- siderolabs/go-blockdevice@bb3ad73 fix: align partition start to physical sector size
- siderolabs/go-blockdevice@1cf7f25 fix: properly handle no child processes error from cmd.Wait
- siderolabs/go-blockdevice@f2728a5 fix: keep contents of PMBR when writing it
- siderolabs/go-blockdevice@2878460 fix: write second copy of partition entries
- siderolabs/go-blockdevice@943b08b fix: blockdevice reset should read partition table from disk
- siderolabs/go-blockdevice@5b4ee44 fix: ignore `/dev/ram` devices
- siderolabs/go-blockdevice@2a1baad fix: correctly build paths for `mmcblk` devices
- siderolabs/go-blockdevice@8076344 fix: return proper disk size from GetDisks function
- siderolabs/go-blockdevice@ceae64e fix: sync kernel partition table incrementally
- siderolabs/go-blockdevice@2cb9516 fix: return correct error value from blkpg functions
- siderolabs/go-blockdevice@c40dcd8 fix: properly inform kernel about partition deletion
- siderolabs/go-blockdevice@3d1ce4f fix: calculate last lba of partition correctly
- siderolabs/go-debug@c6d0ae2 fix: linters and CI
- siderolabs/go-loadbalancer@4a6e29e refactor: clean up names, fix the lingering goroutines
- siderolabs/go-procfs@16ce2ef fix: update cmdline.Set() to drop the value being overwritten
- siderolabs/go-procfs@a077c96 fix: fix go module name
- siderolabs/go-retry@c78cc95 fix: implement `errors.Is` for all errors in the set
- siderolabs/go-retry@8c63d29 fix: correctly implement error interfaces on wrapped errors
- siderolabs/go-smbios@10c1dd8 fix: check for end of the slice properly
- siderolabs/go-smbios@fd5ec8c fix: remove useless (?) goroutines leading to data race error
- siderolabs/go-smbios@d3a32be fix: return UUID in middle endian only on SMBIOS >= 2.6
- siderolabs/grpc-proxy@6dfa2cc fix: ignore errors on duplicate `SetHeader` calls
- siderolabs/grpc-proxy@b076302 fix: use io.EOF error when no backend connections are available
- siderolabs/grpc-proxy@fa6843a chore: fix spelling
- siderolabs/grpc-proxy@ca3bc61 fix: ignore some errors so that we don't spam the logs
- siderolabs/grpc-proxy@6c9f7b3 fix: allow mode to be set for each request being proxied
- siderolabs/grpc-proxy@fc0d27d More tests, small code fixes, updated README
- siderolabs/grpc-proxy@d5b35f6 Update gRPC and fix tests (#27)
- siderolabs/grpc-proxy@67591eb Break StreamDirector interface, fix metadata propagation for gRPC-Go>1.5. (#20)
- siderolabs/grpc-proxy@97396d9 Merge pull request [#11](https://github.com/siderolabs/grpc-proxy/pull/11) from mwitkow/fix-close-bug
- siderolabs/grpc-proxy@428fa1c Fix a channel closing bug
- siderolabs/grpc-proxy@af55d61 Merge pull request [#10](https://github.com/siderolabs/grpc-proxy/pull/10) from mwitkow/bugfix/streaming-fix
- siderolabs/grpc-proxy@84242c4 fix the "i don't know who finished" case
- siderolabs/grpc-proxy@9b22f41 fix full duplex streaming
- siderolabs/grpc-proxy@e5c3df5 Fix compatibility with latest grpc library
- siderolabs/grpc-proxy@52be0a5 bugfix: fix gRPC Java deadlock, due to different dispatch logic
- siderolabs/grpc-proxy@822df7d Fix reference to mwitkow
- siderolabs/net@409926a fix: parse correctly some IPv6 CIDRs
- siderolabs/pkgs@54d7e5c fix: drbd package name
- siderolabs/pkgs@f2f8333 fix: no slack notifications on failure
- siderolabs/pkgs@44579f0 fix: rollback xfsprogs to 5.18.0
- siderolabs/pkgs@e70e3c1 fix: nvidia oss pkg name
- siderolabs/pkgs@2ecd14e fix: containerd version
- siderolabs/siderolink@61ab1c4 fix: include MachineStatusEvent into the list of supported events
- siderolabs/siderolink@93b65f0 fix: ignore 'exist' error on interface managmeent
- siderolabs/siderolink@3a5be65 fix: use correct method to generate Wireguard private key
- siderolabs/siderolink@b38c192 fix: build on Windows
- siderolabs/siderolink@f7cadbc fix: handle duplicate peer updates
- siderolabs/tools@858cfe7 fix: no slack notifications on failure
- siderolabs/tools@1f00d2e fix: revert gawk to 5.1.1

### 1.3.1

- siderolabs/talos@0d11741b9 fix: oralce cloud zone
- siderolabs/talos@8a9ff259e fix: send diagnostic output to stderr consistently
- siderolabs/talos@8700457e5 fix: default the manifest namespace if not set
- siderolabs/talos@10d54686c fix: improve talosctl completion
- siderolabs/talos@ab52ab135 fix: use proper key usage for apid client certificate
- siderolabs/talos@e20e66a19 fix: redact service account key in config in RedactSecrets method
- siderolabs/pkgs@5a39853 fix: patch ipmitool IANA URL

### 1.3.2

- siderolabs/talos@c6fb80aa8 fix: report fatal sequence errors as reboots

### 1.3.3

- siderolabs/talos@921c91dd8 fix: mark DigitalOcean anchor IP as scope link
- siderolabs/talos@66725d5cd fix: unwrap gRPC errors on stop/remove pods check
- siderolabs/talos@1508d4232 fix: build correctly etcd initial cluster URL
- siderolabs/talos@2c171a33c fix: bump COSI runtime with the panic controller restart fix
- siderolabs/talos@db04c33a4 fix: handle overwriting tags in syslinux ADV
- siderolabs/talos@2782efbf2 fix: kubespan MSS clamping
- siderolabs/talos@f9353c779 fix: service restart (including extension services)
- siderolabs/talos@e04bd3b00 test: fix integration test on cp endpoint update

### 1.3.4

- siderolabs/talos@a10316e1a fix: default dns domain to 'cluster.local' in local case
- siderolabs/talos@db3086ddd fix: panic in talosctl cluster show
- siderolabs/talos@37d8d80ca fix: return proper error if download attempts time out
- siderolabs/talos@75c1f5c9a fix: correctly expand parameters in the URL
- siderolabs/talos@7f171014b fix: correctly quote and unquote strings in GRUB config
- siderolabs/talos@0a587cb29 fix: udevd healthcheck

### 1.3.5

- siderolabs/talos@fbd3d8ec4 fix: docker talosctl cluster create provisioner
- siderolabs/talos@4580b06b8 fix: dbus shutdown when it's not initialized
- siderolabs/talos@1ad06f47b fix: quote the ampersand character in GRUB config
- siderolabs/talos@97c8e2417 fix: display correct blockdevice size
- siderolabs/talos@b682cf48b fix: talosctl reboot command passing mode in wait mode
- siderolabs/go-blockdevice@8c7ea19 fix: blockdevice size is reported by Linux in 512 blocks always

### 1.3.6

- siderolabs/talos@4776c433c fix: successful ACPI shutdown in maintenance mode
- siderolabs/talos@dacbee43d fix: improve etcd leave on reset process
- siderolabs/talos@7f2d04336 fix: update go-smbios library with Hyper-V data fix
- siderolabs/go-smbios@c526764 feat: fix reading "broken" Hyper-V DMI data

### 1.3.7

- siderolabs/talos@fe76c56fe fix: correctly parse static pod phase
- siderolabs/talos@dc001d28f fix: output of `talosctl logs` might be corruped
- siderolabs/talos@422e30a2f fix: always shutdown maintenance API service
- siderolabs/talos@13456dab3 fix: use 'no block' etcd dial with multiple endpoints
- siderolabs/talos@93dfa86d7 fix: nil pointer exception in syncLink


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.3.7**, the newest release recorded here for this line.

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
