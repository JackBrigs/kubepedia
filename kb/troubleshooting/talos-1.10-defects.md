---
id: TROUBLE-TALOS_1_10_DEFECTS
type: troubleshooting
title: "talos 1.10: defects fixed in the 1.10 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.10.0 <1.11.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.10 known issues
  - talos 1.10 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.10 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.10: defects fixed in the 1.10 line

## Summary

**234 defects** the project fixed across **10 releases** of the 1.10 line, from 1.10.0 to
1.10.9. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.10.0

- siderolabs/talos@889baabb4 fix: disk image generation with image cache
- siderolabs/talos@947d4b1f9 fix: preserve kubelet image suffix
- siderolabs/talos@9ea205bc9 fix: handle encryption type mismatch
- siderolabs/talos@204fad29a fix: handle correctly changing platform network config
- siderolabs/talos@5205870c4 fix: force DNS runner shutdown on timeout
- siderolabs/talos@1f3d91462 fix: fix Gvisor tests with containerd patch
- siderolabs/talos@6576ce088 fix: set media type to OCI for image cache layer
- siderolabs/talos@bece55108 fix: extension services logging to console
- siderolabs/talos@d4b8090c1 fix: sync PCR extension with volume provisioning lifecycle
- siderolabs/talos@0671304ba fix: grub EFI mount point
- siderolabs/talos@629ea185d fix: grub efi platform install
- siderolabs/talos@c14f52dbe fix: prefer new `MountStatus` resource
- siderolabs/talos@9ef9bb95f docs: fix tabpane styling
- siderolabs/talos@445a7e1e1 test: fix NVIDIA OSS tests
- siderolabs/talos@54a167a61 fix: upgrades with bios
- siderolabs/talos@e8e7f75c7 fix: skip lvm activation if meta is not found
- siderolabs/talos@c4136c27d fix: uki boot detection
- siderolabs/talos@372c62b72 fix: handle override path for registry mirrors correctly
- siderolabs/talos@7e7804b7a fix: avoid printing terminating null byte in SELinux context
- siderolabs/talos@73c9e91c6 fix: race in the volume mount status handling
- siderolabs/talos@07a432cc5 fix: use proper read-only bind mounts in init
- siderolabs/talos@063fca6e0 fix: containerd auth hostname in the config
- siderolabs/talos@5eaaa7ffa test: fix enforcing steps in cron
- siderolabs/talos@190d34af4 fix: image cache generation on Windows
- siderolabs/talos@8f918a34e fix: upgrades with kexec
- siderolabs/talos@0a18656f8 docs: fix version in kube-proxy manual upgrade
- siderolabs/talos@44f3c7248 fix: kata extension
- siderolabs/talos@7ca5ab5e9 fix: shrink installer and imager images
- siderolabs/talos@ea0994cfe fix: kexec with smbios type 11 string
- siderolabs/talos@8e20a5d28 fix: pass /usr/etc/in-container to apid, trustd and extension containers
- siderolabs/talos@433b0237b fix: correct structprotogen example
- siderolabs/talos@6e68a522a chore: fix conformance artifact name
- siderolabs/talos@f592730d9 fix(ci): fix image cache test
- siderolabs/talos@81d1fe0f8 fix: add missing TOOLS_PREFIX for WITH_DEBUG_SHELL builds
- siderolabs/talos@3e38bf6d4 fix: ignore missing config (nocloud) via cidata
- siderolabs/talos@27a4486a8 docs: fix typo cluser -> cluster
- siderolabs/talos@11ebb1078 fix: kexec when using sd-boot
- siderolabs/talos@f9b14e784 fix: reconnect on SideroLink tunnel on/off change
- siderolabs/talos@9531c1c6d fix(ci): image-cache cron
- siderolabs/talos@b4d2e1c3c fix: typo in machinery CloudPlatforms
- siderolabs/talos@7e0475488 fix: qemu: archive cluster logs only after stopping VMs
- siderolabs/talos@dab30a8b9 fix: ensure no goroutines escape in dns controller
- siderolabs/talos@fce824e2f fix: change from "init6" to "inet6" in docs
- siderolabs/talos@f51ebd1bc chore: fix the mount cache ids in the Dockerfile
- siderolabs/talos@1259345e4 fix(ci): image-cache cron
- siderolabs/talos@c3c0d2e42 test: fix dns test in race mode
- siderolabs/talos@d4e3e957c fix(ci): fix integration tests
- siderolabs/talos@88fc6bbeb test: fix UKI preserving talos.config and image cache
- siderolabs/talos@28b5dc738 test: fix reproduciblity test
- siderolabs/talos@d79059a2c chore: fix shutdown typo in shutdown sequence
- siderolabs/talos@a3f88d2ef fix: block NodePort services with ingress firewall
- siderolabs/talos@ebfdb91b4 fix: handle dynamic HTTP proxy settings for discovery client
- siderolabs/talos@d45eaeb74 fix: correctly map link names/aliases when using VIP operator
- siderolabs/talos@468e318ba fix: multiple fixes for dashboard/no data
- siderolabs/talos@79ee304e1 chore: update enumer to a version that fixes Go 1.24 compatibility
- siderolabs/talos@7f1dd2669 fix(ci): fix integration-misc crons
- siderolabs/talos@7ce053638 fix: ignore digest part of images when checking version
- siderolabs/talos@94cf9fb84 chore: fix spurious generate failures
- siderolabs/talos@32a34791e fix: typo in Makefile target talosctl-freebsd-arm64
- siderolabs/talos@9463ac23e fix: make ingress firewall filter traffic to nodeports
- siderolabs/talos@8531d91a1 fix: blockdevice transport detection
- siderolabs/talos@ce616d93a fix: path for ca-certificates
- siderolabs/talos@f35b58779 fix: fix diff printing
- siderolabs/talos@711cf2d99 fix: ignore errors to stop pods
- siderolabs/talos@142d75483 fix: handle empty registry config
- siderolabs/talos@aa11e9abb fix: make image cache volume management less strict
- siderolabs/talos@26a62e342 docs: fix typo in Wireguard docs
- siderolabs/talos@15191aa3e fix: extract cmdline multi profile UKIs
- siderolabs/talos@5e28c8e03 fix: image cache volume provisioning
- siderolabs/talos@270ffb69a fix: duplicate qemu drive ids
- siderolabs/talos@71ec41be1 fix: build of Talos on non-Linux host
- siderolabs/talos@e2aa7c98c fix: installer with SecureBoot should contain UKIs
- siderolabs/talos@3a2d9867b fix: do not close client.Client.conn with finalizer
- siderolabs/talos@b7165615f fix: use local NTP for AWS platform
- siderolabs/talos@673ca4bcb fix: ensure proper closure of client.Client.conn with finalizer
- siderolabs/talos@19040ffd6 fix: handle of PE sections with duplicate names
- siderolabs/talos@edf7c3288 fix: pe uki extract
- siderolabs/talos@baf81cd49 fix(ci): k8s integration suite wait for resource
- siderolabs/talos@f407c88e4 fix(ci): wait for longhorn node resource
- siderolabs/talos@a8d84e315 docs: fix typos and add more explanations in docs
- siderolabs/talos@3a384240e fix: invalid date field in iqn/nqn
- siderolabs/talos@689ea1dbf fix: bring back disk UUID
- siderolabs/talos@7a712fad2 fix: disks with 4k sector size and systemd-boot
- siderolabs/talos@33c7f4195 docs: fix typo an MacOS to on MacOS
- siderolabs/talos@0b7fc7cdf fix: abort node watch on hostname change
- siderolabs/talos@399d53b54 fix: ignore forbidden error when waiting for pod eviction
- siderolabs/talos@8dea57a81 fix: make etc binds read-only
- siderolabs/talos@4310b290d fix: generate UKI only if actually needed
- siderolabs/talos@da2e81120 fix: add informer resync period for node status watcher
- siderolabs/talos@e41a99525 fix: kube-apiserver authorizers order
- siderolabs/talos@8de19758d fix: a couple of imager panics/crashes
- siderolabs/talos@5bc3e34cb fix: detect GPT before ZFS
- siderolabs/talos@edf5c5e29 fix: extfs repair and resize
- siderolabs/talos@6e32ea5b7 fix: merge of VolumeConfig documents with sizes
- siderolabs/talos@bbd6067d4 fix: partition alignment on disks with 4k sectors
- siderolabs/talos@84fcc976f fix: yet another dashboard panic
- siderolabs/talos@6d605fc85 fix: disable NRI plugin in a different way
- siderolabs/talos@499695e24 fix: request previous IP address in discovery
- siderolabs/talos@0abb3dabf docs: fix command to wait for ceph-rook HEALTH_OK
- siderolabs/talos@ae6d065be fix: mount selinuxfs only when SELinux is enabled
- siderolabs/talos@01bf8449b fix: update field name for bus path disk selector
- siderolabs/talos@e915c98d5 fix: exclude disks with empty transport for disk selector
- siderolabs/talos@418945444 fix: build of talosctl on non-Linux platforms
- siderolabs/talos@f98efb333 fix: ignore member not found error on leave cluster
- siderolabs/talos@b72bda0a4 fix: talosctl support and race tests
- siderolabs/talos@5dc15e8db fix: update go-blockdevice to v2.0.9
- siderolabs/talos@5f3acd0f2 fix: use correct default search domain
- siderolabs/talos@7e5d36d46 fix: pci driver rebind config validation
- siderolabs/talos@4b97bbc3f fix: pull in containerd CNI deadlock fix
- siderolabs/talos@066480722 test: fix apparmor tests
- siderolabs/talos@82ea44a6b fix: reduce installer image
- siderolabs/talos@78b3e7f4f fix: get next rule number for IPv6 in the appropriate chain
- siderolabs/talos@675854aa0 docs: fix two typos
- siderolabs/talos@bd85bd5b7 fix: fix `Failed to initialize SELinux labeling handle` udev error
- siderolabs/talos@4c3261626 docs: fix several typos
- siderolabs/talos@fb3675321 fix: dashboard crash on CPU data
- siderolabs/talos@cee6c60a0 fix: make talosctl time work with PTP time sync
- siderolabs/talos@8003536c7 fix: restore previous disk serial fetching
- siderolabs/talos@5bfd829bf docs: fix 'containter' typo
- siderolabs/talos@0ef19171f fix: renovate typo
- siderolabs/talos@c568adc7d fix: renovate config
- siderolabs/talos@ec2e24fd9 fix: match MAC addresses case-insensitive (nocloud)
- siderolabs/talos@c9c685150 fix: node identity flip
- siderolabs/talos@ab5bb6884 fix: generate and serve registries with port
- siderolabs/talos@58236066d fix: support image cache on VFAT USB stick
- siderolabs/talos@e193a5071 fix: image cache integration test
- siderolabs/talos@08ee400fd test: fix flaky test NodeAddressSort
- siderolabs/talos@ef8c3e3b3 docs: fix typo in multus.md
- siderolabs/talos@d54414add fix: authorization config gen
- siderolabs/talos@470b75563 fix: use mtu network option for podman
- siderolabs/talos@61b1489a0 fix: order volume config by the requested size
- siderolabs/talos@30016a0a8 fix: avoid nil-pointer-panic in `RegistriesConfigController`
- siderolabs/talos@fe0457152 fix: power on the machine on reboot request in qemu power api
- siderolabs/talos@707a77bf6 test: fix user namespace test, TPM2 fixes
- siderolabs/talos@cb4d9d673 docs: fix a few mistakes in release notes
- siderolabs/talos@07220fe7f fix: install iptables-nft to the host
- siderolabs/talos@dd61ad861 fix: lock provisioning order of user disk partitions
- siderolabs/go-circular@015a398 fix: replace static buffer allocation on growth
- siderolabs/go-kubernetes@9ba5654 fix: fix ignoring alpha/beta version parsing
- siderolabs/go-talos-support@0f784bd fix: avoid deadlock on context cancel
- siderolabs/pkgs@b530e90 fix: backport sandbox fix for Gvisor
- siderolabs/pkgs@5bb705c fix: build Amazon ENA driver as module
- siderolabs/pkgs@4d4aaad fix: patch containerd with restart fix
- siderolabs/pkgs@5d6ca21 fix: backport MGLRU patch from Linux 6.13
- siderolabs/pkgs@6fb00b4 fix: pull in kmod from tools
- siderolabs/pkgs@cc5317a fix: patch Linux with blackhole patch
- siderolabs/pkgs@80351ca fix: reproducibility tests
- siderolabs/pkgs@e1f11f0 fix: remove patches and other files from copy-only packages
- siderolabs/pkgs@38749d1 fix: build CNI plugins statically linked
- siderolabs/pkgs@e00ad67 chore: rekres to fix reproducibility build
- siderolabs/pkgs@c9d718d fix: adjust kernel options around ACPI/PCI/EFI
- siderolabs/pkgs@73e4353 fix: update config-arm64 to add Rasperry Pi watchdog support
- siderolabs/pkgs@0ab2427 fix: dvb was missing I2C_MUX support and si2168 driver
- siderolabs/pkgs@0b00e86 fix: patch containerd with CNI deadlock fix
- siderolabs/pkgs@a4c4215 fix: drop cgroupsv1 controllers
- siderolabs/pkgs@86e3755 fix: add CONFIG_INTEL_MEI_GSC_PROXY as module
- siderolabs/tools@6d456ca fix: revert util-linux to 2.40.4
- siderolabs/tools@eeb1f9d fix: revert swig update
- siderolabs/tools@fcee25b fix: revert kmod to 33
- siderolabs/tools@6a71711 fix: do not install man and locale for exported packages
- siderolabs/tools@f33fbe4 fix: install policycoreutils under correct prefix
- siderolabs/tools@ef0a679 fix: do not install anything to /usr/lib64
- siderolabs/tools@533b595 chore: rekres to fix reproducibility

