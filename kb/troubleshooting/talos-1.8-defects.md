---
id: TROUBLE-TALOS_1_8_DEFECTS
type: troubleshooting
title: "talos 1.8: defects fixed in the 1.8 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.8.0 <1.9.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.8 known issues
  - talos 1.8 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.8 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.8: defects fixed in the 1.8 line

## Summary

**201 defects** the project fixed across **5 releases** of the 1.8 line, from 1.8.0 to
1.8.4. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.8.0

- siderolabs/talos@8fb2f24b4 fix: update blockdevice library to v2.0.2
- siderolabs/talos@882582a8e docs: fix kubespan name inconsistency
- siderolabs/talos@920d8c829 fix: audit and fix cgroup reservations
- siderolabs/talos@c8dedbe11 fix: filter out non-printable characters in process line
- siderolabs/talos@32076935f fix: strategic merge patch delete for map keys
- siderolabs/talos@815e4bae8 fix: ignore invalid NTP responses
- siderolabs/talos@cdabb7bcf fix: update CoreDNS health check
- siderolabs/talos@c030eef15 fix: parse SideroLink API endpoint correctly
- siderolabs/talos@9e60f1708 fix: remove extra logging on ethtool ioctl failures
- siderolabs/talos@faffa4c3f fix: never unarchive initramfs when loading boot assets in talosctl
- siderolabs/talos@07b91797c fix: report internally service as unhealthy if not running
- siderolabs/talos@6f7c3a8e5 fix: build of talosctl on non-Linux arches
- siderolabs/talos@c8aed3be4 fix: correctly add console args for ttyS0
- siderolabs/talos@81f9fcd9c fix: report errors correctly when pulling, fix EEXIST
- siderolabs/talos@b309e87b4 docs: fix invalid input in field user_data
- siderolabs/talos@2d3bc94bf fix(ci): fix broken tests
- siderolabs/talos@a9551b7ca fix: host DNS access with firewall enabled
- siderolabs/talos@e4f8cb854 fix: merge extension service config files by `mountPath`
- siderolabs/talos@823480800 fix: add missing host/nvme-rdma
- siderolabs/talos@5b4b64979 fix: bump go-smbios for broken SMIOS tables
- siderolabs/talos@f57d1f07e fix: add NVMe target kernel modules
- siderolabs/talos@5ff6cf82c fix: drop /opt mount for containers/tink
- siderolabs/talos@3041d9075 fix: always handle `PermissionDenied` in dashboard resource watches
- siderolabs/talos@ee4290f68 fix: bind HostDNS to 169.254.x link-local address
- siderolabs/talos@e193e7db9 docs: fix incorrect path for openebs in documentation
- siderolabs/talos@a5bd770bf fix: retry with another upstream if the previous failed
- siderolabs/talos@73511c1ef chore: fix release notes
- siderolabs/talos@9a33dce10 docs: fix the VMWare docs
- siderolabs/talos@12562c2d5 docs: fix talos version in vmware.sh
- siderolabs/talos@eba5dafb9 fix: add dns-resolve-cache to the support bundle
- siderolabs/talos@d4f8100bd docs: fix default openebs folder
- siderolabs/talos@60e163d54 docs: fix typo in doc
- siderolabs/talos@98d9abdd0 chore(ci): fix cilium ci tests
- siderolabs/talos@f9f5e0ef5 chore: fix k8s tests
- siderolabs/talos@9d3415850 fix: fix graph diffs in dashboard when node aliases are used
- siderolabs/talos@3f2058aba fix: update containerd configuration and settings
- siderolabs/talos@480ffb88a docs: fix the amd64 PXE boot script URL
- siderolabs/talos@20fe34dbd docs: fix docker getting started typo
- siderolabs/talos@19aa44c54 fix: generate kubeconfig using proper types
- siderolabs/talos@1b8c9ccbb fix: enforce secureboot enroll option only for supported releases
- siderolabs/talos@c288ace7b fix: be more smart when merging DNS resolver config
- siderolabs/talos@d983e4430 fix: panic on shutdown
- siderolabs/talos@980f9ebc0 fix: fix log format in cluster provisioning
- siderolabs/talos@1cf76cfbc docs: fix talosctl spelling
- siderolabs/talos@f14c4795e fix: sort ports and merge adjacent ones in the nft rule
- siderolabs/talos@736c1485e fix: change the UEFI firmware search path order
- siderolabs/talos@398151e64 fix: remove host bind mount for `/tmp` for trustd
- siderolabs/talos@d9db360ab fix: properly output multi-doc machine config in `get mc`
- siderolabs/talos@31af6b3f8 chore: fix the release step to include CNI bundle
- siderolabs/talos@d7cd46643 chore: fix the push/tag steps
- siderolabs/talos@c9aeeca3d chore: fix the Makefile
- siderolabs/talos@2512ef435 test: fix the integrtion tests for apply-config
- siderolabs/talos@9a56b8527 chore(ci): fix parallel runs of tf pipelines
- siderolabs/talos@71857fd4d docs: fix typo: `messure` -> `measure`
- siderolabs/talos@f75f16b0a chore(ci): fix cluster name generation
- siderolabs/talos@4b5a7445e docs: fix missing Akamai platform in supported matrix
- siderolabs/talos@d1a0c1f98 test: fix the integration test for no META name
- siderolabs/talos@535006334 chore: fix our dns server implementation
- siderolabs/talos@7cbdce73f fix: detect CD devices, fix user disks wipe test
- siderolabs/talos@aca475c66 chore: small usability fixes
- siderolabs/talos@5e66e117e fix: initial assignment of Hetzner Cloud Alias IP
- siderolabs/talos@7c9a14383 fix: volume discovery improvements
- siderolabs/talos@80ca8ff71 fix: update the cgroups for Talos core services
- siderolabs/talos@fe317f1e1 docs: fix typo in QEMU guest agent support on Proxmox
- siderolabs/talos@357d7754f fix: clean up VM runners on cluster destroy
- siderolabs/talos@82d9cd322 fix: add upgrade errata for arm64/zboot kernels
- siderolabs/talos@9a23d846c fix: downgrade Azure IMDS required version
- siderolabs/talos@30860210c test: fix hardware test not to require PCI devices
- siderolabs/talos@b0466e0ab fix: disable kexec on GCP/Azure
- siderolabs/talos@911c25574 chore: fix go.work resolution
- siderolabs/talos@3367ded9f fix: correct time adjustment in `time.SyncController`
- siderolabs/talos@893e64fcb fix: replace `nslookup` with `dig` in integration tests
- siderolabs/talos@da7f27640 fix: mount `tracefs` filesystem
- siderolabs/talos@7b37e5b63 chore(ci): fix integration extensions
- siderolabs/talos@de7553d77 fix(ci): cron jobs
- siderolabs/talos@a9cf9b789 fix: correctly handle dns messages in our dns implementation
- siderolabs/talos@92a274e9a fix: workaround problems with udevd races
- siderolabs/talos@8a1371337 fix: produce stable order of bonds with equinix
- siderolabs/talos@01ea82053 fix: time sync over NTP from future era
- siderolabs/talos@5aea42427 fix(ci): fix crons by setting up buildx always
- siderolabs/talos@2e64e9e4e fix: require accepted CAs on worker nodes
- siderolabs/talos@23c1c4560 fix(ci): fix crons fby rekres
- siderolabs/talos@a12e4bb24 chore(ci): fix github action crons
- siderolabs/talos@e7bd9cd2b fix: decrease maximum negative ttl for dns responses
- siderolabs/talos@ce8c86d64 fix: panic in osroot controller
- siderolabs/talos@d4307043f fix: update go-tail library to fix 'short read' error
- siderolabs/talos@53f548913 fix: increase host dns packet ttl for pods
- siderolabs/talos@dedb6d360 fix: update github.com/siderolabs/siderolink to v0.3.7
- siderolabs/talos@43939f1a6 docs: fix typos, add docker socket info
- siderolabs/talos@851b91a0e fix: don't enable hostDNS for versions of Talos which do not have it
- siderolabs/talos@42ac5cd0c fix: check for `nil` machine config during installation
- siderolabs/talos@0b0f9995a docs: add resource information, some grammar fixes
- siderolabs/talos@763dae250 fix: add cluster name to the worker machine config
- siderolabs/talos@c08d79732 docs: fix the variable name typo
- siderolabs/talos@478b862b4 fix: do not fail cli action tracker when boot id cannot be read
- siderolabs/talos@be510f9eb docs: fix grpc_tunnel value to true
- siderolabs/talos@07f78182c fix: use a fresh context for etcd unlock
- siderolabs/talos@98906ed6e fix: use reboot delay only in case of error
- siderolabs/talos@8cdf0f7cb docs: fix typo in Cilium instructions
- siderolabs/talos@dd1d279da fix: allow more flags in `talosctl cluster create --input-dir`
- siderolabs/talos@c5b59df69 fix: wait for devices to be discovered before probing filesystems
- siderolabs/talos@2bf613ad3 fix: add endpoints for "virtual" `host-dns` service
- siderolabs/talos@f4163aefe fix: bump priority of OpenStack routes if IPv6 and default gateway
- siderolabs/talos@d46032821 fix: return proper value from Bridge.STP instead of plain nil
- siderolabs/talos@0a785802e fix: overlay installer operations
- siderolabs/talos@b1b63f658 fix: mark overlay installer executable
- siderolabs/talos@5d07ac5a7 fix: close apid inter-backend connections gracefully for real
- siderolabs/talos@7ba18555b docs: fix typos in Akamai and AWS platform docs
- siderolabs/talos@9550f5ff7 docs: fix getAuthenticationMethod and completePathFromNode docs
- siderolabs/talos@bfbd02abf fix: assign different priority to IPv6 default gateway on OpenStack
- siderolabs/talos@145f24063 fix: don't modify a global map of profiles
- siderolabs/talos@909a5800e fix: generate secureboot ISO .der certificate correctly
- siderolabs/talos@b0fdc3c8c fix: make static pods check output consistent
- siderolabs/talos@c6ad0fcce fix: validate that workers don't get cluster CA key
- siderolabs/talos@3735add87 fix: reconnect to the logs stream in dashboard after reboot
- siderolabs/talos@9aa1e1b79 fix: present all accepted CAs to the kube-apiserver
- siderolabs/talos@336e61174 fix: close the apid connection to other machines gracefully
- siderolabs/talos@ff2c427b0 fix: pre-create nftables chain to make kubelet use nftables
- siderolabs/go-api-signature@8807c5e fix: account for time truncation to a second resolution
- siderolabs/go-api-signature@1b35ea8 chore: bump deps and fix data race
- siderolabs/go-api-signature@4bf0f02 fix: get rid of data race in the key sign interceptor
- siderolabs/go-kubernetes@ee8c6b8 fix: add one more removed feature gate for 1.31
- siderolabs/go-smbios@e781237 fix: stop decoding without error if EOF encountered during header read
- siderolabs/go-tail@7cb7294 fix: remove unexpected short read error
- siderolabs/go-talos-support@f9d46fd fix: add `dns-resolve-cache` to the list of logs gathered
- siderolabs/grpc-proxy@ec3b59c fix: address all gRPC deprecations
- siderolabs/pkgs@df1a1a5 fix: lvm2 modprobe path
- siderolabs/pkgs@01ba455 fix: add mpt3sas UBSAN patches
- siderolabs/pkgs@6ee4e56 fix: reproducible build for ipmitool
- siderolabs/pkgs@5f919c5 fix: add virtio-net GSO issue patch
- siderolabs/pkgs@a6db229 fix: strip CNI plugins
- siderolabs/pkgs@99650c8 fix: enable TPROXY for nftables
- siderolabs/pkgs@7f9c802 fix(kernel): array-index-out-of-bounds error on bpf
- siderolabs/pkgs@25f3a99 fix: update ca-certificates in pkgs
- siderolabs/pkgs@60a91b2 fix: enable CONFIG_PROC_CHILDREN for amd64 kernel
- siderolabs/pkgs@a37f382 fix: network for Rockchip boards like Rock64
- siderolabs/pkgs@95218c7 fix: enable PAGE_TABLE_CHECK
- siderolabs/pkgs@f414bbd fix: disable CONFIG_EFI_DISABLE_PCI_DMA option
- siderolabs/pkgs@f9559de fix: drbd module installation
- siderolabs/pkgs@7b30b61 fix: use proper EFI zBoot image
- siderolabs/pkgs@05db2a8 fix: revert musl to 1.2.4
- siderolabs/protoenc@82f0774 fix: encode (u)int(16|8)s as varints
- siderolabs/protoenc@dceb5a6 fix: proper order for custom EncoderDecoder
- siderolabs/protoenc@3617e19 fix: add missing test and proper check for `map[string]interface{}`
- siderolabs/protoenc@3e56913 fix: support pointer to structs in marshal/unmarshal
- siderolabs/protoenc@bf5e39b chore: support (u)int(8|16) fields ans slices, fix map issues,
- siderolabs/protoenc@aa7ee6c chore: add fast path for ints, fixed ints and floats
- siderolabs/protoenc@6427893 chore: bump Go and fix lint issues
- siderolabs/protoenc@94427a5 chore: even more various fixes and small refactorings
- siderolabs/protoenc@76e5695 chore: various fixes and small refactorings
- siderolabs/protoenc@549761b chore: various embedding fixes
- siderolabs/siderolink@3a587fc fix: do not ever skip updates which have remove flag
- siderolabs/tools@41ed4b2 fix: fix Tcl tag hashes
- siderolabs/tools@3c25a6f fix: update pkg-config configure flag

