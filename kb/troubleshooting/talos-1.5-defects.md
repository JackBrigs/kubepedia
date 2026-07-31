---
id: TROUBLE-TALOS_1_5_DEFECTS
type: troubleshooting
title: "talos 1.5: defects fixed in the 1.5 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.5.0 <1.6.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.5 known issues
  - talos 1.5 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.5 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.5: defects fixed in the 1.5 line

## Summary

**131 defects** the project fixed across **7 releases** of the 1.5 line, from 1.5.0 to
1.5.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.5.0

- siderolabs/talos@7d37108e7 test: fix the check on 'trusted boot'
- siderolabs/talos@2c122b37f fix: match routes on the priority properly
- siderolabs/talos@bd44bf02a chore: fix dependencies in the release pipeline
- siderolabs/talos@c8231d482 fix: make encryption config provider default to `luks2` if not set
- siderolabs/talos@761e7737b fix: calculate log2i properly
- siderolabs/talos@6748efb4e fix: fast-wipe the system disk on talosctl reset
- siderolabs/talos@eae450772 fix: fix azure portion of cloud uploader
- siderolabs/talos@a94cb001c fix: update providerid prefix for aws
- siderolabs/talos@a3a2aa8ef fix: use fast wipe for upgrade
- siderolabs/talos@f863498ff fix: always override APIServer audit policy
- siderolabs/talos@355681dda fix: terminate dashboard gracefully on & switch back to tty1
- siderolabs/talos@9ef4e5efc fix: log explicitly when kubelet has no nodeIP match
- siderolabs/talos@6b39c6a4d fix: enable compression and bump gRPC max msg size
- siderolabs/talos@b84277d7d docs: fix wrong capability name
- siderolabs/talos@14966e718 fix: skip over tpm2 1.2 devices
- siderolabs/talos@166d75fe8 fix: tpm2 encrypt/decrypt flow
- siderolabs/talos@06369e819 fix: retry CRI pod removal, fix upgrade flow in the tests
- siderolabs/talos@936111ce0 fix: properly set up tls for KMS endpoint
- siderolabs/talos@cb226eec4 fix: rewrite encryption system information flow
- siderolabs/talos@bd4f89f63 fix: disable dashboard on Azure, GCP and Scaleway
- siderolabs/talos@74de562b2 fix: mount hugepages with nosuid + nodev
- siderolabs/talos@a4289e870 chore: fix CLI docs generation stability
- siderolabs/talos@e241be85b fix: properly handle YAML comment stripping for multi-doc
- siderolabs/talos@c02ada7d9 fix: capabilities including `ALL` should be uppercase
- siderolabs/talos@35d6adcb9 fix: provide stashed META values before installation
- siderolabs/talos@258f07449 fix: ukify cert generation
- siderolabs/talos@bf3febb7e fix: refine OVMF search paths
- siderolabs/talos@fbebc17f8 fix: disable LVM backups/archive
- siderolabs/talos@7ce87f20c fix: compare only basename of `os.Args[0]` in machined
- siderolabs/talos@d77f0bc7b docs: fix broken link to powershell module
- siderolabs/talos@d8b0903d7 docs: vagrant setup document fix
- siderolabs/talos@665702ddd chore: fix cilium e2e tests
- siderolabs/talos@e858bca3a test: fix cilium integration tests
- siderolabs/talos@455328d05 fix: allow time skew for generated kubeconfig
- siderolabs/talos@3ae05648a fix: usage of custom kernels
- siderolabs/talos@a34a94898 fix: copy missing modules.* files
- siderolabs/talos@aef2192a6 chore: use fixed module list
- siderolabs/talos@c719aa231 fix: allow http:// for discovery service URL
- siderolabs/talos@39134d8d5 chore: fix cron pipeline
- siderolabs/talos@a61dcdbbd fix: don't load RDMA over Ethernet driver by default
- siderolabs/talos@196dfb99b fix: do not probe kernel args in dashboard if not needed
- siderolabs/talos@8c071b579 fix: skip DHCP RENEW if server IP in the lease is all zeroes
- siderolabs/talos@ecce29dee fix: upgrade-k8s use internal IP first, external IP fallback
- siderolabs/talos@1fb29a56a fix: fail quickly if upgrade-k8s is used with multiple nodes
- siderolabs/talos@ea9a97dba fix: fall back to external IP when discovering nodes in upgrade-k8s
- siderolabs/talos@ff11fd39c fix: race with `udevd` and `mountUserDisks`
- siderolabs/talos@dd8336c9e fix: refresh kubelet self-issued serving certificates
- siderolabs/talos@3b36993b9 fix: rlimit nofile test
- siderolabs/talos@4f720d465 fix: revert: set rlimit explicitly in wrapperd
- siderolabs/talos@a2565f674 fix: set rlimit explicitly in wrapperd
- siderolabs/talos@55ae59a0a fix: properly skip/cleanup controlplane configs for workers
- siderolabs/talos@860002c73 fix: don't reload control plane pods on cert SANs changes
- siderolabs/talos@d43c61e80 fix: enforce nolock option for all NFS mounts by default
- siderolabs/talos@339986db9 fix: inhibit timer to follow kubelet timer
- siderolabs/talos@cbf6dc100 fix: set timeout for unmount calls
- siderolabs/talos@b58f913d5 fix: set the static pod priority as values
- siderolabs/talos@7442ff8b0 chore: fix typos inteface -> interface (docs and tests)
- siderolabs/talos@d4e94f7a1 fix: add back required TARGETARCH for installer
- siderolabs/talos@344746ae2 fix: bump max inhibit delay to 20 min
- siderolabs/talos@014008ea2 fix: udevd rules trigger
- siderolabs/talos@9b36bb613 feat: update Linux to 6.1.25, fix virtio on arm64
- siderolabs/talos@b097efcde fix: display correct number of machines on dashboard
- siderolabs/talos@e296a566e fix: support kernel userspace module loading
- siderolabs/talos@ec8c8dbaf chore: fix container image reproducibility
- siderolabs/talos@f661d8487 fix: allow `talosctl cp` to handle special files in `/proc`
- siderolabs/talos@2d824b563 fix: do not show control plane status for workers on dashboard
- siderolabs/talos@7a004a6f7 fix: parse errors correctly
- siderolabs/talos@45d7f0ce9 docs: fix the latest url
- siderolabs/talos@f14928b0a fix: fix dashboard crash when a non-existent node is specified
- siderolabs/talos@3cd1c6bb0 fix: send 'STOP' event on phase end
- siderolabs/talos@2c55550a6 fix: quote ISO kernel args for GRUB
- siderolabs/talos@319d76e38 fix: respect BROWSER=echo in client auth interceptor
- siderolabs/talos@170f73899 fix: correctly parse static pod phase
- siderolabs/talos@c3a595d5b fix: improve action tracking post checks
- siderolabs/talos@eb01edbc8 fix: rework DHCP flow
- siderolabs/go-blockdevice@fbb01f7 fix: properly detect token not found error
- siderolabs/go-blockdevice@3e08968 fix: do not attach token to a key slot
- siderolabs/go-kubernetes@5a3df5b fix: remove removed APIs for 1.27 upgrade
- siderolabs/go-loadbalancer@574126c chore: add 0.1ms tier and fix tiers
- siderolabs/go-loadbalancer@5301800 chore: fix logging and tests
- siderolabs/go-loadbalancer@f3a0e24 fix: use SO_LINGER option when doing TCP healthchecks
- siderolabs/kms-client@50064b6 fix: pass context to the key handler in the server wrapper
- siderolabs/pkgs@e4aa9a2 fix: nonfree kmod pkg name
- siderolabs/pkgs@fb817fe fix: enable USB attached SCSI driver on x86 systems
- siderolabs/pkgs@f7cd916 fix: bump drbd to 9.2.4
- siderolabs/pkgs@a56d15a fix: copy missing `modules.*` files
- siderolabs/pkgs@a859f4f fix: build RDMA_RXE as a module
- siderolabs/pkgs@5327d12 fix: remove FB_NVIDIA drivers, Linux 6.1.23
- siderolabs/tools@c6a41b6 fix: add sd-stub assertion patch