### 1.10.1

- siderolabs/talos@5c4f5a120 fix: multiple logic issues in platform network config controller
- siderolabs/talos@c881e6aa0 fix: deny apply config requests without v1alpha1 in "normal" mode
- siderolabs/talos@5c64e7c27 fix: interactive installer config gen
- siderolabs/talos@46c30f339 fix: generate iso greater than 4 gig
- siderolabs/talos@33401beb2 fix: skip PCR extension if TPM1.2 is found
- siderolabs/talos@77078ff22 fix: containerd crashing with sigsegv
- siderolabs/talos@39561440a fix: ignore http proxy on grpc socket dial
- siderolabs/talos@eb6d98bc9 fix: suppress duplicate platform config updates
- siderolabs/talos@6a438ec93 fix: do correct backoff for nocloud reconcile
- siderolabs/talos@9d64f3194 fix: drop libseccomp from rootfs
- siderolabs/talos@29b20770e fix(ci): provision tests
- siderolabs/talos@52afece5d fix(ci): bios provision test
- siderolabs/talos@e37573ec2 fix: relax etcd APIs RBAC requirements
- siderolabs/pkgs@13e9f09 fix: build containerd with Go 1.23
- siderolabs/pkgs@bdee168 fix: containerd build doesn't need seccomp
- siderolabs/pkgs@61c59a4 fix: downgrade libseccomp to 2.5.5

