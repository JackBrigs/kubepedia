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

**60 defects** the project fixed across **9 releases** of the 1.2 line, from 1.2.0 to
1.2.9. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.2.0

- fix: properly handle `configContext` being `nil` in Talos client
- fix: change the type of returned gRPC connection object from the client
- fix: expose Talos client gRPC connection via the function `Conn`
- fix: get command in the case 'nodes' are not set in the context
- fix: correctly render hosts.toml with multiple endpoints
- fix: update etcd certificates when node addresses changes
- fix: update COSI to the version with gRPC Wait fix
- fix: don't wait for the hostname in maintenance mode
- fix: make 'ca', 'crt' and 'key' flags optional for 'talosctl config add'
- fix: handle grub config being empty in the `Revert` function
- fix: clean up `cancelCtxMu` leftovers in PriorityLock
- fix: make `talosctl` command return nonzero error codes if it had errors
- fix: introduce 'routed' NodeAddresses and use them in kubelet
- fix: properly filter resources in maintenance server
- fix: use controllers/resources for etcd configuration
- fix: reload trusted CA list when client is recreated
- fix: shutdown some streaming API calls when machined API is shuting down
- fix: don't advertise Kubernetes pod networks over KubeSpan by default
- fix: make reset work even if the node is not bootstrapped/not joined
- fix: iterate over etcd members endpoints for member promotion
- fix: update default address if removed from the host
- fix: keep entire vlan id when parsing cmdline
- fix: retry Conflict errors when upgrading k8s manifests
- fix: skip `ResetDuringBoot` test if the `Cluster` config is unknown
- fix: wait for boot done when rebooting a node in the integration tests
- fix: enable stable hostnames for worker configs as well
- fix: folder permissions of overlay mounted folders
- fix: regenerate kubelet certs when hostname changes
- fix: use masks and different firewall mark for KubeSpan
- fix: skip bond itself when matching interface (Equinix Metal)
- fix: update kubelet kubeconfig when cluster control plane endpoint changes
- fix: stabilize etcd join and promote sequences
- fix: avoid double append of `talos.platform` kernel argument
- fix: perform accurate conflict resolution on overal (kubespan)
- fix: provide CA certificates in `/etc/ssl/certs/ca-certificates.crt`
- fix: filter static pods correctly and optimize fetching
- fix: update crypto library with support for RSA-SHA*
- fix: generate correct bootstrap manifests when only IPv6 CIDR is used
- fix: create native image format for DigitalOcean
- fix: siderlink api assume port 443 with https schema
- fix: enable orderly poweroff in hyper-v on Azure
- fix: make `talosctl bootstrap` accept only single node
- fix: support SideroLink "secure" gRPC connection
- fix: wait for `/var` to be mounted in kubelet service controller
- fix: ignore errors on duplicate `SetHeader` calls

### 1.2.1

- fix: automatically discard VIPs for etcd advertised addresses
- fix: prevent panic on health check if a member has no IPs

### 1.2.2

- fix: stop worker nodes from acting as apid routers
- fix: never sign client certificate requests in trustd
- fix: include all node addresses into etcd cert SANs
- fix: list COSI APIs for the apid authenticator
- fix: pass a pointer to specs.Mount into protoenc.Marshal

### 1.2.3

- fix: ensure that custom Decoder gets called for netaddr.IP

### 1.2.4

- fix: lookup Equinix Metal bond slaves using 'permanent addr'
- fix: update discovery client with the redirect fix

### 1.2.5

- feat: patch Linux kernel with UEFI randomize fix

### 1.2.7

- fix: limit SideroLink Wireguard link MTU to 1280
- fix: generate correct Flannel config for IPv6-only clusters

### 1.2.8

- fix: workaround panic in the kubelet service controller

### 1.2.9

- fix: easier upgrade to Talos 1.3 with custom CRI config


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
