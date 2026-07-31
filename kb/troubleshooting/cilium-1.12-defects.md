---
id: TROUBLE-CILIUM_1_12_DEFECTS
type: troubleshooting
title: "cilium 1.12: defects fixed in the 1.12 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.12.0 <1.13.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.12 known issues
  - cilium 1.12 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.12 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.12: defects fixed in the 1.12 line

## Summary

**263 defects** the project fixed across **20 releases** of the 1.12 line, from 1.12.0 to
1.12.19. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.12.0

- Fix an issue where PodDisruptionBudgets were not created by the Helm chart (#18317, @lic17)
- ingress: Fix conformance tests for host-rules and path-rule (#19321, @sayboras)
- Add/Fix traces for the packets received from the network in IPSec + native routing. (#18704, @YutaroHayakawa)
- Additional FQDN selector identity tracking fixes (Backport PR #17988, Upstream PR #17788, @joestringer)
- alibabacloud: Fix derived VPC CIDR block (#19056, @jaffcheng)
- allocator: fix out-of-valid-range identities being allocated (#18151, @ArthurChiao)
- bug: Fixed a rare CiliumIdentity race deletion. (Backport PR #20333, Upstream PR #19936, @nathanjsweet)
- cilium: Fix node mismatch endpoint restoration bug when the CiliumEndPoint CRD is disabled. (#19040, @zhanghe9702)
- contrib: Fix passing ipFamily to kind.sh (#19707, @brb)
- daemon, option: Fix vlan bpf bypass ids loading (Backport PR #20401, Upstream PR #20282, @pippolo84)
- daemon: Fix issue where stale router IPs were not cleaned up (Backport PR #20519, Upstream PR #20389, @gandro)
- datapath: Fix missing monitor events for NodePort BPF traffic when monitor-aggregation set to > none (#18454, @brb)
- endpoint: Fix packets to host dropped with the chaining mode and host firewall (#19734, @ysksuzuki)
- Fix a bug where agent would log warnings such as "JoinEP: Failed to load program" in legitimate cases where endpoints are getting deleted. (#18216, @aditighag)
- Fix agent crash when IPv6 is partially disabled in the host kernel. (#18716, @pchaigno)
- Fix blackhole route error when cleanup (#20042, @soulseen)
- Fix config map options validation (Backport PR #20401, Upstream PR #20304, @pippolo84)
- Fix drop of large packets redirected through an egress gateway node when running in native routing mode. (Backport PR #20401, Upstream PR #20269, @pchaigno)
- Fix error propagation in bpf_lxc (#20144, @DolceTriade)
- fix identity gc to return correct max/min id (Backport PR #20401, Upstream PR #20361, @dkhachyan)
- Fix mtu setting for tunnel interface in init.sh (Backport PR #20563, Upstream PR #20552, @ChengyuanLiCY)
- Fix the bugs when empty CiliumEndpointSlices were created and leaked. (Backport PR #20519, Upstream PR #20251, @alan-kut)
- Fixed PodCIDR announcement being overwritten by SVC announcement (Backport PR #20519, Upstream PR #20413, @dylandreimerink)
- Fixed removal of stale bpf_netdev tc filters for interfaces with a dot in the name (#18344, @stek29)
- Fixes a bug in the BGP control plane which causes the wrong BGP virtual servers to be selected for reconciliation or removal (#19659, @ldelossa)
- helm: Fix cluster-id arguments in clustermesh deployment (Backport PR #20333, Upstream PR #20312, @sayboras)
- helm: Fix Hubble Service when ServiceMonitor is being used (#19220, @juissi-t)
- helm: Fix invalid type for Certificate spec.ipAddresses (#19211, @superbrothers)
- ipsec: fix stale keys reclaim logic (Backport PR #20401, Upstream PR #19932, @jibi)
- Revert Prometheus client to fix 'cilium metrics list' (#19496, @ti-mo)
- vtep: fix pod src identity in send_trace_notify (Backport PR #20534, Upstream PR #19434, @vincentmli)
- github/workflows: fix hubble installation using cilium-cli (#19568, @aanm)
- bpf/test: Fix incorrect macro definition (#18660, @pchaigno)
- checkpatch: update to lastest image to fix off-by-one index in commit list (#18270, @tklauser)
- config: Fix unit tests for native routing CIDR (Backport PR #20519, Upstream PR #20473, @pchaigno)
- ipam/clusterpool_v2: Fix data race in unit test (#19024, @gandro)
- ipcache: Fix failing controller check from SupportsDelete (#19751, @joamaki)
- jenkinsfiles: fix docker manifest inspect commands in GKE pipeline (Backport PR #20333, Upstream PR #20325, @tklauser)
- mlh: update Jenkins jobs following net-next fix for K8s 1.24 (#20220, @nbusseneau)
- prog_test: Fix build breakage (#18659, @joestringer)
- test/helpers: Fix variadic expansion related panic (Backport PR #20519, Upstream PR #20332, @christarazi)
- test/nat46x64: Fix out-of-bounds index error (#19466, @pchaigno)
- test/RuntimePrivilegedUnitTests: Fix always-passing test (#19231, @pchaigno)
- vagrant: Fix IPv6 NAT setup (#19997, @pchaigno)
- workflows: conformance v1.10: fix native-routing-cidr flag (#18656, @jibi)
- workflows: Downgrade to helm v3.8.2 to fix AWS CNI runs for v1.10 (#20073, @joamaki)
- workflows: Fix concurrency groups (#18193, @pchaigno)
- workflows: Fix the fix to concurrency groups (#18201, @nbusseneau)
- github/workflows: fix hubble-relay cilium-cli installation (#19579, @aanm)
- github: Fix 1.11.1 project link for MLH (#18395, @joestringer)
- github: fix conditions for running CODEOWNERS checks (#18981, @qmonnet)
- github: Fix external workloads workflow for master (#19483, @jrajahalme)
- add roadmap section and fix governance link (#19615, @xmulligan)
- alibabacloud: Fix missing instance due to incomplete subnet list (#19155, @jaffcheng)
- alignchecker: fix LLVM 15 build by removing an unused variable (#19368, @aspsk)
- avoid calling OnFlowDelivery with nil (#18605, @kaworu)
- bgp,testing: fix race condition in checking fencer map (#18884, @ldelossa)
- bgp: Fixed broken bgp speaker unit tests (Backport PR #20519, Upstream PR #20521, @dylandreimerink)
- bpf: Fix implicit cast for BPF TPROXY debug message (#18429, @pchaigno)
- bpf: specify handle_lxc_traffic return type to fix -Wimplicit-int error (#19891, @tklauser)
- daemon: Fix build after VTEP routes conflict (#20077, @joestringer)
- eni: Fix broken build due to unit test (#19278, @gandro)
- Fix a function comment typo (#18231, @hangyan)
- Fix a typo in the documentation (#18411, @gjkim42)
- Fix comment for EndpointCreated function (#19465, @Jiang1155)
- Fix missing capabilities when not running Cilium on containerd-based Kubernetes (#19903, @AtkinsChang)
- Fix running documentation make targets on MacOS (#19900, @chancez)
- Fix smoke tests by filtering out go_* metrics from metrics linting (#19399, @chancez)
- Fix the typo in Fatalf message of printConfigurations (#18413, @21kyu)
- Fixed warnings generated by "make -C test/bpf/ nat-test" due to improper castings (#18015, @cdelzotti)
- Fixes:Added the declaration of license (#19834, @yulng)
- fqdn/dnsproxy: fix test build (Backport PR #20534, Upstream PR #20537, @tklauser)
- github: Backport DNS fix for external workloads 1.10 and 1.11 tests (#19516, @jrajahalme)
- helm: Fix syntax error in Hubble UI className (#20056, @gandro)
- images: Fix build on arm64 (#18795, @jrajahalme)
- install/cilium-operator: fix clusterrole rules (#19686, @aanm)
- install: Fix typos of cilium (#20113, @twpayne)
- localdev: fix kind helm install shell function (#19149, @ldelossa)
- maglev: fix TestPermutations backend generation (#19663, @kaworu)
- maps/lbmap: fix maglev test suite build (#19435, @tklauser)
- pkg/endpoint: fix data race in endpoint logger (#18769, @aanm)
- README.rst: fix stable release table (#19517, @tklauser)
- test/bpf: Fix format of `check-complexity.sh` script (#19836, @pchaigno)
- test/bpf: Fix mock dependencies (#19099, @joestringer)
- treewide: Fix typos of Kubernetes (#20114, @twpayne)
- trivial: Fix test step stutter 'to to' (#18188, @joestringer)
- vagrant: fix overlap of IPv6 Node/Pod CIDRs on dev-VM (#19303, @julianwiedmann)
- Fix unstripped id for gh action (#20319, @jtaleric)

### 1.12.1

- fqdn/metrics: Fix ProxyUpstreamTime error=timeout (Backport PR #20851, Upstream PR #20752, @joestringer)
- Fix bug where Cilium would crash on startup with an error about being unable to delete iptables rules. (Backport PR #20890, Upstream PR #20885, @jibi)
- Fix bug where network policies that select namespace labels may incorrectly select identities ([Advisory](https://github.com/cilium/cilium/security/advisories/GHSA-pfhr-pccp-hwmh), commit 2494ce4dca59)
- Fix bug where traffic sent outside the cluster via ToFQDNs policy would be denied despite a policy that allows it (Backport PR #20851, Upstream PR #20721, @joestringer)
- Fix ineffective post-start hook in ENI mode (Backport PR #20851, Upstream PR #20741, @bmcustodio)
- fix k8s latency metrics label cardinality (Backport PR #20851, Upstream PR #20831, @aanm)
- Fix parsing of string map command line options when more than one separator is present. (Backport PR #20851, Upstream PR #20673, @tklauser)
- Fix regression with cilium-health-probe controller in IPv6-only clusters (Backport PR #20867, Upstream PR #20849, @aanm)
- ipcache/kvstore: fix panic when processing ip=<nil> entries (Backport PR #20867, Upstream PR #20706, @ArthurChiao)
- CHANGELOG: fix v1.12.0 changelog (#20696, @aanm)
- Fix `subnet_id` label value being empty in IP allocation and interface creation in ENI IPAM metrics (Backport PR #20851, Upstream PR #20449, @wu0407)
- Fix complaint about nil IP address on restore of cilium_host (Backport PR #20867, Upstream PR #20734, @christarazi)
- ipcache: Fix lock leak (Backport PR #20851, Upstream PR #20833, @joestringer)

### 1.12.2

- clustermesh-apiserver: fix key name for delete during k8s->kvstore sync (Backport PR #21122, Upstream PR #21078, @tklauser)
- Fix conflicting routes for multiple ENIs in IPAM mode (Backport PR #21225, Upstream PR #20112, @recollir)
- Fix identity garbage collection in clustermesh environments (#20932, @aanm)
- Fix node label synchronization in the KVStore when IPSec configuration changes (Backport PR #21122, Upstream PR #21087, @aanm)
- Fix panic during Cilium initialization when a NetworkPolicy with a named-port selected an pod running on that node. (Backport PR #21053, Upstream PR #20911, @aanm)
- Fix Wireguard connectivity issues when using kvstore mode (Backport PR #21225, Upstream PR #21080, @aanm)
- Fixes typos in enabling fqdn_semaphore_rejected_total metric (Backport PR #20940, Upstream PR #20893, @rahulkjoshi)
- ipsec: Fix incorrect parsing of SPI from mark (Backport PR #20940, Upstream PR #20900, @pchaigno)
- k8s/watchers: fix panic in CiliumEndpoint labels update (Backport PR #21053, Upstream PR #20865, @jaffcheng)
- kvstore/allocator: fix panic on receiving invalid identity entries (Backport PR #21292, Upstream PR #21213, @ArthurChiao)
- metrics: fix ts_events API timestamp only emitting zero and unbounded scope label cardinality issue. (Backport PR #21053, Upstream PR #20977, @tommyp1ckles)
- pkg/k8s/watcher: fix deadlock crash that occurs when handling endpoint and service updates. (Backport PR #21225, Upstream PR #21093, @tommyp1ckles)
- v1.12: operator: fix key name for delete during k8s->kvstore sync (#20984, @tklauser)
- [v1.12] vagrant: Bump 4.9 Vagrant box (Linux 4.9.326, to fix a kernel bug) (#21260, @tklauser)
- k8s: fix test flake in TestGenerateToCIDRFromEndpoint. (Backport PR #21225, Upstream PR #21220, @tommyp1ckles)
- k8s: fix test flake in TestGenerateToCIDRFromEndpoint. (Backport PR #21292, Upstream PR #21220, @tommyp1ckles)

### 1.12.3

- bugtool: Fix pprof default ports (Backport PR #21631, Upstream PR #21497, @pippolo84)
- daemon: Fix a nil dereference on cleanup when DNS proxy is not enabled (Backport PR #21466, Upstream PR #21365, @joamaki)
- Fix agent deadlock caused by frequent kube-apiserver IP recycling (Backport PR #21637, Upstream PR #21629, @joestringer)
- Fix bug that can cause some traffic covered by an L7 policy to be dropped when IPsec is enabled on EKS. (Backport PR #21646, Upstream PR #21595, @pchaigno)
- Fixes cilium startup on certain AWS-VPC clusters. (Backport PR #21631, Upstream PR #21444, @squeed)
- ipcache: Fix metadata access from CIDR allocation (Backport PR #21637, Upstream PR #21565, @joestringer)
- alibabacloud: fix incorrect instance-type reported by cilium-agent (Backport PR #21631, Upstream PR #21495, @ArthurChiao)
- Fix a typo in the comment example (Backport PR #21466, Upstream PR #21402, @farcaller)
- Fix grpc-ingress.yaml path in Service Mesh docs (Backport PR #21646, Upstream PR #21601, @pippolo84)
- helm: Fix post-start and pre-stop hooks for cilium-nodeinit on Ubuntu EKS images (Backport PR #21466, Upstream PR #20979, @dctrwatson)
- ipsec: Fix slightly incorrect assumption in XFRM IN policies (Backport PR #21646, Upstream PR #21621, @pchaigno)

### 1.12.4

- Fix overlapping/duplicate PodCIDR allocation when nodes are added while operator is down (Backport PR #22028, Upstream PR #21526, @dylandreimerink)
- Fixed CCNP garbage collection (Backport PR #21809, Upstream PR #21394, @zuzzas)
- Fixes a deadlock that can be exposed in high-churn clusters when Pods are deleted rapidly. (Backport PR #21809, Upstream PR #21771, @squeed)
- Fix incorrect env var name used in docs for Helm installation on Rancher Desktop (Backport PR #22028, Upstream PR #21835, @ehausig)

### 1.12.5

- Fix bug that could lead to inconsistent pod IP information between agents, sometimes leading to a failure to decrypt IPsec traffic. (Backport PR #22308, Upstream PR #22127, @aanm)
- Fix bug where configuring the API rate limiter options could fail when providing multiple options (Backport PR #22696, Upstream PR #22299, @thorn3r)
- Fix Cilium fatal "Could not create or update CiliumNode resource, despite retries" on environments with `enable-ipv4-egress-gateway` (Backport PR #22308, Upstream PR #22298, @aanm)
- Fix forwarding of the security identity by the DNS proxy which could cause random policy denials (Backport PR #22407, Upstream PR #22361, @aspsk)
- Fix GC of CEPs that were not GCed by kube-apiserver (Backport PR #22308, Upstream PR #22213, @aanm)
- fix: some tofqdn flags not being parsed (Backport PR #22500, Upstream PR #22346, @carloscastrojumo)
- Prevent cilium operator crash in AWS region with IPv6-only ENIs without subnet filters. (Backport PR #22308, Upstream PR #22075, @bimmlerd)
- github: fix bpf-checks on ubuntu-latest runner (Backport PR #22328, Upstream PR #22322, @julianwiedmann)
- daemon/cmd: Fix error handling for getting proxy port (Backport PR #22500, Upstream PR #22296, @christarazi)
- fix 'egressIP' field indentation (Backport PR #22500, Upstream PR #22303, @yulng)
- mtu, node: fix build on all non-linux platforms (Backport PR #22308, Upstream PR #22232, @tklauser)
- Update documentation related to metrics; fix incorrect FQDN metrics reference (Backport PR #22308, Upstream PR #22300, @christarazi)

### 1.12.6

- Fix crash of CES queue delay metric when CESTracker is nil (Backport PR #23260, Upstream PR #22884, @dlapcevic)
- Added Agent init check that removes all CiliumEndpoints referencing local Node that are not managed. This fixes issues where sometimes CiliumEndpoints referencing still running Pods can become unmanaged during Cilium restart. (Backport PR #23096, Upstream PR #20350, @tommyp1ckles)
- bpf: nat: fix snat_v4_can_skip() for egress gateway (Backport PR #23331, Upstream PR #23274, @jibi)
- bpf: nodeport: fix drop notification in IPv6 revNAT (Backport PR #23003, Upstream PR #22543, @julianwiedmann)
- bpf: nodeport: fix tracing for handle_nat_fwd() (Backport PR #23260, Upstream PR #22678, @julianwiedmann)
- datapath: Fix L7 ingress with XDP (Backport PR #23260, Upstream PR #22985, @brb)
- envoy: Fix lock leak in config validation failure (Backport PR #23301, Upstream PR #23077, @joestringer)
- Fix a data race in dnsproxy which could lead to DNS requests drops. (Backport PR #23003, Upstream PR #22619, @aspsk)
- Fix bugs where ciliumendpoints for statefulset pods where being incorrectly overwritten/deleted (Backport PR #23096, Upstream PR #21768, @tommyp1ckles)
- Fix missing node neigh metric for counting arping requests (Backport PR #23260, Upstream PR #22930, @christarazi)
- Fix packet drops when service pod connects to itself via clusterIP, and selected by an ingress policy. (Backport PR #23260, Upstream PR #22972, @aditighag)
- Fixes `semaphore_rejected_total` metric and adds new `scope` to `proxy_upstream_reply_seconds` metric. (Backport PR #23260, Upstream PR #21267, @rahulkjoshi)
- ipsec: Fix packet mark for FWD XFRM policy (Backport PR #23301, Upstream PR #23254, @pchaigno)
- bpf: test: fix xdp_lb4_forward_to_other_node test (Backport PR #23260, Upstream PR #23018, @julianwiedmann)
- ctmap: fix-up host_local flag in the DSR NAT entry for GC test (Backport PR #23260, Upstream PR #23037, @julianwiedmann)
- test/helpers: Fix retry condition for CiliumExecContext (Backport PR #23003, Upstream PR #22726, @christarazi)
- ci, github: Fix IPv6 conformance test (Backport PR #23003, Upstream PR #22774, @borkmann)
- gh: fix indentation bug in ingress workflows (Backport PR #23301, Upstream PR #23195, @julianwiedmann)

### 1.12.7

- Avoid deprecation warnings for CiliumEgressNATPolicy when the resource isn't used. (#23226, @pchaigno)
- Fix masquerading bug that caused kube-proxy to pick the wrong IPv4 address in case of tunneling with endpoint routes. (Backport PR #23465, Upstream PR #23241, @pchaigno)
- proxy: Fix deadlock in error path of CreateOrUpdateRedirect (Backport PR #23465, Upstream PR #23377, @gandro)
- certloader flake fixes (Backport PR #23465, Upstream PR #22995, @kaworu)
- github/workflows: fix external contribution detection (Backport PR #23465, Upstream PR #23406, @aanm)
- github/workflows: PR labeler fix GH workflow if expression (Backport PR #23515, Upstream PR #23482, @aanm)
- cilium: Fix missing error log dump from compilation (Backport PR #23465, Upstream PR #23339, @borkmann)

### 1.12.8

- [EKS] Fix deadlock causing network connectivity outages when kube-apiservers scale down (Backport PR #23957, Upstream PR #23836, @christarazi)
- agent: fix incorrect deletion of veth host interfaces on bootstrap (Backport PR #23957, Upstream PR #23787, @giorio94)
- Avoid k8s CiliumNode initialization problems when Cilium connects to the KVStore (Backport PR #24197, Upstream PR #24156, @aanm)
- cilium-health status: fix endpoint reachability in succinct view (Backport PR #23779, Upstream PR #23506, @giorio94)
- clustermesh: fix services cache bloat due to incorrect deletion (Backport PR #24083, Upstream PR #23947, @giorio94)
- Fix connectivity issue upon agent restart in case of ipv6 + direct routing + KPR replacement (Backport PR #23957, Upstream PR #23857, @giorio94)
- Fix enable-stale-cilium-endpoint-cleanup flag not actually disabling the cleanup init set when set to false. This provides a workaround for an existing panic that can occur when running using etcd kvstore. (Backport PR #24310, Upstream PR #23874, @sjdot)
- Fix operator crash race condition for CES identity map concurrent read/write (Backport PR #24197, Upstream PR #23605, @dlapcevic)
- ipam/crd: Fix panic due to concurrent map read and map write (Backport PR #23779, Upstream PR #23713, @gandro)
- bpf: Fix usage of tunnel map structs (Backport PR #24083, Upstream PR #23469, @pchaigno)
- Fixed link to broken anchor in RKE doc (Backport PR #23779, Upstream PR #23706, @raphink)
- workflow: fixes LLVM, Clang cache and install path (Backport PR #23779, Upstream PR #23740, @brlbil)
- v1.12 backport: fix cgroup program detachment and 1.14 downgrade (#24183, @ti-mo)

### 1.12.9

- Add missing xfrm-no-track rules for IPv6 IPSec. This fixes a connectivity issue for IPv6 IPSec with externalTrafficPolicy=local. (Backport PR #24605, Upstream PR #24557, @jschwinger233)
- bpf: policy: fix handling of ICMPv6 packet with extension headers (Backport PR #24822, Upstream PR #24797, @julianwiedmann)
- endpoint: fix k8sNamespace log field when ep gets deleted (Backport PR #24709, Upstream PR #24575, @mhofstetter)
- Fix bug in BGP CP where changing the route-id of an existing router would cause announcements to disappear (Backport PR #24462, Upstream PR #24304, @dylandreimerink)
- Fix Cilium Operator from crashing when encountering empty node pools on Azure (Backport PR #24462, Upstream PR #24189, @forgems)
- Fix for disabled cloud provider rate limiting (Backport PR #24462, Upstream PR #24413, @hemanthmalla)
- Fix missing delete events on informer re-lists to ensure all delete events are correctly emitted and using the latest known object state, so that all event handlers and stores always reflect the actual apiserver state as best as possible (#24871, @aanm)
- Fixed bug where L7 rules would be incorrectly merged between rules for the same (remote) endpoint. This bug could have caused L7 rules to be bypassed via a wildcard header rule being improperly appended to the set of HTTP rules when both a policy with HTTP header rules applying to multiple endpoints and an allow-all rule for only one of those endpoints are specified. (Backport PR #24851, Upstream PR #24788, @jrajahalme)
- Fix race conditions when deleting CNP / CCNP in e2e tests (Backport PR #24709, Upstream PR #24484, @jschwinger233)
- renovate: Fix Hubble release digest regex (Backport PR #24605, Upstream PR #24477, @gandro)
- Avoid clearing objects in CiliumEndpoint conversion funcs (Backport PR #24930, Upstream PR #24928, @aanm)
- Avoid clearing objects in conversion funcs (Backport PR #24930, Upstream PR #24241, @odinuge)
- checker: Fix incorrect checker for ExportedEqual() (Backport PR #24462, Upstream PR #24373, @christarazi)
- Fix duplicated logs for test-output.log (Backport PR #24462, Upstream PR #24171, @romanspb80)
- Add note about fixed regression in ConfigMap values that were being prioritized over flags in Cilium agent (#24744, @aanm)
- v1.12: docs: Fix mitigation for IPsec upgrade issue (#24702, @pchaigno)

### 1.12.10

- datapath: Fix double SNAT (Backport PR #25248, Upstream PR #25189, @brb)
- Fix bug where Cilium configurations running with tunneling disabled, BPF-masq disabled, but with masquerading enabled, do not clean up ipset configuration when a node IP changes. This can lead to a lack of masquerading on those node IPs. (Backport PR #25012, Upstream PR #24825, @christarazi)
- Fix connectivity issue if nodes share the same name across the clustermesh and wireguard is enabled (Backport PR #25012, Upstream PR #24785, @giorio94)
- Fix data race affecting the preferred mark in backends, e.g. backends selected by service with affinity set to local. In very rare cases a backend might be missing its preferred status and a non-local backend might be selected. (Backport PR #25348, Upstream PR #25087, @joamaki)
- Fix incorrect network policy ebpf setup that may lead to incorrect packets denies when CEP is present in multiple CES (Backport PR #25188, Upstream PR #24838, @alan-kut)
- Fix spurious errors containing "Failed to map node IP address to allocated ID". (Backport PR #25348, Upstream PR #25222, @bimmlerd)
- ipsec: Fix packet mark for FWD XFRM policy (Backport PR #25348, Upstream PR #23254, @pchaigno)
- pkg/kvstore: Fix for deadlock in etcd status checker (Backport PR #25012, Upstream PR #24786, @hemanthmalla)
- inctimer: fix test flake where timer does not fire within time. (Backport PR #25248, Upstream PR #25219, @tommyp1ckles)
- pkg/service: Backends leak follow ups with revised fixes, debugging improvements and unit tests (Backport PR #25248, Upstream PR #24770, @aditighag)
- [v1.12] contrib/backporting: Fix main branch reference (#25092, @joestringer)
- contrib/backporting: Fix main branch reference (#25140, @sayboras)

### 1.12.11

- Fix a bug due to which we would leak Linux XFRM policies, potentially leading to increased CPU consumption, when IPsec is enabled with Azure or ENI IPAM. (Backport PR #25896, Upstream PR #25784, @pchaigno)
- Fix a bug that would cause connectivity drops of type XfrmInNoStates on upgrade when IPsec is enabled with ENI or Azure IPAM mode. (Backport PR #25896, Upstream PR #25724, @pchaigno)
- Fix a bug that would cause connectivity drops of type XfrmOutPolBlock on upgrade when IPsec is enabled. (Backport PR #25896, Upstream PR #25735, @pchaigno)
- Fix a possible deadlock when using WireGuard transparent encryption. (Backport PR #25928, Upstream PR #25419, @bimmlerd)
- Fix bug affecting EKS installations with IPsec encryption enabled, where Cilium wouldn't attach its IPsec BPF program to new ENI interfaces, resulting in connectivity loss between pods on remote nodes. (Backport PR #25896, Upstream PR #25744, @joamaki)
- Fix false error log message when IPsec is enabled with IPAM modes ENI or Azure and a remote node is deleted. (Backport PR #26161, Upstream PR #26093, @pchaigno)
- Fix incorrect hubble flow data when HTTP requests contain an `x-forwarded-for` header by adding an explicit `use_remote_address: true` config to Envoy HTTP configuration to always use the actual remote address of the incoming connection rather than the value of `x-forwarded-for` header, which may originate from an untrusted source. This change has no effect on Cilium policy enforcement where the source security identity is always resolved before HTTP headers are parsed. Previous Cilium behavior of not adding `x-forwarded-for` headers is retained via an explicit `skip_xff_append: true` config setting, except for Cilium Ingress where the source IP address is now appended to `x-forwarded-for` header. (Backport PR #25732, Upstream PR #25674, @jrajahalme)
- Fix leak of IPsec XFRM FWD policies in IPAM modes `cluster-pool`, `kubernetes`, and `crd` when nodes are deleted. Fix incorrect catch-all default-drop XFRM OUT policy for IPsec IPv6 traffic that could lead to leaking plain-text IPv6 traffic if combined with some other bug. (Backport PR #26117, Upstream PR #25953, @pchaigno)
- Fix the bug when long-living connections using egress gateway may be reset. (Backport PR #25678, Upstream PR #24905, @gentoo-root)
- Fix three issues in the bug fix to attach IPsec BPF programs to ENI interfaces: do not fatal if loading unexpectedly fails (which may happen if the device is suddenly deleted), ignore veth device changes in order not to reinitialize when new endpoints appear and wait 1 second for further device state changes between reinitializations. (Backport PR #26006, Upstream PR #25936, @joamaki)
- ipsec: Fix cleanup of XFRM states and policies (Backport PR #26117, Upstream PR #26072, @pchaigno)

### 1.12.12

- Fix bug that caused transient IPsec packet drops on upgrades when tunneling is enabled. (Backport PR #26859, Upstream PR #26708, @pchaigno)
- Fix bug where CNI gets installed even if cni.install=false (Backport PR #26420, Upstream PR #26278, @joestringer)
- Fix path asymmetry when using pod-to-pod encryption with IPsec and tunnel mode. (Backport PR #26859, Upstream PR #25440, @pchaigno)
- Fixed Cilium agent crash when policy refers to a non-existing Envoy listener. (Backport PR #26420, Upstream PR #25969, @jrajahalme)
- Fixed proxy redirect policy implementation when any deny rule prevents them. (Backport PR #26750, Upstream PR #26344, @jrajahalme)
- ipsec: Split removeStaleXFRMOnce to fix deprioritization issue (Backport PR #26420, Upstream PR #26113, @jschwinger233)
- Fix "make -C Documentation builder-image" (Backport PR #26916, Upstream PR #26874, @michi-covalent)

### 1.12.13

- Fix a bug that could cause packet drops of type XfrmOutPolBlock when IPsec is enabled and node are recycled. (Backport PR #27138, Upstream PR #27029, @pchaigno)
- Fix a bug that could cause IPsec-encrypted packets to be sent to the wrong destination node when node churn is high. (Backport PR #27138, Upstream PR #27029, @pchaigno)
- Documentation: fix the broken links/dead links (Backport PR #27155, Upstream PR #26880, @vipul-21)
- k8s: fix incorrect EndpointSlice API version (#27378, @nebril)
- Update Service Mesh docs to fix a number of issues (#27335, @youngnick)

### 1.12.14

- Fix a bug that affected the RevDNAT translation of IPv6 packets with extension headers. (Backport PR #27394, Upstream PR #27312, @julianwiedmann)
- Fix a bug that could cause an incorrect max. sequence number to be reported by `cilium encrypt status` when IPsec is enabled. (Backport PR #27934, Upstream PR #27656, @pchaigno)
- Fix bug limiting pod-to-pod network performance under high load when tunneling and IPSec are both enabled. (Backport PR #27394, Upstream PR #27168, @learnitall)
- Fix bug that could cause packet drops of type XfrmOutPolBlock while rotating the IPsec key. (Backport PR #27588, Upstream PR #27319, @jrfastab)
- Fix connectivity issues caused by missing conntrack entry when service pod connects to itself via clusterIP. (Backport PR #27980, Upstream PR #27602, @julianwiedmann)
- IPSec fix for race on init resulting in Xfrm*In* errors and dropped packets (Backport PR #28029, Upstream PR #28012, @jrfastab)

### 1.12.15

- bump grpc dependency to 1.56.3 to fix security vulnerability https://github.com/advisories/GHSA-qppj-fm5r-hxr3 (#28529, @aanm)
- bpf: fix error handling for invoke_tailcall_if() (Backport PR #28414, Upstream PR #26118, @julianwiedmann)
- bpf: lxc: fix one missing drop notification in CT lookup tail calls (Backport PR #28351, Upstream PR #26115, @julianwiedmann)
- envoy: Sync supported resources to fix not found issue (Backport PR #28351, Upstream PR #28272, @sayboras)
- Fix a bug that causes pod-to-pod traffic between nodes to be dropped when IPsec is enabled and kube-proxy installed rules in both iptables-nft and iptables-legacy. (Backport PR #28444, Upstream PR #28258, @pchaigno)
- Fix missing drop notifications on conntrack lookup failures when IPv4 and IPv6 are both enabled or socket-level load balancing is disabled. (Backport PR #28295, Upstream PR #25426, @bleggett)
- Fix the trace notification for hairpinned reply traffic, to indicate the correct security identity for the client. (Backport PR #28295, Upstream PR #28133, @julianwiedmann)
- Fixes a bug causing panic when counting IPsec keys number via "cilium encrypt status". (Backport PR #28295, Upstream PR #27996, @jschwinger233)
- Fix potential nil pointer dereference in SelectorManager implementation (Backport PR #28104, Upstream PR #27805, @learnitall)
- Backport v1.12: FQDN fixes (#28138, @joamaki)
- cocci: backport fix about incorrect warnings and resolve warning related to a const qualifier (#28287, @giorio94)

### 1.12.16

- policy: Fixed a bug that incorrectly omitted port-protocol policy rules that omitted the "protocol" field. An omitted "protocol" field now, correctly, is the same as using the "ANY" protocol. (Backport PR #28762, Upstream PR #28703, @nathanjsweet)
- Fix CIDR labels computation (Backport PR #28893, Upstream PR #28788, @pippolo84)
- Fix IPsec error logs to always have all information needed to identify the XFRM configuration on which the error happened. (Backport PR #29035, Upstream PR #28642, @pchaigno)
- bpf: lb: fix missing drop reason in reverse_map_l4_port() (Backport PR #29035, Upstream PR #28884, @julianwiedmann)

### 1.12.17

- datapath: Fix ENI egress routing table for cilium_host IP (Backport PR #29392, Upstream PR #29335, @gandro)
- Fix bug where deleted nodes would reappear in the cilium_node_connectivity_* metrics (Backport PR #29639, Upstream PR #29566, @christarazi)
- ci-ipsec-upgrade: Fix upgrade/downgrade path and add missed tail calls check to upgrade (Backport PR #29005, Upstream PR #29072, @brb)

### 1.12.18

- Fix and prevent future bugs limiting pod-to-pod network performance under high load when tunneling and IPSec are both enabled. (Backport PR #30004, Upstream PR #29616, @learnitall)
- nodediscovery: Fix bug where CiliumInternalIP was flapping (Backport PR #29979, Upstream PR #29964, @gandro)
- datapath: Fix TestNodeChurnXFRMLeaks (Backport PR #30082, Upstream PR #27274, @brb)
- v1.12: ipam: Fix invalid PodCIDR in CiliumNode in ENI/Azure/MultiPool mode (#30147, @pchaigno)

### 1.12.19

- ci/ipsec: Fix version retrieval for downgrades to closest patch release (Backport PR #30678, Upstream PR #30503, @qmonnet)
- [v1.12] ci/ipsec: Fix downgrade version for release preparation commits (#30714, @qmonnet)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.12.19**, the newest release recorded here for this line.

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
