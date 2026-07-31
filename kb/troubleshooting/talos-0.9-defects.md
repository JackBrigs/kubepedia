---
id: TROUBLE-TALOS_0_9_DEFECTS
type: troubleshooting
title: "talos 0.9: defects fixed in the 0.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.9.0 <0.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 0.9 known issues
  - talos 0.9 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 0.9 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 0.9: defects fixed in the 0.9 line

## Summary

**258 defects** the project fixed across **4 releases** of the 0.9 line, from 0.9.0 to
0.9.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.9.0

- fix: command `etcd remove-member` shouldn't remove etcd data directory
- fix: upgrade-k8s bug with empty config values and provision script
- fix: talosctl health should not check kube-proxy when it is disabled
- fix: properly format spec comments in the resources
- fix: don't touch any partitions on upgrade with --preserve
- fix: move containerd CRI config files under `/var/`
- fix: do not print out help string if the parameters are correct
- fix: mkdir source of the extra mounts for the kubelet
- fix: properly propagate nameservers to provisioned docker clusters
- fix: ignore connection refused errors when updating/converting cp
- fix: align partition start to the physical sector size
- fix: chmod etcd PKI path to fix virtual IP for upgrades with persistence
- fix: ignore 'ENOENT' (no such file directory) on mount
- fix: update in-cluster kubeconfig validity to match other certs
- fix: add ApplyDynamicConfig call in the apply-config --immediate mode
- fix: set hdmi_safe=1 on Raspberry Pi for maximum HDMI compatibility
- fix: show stopped/exited containers via CRI inspector
- fix: correctly set service state in the resource
- fix: update the layout of the Disks API to match proxying requirements
- fix: stop and clean up installer container correctly
- fix: sanitize volume name better in static pod extra volumes
- fix: redirect warnings in manifest apply k8s client
- fix: handle case when kubelet serving certificates are issued
- fix: correctly escape extra args in kube-proxy manifest
- fix: correctly unwrap responses for etcd commands
- fix: move versions to annotations in control plane static pods
- fix: find master node IPs correctly in health checks
- fix: don't use filename from URL when downloading manifest
- fix: correct response structure for GenerateConfig API
- fix: correctly extract wrapped error messages
- fix: prevent crash in machined on apid service stop
- fix: wait for time sync before generating Kubernetes certificates
- fix: mount kubelet secrets from system instead of ephemeral
- fix: prefer configured nameservers, fix DHCP6 in container
- fix: refresh control plane endpoints on worker apids on schedule
- fix: update DHCP client to use Request-Ack sequence after an Offer
- fix: use grpc load-balancing when connecting to trustd
- fix: lower memory usage a bit by disabling memory profiling
- fix: prefix rendered Talos-owned static pod manifests
- fix: bump timeout for worker apid waiting for kubelet client config
- fix: kill all processes and umount all disk on reboot/shutdown
- fix: open blockdevices with exclusive flock for partitioning
- fix: list command unlimited recursion default behavior
- fix: pick first interface valid hostname (vs. last one)
- fix: allow 'console' argument in kernel args to be always overridden
- fix: bring up bonded interfaces correctly on packet
- fix: checkpoint controller-manager and scheduler
- fix: correctly transport gRPC errors from apid
- fix: use SetAll instead of AppendAll when building kernel args
- fix: add more dependencies for bootstrap services
- fix: pass disk image flags to e2e-qemu cluster create command
- fix: ignore pods spun up from checkpoints in health checks
- fix: ignore errors on stopping/removing pod sandboxes
- fix: use the correct console on Banana Pi M64
- fix: don't run LabelNodeAsMaster in two sequences
- fix: command `etcd remove-member` shouldn't remove etcd
- fix: upgrade-k8s bug with empty config values and provis
- fix: function NewKeyPair should create certificate with proper subject
- fix: align partition start to physical sector size
- fix: properly handle no child processes error from cmd.Wait
- fix: attach stack trace to panic error message
- fix: preserve original YAML formatting in resource.Any

### 0.9.1

