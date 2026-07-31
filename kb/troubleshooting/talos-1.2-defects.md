---
id: TROUBLE-TALOS_1_2_DEFECTS
type: troubleshooting
title: "talos 1.2: defects fixed in the 1.2 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.2.0 <1.3.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.2 known issues
  - talos 1.2 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.2 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.2: defects fixed in the 1.2 line

## Summary

**109 defects** the project fixed across **10 releases** of the 1.2 line, from 1.2.0 to
1.2.9. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.2.0

- siderolabs/talos@ece66fe9a fix: properly handle `configContext` being `nil` in Talos client
- siderolabs/talos@a3a29ecd8 fix: change the type of returned gRPC connection object from the client
- siderolabs/talos@623414195 fix: expose Talos client gRPC connection via the function `Conn`
- siderolabs/talos@e2ad58478 test: fix cli reboot test
- siderolabs/talos@7ee20e88e fix: limit apid backoff max delay
- siderolabs/talos@80448a2f0 fix: always abort the maintenance service
- siderolabs/talos@3ba53de25 fix: get command in the case 'nodes' are not set in the context
- siderolabs/talos@96c45e93d fix: correctly render hosts.toml with multiple endpoints
- siderolabs/talos@f543f9775 fix: update etcd certificates when node addresses changes
- siderolabs/talos@4db40b6b8 fix: properly read kexec disabled sysctl
- siderolabs/talos@ba9cfd13f fix: update COSI to the version with gRPC Wait fix
- siderolabs/talos@2eed499dc fix: bump rtnetlink to 1.2.2
- siderolabs/talos@cb492c163 fix: don't wait for the hostname in maintenance mode
- siderolabs/talos@f8a5a1a56 fix: stable default hostname bias
- siderolabs/talos@518da6c72 fix: make 'ca', 'crt' and 'key' flags optional for 'talosctl config add'
- siderolabs/talos@28ffff59a fix: handle grub config being empty in the `Revert` function
- siderolabs/talos@6f89c8f7b fix: clean up `cancelCtxMu` leftovers in PriorityLock
- siderolabs/talos@9bbb6a943 fix: surround `cancelCtx` with the mutex
- siderolabs/talos@f04b9f88c fix: talosctl edit mc loop
- siderolabs/talos@5c6648e3d fix: make `talosctl` command return nonzero error codes if it had errors
- siderolabs/talos@20a564085 fix: introduce 'routed' NodeAddresses and use them in kubelet
- siderolabs/talos@07cd0924e fix: recursive seccomp mounts
- siderolabs/talos@fec0ed29d fix: add missing LinkStatusType registration
- siderolabs/talos@6eefa9d9c fix: properly filter resources in maintenance server
- siderolabs/talos@fa5aad01a docs: fix issues in GCP docs
- siderolabs/talos@4fd676c04 docs: fix typo in theila name
- siderolabs/talos@7795de313 fix: use controllers/resources for etcd configuration
- siderolabs/talos@f9b664c94 fix: reload trusted CA list when client is recreated
- siderolabs/talos@8847ccd03 fix: shutdown some streaming API calls when machined API is shuting down
- siderolabs/talos@f95b53726 fix: allow files in extension spec
- siderolabs/talos@1a8f6ec8e fix: don't advertise Kubernetes pod networks over KubeSpan by default
- siderolabs/talos@e3d4a0e4d fix: make reset work even if the node is not bootstrapped/not joined
- siderolabs/talos@6fc38bae6 fix: iterate over etcd members endpoints for member promotion
- siderolabs/talos@c70b692fb fix: update default address if removed from the host
- siderolabs/talos@1ad8e6122 fix: keep entire vlan id when parsing cmdline
- siderolabs/talos@0cdf22243 fix: retry Conflict errors when upgrading k8s manifests
- siderolabs/talos@e5994ff7a fix: skip `ResetDuringBoot` test if the `Cluster` config is unknown
- siderolabs/talos@8028e1074 fix: wait for boot done when rebooting a node in the integration tests
- siderolabs/talos@ec05aee04 fix: correctly unwrap errors when streaming
- siderolabs/talos@c4d2d20c4 fix: enable stable hostnames for worker configs as well
- siderolabs/talos@6e7dfeeb3 fix: data race in packet capture (part 2)
- siderolabs/talos@c11e1dae7 docs: fix spelling and grammar errors
- siderolabs/talos@18756c7ff fix: folder permissions of overlay mounted folders
- siderolabs/talos@a2aea9726 fix: write etcd PKI files in a controller
- siderolabs/talos@bb4abc096 fix: regenerate kubelet certs when hostname changes
- siderolabs/talos@d650afb6c chore: fix typo in `powercycle`
- siderolabs/talos@644e803ad fix: use masks and different firewall mark for KubeSpan
- siderolabs/talos@80444a43d fix: remove data race in pcap capture
- siderolabs/talos@1677bcc4b fix: skip bond itself when matching interface (Equinix Metal)
- siderolabs/talos@87ea1d961 fix: update kubelet kubeconfig when cluster control plane endpoint changes
- siderolabs/talos@6e3d2d647 docs: fix disk encryption params
- siderolabs/talos@626ef05e6 fix: correct SANs for etcd certs
- siderolabs/talos@83ce92c5f docs: fix theila docs
- siderolabs/talos@8a038d40e fix: stabilize etcd join and promote sequences
- siderolabs/talos@136122556 fix: use correct etcd cert path
- siderolabs/talos@c2a512608 fix: avoid double append of `talos.platform` kernel argument
- siderolabs/talos@27dfe7c03 fix: perform accurate conflict resolution on overal (kubespan)
- siderolabs/talos@915de9cf9 docs: fix bridge documentation
- siderolabs/talos@36c44a651 fix: provide CA certificates in `/etc/ssl/certs/ca-certificates.crt`
- siderolabs/talos@7ebd9bcce docs: fix pod security talos resource name
- siderolabs/talos@284a2f959 fix: filter static pods correctly and optimize fetching
- siderolabs/talos@103c94225 fix: update crypto library with support for RSA-SHA*
- siderolabs/talos@07014e0a8 fix: generate correct bootstrap manifests when only IPv6 CIDR is used
- siderolabs/talos@465edbb47 fix: look for qemu-kvm binary
- siderolabs/talos@63caa281a fix: create native image format for DigitalOcean
- siderolabs/talos@f15ce549e fix: siderlink api assume port 443 with https schema
- siderolabs/talos@b816d0b60 docs: fix the vendor information for Kubernetes conformance tests
- siderolabs/talos@a167a5402 test: fix CLI nodes discovery without provisioner data
- siderolabs/talos@80090a3ed test: fix health endpoint cli test when discovery is disabled
- siderolabs/talos@f54d90787 fix: enable orderly poweroff in hyper-v on Azure
- siderolabs/talos@7a11b4def fix: make `talosctl bootstrap` accept only single node
- siderolabs/talos@217fba288 test: fix csi tests
- siderolabs/talos@c0371410e fix: support SideroLink "secure" gRPC connection
- siderolabs/talos@7114292b6 docs: fix latest release version in docs
- siderolabs/talos@da2985fe1 fix: respect local API server port
- siderolabs/talos@e03266667 fix: correctly validate reboot mode in CLI
- siderolabs/talos@27f8e50ce fix: add ovmf image path for rhel
- siderolabs/talos@87e7de30c docs: fix required ports
- siderolabs/talos@c1aed6240 fix: wait for `/var` to be mounted in kubelet service controller
- siderolabs/talos@d7a64f5d2 fix: improve vip operator shutdown sequence
- siderolabs/pkgs@a7609bb fix: nvidia oss pkg name
- siderolabs/pkgs@8a338a3 fix: containerd version
- talos-systems/grpc-proxy@6dfa2cc fix: ignore errors on duplicate `SetHeader` calls

