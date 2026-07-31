---
id: TROUBLE-CILIUM_1_13_DEFECTS
type: troubleshooting
title: "cilium 1.13: defects fixed in the 1.13 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.13.0 <1.14.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.13 known issues
  - cilium 1.13 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.13 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.13: defects fixed in the 1.13 line

## Summary

**201 defects** the project fixed across **19 releases** of the 1.13 line, from 1.13.0 to
1.13.18. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.13.0

- bpf/tests: fix redundant usage of variable offset (#22390, @sahid)
- bpf: nat: fix usage of ipv6_hdrlen() with unhandled Extension headers (#22544, @julianwiedmann)
- Fix behavior where packets leave node if there are no backends (#21539, @michaelasp)
- Fix crash of CES queue delay metric when CESTracker is nil (Backport PR #23147, Upstream PR #22884, @dlapcevic)
- fix empty message when tunnel and socketLB service missing in switch case (#21314, @vincentmli)
- fqdn/metrics: Fix ProxyUpstreamTime error=timeout (#20752, @joestringer)

### 1.13.1

- [EKS] Fix deadlock causing network connectivity outages when kube-apiservers scale down (Backport PR #23956, Upstream PR #23836, @christarazi)
- agent: fix incorrect deletion of veth host interfaces on bootstrap (Backport PR #23956, Upstream PR #23787, @giorio94)
- Avoid k8s CiliumNode initialization problems when Cilium connects to the KVStore (Backport PR #24200, Upstream PR #24156, @aanm)
- bpf: Fix broken remote-node identity classification (Backport PR #23956, Upstream PR #23091, @ysksuzuki)
- clustermesh: fix cluster synchronization wait group increment (Backport PR #24058, Upstream PR #23741, @giorio94)
- clustermesh: fix services cache bloat due to incorrect deletion (Backport PR #24058, Upstream PR #23947, @giorio94)
- Fix bug that would prevent IPsec from working with GENEVE encapsulation. (Backport PR #24200, Upstream PR #24116, @borkmann)
- Fix bug that would prevent SRv6 decapsulation when BPF Host Routing was disabled. (Backport PR #23834, Upstream PR #23825, @ldelossa)
- Fix connectivity issue upon agent restart in case of ipv6 + direct routing + KPR replacement (Backport PR #23956, Upstream PR #23857, @giorio94)
- Fix enable-stale-cilium-endpoint-cleanup flag not actually disabling the cleanup init set when set to false. This provides a workaround for an existing panic that can occur when running using etcd kvstore. (Backport PR #24311, Upstream PR #23874, @sjdot)
- Fix incorrectly dropping in-cluster traffic for L7 ingress resources (Backport PR #24200, Upstream PR #23984, @sayboras)
- Fix memory leak caused on clustermesh reconnect. (Backport PR #24086, Upstream PR #23785, @oblazek)
- Fix operator crash race condition for CES identity map concurrent read/write (Backport PR #24086, Upstream PR #23605, @dlapcevic)
- Fix restoreServicesLocked() potential nil pointer panic (Backport PR #23834, Upstream PR #23446, @dlapcevic)
- fix(helm): add missing updateStrategy to hubble-ui deployment (Backport PR #24058, Upstream PR #23975, @mhulscher)
- Fixes a bug where the Helm value `cni.configMap` no longer worked. (Backport PR #23834, Upstream PR #23743, @squeed)
- Fixes a memory leak and (possible) source of stale data for Clustermesh whenever the connection to the remote cluster is disrupted or restarted. (Backport PR #23834, Upstream PR #23532, @squeed)
- helm: Fix duplicate `enable-envoy-config` flag when enabling L7LB, Ingress Controller, or GatewayAPI simultaneously (Backport PR #23956, Upstream PR #23866, @DWSR)
- Hubble Relay: fix reported uptime (Backport PR #24058, Upstream PR #23966, @rolinh)
- ipam/crd: Fix panic due to concurrent map read and map write (Backport PR #23834, Upstream PR #23713, @gandro)
- bpf: Fix usage of tunnel map structs (Backport PR #24086, Upstream PR #23469, @pchaigno)
- Fixed broken/deprecated links (Backport PR #24058, Upstream PR #23920, @PhilipSchmid)
- Fixed link to broken anchor in RKE doc (Backport PR #23834, Upstream PR #23706, @raphink)
- Fixes a flake in the kubectl wait part of the CI (Backport PR #23834, Upstream PR #23733, @meyskens)
- workflow: fixes LLVM, Clang cache and install path (Backport PR #23834, Upstream PR #23740, @brlbil)
- v1.13 backport: fix cgroup program detachment and 1.14 downgrade (#24184, @ti-mo)

### 1.13.2

- bpf: dsr: fix parsing of IPv6 AUTH extension header (Backport PR #24821, Upstream PR #24792, @julianwiedmann)
- bpf: fix ipv6 extension header parsing error (Backport PR #24706, Upstream PR #24309, @chenyuezhou)
- bpf: policy: fix handling of ICMPv6 packet with extension headers (Backport PR #24821, Upstream PR #24797, @julianwiedmann)
- endpoint: fix k8sNamespace log field when ep gets deleted (Backport PR #24706, Upstream PR #24575, @mhofstetter)
- Fix a bug where users are unable to change a wrong remote etcd configuration (Backport PR #24547, Upstream PR #24046, @oblazek)
- Fix a memory leak in the service cache, and possible missed service updates on scale to zero events in rare circumstances (Backport PR #24706, Upstream PR #24619, @giorio94)
- Fix bug in BGP CP where changing the route-id of an existing router would cause announcements to disappear (Backport PR #24547, Upstream PR #24304, @dylandreimerink)
- Fix bug where ingress policies for remote-note identities are not applied correctly new nodes join the cluster, specifically when the nodes joining the cluster had IP addresses specified in CIDR policies (Backport PR #24547, Upstream PR #23764, @christarazi)
- Fix Cilium Operator from crashing when encountering empty node pools on Azure (Backport PR #24547, Upstream PR #24189, @forgems)
- Fix for disabled cloud provider rate limiting (Backport PR #24547, Upstream PR #24413, @hemanthmalla)
- Fix missing delete events on informer re-lists to ensure all delete events are correctly emitted and using the latest known object state, so that all event handlers and stores always reflect the actual apiserver state as best as possible (#24870, @aanm)
- Fixed bug where L7 rules would be incorrectly merged between rules for the same (remote) endpoint. This bug could have caused L7 rules to be bypassed via a wildcard header rule being improperly appended to the set of HTTP rules when both a policy with HTTP header rules applying to multiple endpoints and an allow-all rule for only one of those endpoints are specified. (Backport PR #24843, Upstream PR #24788, @jrajahalme)
- Prevent egress gateway from adding and then immediately removing BPF policy entries for policies that don't match any gateway node (Backport PR #24706, Upstream PR #24646, @MrFreezeex)
- bpf/tests: fix mac addresses definitions in egressgw test (Backport PR #24607, Upstream PR #23351, @jibi)
- datapath/linux/route: fix CI expectations for rule string format (Backport PR #24607, Upstream PR #24577, @NikAleksandrov)
- Fix race conditions when deleting CNP / CCNP in e2e tests (Backport PR #24706, Upstream PR #24484, @jschwinger233)
- Fixed flake in the `TestRequestIPWithMismatchedLabel` LB-IPAM tests. (Backport PR #24547, Upstream PR #23297, @dylandreimerink)
- renovate: Fix Hubble release digest regex (Backport PR #24547, Upstream PR #24477, @gandro)
- Avoid clearing objects in CiliumEndpoint conversion funcs (Backport PR #24929, Upstream PR #24928, @aanm)
- Avoid clearing objects in conversion funcs (Backport PR #24929, Upstream PR #24241, @odinuge)
- checker: Fix incorrect checker for ExportedEqual() (Backport PR #24547, Upstream PR #24373, @christarazi)
- Fix duplicated logs for test-output.log (Backport PR #24547, Upstream PR #24171, @romanspb80)
- Fixed BPF tests which would fail on older kernels (<=5.8) due to unsupported program loading (Backport PR #24607, Upstream PR #22980, @dylandreimerink)
- helm: fix poststart-eni.bash execution in agent DS (#24789, @nebril)

### 1.13.3

- cmd/cleanup: Fix cleanup of generic XDP programs (Backport PR #25184, Upstream PR #25117, @pchaigno)
- datapath: Fix double SNAT (Backport PR #25223, Upstream PR #25189, @brb)
- Fix a regression in which link-local addresses were not treated with the "host" identity in some circumstances. (Backport PR #25368, Upstream PR #25298, @asauber)
- Fix broken IPv4 connectivity from outside to NodePort service when using L7 ingress policy, by removing PROXY_RT route table. (Backport PR #25086, Upstream PR #24807, @jschwinger233)
- Fix bug that caused ToCIDR netpols matching kube-apiserver IPs (when external to the cluster) to not reliably allow connectivity. (#25241, @giorio94)
- Fix bug that causes enforcement of host policies on reply IPv6 pod traffic. (Backport PR #25137, Upstream PR #25024, @pchaigno)
- Fix bug where Cilium configurations running with tunneling disabled, BPF-masq disabled, but with masquerading enabled, do not clean up ipset configuration when a node IP changes. This can lead to a lack of masquerading on those node IPs. (Backport PR #25013, Upstream PR #24825, @christarazi)
- Fix connectivity issue if nodes share the same name across the clustermesh and wireguard is enabled (Backport PR #25013, Upstream PR #24785, @giorio94)
- Fix data race affecting the preferred mark in backends, e.g. backends selected by service with affinity set to local. In very rare cases a backend might be missing its preferred status and a non-local backend might be selected. (Backport PR #25346, Upstream PR #25087, @joamaki)
- Fix incorrect network policy ebpf setup that may lead to incorrect packets denies when CEP is present in multiple CES (Backport PR #25184, Upstream PR #24838, @alan-kut)
- Fix operator shutdown hanging when kvstore is enabled (Backport PR #25223, Upstream PR #24979, @giorio94)
- Fix operator startup delay caused by leader election lease not being released correctly (Backport PR #25137, Upstream PR #24978, @giorio94)
- Fix panic due to assignment to nil BGP service announcements map. (Backport PR #25013, Upstream PR #24985, @harsimran-pabla)
- Fix permission issue when copying cni plugins onto host path (Backport PR #25346, Upstream PR #24891, @JohnJAS)
- Fix security-group-tags not working in ENI (Backport PR #25013, Upstream PR #24951, @aanm)
- Fix spurious errors containing "Failed to map node IP address to allocated ID". (Backport PR #25346, Upstream PR #25222, @bimmlerd)
- Fix syncing of relevant node annotations into CiliumNode (Backport PR #25368, Upstream PR #25307, @meyskens)
- Fix the bug when long-living connections using egress gateway may be reset. (Backport PR #25346, Upstream PR #24905, @gentoo-root)
- pkg/kvstore: Fix for deadlock in etcd status checker (Backport PR #25013, Upstream PR #24786, @hemanthmalla)
- inctimer: fix test flake where timer does not fire within time. (Backport PR #25346, Upstream PR #25219, @tommyp1ckles)
- jenkinsfiles: Fix order of ginkgo tests (Backport PR #25137, Upstream PR #25002, @pchaigno)
- Fix missed clustermesh config change race condition with back-to-back changes (Backport PR #25013, Upstream PR #24993, @giorio94)
- Fix possible panic in the ipcache when removing the prefix labels for an unknown resource ID (Backport PR #25346, Upstream PR #25230, @giorio94)
- Fixed documentation regarding cilium versioning scheme and support (Backport PR #25223, Upstream PR #25171, @ayesha-kr)
- pkg/service: Backends leak follow ups with revised fixes, debugging improvements and unit tests (Backport PR #25223, Upstream PR #24770, @aditighag)
- [v1.13] contrib/backporting: Fix main branch reference (#25091, @joestringer)

### 1.13.4

- CPU overhead regression introduced in v1.13 is fixed. (#25548, @jrajahalme)
- Fix a bug due to which we would leak Linux XFRM policies, potentially leading to increased CPU consumption, when IPsec is enabled with Azure or ENI IPAM. (Backport PR #25897, Upstream PR #25784, @pchaigno)
- Fix a bug that would cause connectivity drops of type XfrmInNoStates on upgrade when IPsec is enabled with ENI or Azure IPAM mode. (Backport PR #25897, Upstream PR #25724, @pchaigno)
- Fix a bug that would cause connectivity drops of type XfrmOutPolBlock on upgrade when IPsec is enabled. (Backport PR #25897, Upstream PR #25735, @pchaigno)
- Fix a possible deadlock when using WireGuard transparent encryption. (Backport PR #25923, Upstream PR #25419, @bimmlerd)
- Fix bug affecting EKS installations with IPsec encryption enabled, where Cilium wouldn't attach its IPsec BPF program to new ENI interfaces, resulting in connectivity loss between pods on remote nodes. (Backport PR #25897, Upstream PR #25744, @joamaki)
- Fix downgrade path from 1.14 to 1.13 due to stale IPAM-allocated IPv6 on cilium_host (#25962, @jschwinger233)
- Fix false error log message when IPsec is enabled with IPAM modes ENI or Azure and a remote node is deleted. (Backport PR #26160, Upstream PR #26093, @pchaigno)
- Fix incorrect hubble flow data when HTTP requests contain an `x-forwarded-for` header by adding an explicit `use_remote_address: true` config to Envoy HTTP configuration to always use the actual remote address of the incoming connection rather than the value of `x-forwarded-for` header, which may originate from an untrusted source. This change has no effect on Cilium policy enforcement where the source security identity is always resolved before HTTP headers are parsed. Previous Cilium behavior of not adding `x-forwarded-for` headers is retained via an explicit `skip_xff_append: true` config setting, except for Cilium Ingress where the source IP address is now appended to `x-forwarded-for` header. (Backport PR #25731, Upstream PR #25674, @jrajahalme)
- Fix leak of IPsec XFRM FWD policies in IPAM modes `cluster-pool`, `kubernetes`, and `crd` when nodes are deleted. Fix incorrect catch-all default-drop XFRM OUT policy for IPsec IPv6 traffic that could lead to leaking plain-text IPv6 traffic if combined with some other bug. (Backport PR #26079, Upstream PR #25953, @pchaigno)
- Fix missing drop notifications on conntrack lookup failures when IPv4 and IPv6 are both enabled or socket-level load balancing is disabled. (Backport PR #25588, Upstream PR #25426, @bleggett)
- Fix RevSNAT for ICMPv6 packets. (Backport PR #25503, Upstream PR #25306, @julianwiedmann)
- Fix three issues in the bug fix to attach IPsec BPF programs to ENI interfaces: do not fatal if loading unexpectedly fails (which may happen if the device is suddenly deleted), ignore veth device changes in order not to reinitialize when new endpoints appear and wait 1 second for further device state changes between reinitializations. (Backport PR #25977, Upstream PR #25936, @joamaki)
- Fixed Cilium agent crash when policy refers to a non-existing Envoy listener. (Backport PR #26079, Upstream PR #25969, @jrajahalme)
- ipsec: Fix cleanup of XFRM states and policies (Backport PR #26079, Upstream PR #26072, @pchaigno)

### 1.13.5

- Avoid dropping short packets (that don't have their L3 header in linear data) in the to-netdev and from-host paths. (Backport PR #25739, Upstream PR #25159, @julianwiedmann)
- bpf: ct: fix CT-based packet tracing for IPv6 (Backport PR #26528, Upstream PR #26476, @julianwiedmann)
- bpf: fix error handling for invoke_tailcall_if() (Backport PR #26497, Upstream PR #26118, @julianwiedmann)
- bpf: lxc: fix one missing drop notification in CT lookup tail calls (Backport PR #26421, Upstream PR #26115, @julianwiedmann)
- Fix a bug in the Egress Gateway feature when using the --install-egress-gateway-routes option. Delete stale IP rules after a CiliumEgressGatewayPolicy is updated and selects a different egress network interface. (Backport PR #26947, Upstream PR #26846, @julianwiedmann)
- Fix bug that caused transient IPsec packet drops on upgrades when tunneling is enabled. (Backport PR #26792, Upstream PR #26708, @pchaigno)
- Fix bug where CNI gets installed even if cni.install=false (Backport PR #26421, Upstream PR #26278, @joestringer)
- Fix crash of cilium-agent happening when a remote node without node IP addresses is removed. (Backport PR #26421, Upstream PR #25851, @cyclinder)
- Fix missing metric "cilium_services_events_total" (Backport PR #27036, Upstream PR #26719, @christarazi)
- Fix path asymmetry when using pod-to-pod encryption with IPsec and tunnel mode. (Backport PR #26792, Upstream PR #25440, @pchaigno)
- Fix possible connection drops on agents restart when a service is associated with multiple endpointslices or has backends across multiple clusters (Backport PR #27036, Upstream PR #26912, @giorio94)
- Fix: Return "Content-Type" and "X-Content-Type-Options" headers from Health Check Node Port (Backport PR #26528, Upstream PR #26458, @cezarygerard)
- Fixed proxy redirect policy implementation when any deny rule prevents them. (Backport PR #26749, Upstream PR #26344, @jrajahalme)
- helm: Fix a bug caused by incorrect indentation of the extraEnv parameter for Hubble UI backend (Backport PR #26915, Upstream PR #26797, @toVersus)
- ipsec: Split removeStaleXFRMOnce to fix deprioritization issue (Backport PR #26421, Upstream PR #26113, @jschwinger233)
- docs/upgrading: note that policy bug was fixed in v1.13.3 (#26661, @squeed)
- Fix "make -C Documentation builder-image" (Backport PR #26915, Upstream PR #26874, @michi-covalent)
- metrics: fix missing k8s rest client metrics (#26412, @ysksuzuki)
- v1.13: node: Fix node encryption condition in incorrect backport (#26953, @pchaigno)

### 1.13.6

- Prevent Cilium from running with Delegated IPAM at the same time as Ingress (Backport PR #27239, Upstream PR #26744, @rickysumho)
- Fix a bug that affected the health-check feature in Stand-alone L4LB mode. For certain configurations (eg if both IPv4 and IPv6 support is enabled) health-check traffic would not get IPIP-encapsulated. (Backport PR #27154, Upstream PR #27015, @julianwiedmann)
- Fix a bug that could cause packet drops of type XfrmOutPolBlock when IPsec is enabled and node are recycled. Fix a bug that could cause IPsec-encrypted packets to be sent to the wrong destination node when node churn is high. (Backport PR #27107, Upstream PR #27029, @pchaigno)
- Fix verifier issues in IPv6 BPF tests (Backport PR #27107, Upstream PR #25191, @dylandreimerink)
- bpf: test: Fix the byte order in the IPV4 macro (Backport PR #27107, Upstream PR #25114, @gentoo-root)
- Documentation: fix the broken links/dead links (Backport PR #27154, Upstream PR #26880, @vipul-21)
- Update Service Mesh docs to fix a number of issues (#27333, @youngnick)
- k8s: fix incorrect EndpointSlice API version (#27277, @ysksuzuki)

### 1.13.7

- envoy: fix panic writing accesslog without L7 tags (Backport PR #27651, Upstream PR #27453, @mhofstetter)
- Fix a bug that affected the RevDNAT translation of IPv6 packets with extension headers. (Backport PR #27393, Upstream PR #27312, @julianwiedmann)
- Fix a bug that could cause an incorrect max. sequence number to be reported by `cilium encrypt status` when IPsec is enabled. (Backport PR #27925, Upstream PR #27656, @pchaigno)
- Fix a bug where cilium host IP is not read from k8s node annotations (Backport PR #27651, Upstream PR #27590, @hemanthmalla)
- Fix bug limiting pod-to-pod network performance under high load when tunneling and IPSec are both enabled. (Backport PR #27393, Upstream PR #27168, @learnitall)
- Fix bug that could cause packet drops of type XfrmOutPolBlock while rotating the IPsec key. (Backport PR #27587, Upstream PR #27319, @jrfastab)
- Fix connectivity issues caused by missing conntrack entry when service pod connects to itself via clusterIP. (Backport PR #27998, Upstream PR #27602, @julianwiedmann)
- ingress: fix panic on ingress rule without HTTPIngressRule (Backport PR #27925, Upstream PR #27818, @mhofstetter)
- IPSec fix for race on init resulting in Xfrm*In* errors and dropped packets (Backport PR #28022, Upstream PR #28012, @jrfastab)

### 1.13.8

- bump grpc dependency to 1.56.3 to fix security vulnerability https://github.com/advisories/GHSA-qppj-fm5r-hxr3 (#28528, @aanm)
- envoy: Sync supported resources to fix not found issue (Backport PR #28350, Upstream PR #28272, @sayboras)
- Fix a bug that causes pod-to-pod traffic between nodes to be dropped when IPsec is enabled and kube-proxy installed rules in both iptables-nft and iptables-legacy. (Backport PR #28443, Upstream PR #28258, @pchaigno)
- Fix the trace notification for hairpinned reply traffic, to indicate the correct security identity for the client. (Backport PR #28251, Upstream PR #28133, @julianwiedmann)
- Fixes a bug causing panic when counting IPsec keys number via "cilium encrypt status". (Backport PR #28251, Upstream PR #27996, @jschwinger233)
- ipcache: fix flapping labels in SelectorCache when reserved:host identity has multiple IPs (Backport PR #28416, Upstream PR #28332, @squeed)
- Fix potential nil pointer dereference in SelectorManager implementation (Backport PR #28103, Upstream PR #27805, @learnitall)
- Backport v1.13: FQDN fixes (#28401, @joamaki)
- cocci: fix warnings related to const qualifiers and DROP_MISSED_TAIL_CALL (#28279, @giorio94)

### 1.13.9

- policy: Fixed a bug that incorrectly omitted port-protocol policy rules that omitted the "protocol" field. An omitted "protocol" field now, correctly, is the same as using the "ANY" protocol. (Backport PR #28761, Upstream PR #28703, @nathanjsweet)
- envoy: fix lb backend endpoint calculation (Backport PR #28877, Upstream PR #27923, @mhofstetter)
- Fix CIDR labels computation (Backport PR #28877, Upstream PR #28788, @pippolo84)
- Fix IPsec error logs to always have all information needed to identify the XFRM configuration on which the error happened. (Backport PR #29034, Upstream PR #28642, @pchaigno)
- bpf: lb: fix missing drop reason in reverse_map_l4_port() (Backport PR #29034, Upstream PR #28884, @julianwiedmann)

### 1.13.10

- Avoid missed tail calls due to inserting policy programs too early during endpoint regeneration (#29309, @ti-mo)
- datapath: Fix ENI egress routing table for cilium_host IP (Backport PR #29391, Upstream PR #29335, @gandro)
- Fix bug where deleted nodes would reappear in the cilium_node_connectivity_* metrics (Backport PR #29640, Upstream PR #29566, @christarazi)
- ci-ipsec-upgrade: Fix upgrade/downgrade path and add missed tail calls check to upgrade (Backport PR #29003, Upstream PR #29072, @brb)
- Fix bug preventing endpoint-related debug logs from being emitted (Backport PR #29700, Upstream PR #29495, @learnitall)

### 1.13.11

- Fix and prevent future bugs limiting pod-to-pod network performance under high load when tunneling and IPSec are both enabled. (Backport PR #29997, Upstream PR #29616, @learnitall)
- nodediscovery: Fix bug where CiliumInternalIP was flapping (Backport PR #29974, Upstream PR #29964, @gandro)
- datapath: Fix TestNodeChurnXFRMLeaks (Backport PR #30081, Upstream PR #27274, @brb)
- Fix kind.sh development scripts on MacOS (Backport PR #30010, Upstream PR #25317, @chancez)
- [1.13] loader: fix obsolete XDP program removal (#30231, @rgo3)
- [v1.13] node: Fix IP removal from ipset on node updates (#29898, @qmonnet)
- v1.13: ipam: Fix invalid PodCIDR in CiliumNode in ENI/Azure/MultiPool mode (#30137, @pchaigno)

### 1.13.12

- Fix all packet drops due to missed tail calls, enable zero tolerance for these errors in CI (Backport PR #30315, Upstream PR #30248, @ti-mo)
- Fix nodeinit issue causing NotReady state in Kubernetes nodes when laying down an incorrect CNI config (Backport PR #30522, Upstream PR #30399, @tlcowling)
- [v1.13] backport Go version check fixes in preparation for Go 1.21 update (#30417, @tklauser)
- ci/ipsec: Fix version retrieval for downgrades to closest patch release (Backport PR #30522, Upstream PR #30503, @qmonnet)
- [v1.13] ci/ipsec: Fix downgrade version for release preparation commits (#30715, @qmonnet)
- bpf: l3: fix-up kube-proxy workaround in l3_local_delivery() to bpf_overlay (#30313, @julianwiedmann)

### 1.13.13

- Fixes an L7 proxy issue by re-introducing 2005 route table. (Backport PR #31161, Upstream PR #29530, @jschwinger233)
- Fixes proxy issues by opting out from SNAT for L7 + Tunnel. (Backport PR #31161, Upstream PR #29594, @jschwinger233)
- Fixes proxy issues in egress direction (Backport PR #31161, Upstream PR #30095, @jschwinger233)
- ci/ipsec: Fix downgrade version retrieval (Backport PR #31049, Upstream PR #30742, @qmonnet)
- Fix datapath mode in Network Performance CI test (Backport PR #30865, Upstream PR #30756, @marseel)

### 1.13.14

- Fix a bug where pod label updates are not reflected in endpoint labels in presence of filtered labels. (Backport PR #31476, Upstream PR #31395, @tklauser)
- Fix bug leading to missed ipcache updates for the CiliumInternalIP when `--enable-remote-node-identity=false`, and unnecessary `ipcache_errors_total` metric increase if Cilium operates in kvstore mode. (#31396, @giorio94)
- Hubble: fix traffic direction and is reply when IPSec is enabled (Backport PR #31496, Upstream PR #31211, @kaworu)
- loader: fix issue where errors cancelled compile cause error logs. (Backport PR #31309, Upstream PR #30988, @tommyp1ckles)

### 1.13.15

- cilium-health: Fix broken retry loop in `cilium-health-ep` controller (Backport PR #31722, Upstream PR #31622, @gandro)
- Fixed a race condition in service updates for L7 LB. (Backport PR #31862, Upstream PR #31744, @jrajahalme)
- Fixed issue with assigning 0 nodeID when corresponding bpf map run out of space. Potentially it could have impacted connectivity in large clusters (>4k nodes) with IPSec or Mutual Auth enabled. Otherwise, it was merely generating unnecessary error log messages. (Backport PR #31657, Upstream PR #31380, @marseel)
- controlplane: fix mechanism for ensuring watchers (Backport PR #31587, Upstream PR #31030, @bimmlerd)
- [v1.13] fix aws region being used twice (#31740, @brlbil)
- fqdn: Fix minor restore bug that causes false negative checks against a restored DNS IP map. (#31872, @nathanjsweet)
- fqdn: Fixed bug that caused DNS Proxy to be overly restrictive on allowed DNS selectors. (#31713, @nathanjsweet)

### 1.13.16

- Fix overlapping keys in agent-side service BPF map cache used for retries. In rare cases this bug may have caused retrying of a failed BPF map update for a services entry to be skipped leading to a missing entry. This may have, for example, adversely affected recovering from a full BPF service map after excess services were removed. (Backport PR #31887, Upstream PR #29581, @xyz-li)
- dnsproxy: Fix bug where DNS request timed out too soon (Backport PR #32252, Upstream PR #31999, @gandro)
- Fixes an (unlikely) bug where HostFirewall policies may miss updates to a node's labels. (Backport PR #32386, Upstream PR #30548, @squeed)
- fqdn: fix memory leak in transparent mode when there was a moderately high number of parallel DNS requests (>100). (Backport PR #32053, Upstream PR #31959, @marseel)
- [v1.13] Go linter fix backport (cilium/cilium#31983, @tklauser)
- workflows: Fix CI jobs for push events on private forks (Backport PR #32252, Upstream PR #32085, @pchaigno)
- [v.13] test: Fix Endpoint Test (cilium/cilium#32197, @nathanjsweet)
- [v1.13] endpoint: Fix Endpoint Integration Tests (cilium/cilium#32171, @nathanjsweet)
- Fix spelling in DNS-based proxy info (Backport PR #31887, Upstream PR #31728, @saintdle)
- fqdn: Fix Upgrade Issue Between PortProto Versions (Backport PR #32386, Upstream PR #32325, @nathanjsweet)
- fix k8s versions tested in CI (cilium/cilium#31968, @nbusseneau)

### 1.13.17

- github/workflows: fix digests file creation (Backport PR #32887, Upstream PR #32860, @aanm)
- Fixes accidentally ignoring the preflight.nodeSelector Helm value. (Backport PR #32696, Upstream PR #32548, @squeed)
- background-sync: fix bootstrap issue and edge-case with 1 node (Backport PR #32885, Upstream PR #32630, @marseel)

### 1.13.18

- Fix service connection to terminating backend, when the service has no more backends available. (Backport PR #33276, Upstream PR #31840, @julianwiedmann)
- Fixes unencrypted traffic among nodes when IPsec is used with L7 egress proxy. (Backport PR #31977, Upstream PR #32683, @jschwinger233)
- github: fix cloud workflows for renovate (Backport PR #33315, Upstream PR #33320, @aanm)
- github: fix worfklows used by renovate (Backport PR #33315, Upstream PR #33309, @aanm)
- Fix renovate's concurrency group (Backport PR #33563, Upstream PR #33528, @aanm)
- github: fix concurrency groups for push events (cilium/cilium#33646, @aanm)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.13.18**, the newest release recorded here for this line.

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