### 1.5.1

- siderolabs/talos@4fd4e16c0 fix: copy proper modules to arm64 squashfs
- siderolabs/talos@2d2b8c895 fix: prevent dashboard crashes when process info is not available
- siderolabs/talos@a79ed5e47 fix: properly GC images supplied with both tag and digest
- siderolabs/talos@024053a5c fix: automatically change `rpi_4` board on upgrade
- siderolabs/talos@5c82445d2 fix: support 'List' type manifests
- siderolabs/talos@7b36ada79 fix: use image digest when starting a container
- siderolabs/talos@106078295 fix: ntp query error with bare IPv6 address
- siderolabs/talos@5b1d021d5 fix: write correct capacity to the ovf
- siderolabs/talos@3c8b0856b fix: restore compatibility with Kubernetes 1.26

### 1.5.2

- siderolabs/talos@45c88aedd fix: update kubernetes library for 1.28 upgrade pre-checks
- siderolabs/talos@b8bd8ee43 fix: shorten VLAN link names to fit into the limit of 15 characters
- siderolabs/talos@4552014b9 fix: set correct (1 year) talosconfig expiration
- siderolabs/talos@1804906c7 fix: set proper timeouts for KubePrism loadbalancer
- siderolabs/talos@6ae5b1289 fix: ova contents to be named `disk.*`
- siderolabs/talos@9d6d580f4 fix: properly calculate overal of node address with subnet filters