### 1.10.2

- siderolabs/talos@78df89b87 fix: disable automatic MAC assignment to bridge interfaces
- siderolabs/talos@a5de48b87 fix: selinux detection
- siderolabs/talos@92dcddd19 fix: consistently apply dynamic grpc proxy dialer
- siderolabs/talos@b7e5741e6 test: fix the process runner log collection
- siderolabs/talos@9e71cc8f5 fix: upgrade go-kubernetes for DRA flag bug
- siderolabs/talos@55885600b test: fix some flaky tests
- siderolabs/talos@b183f95c7 fix: k8s 1.32->1.33 upgrade check
- siderolabs/talos@4b27faf44 fix: improve volume mounter automaton
- siderolabs/go-kubernetes@9070be4 fix: remove DynamicResourceAllocation feature gate
- siderolabs/go-kubernetes@8cb588b fix: k8s 1.32->1.33 upgrade check

### 1.10.3

- siderolabs/talos@85110deec fix(ci): reproducibility test
- siderolabs/talos@64609aad5 fix(ci): iso reproducibility file permissions
- siderolabs/talos@d24ef442b fix: nocloud metadata for hostname
- siderolabs/talos@d4eaf78dc fix: allow any PKI in Talos API
- siderolabs/talos@2b5f34a41 fix: metal-iso reproducibility
- siderolabs/talos@3692f6fef fix: bump apid memory limit
- siderolabs/crypto@17107ae fix: add generic CSR generator and OpenSSL interop
- siderolabs/pkgs@39b9c9f fix: drop pcre2 binaries
- siderolabs/pkgs@b622793 fix: drop broken symlinks
- siderolabs/pkgs@ca63fc8 fix: clean up some binaries

