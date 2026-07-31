---
id: TROUBLE-TALOS_1_4_DEFECTS
type: troubleshooting
title: "talos 1.4: defects fixed in the 1.4 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.4.0 <1.5.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 1.4 known issues
  - talos 1.4 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 1.4 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 1.4: defects fixed in the 1.4 line

## Summary

**58 defects** the project fixed across **6 releases** of the 1.4 line, from 1.4.0 to
1.4.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.4.0

- fix: fix dashboard crash when a non-existent node is specified
- fix: add a link-scope route if the cmdline gateway is not reachable
- feat: dhcpv4: send current hostname, fix spec compliance of renewals
- fix: output of `talosctl logs` might be corruped
- fix: use 'no block' etcd dial with multiple endpoints
- fix: upgrade-k8s to flag should not be required since there is a default
- fix: successful ACPI shutdown in maintenance mode
- fix: redo assertHostnames in HostnameMergeSuite.TestMerge
- fix: update go-smbios library with Hyper-V data fix
- fix: use passed `--context` in `talosctl config` cmd
- fix: add `--force` flag to `talosctl gen config`
- fix: docker talosctl cluster create provisioner
- fix: add support for a fallback '*' mirror configuration
- fix: improve error message on single node upgrade
- fix: kernel module dependency tree generation
- fix: quote the ampersand character in GRUB config
- fix: talosctl reboot command passing mode in wait mode
- fix: kubernetes removed resource version check
- fix: wait for network and retry in platform get config funcs
- fix: default dns domain to 'cluster.local' in local case
- fix: trackable action flag usage text. --no-wait does not exist
- fix: return proper error if download attempts time out
- fix: correctly quote and unquote strings in GRUB config
- fix: mark DigitalOcean anchor IP as scope link
- fix: unwrap gRPC errors on stop/remove pods check
- fix: build correctly etcd initial cluster URL
- fix: service restart (including extension services)
- fix: bump COSI runtime with the panic controller restart fix
- fix: implement upgrade version checks for Talos 1.4
- fix: send diagnostic output to stderr consistently
- fix: default the manifest namespace if not set
- fix: use proper key usage for apid client certificate
- fix: redact service account key in config in RedactSecrets method
- fix: fix nil pointer panic and incorrect error output
- fix: workaround panic in the kubelet service controller
- fix: update COSI and reset restart backoff on success
- fix: introduce 'overridePath' setting and fix Talos resolver
- fix: use only kube-apiserver endpoints for Talos API access endpoints
- fix: report errors to Equinix Metal event API
- fix: blockdevice size is reported by Linux in 512 blocks always
- fix: partially revert e6c98fdf54425e6382f226e33bccca6f3875aad3a

### 1.4.1

- feat: update Linux to 6.1.25, fix virtio on arm64
- fix: display correct number of machines on dashboard
- fix: do not show control plane status for workers on dashboard
- fix: allow `talosctl cp` to handle special files in `/proc`

### 1.4.2

- fix: properly skip/cleanup controlplane configs for workers
- fix: don't reload control plane pods on cert SANs changes
- fix: enforce nolock option for all NFS mounts by default
- fix: add back required TARGETARCH for installer

### 1.4.4

- fix: revert: set rlimit explicitly in wrapperd

### 1.4.5

- fix: fail quickly if upgrade-k8s is used with multiple nodes
- fix: fall back to external IP when discovering nodes in upgrade-k8s
- fix: refresh kubelet self-issued serving certificates

### 1.4.6

- fix: provide stashed META values before installation
- fix: allow time skew for generated kubeconfig
- fix: do not probe kernel args in dashboard if not needed
- fix: skip DHCP RENEW if server IP in the lease is all zeroes
- fix: upgrade-k8s use internal IP first, external IP fallback


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.4.6**, the newest release recorded here for this line.

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
