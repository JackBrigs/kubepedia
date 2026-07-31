---
id: TROUBLE-TALOS_1_13_DEFECTS
type: troubleshooting
title: "talos 1.13: defects fixed in the 1.13 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.13.0 <1.14.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.13 known issues
  - talos 1.13 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.13 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.13: defects fixed in the 1.13 line

## Summary

**241 defects** the project fixed across **6 releases** of the 1.13 line, from 1.13.0 to
1.13.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.13.0

- siderolabs/talos@5e2fc260a fix: revert add extraArgs from service-account-issuer
- siderolabs/talos@17448fcd2 fix: revert use append instead of prepend in service-account-issuer
- siderolabs/talos@e9afea74d test: fix OOM test flake
- siderolabs/talos@d34a61c8d fix(talosctl): ensure uncordon runs after reboot/upgrade errors
- siderolabs/talos@f9531d352 test: fix a flake in the manifest sync test
- siderolabs/talos@9f04f2c4e fix: watch kubelet's kubeconfig and time out for cache sync
- siderolabs/talos@d4d018b54 fix: propagate route table down to the resource
- siderolabs/talos@8035e6e49 fix: do not flip machine stage to rebooting during shutdown
- siderolabs/talos@10606bdfe fix: boot entry detection
- siderolabs/talos@23393a5ea fix: zfs extensions test
- siderolabs/talos@a922d1540 fix: return failed precondition on upgrade when not installed
- siderolabs/talos@252799a00 fix: reduce memory dashboard usage
- siderolabs/talos@8180cb11c fix: wrong slot of encryption key was logged
- siderolabs/talos@370c035ab fix: audit trustd code for security
- siderolabs/talos@929ab7165 fix(machined): clear stale bond ARP/NS targets on decode
- siderolabs/talos@41e6866fd fix: encode extra args fields in resources with new id
- siderolabs/talos@53609713f fix: upgrade API in maintenance mode (legacy)
- siderolabs/talos@9b8c1891b fix: panic in reading PCR values
- siderolabs/talos@77406ec31 fix: validate hostDNS forwarding requires hostDNS to be enabled
- siderolabs/talos@7d7776dca fix: handle boot failure
- siderolabs/talos@6dc97e8aa fix(talosctl): always use default GRPC dial options
- siderolabs/talos@db2c007ee fix: create correct blackhole routes for IPv4
- siderolabs/talos@cd8d70fb9 fix: set the minimum TLS version to 1.3
- siderolabs/talos@9be7bc025 fix: don't set xattrs while decompressing extensions
- siderolabs/talos@02d84f582 fix: handle ISOs with zeroes in volume labels
- siderolabs/talos@8499579f4 fix: add os:meta:writer role to the dashboard
- siderolabs/talos@dc59a7e94 fix: drop talosctl install
- siderolabs/talos@a47b76618 fix: unseal with "slow" TPM
- siderolabs/talos@3c79b432a fix: drop unused type from ExternalVolume schema
- siderolabs/talos@38d391e9d fix: always grow disks
- siderolabs/talos@f0c5cb517 fix: add metal-agent mode to runtime capabilities
- siderolabs/talos@fcdfeab2b fix: incorrect route source for on-link routes
- siderolabs/talos@ccf1e0c27 test: fix the PKI mismatch test flake
- siderolabs/talos@7a9467306 test: fix cron failures for provision-1 & provision-2
- siderolabs/talos@797815209 fix: allow blockdevice wipe in maintenance mode
- siderolabs/talos@efc76f0bf test: fix the flakes in tests with trusted roots
- siderolabs/talos@b86360790 fix: add symlinks nvidia-ctk and nvidia-cdi-hook in /usr/bin
- siderolabs/talos@d82fada75 fix: unset rlimits for extension services
- siderolabs/talos@1cb2a8b30 fix: update diff library to v1.0.1
- siderolabs/talos@5e171a3de test: fix the apid test against AWS/GCP
- siderolabs/talos@f98e76f8d fix: panics in diff algorithms
- siderolabs/talos@13d6b4a03 fix: trim down cosign dependencies
- siderolabs/talos@5c39a8581 fix: drop aws & azure KMS APIs from the machined build
- siderolabs/talos@3d059754c fix: accept image cache volume encryption config
- siderolabs/talos@d2661d253 fix: apparmor parser config files
- siderolabs/talos@13ef0cfc9 fix: unmount pseudo-late recursively
- siderolabs/talos@e9d45671a fix: panic in hardware.SystemInfoController
- siderolabs/talos@a728bbd89 fix: validate missing apiVersion in config document decoder
- siderolabs/talos@c8a674afa fix: pull in a fix for dmesg timestamps
- siderolabs/talos@cff0f5782 fix(machined): support USERDATA legacy fallback in OpenNebula driver
- siderolabs/talos@4f4ec9806 fix(machined): align OpenNebula hostname precedence with reference
- siderolabs/talos@ae61f5a5e fix(machined): use ParseFQDN for hostname parsing in OpenNebula
- siderolabs/talos@ad3c59aad fix: prevent stale discovered volumes reads
- siderolabs/talos@ee53a18c8 fix: stop pulling wrong platform for images
- siderolabs/talos@17335107b fix: use non-sensitive resource for health check precondition
- siderolabs/talos@57599fb87 fix: skip some readiness checks when the CNI is disabled
- siderolabs/talos@720a2148a fix: correctly calculate end ranges for nftables sets
- siderolabs/talos@95287d2db fix: environment suite failures
- siderolabs/talos@55b872185 fix: use correct dhcp option for unicast dhcp renewal
- siderolabs/talos@0ab84c2a1 fix: ignore image digest when doing upgrade-k8s
- siderolabs/talos@0bb6413ff fix: do not fail on RO virtiofs
- siderolabs/talos@ad29417ae fix(machined): opennebula: process ETH*_ vars regardless of NETWORK context flag
- siderolabs/talos@cc636f1dd fix: image cache test fails with 'no space left on device'
- siderolabs/talos@c1d0a3360 fix: patch with delete for LinkConfigs
- siderolabs/talos@7cf1de279 fix: bring in new version of go-cmd and go-blockdevice
- siderolabs/talos@c8800b41e fix: update path handling on talosctl cgroups
- siderolabs/talos@5baa0028e fix: add owning inventory annotation to talos manifests
- siderolabs/talos@d3e793d14 fix: stop Kubernetes client from dynamically reloading the certs
- siderolabs/talos@f018fbe7b fix: handle raw encryption keys with `\n` properly
- siderolabs/talos@e5b0eb017 fix: hold user volumes root mountpoint
- siderolabs/talos@a59db0e92 fix: improve OpenStack bare metal network configuration reliability
- siderolabs/talos@659009ad8 fix: remove stale endpoints
- siderolabs/talos@dab0d4783 fix: allow static hosts in `/etc/hosts` without hostname
- siderolabs/talos@35ad0448c fix: switch to better Myers algorithm implementation
- siderolabs/talos@5df10f260 fix: use mcopy instead of diskfs to populate VFAT
- siderolabs/talos@ce53ffa90 fix: disks flag parsing and handling in create qemu command
- siderolabs/talos@3bd3dd7ca fix: memory overuse in imager VFAT
- siderolabs/talos@f118ee47e fix: read multi-doc machine config with newer talosctl
- siderolabs/talos@daf18abf4 fix: fix talosctl debug in enforcing mode
- siderolabs/talos@33b5b2565 fix: ignore volumes in wave calculation without provisioning
- siderolabs/talos@7942d5a98 fix: image gc controller config
- siderolabs/talos@2628eb2ec fix: typo with rpi_5 profile name
- siderolabs/talos@d5ebcd7ca fix: stop building talosctl debug on Windows
- siderolabs/talos@d905035b5 fix: swap volume configuration for min/max size
- siderolabs/talos@1fec5b23d fix: implement merger for PercentageSize
- siderolabs/talos@e48c6d7ab fix: allow to expose a port multiple times in Docker
- siderolabs/talos@410d8cb57 fix: undo CRLF on Windows (talosctl edit)
- siderolabs/talos@0bd48bbc6 fix(talosctl): pass --k8s-endpoint flag to rotate-ca kubernetes rotation
- siderolabs/talos@6aa9b0677 fix: skip empty documents on config decoding
- siderolabs/talos@494492489 fix: always set advertised peer URLs
- siderolabs/talos@782cc507d fix: open the filesystem as read-only
- siderolabs/talos@28e61a740 fix: set GRUB prefix correctly on arm64
- siderolabs/talos@562920701 fix: use node podCIDRs for kubespan advertiseKubernetesNetworks
- siderolabs/talos@417209512 fix: fallback to /proc/meminfo for memory modules
- siderolabs/talos@7f1147bed fix: add warnings to 802.3ad bond
- siderolabs/talos@c7aa266ea fix: overwrite resolver config with machine config
- siderolabs/talos@cf70f05fa fix: oracle platform file format
- siderolabs/talos@77bc3d21f fix: marshal of FailOverMac property
- siderolabs/talos@38e280c93 fix: make OOM expression a bit less sensitive
- siderolabs/talos@3d1301640 fix: wipe the first/last 1MiB in addition to wiping by signatures
- siderolabs/talos@1aa6528ad fix: make OOM controller more precise by considering separate cgroup PSI
- siderolabs/talos@f7072c050 fix: check if the device is not mounted when wiping
- siderolabs/talos@743c3b94b fix: use correct containerd import path
- siderolabs/talos@72fe98a06 fix: boot with GRUB
- siderolabs/talos@d4ed13d93 fix: add talos version to Hetzner Cloud client user agent
- siderolabs/talos@01a367891 fix: use append instead of prepend in service-account-issuer
- siderolabs/talos@96e604874 fix: add hostname to endpoints
- siderolabs/talos@71adaf0ea fix: sort mirrors and tls configs when generating the machine config
- siderolabs/talos@5127ef7c2 fix: wipe disk by signatures
- siderolabs/talos@415bfaedb fix: panic in configpatcher when the whole section is missing
- siderolabs/talos@e5aca71cd fix: fix healthcheck timeout
- siderolabs/talos@308c75090 fix: resolve SideroLink Wireguard endpoint on reconnect
- siderolabs/talos@e4ef494de fix: drop the persist config flag from gen config
- siderolabs/talos@b8ff9677e fix: handle correctly incomplete RegistryTLSConfig
- siderolabs/talos@99f2ddada fix: bond config via platform
- siderolabs/talos@2449ffea4 fix: allow HostnameConfig to be used with incomplete machine config
- siderolabs/talos@35fc52087 fix: lock down etcd listen address to IPv4 localhost
- siderolabs/talos@c9d84ae21 fix: generate OCI-compliant image config
- siderolabs/talos@7a4b2b33a fix: update VIP config example
- siderolabs/talos@b764f5f72 fix: skip sync test when kube-proxy is disabled
- siderolabs/talos@7416dca59 fix: print talosctl images to release notes
- siderolabs/talos@154952175 fix: disable swap for system services
- siderolabs/talos@d98b415af fix: drop more non-overlay SBC stuff
- siderolabs/talos@226cd6bc1 fix: do not allocate for the actual disk image file
- siderolabs/talos@53f5bf8d2 fix: overlay installers
- siderolabs/talos@10d0cfd93 fix: overlay install in image mode
- siderolabs/talos@77086694d fix: partition data population
- siderolabs/talos@4d5657b1a fix: drop SBC board code
- siderolabs/talos@c57701d65 fix: remove interactive installer
- siderolabs/talos@f09ae1e0d fix: probe small images correctly
- siderolabs/talos@0fb50dbd0 fix: invalid versions check in talos-bundle
- siderolabs/talos@3dfa4d6e4 fix: make upgrade work with SELinux enforcing=1
- siderolabs/talos@536541afe fix: mount volume mount/unmount race
- siderolabs/talos@f0f420725 fix: bond setting change detection
- siderolabs/talos@0592ff0cd fix: drop the Omni API URL check on IP address
- siderolabs/talos@884e76662 docs: fix the talosctl cluster create help output
- siderolabs/talos@6dc31be4f fix: exclude new Virtual IPs configured with new config
- siderolabs/talos@f871ab241 fix: provide json support in `nft` binary
- siderolabs/talos@39feb16d2 fix: update containerd 2.2.0 with cgroups patch
- siderolabs/talos@82027eb9b fix: bond configuration with new settings
- siderolabs/talos@121b13b8f fix: disable kexec on arm64
- siderolabs/talos@7eaa725d0 fix: selection of boot entry
- siderolabs/talos@798143a88 fix: discard better klog message from Kubernetes client
- siderolabs/talos@008cd0986 fix: disable kexec in talosctl cluster create on arm64
- siderolabs/talos@e387e48b3 fix: do not override DNS on MacOS
- siderolabs/talos@1e7e87fb1 fix: rework NFT rules for KubeSpan
- siderolabs/talos@f301e3e9b fix: update KubeSpan MSS clamping
- siderolabs/talos@d347ca1af fix: update CNI plugins to 1.9.0
- siderolabs/talos@ba13b6786 fix: correct condition to use UKI cmdline in GRUB
- siderolabs/talos@13df94388 fix: adapt SELinuxSuite.TestNoPtrace to new strace version
- siderolabs/talos@861787c38 fix: mark secureboot as supported for metal
- siderolabs/talos@04e3e87ad fix: clean up kubelet mounts
- siderolabs/talos@21057903a fix: clear provisioning data on SideroLink config change
- siderolabs/talos@d4309d7b1 fix: add a timeout for DNS resolving for NTP
- siderolabs/talos@cc95562bc fix: don't disable LACP by default
- siderolabs/talos@5a03a7a20 chore: fix longhorn test
- siderolabs/talos@51b732bea fix: selection of boot entry
- siderolabs/talos@87ff9f860 test: fix the image-factory test to pass IF endpoint
- siderolabs/talos@2f42202a7 fix: simplify OOM expression
- siderolabs/talos@7b06ae8c2 test: fix flaky LinkSpec/Wireguard test
- siderolabs/talos@e2ee39b8a fix: support specifying patch file without '@' symbol
- siderolabs/talos@e202b1f9e fix: trim trailing dots from certificate SANs
- siderolabs/talos@7f7079f9c fix: assign value of multicast setting properly
- siderolabs/talos@a89108995 fix: add CA subject to generated certificate
- siderolabs/talos@35dd612a5 fix: add more resilient move
- siderolabs/talos@eeded98f5 fix: add riscv64 talosctl to release artifacts
- siderolabs/talos@a6bbae91b fix: fix typos across the project
- siderolabs/crypto@6d82f0c fix: bump minimum TLS version to v1.3
- siderolabs/go-kubernetes@92163c3 fix: set a the context logger
- siderolabs/go-kubernetes@8e6f068 fix: bring back legacy sync
- siderolabs/go-kubernetes@de675a0 fix: stop using custom dialer for Kubernetes client
- siderolabs/go-kubernetes@3bea212 fix: use new Myers diff algorithm
- siderolabs/go-talos-support@387b869 fix: marshal Talos resources as YAML
- siderolabs/go-talos-support@5e0155f fix: add trailing new line when writing to logger
- siderolabs/pkgs@b121566 fix: support disabling module signature verification
- siderolabs/pkgs@46c12db fix: libarchive install prefix
- siderolabs/pkgs@4f784de fix: install apparmor parser require config files
- siderolabs/pkgs@77194e4 fix: disable CONFIG_RT_GROUP_SCHED
- siderolabs/pkgs@6ca02b3 fix: make udev rules read only
- siderolabs/pkgs@30bc671 fix: enable pinctrl for Raspberry Pi 5
- siderolabs/pkgs@59241bd fix: add SBOMs for pigz/igzip
- siderolabs/pkgs@47abca0 fix: add json support to nftables binary
- siderolabs/pkgs@b961ff8 feat: patch containerd 2.2.0 with cgroups fix patch
- siderolabs/pkgs@8b6ae5b fix: regenerate configs
- siderolabs/pkgs@2992598 fix: add missing kernel config entries
- siderolabs/tools@2b3f514 fix: reproducible build for nasm
- siderolabs/tools@896f8b9 fix: add sbom for zlib-ng
- siderolabs/tools@da96a27 chore: rekres to fix reproducibility

