---
id: TROUBLE-TALOS_1_1_DEFECTS
type: troubleshooting
title: "talos 1.1: defects fixed in the 1.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.1.0 <1.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.1 known issues
  - talos 1.1 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.1 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.1: defects fixed in the 1.1 line

## Summary

**109 defects** the project fixed across **3 releases** of the 1.1 line, from 1.1.0 to
1.1.2. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.1.0

- siderolabs/talos@6d6567512 docs: fix the vendor information for Kubernetes conformance tests
- siderolabs/talos@ed09dee4f fix: make `talosctl bootstrap` accept only single node
- siderolabs/talos@86352abe0 test: fix csi tests
- siderolabs/talos@9409975b1 fix: support SideroLink "secure" gRPC connection
- siderolabs/talos@2d1a94e08 fix: correctly validate reboot mode in CLI
- siderolabs/talos@10ac9dc95 fix: respect local API server port
- siderolabs/talos@e23d1979b fix: add ovmf image path for rhel
- siderolabs/talos@6229eefe7 fix: wait for `/var` to be mounted in kubelet service controller
- siderolabs/talos@4712e73c4 fix: improve vip operator shutdown sequence
- siderolabs/talos@0a6fc906f fix: table align hosts file
- siderolabs/talos@be644c96e fix: flannel ipv6 compatibility
- siderolabs/talos@19edbb5bd docs: fix typo in main page
- siderolabs/talos@e40153aef fix: introduce more route protocols as constants
- siderolabs/talos@f9c46fb18 fix: unmarshal HardwareAddr without stdlib help
- siderolabs/talos@f2e94d602 fix: implement unmarshaling from YAML for LinkStatus
- siderolabs/talos@875f67a6e fix: correctly parse empty route flags from YAML
- siderolabs/talos@88efd75d3 docs: fix install script url
- siderolabs/talos@4551cbd7f fix: cluster creation error message formatting
- siderolabs/talos@bafa1f49d fix: improve error message when creating cluster
- siderolabs/talos@1156daac2 fix: azure hostname definition
- siderolabs/talos@40e57efa4 chore: fix reference to talosconfig
- siderolabs/talos@4b3935fa4 docs: fix 1.1.x support matrix
- siderolabs/talos@5bac5e91a docs: fix "double-base64-encode" in cert/key examples
- siderolabs/talos@5a8e011db fix: match for WSL platform in case-insentive way
- siderolabs/talos@14985674c fix: allow SideroLink IPs in NodeAddresses
- siderolabs/talos@850cfba72 chore: fix type order in deep-copy generation line
- siderolabs/talos@5a91f6076 fix: ignore completed pods in cluster health check
- siderolabs/talos@91a49c4e7 fix: dhcpv6 leasetime segfault loop
- siderolabs/talos@afb679586 fix: reset certificate SANs on update
- siderolabs/talos@c87432fe1 fix: detect WSL for `talosctl cluster create` on Docker
- siderolabs/talos@86741d998 fix: append hostname to cluster SANs when port is not specified
- siderolabs/talos@9885bbe17 docs: fix typos, edited for clarity
- siderolabs/talos@7fd1c80c3 fix: ignore failures to dial wireguard client
- siderolabs/talos@c2be65b66 fix: openstack unable to parseIP
- siderolabs/talos@79ae76a6f fix: properly set `allowSchedulingOnMasters` in the interactive install
- siderolabs/talos@802d4a23c fix: load kubelet system service in StartAllServices task
- siderolabs/talos@67019c434 fix: add source path for ovmf flash image
- siderolabs/talos@8bc97a30f fix: remove D-Bus sockets before listen attempts
- siderolabs/talos@54cfa039a fix: use json.Unmarshal instead of yaml.Unmarshal
- siderolabs/talos@b189e8426 chore: fix incorrect ManifestSpec.MarshalYAML signature
- siderolabs/talos@b52e0b9b9 fix: talosctl throws error if gen option and --input-dir flags are combined
- siderolabs/talos@3136334b9 docs: fix links in VMware documentation
- siderolabs/talos@483201026 fix: return an error if there is no byte slice in ReadonlyProvider
- siderolabs/talos@6e7486f09 fix: allow graceful node shutdown to be overridden
- siderolabs/talos@03ef62ad8 fix: include Go primitive types into unstructured deepcopy
- siderolabs/talos@c0d386abb fix: don't mount D-Bus socket via mount under recursive bind mount
- siderolabs/talos@7568d51fc fix: trigger CRI config merge on correct resource update
- siderolabs/talos@7ad27751c docs: fix analytics and sitemap
- siderolabs/talos@f1f43131f fix: strip 'v' prefix from versions on Kubernetes upgrade
- siderolabs/talos@f3e330a0a docs: fix network dependency
- siderolabs/talos@d78ed320b docs: fix the docs reference to star registry redirects
- siderolabs/talos@257dfb870 fix: run the 'post' stage of the service always
- siderolabs/talos@992e23023 fix: correctly handle stopping services with reverse dependencies
- siderolabs/talos@bb7a50bd5 docs: fix netlify redirects
- siderolabs/talos@486f79bc7 docs: fix netlify deploy url
- siderolabs/talos@23984efcd fix: detect lingering mounts in the installer correctly
- siderolabs/talos@68dfdd331 fix: provide logger to the etcd snapshot restore
- siderolabs/talos@2b68c8b67 fix: enable long timestamps for xfs
- siderolabs/talos@460d5ab13 docs: fix extension services alias
- siderolabs/talos@8af50fcd2 fix: correct cri package import path
- siderolabs/talos@0cb84e8c1 fix: correctly parse tags out of images
- siderolabs/talos@18d0038ec fix: avoid panic in DHCPv6 operator on nil dereference
- siderolabs/talos@9e3d438db docs: fix code fence formatting
- siderolabs/talos@b3f1bb2cf fix: add support for FAT12/16 filesystems
- siderolabs/talos@5192ba4e2 docs: fix a typo in QEMU VM setup guide
- siderolabs/talos@19bf12af0 fix: enable IPv6 in Docker-based Talos clusters
- siderolabs/talos@2ca5279e5 fix: retry manifest updates in upgrade-k8s
- siderolabs/talos@12931dced fix: align partitions on 1M boundary
- siderolabs/talos@37f868e37 fix: validate empty TLS config for registries
- siderolabs/talos@ad6b7ec1a fix: enable etcd consistency on check startup
- siderolabs/talos@efa3f2898 fix: correctly find partitions with config data (`metal-iso`)
- siderolabs/talos@9ebeec0d0 docs: fix incorrect path for talosconfig
- siderolabs/talos@9fef4540e docs: fix non-latest download links
- siderolabs/talos@0fd2aa08b fix: correctly escape '.' in volume names
- siderolabs/talos@108fd03a7 fix: give up virtual IPs before the kubelet workloads are shut down
- siderolabs/talos@856e1333d fix: use 'localhost' endpoint in docker provisioner on Windows
- siderolabs/talos@5344d6e7c docs: fix extension service `path` dependency
- siderolabs/talos@9b9191c5e fix: increase intiial window and connection window sizes
- siderolabs/talos@9ff42b432 docs: fix redirects for /docs URLs
- siderolabs/talos@73966f51e docs: fix extensions
- siderolabs/talos@f47750726 fix: the etcd recovery client and tests
- siderolabs/talos@69e07cddc fix: trigger properly `udevd` on types and actions
- siderolabs/talos@47d0e629d fix: clean up custom udev rules if the config is cleared
- siderolabs/talos@1e982808f fix: ignore pod CIDRs for kubelet node IPs
- siderolabs/talos@5e0c80f61 fix: ignore connection reset errors on k8s upgrade
- siderolabs/talos@c156580a3 fix: split regular network operation configuration and virtual IP
- siderolabs/talos@50594ab1a fix: ignore terminated pods in pod health checks
- siderolabs/talos@327ce5aba fix: invert the condition to skip kubelet kernel checks
- siderolabs/talos@355b1a4be fix: refresh etcd certs on startup/join
- siderolabs/talos@d256b5c5e docs: fix spelling mistakes
- siderolabs/talos@a095acb09 chore: fix equinixMetal platform name
- siderolabs/talos@2a7f9a445 fix: check for IPv6 before applying accept_ra
- siderolabs/talos@59681b8c9 fix: backport fixes from release-1.0 branch
- siderolabs/pkgs@4dace49 fix: ipxe prompt arm64
- talos-systems/go-blockdevice@fccee8b chore: rekres the source, fix issues
- talos-systems/go-blockdevice@b374eb4 fix: align partition to 1M boundary by default
- talos-systems/go-loadbalancer@4a6e29e refactor: clean up names, fix the lingering goroutines
- talos-systems/siderolink@3a5be65 fix: use correct method to generate Wireguard private key
- talos-systems/siderolink@b38c192 fix: build on Windows

### 1.1.1

- siderolabs/talos@6b7c6110c fix: stabilize etcd join and promote sequences
- siderolabs/talos@6dbc086b0 fix: use correct etcd cert path
- siderolabs/talos@56daca8f3 fix: siderlink api assume port 443 with https schema
- siderolabs/talos@f9f1c432f fix: provide CA certificates in `/etc/ssl/certs/ca-certificates.crt`
- siderolabs/talos@a76a90a43 fix: generate correct bootstrap manifests when only IPv6 CIDR is used
- siderolabs/talos@76d048ffc fix: look for qemu-kvm binary

### 1.1.2

- siderolabs/talos@c5959d66f chore: fix typo in `powercycle`
- siderolabs/talos@d8e893b25 fix: folder permissions of overlay mounted folders
- siderolabs/talos@2ae1455c8 fix: use masks and different firewall mark for KubeSpan
- siderolabs/talos@e88c1fba8 fix: skip bond itself when matching interface (Equinix Metal)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.1.2**, the newest release recorded here for this line.

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
