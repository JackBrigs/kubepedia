---
id: TROUBLE-TALOS_1_11_DEFECTS
type: troubleshooting
title: "talos 1.11: defects fixed in the 1.11 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.11.0 <1.12.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.11 known issues
  - talos 1.11 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.11 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.11: defects fixed in the 1.11 line

## Summary

**166 defects** the project fixed across **6 releases** of the 1.11 line, from 1.11.0 to
1.11.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.11.0

- siderolabs/talos@a5f80b4fe fix: bring back linux/armv7 build and update xz
- siderolabs/talos@751dae432 fix: drop linux/armv7 build
- siderolabs/talos@8cbd75320 fix: update xz module (security)
- siderolabs/talos@1ee82120e docs: apply fixes for what is new
- siderolabs/talos@0f22913d9 fix: image cache lockup on a missing volume
- siderolabs/talos@350319063 fix: actually use SIDEROV1_KEYS_DIR env var if it's provided
- siderolabs/talos@430a27dc2 fix: kubernetes upgrade options for kubelet
- siderolabs/talos@e3a9097c4 fix: set secs field in DHCPv4 packets
- siderolabs/talos@babddd0e4 fix: dial with proxy
- siderolabs/talos@bbd01b6b7 refactor: fix deadcode elimination with godbus
- siderolabs/talos@85589662a fix: unmarshal encryption STATE from META
- siderolabs/talos@614ca2e22 fix: one more attempt to fix volume mount race on restart
- siderolabs/talos@7dee810d4 fix: live reload of TLS client config for discovery client
- siderolabs/talos@a5dc22466 fix: enforce minimum size on user volumes if not set explicitly
- siderolabs/talos@d108e0a08 fix(ci): use a random suffix for ami names
- siderolabs/talos@504225546 fix: issues with reading GPT
- siderolabs/talos@201b6801f fix: issue with volume remount on service restart
- siderolabs/talos@31a67d379 fix: do not download artifacts for cron Grype scan
- siderolabs/talos@a60101c55 fix: fill serial using helpers
- siderolabs/talos@75b5dec06 fix: sd-boot kexec with disk images
- siderolabs/talos@3f35b83ae fix: ignore absent extensions SBOM directory
- siderolabs/talos@993b4ade8 docs: fix typo in hugo config: pre-releaase
- siderolabs/talos@130b7fd6e test: fix flaky TestDNS
- siderolabs/talos@a966321cc fix: add more bootloader probe logs on upgrade
- siderolabs/talos@0b8c180b8 fix: rename instances to referenceCount
- siderolabs/talos@9f0792632 fix: improve volume provisioning errors
- siderolabs/talos@b8fcf3c71 fix: change module instance evaluation
- siderolabs/talos@d531b682c fix: provide FIPS 140-3 compliance
- siderolabs/talos@54bd50be3 fix: talos endpoint might not be created in Kubernetes
- siderolabs/talos@1f1f78106 fix: add limited retries for not found images
- siderolabs/talos@1e5a008f5 fix: hold user volume mount point across kubelet restarts
- siderolabs/talos@b9dbdc8e7 fix: etcd recover with multiple advertised addresses
- siderolabs/talos@44a1fc3b7 fix: treat context canceled as expected error on image pull
- siderolabs/talos@6c7f8201a fix: set default MTU on Azure to 1400
- siderolabs/talos@091cd6989 docs: small yaml typo fix
- siderolabs/talos@c948d7617 docs: minor fixes for creating kernel modules
- siderolabs/talos@9642198d7 fix: userspace wireguard library overrides
- siderolabs/talos@208f0763e chore: fix talosctl build on non-Linux hosts
- siderolabs/talos@8e84c8b0f fix: nil pointer deref in quirk
- siderolabs/talos@260d1bc9a fix: correctl close encrypted volumes
- siderolabs/talos@034ef42af fix: update siderolink library for wgtunnel panic fix
- siderolabs/talos@3035744a8 fix: correctly predict interface name on darwin
- siderolabs/talos@58a868e68 chore: fix renovate config, add release-gate label
- siderolabs/talos@aab053394 fix: mashal resource byte slices as strings in YAML
- siderolabs/talos@c7d4191e7 fix: rework the way CRI config generation is waited for
- siderolabs/talos@2d5a805b0 fix: typo in DiscoverdVolume spec
- siderolabs/talos@0fd622c82 fix(talosctl): correct --help output for dashboard command
- siderolabs/talos@a60b6322d fix(ci): drop nebula from extensions test
- siderolabs/talos@ff80e4cca docs: fix CIDR name
- siderolabs/talos@a5fd15e8b fix(ci): reproducibility test
- siderolabs/talos@c6b86872d fix(ci): iso reproducibility file permissions
- siderolabs/talos@9db5d0c97 fix: nocloud metadata for hostname
- siderolabs/talos@3524745cc fix: allow any PKI in Talos API
- siderolabs/talos@11c17fb9a fix: metal-iso reproducibility
- siderolabs/talos@0cb137ad7 fix: make disk size check work on old Talos
- siderolabs/talos@7c057edd5 fix: use vmdk-convert istead of qemu-img to create VMDK for OVA files
- siderolabs/talos@0b99631a0 fix: bump apid memory limit
- siderolabs/talos@e1a939144 docs: fix formatting in disk encryption
- siderolabs/talos@f35b213b2 test: fix DHCP unicast failures in QEMU environment
- siderolabs/talos@7064bbf05 docs: fix vmware factory URL
- siderolabs/talos@da6795266 fix: disable automatic MAC assignment to bridge interfaces
- siderolabs/talos@ea5de19fa fix: selinux detection
- siderolabs/talos@52c76ea3a fix: consistently apply dynamic grpc proxy dialer
- siderolabs/talos@1161faa05 docs: fix typo in Cilium docs
- siderolabs/talos@9a2ecbaaf fix: makefile operating system param
- siderolabs/talos@e2f819d88 test: fix the process runner log collection
- siderolabs/talos@fdac4cfb9 fix: upgrade go-kubernetes for DRA flag bug
- siderolabs/talos@09d88e1e8 test: fix some flaky tests
- siderolabs/talos@95259337e fix: k8s 1.32->1.33 upgrade check
- siderolabs/talos@c3c326b40 fix: improve volume mounter automaton
- siderolabs/talos@97ceab001 fix: multiple logic issues in platform network config controller
- siderolabs/talos@0cfcdd3de docs: fix search on base talos.dev
- siderolabs/talos@c6824c211 fix: deny apply config requests without v1alpha1 in "normal" mode
- siderolabs/talos@7df0408e4 fix: interactive installer config gen
- siderolabs/talos@881c5d62b fix: suppress duplicate platform config updates
- siderolabs/talos@66d77888e fix: replace downloaded asset paths correctly in cluster create cmd
- siderolabs/talos@6bd6c9b5a fix: generate iso greater than 4 gig
- siderolabs/talos@ac140324e fix: skip PCR extension if TPM1.2 is found
- siderolabs/talos@09ef1f8a4 fix: ignore http proxy on grpc socket dial
- siderolabs/talos@22c34a50f fix(ci): provision cron jobs
- siderolabs/talos@b3b20eff3 fix: containerd crashing with sigsegv
- siderolabs/talos@ae87edffb fix: drop libseccomp from rootfs
- siderolabs/talos@f74a805bb fix: do correct backoff for nocloud reconcile
- siderolabs/talos@01bb294af fix(ci): provision tests
- siderolabs/talos@2b89c2810 fix: relax etcd APIs RBAC requirements
- siderolabs/talos@1e677587c fix: preserve kubelet image suffix
- siderolabs/talos@62ab8af45 fix: disk image generation with image cache
- siderolabs/talos@d60626f01 fix: handle encryption type mismatch
- siderolabs/talos@fa95a2146 fix(ci): bios provision test
- siderolabs/talos@f7c5b86be fix: sync PCR extension with volume provisioning lifecycle
- siderolabs/talos@8db34624c fix: handle correctly changing platform network config
- siderolabs/talos@c4fb7dad0 fix: force DNS runner shutdown on timeout
- siderolabs/talos@be3f0c018 fix: fix Gvisor tests with containerd patch
- siderolabs/talos@ec60b70e7 fix: set media type to OCI for image cache layer
- siderolabs/talos@54ad5b872 fix: extension services logging to console
- siderolabs/talos@a1d08a362 docs: fixes typo at OpenEBS Mayastor worker patches
- siderolabs/talos@c76189c58 fix: grub EFI mount point
- siderolabs/talos@4ca985c65 fix: grub efi platform install
- siderolabs/talos@e51a8ef8c fix: prefer new `MountStatus` resource
- siderolabs/talos@8cd3c8dc7 test: fix NVIDIA OSS tests
- siderolabs/talos@141326ea3 docs: fix tabpane styling
- siderolabs/crypto@62a079b fix: update TLS config, add tests for TLS interactions
- siderolabs/crypto@c2b4e26 fix: remove code duplication and fix Ed255119 CA generation
- siderolabs/crypto@2a07632 fix: enforce FIPS-140-3 compliance
- siderolabs/crypto@17107ae fix: add generic CSR generator and OpenSSL interop
- siderolabs/discovery-client@0bffa6f fix: allow TLS config to be passed as a function
- siderolabs/discovery-client@09c6687 chore: fix project name in release.toml
- siderolabs/discovery-client@71b0c6d fix: add FIPS-140-3 strict compliance
- siderolabs/go-circular@5b39ef8 fix: do not log error if chunk zero was never written
- siderolabs/go-kubernetes@9070be4 fix: remove DynamicResourceAllocation feature gate
- siderolabs/go-kubernetes@8cb588b fix: k8s 1.32->1.33 upgrade check
- siderolabs/pkgs@f31e192 fix: bump NVIDIA production to 570.172.08
- siderolabs/pkgs@3bb9cc9 fix: backport CVE kernel patches to 6.12
- siderolabs/pkgs@2598d53 fix: re-enable CPUSETS_V1 cgroups controller
- siderolabs/pkgs@48afc2a fix: enable ISCSI IBFT
- siderolabs/pkgs@c97d25e fix: remove erroneous PURLs
- siderolabs/pkgs@fae59df fix: download and copy hailo8 firmware
- siderolabs/pkgs@1b1430e fix: drop pcre2 binaries
- siderolabs/pkgs@487610c fix: drop broken symlinks
- siderolabs/pkgs@f31d518 fix: clean up some binaries
- siderolabs/pkgs@89b4037 fix: tenstorrent pkg name
- siderolabs/pkgs@2a1c42f fix(renovate): flannel config
- siderolabs/pkgs@9f1ba1f fix: bring back updated containerd gvisor patch
- siderolabs/pkgs@a347857 fix: build containerd with Go 1.23
- siderolabs/pkgs@74da85c fix: containerd build doesn't need seccomp
- siderolabs/pkgs@4effa05 fix: downgrade libseccomp to 2.5.5
- siderolabs/pkgs@d042432 fix: backport sandbox fix for Gvisor
- siderolabs/siderolink@d09ff45 fix: race in wait value
- siderolabs/siderolink@d2a79e0 fix: clean up device on failure