### 1.13.3

- siderolabs/talos@01b434870 fix: guard apply config API call
- siderolabs/talos@d62d54ca7 fix: memorymodules resource reporting
- siderolabs/talos@b673b4be7 fix: bump Go golang.org/x modules
- siderolabs/talos@532bc6baa fix: relax hostname config validation
- siderolabs/talos@3bbd3ed35 fix: bump Kubernetes to 1.36.1 in one more place
- siderolabs/talos@6d53ce0d5 chore(ci): fix cloud image upload job name
- siderolabs/talos@5633c7791 fix: rework how scheduler config is marshaled
- siderolabs/talos@52f056084 fix: restore some shared (and some lower tier slave) mount propagation
- siderolabs/talos@9de3c12d9 fix: image verification issue with registry.k8s.io
- siderolabs/talos@e99744bad fix: update containerd to 2.2.4
- siderolabs/pkgs@b3dd525 fix: macb silent TX stall on BCM2712/RP1 (v2 patches from netdev)

### 1.13.4

- siderolabs/talos@27d7a1985 fix: handle cluster-scoped resources with a namespace correctly
- siderolabs/talos@f44cafbcd fix: recreate dns server and listeners on host DNS runner restart
- siderolabs/talos@5ed296b76 fix: marshal kube-scheduler config correctly with int types
- siderolabs/talos@5992015b0 fix: machine configuration schemas
- siderolabs/talos@b8dfda7ee fix: mark more resources as sensitive
- siderolabs/talos@7c0900b85 fix(ci): aws nvidia tests
- siderolabs/talos@cf62af3e2 fix: etcd client leak in the (legacy) Upgrade API
- siderolabs/talos@c83dad3c5 fix: health request server-side
- siderolabs/talos@577cc6f6c fix: bring in a change to BCM2712_MIP
- siderolabs/talos@29da68ae2 fix: touch rootfs files with SOURCE_DATE_EPOCH
- siderolabs/talos@b19a03bc2 fix: ignore cgroups with zero rank in OOM handler
- siderolabs/go-kubernetes@131a2bd fix: handle cluster-scoped resources with a ns correctly
- siderolabs/pkgs@54ec9fc fix: disable PAGE_TABLE_CHECK_ENFORCED in kernel config
- siderolabs/pkgs@366f575 fix: enable CONFIG_BCM2712_MIP as built-in in arm64 kernel config