### 1.5.3

- siderolabs/talos@721b69b40 fix: generate of modules.dep when on the machine
- siderolabs/talos@802aedd21 fix: build CPU ucode correctly for early loader
- siderolabs/talos@6e27fe3a6 fix: calculate UKI ISO size dynamically
- siderolabs/talos@43d4afc92 fix: set default route priority for hcloud platform
- siderolabs/talos@63a4257a9 fix: handle correctly change of listen address for maintenance service
- siderolabs/talos@2e13558ac fix: trim file path in the container image

### 1.5.4

- siderolabs/talos@b72abb613 test: fix 'talosctl gen' tests
- siderolabs/talos@69f1ea283 fix: handle secure boot state policy pcr digest error
- siderolabs/talos@738092fda fix: use tpm2 hash algorithm constants and allow non-SHA-256 PCRs
- siderolabs/talos@21d874a8a fix: clear the encryption config in META when STATE is reset
- siderolabs/talos@124c2ff13 fix: the node IP for kubelet shouldn't change if nothing matches

### 1.5.5

- siderolabs/talos@5f70f05e9 fix: don't validate machine.install if installed
- siderolabs/talos@0b18d7403 fix: when writing to META in the installer/imager, use fixed name
- siderolabs/talos@6be1e5836 fix: fix error output of cli action tracker
- siderolabs/talos@61413ed11 fix: make Talos work on Rockpi 4c boards again
- siderolabs/talos@9fe31bd42 fix: update gRPC library to 1.57.2

### 1.5.6

- siderolabs/talos@e7475d8fd fix: take into account the moment seen when cleaning up CRI images
- siderolabs/talos@9b819ee1e fix: watch bufer overrun for RouteStatus
- siderolabs/talos@730913fdb fix: update kmsg with utf-8 fix
- siderolabs/talos@a3b48c696 fix: disk UUID & WWID always empty in `talosctl disks`
- siderolabs/talos@e4a23412f fix: skip writing the file if the contents haven't changed
- siderolabs/talos@8516708a5 fix: retry blockdevice open in the installer
- siderolabs/talos@d82b14eae fix: be more tolerant to error handling in Mounts API
- siderolabs/talos@d35002777 fix: ignore kernel command line in container mode
- siderolabs/talos@06424ad5d fix: allow extra kernel args for secureboot installer
- siderolabs/talos@985ed8de6 fix: set max msg recv size when proxying
- siderolabs/go-kmsg@e358d13 fix: decode escape sequences while reading from kmsg


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.5.6**, the newest release recorded here for this line.

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