### 1.2.1

- siderolabs/talos@6efe6144d fix: automatically discard VIPs for etcd advertised addresses
- siderolabs/talos@0e4cead3f fix: flip the client-server version check
- siderolabs/talos@b902247ee fix: prevent panic on health check if a member has no IPs

### 1.2.2

- siderolabs/talos@6ba6b91ae test: fix api controller test
- siderolabs/talos@b644fbde2 fix: stop worker nodes from acting as apid routers
- siderolabs/talos@d0a0341f6 fix: never sign client certificate requests in trustd
- siderolabs/talos@39c68b625 fix: include all node addresses into etcd cert SANs
- siderolabs/talos@09140a855 fix: list COSI APIs for the apid authenticator
- siderolabs/talos@015c6d438 fix: pass a pointer to specs.Mount into protoenc.Marshal

### 1.2.3

- siderolabs/talos@1d7d8d5dd fix: set etcd options consistently
- siderolabs/talos@1d522938d fix: ensure that custom Decoder gets called for netaddr.IP

### 1.2.4

- siderolabs/talos@ce540ff6a fix: lookup Equinix Metal bond slaves using 'permanent addr'
- siderolabs/talos@afa5e087b fix: update discovery client with the redirect fix
- siderolabs/talos@0cce9ef0a fix: update go-smbios to v0.2.1
- siderolabs/discovery-client@230f317 fix: reconnect the client on update failure
- talos-systems/go-smbios@72c40f7 fix: check for end of the slice properly

### 1.2.5

- siderolabs/talos@7e7b07b7d feat: patch Linux kernel with UEFI randomize fix

### 1.2.6

- siderolabs/talos@8dd393e77 fix: regenerate cert on node labeling retry
- siderolabs/talos@06266edaf fix: lowercase nodename

### 1.2.7

- siderolabs/talos@54f1b0e19 fix: limit SideroLink Wireguard link MTU to 1280
- siderolabs/talos@bd8ca9da4 fix: generate correct Flannel config for IPv6-only clusters

### 1.2.8

- siderolabs/talos@426fd28aa fix: workaround panic in the kubelet service controller
- siderolabs/talos@05430b987 fix: ignore many more filesystems in IMA
- siderolabs/talos@4af93c3b6 fix: parse correctly upgrade cmd force flag
- siderolabs/pkgs@3903d18 fix: use proper containerd version tag

### 1.2.9

- siderolabs/talos@346a1e28e fix: easier upgrade to Talos 1.3 with custom CRI config


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.2.9**, the newest release recorded here for this line.

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
