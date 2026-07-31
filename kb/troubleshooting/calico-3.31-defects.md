---
id: TROUBLE-CALICO_3_31_DEFECTS
type: troubleshooting
title: "calico 3.31: defects fixed in the 3.31 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.31.0 <3.32.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - calico 3.31 known issues
  - calico 3.31 fixed in
  - is this calico bug already fixed
tags:
  - troubleshooting
  - upgrade
  - calico
sources:
  - type: docs
    path: projectcalico/calico release notes for the 3.31 line — bug-fix entries
    url: https://github.com/projectcalico/calico/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# calico 3.31: defects fixed in the 3.31 line

## Summary

**88 defects** the project fixed across **6 releases** of the 3.31 line, from 3.31.0 to
3.31.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.31.0

- Fix slow IPAM release performance when releasing IPs from disabled or deleted pools (especially for bulk deletions like those done by IPAM GC). Consider disabled pools as potential IP owners and cache any loaded blocks for fast access. [calico 11094](https://github.com/projectcalico/calico/pull/11094) (@fasaxc)
- Fix race condition that could result in a Wireguard IP not being assigned. [calico 10883](https://github.com/projectcalico/calico/pull/10883) (@caseydavenport)
- Calico waits until networking is fully established before setting the NetworkUnavailable=false condition. [calico 10866](https://github.com/projectcalico/calico/pull/10866) (@caseydavenport)
- Add missing staged policy permissions to apiserver.yaml [calico 11031](https://github.com/projectcalico/calico/pull/11031) (@caseydavenport)
- Fix that whisker wouldn't bind to IPv6 addresses. [calico 10839](https://github.com/projectcalico/calico/pull/10839) (@caseydavenport)
- Fix confd on Windows by skipping watching endpoint status files. [calico 10691](https://github.com/projectcalico/calico/pull/10691) (@song-jiang)
- Fix that IPAM allocation could leak handles when many workloads are scheduled to the same node at the same time, causing timeouts by "thundering herd". [calico 10658](https://github.com/projectcalico/calico/pull/10658) (@fasaxc)
- Fix: In Calico for OpenStack the operation to rebuild a VM could sometimes fail to complete successfully, with the VM getting stuck in ERROR state. (Completion of #10608) [calico 10656](https://github.com/projectcalico/calico/pull/10656) (@nelljerram)
- Fix that CalicoNodeStatus updates could get blocked by datastore errors [calico 10555](https://github.com/projectcalico/calico/pull/10555) (@theboringstuff)
- Reduce log level for spammy IPv6 RA log when IPv6 is disabled. [calico 10553](https://github.com/projectcalico/calico/pull/10553) (@caseydavenport)
- Helm: fix role binding to use correct serviceaccount name when deployed in an alternative namespace. [calico 10516](https://github.com/projectcalico/calico/pull/10516) (@caseydavenport)
- Fix race condition in Goldmane startup [calico 10512](https://github.com/projectcalico/calico/pull/10512) (@caseydavenport)
- Fix Goldmane race condition when terminating streams [calico 10508](https://github.com/projectcalico/calico/pull/10508) (@caseydavenport)
- windows: fix connections occasionally being reset on periodic updates when HNS rules had not been modified [calico 10437](https://github.com/projectcalico/calico/pull/10437) (@song-jiang)
- Disable WatchList in Calico API server, fixing issue with stuck Namespace termination. [calico 10433](https://github.com/projectcalico/calico/pull/10433) (@caseydavenport)
- Add missing tiers permissions for flannel migration controller [calico 10383](https://github.com/projectcalico/calico/pull/10383) (@caseydavenport)
- Fix flannel migration use of deprecated flag "delete-local-data" [calico 10377](https://github.com/projectcalico/calico/pull/10377) (@caseydavenport)
- Fix a panic in calicoctl when using a wrong WorkloadEndpoint name with a specific format. [calico 10355](https://github.com/projectcalico/calico/pull/10355) (@coutinhop)
- Fix spammy logs when handling endpoint status creation events. [calico 10326](https://github.com/projectcalico/calico/pull/10326) (@song-jiang)
- Fail and retry if mtu file is failed to be written or not found. [calico 10270](https://github.com/projectcalico/calico/pull/10270) (@lubronzhan)
- Fix Operator not installing manifests in the correct order when creating OpenShift HCP clusters [calico 10246](https://github.com/projectcalico/calico/pull/10246) (@coutinhop)
- Fix dangling symlink preventing programs from launching on the s390x architecture. [calico 10205](https://github.com/projectcalico/calico/pull/10205) (@hjiawei)
- Fix potential nil pointer access in confd getNodeMeshPasswordKVPair. [calico 10113](https://github.com/projectcalico/calico/pull/10113) (@fasaxc)
- Fix various spammy warning logs. [calico 10088](https://github.com/projectcalico/calico/pull/10088) (@fasaxc)
- Fix a bug where the Calico APIserver would restart for all updates to the `extension-apiserver-authentication`, regardless of whether the ConfigMap's data actually changed. [calico 9719](https://github.com/projectcalico/calico/pull/9719) (@aaaaaaaalex)
- nftables: fix reprogramming of base chain rules after out-of-band flush. [calico 10936](https://github.com/projectcalico/calico/pull/10936) (@caseydavenport)
- ebpf: do not blindly redirect back to the same host iface (regression from 3.29) [calico 11154](https://github.com/projectcalico/calico/pull/11154) (@tomastigera)
- ebpf: some old kernels do not verify ipv4 defrag code correctly. We disable the code if the kernel does not have CO-RE or bpf_loop() (~<5.17) [calico 10859](https://github.com/projectcalico/calico/pull/10859) (@tomastigera)
- ebpf: Fix race between loading kubernetes services and conntrack cleanup. If conntrack cleanup ran before services were loaded, all service entries would look stale and get cleaned up. [calico 10721](https://github.com/projectcalico/calico/pull/10721) (@fasaxc)
- Fix benign "Not a valid CIDR." log when processing headless services in kube proxy. [calico 10698](https://github.com/projectcalico/calico/pull/10698) (@fasaxc)
- ebpf: fixes ICMP response source IP when nodes have multiple IPs assigned [calico 10660](https://github.com/projectcalico/calico/pull/10660) (@tomastigera)
- ebpf: Fix large policy programs in case jit_harden is set, e.g. like in Bottlerocket [calico 10602](https://github.com/projectcalico/calico/pull/10602) (@tomastigera)
- ebpf: Fixed mounting cgroupv2 for connect time load balancing. [calico 10503](https://github.com/projectcalico/calico/pull/10503) (@sridhartigera)
- ebpf: fix forwarding for asymetric routing https://github.com/projectcalico/calico/issues/10469 [calico 10511](https://github.com/projectcalico/calico/pull/10511) (@tomastigera)
- ebpf: handles fragmented IPv4 packets, some limitations apply [calico 10335](https://github.com/projectcalico/calico/pull/10335) (@tomastigera)
- ebpf: Fix configuring arp entries for bpf NAT devices for systemd >= 242 [calico 10216](https://github.com/projectcalico/calico/pull/10216) (@sridhartigera)
- ebpf: Fixed a bug where BPF programs were being re-attached to network interfaces unnecessarily, even when the host IP address had not changed. [calico 10161](https://github.com/projectcalico/calico/pull/10161) (@sridhartigera)
- ebpf: Fix dropping packets from workloads to host interfaces not managed by calico. [calico 10069](https://github.com/projectcalico/calico/pull/10069) (@sridhartigera)
- ebpf: fix cleanup of UDP service entries when a service gets (re)created [calico 10049](https://github.com/projectcalico/calico/pull/10049) (@tomastigera)
- Avoid loading wireguard kernel module when Wireguard is disabled. [calico 10821](https://github.com/projectcalico/calico/pull/10821) (@bartekzurawski)
- Added support for packet burst configuration to packet rate QoS controls. Fixed upper and lower boundaries of packet rate and number of connections QoS controls to be in-line with kernel limits. [calico 10489](https://github.com/projectcalico/calico/pull/10489) (@coutinhop)
- ebpf: Fixed attaching bpf programs by atomically replacing the old program rather than attaching new and detaching old. [calico 10445](https://github.com/projectcalico/calico/pull/10445) (@sridhartigera)
- ebpf: Fix forwarding of packets to kubevirt pods when in bridge mode. [calico 10308](https://github.com/projectcalico/calico/pull/10308) (@sridhartigera)

### 3.31.1

- ebpf: kube-proxy binds service health probes to node IPs instead of "any" [calico 11300](https://github.com/projectcalico/calico/pull/11300) (@tomastigera)
- fix (release-tool): include image tarballs in release archive file [calico 11295](https://github.com/projectcalico/calico/pull/11295) (@radTuti)
- Fix BGP advertisement of externalIP addresses on Services with type=ClusterIP. [calico 11234](https://github.com/projectcalico/calico/pull/11234) (@caseydavenport)
- Fix IPAM block leak of older blocks when deleting IP pools. [calico 11233](https://github.com/projectcalico/calico/pull/11233) (@caseydavenport)
- ebpf: start only a single kube-proxy health-server in dual stack mode [calico 11224](https://github.com/projectcalico/calico/pull/11224) (@tomastigera)
- Bugfix: reinstate support for VMs that are configured not to respond to ARP requests. [calico 11100](https://github.com/projectcalico/calico/pull/11100) (@nelljerram)

### 3.31.3

- Fix IPPool CIDR Validation Failing on Semantically-Identical IPv6 CIDRs. [calico 11438](https://github.com/projectcalico/calico/pull/11438) (@skoryk-oleksandr)
- Fix AllowSpoofedSourcePrefixes for dual stack clusters. [calico 11372](https://github.com/projectcalico/calico/pull/11372) (@lucastigera)
- Openstack: Stop compressing DWARF debugging information with dwz because Golang 1.25 has moved to the unsupported DWARF 5. [calico 11422](https://github.com/projectcalico/calico/pull/11422) (@nelljerram)
- Fixed bug where ingress and egress policy program indexes were confused, resulting in cleaning up the wrong policy program. [calico 11569](https://github.com/projectcalico/calico/pull/11569) (@fasaxc)
- Fixed map operations for older kernels. [calico 11497](https://github.com/projectcalico/calico/pull/11497) (@sridhartigera)
- Fixed loading connecttime load balancer program in 6.12 kernel. [calico 11407](https://github.com/projectcalico/calico/pull/11407) (@sridhartigera)

### 3.31.4

- Fix race in EndpointSlice logic for BGP service advertisement [calico 11786](https://github.com/projectcalico/calico/pull/11786) (@MichalFupso)
- Fix rendering of NatPortRange option when using nftables. [calico 11741](https://github.com/projectcalico/calico/pull/11741) (@nelljerram)
- Don't uninstall CNI and kube-proxy service when using non-Calico CNI on Windows with operator install. [calico 11722](https://github.com/projectcalico/calico/pull/11722) (@coutinhop)
- Fix that the CNI plugin installer generated a malformed URL for IPv4 addresses. This bug was exposed by a fix to the golang URL parser. [calico 11719](https://github.com/projectcalico/calico/pull/11719) (@fasaxc)
- Various fixes for 32bit architectures. [calico 11705](https://github.com/projectcalico/calico/pull/11705) (@juanluisvaladas)
- ebpf: fix - The eBPF dataplane regressed when switching to the flow based vxlan device and the VNI is always 0 regardless of the actual setting [calico 11695](https://github.com/projectcalico/calico/pull/11695) (@tomastigera)
- ebpf: fixed performance for UDP (QUIC/HTTP3) nodeports [calico 11659](https://github.com/projectcalico/calico/pull/11659) (@tomastigera)
- eBPF: fix that local workload with borrowed IPs lose connectivity [calico 11654](https://github.com/projectcalico/calico/pull/11654) (@fasaxc)
- ebpf: Do not adjust gso_size after nodeport tunnel vxlan decap. There is no guarantee that there would be enough data after removing tunnel headers. The packet is shrunk by 50 bytes while the gso_size would grow. Kernel would drop the packet if the original gso packet is too small. [calico 11613](https://github.com/projectcalico/calico/pull/11613) (@tomastigera)
- OpenStack bugfix: request etcd compaction periodically regardless of how long resync takes, or if periodic resync is disabled. [calico 11575](https://github.com/projectcalico/calico/pull/11575) (@nelljerram)
- bpf: Fix IP fragment reassembly between 8,000 and 16,000 bytes. Offsets were miscalculated due to incorrect order of operations. [calico 11562](https://github.com/projectcalico/calico/pull/11562) (@fasaxc)

### 3.31.5

- Fix memory leak in LoadBalancer controller where `deleteService` and `releaseAddressFromService` left stale entries in the `ipsByBlock` index, causing unbounded memory growth in kube-controllers in clusters with high LoadBalancer service churn. [calico 12369](https://github.com/projectcalico/calico/pull/12369) (@caseydavenport)
- ebpf: Fix conntrack counter accounting for NAT-outgoing flows where bytes_in and packets_in were always zero. [calico 12324](https://github.com/projectcalico/calico/pull/12324) (@lucastigera)
- ebpf: Fix that BPF programs could be incorrectly removed from workload interfaces on recent kernels due to change in kernel use of IFLA_LINK netlink message. [calico 12210](https://github.com/projectcalico/calico/pull/12210) (@tomastigera)
- Fix memory leak in routing table logic. The "interfaces to ARP" set was not properly cleaned out when an interface was removed, resulting in leaving old interface names in the set. [calico 12193](https://github.com/projectcalico/calico/pull/12193) (@fasaxc)
- Fix a goroutine leak in Felix's interface monitor that could occur on netlink reconnect. [calico 12193](https://github.com/projectcalico/calico/pull/12193) (@fasaxc)
- Fix goroutine leak after nflog reader restart. [calico 12193](https://github.com/projectcalico/calico/pull/12193) (@fasaxc)
- Fix BGP syncing on Windows [calico 12063](https://github.com/projectcalico/calico/pull/12063) (@rbrtbnfgl)
- Fix failure to enable ingress bandwidth QoS controls when a non-default qdisc previously existed on the workload interface (handle != 0). [calico 11972](https://github.com/projectcalico/calico/pull/11972) (@coutinhop)
- Fix CNI delete timeout to start after IPAM lock acquisition, preventing "context deadline exceeded" failures during high pod churn [calico 11942](https://github.com/projectcalico/calico/pull/11942) (@sridhartigera)
- Prevent nil pointer dereference in handleBlockUpdate in LoadBalancer controller [calico 11924](https://github.com/projectcalico/calico/pull/11924) (@MichalFupso)
- ebpf: corrected setting of bpf_skb_adjust_room flags for UDP [calico 11661](https://github.com/projectcalico/calico/pull/11661) (@tomastigera)

### 3.31.6

- calico/node now refreshes the CNI plugin's kubeconfig immediately when the pod's projected ServiceAccount token is rotated, closing a 6-12h window where an externally-invalidated token could cause CNI ADD to fail with "Unauthorized" until the calico-node pod was restarted. [calico 12941](https://github.com/projectcalico/calico/pull/12941) (@skoryk-oleksandr)
- Fix SNAT being skipped for traffic destined to LoadBalancer-only IPPools by excluding them from the all-ipam-pools ipset. [calico 12857](https://github.com/projectcalico/calico/pull/12857) (@defo89)
- Fix calico-kube-controllers IPAM GC controller getting stuck when cleaning up nodes during rapid scale-down. [calico 12746](https://github.com/projectcalico/calico/pull/12746) (@haojiwu)
- ebpf - Fix kube-proxy losing the NodePort externalTrafficPolicy=Local route-fixup trigger after a syncer swap, which could cause stale NAT entries on remote backends. [calico 12744](https://github.com/projectcalico/calico/pull/12744) (@tomastigera)
- Fixes nft binary segfaults in calico/node when newer nftables is in use elsewhere on the host. [calico 12714](https://github.com/projectcalico/calico/pull/12714) (@caseydavenport)
- ebpf - Fix transient NodePort connection failures when Felix restarts on a node receiving external NodePort traffic. [calico 12693](https://github.com/projectcalico/calico/pull/12693) (@tomastigera)
- Fixes a Felix panic that could occur when an IP set selector matched both a NetworkSet CIDR and workload IPs contained within it, with nftables as the active dataplane. [calico 12672](https://github.com/projectcalico/calico/pull/12672) (@caseydavenport)
- Typha now rejects oversized inbound client gob frames before reading them, preventing a potential denial-of-service caused by excessive memory allocation. [calico 12591](https://github.com/projectcalico/calico/pull/12591) (@Behnam-Shobiri)
- Fix LoadBalancer IPAM race on kube-controllers startup that could assign multiple addresses to a Service. [calico 12569](https://github.com/projectcalico/calico/pull/12569) (@MichalFupso)
- Fixed a Felix eBPF cleanup race condition that could cause a nil-pointer panic when an interface disappeared during TC qdisc cleanup. [calico 12481](https://github.com/projectcalico/calico/pull/12481) (@Behnam-Shobiri)
- Fix nftables segfault on systems with newer nft versions (Debian Trixie, Fedora 42+) by bumping knftables to v0.0.21. [calico 12470](https://github.com/projectcalico/calico/pull/12470) (@caseydavenport)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.31.6**, the newest release recorded here for this line.

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
