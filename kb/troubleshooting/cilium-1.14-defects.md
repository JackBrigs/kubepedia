---
id: TROUBLE-CILIUM_1_14_DEFECTS
type: troubleshooting
title: "cilium 1.14: defects fixed in the 1.14 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.14.0 <1.15.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.14 known issues
  - cilium 1.14 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.14 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.14: defects fixed in the 1.14 line

## Summary

**363 defects** the project fixed across **19 releases** of the 1.14 line, from 1.14.0 to
1.14.19. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.14.0

- Change cilium_host IPv6 address, use node router IPv6 instead of native node IPv6, and fixed several relative IPv6 issues. (#24208, @jschwinger233)
- Fix broken IPv6 connectivity from outside to NodePort service when L7 ingress policy applied by removing PROXY_RT route table. (#24882, @jschwinger233)
- Fix CIDR json tag in CNP CIDRRule (#25617, @pippolo84)
- Fix docker-cilium-image target for DOCKER_FLAGS=--push (#23679, @pippolo84)
- Fix endpoint slices filtering to ensure we filter out headless services and continue to support older k8s versions where service labels are not propagated to endpoint slices (Backport PR #26799, Upstream PR #25351, @odinuge)
- Fixed incorrectly rendered chart when specified both configMap and customConf (#25200, @marseel)
- identity/cache: fix panic when re-init of cache after close. (#25269, @tommyp1ckles)
- operator: Fix default API server addr in metrics subcommand (#26132, @pippolo84)
- policy: Derivative policies (policies for cloud provider-specific identities) for egress deny rules were not being generated, this has now been fixed. (#23927, @rockc2020)
- bpf/nat: fix current behavior that is silently ignoring errors in a revSNAT context (#19753, @sahid)
- bpf: nodeport: fix handling of stale CT entry with CT_REPLY (#23894, @julianwiedmann)
- bpf: nodeport: fix up trace point in to-overlay NAT paths (#24886, @julianwiedmann)
- Bypassing policy check for IPv6 NDP to fix broken pod-to-pod connectivity when per-endpoint route is enabled with policy. (#24919, @jschwinger233)
- datapath: bigtcp: Fix the IPv4 BIG TCP may not work (#26336, @haiyuewa)
- datapath: Fix L7 reply to outside when endpoint routes disabled (#21980, @brb)
- egressgw: fix race with endpoint deletion (Backport PR #27038, Upstream PR #26901, @jibi)
- Fix a bug in the Egress Gateway feature when using the --install-egress-gateway-routes option. Delete stale IP rules after a CiliumEgressGatewayPolicy is updated and selects a different egress network interface. (Backport PR #27069, Upstream PR #26846, @julianwiedmann)
- Fix a bug where datapath option DisableSipVerification can no longer be used. (#25533, @oblazek)
- Fix broken IPv6 access to native node devices due to wrong source IPv6 of NA response. (#25329, @jschwinger233)
- Fix bug in AlibabaCloud where instance type limits could not be determined (#25387, @haozhangami)
- Fix bug that caused transient IPsec packet drops on upgrades when tunneling is enabled. (Backport PR #26914, Upstream PR #26708, @pchaigno)
- Fix bug where bpf map entries may not be reliably dumped or garbage collected when the map is actively being updated. (Backport PR #26838, Upstream PR #26583, @tommyp1ckles)
- Fix bug with `toServices` policy where service backend churn left stale CIDR identities (#25687, @christarazi)
- Fix Cilium crash during network policy computation (#24322, @joestringer)
- Fix compilation error when enabling Wireguard and XDP (#25734, @ysksuzuki)
- Fix data race affecting the preferred mark in backends, e.g. backends selected by service with affinity set to local. In very rare cases a backend might be missing its preferred status and a non-local backend might be selected. (#25087, @joamaki)
- Fix enable-stale-cilium-endpoint-cleanup flag not actually disabling the cleanup init set when set to false. This provides a workaround for an existing panic that can occur when running using etcd kvstore. (#23874, @sjdot)
- Fix error propagation issue in clustermesh which prevented retrying on certain validation errors (Backport PR #26799, Upstream PR #26613, @giorio94)
- Fix failure to load the datapath for new pods on latest kernel when (almost) all datapath features are enabled. (#24405, @borkmann)
- Fix for Identities that can be deleted before CESs are reconciled (#25001, @dlapcevic)
- Fix issue where Cilium ServiceAPI would ignore backend changes to services with backends that were used in several services and updated at least once (#24474, @strudelPi)
- Fix issues that caused SPIRE not to install properly (#25160, @meyskens)
- Fix missed deletion events when reconnecting to/disconnecting from remote clusters (identities) (#25677, @giorio94)
- Fix missing metric "cilium_services_events_total" (Backport PR #27038, Upstream PR #26719, @christarazi)
- Fix operator entering broken state when it has outdated version of the CES in the cache. (Backport PR #27038, Upstream PR #26455, @alan-kut)
- Fix panic due to nil-map assignment in l2announcer (#26315, @dylandreimerink)
- Fix panic in hubble http v2 metrics (#24350, @chancez)
- Fix possible connection drops on agents restart when a service is associated with multiple endpointslices or has backends across multiple clusters (Backport PR #27038, Upstream PR #26912, @giorio94)
- Fix SNAT by the N/S load-balancer for fragmented IPv4 requests. (Backport PR #26636, Upstream PR #26550, @julianwiedmann)
- Fix some test failures for bpf_nat_test.c (#24534, @YutaroHayakawa)
- Fixed double metric accounting for k8s events (Backport PR #26636, Upstream PR #26349, @dylandreimerink)
- Fixed proxy redirect policy implementation when any deny rule prevents them. (Backport PR #26813, Upstream PR #26344, @jrajahalme)
- Fixes an issue where SRv6 encapsulated packets are forwarded to the wrong layer 2 next hop. (#26136, @ldelossa)
- Fixes issue in BGP reconciler when multiple pod cidr withdrawals are done. (#25320, @harsimran-pabla)
- helm: Fix a bug caused by incorrect indentation of the extraEnv parameter for Hubble UI backend (Backport PR #26914, Upstream PR #26797, @toVersus)
- ipam/azure: fix crash due to race condition when handling new node. (Backport PR #27038, Upstream PR #26658, @tommyp1ckles)
- iptables: Fix wrong use of podCIDR in cluster node NAT exclusion (#26397, @gandro)
- nat: fix usage in nat.h of csum.h module (#25576, @sahid)
- Policy auth precedence fix (Backport PR #26813, Upstream PR #26331, @jrajahalme)
- github: Fix chart push on forks (#25274, @chancez)
- bpf: test: fix pktgen for IPv6 NEXTHDR_DEST option (#26151, @julianwiedmann)
- bpf: Various fixes for `MAX_*_OPTIONS` and support for 5.10 (#24122, @pchaigno)
- CI Workflows: Fix matrix generation (#26406, @brlbil)
- CI Workflows: Fix sysdump file creation (#26402, @brlbil)
- CI Workflows: Fix sysdump name typo (#26415, @brlbil)
- ci-datapath: Fix issue where test were wrongly reported as passing (#24813, @gandro)
- cocci: Fix Python path for coccilib (#24430, @qmonnet)
- datapath/linux/route: fix CI expectations for rule string format (#24577, @NikAleksandrov)
- Fix broken target_url for conformance-clustermesh (#24315, @YutaroHayakawa)
- Fix execution of coccinelle checks (#24392, @qmonnet)
- Fix external-contribution-label workflow renovate tag (#25429, @chancez)
- Fix k8s podCIDRs for vagrant deployment (#22786, @romanspb80)
- Fix potential panic logic for checker.go (#22354, @yanggangtony)
- Fix verifier issues in IPv6 BPF tests (#25191, @dylandreimerink)
- Fixed flake in pkg/hive/job tests. (#25293, @dylandreimerink)
- Fixed TestTimer_ExitOnCloseFnCtx channel close panic (#25211, @dylandreimerink)
- gateway-api: Fix flaky conformance tests (#24317, @sayboras)
- gh/workflows: Fix encryption installation in ci-datapath (#23325, @brb)
- kvstore: fix TestWorkqueueSyncStoreMetrics flake (#25706, @giorio94)
- test/verifier: Fix compilation command (#24412, @pchaigno)
- workflows/datapath: Fix always-passing step (#24918, @pchaigno)
- workflows: Fix owner tag for stable branch workflows (#25158, @pchaigno)
- workflows: l4lb/verifier: fix skip-test-run job (#24072, @jibi)
- github: fix renovate docker image update (#23229, @aanm)
- github: fix renovate's config file (#23231, @aanm)
- [cilium cmd] fix wrong notes. (#22871, @yanggangtony)
- auth: fix initial k8s events sync in auth map gc (#26059, @mhofstetter)
- AWS CNI v1.12 Cilium install fixed. (#26084, @viktor-kurchenko)
- backporting: Fix pattern to handle commit subjects that begin with a space (#25653, @gentoo-root)
- bgpv1: Fix use of k8s.LocalNodeResource and LocalCiliumNodeResource types (#25615, @joamaki)
- bpf: dsr: fix IPIP health-encap on older kernels (Backport PR #26636, Upstream PR #26609, @julianwiedmann)
- bpf: Fix VTEP compilation error (#24152, @pchaigno)
- bpf: fixes for IPv6 revNAT (#24610, @julianwiedmann)
- bpf: nat: fix build error in snat_v6_prepare_state() (#26510, @julianwiedmann)
- bpf: nat: fix L4 csum case in ingress path for ICMP-embedded SCTP (#25315, @julianwiedmann)
- bpf: test: Fix the byte order in the IPV4 macro (#25114, @gentoo-root)
- bpf: Update IPv6 BPF masquerading code to bring it closer to IPv4's, fix SNAT for packets from local endpoints, for overlay (#26236, @qmonnet)
- bpf: xdp: fix coccicheck warning about DROP_MISSED_TAIL_CALL (#25924, @julianwiedmann)
- bug: Fix Potential Nil Reference in GetLabels Implementation (#24416, @nathanjsweet)
- Bump version in Readme and fix script (#24459, @aanm)
- Change enableEndpointCRD helm option type from string to boolean Fix operator panic that occurs when Endpoint CRD is disabled and CiliumEndpointSlice is enabled (#25798, @doniacld)
- clustermesh: fix broken test due to merge race (#26389, @giorio94)
- clustermesh: fix client usage when setting the cluster configuration (#24591, @giorio94)
- clustermesh: fix SyncedCanaries capability name mismatch (#25685, @giorio94)
- config: fix tunnel port for DSR-GENEVE with direct-routing (#25384, @julianwiedmann)
- contrib: Fix codegen script to avoid double make (#24718, @joestringer)
- contrib: Fix GitHub token check to allow fine-grained tokens (#22963, @gentoo-root)
- daemon/cmd: fix a couple of func doc string (#25030, @cuishuang)
- daemon: fix issue where IPAM options in custom CNI confs was ignored (Backport PR #26799, Upstream PR #26732, @squeed)
- daemon: fix spelling in ipam-multi-pool-pre-allocation flag usage (#26529, @tklauser)
- Documentation: Fix Envoy LB docs incorrect supported annotation values (Backport PR #27038, Upstream PR #26867, @rauanmayemir)
- egressgw: fix up removal for IP routes (Backport PR #27097, Upstream PR #26857, @julianwiedmann)
- endpoint: fix policy map sync warning due to policymap authtype diffs (#26218, @mhofstetter)
- Fix implicit conversion warning in DSR with GENEVE (#25299, @ysksuzuki)
- Fix "make -C Documentation builder-image" (Backport PR #26887, Upstream PR #26874, @michi-covalent)
- Fix a typo in pkg/option/config.go (#23731, @meyskens)
- Fix and improve Conformance Ginkgo UX (#25950, @aanm)
- Fix bug that causes traffic not to be encrypted when WireGuard node encryption is enabled. (#24903, @3u13r)
- Fix comment error about monitorNotify in `pkg/datapath/ipcache/listener.go`. (#23963, @hxysayhi)
- Fix fatal error when shutting down the clustermesh-apiserver (#25310, @giorio94)
- Fix hive test argument order and race (#25545, @bimmlerd)
- fix kind job with network policy failures (Backport PR #26799, Upstream PR #26639, @aojea)
- Fix kind.sh development scripts on MacOS (#25317, @chancez)
- Fix misleading use of bpf_ntohl (#24483, @lazybetrayer)
- Fix possible race condition in the clustermesh's users management test (#24652, @giorio94)
- Fix some map handling logic as well as some issues with CLI commands related to ip-masq-agent, introduced with IPv6 support (#26435, @qmonnet)
- Fix TLS policies after certificatemanager modularization (#23895, @tklauser)
- fix(deps): pin dependencies (main) (#25026, @renovate[bot])
- fix(deps): pin dependencies (main) (#25539, @renovate[bot])
- fix(deps): pin dependencies (main) (#25849, @renovate[bot])
- fix(deps): pin dependencies (master) (#24147, @renovate[bot])
- fix(deps): pin dependencies (master) (#24277, @renovate[bot])
- fix(deps): pin dependencies (master) (#24299, @renovate[bot])
- fix(deps): pin dependencies (master) (#24438, @renovate[bot])
- fix(deps): pin dependencies (master) (#24659, @renovate[bot])
- fix(deps): pin dependencies (master) (#24881, @renovate[bot])
- fix(deps): update all go dependencies main (main) (minor) (#26286, @renovate[bot])
- fix(deps): update all go dependencies main (main) (minor) (#26429, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#25035, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#25414, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#25542, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#26056, @renovate[bot])
- fix(deps): update all go dependencies main (main) (patch) (#26427, @renovate[bot])
- fix(deps): update all go dependencies master (master) (#23987, @renovate[bot])
- fix(deps): update all go dependencies master (master) (patch) (#23982, @renovate[bot])
- fix(deps): update all go dependencies master (master) (patch) (#24149, @renovate[bot])
- fix(deps): update all go dependencies master (master) (patch) (#24279, @renovate[bot])
- fix(deps): update all go dependencies master to v2 (master) (major) (#24110, @renovate[bot])
- fix: clean golang code for golint (#22665, @yulng)
- fix: Flag --ipv4-native-routing-cidr update in cli (#23643, @deepeshaburse)
- fix:'go routine' should be 'goroutine' (#22904, @yulng)
- fix:prevent goroutine leakage for pkg/k8s/watchers (#22362, @yulng)
- Fixed panic when generating code coverage report of eBPF tests (#24094, @dylandreimerink)
- fix：make fsnotify event more readable (#22903, @yulng)
- gha: fix conformance-ginkgo base branch retrieval (#26085, @giorio94)
- hive/jobs: fix enqueueing of multiple jobs via variadic func (#25633, @mhofstetter)
- hive: fix documentation for cell.Provide & cell.ProvidePrivate (#24238, @mhofstetter)
- hubble: fix Hubble Relay BASE_IMAGE (#23636, @kaworu)
- ipcache: fix not waiting for k8s caches to sync (#25975, @squeed)
- ipcache: Fix wrong assertion in ipcache metadata test (#23549, @christarazi)
- k8s/watchers: Fix calling Done() with proper error (#24616, @christarazi)
- k8s/watchers: Fix erroneous warning logs due to empty CIDRGroupRef (#25072, @christarazi)
- k8s/watchers: Fix race condition in init functions (#23170, @christarazi)
- k8s: fix ciliumpodippools CRD controller-gen version (#25976, @mhofstetter)
- operator: fix deadlock when running in kvstore mode (#24631, @giorio94)
- operator: Fix use of Resource.Events() in CEC controller (#22844, @joamaki)
- README.rst: Fix broken link to L7 policies (#24488, @PriyaSharma9)
- README.rst: Fix timezones in details for community meeting (#24520, @qmonnet)
- Renovate configuration fixes (#25330, @kaworu)
- renovate: fix config file format (#24109, @tklauser)
- resource: Fix flaky test due to missing Done call (#25646, @joamaki)
- Revert and fix ip rules (#25350, @NikAleksandrov)
- statedb: Fix WriteJSON with multiple tables (#24970, @joamaki)
- treewide: Fix code comment stutters (#24940, @joestringer)
- treewide: fix some shebangs (#26293, @markpash)
- versioncheck: fix parsing of snapshot release versions (#24286, @tklauser)

### 1.14.1

- Prevent Cilium from running with Delegated IPAM at the same time as Ingress (Backport PR #27238, Upstream PR #26744, @rickysumho)
- Fix a bug that affected the health-check feature in Stand-alone L4LB mode. For certain configurations (eg if both IPv4 and IPv6 support is enabled) health-check traffic would not get IPIP-encapsulated. (Backport PR #27190, Upstream PR #27015, @julianwiedmann)
- Fix a bug that affected the RevDNAT translation of IPv6 packets with extension headers. (Backport PR #27345, Upstream PR #27312, @julianwiedmann)
- Fix a bug that could cause packet drops of type XfrmOutPolBlock when IPsec is enabled and node are recycled
- Fix a bug that could cause IPsec-encrypted packets to be sent to the wrong destination node when node churn is high. (Backport PR #27238, Upstream PR #27029, @pchaigno)
- Fix agent panic in case malformed objects are retrieved from the kvstore, and improve validation (Backport PR #27345, Upstream PR #27237, @giorio94)
- Fix bug limiting pod-to-pod network performance under high load when tunneling and IPSec are both enabled. (Backport PR #27345, Upstream PR #27168, @learnitall)
- Fix bug where startup CIDR restore logic would mishandle reference counting, leading to persistent packet loss to those CIDRs (Backport PR #27419, Upstream PR #27327, @joestringer)
- Fix generation of the clustermesh config through Helm when kvstoremesh is enabled, and the TLS key/cert pair is manually specified for a given remote cluster (Backport PR #27238, Upstream PR #27177, @giorio94)
- Resolve a deadlock on startup when local redirect policies are used. (Backport PR #27238, Upstream PR #27115, @bimmlerd)
- Documentation: fix the broken links/dead links (Backport PR #27190, Upstream PR #26880, @vipul-21)
- fix: use proper helm param name for specifying pod cidr (Backport PR #27238, Upstream PR #27141, @yandzee)

### 1.14.2

- Fix: Affinity in cilium-pre-flight-check daemonset. (Backport PR #27629, Upstream PR #27475, @ishuar)
- cgroups: Fix race to load cgroup.hostRoot option (Backport PR #27629, Upstream PR #27561, @kvaps)
- envoy: fix panic writing accesslog without L7 tags (Backport PR #27629, Upstream PR #27453, @mhofstetter)
- Fix a bug that could cause an incorrect max. sequence number to be reported by `cilium encrypt status` when IPsec is enabled. (Backport PR #27917, Upstream PR #27656, @pchaigno)
- Fix a bug where cilium host IP is not read from k8s node annotations (Backport PR #27679, Upstream PR #27590, @hemanthmalla)
- Fix behavior where SPIRE doesn't work when kubelet does not listen on 127.0.0.1 (Backport PR #27679, Upstream PR #27583, @weizhoublue)
- Fix bug that could cause packet drops of type XfrmOutPolBlock while rotating the IPsec key. (Backport PR #27586, Upstream PR #27319, @jrfastab)
- Fix connectivity issues caused by missing conntrack entry when service pod connects to itself via clusterIP. (Backport PR #27920, Upstream PR #27602, @julianwiedmann)
- Fix deletion of tunnel map entries when node has non-zero cluster ID. (Backport PR #27629, Upstream PR #27353, @giorio94)
- Fix Gateway managed services not exposing all ports (Backport PR #27917, Upstream PR #27695, @Managarmrr)
- Fix global service incompatibility when v1.14 agents connect to a v1.13 cluster (#27882, @giorio94)
- Fix issue which caused the map reconciliation process to never complete successfully if the error resolved automatically (Backport PR #27629, Upstream PR #26742, @giorio94)
- Fix missing packet trace after `from-container` for reply traffic to the proxy. (Backport PR #27917, Upstream PR #27872, @pchaigno)
- Fix potential cross-node connectivity issue when IPsec is enabled with ENI or Azure IPAM modes. (Backport PR #27924, Upstream PR #26663, @gandro)
- Fix propagation of namespace labels to CEP labels (Backport PR #27917, Upstream PR #27831, @tklauser)
- Fix several paths in the North-South load-balancer where the TTL / hop-limit field of a forwarded packet was not updated. (Backport PR #27379, Upstream PR #27299, @julianwiedmann)
- Fixes a issue that IPsec key rotation can't be triggered. (Backport PR #27739, Upstream PR #27694, @jschwinger233)
- helm: fix envoy daemonset loglevel with multiple verbose debug groups (Backport PR #27917, Upstream PR #27698, @mhofstetter)
- ingress: fix panic on ingress rule without HTTPIngressRule (Backport PR #27917, Upstream PR #27818, @mhofstetter)
- IPSec fix for race on init resulting in Xfrm*In* errors and dropped packets (Backport PR #28021, Upstream PR #28012, @jrfastab)
- gha: fix waiting for images in conformance-gingko (Backport PR #27629, Upstream PR #27397, @giorio94)
- [v1.14] cilium: Fix 16bit ifindex limitation (#27880, @borkmann)
- Correct cni path in k3s installation documentation for rancher desktop (Backport PR #27739, Upstream PR #27702, @RichardoC)
- egressgw: small test fixes (Backport PR #27701, Upstream PR #27574, @lmb)

### 1.14.3

- bump grpc dependency to 1.56.3 to fix security vulnerability https://github.com/advisories/GHSA-qppj-fm5r-hxr3 (#28527, @aanm)
- bpf: overlay: fix missing DBG_DECAP for Inter-Cluster-SNAT (Backport PR #28494, Upstream PR #28466, @julianwiedmann)
- datapath: fix NodePort to remote hostns backend with tunnel config (Backport PR #28494, Upstream PR #27323, @michaelasp)
- envoy: Sync supported resources to fix not found issue (Backport PR #28349, Upstream PR #28272, @sayboras)
- Fix a bug that causes pod-to-pod traffic between nodes to be dropped when IPsec is enabled and kube-proxy installed rules in both iptables-nft and iptables-legacy. (Backport PR #28442, Upstream PR #28258, @pchaigno)
- fix bug: pull skb data in cil_from_netdev path for HIGH_SCALE_IPCACHE mode (Backport PR #28095, Upstream PR #27913, @sofat1989)
- Fix Gateway API HttpRoute cannot strip path prefix. (Backport PR #28282, Upstream PR #28018, @chaunceyjiang)
- Fix hubble metric labeling when only directed Source/Destination Ingress/Egress options are specified. (Backport PR #28095, Upstream PR #27792, @marqc)
- Fix minor bug where the previous Cilium proxy port was not reused (Backport PR #28127, Upstream PR #27634, @christarazi)
- Fix the trace notification for hairpinned reply traffic, to indicate the correct security identity for the client. (Backport PR #28282, Upstream PR #28133, @julianwiedmann)
- Fix wrong host and router IP being used for some IPv6 deployments, which was causing various connectivity problems. (Backport PR #28435, Upstream PR #28417, @ti-mo)
- Fix: Gateway API double slash while stripping path prefix (Backport PR #28442, Upstream PR #28294, @nxy7)
- Fixes a bug causing panic when counting IPsec keys number via "cilium encrypt status". (Backport PR #28282, Upstream PR #27996, @jschwinger233)
- fqdn proxy: fix data race by using separate sessionUDPFactories (Backport PR #28282, Upstream PR #28163, @mhofstetter)
- ipam/multipool: Fix bug where allocator was unable to update CiliumNode (Backport PR #28095, Upstream PR #27963, @gandro)
- ipcache: fix flapping labels in SelectorCache when reserved:host identity has multiple IPs (Backport PR #28418, Upstream PR #28332, @squeed)
- resource: Fix race condition in handling of Kubernetes object delete event retrying. In the very rare case when an object was created, deleted and re-created with the same name and the handling of the first deletion failed, the handling of delete event may have been retried even though the object was re-created. Only affected features using the Resource-library (LB IPAM, Mutual Auth and ClusterMesh). (Backport PR #28494, Upstream PR #27340, @joamaki)
- endpoint: Fix use of PolicyMapFullReconciliationInterval option (Backport PR #28095, Upstream PR #27985, @joamaki)
- Fix bug when reusing the same cell in multiple hives (Backport PR #28282, Upstream PR #27873, @giorio94)
- Fix potential nil pointer dereference in SelectorManager implementation (Backport PR #28095, Upstream PR #27805, @learnitall)
- fqdn proxy: fix data race detection on TCP fqdn proxy (Backport PR #28282, Upstream PR #28219, @mhofstetter)
- Fix possible cross-cluster connection drops on agents restart when clustermesh is enabled (#27611, @giorio94)

### 1.14.4

- policy: Fixed a bug that incorrectly omitted port-protocol policy rules that omitted the "protocol" field. An omitted "protocol" field now, correctly, is the same as using the "ANY" protocol. (Backport PR #28759, Upstream PR #28703, @nathanjsweet)
- envoy: fix lb backend endpoint calculation (Backport PR #28870, Upstream PR #27923, @mhofstetter)
- Fix CIDR labels computation (Backport PR #28870, Upstream PR #28788, @pippolo84)
- Fix concurrency issue when changing labels on pods started before Cilium setup their network. Cilium will now process pod labels modified while setting up the pod network. (Backport PR #28870, Upstream PR #28789, @aanm)
- Fix false positives of 'Key allocation attempt failed' in CRD mode (Backport PR #29064, Upstream PR #28810, @aanm)
- Fix incorrect logic used by the Ingress Controller to sync Cilium's IngressClass on startup. (Backport PR #28870, Upstream PR #28663, @learnitall)
- Fix IPsec error logs to always have all information needed to identify the XFRM configuration on which the error happened. (Backport PR #29030, Upstream PR #28642, @pchaigno)
- Fix issue causing KVStoreMesh metrics to be included in the dedicated Service/ServiceMonitor when KVStoreMesh is disabled (Backport PR #28759, Upstream PR #28481, @giorio94)
- fix: Correct spire labels identation in helm chart (Backport PR #28759, Upstream PR #28610, @sayboras)
- fixed cilium-operator delete CEC cilium-ingress when other ingressclass resources are created (Backport PR #28759, Upstream PR #28638, @chaunceyjiang)
- bpf: lb: fix missing drop reason in reverse_map_l4_port() (Backport PR #29030, Upstream PR #28884, @julianwiedmann)

### 1.14.5

- Avoid missed tail calls due to inserting policy programs too early during endpoint regeneration (#29308, @ti-mo)
- bpf: Fix drop of IPv6 reply traffic when 1) pod-originating connection is SNATed by iptables, and 2) Host Firewall is enabled. (Backport PR #29477, Upstream PR #28813, @oblazek)
- datapath: Fix ENI egress routing table for cilium_host IP (Backport PR #29390, Upstream PR #29335, @gandro)
- endpoint: fix panic in RunMetadataResolver due to send on closed channel (Backport PR #29251, Upstream PR #29615, @mhofstetter)
- Fix bug where deleted nodes would reappear in the cilium_node_connectivity_* metrics (Backport PR #29641, Upstream PR #29566, @christarazi)
- Fix external workloads not working with non-default ClusterID (Backport PR #29477, Upstream PR #29378, @giorio94)
- Fix possible disruption of long running, cross-cluster, pod to node traffic on agent restart (Backport PR #29641, Upstream PR #29613, @giorio94)
- Fix routing delegation to AWS-VPC-CNI when using the security groups feature. (Backport PR #29641, Upstream PR #29111, @Alex-Waring)
- Fix the Created timestamps in `cilium bpf nat list` that used to display the same values. (Backport PR #29187, Upstream PR #27062, @gentoo-root)
- Fixed label synchronization issues in Cilium, ensuring accurate representation of endpoint labels during restoration and addressing out-of-sync problems caused by label changes while the Cilium agent is down. (Backport PR #29251, Upstream PR #29248, @aanm)
- ingress: fix foreground deletion of Ingress (Backport PR #29477, Upstream PR #29367, @mhofstetter)
- ipam: Fix bug where IP lease did not expire (Backport PR #29641, Upstream PR #29443, @gandro)
- ipam: Fix bug where IP lease did not expire (Backport PR #29652, Upstream PR #29443, @gandro)
- metrics: fix potential conflict on metrics registration (Backport PR #29270, Upstream PR #27007, @ysksuzuki)
- metrics: fix potential conflict on metrics registration (Backport PR #29477, Upstream PR #27007, @ysksuzuki)
- ci-ipsec-upgrade: Fix upgrade/downgrade path and add missed tail calls check to upgrade (Backport PR #28876, Upstream PR #29072, @brb)
- [v1.14] CI: fix broken BPF complexity tests (#29553, @lmb)
- [v1.14] bgpv1: Fix BGP component tests using the same VirtualRouter config (#29453, @rastislavs)
- [v1.14] bpf: Fix identity determination in bpf_overlay.c (#29606, @ysksuzuki)

### 1.14.6

- [1.14] ingress: fix ingress class reconciliation (#29810, @mhofstetter)
- Fix a bug that may cause traffic to the node internal IP addresses to be incorrectly masqueraded when node encryption and remote node identities are both disabled, due to an inconsistency in the node manager when handling ipset entries insertions and deletions on node updates. (Backport PR #30221, Upstream PR #29986, @qmonnet)
- Fix and prevent future bugs limiting pod-to-pod network performance under high load when tunneling and IPSec are both enabled. (Backport PR #29996, Upstream PR #29616, @learnitall)
- Fix cleanup of AWS-related leftover iptables chains (Backport PR #29863, Upstream PR #29448, @giorio94)
- helm: Fix envoy servicemonitor annotations (Backport PR #30198, Upstream PR #30017, @pmcgrath)
- metrics: fix issue where logging err/warn metric is never updated. (Backport PR #29863, Upstream PR #29201, @tommyp1ckles)
- nodediscovery: Fix bug where CiliumInternalIP was flapping (Backport PR #29972, Upstream PR #29964, @gandro)
- policy: Fix mapstate changes error in entry change comparison (Backport PR #29996, Upstream PR #29815, @jrajahalme)
- Unify parsing of StringSlice flags and allow splitting by commas (preferably) or by spaces. This fixes parsing of 'prometheus.metrics'. (Backport PR #30080, Upstream PR #29848, @joamaki)
- bpf: fix test configuration for 5.10 and 6.1 kernels (Backport PR #30198, Upstream PR #29999, @julianwiedmann)
- datapath: Fix TestNodeChurnXFRMLeaks (Backport PR #30080, Upstream PR #27274, @brb)
- Fix collecting of verifier logs in ci-verifier (Backport PR #29863, Upstream PR #29752, @lmb)
- Fix bug preventing endpoint-related debug logs from being emitted (Backport PR #29829, Upstream PR #29495, @learnitall)
- Fix cilium-envoy ServiceMonitor template typo (Backport PR #30198, Upstream PR #29976, @cornfeedhobo)
- Fix log error in clustermesh-apiserver when connecting external workloads (Backport PR #29919, Upstream PR #29896, @giorio94)
- fix: remove help message in build config failure (Backport PR #30265, Upstream PR #28974, @vipul-21)
- resource: Fix flaky TestResource_RepeatedDelete (Backport PR #29996, Upstream PR #28588, @joamaki)
- [1.14] loader: fix obsolete XDP program removal (#30229, @rgo3)

### 1.14.7

- Fix all packet drops due to missed tail calls, enable zero tolerance for these errors in CI (Backport PR #30323, Upstream PR #30248, @ti-mo)
- Fix cilium-envoy ServiceMonitor port name (Backport PR #30554, Upstream PR #27207, @pixiono)
- Fix error when using multiple allowRoutes namespaces in gateway (#30551, @mhofstetter)
- Fix error when using multiple allowRoutes namespaces in gateway (Backport PR #30554, Upstream PR #30100, @chaunceyjiang)
- Fix issue where agent attempting to restore local node information (such as cilium_host ip) would fail on k8s fallback method. (Backport PR #30355, Upstream PR #29460, @tommyp1ckles)
- Fix nodeinit issue causing NotReady state in Kubernetes nodes when laying down an incorrect CNI config (Backport PR #30554, Upstream PR #30399, @tlcowling)
- Fix performance regression for pod-to-pod traffic WireGuard and tunneling. (Backport PR #30554, Upstream PR #30329, @3u13r)
- Fix rare bug possibly causing connection disruption and/or agent panic due to node events processing before full initialization. (Backport PR #30554, Upstream PR #30282, @giorio94)
- hive: Fix start hook log output (Backport PR #30724, Upstream PR #30712, @joamaki)
- init well-known identity before new policy repository to fix the fqdn policy issue when enable well-known identity. (Backport PR #30554, Upstream PR #30052, @yingnanzhang666)
- node/wireguard: Fix node-to-node encryption inconsistencies in kvstore mode (Backport PR #30534, Upstream PR #30423, @gandro)
- ci/ipsec: Fix version retrieval for downgrades to closest patch release (Backport PR #30554, Upstream PR #30503, @qmonnet)
- bpf: fib: fix issues with L2 resolution (Backport PR #30372, Upstream PR #30128, @julianwiedmann)
- hive: Fix hive hook output and move lifecycle to cell package (Backport PR #30554, Upstream PR #30416, @joamaki)
- Rerun go mod tidy to fix missing entry (#30358, @giorio94)
- [v1.14] ci/ipsec: Fix downgrade version for release preparation commits (#30716, @qmonnet)

### 1.14.8

- Fixes a bug where ToFQDN IPs may be garbage collected too early, disrupting existing connections. (Backport PR #31337, Upstream PR #31205, @squeed)
- endpoint: fix inability to create endpoint with labels in a single API call (Backport PR #31000, Upstream PR #30170, @oblazek)
- Fix bug prevented endpoints from sending or receiving network traffic due to the 'reserved:init' label persisting after initialization. (Backport PR #31048, Upstream PR #30909, @aanm)
- Fixes an IPv6 issue that cilium doesn't respond to Neighbor Solicitation targeting the pods on same node. (Backport PR #31186, Upstream PR #30837, @jschwinger233)
- Fixes an L7 proxy issue by re-introducing 2005 route table. (Backport PR #31160, Upstream PR #29530, @jschwinger233)
- Fixes proxy issues by opting out from SNAT for L7 + Tunnel. (Backport PR #31160, Upstream PR #29594, @jschwinger233)
- Fixes proxy issues in egress direction (Backport PR #31160, Upstream PR #30095, @jschwinger233)
- srv6: Fix packet drop with GSO type mismatch (Backport PR #30800, Upstream PR #30732, @YutaroHayakawa)
- Align again conformance clustermesh matrix entries with main as the interoperability issue has been fixed (#30912, @giorio94)
- ci/ipsec: Fix downgrade version retrieval (Backport PR #31048, Upstream PR #30742, @qmonnet)
- Fix datapath mode in Network Performance CI test (Backport PR #30864, Upstream PR #30756, @marseel)

### 1.14.9

- Fix a bug where pod label updates are not reflected in endpoint labels in presence of filtered labels. (Backport PR #31474, Upstream PR #31395, @tklauser)
- Hubble: fix traffic direction and is reply when IPSec is enabled (Backport PR #31569, Upstream PR #31211, @kaworu)
- controlplane: fix mechanism for ensuring watchers (Backport PR #31542, Upstream PR #31030, @bimmlerd)
- loader: fix issue where errors cancelled compile cause error logs. (Backport PR #31335, Upstream PR #30988, @tommyp1ckles)

### 1.14.10

- Fix overlapping keys in agent-side service BPF map cache used for retries. In rare cases this bug may have caused retrying of a failed BPF map update for a services entry to be skipped leading to a missing entry. This may have, for example, adversely affected recovering from a full BPF service map after excess services were removed. (Backport PR #31888, Upstream PR #29581, @xyz-li)
- cilium-health: Fix broken retry loop in `cilium-health-ep` controller (Backport PR #31724, Upstream PR #31622, @gandro)
- fix: Delegated ipam not configure ipv6 if ipv6 disabled in agent (Backport PR #31724, Upstream PR #31104, @tamilmani1989)
- Fixed a race condition in service updates for L7 LB. (Backport PR #31861, Upstream PR #31744, @jrajahalme)
- Fixed issue with assigning 0 nodeID when corresponding bpf map run out of space. Potentially it could have impacted connectivity in large clusters (>4k nodes) with IPSec or Mutual Auth enabled. Otherwise, it was merely generating unnecessary error log messages. (Backport PR #31656, Upstream PR #31380, @marseel)
- fqdn: Fix minor restore bug that causes false negative checks against a restored DNS IP map. (#31871, @nathanjsweet)
- fqdn: Fixed bug that caused DNS Proxy to be overly restrictive on allowed DNS selectors. (#31801, @nathanjsweet)
- bitlpm: Document and Fix Descendants Bug (Backport PR #31888, Upstream PR #31851, @nathanjsweet)
- Fix spelling in DNS-based proxy info (Backport PR #31888, Upstream PR #31728, @saintdle)
- [v1.14] fix unsupported aws region (#31742, @brlbil)

### 1.14.11

- dnsproxy: Fix bug where DNS request timed out too soon (Backport PR #32251, Upstream PR #31999, @gandro)
- Fix failing service connections, when the service requests are transported via cilium's overlay network. (Backport PR #31797, Upstream PR #32116, @julianwiedmann)
- Fixes a bug where Cilium in chained mode removed the `agent-not-ready` taint too early if the primary network is slow in deploying. (Backport PR #32251, Upstream PR #32168, @squeed)
- Fixes an (unlikely) bug where HostFirewall policies may miss updates to a node's labels. (Backport PR #32385, Upstream PR #30548, @squeed)
- fqdn: fix memory leak in transparent mode when there was a moderately high number of parallel DNS requests (>100). (Backport PR #32104, Upstream PR #31959, @marseel)
- operator: fix errors/warnings metric. (Backport PR #31907, Upstream PR #31214, @tommyp1ckles)
- workflows: Fix CI jobs for push events on private forks (Backport PR #32251, Upstream PR #32085, @pchaigno)
- fqdn: Fix Upgrade Issue Between PortProto Versions (Backport PR #32385, Upstream PR #32325, @nathanjsweet)
- fix k8s versions tested in CI (cilium/cilium#31969, @nbusseneau)

### 1.14.12

- github/workflows: fix digests file creation (Backport PR #32888, Upstream PR #32860, @aanm)
- Fix PromQL query in Cilium Metrics dashboard (Backport PR #32695, Upstream PR #32017, @mikemykhaylov)
- Fix rare race condition afflicting clustermesh when disconnecting from a remote cluster, possibly causing the agent to panic (Backport PR #32695, Upstream PR #32513, @giorio94)
- Fix: Ensure enabling metrics turns on identity GC metrics (cilium/cilium#32447, @jaredledvina)
- Fixes accidentally ignoring the preflight.nodeSelector Helm value. (Backport PR #32695, Upstream PR #32548, @squeed)
- background-sync: fix bootstrap issue and edge-case with 1 node (Backport PR #32874, Upstream PR #32630, @marseel)
- [1.14-backport] ipsec: Fix unencrypted traffic when IPsec is used with L7 egress proxy (cilium/cilium#31976, @jschwinger233)

### 1.14.13

- Fix service connection to terminating backend, when the service has no more backends available. (Backport PR #32093, Upstream PR #31840, @julianwiedmann)
- Fix too many open Unix sockets (Backport PR #33632, Upstream PR #33569, @chaunceyjiang)
- IPv6 and IPv4 '0.0.0.0/0' CIDR parsing in policy processing has been fixed (Backport PR #33530, Upstream PR #33448, @jrajahalme)
- github: fix cloud workflows for renovate (Backport PR #33322, Upstream PR #33320, @aanm)
- github: fix worfklows used by renovate (Backport PR #33316, Upstream PR #33309, @aanm)
- github: fix workflows for on push (cilium/cilium#33369, @aanm)
- examples: Fix subject selector in ingress policy (Backport PR #33377, Upstream PR #33292, @joestringer)
- Fix renovate's concurrency group (Backport PR #33561, Upstream PR #33528, @aanm)
- ipcache: Fix orphaned ipcache entries when mixing Upsert and Inject (Backport PR #33270, Upstream PR #33120, @squeed)
- LRP: Misc fix-ups (Backport PR #33530, Upstream PR #33442, @aditighag)
- github: fix concurrency groups for push events (cilium/cilium#33645, @aanm)

### 1.14.14

- Fix bug causing etcd upsertion/deletion events to be potentially missed during the initial synchronization, when Cilium operates in KVStore mode, or Cluster Mesh is enabled. (Backport PR #34184, Upstream PR #34091, @giorio94)
- Fix rare race condition afflicting clustermesh while stopping the retrieval of the remote cluster configuration, possibly causing a deadlock (Backport PR #33815, Upstream PR #33735, @giorio94)
- pkg/metrics: fix data race warning on metrics init hook. (Backport PR #33963, Upstream PR #33823, @tommyp1ckles)
- Fix IPSec XfrmInStateProtoError errors on agent restart in cluster pool IPAM mode (cilium/cilium#34030, @dylandreimerink)

### 1.14.15

- config: fix disabling config 'Debug' (Backport PR #34471, Upstream PR #34401, @mhofstetter)
- envoy: fix log level mapping when changing log level via API (Backport PR #34459, Upstream PR #34400, @mhofstetter)
- ipcache: Yet another refcounting fix with mix of APIs (Backport PR #34713, Upstream PR #34715, @gandro)
- Fix: push PR changes when renovate build images under the workflow_call context (Backport PR #34829, Upstream PR #34650, @Artyop)
- fix: base image update workflow will now be triggered on renovate branches with a workflow_call event type (Backport PR #34459, Upstream PR #34372, @Artyop)
- images: fix path script (Backport PR #34766, Upstream PR #34764, @aanm)

### 1.14.16

- datapath: Fix redirect from from L3 netdev to tunnel (Backport PR #35265, Upstream PR #33421, @brb)
- Fixed bug in tracking policy changes that could have resulted in revert not woking in failure cases as expected. (Backport PR #35279, Upstream PR #35109, @jrajahalme)
- Fixed bug where service id allocator would loop infinity when out of service ids (Backport PR #35279, Upstream PR #35033, @WeeNews)
- Fixes startup fatal error when updating CiliumNode resource. (Backport PR #34916, Upstream PR #34862, @harsimran-pabla)
- github/lint-build-commits: fix workflow for push events (Backport PR #35279, Upstream PR #35264, @aanm)
- fix: repository nil value handled on workflow_dispatch context for renovate updates (Backport PR #34916, Upstream PR #34902, @Artyop)
- github: fix build image process to commit changes (Backport PR #35279, Upstream PR #35262, @aanm)
- github: fix lvh-kind warnings (Backport PR #35176, Upstream PR #34811, @aanm)
- github: fix runtime image digests (Backport PR #35119, Upstream PR #35107, @aanm)

### 1.14.17

- [v1.14] gha: fix incorrect go version in lint-build-commits workflow (cilium/cilium#35313, @giorio94)
- dnsproxy: fix error when sessionUDPFactory fails (Backport PR #35588, Upstream PR #33998, @marseel)

### 1.14.19

- github: fix conformance-k8s NP test (Backport PR cilium/cilium#36519, Upstream PR cilium/cilium#36355, @aanm)
- Fix `make -C Documentation update-cmdref` when make uses `--jobserver-style=fifo`. (Backport PR cilium/cilium#36870, Upstream PR cilium/cilium#36788, @gentoo-root)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.14.19**, the newest release recorded here for this line.

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