- fix: prevent panic in validate config if `machine.install` is missing
- fix: allow `convert-k8s --remove-initialized-keys` with K8s cp is down
- fix: get rid of data race in encoder and fix concurrent map access
- fix: resolve the issue with DHCP lease not being renewed
- fix: command `etcd remove-member` shouldn't remove etcd data directory
- fix: upgrade-k8s bug with empty config values and provision script
- fix: talosctl health should not check kube-proxy when it is disabled
- fix: properly format spec comments in the resources
- fix: don't touch any partitions on upgrade with --preserve
- fix: move containerd CRI config files under `/var/`
- fix: do not print out help string if the parameters are correct
- fix: mkdir source of the extra mounts for the kubelet
- fix: properly propagate nameservers to provisioned docker clusters
- fix: ignore connection refused errors when updating/converting cp
- fix: align partition start to the physical sector size
- fix: chmod etcd PKI path to fix virtual IP for upgrades with persistence
- fix: ignore 'ENOENT' (no such file directory) on mount
- fix: update in-cluster kubeconfig validity to match other certs
- fix: add ApplyDynamicConfig call in the apply-config --immediate mode
- fix: set hdmi_safe=1 on Raspberry Pi for maximum HDMI compatibility
- fix: show stopped/exited containers via CRI inspector
- fix: correctly set service state in the resource
- fix: update the layout of the Disks API to match proxying requirements
- fix: stop and clean up installer container correctly
- fix: sanitize volume name better in static pod extra volumes
- fix: redirect warnings in manifest apply k8s client
- fix: handle case when kubelet serving certificates are issued
- fix: correctly escape extra args in kube-proxy manifest
- fix: correctly unwrap responses for etcd commands
- fix: move versions to annotations in control plane static pods
- fix: find master node IPs correctly in health checks
- fix: don't use filename from URL when downloading manifest
- fix: correct response structure for GenerateConfig API
- fix: correctly extract wrapped error messages
- fix: prevent crash in machined on apid service stop
- fix: wait for time sync before generating Kubernetes certificates
- fix: mount kubelet secrets from system instead of ephemeral
- fix: prefer configured nameservers, fix DHCP6 in container
- fix: refresh control plane endpoints on worker apids on schedule
- fix: update DHCP client to use Request-Ack sequence after an Offer
- fix: use grpc load-balancing when connecting to trustd
- fix: lower memory usage a bit by disabling memory profiling
- fix: prefix rendered Talos-owned static pod manifests
- fix: bump timeout for worker apid waiting for kubelet client config
- fix: kill all processes and umount all disk on reboot/shutdown
- fix: open blockdevices with exclusive flock for partitioning
- fix: list command unlimited recursion default behavior
- fix: pick first interface valid hostname (vs. last one)
- fix: allow 'console' argument in kernel args to be always overridden
- fix: bring up bonded interfaces correctly on packet
- fix: checkpoint controller-manager and scheduler
- fix: correctly transport gRPC errors from apid
- fix: use SetAll instead of AppendAll when building kernel args
- fix: add more dependencies for bootstrap services
- fix: pass disk image flags to e2e-qemu cluster create command
- fix: ignore pods spun up from checkpoints in health checks
- fix: ignore errors on stopping/removing pod sandboxes
- fix: use the correct console on Banana Pi M64
- fix: don't run LabelNodeAsMaster in two sequences
- fix: function NewKeyPair should create certificate with proper subject
- fix: align partition start to physical sector size
- fix: properly handle no child processes error from cmd.Wait
- fix: attach stack trace to panic error message
- fix: preserve original YAML formatting in resource.Any

### 0.9.2

- fix: zero out manifest contents before setting new value
- fix: ignore EOF errors from Kubernetes API when converting control plane
- fix: prevent panic in validate config if `machine.install` is missing
- fix: allow `convert-k8s --remove-initialized-keys` with K8s cp is down
- fix: get rid of data race in encoder and fix concurrent map access
- fix: resolve the issue with DHCP lease not being renewed
- fix: command `etcd remove-member` shouldn't remove etcd data directory
- fix: upgrade-k8s bug with empty config values and provision script
- fix: talosctl health should not check kube-proxy when it is disabled
- fix: properly format spec comments in the resources
- fix: don't touch any partitions on upgrade with --preserve
- fix: move containerd CRI config files under `/var/`
- fix: do not print out help string if the parameters are correct
- fix: mkdir source of the extra mounts for the kubelet
- fix: properly propagate nameservers to provisioned docker clusters
- fix: ignore connection refused errors when updating/converting cp
- fix: align partition start to the physical sector size
- fix: chmod etcd PKI path to fix virtual IP for upgrades with persistence
- fix: ignore 'ENOENT' (no such file directory) on mount
- fix: update in-cluster kubeconfig validity to match other certs
- fix: add ApplyDynamicConfig call in the apply-config --immediate mode
- fix: set hdmi_safe=1 on Raspberry Pi for maximum HDMI compatibility
- fix: show stopped/exited containers via CRI inspector
- fix: correctly set service state in the resource
- fix: update the layout of the Disks API to match proxying requirements
- fix: stop and clean up installer container correctly
- fix: sanitize volume name better in static pod extra volumes
- fix: redirect warnings in manifest apply k8s client
- fix: handle case when kubelet serving certificates are issued
- fix: correctly escape extra args in kube-proxy manifest
- fix: correctly unwrap responses for etcd commands
- fix: move versions to annotations in control plane static pods
- fix: find master node IPs correctly in health checks
- fix: don't use filename from URL when downloading manifest
- fix: correct response structure for GenerateConfig API
- fix: correctly extract wrapped error messages
- fix: prevent crash in machined on apid service stop
- fix: wait for time sync before generating Kubernetes certificates
- fix: mount kubelet secrets from system instead of ephemeral
- fix: prefer configured nameservers, fix DHCP6 in container
- fix: refresh control plane endpoints on worker apids on schedule
- fix: update DHCP client to use Request-Ack sequence after an Offer
- fix: use grpc load-balancing when connecting to trustd
- fix: lower memory usage a bit by disabling memory profiling
- fix: prefix rendered Talos-owned static pod manifests
- fix: bump timeout for worker apid waiting for kubelet client config
- fix: kill all processes and umount all disk on reboot/shutdown
- fix: open blockdevices with exclusive flock for partitioning
- fix: list command unlimited recursion default behavior
- fix: pick first interface valid hostname (vs. last one)
- fix: allow 'console' argument in kernel args to be always overridden
- fix: bring up bonded interfaces correctly on packet
- fix: checkpoint controller-manager and scheduler
- fix: correctly transport gRPC errors from apid
- fix: use SetAll instead of AppendAll when building kernel args
- fix: add more dependencies for bootstrap services
- fix: pass disk image flags to e2e-qemu cluster create command
- fix: ignore pods spun up from checkpoints in health checks
- fix: ignore errors on stopping/removing pod sandboxes
- fix: use the correct console on Banana Pi M64
- fix: don't run LabelNodeAsMaster in two sequences
- fix: function NewKeyPair should create certificate with proper subject
- fix: align partition start to physical sector size
- fix: properly handle no child processes error from cmd.Wait
- fix: attach stack trace to panic error message
- fix: preserve original YAML formatting in resource.Any

