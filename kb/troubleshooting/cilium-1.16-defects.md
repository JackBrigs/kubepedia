---
id: TROUBLE-CILIUM_1_16_DEFECTS
type: troubleshooting
title: "cilium 1.16: defects fixed in the 1.16 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.16.0 <1.17.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.16 known issues
  - cilium 1.16 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.16 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.16: defects fixed in the 1.16 line

## Summary

**179 defects** the project fixed across **19 releases** of the 1.16 line, from 1.16.0 to
1.16.19. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.16.0

- mountain_cableway: *Networking* :speedboat: *Cilium NetKit:* container-network throughput and latency as fast as host-network. :globe_with_meridians: *BGPv2:* Fresh new API for Cilium's BGP feature. :loudspeaker: *BGP ClusterIP Advertisement:* BGP advertisements of ExternalIP and Cluster IP Services. :twisted_rightwards_arrows: *Service Traffic Distribution:* Kubernetes 1.30 Service Traffic Distribution can be enabled directly in the Service spec instead of using annotations. :arrows_counterclockwise: *Local Redirect Policy promoted to Stable:* Redirecting the traffic bound for services to the local backend, such as node-local DNS. :satellite: *Multicast Datapath:* Define multicast groups in Cilium. :label: *Per-Pod Fixed MAC Address:* Specify the MAC address used on a pod

### 1.16.1