### 1.13.5

- siderolabs/talos@c5089c655 fix: bump number of open files for etcd
- siderolabs/talos@e0b4d9d75 fix: stop the log persistence and close all files on shutdown
- siderolabs/talos@23a080dcf fix: honor FailurePauseTimeout when pausing before reboot
- siderolabs/talos@9adc63a32 fix: correct the link alias condition
- siderolabs/talos@765f0a1dc fix: relax LUKS header validation
- siderolabs/talos@f0a5842ab fix: update go.mod and rekres
- siderolabs/pkgs@7ede376 fix: avoid page_table_check BUG on time namespace VVAR page

### 1.13.6

- siderolabs/talos@31552f400 fix: shutdown/reboot via usermode helpers
- siderolabs/talos@bc0c3f3d3 fix: flaky serviceaccount suite test
- siderolabs/talos@fbe4d900d fix: data race in manifest sync
- siderolabs/talos@6df3a452b fix: provide cooldown period for the QoS trigger
- siderolabs/talos@85f8dd63e fix: decode extraArgs list values correctly
- siderolabs/talos@c2a56d592 fix: kubelet stuck restarting
- siderolabs/talos@3e37ef8cd fix: handle image cache being disabled
- siderolabs/talos@466bcd804 fix: align documented image cache partition label
- siderolabs/talos@d3cf09bcb fix: image verification with referrers
- siderolabs/gen@c526410 fix: skip unknown-key check for types with custom YAML unmarshaler
- siderolabs/pkgs@389b8aa fix: patch Linux kernel for tunnel metadata buffer overflow

### 1.13.7

- siderolabs/talos@202dc152a fix: add ca-certificates to talosctl
- siderolabs/talos@a4c1e6eb4 fix: oom podruntime protection
- siderolabs/talos@58a78fe22 fix: use symlinks for init aliases
- siderolabs/talos@428872bf4 fix: do proper backoff for NTP Kiss-of-Death responses
- siderolabs/talos@576638def fix: make audit restartable
- siderolabs/talos@76328f941 fix: avoid image cache mount request churn
- siderolabs/talos@0d752e784 fix: provide correct handler for Ctrl-Alt-Delete sequence
- siderolabs/talos@fe9d33095 fix: terminate log persistence a bit harder
- siderolabs/talos@a155bad1b fix: do not block volume lifecycle teardown on failed user volumes
- siderolabs/pkgs@971fd23 fix: enable CONFIG_IFB as a module


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.13.7**, the newest release recorded here for this line.

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
