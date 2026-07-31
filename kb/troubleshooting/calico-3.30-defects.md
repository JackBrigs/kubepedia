---
id: TROUBLE-CALICO_3_30_DEFECTS
type: troubleshooting
title: "calico 3.30: defects fixed in the 3.30 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.30.0 <3.31.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - calico 3.30 known issues
  - calico 3.30 fixed in
  - is this calico bug already fixed
tags:
  - troubleshooting
  - upgrade
  - calico
sources:
  - type: docs
    path: projectcalico/calico release notes for the 3.30 line — bug-fix entries
    url: https://github.com/projectcalico/calico/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# calico 3.30: defects fixed in the 3.30 line

## Summary

**80 defects** the project fixed across **8 releases** of the 3.30 line, from 3.30.0 to
3.30.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.30.0

- Fix spammy logs when handling endpoint status creation events. [calico 10327](https://github.com/projectcalico/calico/pull/10327) (@song-jiang)
- Change OpenShift manifests order to fix an error when creating HCP clusters. [calico 10254](https://github.com/projectcalico/calico/pull/10254) (@coutinhop)
- Fix potential nil pointer access in confd [calico 10177](https://github.com/projectcalico/calico/pull/10177) (@fasaxc)
- Fix up various spammy warning logs. [calico 10176](https://github.com/projectcalico/calico/pull/10176) (@fasaxc)
- Fix that BPF-based conntrack cleaner would expire DSR entries too soon due to missing type check. [calico 9957](https://github.com/projectcalico/calico/pull/9957) (@fasaxc)
- Fix missing RBAC permissions for kube-controller-manager to access tiers in manifest installs, which was preventing proper resource garbage collection. [calico 9879](https://github.com/projectcalico/calico/pull/9879) (@caseydavenport)
- Fixed tiers RBAC for calicoctl when it runs as a k8s pod. [calico 9822](https://github.com/projectcalico/calico/pull/9822) (@lucastigera)
- Rev bpftool to v7.5.0. Should fix issues with listing programs when there are non-Calico programs present that bpftool doesn't understand. [calico 9806](https://github.com/projectcalico/calico/pull/9806) (@fasaxc)
- Fix: Map OpenStack-derived policy to the "default" tier, not "ossg". [calico 9777](https://github.com/projectcalico/calico/pull/9777) (@nelljerram)
- Fix that netlink list operations could fail with "device or resource busy" errors when under load resulting in Felix restarting. [calico 9769](https://github.com/projectcalico/calico/pull/9769) (@fasaxc)
- Fix incorrect comment for TCPResetSeen. [calico 9759](https://github.com/projectcalico/calico/pull/9759) (@ioworker0)
- The default value of endpointStatusPathPrefix in FelixConfiguration is /var/run/calico. Felix writes endpoint status files by default unless explicitly disabled by setting endpointStatusPathPrefix to an empty value. [calico 9721](https://github.com/projectcalico/calico/pull/9721) (@song-jiang)
- Fix route programming for VXLAN tunnel IPs assigned from a /32 or /128 IPAM block. [calico 9698](https://github.com/projectcalico/calico/pull/9698) (@caseydavenport)
- Fix spammy Tier already exists message from kube-controllers. [calico 9670](https://github.com/projectcalico/calico/pull/9670) (@fasaxc)
- Fix that nodes with borrowed VXLAN tunnel addresses were not reachable by pods. [calico 9662](https://github.com/projectcalico/calico/pull/9662) (@caseydavenport)
- Fix nftables mode for arm64 including wrong libnftnl version [calico 9657](https://github.com/projectcalico/calico/pull/9657) (@caseydavenport)
- Policies part of the default tier can be managed only with the original name they were created with. Policies are no longer able to be managed interchangeably with or without the default. tier prefix [calico 9615](https://github.com/projectcalico/calico/pull/9615) (@MichalFupso)
- Fixed file handle leak in felix, caused by failing to close netlink handles. [calico 9609](https://github.com/projectcalico/calico/pull/9609) (@sridhartigera)
- Fix that libcalico-go would not always fill in the revision when listing certain resources (or single instances of certain resources). This could result in missed watch events in components such as Typha. [calico 9599](https://github.com/projectcalico/calico/pull/9599) (@fasaxc)
- Fix that non-amd64 builds of node-driver-registrar contained x86 binaries. [calico 9594](https://github.com/projectcalico/calico/pull/9594) (@caseydavenport)
- Fix that in-use VXLAN ARP entries could be repeatedly cleaned up and then re-added if they shared a MAC address with an stale entry that was supposed to be cleaned up. [calico 9576](https://github.com/projectcalico/calico/pull/9576) (@fasaxc)
- Felix: fix that a map used to cache loaded datastore keys would always use RAM proportional to the total number of keys rather than shrinking when no longer needed. [calico 9526](https://github.com/projectcalico/calico/pull/9526) (@fasaxc)
- Fix that the new tiers resource was omitted from etcd->Kubernetes migration. [calico 9493](https://github.com/projectcalico/calico/pull/9493) (@fasaxc)
- Fix a panic in Felix when accessing a nil address in flushing host addresses, i.e. flushHostIPUpdates function. [calico 9466](https://github.com/projectcalico/calico/pull/9466) (@cyclinder)
- Helm: Fix that uninstall Job had duplicate k8s-app labels [calico 9438](https://github.com/projectcalico/calico/pull/9438) (@caseydavenport)
- Fix that single-IP entries on BGPConfiguration serviceExternalIPs were not advertised according to external traffic policy. [calico 9422](https://github.com/projectcalico/calico/pull/9422) (@tanujd11)
- Fix missing routes when vxlan mode is cross-subnet and the environment is purely V6 (no V4 host addresses) [calico 9416](https://github.com/projectcalico/calico/pull/9416) (@tomastigera)
- Fix spurious warning about unexpected inserted rules. [calico 9393](https://github.com/projectcalico/calico/pull/9393) (@fasaxc)
- Fixed memory leak in BPF endpoint manager. [calico 9307](https://github.com/projectcalico/calico/pull/9307) (@sridhartigera)
- Helm: Fix OpenShift provider case sensitivity [calico 9305](https://github.com/projectcalico/calico/pull/9305) (@unai-ttxu)
- Fix a bug where pods with flexvol/nodeagent volumes would get stuck in the Terminating phase, if, during termination, their node rebooted. [calico 9279](https://github.com/projectcalico/calico/pull/9279) (@aaaaaaaalex)
- fix image in flannel migration manifest [calico 9263](https://github.com/projectcalico/calico/pull/9263) (@radTuti)
- ebpf: Fix configuring arp entries for bpf NAT devices for systemd >= 242 [calico 10209](https://github.com/projectcalico/calico/pull/10209) (@sridhartigera)
- ebpf: Fixed a bug where BPF programs were being re-attached to network interfaces unnecessarily, even when the host IP address had not changed. [calico 10163](https://github.com/projectcalico/calico/pull/10163) (@sridhartigera)
- ebpf: fix cleanup of UDP service entries when a service gets (re)created [calico 10098](https://github.com/projectcalico/calico/pull/10098) (@tomastigera)
- ebpf: Fix dropping packets from workloads to host interfaces not managed by calico. [calico 10085](https://github.com/projectcalico/calico/pull/10085) (@sridhartigera)
- ebpf: fix icmp error delivery to host networked pods [calico 9747](https://github.com/projectcalico/calico/pull/9747) (@tomastigera)
- ebpf: fixed routing from outside the cluster in EKS with aws-cni [calico 9569](https://github.com/projectcalico/calico/pull/9569) (@tomastigera)
- ebpf: Fix that we'd fail to clear mark bits after applying do-not-track policy. Use dedicated mark for XDP bypass traffic. [calico 9392](https://github.com/projectcalico/calico/pull/9392) (@fasaxc)
- Resolved an issue preventing the program from launching on the s390x architecture. [calico 10206](https://github.com/projectcalico/calico/pull/10206) (@hjiawei)

### 3.30.1

- ebpf: Fixed attaching bpf programs by atomically replacing the old program rather than attaching new and detaching old. [calico 10454](https://github.com/projectcalico/calico/pull/10454) (@sridhartigera)
- Disable WatchList in Calico API server, fixing issue with stuck Namespace termination. [calico 10440](https://github.com/projectcalico/calico/pull/10440) (@tmjd)
- Policies created prior to v3.28.0 have their name retained across upgrade. Policies created in the default tier with version v3.29.[0-3] will have their names changed from `default.name` to `name`. [calico 10418](https://github.com/projectcalico/calico/pull/10418) (@MichalFupso)
- eBPF - Fix forwarding of packets to kubevirt pods when in bridge mode. [calico 10415](https://github.com/projectcalico/calico/pull/10415) (@sridhartigera)
- Add missing tiers permissions for flannel migration controller [calico 10385](https://github.com/projectcalico/calico/pull/10385) (@caseydavenport)
- Fix flannel migration use of deprecated flag "delete-local-data" [calico 10379](https://github.com/projectcalico/calico/pull/10379) (@caseydavenport)

### 3.30.2

- Fixed upper and lower boundaries of packet rate and number of connections QoS controls to be in-line with kernel limits
- ebpf: fix forwarding for asymetric routing https://github.com/projectcalico/calico/issues/10469 [calico 10535](https://github.com/projectcalico/calico/pull/10535) (@tomastigera)
- Fix race condition in Goldmane startup [calico 10514](https://github.com/projectcalico/calico/pull/10514) (@caseydavenport)
- Fix Goldmane race condition when terminating streams [calico 10513](https://github.com/projectcalico/calico/pull/10513) (@caseydavenport)

### 3.30.3

- Fix that whisker wouldn't bind to IPv6 addresses. [calico 10840](https://github.com/projectcalico/calico/pull/10840) (@caseydavenport)
- ebpf: Fix race between loading kubernetes services and conntrack cleanup. If conntrack cleanup ran before services were loaded, all service entries would look stale and get cleaned up. [calico 10724](https://github.com/projectcalico/calico/pull/10724) (@fasaxc)
- Fix confd on Windows by skipping watching endpoint status files. [calico 10703](https://github.com/projectcalico/calico/pull/10703) (@song-jiang)
- ebpf: fixes ICMP response source IP when nodes have multiple IPs assigned [calico 10661](https://github.com/projectcalico/calico/pull/10661) (@tomastigera)
- Fix that CalicoNodeStatus updates could get blocked by datastore errors [calico 10595](https://github.com/projectcalico/calico/pull/10595) (@theboringstuff)

### 3.30.4

- ebpf: do not blindly redirect back to the same host iface - fixed regression from 3.29 to 3.30 [calico 11155](https://github.com/projectcalico/calico/pull/11155) (@tomastigera)
- Reinstate support for VMs that are configured not to respond to ARP requests. [calico 11099](https://github.com/projectcalico/calico/pull/11099) (@nelljerram)
- Fix that IPAM allocation could leak handles when many workloads are scheduled to the same node at the same time, causing timeouts by "thundering herd". [calico 11096](https://github.com/projectcalico/calico/pull/11096) (@fasaxc)
- Fix slow IPAM release performance when releasing IPs from disabled or deleted pools (especially for bulk deletions like those done by IPAM GC). Consider disabled pools as potential IP owners and cache any loaded blocks for fast access. [calico 11095](https://github.com/projectcalico/calico/pull/11095) (@fasaxc)
- nftables: fix reprogramming of base chain rules after out-of-band flush. [calico 10939](https://github.com/projectcalico/calico/pull/10939) (@caseydavenport)
- Helm: fix role binding to use correct serviceaccount name when deployed in an alternative namespace. [calico 10908](https://github.com/projectcalico/calico/pull/10908) (@caseydavenport)

### 3.30.5

- ebpf: Fixed loading connecttime load balancer program in 6.12 kernel [calico 11406](https://github.com/projectcalico/calico/pull/11406) (@sridhartigera)
- Felix now explicitly sets priority 1024 for IPv6 routes instead of relying on kernel default, ensuring routes round-trip correctly when read from the kernel. [calico 11395](https://github.com/projectcalico/calico/pull/11395) (@fasaxc)
- Fix AllowSpoofedSourcePrefixes for dual stack clusters. [calico 11373](https://github.com/projectcalico/calico/pull/11373) (@lucastigera)
- fix (release-tool): include image tarballs in release archive file [calico 11296](https://github.com/projectcalico/calico/pull/11296) (@radTuti)
- Default KubeControllersConfiguration.LoadBalancer when not set to AllServices [calico 11267](https://github.com/projectcalico/calico/pull/11267) (@MichalFupso)
- ebpf: Do not adjust gso_size after nodeport tunnel vxlan decap. There is no guarantee that there would be enough data after removing tunnel headers. The packet is shrunk by 50 bytes while the gso_size would grow. Kernel would drop the packet if the original gso packet is too small. [calico 11259](https://github.com/projectcalico/calico/pull/11259) (@tomastigera)
- Fix BGP advertisement of externalIP addresses on Services with type=ClusterIP. [calico 11235](https://github.com/projectcalico/calico/pull/11235) (@caseydavenport)
- ebpf: start only a single kube-proxy health-server in dual stack mode [calico 11222](https://github.com/projectcalico/calico/pull/11222) (@tomastigera)
- Fix typo in FelixConfiguration BPFKubeProxyHealthzPort field. [calico 11209](https://github.com/projectcalico/calico/pull/11209) (@tomastigera)
- Fix IPAM block leak of older blocks when deleting IP pools. [calico 11196](https://github.com/projectcalico/calico/pull/11196) (@gojoy)

### 3.30.6

- OpenStack: make periodic compaction loop independent of resync [calico 11574](https://github.com/projectcalico/calico/pull/11574) (@nelljerram)

### 3.30.7

- ebpf: Fixed issue where VXLAN traffic was dropped on nodes still running Calico 3.30 during a rolling upgrade to 3.31. This caused connectivity failures for host-networked pods communicating via Kubernetes services across nodes at different versions. Upgrading to this 3.30 patch release before upgrading to 3.31 resolves the issue. [calico 12054](https://github.com/projectcalico/calico/pull/12054) (@tomastigera)
- Fix failure to enable ingress bandwidth QoS controls when a non-default qdisc previously existed on the workload interface (handle != 0). [calico 11984](https://github.com/projectcalico/calico/pull/11984) (@coutinhop)
- Fix CNI delete timeout to start after IPAM lock acquisition, preventing "context deadline exceeded" failures during high pod churn. [calico 11943](https://github.com/projectcalico/calico/pull/11943) (@sridhartigera)
- Fix advertisement of /32 LB IP addresses when not present in the Service Spec [calico 11928](https://github.com/projectcalico/calico/pull/11928) (@caseydavenport)
- Prevent nil pointer dereference in LoadBalancer controller `handleBlockUpdate` [calico 11923](https://github.com/projectcalico/calico/pull/11923) (@MichalFupso)
- Bugfix: fix rendering of NatPortRange option when using nftables. [calico 11740](https://github.com/projectcalico/calico/pull/11740) (@nelljerram)
- Don't uninstall CNI and kube-proxy service when using non-Calico CNI on Windows with operator install. [calico 11723](https://github.com/projectcalico/calico/pull/11723) (@coutinhop)
- Fix that the CNI plugin installer generated a malformed URL for IPv4 addresses. This bug was exposed by a fix to the golang URL parser. [calico 11720](https://github.com/projectcalico/calico/pull/11720) (@fasaxc)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.30.7**, the newest release recorded here for this line.

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