### 1.8.1

- siderolabs/talos@f6d630624 fix: wipe system partitions correctly via kernel args
- siderolabs/talos@4d279c65f fix: volume encryption with failing keyslots
- siderolabs/talos@070defad1 fix: update grpc-go the latest patch release
- siderolabs/talos@e4341fa66 fix: make /var/run empty on reboots
- siderolabs/talos@66228ef10 fix: multiple fixes for LVM activation
- siderolabs/talos@5f4515f30 fix: prevent file descriptors leaks to child processes
- siderolabs/talos@ffcdc0bb7 fix: build talosctl without `tcell_minimal`
- siderolabs/pkgs@47dff98 fix: drop the LVM2 udev lvm rule
- siderolabs/pkgs@480d765 fix: force LVM to use `/run` as state directory

### 1.8.2

- siderolabs/talos@cfc10106a fix: include iptables/netfilter ipv6 fix
- siderolabs/talos@d8e2daf77 fix: wait for udevd to be running before activating LVM
- siderolabs/talos@e105a3d74 fix: talosctl process null character
- siderolabs/talos@0e96e99b2 fix: rework the 'metal-iso' config acquisition
- siderolabs/talos@7ef579650 fix: improve error messages for invalid bridge/bond configuration
- siderolabs/talos@a9e6e60ca fix: correct error message for invalid ip=
- siderolabs/talos@49de0abaa fix: update incorrect alias for PCIDevice resource
- siderolabs/talos@f20a6900d fix: json logging panic
- siderolabs/talos@d855bb8be fix: skip ram disks
- siderolabs/talos@b429e7f28 fix: do not use pflag csv comma reader for config-patch
- siderolabs/talos@7d055af29 fix: scaleway metadata
- siderolabs/go-circular@9a0f7b0 fix: multiple data race issues
- siderolabs/pkgs@e72b2f4 fix: apply netfilter ipv6 fix
- siderolabs/pkgs@f7cc89e fix: default IOMMU mode to 'lazy'
- siderolabs/siderolink@1893385 fix: initialize tls listener properly