- auth: Fix data race in Upsert (Backport PR #34158, Upstream PR #33905, @chaunceyjiang)
- BGPv1 + BGPv2: Fix incorrect service reconciliation in setups with multiple BGP instances (virtual routers) (Backport PR #34297, Upstream PR #34177, @rastislavs)
- bgpv1: Fix data race in bgppSelection (Backport PR #34158, Upstream PR #33904, @chaunceyjiang)
- BGPv2: Fix `Service` advertisement selector: do not require matching `CiliumLoadBalancerIPPool` (Backport PR #34201, Upstream PR #34182, @rastislavs)
- Fix a nil dereference crash during cilium-agent initialization affecting setups with FQDN policies. The crash is triggered when a restored endpoint performs a DNS request just a the right time during early cilium-agent restoration. Problem is not expected to be persistent and the agent should get pass the problematic part of the initialization on restart. (Backport PR #34158, Upstream PR #34059, @joamaki)
- Fix appArmorProfile condition for CronJob helm template (Backport PR #34297, Upstream PR #34100, @sathieu)
- Fix bug causing etcd upsertion/deletion events to be potentially missed during the initial synchronization, when Cilium operates in KVStore mode, or Cluster Mesh is enabled. (Backport PR #34181, Upstream PR #34091, @giorio94)
- Fix issue in picking node IP addresses from the loopback device. This fixes a regression in v1.15 and v1.16 where VIPs assigned to the lo device were not considered by Cilium. Fix spurious updates node addresses to avoid unnecessary datapath reinitializations. (Backport PR #34085, Upstream PR #34012, @joamaki)
- Fix possible connection disruption on agent restart with WireGuard + kvstore (Backport PR #34158, Upstream PR #34062, @giorio94)
- Fixes DNS proxy "connect: cannot assign requested address" errors in transparent mode, which were due to opening multiple TCP connections to the upstream DNS server. (Backport PR #34201, Upstream PR #33989, @bimmlerd)
- lbipam: fixed bug in sharing key logic (Backport PR #34158, Upstream PR #34106, @dylandreimerink)
- policy: Fix policy cache covers context lookup. (cilium/cilium#34322, @nathanjsweet)
- Fix workflow telemetry in ci-ipsec-upgrade (Backport PR #34158, Upstream PR #34097, @chancez)
- Fix two bugs in dnsproxy tcp conn reuse (Backport PR #34201, Upstream PR #34175, @bimmlerd)

### 1.16.2

- bgpv2: fix cilium-dbg bgp filtering by ASN & route-policy dump format (Backport PR #34452, Upstream PR #34335, @rastislavs)
- bpf: Fix `Prune` map operation leaking BPF map entries (Backport PR #34586, Upstream PR #34476, @gandro)
- config: fix disabling config 'Debug' (Backport PR #34469, Upstream PR #34401, @mhofstetter)
- daemon: Fix error logic flow for pod store being out of date (Backport PR #34586, Upstream PR #34389, @christarazi)
- envoy: fix log level mapping when changing log level via API (Backport PR #34452, Upstream PR #34400, @mhofstetter)
- Fix "invalid sysctl parameter" error when Cilium needs to modify a sysctl with capital letters in its name. (Backport PR #34586, Upstream PR #34298, @julianwiedmann)
- Fix a bug in Cilium's kube-proxy replacement, where replies by a local backend are dropped with DROP_NO_FIB. (Backport PR #34452, Upstream PR #34303, @julianwiedmann)
- Fix a race condition that would cause errors related to maps `LB{4,6}_SKIP_MAP` when loading programs. (Backport PR #34586, Upstream PR #34453, @pchaigno)
- Fix agent panic when IPsec is enabled but XFRM stats are not exposed by the kernel. (Backport PR #34831, Upstream PR #34647, @chaunceyjiang)
- Fix issue where a hostport service would be created on an incorrect node when cilium-agent is configured with disable-endpoint-crd (Backport PR #34644, Upstream PR #34385, @haozhangami)
- Fix operator deployment connecting to clustermesh kvstoremesh when endpointslice sync or MCS-API Service exports is enabled (Backport PR #34586, Upstream PR #34295, @MrFreezeex)
- Fix parsing of complex api-rate-limit options. The parsing failed when rate limits were configured for multiple API endpoints with multiple options, for example: "endpoint-create=rate-limit:1/s,rate-burst=1,endpoint-delete=rate-limit:2/s,rate-burst=2". The ability to also specify the rate limits as JSON strings was also returned. (Backport PR #34586, Upstream PR #34249, @joamaki)
- Fix possible connection disruption on agent restart with WireGuard + native routing (Backport PR #34831, Upstream PR #34095, @giorio94)
- Fix possible panic occurring in case errors are returned while updating/deleting IPv6 routes (Backport PR #34831, Upstream PR #34721, @giorio94)
- Fix the Egress Gateway reconciliation logic to make progress after setting the rp_filter sysctl failed. (Backport PR #34831, Upstream PR #34775, @julianwiedmann)
- Fixes broken pod-to-remote-hostport connectivity when IPsec is used with L7 ingress policy and KPR. (Backport PR #34586, Upstream PR #33805, @jschwinger233)
- Fixes deadlock in identity watcher. This fixes an issue where a kvstore disconnect can cause the event receiver to exit and the event sender to get stuck forever. (Backport PR #34831, Upstream PR #34611, @dboslee)
- helm: fix envoy prometheus metrics scraping with servicemonitor (Backport PR #34472, Upstream PR #34448, @mhofstetter)
- lbipam: fix panic when changing the shared key & req. ip annotation (Backport PR #34452, Upstream PR #34236, @mhofstetter)
- policy: Fixed CIDRGroupRef breaking the sanitization (Backport PR #34452, Upstream PR #34076, @chaunceyjiang)
- bgpv1/test: fix route matching in PodIPPoolAdvert test (Backport PR #34452, Upstream PR #34270, @rastislavs)
- Fix: push PR changes when renovate build images under the workflow_call context (Backport PR #34831, Upstream PR #34650, @Artyop)
- clustermesh/endpointslicesync: fix panic on failure in Test_meshEndpointSlice_Reconcile (Backport PR #34831, Upstream PR #34699, @tklauser)
- fix: base image update workflow will now be triggered on renovate branches with a workflow_call event type (Backport PR #34452, Upstream PR #34372, @Artyop)
- images: fix path script (Backport PR #34768, Upstream PR #34764, @aanm)
- Fix panic in endpoint regeneration when DNS requests are processed during early initialization. (cilium/cilium#34892, @joamaki)

### 1.16.3

- bgpv2: fix reconciliation of services with shared VIPs (Backport PR #35274, Upstream PR #35166, @rastislavs)
- bgpv2: Fix service reconciliation logic to update service advertisement metadata only after successful reconciliation (Backport PR #35036, Upstream PR #34976, @rastislavs)
- bugtool: fix cilium-health command (Backport PR #35274, Upstream PR #35068, @ayuspin)
- Fix a low-probability issue where the DNS proxy could occasionally drop DNS queries due to "duplicate request id" errors. (Backport PR #35036, Upstream PR #34941, @bimmlerd)
- Fix issue where bpf packet buffer mark would in some cases set incorrect mark value resulting in incorrectly SNATed traffic. (Backport PR #35036, Upstream PR #34789, @tommyp1ckles)
- Fix parameter check to forbid IPAM ENI with TUNNEL routing, and prevent agent segfault when also IPSec is enabled. (Backport PR #34918, Upstream PR #34651, @smagnani96)
- Fixed bug in LB-IPAM where restarting the operator would unshare previously shared IPs between services (Backport PR #35036, Upstream PR #34783, @dylandreimerink)
- Fixed bug in tracking policy changes that could have resulted in revert not woking in failure cases as expected. (Backport PR #35274, Upstream PR #35109, @jrajahalme)
- Fixed bug where service id allocator would loop infinity when out of service ids (Backport PR #35274, Upstream PR #35033, @WeeNews)
- Fixes startup fatal error when updating CiliumNode resource. (Backport PR #34918, Upstream PR #34862, @harsimran-pabla)
- ipcache: Yet another refcounting fix with mix of APIs (Backport PR #35036, Upstream PR #34715, @gandro)
- wireguard: Fix issue where updates to a WireGuard device's configuration caused connectivity blips. (Backport PR #35115, Upstream PR #34612, @jrife)
- github/lint-build-commits: fix workflow for push events (Backport PR #35274, Upstream PR #35264, @aanm)
- [v1.16] gha: fix incorrect go version in lint-build-commits workflow (cilium/cilium#35312, @giorio94)
- fix: repository nil value handled on workflow_dispatch context for renovate updates (Backport PR #34918, Upstream PR #34902, @Artyop)
- github: fix build image process to commit changes (Backport PR #35274, Upstream PR #35262, @aanm)
- github: fix lvh-kind warnings (Backport PR #35157, Upstream PR #34811, @aanm)
- github: fix runtime image digests (Backport PR #35274, Upstream PR #35107, @aanm)
- fix: Assign PodStore from Pod resource until cell migration is completed (Backport PR #35274, Upstream PR #34090, @dlapcevic)
- install/kubernetes: fix Operator's clusterrole for pods deletion (Backport PR #35274, Upstream PR #35193, @aanm)
- [v1.16] author backport: fix ENABLE_LOCAL_REDIRECT_POLICY (cilium/cilium#35129, @ysksuzuki)
- [v1.16] author backport: LRP fixes (cilium/cilium#35072, @ysksuzuki)

### 1.16.4

- netkit: Fix issue where traffic originating from the host namespace fails to reach the pod when using endpoint routes and network policies. (Backport PR #35543, Upstream PR #35306, @jrife)
- Avoid duplicate errors in health status for node-neighbor-link-updater (Backport PR #35468, Upstream PR #35179, @wedaly)
- bgpv1: fix reconciliation of services with shared VIPs (Backport PR #35468, Upstream PR #35333, @rastislavs)
- bgpv2,operator: Fix the race condition in the nodeSelector conflict detection logic (Backport PR #35863, Upstream PR #35690, @YutaroHayakawa)
- Fix missing flowlabel hash on SRv6 traffic. (Backport PR #35781, Upstream PR #35498, @akaliwod)
- Fix packet drops for pod-to-pod connections that pass through ingress & egress proxy when using IPsec, caused by MTU misconfiguration. (Backport PR #35543, Upstream PR #35173, @smagnani96)
- Fix possible disruption of long running pod to node traffic on agent restart in kvstore mode (Backport PR #35781, Upstream PR #35673, @giorio94)
- Fix redirect from L3 device to remote endpoint via overlay network. (Backport PR #35468, Upstream PR #35165, @julianwiedmann)
- Fixed a bug where replies for pod-originating connections came into scope of HostFW Ingress Network policy. Applicable to configurations that use iptables for Masquerading. (Backport PR #35908, Upstream PR #35694, @julianwiedmann)
- Fixes a bug where the operator incorrectly flagged CiliumNetworkPolicies containing ICMP rules as invalid. (Backport PR #35781, Upstream PR #35599, @squeed)
- Fixes a performance regression when ingesting network policies in clusters with large numbers of Services. (Backport PR #35543, Upstream PR #35293, @squeed)
- Fixes a potential deadlock when restarting cilium agent with pods with DNS interception configured (Backport PR #35906, Upstream PR #35890, @squeed)
- Fixes BPF Masquerading exclusion CIDR for IPAM modes "eni", "azure" and "alibabacloud". (cilium/cilium#35611, @pippolo84)
- helm: Fix configmap unmarshal error on egressGateway.maxPolicyEntries (Backport PR #35319, Upstream PR #35301, @hox)
- helm: fix duplicate configmap key for `bpf-lb-sock-terminate-pod-connections` (Backport PR #35781, Upstream PR #35703, @solidDoWant)
- hubble: fix endpoint cluster name (Backport PR #35781, Upstream PR #35415, @kaworu)
- l7lb: fix registration of flag loadbalancer-l7 (Backport PR #35781, Upstream PR #35623, @mhofstetter)
- wireguard: Fix connectivity issues following node reboots. (Backport PR #35908, Upstream PR #35750, @jrife)
- dnsproxy: fix error when sessionUDPFactory fails (Backport PR #35543, Upstream PR #33998, @marseel)
- docs/xfrm: Fix incorrect statement regarding XFRM IN policies (Backport PR #35781, Upstream PR #35626, @pchaigno)
- Fix wrongly spelled config option in error message (Backport PR #35543, Upstream PR #35390, @baurmatt)
- [v1.16] policy/correlation: Fix `PolicyMatch{L3Proto,L4Only}` case (cilium/cilium#35681, @gandro)

### 1.16.5

- bgp: fix race in bgp stores (Backport PR cilium/cilium#36066, Upstream PR cilium/cilium#35971, @harsimran-pabla)
- BGPv1: Fix race by reconciliation of services with externalTrafficPolicy=Local by populating locally available services after performing service diff (Backport PR cilium/cilium#36286, Upstream PR cilium/cilium#36230, @rastislavs)
- BGPv2: Fix race by reconciliation of services with externalTrafficPolicy=Local by populating locally available services after performing service diff (Backport PR cilium/cilium#36286, Upstream PR cilium/cilium#36165, @rastislavs)
- Fix an issue where pod-to-world traffic goes up stack when BPF host routing is enabled with tunnel. (Backport PR cilium/cilium#35861, Upstream PR cilium/cilium#35098, @jschwinger233)
- Fix identity leak for kvstore identity mode (Backport PR cilium/cilium#36066, Upstream PR cilium/cilium#34893, @odinuge)
- Fix potential Cilium agent panic during endpoint restoration, occurring if the corresponding pod gets deleted while the agent is restarting. This regression only affects Cilium v1.16.4. (Backport PR cilium/cilium#36302, Upstream PR cilium/cilium#36292, @giorio94)
- gateway-api: Fix gateway checks for namespace (Backport PR cilium/cilium#36462, Upstream PR cilium/cilium#35452, @sayboras)
- iptables: Fix data race in iptables manager (Backport PR cilium/cilium#36066, Upstream PR cilium/cilium#35902, @pippolo84)
- policy: Fix bug that allowed port ranges to be attached to L7 policies, which is not permitted. (cilium/cilium#36050, @nathanjsweet)
- Fixed BGP documentation (Backport PR cilium/cilium#36066, Upstream PR cilium/cilium#35953, @seadog007)
- lrp: fix kernel version requirement in warning log (Backport PR cilium/cilium#36286, Upstream PR cilium/cilium#36141, @ysksuzuki)
- [v1.16] cilium, service: Fix checkLBSrcRange propagation to LB map (cilium/cilium#36511, @borkmann)

### 1.16.6

- cilium: LB source ranges fixes (Backport PR cilium/cilium#36635, Upstream PR cilium/cilium#36517, @borkmann)
- Fix connectivity issue caused by stale cilium eBPF program when using --bpf-filter-priority (Backport PR cilium/cilium#36635, Upstream PR cilium/cilium#36176, @tamilmani1989)
- pkg/redirectpolicy: Fix backend slices in processConfig (Backport PR cilium/cilium#36872, Upstream PR cilium/cilium#35496, @Sm0ckingBird)
- gha: fix merging of features-related artifacts (cilium/cilium#36665, @giorio94)
- github: fix conformance-k8s NP test (Backport PR cilium/cilium#36263, Upstream PR cilium/cilium#36355, @aanm)
- Fix `make -C Documentation update-cmdref` when make uses `--jobserver-style=fifo`. (Backport PR cilium/cilium#36872, Upstream PR cilium/cilium#36788, @gentoo-root)

### 1.16.7

- ces: Fix bug where stale endpoint information was injected into IPCache (Backport PR cilium/cilium#37417, Upstream PR cilium/cilium#37347, @gandro)
- Fix a bug that prevents a pod from accessing Nodeport services when the pod is also in scope of a broad-range Egress Gateway policy. (Backport PR cilium/cilium#37168, Upstream PR cilium/cilium#36929, @julianwiedmann)
- Fix bug causing the endpoint regeneration failure handler to be effective only once (Backport PR cilium/cilium#37278, Upstream PR cilium/cilium#37085, @giorio94)
- Fix bug potentially causing newly added endpoints to remain stuck in waiting-to-regenerate state forever, causing traffic from/to that endpoint to be incorrectly dropped. (Backport PR cilium/cilium#37168, Upstream PR cilium/cilium#37086, @giorio94)
- Fix specifying multiple interfaces for egress masquerade with enable-masquerade-to-route-source=false (Backport PR cilium/cilium#37168, Upstream PR cilium/cilium#36103, @viktor-kurchenko)
- socket-lb: Fix null pointer dereference in socketlb/cgroup.go (Backport PR cilium/cilium#37441, Upstream PR cilium/cilium#37426, @alvaroaleman)
- gha: fix retrieval of DNS server in conformance external workloads (Backport PR cilium/cilium#37375, Upstream PR cilium/cilium#37361, @giorio94)
- renovate: add fix grpc-go autodetection (Backport PR cilium/cilium#37278, Upstream PR cilium/cilium#33570, @aanm)

### 1.16.8

- Fix creation and deletion of host port maps that would occasionally leave pods without them (Backport PR cilium/cilium#37900, Upstream PR cilium/cilium#37419, @javanthropus)
- Fix envoy metrics could not be obtained on IPv6-only clusters (Backport PR cilium/cilium#37900, Upstream PR cilium/cilium#37818, @haozhangami)
- Fix the `--dns-policy-unload-on-shutdown` feature for restored endpoints (Backport PR cilium/cilium#37647, Upstream PR cilium/cilium#37532, @antonipp)
- fix: cilium-config configmap was incorrectly resulting in values like `2.09715…2e+06` instead of `2097152` (Backport PR cilium/cilium#37647, Upstream PR cilium/cilium#37236, @dee-kryvenko)
- Fix: cilium-operator no longer patches services on shutdown (Backport PR cilium/cilium#38106, Upstream PR cilium/cilium#37967, @rsafonseca)
- helm: fix large number handling (Backport PR cilium/cilium#37743, Upstream PR cilium/cilium#37670, @justin0u0)
- identity: fix bug where fromNodes/toNodes could be used to allow custom endpoint (Backport PR cilium/cilium#38014, Upstream PR cilium/cilium#36657, @oblazek)
- Fix API generation and add trusted dependencies to renovate config (Backport PR cilium/cilium#37647, Upstream PR cilium/cilium#36957, @aanm)
- Fix helm value for IPAM Multi-Pool (Backport PR cilium/cilium#38014, Upstream PR cilium/cilium#37963, @saintdle)
- labels: fix TestNewFrom test (Backport PR cilium/cilium#37900, Upstream PR cilium/cilium#37846, @giorio94)

### 1.16.9

- Fix panic caused in dual cluster setups where LRPs with `skipRedirectFromBackend` flag set to true are installed and IPv6 is disabled. (Backport PR cilium/cilium#38701, Upstream PR cilium/cilium#38656, @aditighag)
- Fix checked L4 port for UDP IPv6 packets in check-encryption-leak script. (Backport PR cilium/cilium#38521, Upstream PR cilium/cilium#38265, @smagnani96)
- Fix endianness for WireGuard UDP traffic in the check-encryption-leak script. (Backport PR cilium/cilium#38521, Upstream PR cilium/cilium#38292, @smagnani96)
- Fix erroneous TCP RST condition when no TCP packets in the check-encryption-leak script. (Backport PR cilium/cilium#38521, Upstream PR cilium/cilium#38291, @smagnani96)
- Documentation: fix mentions of per-node `cilium-dbg` tool (Backport PR cilium/cilium#38299, Upstream PR cilium/cilium#38276, @tklauser)
- pkg/controller: fix data race in update params locked (Backport PR cilium/cilium#38525, Upstream PR cilium/cilium#38327, @aanm)
- pkg/endpoint: fix race in unit test (Backport PR cilium/cilium#38299, Upstream PR cilium/cilium#38129, @squeed)
- [v1.16] hubble: fix flowfilter flag parsing allowing only one filter (cilium/cilium#38794, @devodev)
- fix AWS ENI IPAM mode performance regression in the Operator when `--update-ec2-adapter-limit-via-api` is set to `true` (cilium/cilium#38533, @antonipp)

### 1.16.10

- Fix a bug where a `CiliumNetworkPolicy`/`CiliumClusterwideNetworkPolicy` containing invalid rules would not be reported with invalid status. (Backport PR cilium/cilium#38949, Upstream PR cilium/cilium#38801, @tklauser)
- Fix a deadlock when a host has no IPv4 address. (Backport PR cilium/cilium#39077, Upstream PR cilium/cilium#38938, @EmilyShepherd)
- Fix a panic happening in the ipset reconciler when a previous reconciliation failed. (Backport PR cilium/cilium#38949, Upstream PR cilium/cilium#38890, @pippolo84)
- Fix bug that would cause the `cilium-dbg encrypt status` command to not list any decryption interfaces when KPR is enabled. (Backport PR cilium/cilium#39215, Upstream PR cilium/cilium#39170, @pchaigno)
- Fixes a bug where layer-7 rules would override enableDefaultDeny: false, incorrectly dropping traffic. (Backport PR cilium/cilium#39382, Upstream PR cilium/cilium#38841, @nimishamehta5)
- ipsec: Fix key derivation error in case of corrupted boot IDs (Backport PR cilium/cilium#39077, Upstream PR cilium/cilium#39059, @pchaigno)
- k8s: Fixed a case when delete event for service endpointslices might have been missed if connectivity to k8s apiserver was broken causing stale service cache for service. (Backport PR cilium/cilium#38949, Upstream PR cilium/cilium#38779, @marseel)
- bpf: tests: fix ethertype when building inner headers of VXLAN packet (Backport PR cilium/cilium#39077, Upstream PR cilium/cilium#39060, @julianwiedmann)
- cilium: Fix device controller's dependency on netfilter (Backport PR cilium/cilium#38949, Upstream PR cilium/cilium#38777, @borkmann)
- contrib/scripts: Fix IndexError in stacktrace script (Backport PR cilium/cilium#39215, Upstream PR cilium/cilium#39101, @christarazi)
- documentation: fix get deployment cmd (Backport PR cilium/cilium#39215, Upstream PR cilium/cilium#39155, @g0gn)
- maglev: Fix division by zero upon table recreation (Backport PR cilium/cilium#39077, Upstream PR cilium/cilium#38659, @borkmann)

### 1.16.11

- Fixed bug where datapath is unable to compile when active connection tracking and IPv6 are enabled at the same time. (Backport PR cilium/cilium#39563, Upstream PR cilium/cilium#39509, @dylandreimerink)
- bpf: test: fix up mis-spelled HAVE_NETNS_COOKIE (Backport PR cilium/cilium#39563, Upstream PR cilium/cilium#39420, @julianwiedmann)

### 1.16.12

- Fix CIDRGroupRef handling in cilium network policy rule spec. (cilium/cilium#40139, @fristonio)
- LBIPAM: Fix deletion of CiliumLoadBalancerIPPool with multiple IP blocks that led to an operator crash (Backport PR cilium/cilium#40093, Upstream PR cilium/cilium#40013, @pippolo84)
- Backported setting egressMasqueradeInterfaces and concurrent test runs to fix ci-eks workflow. (cilium/cilium#40468, @jrajahalme)
- docs/ipsec: Fix incorrect statement on hostns encryption (Backport PR cilium/cilium#40173, Upstream PR cilium/cilium#40133, @pchaigno)

### 1.16.13

- bgp: Use private fork of the GoBGP to fix BGP MD5 auth (Backport PR cilium/cilium#40579, Upstream PR cilium/cilium#40566, @YutaroHayakawa)
- install/kubernetes: fix clustermesh-apiserver extraEnv (Backport PR cilium/cilium#41073, Upstream PR cilium/cilium#41021, @aanm)
- Fix GKE cluster creation failures when branch names exceed 63-byte label limit by implementing automatic truncation with hash-based uniqueness preservation. (Backport PR cilium/cilium#40851, Upstream PR cilium/cilium#40725, @pillai-ashwin)
- spire: Fix unreliable test (Backport PR cilium/cilium#40663, Upstream PR cilium/cilium#40561, @joestringer)
- github: fix removal of all files in /mnt (Backport PR cilium/cilium#40851, Upstream PR cilium/cilium#40818, @aanm)
- github: fix upload artifacts for features.json (cilium/cilium#41089, @aanm)

### 1.16.15

- github: fix upload artifacts for features.json (Backport PR cilium/cilium#41372, Upstream PR cilium/cilium#41119, @aanm)
- Fix release script steps (Backport PR cilium/cilium#41179, Upstream PR cilium/cilium#41502, @aanm)
- Fix a bug that caused the kernel verifier on pre-v5.7 kernels to reject the bpf_sock program with "invalid func unknown#122" when the LocalRedirectPolicy feature is enabled. (cilium/cilium#41457, @julianwiedmann)

### 1.16.16

- bpf:tests:egressgw: fix metrics count (Backport PR cilium/cilium#41824, Upstream PR cilium/cilium#40338, @smagnani96)
- operator/pkg/lbipam: fix LoadBalancerIPPool conditions update logic (Backport PR cilium/cilium#41830, Upstream PR cilium/cilium#41322, @alimehrabikoshki)
- xds: Fix a case in which after cilium-agent we were not sending updated resources to Envoy (Backport PR cilium/cilium#41993, Upstream PR cilium/cilium#38654, @marseel)
- workflows: fix GCP OIDC authentication's project ID (cilium/cilium#42175, @nbusseneau)
- [v1.16] bpf:tests:egressgw: fix metrics count (part 2) (cilium/cilium#42207, @julianwiedmann)
- gh: ipsec-upgrade: fix patch-level upgrade from v1.16.14 (cilium/cilium#41776, @julianwiedmann)

### 1.16.17

- Fix cilium_operator_lbipam_conflicting_pools metric to report correct value. (Backport PR cilium/cilium#42321, Upstream PR cilium/cilium#41999, @hanapedia)
- gh: ginkgo: fix focus for service hairpin test (Backport PR cilium/cilium#42650, Upstream PR cilium/cilium#42633, @julianwiedmann)
- fix: run post-release and publish-helm workflows on cilium org (Backport PR cilium/cilium#42321, Upstream PR cilium/cilium#42279, @sekhar-isovalent)
- Stop tracking selectorPolicy in endpoint to fix policy deadlock referencing the the old identity after an identity change (cilium/cilium#42418, @odinuge)

### 1.16.18

- AWS EC2: Fix ENI attachment on multi-network card instances with high-performance networking (EFA) setups (Backport PR cilium/cilium#42746, Upstream PR cilium/cilium#42512, @41ks)
- Fix a bug that would cause IPsec logs to incorrectly report the XFRM rules being processed as "Ingress" rules. (Backport PR cilium/cilium#42826, Upstream PR cilium/cilium#42640, @sjohnsonpal)
- Fix bug that could cause the agent to fail to add XFRM states when IPsec is enabled, thus preventing a proper startup. (Backport PR cilium/cilium#42951, Upstream PR cilium/cilium#42666, @pchaigno)
- policy: Fix Endpoint Selector Policy Deadlock (Backport PR cilium/cilium#43082, Upstream PR cilium/cilium#38139, @nathanjsweet)
- policy: Fix rare bug that prevented two endpoints that shared the same identity from being simultaneously updated. (Backport PR cilium/cilium#43082, Upstream PR cilium/cilium#37910, @nathanjsweet)
- policy: Fix rare Endpoint Selector Policy Deadlock causing policies to not be updated with new identities (Backport PR cilium/cilium#43082, Upstream PR cilium/cilium#42306, @odinuge)
- bpf: test: egressgw: fix up ENABLE_MASQUERADE (Backport PR cilium/cilium#42972, Upstream PR cilium/cilium#42912, @julianwiedmann)
- gh: conn-disrupt: fix XFRM error checks (Backport PR cilium/cilium#42777, Upstream PR cilium/cilium#42724, @julianwiedmann)
- gh: ipsec-e2e: fix flaky connection disruptivity test (Backport PR cilium/cilium#42851, Upstream PR cilium/cilium#42780, @julianwiedmann)
- [v1.16] ci: fix nodegroups volume size (cilium/cilium#43051, @Artyop)

### 1.16.19

- ipcache: Fix leak in CIDR metadata consolidation logic (Backport PR cilium/cilium#43427, Upstream PR cilium/cilium#43074, @christarazi)
- xds: fix nil-pointer in `processRequestStream` (Backport PR cilium/cilium#43614, Upstream PR cilium/cilium#43609, @mhofstetter)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.16.19**, the newest release recorded here for this line.

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