### 1.11.1

- siderolabs/talos@ff8644cd2 fix: correctly handle status-code 204
- siderolabs/talos@9e310a9dd fix: enable support for VMWare arm64

### 1.11.2

- siderolabs/talos@ac452574e fix: default gateway as string
- siderolabs/talos@7cec0e042 fix: uefi boot entry handling logic
- siderolabs/talos@24c1bcecf fix: bump trustd memory limit
- siderolabs/talos@682df89d7 fix: use correct order to determine SideroV1 keys directory path
- siderolabs/talos@a838881fa fix: trim zero bytes in the DHCP host & domain response
- siderolabs/talos@9c962ae9c fix: re-create cgroups when restarting runners
- siderolabs/talos@de243f9ae test: fix flakiness in RawVolumes test

### 1.11.3

- siderolabs/talos@560241c00 fix: make Akamai platform usable
- siderolabs/talos@1b23cad61 fix: cherry-pick of commit `0fbb0b0` from #11959
- siderolabs/talos@876719a92 fix: cherry-pick of commit `cd9fb27` from #11943
- siderolabs/talos@0fbb0b028 fix: provide nocloud metadata with missing network config
- siderolabs/talos@49182b386 fix: support secure HTTP proxy with gRPC dial
- siderolabs/talos@48ee8581b fix: don't set broadcast for /31 and /32 addresses
- siderolabs/talos@7668c52dd fix: provide refreshing CA pool (resolvers)