### 0.9.3

- fix: zero out manifest contents before setting new value
- fix: ignore EOF errors from Kubernetes API when converting control plane
- fix: prevent panic in validate config if `machine.install` is missing
- fix: allow `convert-k8s --remove-initialized-keys` with K8s cp is down
- fix: get rid of data race in encoder and fix concurrent map access
- fix: resolve the issue with DHCP lease not being renewed
- fix: command `etcd remove-member` shouldn't remove etcd data directory
- fix: upgrade-k8s bug with empty config values and provision script
- fix: talosctl health should not check kube-proxy when it is disabled
- fix: properly format spec comments in the resources
- fix: don't touch any partitions on upgrade with --preserve
- fix: move containerd CRI config files under `/var/`
- fix: do not print out help string if the parameters are correct
- fix: mkdir source of the extra mounts for the kubelet
- fix: properly propagate nameservers to provisioned docker clusters
- fix: ignore connection refused errors when updating/converting cp
- fix: align partition start to the physical sector size
- fix: chmod etcd PKI path to fix virtual IP for upgrades with persistence
- fix: ignore 'ENOENT' (no such file directory) on mount
- fix: update in-cluster kubeconfig validity to match other certs
- fix: add ApplyDynamicConfig call in the apply-config --immediate mode
- fix: set hdmi_safe=1 on Raspberry Pi for maximum HDMI compatibility
- fix: show stopped/exited containers via CRI inspector
- fix: correctly set service state in the resource
- fix: update the layout of the Disks API to match proxying requirements
- fix: stop and clean up installer container correctly
- fix: sanitize volume name better in static pod extra volumes
- fix: redirect warnings in manifest apply k8s client
- fix: handle case when kubelet serving certificates are issued
- fix: correctly escape extra args in kube-proxy manifest
- fix: correctly unwrap responses for etcd commands
- fix: move versions to annotations in control plane static pods
- fix: find master node IPs correctly in health checks
- fix: don't use filename from URL when downloading manifest
- fix: correct response structure for GenerateConfig API
- fix: correctly extract wrapped error messages
- fix: prevent crash in machined on apid service stop
- fix: wait for time sync before generating Kubernetes certificates
- fix: mount kubelet secrets from system instead of ephemeral
- fix: prefer configured nameservers, fix DHCP6 in container
- fix: refresh control plane endpoints on worker apids on schedule
- fix: update DHCP client to use Request-Ack sequence after an Offer
- fix: use grpc load-balancing when connecting to trustd
- fix: lower memory usage a bit by disabling memory profiling
- fix: prefix rendered Talos-owned static pod manifests
- fix: bump timeout for worker apid waiting for kubelet client config
- fix: kill all processes and umount all disk on reboot/shutdown
- fix: open blockdevices with exclusive flock for partitioning
- fix: list command unlimited recursion default behavior
- fix: pick first interface valid hostname (vs. last one)
- fix: allow 'console' argument in kernel args to be always overridden
- fix: bring up bonded interfaces correctly on packet
- fix: checkpoint controller-manager and scheduler
- fix: correctly transport gRPC errors from apid
- fix: use SetAll instead of AppendAll when building kernel args
- fix: add more dependencies for bootstrap services
- fix: pass disk image flags to e2e-qemu cluster create command
- fix: ignore pods spun up from checkpoints in health checks
- fix: ignore errors on stopping/removing pod sandboxes
- fix: use the correct console on Banana Pi M64
- fix: don't run LabelNodeAsMaster in two sequences
- fix: function NewKeyPair should create certificate with proper subject
- fix: align partition start to physical sector size
- fix: properly handle no child processes error from cmd.Wait
- fix: attach stack trace to panic error message
- fix: preserve original YAML formatting in resource.Any


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.9.3**, the newest release recorded here for this line.

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
