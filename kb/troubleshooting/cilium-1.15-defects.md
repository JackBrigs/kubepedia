---
id: TROUBLE-CILIUM_1_15_DEFECTS
type: troubleshooting
title: "cilium 1.15: defects fixed in the 1.15 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.15.0 <1.16.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.15 known issues
  - cilium 1.15 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.15 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.15: defects fixed in the 1.15 line

## Summary

**325 defects** the project fixed across **20 releases** of the 1.15 line, from 1.15.0 to
1.15.19. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.15.0

- ENI: fix calculateExcessIPs excessive calculate of excess ip (#28467, @wu0407)
- Fix inaccurate calculation for bootstrap stats of restore (#27983, @PlatformLC)
- fix: Preserve OwnerReferences when updating Ingresses with Load Balancer in shared mode (#28452, @bittermandel)
- Fixes name used for disabling KVStoreMesh metrics. (#27680, @marseel)
- Avoid panic during BPF program compilation when clang command fails to start (Backport PR #30264, Upstream PR #30009, @ti-mo)
- bgpv1: fix manager_test.go build error (#27543, @ldelossa)
- bpf: fix wrong loopback address mask value (Backport PR #30230, Upstream PR #29946, @haiyuewa)
- bpf: fixes an issue where inserting inner maps into an outer may fail with EINVAL due to flags mismatch (#28710, @ldelossa)
- bug fix: close status collector when daemon exits (#27937, @sofat1989)
- datapath: fix dbg-capture-proxy-[pre/post] reporting (#27704, @mhofstetter)
- datapath: Fix primary flag in NodeAddress (#29483, @joamaki)
- egressgw: Fix the issue that an iptables SNAT rule in the host netns interferes packets to egress gw and bypass the egress GW policy (#29379, @ysksuzuki)
- endpointmanager: fix bpf policy pressure getting stuck. (#28185, @tommyp1ckles)
- envoy: fix init order between accesslog and xDS server (#27617, @mhofstetter)
- envoy: fix SO_REUSEPORT with BPF TPROXY (#30459, @mhofstetter)
- examples: Fix YAML error backendRefs in HTTP Header Modifier (#27871, @haiyuewa)
- Fix a bug that may cause traffic to the node internal IP addresses to be incorrectly masqueraded when node encryption and remote node identities are both disabled, due to an inconsistency in the node manager when handling ipset entries insertions and deletions on node updates. (Backport PR #30230, Upstream PR #29986, @qmonnet)
- Fix all packet drops due to missed tail calls, enable zero tolerance for these errors in CI (Backport PR #30324, Upstream PR #30248, @ti-mo)
- Fix and prevent future bugs limiting pod-to-pod network performance under high load when tunneling and IPSec are both enabled. (Backport PR #30079, Upstream PR #29616, @learnitall)
- Fix bug that could cause IPsec route change failures to be silent. (Backport PR #30529, Upstream PR #29423, @derailed)
- Fix bugs in health-server that cause the state in the prober's cache to drift and allow nodes with empty IP addresses to be added. (Backport PR #30230, Upstream PR #29745, @thorn3r)
- Fix cilium-envoy ServiceMonitor port name (#27207, @pixiono)
- Fix connection disruption for IPsec during downgrade to v1.14 by attaching correct bpf program to devices. (#27480, @jschwinger233)
- Fix endpoint logger not formatting logs as JSON when daemon log format is set to JSON (#27263, @leblowl)
- Fix error when using multiple allowRoutes namespaces in gateway (#30550, @mhofstetter)
- Fix Helm rendering for `dashboards.enabled=true` (#28542, @bakito)
- Fix instances of leaked health reporter updates. (Backport PR #30230, Upstream PR #30134, @tommyp1ckles)
- Fix issue where agent attempting to restore local node information (such as cilium_host ip) would fail on k8s fallback method. (Backport PR #30349, Upstream PR #29460, @tommyp1ckles)
- Fix missing NODE_ADD Hubble peer messages in some cases (#28226, @AwesomePatrol)
- Fix nodeinit issue causing NotReady state in Kubernetes nodes when laying down an incorrect CNI config (Backport PR #30529, Upstream PR #30399, @tlcowling)
- Fix performance regression for pod-to-pod traffic WireGuard and tunneling. (Backport PR #30529, Upstream PR #30329, @3u13r)
- Fix potential deadlock that results in stale authentication entries in Cilium (#29082, @meyskens)
- Fix rare bug possibly causing connection disruption and/or agent panic due to node events processing before full initialization. (Backport PR #30529, Upstream PR #30282, @giorio94)
- Fix rendering helm operator-dashboard annotations (#29106, @Zariel)
- Fix wrong host and router IP being used for some IPv6 deployments, which was causing various connectivity problems. (Backport PR #28500, Upstream PR #28417, @ti-mo)
- fix: PromQL syntax on cilium policy query Grafana dashboard (Backport PR #30529, Upstream PR #29938, @M0NsTeRRR)
- Fixed health probing where ICMP probe was incorrectly reporting node as unreachable or reporting unreachable node as reachable in some cases. (Backport PR #30529, Upstream PR #30504, @marseel)
- Fixes an issue where an empty ControlPlaneState was used during registration of BGP speakers. This would cause reconciliation issues as the current state would be unknown. (#27117, @ldelossa)
- Fixes an L7 proxy issue by re-introducing 2005 route table. (#29530, @jschwinger233)
- gateway-api: fix empty URI when removing path prefix (#28606, @dddddai)
- gateway-api: fix status reconcile error handling (Backport PR #30230, Upstream PR #29894, @mhofstetter)
- helm: Fix envoy servicemonitor annotations (Backport PR #30230, Upstream PR #30017, @pmcgrath)
- init well-known identity before new policy repository to fix the fqdn policy issue when enable well-known identity. (Backport PR #30529, Upstream PR #30052, @yingnanzhang666)
- l7lb: Fix bug where not all relevant ports of a Service were synchronized to Envoy (Backport PR #30264, Upstream PR #30107, @mhofstetter)
- lbipam: Fix off-by-one error in LBIPAM range allocation (#29425, @YutaroHayakawa)
- node/wireguard: Fix node-to-node encryption inconsistencies in kvstore mode (Backport PR #30530, Upstream PR #30423, @gandro)
- nodediscovery: Fix bug where CiliumInternalIP was flapping (Backport PR #29973, Upstream PR #29964, @gandro)
- pkg/endpoint: fix endpoint health update always being ok. (Backport PR #30529, Upstream PR #30365, @tommyp1ckles)
- policy: Fix mapstate changes error in entry change comparison (Backport PR #30079, Upstream PR #29815, @jrajahalme)
- proxy: fix multiple envoy listeners for same proxyType (#27510, @mhofstetter)
- statedb: Fix termination of string and IP keys (#29368, @joamaki)
- Unify parsing of StringSlice flags and allow splitting by commas (preferably) or by spaces. This fixes parsing of 'prometheus.metrics'. (Backport PR #30079, Upstream PR #29848, @joamaki)
- bpf/tests: Fixed `loop not unrolled` error in pktgen (#28942, @dylandreimerink)
- bpf: fix flakes when checking metrics map values. (#28325, @tommyp1ckles)
- bpf: fix test configuration for 5.10 and 6.1 kernels (Backport PR #30230, Upstream PR #29999, @julianwiedmann)
- ci/ipsec: Fix version retrieval for downgrades to closest patch release (Backport PR #30529, Upstream PR #30503, @qmonnet)
- Fix container scanning workflow (#26542, @ferozsalam)
- Fix exporting results to gs bucket. (#29587, @marseel)
- Fix pre-flight clusterrole check (#29224, @marseel)
- gh/workflows: Fix setting endpoint routes in ci-e2e (#27384, @brb)
- ipam: Fix race in NodeManager.Resync (#26963, @jaffcheng)
- renovate: fix match string for go version updates in go.mod (#28000, @tklauser)
- Avoid requiring the latest Go toolchain patch version to build (#28686, @joestringer)
- bgp: fix up formatting in CiliumBGPPeeringPolicy (#27219, @julianwiedmann)
- bgpv1: fix incorrect error messages in the reconcilePodIPPool function (#29125, @hargrovee)
- bgpv1: fix merge race conflict on NewGoBGPServer (#29321, @mhofstetter)
- bpf: don't build all bpf when making containers (fix) (#25937, @squeed)
- bpf: fib: fix issues with L2 resolution (Backport PR #30349, Upstream PR #30128, @julianwiedmann)
- Bug: Fix module health status output (#29140, @derailed)
- cilium-dbg, policy, api: Fix labels in policy selectors output (#29152, @christarazi)
- cilium: iptables masquerade to route source fixes (#29591, @borkmann)
- contrib: fix bump-readme script (#27648, @nebril)
- contrib: Fix missing function in post-release.sh (#28372, @joestringer)
- contrib: Fix prerelease pullPolicy (#28906, @joestringer)
- contrib: Fix remote detection for security branches (#27891, @joestringer)
- contrib: Fix remote repo detection for .git suffix (#28198, @joestringer)
- correct stats calculation for prepareBuild of endpoint_regeneration_time (#28150, @PlatformLC)
- correct stats for total time of policyregenerateion (#28153, @PlatformLC)
- Correct the comment for Service4Value and Service6Value (#27824, @haiyuewa)
- daemon: Fix incorrect node and ciliumnode resource type in annotations (#29522, @hargrovee)
- Do not ignore link local addresses when detecting network devices. This fixes a problem in setups where network devices that only had link local addresses were ignored. (#27868, @joamaki)
- egressgw: doc fixes for install-egress-gateway-routes removal (#28523, @lmb)
- endpoint: fix removed code comment. (#29172, @tommyp1ckles)
- endpointslice: fix EndpointSlice import (#26938, @mhofstetter)
- example/connectivity-check: fix port conflict, capture termination log (#28833, @squeed)
- Fix Cilium Datapath Prometheus metric names (#29226, @carnerito)
- Fix cilium-envoy ServiceMonitor template typo (Backport PR #30230, Upstream PR #29976, @cornfeedhobo)
- Fix data race during Hubble setup (#28322, @glrf)
- fix duplicated ids in prerelease testing template (#27865, @jspaleta)
- Fix IPv4 checksum recalculation in SNAT flows where ports are rewritten. (#28768, @gentoo-root)
- Fix log error in clustermesh-apiserver when connecting external workloads (Backport PR #30079, Upstream PR #29896, @giorio94)
- Fix LookupReservedIdentityByLabels function to return consistent results (#26795, @skmatti)
- Fix regression causing a 10x increase in the duration of endpoint integration tests (Backport PR #30079, Upstream PR #29826, @giorio94)
- Fix restore of previous router IP due to missing VPC CIDR in Alibabacloud section of CiliumNode Spec (#26843, @haozhangami)
- Fix spelling for "WireGuard" (#26764, @qmonnet)
- Fix up CCG related metrics (#27806, @christarazi)
- fix(deps): update all go dependencies main (main) (#26567, @renovate[bot])
- fix(deps): update all go dependencies main (main) (#27348, @renovate[bot])
- fix(deps): update all go dependencies main (main) (#27440, @renovate[bot])
- fix(deps): update all go dependencies main (main) (#27906, @renovate[bot])
- fix(deps): update all go dependencies main (main) (minor) (#26695, @renovate[bot])
- fix(deps): update all go dependencies main (main) (minor) (#26822, @renovate[bot])
- fix(deps): update all go dependencies main (main) (minor) (#27266, @renovate[bot])
- fix(deps): update all go dependencies main (main) (minor) (#27742, @renovate[bot])
- fix(deps): update all go dependencies main (main) (minor) (#28072, @renovate[bot])
- fix(deps): update all go dependencies main (main) (minor) (#28098, @renovate[bot])
- fix(deps): update all go dependencies main (main) (minor) (#28618, @renovate[bot])
- fix(deps): update all go dependencies main (main) (minor) (#28730, @renovate[bot])
- fix(deps): update all go dependencies main (main) (minor) (#28994, @renovate[bot])
- fix(deps): update all go dependencies main (main) (minor) (#29264, @renovate[bot])
- fix(deps): update all go dependencies main (main) (minor) (#29398, @renovate[bot])
- fix(deps): update all go dependencies main (main) (minor) (#29538, @renovate[bot])
- fix(deps): update all go dependencies main (main) (minor) (#29771, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#26569, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#26693, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#26820, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#27135, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#27260, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#27441, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#27736, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#27939, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#28070, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#28193, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#28348, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#28514, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#28615, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#28727, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#28866, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#28993, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#29134, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#29389, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#29536, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#29574, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#29593, @renovate[bot])
- fix: add check if debug is enabled when adding trace levels to envoy deamonset. (#27161, @dreanor65)
- fix: remove help message in build config failure (Backport PR #30230, Upstream PR #28974, @vipul-21)
- fix: Remove the latest image tag from docs as latest tag is not published (#28241, @vipul-21)
- Fixed conflicting PRs in main (#27209, @dylandreimerink)
- Fixes rate limiting for CES Controller (#28963, @alan-kut)
- gateway-api: fix up for import rename (#29143, @julianwiedmann)
- helm: Fix annotation duplication problems for cilium-agent (#28978, @bradwhitfield)
- hive: Fix hive hook output and move lifecycle to cell package (Backport PR #30529, Upstream PR #30416, @joamaki)
- hubble-relay: fix panic during server shutdown (#29705, @mhofstetter)
- images: Fix init-container script for cilium-dbg (#29424, @joestringer)
- ipam/multipool: Fix comment for removeExpiration (#28031, @hargrovee)
- ipam: Fix duplicate metric ipam_event release (#29520, @christarazi)
- ipcache: Fix incorrect source for kube-apiserver in tests (#28407, @christarazi)
- ipcache: fix releasing node CIDRs after restoration (#28620, @squeed)
- ipsec: Fix Godoc document comment typo (#27721, @haiyuewa)
- labels/cidr: Fix slice preallocation size (#28378, @pippolo84)
- maps: nat: fix copy & paste in error message from doFlush*() (#29097, @julianwiedmann)
- Minor documentation fixes and improvements for the BGP MD5 feature (#29375, @nvibert)
- mountinfo: fix build on linux/386 (#29481, @tklauser)
- operator: Fix CEP and CES events debug logs (#28797, @dlapcevic)
- policy: Fix MapState.Equals() (Backport PR #30264, Upstream PR #30233, @jrajahalme)
- proxy: allow to provide fixed port for DNS proxy via cell (#28786, @tklauser)
- service: fix service manager interface mismatch caused by merge race (#29018, @giorio94)
- Some small fixes to make kind-fast (#28621, @squeed)
- statedb: Fix revision indexing (#29840, @joamaki)
- statedb: Fix watch channel returned by LowerBound (#28644, @joamaki)
- stream: fix spurious event on termination when Debounce is used (#29347, @giorio94)
- test/controlplane: Fix hostport test after API change (#26685, @pippolo84)
- Typo fix in the docs (Backport PR #30529, Upstream PR #30407, @nvibert)
- [1.15] loader: fix obsolete XDP program removal (#30224, @rgo3)

### 1.15.1

- Fix bug in indexing of routes that lead to veth devices being considered native devices, which caused the wrong BPF program to be loaded onto them. (Backport PR #30767, Upstream PR #30762, @dylandreimerink)
- fix edge case in node addressing logic which could result in a panic (Backport PR #30767, Upstream PR #30757, @dylandreimerink)
- hive: Fix start hook log output (Backport PR #30727, Upstream PR #30712, @joamaki)
- Fix failure in `FuzzDenyPreferredInsert` test (Backport PR #30681, Upstream PR #30368, @christarazi)
- [v1.15] ci/ipsec: Fix downgrade version for release preparation commits (#30718, @qmonnet)

### 1.15.2

- Fixes a bug where ToFQDN IPs may be garbage collected too early, disrupting existing connections. (Backport PR #31318, Upstream PR #31205, @squeed)
- endpoint: fix inability to create endpoint with labels in a single API call (Backport PR #30997, Upstream PR #30170, @oblazek)
- Fix bug in the VTEP feature which caused all traffic from the VTEP to be dropped with "Incorrect VNI from VTEP" (Backport PR #31154, Upstream PR #31039, @joestringer)
- Fix bug prevented endpoints from sending or receiving network traffic due to the 'reserved:init' label persisting after initialization. (Backport PR #31047, Upstream PR #30909, @aanm)
- Fix GC interval calculation by taking into account the actual time passed between GC runs. (Backport PR #31154, Upstream PR #28657, @gentoo-root)
- Fix host firewall policy enforcement for pod to node traffic when tunneling is enabled and KPR is disabled (Backport PR #30997, Upstream PR #30818, @giorio94)
- Fix the referenced interface in iptables rules (`eni+` instead of `lxc+`) when `--enable-endpoint-routes=true` and `--cni-chaining-mode="aws-cni"` (Backport PR #31154, Upstream PR #30766, @pippolo84)
- Fixes an IPv6 issue that cilium doesn't respond to Neighbor Solicitation targeting the pods on same node. (Backport PR #31155, Upstream PR #30837, @jschwinger233)
- Fixes proxy issues by opting out from SNAT for L7 + Tunnel. (Backport PR #31158, Upstream PR #29594, @jschwinger233)
- Fixes proxy issues in egress direction (Backport PR #31158, Upstream PR #30095, @jschwinger233)
- Fixes some valid GC entries being removed at agent restart (Backport PR #30863, Upstream PR #29696, @rsafonseca)
- hubble: fix parsing of invalid HTTP URLs (Backport PR #31154, Upstream PR #31100, @kaworu)
- srv6: Fix packet drop with GSO type mismatch (Backport PR #30799, Upstream PR #30732, @YutaroHayakawa)
- statedb: Fix race between Observable and DB stopping (Backport PR #30863, Upstream PR #30816, @joamaki)
- ci/ipsec: Fix downgrade version retrieval (Backport PR #31047, Upstream PR #30742, @qmonnet)
- Fix datapath mode in Network Performance CI test (Backport PR #30863, Upstream PR #30756, @marseel)
- Prevent E2E tests from failing on a known-ok warning log of temporary CRD failure (Backport PR #31154, Upstream PR #30778, @learnitall)

### 1.15.3

- Fix a bug in the StateDB library that may have caused stale read after write. This may have potentially affected the L2 announcements feature and the node address selection. (Backport PR #31342, Upstream PR #31164, @joamaki)
- Fix a bug where pod label updates are not reflected in endpoint labels in presence of filtered labels. (Backport PR #31473, Upstream PR #31395, @tklauser)
- Fixed issue with assigning 0 nodeID when corresponding bpf map run out of space. Potentially it could have impacted connectivity in large clusters (>4k nodes) with IPSec or Mutual Auth enabled. Otherwise, it was merely generating unnecessary error log messages. (Backport PR #31490, Upstream PR #31380, @marseel)
- hubble/relay: Fix certificate reloading in PeerManager (Backport PR #31568, Upstream PR #31376, @glrf)
- Hubble: fix traffic direction and is reply when IPSec is enabled (Backport PR #31568, Upstream PR #31211, @kaworu)
- operator: fix errors/warnings metric. (Backport PR #31490, Upstream PR #31214, @tommyp1ckles)
- bgpv1: fix Test_PodIPPoolAdvert flakiness (Backport PR #31490, Upstream PR #31365, @rastislavs)
- bpf: fix go testdata check in ci (Backport PR #31554, Upstream PR #31419, @mhofstetter)
- controlplane: fix mechanism for ensuring watchers (Backport PR #31490, Upstream PR #31030, @bimmlerd)
- Fix bug preventing consistent symbols between ELF and BTF for eBPF unit tests. (Backport PR #31342, Upstream PR #30610, @learnitall)
- loader: fix issue where errors cancelled compile cause error logs. (Backport PR #31342, Upstream PR #30988, @tommyp1ckles)
- policy: Fix missing labels from SelectorCache selectors (Backport PR #31490, Upstream PR #31358, @christarazi)

### 1.15.4

- Fix overlapping keys in agent-side service BPF map cache used for retries. In rare cases this bug may have caused retrying of a failed BPF map update for a services entry to be skipped leading to a missing entry. This may have, for example, adversely affected recovering from a full BPF service map after excess services were removed. (Backport PR #31890, Upstream PR #29581, @xyz-li)
- Avoid drops with "CT: Unknown L4 protocol" for non-ICMP/TCP/UDP traffic, caused by an error check in the BPF NAT engine. (Backport PR #31890, Upstream PR #31820, @julianwiedmann)
- cilium-health: Fix broken retry loop in `cilium-health-ep` controller (Backport PR #31727, Upstream PR #31622, @gandro)
- Fix a bug that could cause local packet delivery to be skipped, leading to lower performance, when IPsec was enabled and `--devices` provided. (Backport PR #31601, Upstream PR #31345, @pchaigno)
- Fix incorrect reporting of the number of etcd lock leases in cilium-dbg status. (Backport PR #31890, Upstream PR #31781, @giorio94)
- fix: Delegated ipam not configure ipv6 if ipv6 disabled in agent (Backport PR #31727, Upstream PR #31104, @tamilmani1989)
- Fixed a race condition in service updates for L7 LB. (Backport PR #31860, Upstream PR #31744, @jrajahalme)
- fqdn: Fix minor restore bug that causes false negative checks against a restored DNS IP map. (#31870, @nathanjsweet)
- fqdn: Fixed bug that caused DNS Proxy to be overly restrictive on allowed DNS selectors. (Backport PR #31727, Upstream PR #31328, @nathanjsweet)
- gateway-api: fixed RequestRedirect picks wrong port with multiple listeners (Backport PR #31769, Upstream PR #31361, @chaunceyjiang)
- bitlpm: Document and Fix Descendants Bug (Backport PR #31890, Upstream PR #31851, @nathanjsweet)
- Fix spelling in DNS-based proxy info (Backport PR #31890, Upstream PR #31728, @saintdle)

### 1.15.5

- dnsproxy: Fix bug where DNS request timed out too soon (Backport PR #32230, Upstream PR #31999, @gandro)
- Fix failing service connections, when the service requests are transported via cilium's overlay network. (Backport PR #32230, Upstream PR #32116, @julianwiedmann)
- Fix issue causing clustermesh-apiserver/kvstoremesh to not start when run with a non-root user (Backport PR #31879, Upstream PR #31539, @giorio94)
- Fix service connection to terminating backend, when the service has no more backends available. (Backport PR #32092, Upstream PR #31840, @julianwiedmann)
- Fix various bugs related to restart of StatefulSet pods that may result in connectivity issues (Backport PR #32432, Upstream PR #31605, @christarazi)
- Fixes a bug where Cilium in chained mode removed the `agent-not-ready` taint too early if the primary network is slow in deploying. (Backport PR #32230, Upstream PR #32168, @squeed)
- Fixes an (unlikely) bug where HostFirewall policies may miss updates to a node's labels. (Backport PR #32384, Upstream PR #30548, @squeed)
- fqdn: fix memory leak in transparent mode when there was a moderately high number of parallel DNS requests (>100). (Backport PR #32103, Upstream PR #31959, @marseel)
- Prevent Cilium agents from incorrectly restarting an etcd watch against a different etcd instance. (cilium/cilium#32005, @giorio94)
- workflows: Fix CI jobs for push events on private forks (Backport PR #32230, Upstream PR #32085, @pchaigno)
- clustermesh: fix panic if the etcd client cannot be created (Backport PR #32384, Upstream PR #32225, @giorio94)
- Fix helm chart incompatible types for comparison (Backport PR #32230, Upstream PR #32025, @lou-lan)
- fqdn: Fix Upgrade Issue Between PortProto Versions (Backport PR #32384, Upstream PR #32325, @nathanjsweet)
- fix k8s versions tested in CI (cilium/cilium#31965, @nbusseneau)

### 1.15.6

- github/workflows: fix digests file creation (Backport PR #32889, Upstream PR #32860, @aanm)
- Fix DNS proxy regression from Cilium 1.15 on IPv4 only nodes (Backport PR #32789, Upstream PR #31671, @foyerunix)
- Fix indexing bug in the logic for picking NodePort addresses. In rare cases this may have caused wrong address to be selected for NodePort use, or an out-of-bounds access. (Backport PR #32691, Upstream PR #32506, @joamaki)
- Fix PromQL query in Cilium Metrics dashboard (Backport PR #32691, Upstream PR #32017, @mikemykhaylov)
- Fix rare race condition afflicting clustermesh when disconnecting from a remote cluster, possibly causing the agent to panic (Backport PR #32691, Upstream PR #32513, @giorio94)
- Fixes accidentally ignoring the preflight.nodeSelector Helm value. (Backport PR #32691, Upstream PR #32548, @squeed)
- Fixes unencrypted traffic among nodes when IPsec is used with L7 egress proxy. (Backport PR #32932, Upstream PR #32683, @jschwinger233)
- background-sync: fix bootstrap issue and edge-case with 1 node (Backport PR #32748, Upstream PR #32630, @marseel)
- Fix: LB service lookup for flow matching conntrack entry (cilium/cilium#32608, @sypakine)

### 1.15.7

- datapath: Fix redirect from from L3 netdev to tunnel (Backport PR #33529, Upstream PR #33421, @brb)
- Datasource error fixed for Hubble DNS and Network dashboards (Backport PR #33631, Upstream PR #30580, @Pionerd)
- Fix #32587 concurrent hubble dynamic exporter stop and reload (Backport PR #33098, Upstream PR #33000, @marqc)
- Fix hubble metrics leak by using CiliumEndpoint watcher to remove stale metrics. (Backport PR #33529, Upstream PR #33260, @sgargan)
- Fix rare spurious double reconnection upon clustermesh configuration change for remote cluster (Backport PR #33378, Upstream PR #33248, @giorio94)
- Fix too many open Unix sockets (Backport PR #33631, Upstream PR #33569, @chaunceyjiang)
- IPv6 and IPv4 '0.0.0.0/0' CIDR parsing in policy processing has been fixed (Backport PR #33529, Upstream PR #33448, @jrajahalme)
- Recreate CT entries for non-TCP to fix L7 proxy redirect failures. (Backport PR #33378, Upstream PR #33222, @ysksuzuki)
- workflows: e2e-upgrade: fix EXTRA parameters (Backport PR #33223, Upstream PR #33150, @jibi)
- github: fix cloud workflows for renovate (Backport PR #33321, Upstream PR #33320, @aanm)
- github: fix worfklows used by renovate (Backport PR #33317, Upstream PR #33309, @aanm)
- bpf: encap: fix ifindex in TO_OVERLAY trace notification (Backport PR #33575, Upstream PR #33083, @julianwiedmann)
- bpf: lxc: fix ifindex in TO_ENDPOINT trace notification (Backport PR #33575, Upstream PR #33085, @julianwiedmann)
- examples: Fix subject selector in ingress policy (Backport PR #33378, Upstream PR #33292, @joestringer)
- Fix renovate's concurrency group (Backport PR #33559, Upstream PR #33528, @aanm)
- ipcache: Fix orphaned ipcache entries when mixing Upsert and Inject (Backport PR #33152, Upstream PR #33120, @squeed)
- LRP: Misc fix-ups (Backport PR #33529, Upstream PR #33442, @aditighag)
- [v1.15] gh/workflows: fix skipping of no-frag test in ipsec-e2e workflow (cilium/cilium#33671, @julianwiedmann)

### 1.15.8

- auth: Fix data race in Upsert (Backport PR #34157, Upstream PR #33905, @chaunceyjiang)
- auth: fix fatal error: concurrent map iteration and map write (Backport PR #33809, Upstream PR #33634, @chaunceyjiang)
- Fix an issue in updates to node addresses which may have caused missing NodePort frontend IP addresses. May have affected NodePort/LoadBalancer services for users running with runtime device detection enabled when node's IP addresses were changed after Cilium had started. Node IP as defined in the Kubernetes Node is now preferred when selecting the NodePort frontend IPs. (Backport PR #33818, Upstream PR #33629, @joamaki)
- Fix bug causing etcd upsertion/deletion events to be potentially missed during the initial synchronization, when Cilium operates in KVStore mode, or Cluster Mesh is enabled. (Backport PR #34183, Upstream PR #34091, @giorio94)
- Fix issue in picking node IP addresses from the loopback device. This fixes a regression in v1.15 and v1.16 where VIPs assigned to the lo device were not considered by Cilium. Fix spurious updates node addresses to avoid unnecessary datapath reinitializations. (Backport PR #34086, Upstream PR #34012, @joamaki)
- Fix rare race condition afflicting clustermesh while stopping the retrieval of the remote cluster configuration, possibly causing a deadlock (Backport PR #33809, Upstream PR #33735, @giorio94)
- Fixes a race condition during agent startup that causes the k8s node label updates to not get propagated to the host endpoint. (Backport PR #33663, Upstream PR #33511, @skmatti)
- lbipam: fixed bug in sharing key logic (Backport PR #34157, Upstream PR #34106, @dylandreimerink)
- pkg/metrics: fix data race warning on metrics init hook. (Backport PR #33962, Upstream PR #33823, @tommyp1ckles)
- [v1.15] gh/e2e: fix up config 15 to not use bpf-next (cilium/cilium#33738, @julianwiedmann)
- policy: Fix `mapstate.Diff()` used in tests (Backport PR #33809, Upstream PR #33449, @jrajahalme)
- Fix bug in Bandwidth Manager that caused it to not find native devices. (cilium/cilium#33910, @joamaki)

### 1.15.9

- BGPv1 + BGPv2: Fix incorrect service reconciliation in setups with multiple BGP instances (virtual routers) (cilium/cilium#34331, @rastislavs)
- config: fix disabling config 'Debug' (Backport PR #34470, Upstream PR #34401, @mhofstetter)
- daemon: Fix error logic flow for pod store being out of date (Backport PR #34587, Upstream PR #34389, @christarazi)
- envoy: fix log level mapping when changing log level via API (Backport PR #34456, Upstream PR #34400, @mhofstetter)
- Fix synchronization of CiliumEndpointSlices when running the Cilium Operator in identity-based slicing mode. (Backport PR #34456, Upstream PR #32239, @thorn3r)
- Fix the Egress Gateway reconciliation logic to make progress after setting the rp_filter sysctl failed. (Backport PR #34830, Upstream PR #34775, @julianwiedmann)
- helm: fix envoy prometheus metrics scraping with servicemonitor (Backport PR #34473, Upstream PR #34448, @mhofstetter)
- ipcache: Yet another refcounting fix with mix of APIs (Backport PR #34933, Upstream PR #34715, @gandro)
- lbipam: fix panic when changing the shared key & req. ip annotation (Backport PR #34456, Upstream PR #34236, @mhofstetter)
- bgpv1/test: fix route matching in PodIPPoolAdvert test (Backport PR #34456, Upstream PR #34270, @rastislavs)
- Fix: push PR changes when renovate build images under the workflow_call context (Backport PR #34830, Upstream PR #34650, @Artyop)
- fix: base image update workflow will now be triggered on renovate branches with a workflow_call event type (Backport PR #34456, Upstream PR #34372, @Artyop)
- images: fix path script (Backport PR #34767, Upstream PR #34764, @aanm)

### 1.15.10

- bugtool: fix cilium-health command (Backport PR #35276, Upstream PR #35068, @ayuspin)
- Fix a bug in Cilium's kube-proxy replacement, where replies by a local backend are dropped with DROP_NO_FIB. (Backport PR #34917, Upstream PR #34303, @julianwiedmann)
- Fix issue where bpf packet buffer mark would in some cases set incorrect mark value resulting in incorrectly SNATed traffic. (Backport PR #35037, Upstream PR #34789, @tommyp1ckles)
- Fixed bug in LB-IPAM where restarting the operator would unshare previously shared IPs between services (Backport PR #35037, Upstream PR #34783, @dylandreimerink)
- Fixed bug in tracking policy changes that could have resulted in revert not woking in failure cases as expected. (Backport PR #35276, Upstream PR #35109, @jrajahalme)
- Fixed bug where service id allocator would loop infinity when out of service ids (Backport PR #35276, Upstream PR #35033, @WeeNews)
- Fixes deadlock in identity watcher. This fixes an issue where a kvstore disconnect can cause the event receiver to exit and the event sender to get stuck forever. (Backport PR #35276, Upstream PR #34611, @dboslee)
- Fixes startup fatal error when updating CiliumNode resource. (Backport PR #34917, Upstream PR #34862, @harsimran-pabla)
- github/lint-build-commits: fix workflow for push events (Backport PR #35276, Upstream PR #35264, @aanm)
- [v1.15] ci: fix check generated documentation (cilium/cilium#35261, @mhofstetter)
- fix: repository nil value handled on workflow_dispatch context for renovate updates (Backport PR #34917, Upstream PR #34902, @Artyop)
- github: fix build image process to commit changes (Backport PR #35276, Upstream PR #35262, @aanm)
- github: fix lvh-kind warnings (Backport PR #35168, Upstream PR #34811, @aanm)
- github: fix runtime image digests (Backport PR #35118, Upstream PR #35107, @aanm)
- policy: Fix breakages on v1.15 branch (cilium/cilium#35300, @christarazi)

### 1.15.11

- Fix packet drops for pod-to-pod connections that pass through ingress & egress proxy when using IPsec, caused by MTU misconfiguration. (Backport PR #35586, Upstream PR #35173, @smagnani96)
- Fix redirect from L3 device to remote endpoint via overlay network. (Backport PR #35586, Upstream PR #35165, @julianwiedmann)
- Fixed bug which prevented IP surge allocation from working (Backport PR #35419, Upstream PR #34090, @dlapcevic)
- l7lb: fix registration of flag loadbalancer-l7 (Backport PR #35778, Upstream PR #35623, @mhofstetter)
- dnsproxy: fix error when sessionUDPFactory fails (Backport PR #35586, Upstream PR #33998, @marseel)
- [v1.15] .github: Fix missing variable escaping in LVH command (cilium/cilium#35893, @gandro)

### 1.15.12

- bgp: fix race in bgp stores (Backport PR cilium/cilium#36071, Upstream PR cilium/cilium#35971, @harsimran-pabla)
- gateway-api: Fix gateway checks for namespace (Backport PR cilium/cilium#36464, Upstream PR cilium/cilium#35452, @sayboras)

### 1.15.13

- github: fix conformance-k8s NP test (Backport PR cilium/cilium#36483, Upstream PR cilium/cilium#36355, @aanm)
- Fix `make -C Documentation update-cmdref` when make uses `--jobserver-style=fifo`. (Backport PR cilium/cilium#36871, Upstream PR cilium/cilium#36788, @gentoo-root)

### 1.15.14

- Fix bug potentially causing newly added endpoints to remain stuck in waiting-to-regenerate state forever, causing traffic from/to that endpoint to be incorrectly dropped. (Backport PR cilium/cilium#37281, Upstream PR cilium/cilium#37086, @giorio94)
- Fix specifying multiple interfaces for egress masquerade with enable-masquerade-to-route-source=false (Backport PR cilium/cilium#37281, Upstream PR cilium/cilium#36103, @viktor-kurchenko)
- gha: fix retrieval of DNS server in conformance external workloads (Backport PR cilium/cilium#37376, Upstream PR cilium/cilium#37361, @giorio94)
- Fix API generation and add trusted dependencies to renovate config (Backport PR cilium/cilium#37646, Upstream PR cilium/cilium#36957, @aanm)
- renovate: add fix grpc-go autodetection (Backport PR cilium/cilium#37281, Upstream PR cilium/cilium#33570, @aanm)
- gha: Fix feature test artifact upload (cilium/cilium#37205, @sayboras)

### 1.15.15

- Fix creation and deletion of host port maps that would occasionally leave pods without them (Backport PR cilium/cilium#37899, Upstream PR cilium/cilium#37419, @javanthropus)
- Fix envoy metrics could not be obtained on IPv6-only clusters (Backport PR cilium/cilium#37899, Upstream PR cilium/cilium#37818, @haozhangami)
- Fix: cilium-operator no longer patches services on shutdown (Backport PR cilium/cilium#38107, Upstream PR cilium/cilium#37967, @rsafonseca)
- Fix helm value for IPAM Multi-Pool (Backport PR cilium/cilium#38013, Upstream PR cilium/cilium#37963, @saintdle)

### 1.15.16

- Fixed a bug where replies for pod-originating connections came into scope of HostFW Ingress Network policy. Applicable to configurations that use iptables for Masquerading. (Backport PR cilium/cilium#38776, Upstream PR cilium/cilium#35694, @julianwiedmann)
- Fix checked L4 port for UDP IPv6 packets in check-encryption-leak script. (Backport PR cilium/cilium#38522, Upstream PR cilium/cilium#38265, @smagnani96)
- Fix endianness for WireGuard UDP traffic in the check-encryption-leak script. (Backport PR cilium/cilium#38522, Upstream PR cilium/cilium#38292, @smagnani96)
- Fix erroneous TCP RST condition when no TCP packets in the check-encryption-leak script. (Backport PR cilium/cilium#38522, Upstream PR cilium/cilium#38291, @smagnani96)
- [v1.15] Manually fix builder image (cilium/cilium#38748, @smagnani96)
- Documentation: fix mentions of per-node `cilium-dbg` tool (Backport PR cilium/cilium#38301, Upstream PR cilium/cilium#38276, @tklauser)
- pkg/endpoint: fix race in unit test (Backport PR cilium/cilium#38301, Upstream PR cilium/cilium#38129, @squeed)

### 1.15.17

- Fix a deadlock when a host has no IPv4 address. (Backport PR cilium/cilium#39078, Upstream PR cilium/cilium#38938, @EmilyShepherd)
- Fix bug that would cause the `cilium-dbg encrypt status` command to not list any decryption interfaces when KPR is enabled. (Backport PR cilium/cilium#39216, Upstream PR cilium/cilium#39170, @pchaigno)
- k8s: Fixed a case when delete event for service endpointslices might have been missed if connectivity to k8s apiserver was broken causing stale service cache for service. (Backport PR cilium/cilium#38952, Upstream PR cilium/cilium#38779, @marseel)
- documentation: fix get deployment cmd (Backport PR cilium/cilium#39216, Upstream PR cilium/cilium#39155, @g0gn)

### 1.15.18

- bpf: test: fix up mis-spelled HAVE_NETNS_COOKIE (Backport PR cilium/cilium#39562, Upstream PR cilium/cilium#39420, @julianwiedmann)

### 1.15.19

- LBIPAM: Fix deletion of CiliumLoadBalancerIPPool with multiple IP blocks that led to an operator crash (Backport PR cilium/cilium#40092, Upstream PR cilium/cilium#40013, @pippolo84)
- docs/ipsec: Fix incorrect statement on hostns encryption (Backport PR cilium/cilium#40172, Upstream PR cilium/cilium#40133, @pchaigno)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.15.19**, the newest release recorded here for this line.

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