### 1.10.4

- siderolabs/talos@7caf90a37 fix: nil pointer deref in quirk
- siderolabs/talos@b6f16e592 fix: update siderolink library for wgtunnel panic fix
- siderolabs/talos@037801f5f fix: correctl close encrypted volumes
- siderolabs/talos@2755aebec chore: fix renovate config, add release-gate label
- siderolabs/talos@1cab7bba1 fix: rework the way CRI config generation is waited for
- siderolabs/talos@bda53869e fix: typo in DiscoverdVolume spec
- siderolabs/talos@4f96f35a4 fix(ci): drop nebula from extensions test
- siderolabs/talos@141e452c4 fix: use correct FUSE magic for IMA `fsmagic` matching
- siderolabs/talos@09a4ed1e0 fix: upgrade grpc library to the latest 1.71.x
- siderolabs/siderolink@d09ff45 fix: race in wait value
- siderolabs/siderolink@d2a79e0 fix: clean up device on failure

### 1.10.5

- siderolabs/talos@2017ec228 fix: add limited retries for not found images
- siderolabs/talos@4a40cddbb fix: hold user volume mount point across kubelet restarts
- siderolabs/talos@9e1f347f5 fix: etcd recover with multiple advertised addresses
- siderolabs/talos@87ed1b589 fix: treat context canceled as expected error on image pull
- siderolabs/talos@9a0644a64 fix: set default MTU on Azure to 1400

