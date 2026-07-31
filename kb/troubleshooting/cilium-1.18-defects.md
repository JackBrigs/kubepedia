---
id: TROUBLE-CILIUM_1_18_DEFECTS
type: troubleshooting
title: "cilium 1.18: defects fixed in the 1.18 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.18.0 <1.19.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.18 known issues
  - cilium 1.18 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.18 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.18: defects fixed in the 1.18 line

## Summary

**165 defects** the project fixed across **12 releases** of the 1.18 line, from 1.18.1 to
1.18.12. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.18.1

- clustermesh: fix regression possibly causing cross-cluster connections disruption if the clustermesh-apiserver is restarted at the same time as Cilium agents. (Backport PR cilium/cilium#40979, Upstream PR cilium/cilium#40786, @giorio94)
- clustermesh: fix regression preventing global services with unnamed ports from including remote backends (Backport PR cilium/cilium#40865, Upstream PR cilium/cilium#40848, @giorio94)
- Fix bug where the presence of a label called "ingress" causes incorrect assignment of identities to workloads, affecting policy enforcement. (Backport PR cilium/cilium#40847, Upstream PR cilium/cilium#40791, @christarazi)
- Fix skipping of LoadBalancer services when IPMode is not set to VIP (KEP-1860) (Backport PR cilium/cilium#40979, Upstream PR cilium/cilium#40915, @joamaki)
- fix(GH-37724): Sync policies on startup (Backport PR cilium/cilium#40847, Upstream PR cilium/cilium#40357, @anubhabMajumdar)
- fix: create policy snapshot only for sdp (Backport PR cilium/cilium#40979, Upstream PR cilium/cilium#40785, @vipul-21)
- Fixes a bug where the Cilium agent may segfault when starting. (Backport PR cilium/cilium#40847, Upstream PR cilium/cilium#40824, @squeed)
- Fixes an error where the Ingress controller, when run in host network, created an invalid Service. (Backport PR cilium/cilium#41078, Upstream PR cilium/cilium#40232, @rtheobald)
- install/kubernetes: fix clustermesh-apiserver extraEnv (Backport PR cilium/cilium#41078, Upstream PR cilium/cilium#41021, @aanm)
- loadbalancer: Fix backend state in REST API (Backport PR cilium/cilium#40847, Upstream PR cilium/cilium#40780, @mhofstetter)
- Fix GKE cluster creation failures when branch names exceed 63-byte label limit by implementing automatic truncation with hash-based uniqueness preservation. (Backport PR cilium/cilium#40847, Upstream PR cilium/cilium#40725, @pillai-ashwin)
- ipsec: fix privileged tests (Backport PR cilium/cilium#41078, Upstream PR cilium/cilium#41006, @smagnani96)
- workflows/ipsec: Fix leak detection for IPv6-only in e2e downgrade (Backport PR cilium/cilium#40979, Upstream PR cilium/cilium#40881, @smagnani96)
- github: fix removal of all files in /mnt (Backport PR cilium/cilium#40847, Upstream PR cilium/cilium#40818, @aanm)
- Fix loadbalancer handling of backends with ClusterID set (Backport PR cilium/cilium#41078, Upstream PR cilium/cilium#40968, @giorio94)
- Fix race condition issues (Backport PR cilium/cilium#40979, Upstream PR cilium/cilium#40949, @aanm)

### 1.18.2

- Fix validation bug where namespaced CiliumNetworkPolicies with nodeSelector in specs array were silently accepted but ignored. Now properly rejected with validation error. (Backport PR cilium/cilium#41365, Upstream PR cilium/cilium#40702, @pillai-ashwin)
- Fix "Error while correcting L4 checksum" dropped packets for ICMP destination unreachable error packets. (Backport PR cilium/cilium#41591, Upstream PR cilium/cilium#40194, @br4243)
- Fix "No mapping for NAT masquerade" flakes in the CI, make NAT LRU fallbacks more robust. (Backport PR cilium/cilium#41365, Upstream PR cilium/cilium#40971, @gentoo-root)
- Fix --exclude-local-address with eBPF Host-Routing (Backport PR cilium/cilium#41365, Upstream PR cilium/cilium#41275, @antonipp)
- Fix a BGP bug where the routerID specified in a CiliumBGPNodeConfigOverride was not correctly updated in RouterIDIPPool mode. (Backport PR cilium/cilium#41267, Upstream PR cilium/cilium#40340, @liyihuang)
- Fix a bug that would cause NodePort requests to be sent to the wrong backends when using KPR and Clustermesh with two identical, non-global NodePort services on different clusters. (Backport PR cilium/cilium#41591, Upstream PR cilium/cilium#41337, @pchaigno)
- Fix a bug where cilium-agent would report "Link not found" for an endpoint deleted during state restore after cilium-agent restart. (Backport PR cilium/cilium#41267, Upstream PR cilium/cilium#40568, @fristonio)
- Fix a regression where enabling unknown Hubble metrics would crash the cilium agent (Backport PR cilium/cilium#41479, Upstream PR cilium/cilium#41368, @devodev)
- Fix agent config initContainer unable to hit apiservers in apiServerURLs by passing as container arg (Backport PR cilium/cilium#41267, Upstream PR cilium/cilium#41110, @JJGadgets)
- Fix bug that would cause error messages when disabling agent health checks (Backport PR cilium/cilium#41479, Upstream PR cilium/cilium#41297, @HadrienPatte)
- Fix issue in Local Redirect Policies where traffic was dropped when no local pods were available to be redirected to. In these scenarios the traffic should have been processed as if the Local Redirect Policy did not exist. (Backport PR cilium/cilium#41591, Upstream PR cilium/cilium#41463, @joamaki)
- Fix issue where Local Redirect Policy (LRP) services with a single named port did not create a local redirect service entry. (Backport PR cilium/cilium#41591, Upstream PR cilium/cilium#41534, @aditighag)
- Fix the bug local redirect policy not doing filter based destination port (Backport PR cilium/cilium#41479, Upstream PR cilium/cilium#41411, @liyihuang)
- Fixes a cosmetic bug where the cilium_bpf_map_ops_total error count was incorrectly being incremented for map cilium_lb_affinity_match. (Backport PR cilium/cilium#41479, Upstream PR cilium/cilium#41378, @squeed)
- Fixes an issue in NodeManager where restored cluster nodes can be pruned before the initial node listing completes. (Backport PR cilium/cilium#41267, Upstream PR cilium/cilium#41039, @0xch4z)
- iptables: Fix IPv6 SNAT for L7 proxy upstream traffic (Backport PR cilium/cilium#41249, Upstream PR cilium/cilium#41034, @gentoo-root)
- neighbor: Fix bug where neighbor discovery subsystem reports unhealthy when it is healthy (Backport PR cilium/cilium#41365, Upstream PR cilium/cilium#41186, @mhofstetter)
- pkg/ipam: fix nil dereference during pool shrink operation (Backport PR cilium/cilium#41365, Upstream PR cilium/cilium#41198, @alimehrabikoshki)
- policy: fix agent crash due to policy cache update-delete race (Backport PR cilium/cilium#41267, Upstream PR cilium/cilium#41079, @fristonio)
- github/actions: fix boolean condition check in post-logic action (Backport PR cilium/cilium#41479, Upstream PR cilium/cilium#41395, @aanm)
- github: fix upload artifacts for features.json (Backport PR cilium/cilium#41365, Upstream PR cilium/cilium#41119, @aanm)
- Fix multiple workflows with missing features and steps (Backport PR cilium/cilium#41479, Upstream PR cilium/cilium#41398, @aanm)
- ipsec: fix xfrm privileged tests (Backport PR cilium/cilium#41365, Upstream PR cilium/cilium#41279, @smagnani96)
- node:tests: fix privileged (cilium/cilium#41281, @smagnani96)
- testutils: differentiate {Test,Benchmark}Privileged and fix benchmarks (Backport PR cilium/cilium#41267, Upstream PR cilium/cilium#41007, @smagnani96)
- workflows/ipsec: yet another fix for downgrade (Backport PR cilium/cilium#41365, Upstream PR cilium/cilium#41260, @smagnani96)
- bpf: fix svc annotation handling (Backport PR cilium/cilium#41365, Upstream PR cilium/cilium#41310, @borkmann)
- Fix release script steps (Backport PR cilium/cilium#41177, Upstream PR cilium/cilium#41502, @aanm)
- kvstore: fix overly verbose debug log and error message (Backport PR cilium/cilium#41267, Upstream PR cilium/cilium#41148, @giorio94)
- loadbalancer: Fixes to test flakes (Backport PR cilium/cilium#41267, Upstream PR cilium/cilium#41085, @joamaki)
- metrics/features: Fix counter metrics to use Set() instead of Add() (Backport PR cilium/cilium#41479, Upstream PR cilium/cilium#41382, @aanm)
- Prevent `cilium-dbg` from panicing when `/sys` is not mounted (Backport PR cilium/cilium#41365, Upstream PR cilium/cilium#41287, @HadrienPatte)
- workflows/conformance-ginkgo: fix steps for stable branches (Backport PR cilium/cilium#41591, Upstream PR cilium/cilium#41599, @aanm)
- xds: fix NACK logging after slog migration (Backport PR cilium/cilium#41267, Upstream PR cilium/cilium#41171, @mhofstetter)

### 1.18.3

- Fix a complexity issue for the bpf_xdp program (Backport PR cilium/cilium#42198, Upstream PR cilium/cilium#42193, @aspsk)
- Avoid scenario where ENI device configuration can be skipped. (Backport PR cilium/cilium#41968, Upstream PR cilium/cilium#41760, @jasonaliyetti)
- Fix a bug that was preventing Cilium to delete stale pod CIDRs routes when changing routing mode to native (Backport PR cilium/cilium#41968, Upstream PR cilium/cilium#41819, @pippolo84)
- Fix a fatal error when accessing multicast map using cilium-dbg bpf multicast (Backport PR cilium/cilium#42151, Upstream PR cilium/cilium#42080, @tklauser)
- Fix BGP auto discovery not sending community info (Backport PR cilium/cilium#41968, Upstream PR cilium/cilium#41920, @jiashengz)
- Fix bug in ENI routing where Cilium would chose the wrong subnet for routing traffic on secondary interfaces (Backport PR cilium/cilium#41828, Upstream PR cilium/cilium#40860, @liyihuang)
- Fix bug that could cause ICMP error packets to have an incorrect inner IP checksum when KPR is enabled. (Backport PR cilium/cilium#41828, Upstream PR cilium/cilium#41551, @yushoyamaguchi)
- Fix bug with delegated IPAM where IPv6 traffic was routed via the wrong interface (Backport PR cilium/cilium#41968, Upstream PR cilium/cilium#41598, @NihaNallappagari)
- Fix failing node health check on dual stack cluster if NodeInternalIPs are not configured for both families. (Backport PR cilium/cilium#42055, Upstream PR cilium/cilium#41633, @Dennor)
- Fix increase in memory usage when service names are looked up at high rate during Hubble flow creation (Backport PR cilium/cilium#42151, Upstream PR cilium/cilium#41965, @joamaki)
- Fix panic at startup in IPsec subsystem with Multi-Pool IPAM mode (cilium/cilium#41725, @pippolo84)
- Fix race condition preventing the skiplbmap BPF map from sometimes being pruned after restart. (Backport PR cilium/cilium#41828, Upstream PR cilium/cilium#41529, @joamaki)
- Fixes a rare bug where endpoints may have incomplete policies in large clusters. (Backport PR cilium/cilium#42151, Upstream PR cilium/cilium#42049, @squeed)
- operator/pkg/lbipam: fix LoadBalancerIPPool conditions update logic (Backport PR cilium/cilium#41828, Upstream PR cilium/cilium#41322, @alimehrabikoshki)
- cli: Fix unreliable tests due to error emitted in Cilium logs "retrieving device lxc*: Link not found" (Backport PR cilium/cilium#42200, Upstream PR cilium/cilium#42146, @fristonio)
- workflows: fix GCP OIDC authentication's project ID (cilium/cilium#42173, @nbusseneau)
- gateway-api: Fix incorrect `Owns` call in refactor (Backport PR cilium/cilium#41968, Upstream PR cilium/cilium#41807, @youngnick)
- redirectpolicy: Fix comparison of BackendParams (Backport PR cilium/cilium#41848, Upstream PR cilium/cilium#41705, @joamaki)

### 1.18.4

- fix indentation for certgen resources in helm templates (Backport PR cilium/cilium#42450, Upstream PR cilium/cilium#42412, @sdickhoven)
- Fix BGP operator crash when bgp-secrets-namespace not set. (Backport PR cilium/cilium#42577, Upstream PR cilium/cilium#42425, @rastislavs)
- Fix cilium_operator_lbipam_conflicting_pools metric to report correct value. (Backport PR cilium/cilium#42289, Upstream PR cilium/cilium#41999, @hanapedia)
- Fix issue where fqdn GC starts too early that results in potentially missed ips in the IPCache (Backport PR cilium/cilium#42617, Upstream PR cilium/cilium#42502, @odinuge)
- Fix potential policy deadlock causing endpoint to use previous identity for policy calculation when endpoint changes identity (Backport PR cilium/cilium#42617, Upstream PR cilium/cilium#42420, @odinuge)
- Fix the output of cilium lrp list command to show LRP selected backends. (Backport PR cilium/cilium#42577, Upstream PR cilium/cilium#42110, @Bigdelle)
- Fix trace aggregation for IPv4 Host Firewall, reducing the amount of generated events. (Backport PR cilium/cilium#42617, Upstream PR cilium/cilium#42595, @smagnani96)
- fix: Panic during endpoint restore due to nil logger (Backport PR cilium/cilium#42450, Upstream PR cilium/cilium#42385, @pinaki-08)
- gh: ginkgo: fix focus for service hairpin test (Backport PR cilium/cilium#42641, Upstream PR cilium/cilium#42633, @julianwiedmann)
- fix: run post-release and publish-helm workflows on cilium org (Backport PR cilium/cilium#42450, Upstream PR cilium/cilium#42279, @sekhar-isovalent)
- loadbalancer: fix up code comment (Backport PR cilium/cilium#42450, Upstream PR cilium/cilium#42273, @julianwiedmann)
- [v1.18] ipam: fix TestNodeManagerAbortReleaseIPReassignment test (cilium/cilium#42636, @rastislavs)

### 1.18.5

- AWS EC2: Fix ENI attachment on multi-network card instances with high-performance networking (EFA) setups (Backport PR cilium/cilium#42745, Upstream PR cilium/cilium#42512, @41ks)
- ENI: Fix panic on nil subnet (Backport PR cilium/cilium#43117, Upstream PR cilium/cilium#43023, @HadrienPatte)
- Fix a bug that would cause Cilium to not report L4 checksum update errors when the length attribute is missing in ICMP Error messages with TCP inner packets. (Backport PR cilium/cilium#42828, Upstream PR cilium/cilium#42426, @yushoyamaguchi)
- Fix a bug that would cause IPsec logs to incorrectly report the XFRM rules being processed as "Ingress" rules. (Backport PR cilium/cilium#42828, Upstream PR cilium/cilium#42640, @sjohnsonpal)
- Fix agent local identity leak (Backport PR cilium/cilium#43117, Upstream PR cilium/cilium#42662, @odinuge)
- Fix bug that could cause the agent to fail to add XFRM states when IPsec is enabled, thus preventing a proper startup. (Backport PR cilium/cilium#42948, Upstream PR cilium/cilium#42666, @pchaigno)
- Fix GC of per-cluster ctmap entries (Backport PR cilium/cilium#43294, Upstream PR cilium/cilium#43160, @giorio94)
- Fix ipcache issues causing severe issues with the fqdn subsystem (Backport PR cilium/cilium#42864, Upstream PR cilium/cilium#42815, @odinuge)
- Fix issue where endpoints got stuck in "waiting-to-regenerate" (Backport PR cilium/cilium#42948, Upstream PR cilium/cilium#42856, @odinuge)
- Fix leak in the policy subsystem (Backport PR cilium/cilium#43117, Upstream PR cilium/cilium#42661, @odinuge)
- Fix rare kvstore issue where cilium continues to use an expired lease causing kvstore operations to fail consistently (Backport PR cilium/cilium#42745, Upstream PR cilium/cilium#42709, @odinuge)
- fqdn: Fix fqdn subsystem correctness issues causing packet drops and inconsistent ipcache (Backport PR cilium/cilium#43117, Upstream PR cilium/cilium#42500, @odinuge)
- policy: Fix rare Endpoint Selector Policy Deadlock causing policies to not be updated with new identities (Backport PR cilium/cilium#42864, Upstream PR cilium/cilium#42306, @odinuge)
- bpf: test: egressgw: fix up ENABLE_MASQUERADE (Backport PR cilium/cilium#42966, Upstream PR cilium/cilium#42912, @julianwiedmann)
- gh: conn-disrupt: fix XFRM error checks (Backport PR cilium/cilium#42764, Upstream PR cilium/cilium#42724, @julianwiedmann)
- gh: ipsec-e2e: fix flaky connection disruptivity test (Backport PR cilium/cilium#42823, Upstream PR cilium/cilium#42780, @julianwiedmann)
- [v1.18] ipcache: Fix leak in CIDR metadata consolidation logic (cilium/cilium#43354, @christarazi)

### 1.18.6

- Fix a bug with local redirect service entries being created when backend pods weren't ready. (Backport PR cilium/cilium#43425, Upstream PR cilium/cilium#43095, @aditighag)
- Fix an issue in proxy NOTRACK iptables rule for aws-cni chaining mode which causes proxy->upstream(outside cluster) traffic not being SNAT'd. (Backport PR cilium/cilium#43676, Upstream PR cilium/cilium#43566, @fristonio)
- Fix GC of possible duplicated identities in kvstore mode (Backport PR cilium/cilium#43425, Upstream PR cilium/cilium#43287, @giorio94)
- Fixes a deadlock that was causing endpoint to be stuck without progressing with any updates. (Backport PR cilium/cilium#43290, Upstream PR cilium/cilium#43242, @marseel)
- xds: fix nil-pointer in `processRequestStream` (Backport PR cilium/cilium#43612, Upstream PR cilium/cilium#43609, @mhofstetter)
- cmapisrv/test: miscellaneous fixes to the ciliumidentities script test (Backport PR cilium/cilium#43425, Upstream PR cilium/cilium#43372, @giorio94)
- Fix a regression in the new services control plane where loadBalancerSourceRanges was applied by default to all service types. (Backport PR cilium/cilium#43575, Upstream PR cilium/cilium#42351, @borkmann)

### 1.18.7

- bpf: Fix marker to skip nodeport when punting to proxy (Backport PR cilium/cilium#43886, Upstream PR cilium/cilium#43069, @borkmann)
- Fix a bug with local redirect service entries being created when backend pods weren't ready. (Backport PR cilium/cilium#43756, Upstream PR cilium/cilium#43095, @aditighag)
- Fix ICMP error packet handling by adding the missing checksum recalculation performed during RevNAT for SNATed load-balanced traffic. (Backport PR cilium/cilium#43861, Upstream PR cilium/cilium#43196, @yushoyamaguchi)
- helm: Fixed RBAC errors with `operator.enabled=false` by aligning cilium-tlsinterception-secrets Role/RoleBinding conditionals (Backport PR cilium/cilium#44281, Upstream PR cilium/cilium#44159, @puwun)
- loadbalancer: Fix GetInstancesOfService to avoid removing an endpoint from Service A causes all requests to Service B to fail if the name of Service A is the prefix of Service B (Backport PR cilium/cilium#43777, Upstream PR cilium/cilium#43620, @imroc)
- fix(ctmap/gc): fix race conditions and flakiness in TestGCEnableRatchet (Backport PR cilium/cilium#44056, Upstream PR cilium/cilium#42009, @AritraDey-Dev)
- multicast: fix nil assignment to node configuration cell.Out map (Backport PR cilium/cilium#43865, Upstream PR cilium/cilium#40859, @ldelossa)

### 1.18.8

- cilium-dbg: fix seg-fault `ip get -l reserved:host` (Backport PR cilium/cilium#44519, Upstream PR cilium/cilium#44443, @aanm)
- Fix a bug where node IPv6 updates and deletes were not correctly propagated to the Linux kernel neighbor subsystem. (Backport PR cilium/cilium#44592, Upstream PR cilium/cilium#44540, @tklauser)
- Fix a bug where removed addresses from EndpointSlices might be missed if multiple EndpointSlices share the same name (Backport PR cilium/cilium#44021, Upstream PR cilium/cilium#43999, @EmilyShepherd)
- Fix envoy admin socket being created as world-accessible (Backport PR cilium/cilium#44592, Upstream PR cilium/cilium#44512, @0xch4z)
- Fixed an issue where wildcard FQDN network policy identities were not correctly pushed to Envoy when using SNI-based policies. (Backport PR cilium/cilium#44519, Upstream PR cilium/cilium#44462, @liyihuang)
- Fixed VTEP ARP responses returning 00:00:00:00:00:00 MAC due to interface MAC missing from eBPF Overlay configuration. (Backport PR cilium/cilium#44700, Upstream PR cilium/cilium#44513, @akos011221)
- gateway-api: Fix hostname intersection bug that was preventing cert-manager challenges from working correctly. (Backport PR cilium/cilium#44519, Upstream PR cilium/cilium#44492, @youngnick)
- l7lb: fix bypassing ingress policies for local backends (Backport PR cilium/cilium#44804, Upstream PR cilium/cilium#44693, @smagnani96)
- fix(deps): update k8s.io patch updates stable (v1.18) (cilium/cilium#44477, @cilium-renovate[bot])
- fix(deps): update k8s.io patch updates stable to v0.33.9 (v1.18) (patch) (cilium/cilium#44578, @cilium-renovate[bot])
- fix(deps): update sigs.k8s.io/mcs-api/controllers digest to 0f775a3 (v1.18) (cilium/cilium#44576, @cilium-renovate[bot])
- fix(deps): update sigs.k8s.io/mcs-api/controllers digest to 15301c2 (v1.18) (cilium/cilium#44675, @cilium-renovate[bot])
- [v1.18] loadbalancer: Fix flake in hybrid-dsr.txtar (cilium/cilium#44756, @julianwiedmann)

### 1.18.9

- Fix performance bug in L7 policy proxy redirect handling (Backport PR cilium/cilium#44827, Upstream PR cilium/cilium#44613, @fristonio)
- [v1.18] Fix incorrect policy service selector handling (cilium/cilium#44949, @fristonio)
- envoy: Fix xds server npds listeners accounting (Backport PR cilium/cilium#45218, Upstream PR cilium/cilium#44830, @fristonio)
- Fix a slow memory leak triggered by incremental policy updates (Backport PR cilium/cilium#45053, Upstream PR cilium/cilium#44328, @odinuge)
- Fix endpoints for static pods stuck in init identity (Backport PR cilium/cilium#45213, Upstream PR cilium/cilium#45016, @aaroniscode)
- Fix memory leak triggered by policies being created and deleted (Backport PR cilium/cilium#44827, Upstream PR cilium/cilium#44724, @odinuge)
- Fix panic in Hubble Relay when new peer address is unresolvable (Backport PR cilium/cilium#45213, Upstream PR cilium/cilium#45021, @pesarkhobeee)
- Fixed a bug in dual-stack cluster-pool IPAM where an operator restart with a pre-existing duplicate IPv6 PodCIDR could cause the affected node's IPv4 PodCIDR to be incorrectly freed and reassigned to another node. (Backport PR cilium/cilium#44867, Upstream PR cilium/cilium#44832, @christarazi)
- Fixed a bug in service load balancing where backend slot assignments could have gaps when maintenance backends exist, potentially causing traffic misrouting. (Backport PR cilium/cilium#44972, Upstream PR cilium/cilium#43902, @Aman-Cool)
- Fixed an issue where policy update ack is never completed after endpoint deletion. (Backport PR cilium/cilium#44819, Upstream PR cilium/cilium#44754, @jrajahalme)
- Fixed ipcache identity update hang when last proxy listener is removed. (Backport PR cilium/cilium#45218, Upstream PR cilium/cilium#44597, @jrajahalme)
- Fixes increased CPU usage in `hubble observe` caused by log coloring feature, even when coloring was disabled (Backport PR cilium/cilium#44827, Upstream PR cilium/cilium#44119, @tporeba)
- lb: fix panic in orphan backend cleanup when addr is zero-value (Backport PR cilium/cilium#45053, Upstream PR cilium/cilium#44853, @vipul-21)
- operator/identitygc: fix nil pointer dereference on shutdown (Backport PR cilium/cilium#45213, Upstream PR cilium/cilium#45091, @tsotne95)
- fix: escape $ character in regex to prevent injection (Backport PR cilium/cilium#44827, Upstream PR cilium/cilium#44638, @peoyekunle)
- fix(deps): update k8s.io patch updates stable to v0.33.10 (v1.18) (patch) (cilium/cilium#44939, @cilium-renovate[bot])
- fix(deps): update k8s.io/utils digest to 28399d8 (v1.18) (cilium/cilium#44936, @cilium-renovate[bot])
- fix(deps): update sigs.k8s.io/mcs-api/controllers digest to 4b9911b (v1.18) (cilium/cilium#45170, @cilium-renovate[bot])

### 1.18.10

- Fix cilium-agent crash when a transient network error occurs during CiliumNode update. The agent now retries instead of calling Fatal. (Backport PR cilium/cilium#45753, Upstream PR cilium/cilium#44526, @nebojsaj1726)
- Fix CiliumLocalRedirectPolicy addressMatcher overriding an existing Service's frontend when its backend pods are not yet Ready. (Backport PR cilium/cilium#45585, Upstream PR cilium/cilium#45522, @ysksuzuki)
- Fix missing global service backends in Cluster Mesh when multiple service ports point to the same target port. (Backport PR cilium/cilium#45354, Upstream PR cilium/cilium#45179, @RiccardoAtzori91)
- fix(egressGateway): skip unmatched gateways when using multiple gateway (Backport PR cilium/cilium#45631, Upstream PR cilium/cilium#44705, @ieth0)
- fix(ipsec): panic in parseSPI on malformed input (Backport PR cilium/cilium#45498, Upstream PR cilium/cilium#44815, @isoyuki)
- fix(deps): update k8s.io patch updates stable to v0.33.11 (v1.18) (patch) (cilium/cilium#45472, @cilium-renovate[bot])
- test/operator: fix TestUpdateUsedCIDIsReverted flakiness (Backport PR cilium/cilium#45631, Upstream PR cilium/cilium#41739, @giorio94)
- [v1.18] ipam: fix data race in MultiPoolManager node update (cilium/cilium#45520, @Kunalbehbud)

### 1.18.11

- bug: fixed weighted backend traffic splitting for TLSRoute passthrough listeners in Gateway API (Backport PR cilium/cilium#46249, Upstream PR cilium/cilium#45937, @nickolaev)
- Fix memory leak issue with reusing a watch channel hash map from very large StateDB transactions (cilium/cilium#46498, @joamaki)
- Fix TLS passthrough routes failing silently when a gateway has mixed HTTP, HTTPS, and TLS listeners and a TLSRoute with no sectionName. (Backport PR cilium/cilium#46234, Upstream PR cilium/cilium#45371, @syedazeez337)
- multipool: Fix retries for CiliumNode Get errors (Backport PR cilium/cilium#46410, Upstream PR cilium/cilium#46124, @pippolo84)
- sockets: fix nil pointer dereference in filterAndDestroySockets (Backport PR cilium/cilium#46029, Upstream PR cilium/cilium#44843, @umut-polat)
- Fixed an issue where privileged tests failed locally (Backport PR cilium/cilium#46029, Upstream PR cilium/cilium#40150, @AritraDey-Dev)
- fix(deps): update k8s.io patch updates stable to v0.33.12 (v1.18) (cilium/cilium#46145, @cilium-renovate[bot])
- fix(deps): update k8s.io patch updates stable to v0.33.12 (v1.18) (patch) (cilium/cilium#46017, @cilium-renovate[bot])
- fix(deps): update k8s.io patch updates stable to v0.33.13 (v1.18) (cilium/cilium#46565, @cilium-renovate[bot])
- fix(deps): update k8s.io/utils digest to ff6756f (v1.18) (cilium/cilium#46000, @cilium-renovate[bot])

### 1.18.12

- Fix incorrect policy denials for traffic to L7 load balanced services when remote identity changes (Backport PR cilium/cilium#47003, Upstream PR cilium/cilium#46821, @fristonio)
- Fix regression preventing Cilium from starting when configured in kvstore mode with KPR enabled, if etcd is behind a Kubernetes service (Backport PR cilium/cilium#47196, Upstream PR cilium/cilium#46444, @giorio94)
- Fix instance of cilium having incorrect specified policy_change_total failure label "failure" value which caused unnecessary warnings. (Backport PR cilium/cilium#46794, Upstream PR cilium/cilium#46388, @tommyp1ckles)
- fix(deps): update k8s.io/utils digest to be93311 (v1.18) (cilium/cilium#46911, @cilium-renovate[bot])
- fix(deps): update k8s.io/utils digest to cf1189d (v1.18) (cilium/cilium#47116, @cilium-renovate[bot])


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.18.12**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `cilium/cilium`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cilium.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
