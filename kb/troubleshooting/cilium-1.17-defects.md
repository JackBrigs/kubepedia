---
id: TROUBLE-CILIUM_1_17_DEFECTS
type: troubleshooting
title: "cilium 1.17: defects fixed in the 1.17 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.17.0 <1.18.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.17 known issues
  - cilium 1.17 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.17 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.17: defects fixed in the 1.17 line

## Summary

**166 defects** the project fixed across **17 releases** of the 1.17 line, from 1.17.1 to
1.17.18. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.17.1

- ces: Fix bug where stale endpoint information was injected into IPCache (Backport PR cilium/cilium#37416, Upstream PR cilium/cilium#37347, @gandro)
- socket-lb: Fix null pointer dereference in socketlb/cgroup.go (Backport PR cilium/cilium#37440, Upstream PR cilium/cilium#37426, @alvaroaleman)

### 1.17.2

- Fix a regression that made it impossible to disable Hubble via Helm charts (Backport PR cilium/cilium#37648, Upstream PR cilium/cilium#37587, @devodev)
- Fix bug causing `cilium-dbg bpf` commands to fail with a map not found error in IPv6-only clusters. (Backport PR cilium/cilium#37904, Upstream PR cilium/cilium#37787, @pchaigno)
- Fix creating ServiceMonitor for Hubble when dynamic metrics are enabled in the Helm chart (Backport PR cilium/cilium#37648, Upstream PR cilium/cilium#37474, @dustinspecker)
- Fix creation and deletion of host port maps that would occasionally leave pods without them (Backport PR cilium/cilium#37904, Upstream PR cilium/cilium#37419, @javanthropus)
- Fix dropped NodePort traffic to hostNetwork backends with Geneve+DSR (Backport PR cilium/cilium#37648, Upstream PR cilium/cilium#36978, @tommasopozzetti)
- Fix envoy metrics could not be obtained on IPv6-only clusters (Backport PR cilium/cilium#37904, Upstream PR cilium/cilium#37818, @haozhangami)
- Fix helm charts to properly configure tls and peer service for dynamic Hubble metrics. (Backport PR cilium/cilium#37904, Upstream PR cilium/cilium#37543, @rectified95)
- Fix service id exceeds max limit (Backport PR cilium/cilium#37648, Upstream PR cilium/cilium#37191, @haozhangami)
- Fix the `--dns-policy-unload-on-shutdown` feature for restored endpoints (Backport PR cilium/cilium#37648, Upstream PR cilium/cilium#37532, @antonipp)
- Fix the possible race condition caused by async update from aws to instance map in issue #36428 (Backport PR cilium/cilium#38104, Upstream PR cilium/cilium#37650, @liyihuang)
- Fix traffic not getting masqueraded with wildcard devices or egress-masquerade-interfaces when enable-masquerade-to-route-source flag is set. (Backport PR cilium/cilium#37648, Upstream PR cilium/cilium#37450, @liyihuang)
- fix(helm): multiPoolPreAllocation fix conditional avoid null (Backport PR cilium/cilium#37742, Upstream PR cilium/cilium#37585, @acelinkio)
- fix: cilium-config configmap was incorrectly resulting in values like `2.09715…2e+06` instead of `2097152` (Backport PR cilium/cilium#37648, Upstream PR cilium/cilium#37236, @dee-kryvenko)
- fix: duplicate label maps in helm chart templates and add missing commonlabels (Backport PR cilium/cilium#37742, Upstream PR cilium/cilium#37693, @cmergenthaler)
- Fix: Resolved an issue causing ArgoCD to report constant out-of-sync status due to the hasKey check in Helm. The condition has been simplified to ensure proper synchronization. No functional changes to deployments. (Backport PR cilium/cilium#37648, Upstream PR cilium/cilium#37536, @nicl-dev)
- Fixed Envoy JSON log format conversion in Helm, preventing crashes. (Backport PR cilium/cilium#37742, Upstream PR cilium/cilium#37656, @kahirokunn)
- helm: fix large number handling (Backport PR cilium/cilium#37742, Upstream PR cilium/cilium#37670, @justin0u0)
- hubble: fix locking of hubble metrics registry for dynamically configured metrics (Backport PR cilium/cilium#38104, Upstream PR cilium/cilium#37923, @marseel)
- identity: fix bug where fromNodes/toNodes could be used to allow custom endpoint (Backport PR cilium/cilium#38104, Upstream PR cilium/cilium#36657, @oblazek)
- operator: Fix duplicate configurations (Backport PR cilium/cilium#37648, Upstream PR cilium/cilium#37293, @joestringer)
- cilium: Pull in vxlan netlink Go fix and uncomment assertion in test (Backport PR cilium/cilium#37904, Upstream PR cilium/cilium#37808, @borkmann)
- Fix API generation and add trusted dependencies to renovate config (Backport PR cilium/cilium#37648, Upstream PR cilium/cilium#36957, @aanm)
- Fix helm value for IPAM Multi-Pool (Backport PR cilium/cilium#38104, Upstream PR cilium/cilium#37963, @saintdle)
- labels: fix TestNewFrom test (Backport PR cilium/cilium#37904, Upstream PR cilium/cilium#37846, @giorio94)
- Update Hubble UI to v0.13.2 which contains security fixes, add the missing traffic direction in the flow table, and enhance the home namespace list. See [v0.13.2](https://github.com/cilium/hubble-ui/releases/tag/v0.13.2) for more details (Backport PR cilium/cilium#37742, Upstream PR cilium/cilium#37631, @yannikmesserli)
- [v1.17] Revert "Fix dropped NodePort traffic to hostNetwork backends with Geneve+DSR" (cilium/cilium#38101, @julianwiedmann)

### 1.17.3

- Avoid installing no-track rules when IP family is disabled (Backport PR cilium/cilium#38526, Upstream PR cilium/cilium#38438, @ysksuzuki)
- bgpv2: Fix service reconciliation by BGP peer IP change (Backport PR cilium/cilium#38700, Upstream PR cilium/cilium#38620, @rastislavs)
- clustermesh: fix mcs-api count of clusters disagreeing with a conflict (the count was previously increased by one) (Backport PR cilium/cilium#38298, Upstream PR cilium/cilium#38267, @MrFreezeex)
- Fix deadlock in compilation lock (Backport PR cilium/cilium#38805, Upstream PR cilium/cilium#38784, @dylandreimerink)
- Fix panic caused in dual cluster setups where LRPs with `skipRedirectFromBackend` flag set to true are installed and IPv6 is disabled. (Backport PR cilium/cilium#38700, Upstream PR cilium/cilium#38656, @aditighag)
- Fix the ipv6 only cluster doesn't work with multi pool in some k8s distribution(Openshift) (Backport PR cilium/cilium#38526, Upstream PR cilium/cilium#38472, @liyihuang)
- Fix: cilium-operator no longer patches services on shutdown (Backport PR cilium/cilium#38298, Upstream PR cilium/cilium#37967, @rsafonseca)
- Fixes an issue where the agent failed to start on clusters with large numbers of network policies. (Backport PR cilium/cilium#38700, Upstream PR cilium/cilium#38556, @squeed)
- netkit: Fix issue where MAC addresses get changed by systemd in L2 mode causing health checks to fail (Backport PR cilium/cilium#38526, Upstream PR cilium/cilium#37812, @jrife)
- Fix checked L4 port for UDP IPv6 packets in check-encryption-leak script. (Backport PR cilium/cilium#38517, Upstream PR cilium/cilium#38265, @smagnani96)
- Fix endianness for WireGuard UDP traffic in the check-encryption-leak script. (Backport PR cilium/cilium#38517, Upstream PR cilium/cilium#38292, @smagnani96)
- Fix erroneous TCP RST condition when no TCP packets in the check-encryption-leak script. (Backport PR cilium/cilium#38517, Upstream PR cilium/cilium#38291, @smagnani96)
- proxy/proxyports: fix flake and data race in TestPortAllocator (Backport PR cilium/cilium#38674, Upstream PR cilium/cilium#38062, @tklauser)
- proxy: fix flake in TestPortAllocator test (Backport PR cilium/cilium#38674, Upstream PR cilium/cilium#38646, @mhofstetter)
- Documentation: fix mentions of per-node `cilium-dbg` tool (Backport PR cilium/cilium#38298, Upstream PR cilium/cilium#38276, @tklauser)
- fix SBOM attestation documentation (Backport PR cilium/cilium#38526, Upstream PR cilium/cilium#38429, @jaehanbyun)
- fix(Documentation/installationk0s.rst): adjust kuberouter naming in k0s documentation (Backport PR cilium/cilium#38298, Upstream PR cilium/cilium#38243, @RiRa12621)
- maglev: Fix division by zero upon table recreation (Backport PR cilium/cilium#38700, Upstream PR cilium/cilium#38659, @borkmann)
- pkg/controller: fix data race in update params locked (Backport PR cilium/cilium#38526, Upstream PR cilium/cilium#38327, @aanm)
- pkg/endpoint: fix GetLabels data race access (Backport PR cilium/cilium#38526, Upstream PR cilium/cilium#38328, @aanm)
- pkg/endpoint: fix race in unit test (Backport PR cilium/cilium#38298, Upstream PR cilium/cilium#38129, @squeed)
- proxy: Fix data race in proxyports test (Backport PR cilium/cilium#38674, Upstream PR cilium/cilium#37890, @jrajahalme)
- [v1.17] hubble/exporter: Fix logging exporter options as JSON (cilium/cilium#38476, @devodev)
- fix AWS ENI IPAM mode performance regression in the Operator when `--update-ec2-adapter-limit-via-api` is set to `true` (cilium/cilium#38532, @antonipp)
- Fix IPv6 for LocalRedirectPolicy with `skipRedirectFromBackend` option. (cilium/cilium#38509, @julianwiedmann)

### 1.17.4

- Fix a bug where a `CiliumNetworkPolicy`/`CiliumClusterwideNetworkPolicy` containing invalid rules would not be reported with invalid status. (Backport PR cilium/cilium#38948, Upstream PR cilium/cilium#38801, @tklauser)
- Fix a bug where services would fail to match wildcard protocols after switching to Local traffic policy with protocol differentiation enabled. (Backport PR cilium/cilium#39404, Upstream PR cilium/cilium#39360, @pasteley)
- Fix a deadlock when a host has no IPv4 address. (Backport PR cilium/cilium#39075, Upstream PR cilium/cilium#38938, @EmilyShepherd)
- Fix a panic happening in the ipset reconciler when a previous reconciliation failed. (Backport PR cilium/cilium#39075, Upstream PR cilium/cilium#38890, @pippolo84)
- Fix bug that would cause the `cilium-dbg encrypt status` command to not list any decryption interfaces when KPR is enabled. (Backport PR cilium/cilium#39214, Upstream PR cilium/cilium#39170, @pchaigno)
- Fixes a bug where layer-7 rules would override enableDefaultDeny: false, incorrectly dropping traffic. (Backport PR cilium/cilium#39375, Upstream PR cilium/cilium#38841, @nimishamehta5)
- gateway-api: Fix Gateway reconciler failure when TLSRoute CRD is not installed (Backport PR cilium/cilium#39377, Upstream PR cilium/cilium#38874, @syedazeez337)
- gateway-api: Fix parentRefMatched to check Group and Kind (Backport PR cilium/cilium#39377, Upstream PR cilium/cilium#39275, @syedazeez337)
- helm: fix hubble dynamic metrics config conflict (Backport PR cilium/cilium#39075, Upstream PR cilium/cilium#38893, @devodev)
- ipsec: Fix key derivation error in case of corrupted boot IDs (Backport PR cilium/cilium#39214, Upstream PR cilium/cilium#39059, @pchaigno)
- k8s: Fixed a case when delete event for service endpointslices might have been missed if connectivity to k8s apiserver was broken causing stale service cache for service. (Backport PR cilium/cilium#38948, Upstream PR cilium/cilium#38779, @marseel)
- xds: Fix a case in which after cilium-agent we were not sending updated resources to Envoy (Backport PR cilium/cilium#38977, Upstream PR cilium/cilium#38654, @marseel)
- bpf: tests: fix ethertype when building inner headers of VXLAN packet (Backport PR cilium/cilium#39075, Upstream PR cilium/cilium#39060, @julianwiedmann)
- cilium: Fix device controller's dependency on netfilter (Backport PR cilium/cilium#38948, Upstream PR cilium/cilium#38777, @borkmann)
- cilium: Fix ipip device mtu (Backport PR cilium/cilium#38948, Upstream PR cilium/cilium#38682, @borkmann)
- contrib/scripts: Fix IndexError in stacktrace script (Backport PR cilium/cilium#39214, Upstream PR cilium/cilium#39101, @christarazi)
- documentation: fix get deployment cmd (Backport PR cilium/cilium#39214, Upstream PR cilium/cilium#39155, @g0gn)
- dynamiclifecycle: fix goroutine leak (Backport PR cilium/cilium#39214, Upstream PR cilium/cilium#39149, @squeed)
- Fix LRU maps to streamline distributed LRU flag implementation with map prealloc handling (Backport PR cilium/cilium#39214, Upstream PR cilium/cilium#39087, @borkmann)
- Fix map recreation loop when distributed lru setting is enabled (Backport PR cilium/cilium#39075, Upstream PR cilium/cilium#38978, @borkmann)
- [v1.17] k8s/statedb: Fix buffering order of objects (cilium/cilium#38585, @joamaki)
- bpf,encrypt: fixes the placement of a particular vxlan helper function (cilium/cilium#39088, @ldelossa)

### 1.17.5

- Fix connections to deleted service backends not getting terminated in certain cases involving services with multiple protocol ports. (Backport PR cilium/cilium#39564, Upstream PR cilium/cilium#37745, @foyerunix)
- Fix handle_policy_egress programs not being cleaned up during endpoint teardown (Backport PR cilium/cilium#39685, Upstream PR cilium/cilium#39560, @ti-mo)
- Fixed bug where datapath is unable to compile when active connection tracking and IPv6 are enabled at the same time. (Backport PR cilium/cilium#39564, Upstream PR cilium/cilium#39509, @dylandreimerink)
- Fixes a bug where a CIDRRule of 0.0.0.0/0 would not select all external traffic. (Backport PR cilium/cilium#39765, Upstream PR cilium/cilium#39693, @squeed)
- helm/hubble: Fix wrong value for metrics server tls existingSecret (Backport PR cilium/cilium#39685, Upstream PR cilium/cilium#39668, @devodev)
- bpf: test: fix up mis-spelled HAVE_NETNS_COOKIE (Backport PR cilium/cilium#39564, Upstream PR cilium/cilium#39420, @julianwiedmann)

### 1.17.6

- Fix bug preventing a global service from including remote backends, if the local service has no selector, and the remote one gets removed and then added again. (cilium/cilium#40361, @giorio94)
- Fix data race involving DumpReliablyWithCallback map operation. (Backport PR cilium/cilium#40094, Upstream PR cilium/cilium#38590, @aditighag)
- Fix IPAM IP release racing condition when IP reassigned back to ENI (Backport PR cilium/cilium#40289, Upstream PR cilium/cilium#40019, @victorcq)
- LBIPAM: Fix deletion of CiliumLoadBalancerIPPool with multiple IP blocks that led to an operator crash (Backport PR cilium/cilium#40094, Upstream PR cilium/cilium#40013, @pippolo84)
- policy: fix error handling for selector policy resolution (cilium/cilium#40404, @fristonio)
- cilium: fix socket termination for v4-in-v6 clients (Backport PR cilium/cilium#40295, Upstream PR cilium/cilium#39994, @borkmann)
- docs/ipsec: Fix incorrect statement on hostns encryption (Backport PR cilium/cilium#40176, Upstream PR cilium/cilium#40133, @pchaigno)

### 1.17.7

- bgp: Use private fork of the GoBGP to fix BGP MD5 auth (Backport PR cilium/cilium#40578, Upstream PR cilium/cilium#40566, @YutaroHayakawa)
- bpf/nat: fix header offset while reverse nat-ing icmp6 pkt too big. (Backport PR cilium/cilium#40387, Upstream PR cilium/cilium#40002, @tommyp1ckles)
- Fix a bug where Cilium leaks stale routes when IPsec is enabled. (Backport PR cilium/cilium#40664, Upstream PR cilium/cilium#40653, @pippolo84)
- fix(helm): fix values.schema.json types for bpf.events.default.{rateLimit,burstLimit} (Backport PR cilium/cilium#40578, Upstream PR cilium/cilium#40543, @vchirikov)
- fix: kube-proxy healthz panic on port 10256 (cilium/cilium#40590, @tamilmani1989)
- install/kubernetes: fix clustermesh-apiserver extraEnv (Backport PR cilium/cilium#41074, Upstream PR cilium/cilium#41021, @aanm)
- pkg/ipam: fix multi-pool allocator not releasing un-used /32 and /128 CIDRs (Backport PR cilium/cilium#40578, Upstream PR cilium/cilium#40393, @alimehrabikoshki)
- Fix GKE cluster creation failures when branch names exceed 63-byte label limit by implementing automatic truncation with hash-based uniqueness preservation. (Backport PR cilium/cilium#40849, Upstream PR cilium/cilium#40725, @pillai-ashwin)
- spire: Fix unreliable test (Backport PR cilium/cilium#40664, Upstream PR cilium/cilium#40561, @joestringer)
- github: fix removal of all files in /mnt (Backport PR cilium/cilium#40849, Upstream PR cilium/cilium#40818, @aanm)
- github: fix upload artifacts for features.json (cilium/cilium#41091, @aanm)
- Fix race condition issues (Backport PR cilium/cilium#40988, Upstream PR cilium/cilium#40949, @aanm)
- Fix bug where LocalRedirectPolicy forwarding would break if you enable `bpf-lb-algorithm-annotation` (cilium/cilium#40246, @tarabrind)

### 1.17.8

- Fix "No mapping for NAT masquerade" flakes in the CI, make NAT LRU fallbacks more robust. (Backport PR cilium/cilium#41369, Upstream PR cilium/cilium#40971, @gentoo-root)
- github: fix upload artifacts for features.json (Backport PR cilium/cilium#41369, Upstream PR cilium/cilium#41119, @aanm)
- ci-aks: Fix concurrency for ipsec tests (cilium/cilium#41161, @joestringer)
- Fix release script steps (Backport PR cilium/cilium#41178, Upstream PR cilium/cilium#41502, @aanm)
- workflows/conformance-ginkgo: fix steps for stable branches (Backport PR cilium/cilium#41618, Upstream PR cilium/cilium#41599, @aanm)
- Fix a bug that caused the kernel verifier on pre-v5.7 kernels to reject the bpf_sock program with "invalid func unknown#122" when the LocalRedirectPolicy feature is enabled. (cilium/cilium#41449, @julianwiedmann)

### 1.17.9

- bpf:tests:egressgw: fix metrics count (Backport PR cilium/cilium#41823, Upstream PR cilium/cilium#40338, @smagnani96)
- Fix a bug that was preventing Cilium to delete stale pod CIDRs routes when changing routing mode to native (Backport PR cilium/cilium#41983, Upstream PR cilium/cilium#41819, @pippolo84)
- Fix a bug where cilium-agent would report "Link not found" for an endpoint deleted during state restore after cilium-agent restart. (Backport PR cilium/cilium#42203, Upstream PR cilium/cilium#40568, @fristonio)
- Fix bug where configuring Cilium with bpfClockProbe=true would fail during BPF compilation (cilium/cilium#42244, @joestringer)
- fix(GH-37724): Sync policies on startup (Backport PR cilium/cilium#41971, Upstream PR cilium/cilium#40357, @anubhabMajumdar)
- Fixes a rare bug where endpoints may have incomplete policies in large clusters. (Backport PR cilium/cilium#42154, Upstream PR cilium/cilium#42049, @squeed)
- operator/pkg/lbipam: fix LoadBalancerIPPool conditions update logic (Backport PR cilium/cilium#41829, Upstream PR cilium/cilium#41322, @alimehrabikoshki)
- policy: Fix a bug where transient errors in endpoint regeneration lead to broken connectivity. (Backport PR cilium/cilium#41971, Upstream PR cilium/cilium#40696, @jrife)
- cli: Fix unreliable tests due to error emitted in Cilium logs "retrieving device lxc*: Link not found" (Backport PR cilium/cilium#42203, Upstream PR cilium/cilium#42146, @fristonio)

### 1.17.10

- Fix cilium_operator_lbipam_conflicting_pools metric to report correct value. (Backport PR cilium/cilium#42316, Upstream PR cilium/cilium#41999, @hanapedia)
- gh: ginkgo: fix focus for service hairpin test (Backport PR cilium/cilium#42651, Upstream PR cilium/cilium#42633, @julianwiedmann)
- workflows: fix GCP OIDC authentication's project ID (cilium/cilium#42174, @nbusseneau)
- fix: run post-release and publish-helm workflows on cilium org (Backport PR cilium/cilium#42316, Upstream PR cilium/cilium#42279, @sekhar-isovalent)

### 1.17.11

- AWS EC2: Fix ENI attachment on multi-network card instances with high-performance networking (EFA) setups (Backport PR cilium/cilium#42744, Upstream PR cilium/cilium#42512, @41ks)
- Fix a bug that would cause IPsec logs to incorrectly report the XFRM rules being processed as "Ingress" rules. (Backport PR cilium/cilium#42827, Upstream PR cilium/cilium#42640, @sjohnsonpal)
- Fix bug that could cause the agent to fail to add XFRM states when IPsec is enabled, thus preventing a proper startup. (Backport PR cilium/cilium#42949, Upstream PR cilium/cilium#42666, @pchaigno)
- Fix certain cases where LRPs with the skipRedirectFromBackend flag set were not correctly processed. (cilium/cilium#42751, @aditighag)
- policy: Fix Endpoint Selector Policy Deadlock (Backport PR cilium/cilium#42969, Upstream PR cilium/cilium#38139, @nathanjsweet)
- policy: Fix rare bug that prevented two endpoints that shared the same identity from being simultaneously updated. (Backport PR cilium/cilium#42969, Upstream PR cilium/cilium#37910, @nathanjsweet)
- policy: Fix rare Endpoint Selector Policy Deadlock causing policies to not be updated with new identities (Backport PR cilium/cilium#42969, Upstream PR cilium/cilium#42306, @odinuge)
- bpf: test: egressgw: fix up ENABLE_MASQUERADE (Backport PR cilium/cilium#42967, Upstream PR cilium/cilium#42912, @julianwiedmann)
- gh: conn-disrupt: fix XFRM error checks (Backport PR cilium/cilium#42765, Upstream PR cilium/cilium#42724, @julianwiedmann)
- gh: ipsec-e2e: fix flaky connection disruptivity test (Backport PR cilium/cilium#42850, Upstream PR cilium/cilium#42780, @julianwiedmann)

### 1.17.12

- Fix an issue in proxy NOTRACK iptables rule for aws-cni chaining mode which causes proxy->upstream(outside cluster) traffic not being SNAT'd. (Backport PR cilium/cilium#43677, Upstream PR cilium/cilium#43566, @fristonio)
- ipcache: Fix leak in CIDR metadata consolidation logic (Backport PR cilium/cilium#43426, Upstream PR cilium/cilium#43074, @christarazi)
- iptables: Fix IPv6 SNAT for L7 proxy upstream traffic (Backport PR cilium/cilium#43677, Upstream PR cilium/cilium#41034, @gentoo-root)
- xds: fix nil-pointer in `processRequestStream` (Backport PR cilium/cilium#43613, Upstream PR cilium/cilium#43609, @mhofstetter)
- [v1.17] ipcache: Fix leak in CIDR metadata consolidation logic (cilium/cilium#43355, @christarazi)

### 1.17.14

- Fix envoy admin socket being created as world-accessible (Backport PR cilium/cilium#44591, Upstream PR cilium/cilium#44512, @0xch4z)
- l7lb: fix bypassing ingress policies for local backends (Backport PR cilium/cilium#44805, Upstream PR cilium/cilium#44693, @smagnani96)
- fix(deps): update k8s.io patch updates stable (v1.17) (patch) (cilium/cilium#44508, @cilium-renovate[bot])
- fix(deps): update k8s.io patch updates stable to v0.32.13 (v1.17) (patch) (cilium/cilium#44582, @cilium-renovate[bot])
- fix(deps): update k8s.io/utils digest to b8788ab (v1.17) (cilium/cilium#44482, @cilium-renovate[bot])
- Fix gke channels (cilium/cilium#44558, @Artyop)

### 1.17.15

- [v1.17] Fix incorrect policy service selector handling (cilium/cilium#44950, @fristonio)
- envoy: Fix xds server npds listeners accounting (Backport PR cilium/cilium#45262, Upstream PR cilium/cilium#44830, @fristonio)
- Fix a slow memory leak triggered by incremental policy updates (Backport PR cilium/cilium#45054, Upstream PR cilium/cilium#44328, @odinuge)
- Fix issue where endpoints got stuck in "waiting-to-regenerate" (Backport PR cilium/cilium#44825, Upstream PR cilium/cilium#42856, @odinuge)
- Fix memory leak triggered by policies being created and deleted (Backport PR cilium/cilium#44825, Upstream PR cilium/cilium#44724, @odinuge)
- Fix panic in Hubble Relay when new peer address is unresolvable (Backport PR cilium/cilium#45238, Upstream PR cilium/cilium#45021, @pesarkhobeee)
- Fixed a bug in dual-stack cluster-pool IPAM where an operator restart with a pre-existing duplicate IPv6 PodCIDR could cause the affected node's IPv4 PodCIDR to be incorrectly freed and reassigned to another node. (Backport PR cilium/cilium#44868, Upstream PR cilium/cilium#44832, @christarazi)
- Fixed an issue where policy update ack is never completed after endpoint deletion. (Backport PR cilium/cilium#44820, Upstream PR cilium/cilium#44754, @jrajahalme)
- Fixed ipcache identity update hang when last proxy listener is removed. (Backport PR cilium/cilium#45262, Upstream PR cilium/cilium#44597, @jrajahalme)
- Fixes increased CPU usage in `hubble observe` caused by log coloring feature, even when coloring was disabled (Backport PR cilium/cilium#44825, Upstream PR cilium/cilium#44119, @tporeba)
- operator/identitygc: fix nil pointer dereference on shutdown (Backport PR cilium/cilium#45238, Upstream PR cilium/cilium#45091, @tsotne95)
- [v1.17] ci: fix setup-eks-cluster action (cilium/cilium#44992, @tklauser)
- fix: escape $ character in regex to prevent injection (Backport PR cilium/cilium#44825, Upstream PR cilium/cilium#44638, @peoyekunle)
- Fix the typo to get the correct ipv6 pool name. (Backport PR cilium/cilium#45054, Upstream PR cilium/cilium#39877, @liyihuang)
- fix(deps): update k8s.io/utils digest to 28399d8 (v1.17) (cilium/cilium#44942, @cilium-renovate[bot])
- [v1.17] ipam: Fix race in multipool test helper causing flaky timeout (cilium/cilium#44870, @christarazi)

### 1.17.16

- fix(ipsec): panic in parseSPI on malformed input (Backport PR cilium/cilium#45506, Upstream PR cilium/cilium#44815, @isoyuki)
- [v1.17] ipam: fix data race in MultiPoolManager node update (cilium/cilium#45383, @Kunalbehbud)
- Fix endpoint identity resolution for static pods whose CNI pod UID differs from the Kubernetes mirror pod UID. (cilium/cilium#45886, @aaroniscode)

### 1.17.17

- multipool: Fix retries for CiliumNode Get errors (Backport PR cilium/cilium#46413, Upstream PR cilium/cilium#46124, @pippolo84)
- fix(deps): update k8s.io/utils digest to ff6756f (v1.17) (cilium/cilium#46004, @cilium-renovate[bot])

### 1.17.18

- Fix incorrect policy denials for traffic to L7 load balanced services when remote identity changes (Backport PR cilium/cilium#47006, Upstream PR cilium/cilium#46821, @fristonio)
- Fix instance of cilium having incorrect specified policy_change_total failure label "failure" value which caused unnecessary warnings. (Backport PR cilium/cilium#46795, Upstream PR cilium/cilium#46388, @tommyp1ckles)
- fix(deps): update k8s.io/utils digest to be93311 (v1.17) (cilium/cilium#46915, @cilium-renovate[bot])
- fix(deps): update k8s.io/utils digest to cf1189d (v1.17) (cilium/cilium#47117, @cilium-renovate[bot])


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.17.18**, the newest release recorded here for this line.

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
