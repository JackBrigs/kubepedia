---
id: TROUBLE-CALICO_3_29_DEFECTS
type: troubleshooting
title: "calico 3.29: defects fixed in the 3.29 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.29.0 <3.30.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - calico 3.29 known issues
  - calico 3.29 fixed in
  - is this calico bug already fixed
tags:
  - troubleshooting
  - upgrade
  - calico
sources:
  - type: docs
    path: projectcalico/calico release notes for the 3.29 line — bug-fix entries
    url: https://github.com/projectcalico/calico/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# calico 3.29: defects fixed in the 3.29 line

## Summary

**91 defects** the project fixed across **8 releases** of the 3.29 line, from 3.29.0 to
3.29.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.29.0

- Fixed memory leak in BPF endpoint manager. [calico 9309](https://github.com/projectcalico/calico/pull/9309) (@tomastigera)
- ebpf: Fix for Istio ambient mode - traffic that arrives from host should go back through host and not skip iptables [calico 9192](https://github.com/projectcalico/calico/pull/9192) (@tomastigera)
- ebpf: When bpfConntrackBypass is disabled, ensure that iptables rules, which allow 3rd party iptables rules work for traffic originally for the host, are in place. [calico 9188](https://github.com/projectcalico/calico/pull/9188) (@tomastigera)
- ebpf: Fixed frequently attaching BPF programs when pods annotations/labels change and eventually failing due to running out of tc priority. [calico 9089](https://github.com/projectcalico/calico/pull/9089) (@sridhartigera)
- ebpf: Fix parsing host IP update and re-attach program on all interfaces when there is a host IP update. [calico 9084](https://github.com/projectcalico/calico/pull/9084) (@sridhartigera)
- Fixed Missing routes for UDP services when in dual stack mode. [calico 9050](https://github.com/projectcalico/calico/pull/9050) (@sridhartigera)
- ebpf: Fixed bug that would leave residual logging when log filters were applied and then disabled. [calico 9137](https://github.com/projectcalico/calico/pull/9137) (@tomastigera)
- ebpf: Attach XDP to bond slave devices. [calico 9132](https://github.com/projectcalico/calico/pull/9132) (@sridhartigera)
- ebpf: Fix Felix panic when using non-default BPF map sizes. Size was not updated in all places resulting in failure to attach programs. [calico 9117](https://github.com/projectcalico/calico/pull/9117) (@fasaxc)
- ebpf: Fixes missing iptables rules that would keep preexisting V6 connections working when switching to ebpf mode [calico 8943](https://github.com/projectcalico/calico/pull/8943) (@tomastigera)
- ebpf: Don't drop, but reject unknown midflow tcp packets with rst [calico 8933](https://github.com/projectcalico/calico/pull/8933) (@tomastigera)
- ebpf: Set bpfin/out.cali MTU to the smallest of all host ifaces including overlay. That means if jumbo frames are used, this device also uses them. [calico 8922](https://github.com/projectcalico/calico/pull/8922) (@tomastigera)
- ebpf: Fix - let the node handle packet when we are not sure about the destination [calico 8921](https://github.com/projectcalico/calico/pull/8921) (@tomastigera)
- ebpf: Cleanup BPF special devices when BPF is turned off [calico 8884](https://github.com/projectcalico/calico/pull/8884) (@tomastigera)
- ebpf: Support for service loop prevention [calico 8876](https://github.com/projectcalico/calico/pull/8876) (@sridhartigera)
- ebpf: Fixed forwarding, NATing and checksumming of related ICMP traffic (icmp errors) [calico 8858](https://github.com/projectcalico/calico/pull/8858) (@tomastigera)
- ebpf: If a bond master device is part of the bpfDataIfacePattern regexp, calico attaches to it and not to the slaves [calico 8803](https://github.com/projectcalico/calico/pull/8803) (@sridhartigera)
- ebpf: Forwarding services via vxlan tunnel uses different source ports for different flows to better utilize bonded devices and CPUs on the receiving side. [calico 8790](https://github.com/projectcalico/calico/pull/8790) (@tomastigera)
- ebpf: Do not panic in dual-stack mode when a node is configured with only one and not both IPs or autodetection is not enabled for one. [calico 8760](https://github.com/projectcalico/calico/pull/8760) (@tomastigera)
- ebpf: Clean up stale icmp6 conntrack entries [calico 8749](https://github.com/projectcalico/calico/pull/8749) (@tomastigera)
- ebpf: Update map definition in sockops program to let libbpf v1.0+ load them successfully. [calico 8693](https://github.com/projectcalico/calico/pull/8693) (@debasishbsws)
- ebpf: Fix map creation during upgrade. [calico 8684](https://github.com/projectcalico/calico/pull/8684) (@sridhartigera)
- ebpf: Fix natOutgoing SNAT for icmp6 [calico 8679](https://github.com/projectcalico/calico/pull/8679) (@sridhartigera)
- Configure kubelet certificate rotation on manually installed Calico for Windows. [calico 9178](https://github.com/projectcalico/calico/pull/9178) (@jxlwqq)
- Added support for non-English language versions of Windows. [calico 9062](https://github.com/projectcalico/calico/pull/9062) (@wayne-cheng)
- Fix non-HPC Calico for Windows startup issue with the CalicoNode service. [calico 9016](https://github.com/projectcalico/calico/pull/9016) (@coutinhop)
- [windows] Skip node IP discovery if --NodeIp parameter is provided to kubelet-service.ps1. [calico 8915](https://github.com/projectcalico/calico/pull/8915) (@wayne-cheng)
- Helm: Fix error parsing kubernetesServiceEndpoint.host as an integer [calico 9067](https://github.com/projectcalico/calico/pull/9067) (@MichalFupso)
- Helm: Fix rendering of KUBERNETES_SERVICE_PORT [calico 8865](https://github.com/projectcalico/calico/pull/8865) (@simonostendorf)
- Fix error when using helm additionalLabels in conjunction with image pull secrets [calico 8785](https://github.com/projectcalico/calico/pull/8785) (@caseydavenport)
- Fix spurious warning about unexpected inserted rules. [calico 9397](https://github.com/projectcalico/calico/pull/9397) (@fasaxc)
- Fix image in flannel migration manifest [calico 9265](https://github.com/projectcalico/calico/pull/9265) (@radTuti)
- Ignore empty CIDRs specified in the BGPConfiguration. [calico 9230](https://github.com/projectcalico/calico/pull/9230) (@fasaxc)
- Update flannel to version v0.24.4 to fix kube-flannel log spam when ipv6 is disabled. [calico 9208](https://github.com/projectcalico/calico/pull/9208) (@mkhpalm)
- [etcd mode] Fix issue where Calico nodes failed to decommission if calico-kube-controllers was running on the terminated node. [calico 9190](https://github.com/projectcalico/calico/pull/9190) (@caseydavenport)
- BGP: Prevent the advertisement of local kernel routes learned from eBPF interfaces (bpf*.cali) to peers. [calico 9112](https://github.com/projectcalico/calico/pull/9112) (@mstansberry)
- Fix that shutting down a ticker waited a whole tick. (Mainly impacts tests.) [calico 9111](https://github.com/projectcalico/calico/pull/9111) (@fasaxc)
- Fix interaction between kube-proxy and Calico's SNAT rules that could cause corrupted VXLAN packets when checksum offload was enabled. Move Calico's rules after kube-proxy's to make sure kube-proxy's mark bit is cleared if both would have done SNAT. [calico 9091](https://github.com/projectcalico/calico/pull/9091) (@tomastigera)
- Fix that Felix would panic when trying to resync a temporary IP set. Temporary IP sets are created in certain scenarios after previous failures. [calico 9077](https://github.com/projectcalico/calico/pull/9077) (@fasaxc)
- Fix missing resources in calicoctl command help text [calico 9054](https://github.com/projectcalico/calico/pull/9054) (@caseydavenport)
- Calico now uses the logging framework's built in capability to capture the caller's filename/line number. This removes a potential source of concurrency bugs. [calico 9044](https://github.com/projectcalico/calico/pull/9044) (@fasaxc)
- Fix that the conversion from Pod to WorkloadEndpoint could mutate the pod labels; this isn't safe if something else has a reference to the Pod (e.g. if we're used with a caching informer). [calico 9039](https://github.com/projectcalico/calico/pull/9039) (@fasaxc)
- Fix 'undefined symbol: xtables_strdup' error when running 'iptables-legacy-save' in the calico-node image. [calico 9022](https://github.com/projectcalico/calico/pull/9022) (@coutinhop)
- Fixed continuous addition/deletion of service routes in eBPF mode. [calico 8983](https://github.com/projectcalico/calico/pull/8983) (@sridhartigera)
- Felix now arranges for VXLAN packets to skip netfilter conntrack. VXLAN uses pseudo random source ports so the "flows" are unidirectional and not meaningful to conntrack. [calico 8977](https://github.com/projectcalico/calico/pull/8977) (@cyclinder)
- Add IPReservation and BGPFilter to etcd datastore migration [calico 8971](https://github.com/projectcalico/calico/pull/8971) (@caseydavenport)
- Don't run pprof on prometheus metrics port [calico 8967](https://github.com/projectcalico/calico/pull/8967) (@caseydavenport)
- Felix: Move log initialisation earlier in start-up sequence to avoid missing some logs. [calico 8944](https://github.com/projectcalico/calico/pull/8944) (@fasaxc)
- Felix now sets the Go runtime's GC threshold to 40% (instead of the more aggressive 20% used previously). This trades slight extra RAM usage for significantly lower GC CPU usage. The setting is now exposed in the FelixConfiguration as goGCThreshold, along with goMemoryLimitMB. To get the old behaviour, set goGCThreshold to 20. If memory usage is not a concern, the value can be set even higher to reduce CPU usage. [calico 8904](https://github.com/projectcalico/calico/pull/8904) (@fasaxc)
- Upgrade bpftool to v7.4 to fix the issue of loading XDP programs in iptables data plane that happens in few distributions. [calico 8880](https://github.com/projectcalico/calico/pull/8880) (@mazdakn)
- Reduce spammy logs in route table [calico 8879](https://github.com/projectcalico/calico/pull/8879) (@caseydavenport)
- Fixed incorrect logging level related to service IPs. [calico 8816](https://github.com/projectcalico/calico/pull/8816) (@mazdakn)
- Fix that Calico would ignore changes to Kubernetes Node InternalIP when using InternalIP node address autodetection. [calico 8728](https://github.com/projectcalico/calico/pull/8728) (@Levi080513)
- ebpf: wg6 traffic is allowed even if blocked by policy [calico 8712](https://github.com/projectcalico/calico/pull/8712) (@tomastigera)
- Fix pods stuck in ContainerCreating state due to "failed to create host netlink handle: protocol not supported" error on kernels that don't support XFRM. [calico 8710](https://github.com/projectcalico/calico/pull/8710) (@carloslima)
- Fix missing log line numbers in cni-installer log output [calico 8696](https://github.com/projectcalico/calico/pull/8696) (@caseydavenport)
- Restart calico/node if unable to set the NodeNetwork condition. [calico 8673](https://github.com/projectcalico/calico/pull/8673) (@cyclinder)
- Clean up IP addresses of pods with Evicted status. [calico 7713](https://github.com/projectcalico/calico/pull/7713) (@gaopeiliang)

### 3.29.1

- Fix that the new tiers resource was omitted from etcd->Kubernetes migration. [calico 9494](https://github.com/projectcalico/calico/pull/9494) (@fasaxc)
- Fix a panic in Felix when accessing a nil address in flushing host addresses, i.e. flushHostIPUpdates function. [calico 9488](https://github.com/projectcalico/calico/pull/9488) (@mazdakn)
- Add permission to Calico API server to create tier resources. [calico 9484](https://github.com/projectcalico/calico/pull/9484) (@mazdakn)
- Do not fail data store initialisation when unauthorised error happen while creating default and adminnetworkpolicy tiers. Those tiers eventually get created by another component. [calico 9454](https://github.com/projectcalico/calico/pull/9454) (@mazdakn)
- Helm: Fix that uninstall Job had duplicate k8s-app labels [calico 9439](https://github.com/projectcalico/calico/pull/9439) (@caseydavenport)
- Fix missing routes when vxlan mode is cross-subnet and the environment is purely V6 (no V4 host addresses) [calico 9430](https://github.com/projectcalico/calico/pull/9430) (@tomastigera)

### 3.29.2

- ebpf: fix icmp error delivery to host networked pods [calico 9749](https://github.com/projectcalico/calico/pull/9749) (@tomastigera)
- ebpf: fixed routing from outside the cluster in EKS with aws-cni [calico 9629](https://github.com/projectcalico/calico/pull/9629) (@tomastigera)
- Fix: Map OpenStack-derived policy to the "default" tier, not "ossg". [calico 9778](https://github.com/projectcalico/calico/pull/9778) (@nelljerram)
- Fix that libcalico-go would not always fill in the revision when listing certain resources (or single instances of certain resources). This could result in missed watch events in components such as Typha. [calico 9689](https://github.com/projectcalico/calico/pull/9689) (@fasaxc)
- Fix that nodes with borrowed VXLAN tunnel addresses were not reachable by pods. [calico 9685](https://github.com/projectcalico/calico/pull/9685) (@caseydavenport)
- Fix spammy Tier already exists log from kube-controllers. [calico 9671](https://github.com/projectcalico/calico/pull/9671) (@fasaxc)
- Fixed file handle leak in felix, caused by failing to close netlink handles. [calico 9612](https://github.com/projectcalico/calico/pull/9612) (@fasaxc)
- Fix that non-amd64 builds of node-driver-registrar contained x86 binaries. [calico 9601](https://github.com/projectcalico/calico/pull/9601) (@caseydavenport)
- Fix that in-use VXLAN ARP entries could be repeatedly cleaned up and then re-added if they shared a MAC address with an stale entry that was supposed to be cleaned up. [calico 9582](https://github.com/projectcalico/calico/pull/9582) (@fasaxc)
- Felix: fix that a map used to cache loaded datastore keys would always use RAM proportional to the total number of keys rather than shrinking when no longer needed. [calico 9538](https://github.com/projectcalico/calico/pull/9538) (@fasaxc)

### 3.29.3

- Fix race when setting wireguard NAPI setting that could cause the NAPI setting not to be applied for several minutes. [calico 9801](https://github.com/projectcalico/calico/pull/9801) (@fasaxc)

### 3.29.4

- Change OpenShift manifests order to fix an error when creating HCP clusters. [calico 10255](https://github.com/projectcalico/calico/pull/10255) (@coutinhop)
- Fix missing RBAC permissions for kube-controller-manager to access tiers in manifest installs, which was preventing proper resource garbage collection. [calico 10230](https://github.com/projectcalico/calico/pull/10230) (@caseydavenport)
- ebpf - Fix dropping packets from workloads to host interfaces not managed by calico. [calico 10226](https://github.com/projectcalico/calico/pull/10226) (@sridhartigera)
- ebpf - Fix configuring arp entries for bpf NAT devices for systemd >= 242 [calico 10217](https://github.com/projectcalico/calico/pull/10217) (@sridhartigera)
- ebpf - Fixed a bug where BPF programs were being re-attached to network interfaces unnecessarily, even when the host IP address had not changed. [calico 10164](https://github.com/projectcalico/calico/pull/10164) (@sridhartigera)

### 3.29.5

- Fix CalicoNodeStatus updates could get blocked by datastore errors [calico 10594](https://github.com/projectcalico/calico/pull/10594) (@theboringstuff)
- ebpf: Fixed mounting cgroupv2 for connect time load balancing. [calico 10505](https://github.com/projectcalico/calico/pull/10505) (@sridhartigera)
- ebpf: Fixed attaching bpf programs by atomically replacing the old program rather than attaching new and detaching old. [calico 10455](https://github.com/projectcalico/calico/pull/10455) (@sridhartigera)

### 3.29.6

- eBPF: Fix race between loading kubernetes services and conntrack cleanup. If conntrack cleanup ran before services were loaded, all service entries would look stale and get cleaned up. [calico 10725](https://github.com/projectcalico/calico/pull/10725) (@fasaxc)
- Add validation to guard against catch-all CIDRs (e.g. 0.0.0.0/0) on negated (notnets) policy rules, as those would effectively disallow all addresses. [calico 10687](https://github.com/projectcalico/calico/pull/10687) (@dzacball)

### 3.29.7

- ebpf: Fixed loading connecttime load balancer program in 6.12 kernel [calico 11405](https://github.com/projectcalico/calico/pull/11405) (@sridhartigera)
- Fix AllowSpoofedSourcePrefixes for dual stack clusters. [calico 11374](https://github.com/projectcalico/calico/pull/11374) (@lucastigera)
- Fix (release-tool): include image tarballs in release archive file [calico 11297](https://github.com/projectcalico/calico/pull/11297) (@radTuti)
- Fix: reinstate support for VMs that are configured not to respond to ARP requests. [calico 11271](https://github.com/projectcalico/calico/pull/11271) (@nelljerram)
- Fix that IPAM allocation could leak handles when many workloads are scheduled to the same node at the same time, causing timeouts by "thundering herd". [calico 11097](https://github.com/projectcalico/calico/pull/11097) (@fasaxc)
- Make Calico's backing CRDs optional. Calico will no longer fail to start if a CRD is missing. [calico 11037](https://github.com/projectcalico/calico/pull/11037) (@caseydavenport)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.29.7**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `projectcalico/calico`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/calico.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