### 1.11.4

- siderolabs/talos@9c27f9e62 fix: race between VolumeConfigController and UserVolumeConfigController
- siderolabs/talos@ac27129b1 fix: provide minimal platform metadata always
- siderolabs/talos@19463323e fix: image-signer commands
- siderolabs/talos@075f9ef22 fix: userspace wireguard handling
- siderolabs/talos@35b97016c fix: log duplication on log senders
- siderolabs/talos@d00754e35 fix: add video kernel module to arm
- siderolabs/talos@89bca7590 fix: set a timeout for SideroLink provision API call
- siderolabs/talos@23b21eb90 fix: imager build on arm64
- siderolabs/talos@8edddafcd fix: reserve the apid and trustd ports from the ephemeral port range

### 1.11.6

- siderolabs/talos@dcbbe2ca0 test: backport test fixes for CRI seccomp profile
- siderolabs/talos@428b5921e fix: disable kexec on arm64
- siderolabs/talos@c36ffc626 fix: disable kexec in talosctl cluster create on arm64
- siderolabs/talos@0a90bf640 fix: selection of boot entry
- siderolabs/talos@afc08b34e fix: update KubeSpan MSS clamping
- siderolabs/talos@aedddccef fix: adapt SELinuxSuite.TestNoPtrace to new strace version
- siderolabs/talos@004213799 fix: clear provisioning data on SideroLink config change
- siderolabs/talos@e7e354162 fix: selection of boot entry
- siderolabs/talos@b5244f901 fix: remove CoreDNS cpu limit
- siderolabs/talos@42897dee5 fix: uefi bootorder setting
- siderolabs/talos@bde8be2c8 fix: uefi boot order setting
- siderolabs/talos@7e99ced96 fix: stop attaching to tearing down mount parents


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.11.6**, the newest release recorded here for this line.

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