### 1.10.6

- siderolabs/talos@755308906 fix: issues with reading GPT
- siderolabs/talos@bb1cdc86b fix: issue with volume remount on service restart
- siderolabs/talos@68a485269 fix: add more bootloader probe logs on upgrade
- siderolabs/talos@d76649dd5 fix: talos endpoint might not be created in Kubernetes

### 1.10.7

- siderolabs/talos@d7936dec6 fix: image cache lockup on a missing volume
- siderolabs/talos@f6541fa71 fix: live reload of TLS client config for discovery client
- siderolabs/talos@29cfd9fd0 fix: enforce minimum size on user volumes if not set explicitly
- siderolabs/discovery-client@0bffa6f fix: allow TLS config to be passed as a function
- siderolabs/discovery-client@09c6687 chore: fix project name in release.toml
- siderolabs/discovery-client@71b0c6d fix: add FIPS-140-3 strict compliance
- siderolabs/pkgs@4cf5eeb fix: re-enable CPUSETS_V1 cgroups controller

### 1.10.8

- siderolabs/talos@50fed880f fix: reserve the apid and trustd ports from the ephemeral port range
- siderolabs/talos@8a2aaad36 fix: bump trustd memory limit
- siderolabs/talos@cf91423af fix: trim zero bytes in the DHCP host & domain response
- siderolabs/talos@b5424e4c8 fix: correctly handle status-code 204

### 1.10.9

- siderolabs/talos@51c680ae2 test: backport test fixes for CRI seccomp profile
- siderolabs/talos@0f42034b0 fix: adapt SELinuxSuite.TestNoPtrace to new strace version
- siderolabs/talos@a705f8e8c fix: clear provisioning data on SideroLink config change
- siderolabs/talos@b7c49777f fix: disable kexec on arm64


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.10.9**, the newest release recorded here for this line.

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