### 1.8.3

- siderolabs/talos@01c9f4584 fix: arch linux search paths and names for QEMU provisioner
- siderolabs/talos@8b5c5f108 chore: fix nil pointer dereference in AWS uploader
- siderolabs/talos@fbf85dd0d fix: install disk matcher error
- siderolabs/talos@8c193c8b1 fix: update permissions for logging directories in /var
- siderolabs/talos@5044a410c fix: mount /sys/kernel/security conditionally
- siderolabs/talos@83abb6644 fix: make route normalization keep family
- siderolabs/talos@228a94387 fix: do not trim 0 from process SELinux label
- siderolabs/talos@d4a3a2b62 fix: prevent panic in nocloud platform code
- siderolabs/talos@5c7b02d7e fix: update the CRI sandbox image reference
- siderolabs/talos@ea19f157f fix: generation of SecureBoot iso
- siderolabs/pkgs@b4fa648 fix: enable nvme and 2.5gbit ethernet on nanopi-r5s

### 1.8.4

- siderolabs/talos@1fb38e4c7 fix: use mtu network option for podman
- siderolabs/talos@acd9fda42 fix: order volume config by the requested size
- siderolabs/talos@c547557ae fix: install iptables-nft to the host
- siderolabs/talos@94b342bfe fix: lock provisioning order of user disk partitions
- siderolabs/talos@3a1727ee1 fix: don't reset health status if service doesn't support health checks
- siderolabs/talos@7ff796f65 fix: make `system_disk` condition work properly before install
- siderolabs/talos@379eefdd6 fix: nocloud network link matching on MAC addresses
- siderolabs/talos@aa14ae560 fix: small logrus fixes
- siderolabs/talos@b90863a07 fix: properly halt installation if Talos already installed
- siderolabs/talos@6d20ade14 fix: make vmware platform common code build on all arches
- siderolabs/talos@bc2d547f8 fix: allow CEL expressions config merge
- siderolabs/talos@5188f645e fix: install on non-empty disk


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.8.4**, the newest release recorded here for this line.

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
