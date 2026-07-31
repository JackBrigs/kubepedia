---
id: TROUBLE-CILIUM_1_11_DEFECTS
type: troubleshooting
title: "cilium 1.11: defects fixed in the 1.11 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.11.0 <1.12.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.11 known issues
  - cilium 1.11 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.11 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.11: defects fixed in the 1.11 line

## Summary

**327 defects** the project fixed across **21 releases** of the 1.11 line, from 1.11.0 to
1.11.20. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.11.0

- Fixes connectivity issues when kube-proxy replacement is enabled, caused by ineffective socket based load balancing (aka host reachable services) in the private cgroup namespace mode of container runtimes (e.g., docker cgroupv2 configuration). (#16259, @aditighag)
- bpf: fix hw_csum issue for icmp probe packets (#16604, @borkmann)
- bpf: fix iptables masquerading for node -> remote pod traffic (#16136, @jibi)
- bug/pkg/health: Fix Nil Address Issue in Node Update Mechanism (#17667, @nathanjsweet)
- bugtool: fix data race occurring when running commands (#17916, @rolinh)
- bugtool: fix IP route debug gathering commands (Backport PR #18076, Upstream PR #18059, @tklauser)
- cilium: Encryption EKS 4.14 kernel (default) fixes (#15867, @jrfastab)
- daemon, node: Fix faulty router IP restoration logic (#16672, @christarazi)
- egress gateway: fix non-tunnel (direct routing) mode (#17517, @kkourt)
- egressgateway: fix manager logic (Backport PR #18027, Upstream PR #17813, @jibi)
- eni: Fix Cilium overallocating network interfaces (#15911, @gandro)
- Envoy configuration is fixed to work also when IPv6 is disabled. (#17281, @rock-andy)
- Envoy configuration with `--proxy-prometheus-port` is fixed. (#16834, @jrajahalme)
- Fix "unable to update ipcache map entry on pod add" harmless log warnings (#16286, @aanm)
- Fix 5.10+ complexity issue with `kubeProxyReplacement=disabled` (#16084, @pchaigno)
- Fix a crash where user specifies incorrect service name in a local redirect policy config, or policy selected service is added after the policy is added. (#16216, @aditighag)
- Fix aws-cni integration where pods were not being scheduled (#15915, @aanm)
- Fix bug where Cilium allocates a new router (`cilium_host`) IP upon node reboot, breaking connectivity especially with IPsec (#16307, @christarazi)
- Fix bug where IP addresses of devices in unknown state are resolved as remote-node (#17418, @jibi)
- Fix bug where L7 ingress policies with IPsec dropped traffic in tunneling mode (#16057, @christarazi)
- Fix bug where the agents would silently skip all IPv6 masquerading due to an incorrect configuration. (#17906, @pchaigno)
- Fix bug where timers used for retries sometimes fired immediately (#16955, @gandro)
- Fix bug where users were unable to use node-selectors in the BGP configuration when using BGP support (#16341, @christarazi)
- Fix bug with Helm chart where a user could not enable BGP and set Operator resources. (#16273, @rkage)
- Fix identity leak via FQDN selectors (#17699, #17788, @joestringer)
- Fix incorrect application of egress gateway policy to internal cluster traffic. Require a 5.2 kernel or later for the egress gateway policy feature. (#17639, @kkourt)
- Fix incorrect packet path with IPsec and endpoint routes, which can cause incorrect policy drops. (#17000, @pchaigno)
- Fix issue where generating Hubble certs were broken (#16509, @alex1989hu)
- Fix issue where local host IPs may be briefly associated with the remote-node identity, causing policy drops when policy should allow traffic from the host. (#17836, @joestringer)
- Fix Linux slave interface detection (#17189, @pchaigno)
- Fix memory leak that can occur with the presence of FQDN policies (#17432, @aanm)
- Fix several complexity and program size issues when only one of IPv4/IPv6 is enabled. (#17573, @pchaigno)
- Fix transient policy deny during agent restart (#17115, @jaffcheng)
- Fixed bug causing policy realization being skipped in some scenarios with endpoint identity churn. (#16271, @jrajahalme)
- Fixes a bug where IPv6 pod CIDRs with leading zeros where not supported (#17707, @gandro)
- Fixes an issue which can cause traffic to be dropped when running Cilium in ENI mode due to the presence of iptables rules left over by the AWS VPC CNI plugin. Notable features that could be impacted include the egress gateway functionality. (#17845, @bmcustodio)
- Fixes for IPsec and endpoint routes (#17865, @kkourt)
- Fixes out-of-sycn CEP update (#17001, @Weil0ng)
- helm: Fix operator cloud image digests (Backport PR #18119, Upstream PR #18116, @joestringer)
- helm: Fix patch failure when updating `hubble-generate-certs` (#16373, @gandro)
- hubble/recorder: Refactor service implementation to fix multiple races (#16472, @gandro)
- ipam/crd: Fix spurious "Unable to update CiliumNode custom resource" failures in cilium-agent (Backport PR #18027, Upstream PR #17856, @gandro)
- ipsec: Fix logging of SPI after key rotations (#16557, @pchaigno)
- ipsec: Fix off-by-one error on max keyID (#16647, @pchaigno)
- L7 proxy redirection on IPv6 ingress to a pod is fixed to properly update IPv6 hop limit. (#17718, @jrajahalme)
- lbmap: fix deletion and recreation logic for maglev maps (#16850, @jibi)
- node: Fix race condition on labels' getter/setter (#17217, @pchaigno)
- pkg/k8s: fix invalid memory address or nil pointer dereference (#17642, @aanm)
- pkg/option: Fix default assignment of EnableWellKnownIdentities (#16434, @mauriciovasquezbernal)
- policy: Fix `cilium policy trace` output when only deny rules are applied (#16991, @chez-shanpu)
- Potential deadlock in pod identity updates has been fixed. (#16529, #16801, @jrajahalme)
- routing: Fix incorrect interface selection for egress pod routes (#17169, @pchaigno)
- ui envoy: fix config to keep grpc conn (#15938, @geakstr)
- wireguard: Fix traffic counters in `cilium debuginfo` (#16178, @gandro)
- github: Fix codeQL workflow skip logic (#17587, @joestringer)
- github: Fix concurrency group comment triggers (#16310, @pchaigno)
- github: Fix error triggered by large comments (#16360, @pchaigno)
- github: Fix scheduled end-to-end tests (#16274, @pchaigno)
- github: Fix smoke tests sysdump collection from failing prematurely (#17032, @christarazi)
- aks: fix AKS cluster creation following new taint limitations (#17529, @nbusseneau)
- checkpatch: update to lastest image to fix checkpatch exit status (#17450, @qmonnet)
- ci-multicluster: Fix post-test information gathering (#16712, @gandro)
- ci/conformance: Various image-related fixes (#16715, @gandro)
- Fix and add more commands in CI sysdumps (#16721, @aanm)
- Fix Azure-related data races (#17054, @christarazi)
- Fix kubectl CI flakiness (Backport PR #18109, Upstream PR #18087, @aanm)
- hubble/relay: Fix close of closed channel in unit test (#16958, @gandro)
- jenkinsfiles: fix race detector pipelines (#16056, @nbusseneau)
- node-neigh: Fix concurrent arping update unit test flake (#16578, @brb)
- node-neigh: Fix unit test flake (#16072, @brb)
- rate: fix TestStressRateLimiter when run with race detector (#16262, @tklauser)
- test/helpers: Fix incorrect count of endpoints (#16437, @pchaigno)
- test/helpers: Fix panic due to missing CEP status (#16443, @pchaigno)
- wireguard: Fix timeout in unit test (#16001, @gandro)
- workflows: fix build-and-push-with-qemu on v1.11 (#18071, @nbusseneau)
- workflows: Fix change detection of comment-triggered jobs (#17171, @pchaigno)
- workflows: fix concurrency group names (#16711, @nbusseneau)
- workflows: Fix Hubble flow capture in smoke tests (#17137, @pchaigno)
- workflows: fix L4LB test missing PR reporting on issue_comment (#16830, @nbusseneau)
- workflows: fix permissions (#17008, @nbusseneau)
- workflows: fix Relay pgrep check when using additional flags (#16831, @nbusseneau)
- workflows: Fix use of paths-filter on master pushes (#16507, @pchaigno)
- workflows: various fixes & consistency passes (#16787, @nbusseneau)
- workflows: various small fixes (#16311, @nbusseneau)
- github: Fix image digest job printing (#16660, @joestringer)
- github: fix MLH configuration file for v1.11 branch (#18032, @aanm)
- Avoid transitive dependency on github.com/miekg/dns in policy API (#16806, @tklauser)
- bpf: Fix reset of CB_PROXY_MAGIC (#17592, @jrajahalme)
- bpf: Fix stale map removal in agent logs (Backport PR #18027, Upstream PR #17973, @borkmann)
- bwm: queue mapping & cong fixes (#15964, @borkmann)
- checkpatch: update image to fix checks on commit object and message (#17067, @qmonnet)
- cilium: fix ipv6 neighbor discovery (#17842, @borkmann)
- clustermesh: fix CEP status patch (#16986, @nbusseneau)
- codeql: Fix GitHub Action permissions (#17376, @twpayne)
- contrib: Fix bump-readme.sh script (#17311, @joestringer)
- contrib: fix dual-stack support in dev VMs (#15887, @aanm)
- contrib: Fix scripts for v1.10 (#15898, @joestringer)
- contrib: Fix submit-release.sh regression (#17607, @joestringer)
- correct comment Service6Key and Service4Key (#17271, @ChenYahui2019)
- daemon: fix race in config handler (#17413, @h3llix)
- docs, bpf: fix llvm-objdump --no-show-raw-insn options (#16848, @ClaudiaJKang)
- Documentation/gettingstarted: fix helm arguments (#17496, @AlexZzz)
- examples: Fix up standalone-etcd.yaml (#17369, @joestringer)
- Fix alias of cilium-health get (#16891, @xyz-li)
- Fix documented EC2 IAM action (Backport PR #18076, Upstream PR #17958, @austince)
- Fix encryption getting started guides for v1.10 (#15961, @jibi)
- Fix label shown as Unknown App in hubble ui for http-sw-app example (#17597, @hemslo)
- Fix logging for expired FQDN IPs (#16030, @youssefazrak)
- fix warning log for list IPV6 address: move IPV4 to IPv6. (#16475, @lic17)
- fix(docs): bandwidth-manager install error (#17338, @withlin)
- Fixed a minor race condition on drop counts when hubble starts drops flows/events, because of a full channel. This change also will log the fact that drops are happening once, rather than a log message for every drop, and will log an additional comment after drops are no longer happening with the number of events/flows that were dropped. (#15967, @nathanjsweet)
- github: Fix external workloads test file syntax (#17019, @brb)
- health: Fix cluster-health-port for health endpoint (Backport PR #18076, Upstream PR #18061, @gandro)
- helm: Fix hubble-ui clusterrole guard (#17846, @gandro)
- hubble: Fix data races in `pkg/hubble.TestRingReader_NextFollow_WithEmptyRing` (#17397, @gandro)
- install/kubernetes: fix helm generation for operator image digest (Backport PR #18027, Upstream PR #17968, @aanm)
- install: Fix hubble-ui-backend digest tracking (#15900, @joestringer)
- install: Fix README links to getting started guides (#16947, @joestringer)
- ipam/allocator/podcidr: fix old pod cidr logging error (#17372, @lrouter)
- issue_14922: Fixed the 429 response code handling (#15760, @Maddy007-maha)
- Minor fixes for OKD GSG (#16000, @errordeveloper)
- monitor: Fix mismatching frontend service debug trace types (#16953, @christarazi)
- option: Fix ipvlan master device config (#17130, @joestringer)
- pkg/kvstore: fix concurrent access of var in testing (#16427, @aanm)
- pkg/kvstore: fix TestRunLocksGC unit test (#16596, @aanm)
- proxylib/test: fix data race between StartAccessLogServer and Close (#16298, @tklauser)
- proxylib: Fix data races in unit tests (#17141, @gandro)
- README: fix the Weekly Community Meeting time (#17215, @tixxdz)
- treewide: Fix problems identified by CodeQL (#17516, @twpayne)

### 1.11.1

- daemon: Fix KPR init finalisation (Backport PR #18418, Upstream PR #18304, @brb)
- daemon: Fix multi-dev XDP check (Backport PR #18364, Upstream PR #18305, @brb)
- egressgateway: fix initial reconciliation (Backport PR #18418, Upstream PR #18325, @jibi)
- identity: fix incorrect maximum identity when ClusterID > 0 (Backport PR #18232, Upstream PR #18148, @ArthurChiao)
- Fix an issue where the tunnel map sync controller causes errors even though tunneling is disabled. (Backport PR #18275, Upstream PR #18247, @tklauser)
- Fix crash on startup if proxy is disabled (Backport PR #18275, Upstream PR #18198, @chaosbox)
- Fix deadlock with kube-apiserver policy matching feature (Backport PR #18418, Upstream PR #18343, @codablock)
- Fix for a bug where unused IPs on the node cannot be allocated when IP release handshake is enabled. Adds support for aborting IP release, if the node doesn't have excess anymore. (Backport PR #18418, Upstream PR #18330, @hemanthmalla)
- Fix for data race in IP release features (Backport PR #18232, Upstream PR #18217, @hemanthmalla)
- Fix for excess IP release race condition. New operator flag excess-ip-release-delay is introduced to control waiting period before marking an IP for release. (Backport PR #18232, Upstream PR #17939, @hemanthmalla)
- Fix possible IP leak in case ENI's are not present in the CN yet (Backport PR #18418, Upstream PR #18352, @codablock)
- Fix TCP connectivity issues in the DSR mode when conntrack entries with missing DSR flag are reused. (Backport PR #18275, Upstream PR #18041, @Inode1)
- helm: Fix Helm template for externalWorkloads (Backport PR #18275, Upstream PR #18206, @gandro)
- hubble: Fix misclassification of `to-network` reply packets (Backport PR #18275, Upstream PR #18196, @gandro)
- policy: Fix selector identity release for FQDN (Backport PR #18232, Upstream PR #18166, @joestringer)
- test/helpers: fix kubectl version detection for RCs (Backport PR #18232, Upstream PR #18133, @tklauser)
- bpf: Reset Pod's queue mapping in host veth to fix phys dev mq selection (Backport PR #18418, Upstream PR #18388, @borkmann)
- Fix helm chart annotations for CRDs installed by Cilium (Backport PR #18364, Upstream PR #18141, @joestringer)
- install: Fix hubble-ui image references (Backport PR #18232, Upstream PR #18209, @joestringer)
- k8s: Fix CRD schema version for v2alpha1 (Backport PR #18275, Upstream PR #18215, @joestringer)

### 1.11.2

- clustermesh-apiserver: fix cmd-line args processing (Backport PR #18726, Upstream PR #18277, @abocim)
- cmd: Fix issue reading string map type via config map (Backport PR #18726, Upstream PR #18478, @sayboras)
- daemon: Fix missing errors in KPR init (Backport PR #18630, Upstream PR #18499, @brb)
- Fix `bpf lb maglev list` command when ipv4 or ipv6 Maglev lookup tables are empty (Backport PR #18630, Upstream PR #18469, @ti-mo)
- Fix a bug with local redirect policies selecting host networked pods as local endpoints not taking effect. (Backport PR #18726, Upstream PR #18563, @aditighag)
- Fix BPF attachment when bandwidth manager is enabled without host firewall or kube-proxy-replacement. (Backport PR #18780, Upstream PR #18717, @pchaigno)
- Fix bug where Cilium drops traffic from remote nodes in etcd mode, despite policy that allows the traffic (Backport PR #18800, Upstream PR #18777, @joestringer)
- Fix bug where Hubble flows report that a packet is both forwarded and dropped by host firewall. It will now only report the drop. (Backport PR #18630, Upstream PR #18484, @YutaroHayakawa)
- Fix incorrect packet trace for encrypted packets received from the network (Backport PR #18726, Upstream PR #18643, @YutaroHayakawa)
- Fix kube-apiserver policy matching feature with tunneling enabled (Backport PR #18669, Upstream PR #18527, @christarazi)
- Fix the bug that ipsec packets bypass the <- stack trace after encryption (Backport PR #18669, Upstream PR #18608, @YutaroHayakawa)
- Prevent unmanaged pods in GKE's containerd flavors. (Backport PR #18726, Upstream PR #18486, @bmcustodio) *Important:* Users should update their node taints from `node.cilium.io/agent-not-ready=true:NoSchedule` to `node.cilium.io/agent-not-ready=true:NoExecute`. *Important:* During the first node reboot after the fix is applied pods may still get IPs from the default CNI as cilium-node-init is only run later in the node startup process. The fix will then be in place for all subsequent reboots
- Fix EncryptStatusSuite.TestCountUniqueIPsecKeys (Backport PR #18569, Upstream PR #18506, @tklauser)
- test/runtime: fix flake on non-ready endpoints (Backport PR #18669, Upstream PR #18627, @tklauser)
- Alibabacloud fixes (Backport PR #18836, Upstream PR #18762, @jaffcheng)
- contrib: Fix backport submission for own PRs (Backport PR #18569, Upstream PR #17988, @joestringer)
- contrib: Fix release script helm value generation (Backport PR #18630, Upstream PR #18538, @joestringer)
- iptables: Fix race condition on ipset removal (Backport PR #18836, Upstream PR #18790, @pchaigno)
- node: Fix bug where node ipsets are never cleaned (Backport PR #18630, Upstream PR #18582, @pchaigno)

### 1.11.3

- Fixes L7 policies with Azure CNI chaining. (Backport PR #19142, Upstream PR #19088, @nitishm)
- Add missing & fix wrong traces for IPSec + overlay receive path (Backport PR #18905, Upstream PR #18731, @YutaroHayakawa)
- Avoid deleting in-use program arrays in bpf_load() and bpf_load_cgroups() in init.sh (Backport PR #19066, Upstream PR #18985, @ti-mo)
- clustermesh: fix: identities allocation range (Backport PR #19142, Upstream PR #19076, @abocim)
- datapath/config: Fix L2 addr retrieval (Backport PR #19142, Upstream PR #19081, @brb)
- Fix 'node-init' in GKE's 'cos' images. (Backport PR #19142, Upstream PR #19017, @bmcustodio)
- Fix a bug where Cilium would constantly create network interfaces if IPAM limits are reached (Backport PR #19142, Upstream PR #18975, @michi-covalent)
- Fix bug where FQDN policy calculation could trigger a deadlock in cilium-agent (Backport PR #19142, Upstream PR #19031, @joestringer)
- Fix bug where unnecessary ipset was created and populated in tunneling mode with iptables masquerading. (Backport PR #18905, Upstream PR #18788, @pchaigno)
- Fix concurrency issue while waiting for node-init DaemonSet to be ready (Backport PR #19142, Upstream PR #18897, @aanm)
- Fix connectivity outage periods with ENI IPAM mode and IPsec enabled when nodes are deleted from the cluster (Backport PR #18905, Upstream PR #18827, @christarazi)
- Fix IPsec in Azure's IPAM mode (Backport PR #19142, Upstream PR #18911, @pchaigno)
- Fix issue where StatefulSet pod restarts could trigger persistent connectivity issues for the pods due to overzealous CiliumEndpoint resource removal by cilium-agent instances (Backport PR #19142, Upstream PR #18864, @timoreimann)
- Fix support of BPF-based HostPort on init containers. (Backport PR #18905, Upstream PR #18725, @pchaigno)
- Fixed a bug where deleted identities would remain in BPF policy maps. (Backport PR #19142, Upstream PR #19005, @jrajahalme)
- pkg/maps: Fix data races around accessing nat maps (Backport PR #19142, Upstream PR #18952, @aditighag)

### 1.11.4

- bpf: Fix maglev hash with hostServices.hostNamespaceOnly (Backport PR #19277, Upstream PR #18336, @ysksuzuki)
- cmd: Fix issue where a ConfigMap value of `{}` was parsed as `map["{}":""]`. (Backport PR #19277, Upstream PR #19172, @gandro)
- Fix a bug where a backend pod can be selected by a local redirect policy deployed in a different namespace if the local redirect policy was deployed first. (Backport PR #19277, Upstream PR #19193, @aditighag)
- Fix bug that would cause some pod traffic to leave through the wrong interface if --aws-release-excess-ips is used and masquerading disabled. (Backport PR #19277, Upstream PR #19162, @pchaigno)
- Fix bug where the 'ipcache-inject-labels' controller constantly fails in non-Kubernetes environments (Backport PR #19277, Upstream PR #19165, @christarazi)
- Fix bug where the Cilium DNS proxy slows down significantly (and even OOMs) due to lock contention from spawning many goroutines when handling bursty DNS traffic (Backport PR #19418, Upstream PR #19336, @nebril)
- Fix log rotation of compressed logs (Backport PR #19277, Upstream PR #19152, @chancez)
- Fixed node init in RKE (Backport PR #19418, Upstream PR #19286, @raphink)
- install/kubernetes: fix hubble-ui with TLS (Backport PR #19418, Upstream PR #19338, @aanm)
- metallb: fix SIGSEGV error when Service resource is deleted. (Backport PR #19277, Upstream PR #19249, @Inode1)
- Bpf fix conditional compilation (Backport PR #19277, Upstream PR #19104, @jrajahalme)
- logo: fix position of central polygon (Backport PR #19277, Upstream PR #19216, @sisp)
- wireguard: Fix invalid bits when agent init (Backport PR #19277, Upstream PR #19118, @Junnplus)

### 1.11.5

- clustermesh-apiserver: fixed nil pointer dereference (Backport PR #19752, Upstream PR #18957, @abocim)
- Fix drop for packets sent via AF_PACKET + mmap ring buffer in pod (Backport PR #19481, Upstream PR #19308, @liuyuan10)
- Fixed Cilium agent regression causing a crash due to ipcache controller being scheduled too soon. (Backport PR #19573, Upstream PR #19501, @jrajahalme)
- operator: fix identity GC collection (Backport PR #19671, Upstream PR #19649, @aanm)

### 1.11.6

- datapath: Fix implicit-int-conversion err in common.h (Backport PR #19966, Upstream PR #19832, @brb)
- Fix bug where established host connections would be interrupted on agent restart if the host firewall was enabled. (Backport PR #20111, Upstream PR #19998, @pchaigno)
- Fix memory leak in the DNS cache when a long-lived endpoint makes many unique DNS lookups over time (Backport PR #20111, Upstream PR #19925, @christarazi)
- Fix race condition leading to inconsistent CiliumNode that can cause the agent to fatal. (Backport PR #20111, Upstream PR #19923, @pchaigno)
- metrics: Fix NaN value for cilium metrics list CLI (Backport PR #20111, Upstream PR #19987, @sayboras)

### 1.11.7

- bug: Fixed a rare CiliumIdentity race deletion. (Backport PR #20364, Upstream PR #19936, @nathanjsweet)
- cilium: fix conflicting iptables-legacy and iptables-nft rules (Backport PR #20364, Upstream PR #20123, @jrfastab)
- daemon, option: Fix vlan bpf bypass ids loading (Backport PR #20412, Upstream PR #20282, @pippolo84)
- daemon: Fix issue where stale router IPs were not cleaned up (Backport PR #20412, Upstream PR #20389, @gandro)
- datapath: Fix security ID propagation in tunnel header for NodePort BPF forwarded requests (Backport PR #20301, Upstream PR #19061, @brb)
- Fix agent panic in some cases when service matcher local redirect policy was deployed prior to the selected service. (Backport PR #20263, Upstream PR #19522, @aditighag)
- Fix Azure IPAM 403 errors for Azure instances using Azure Compute Gallery images (Backport PR #20364, Upstream PR #19697, @andrew-bulford-form3)
- Fix Cilium bootstrapping regression with etcd without relying on DNS (Backport PR #20263, Upstream PR #20106, @aanm)
- Fix Cilium initialization for clusters with etcd-operator (Backport PR #20263, Upstream PR #20131, @aanm)
- Fix drop of large packets redirected through an egress gateway node when running in native routing mode. (Backport PR #20412, Upstream PR #20269, @pchaigno)
- fix identity gc to return correct max/min id (Backport PR #20412, Upstream PR #20361, @dkhachyan)
- Fixed SystemD >=245 sysctl(`rp_filter`) config incompatibility (Backport PR #20364, Upstream PR #20072, @dylandreimerink)
- helm: Fix cluster-id arguments in clustermesh deployment (Backport PR #20364, Upstream PR #20312, @sayboras)
- ipsec: fix stale keys reclaim logic (Backport PR #20157, Upstream PR #19932, @jibi)
- nodemanager: Fix bug where Cilium tried to reach stale health endpoints on kubeapi-server nodes (Backport PR #20263, Upstream PR #20210, @gandro)
- jenkinsfiles: fix docker manifest inspect commands in GKE pipeline (Backport PR #20364, Upstream PR #20325, @tklauser)

### 1.11.8

- Fix bug where network policies that select namespace labels may incorrectly select identities ([Advisory](https://github.com/cilium/cilium/security/advisories/GHSA-pfhr-pccp-hwmh), commit 5639787e3d55)
- Fix ineffective post-start hook in ENI mode (Backport PR #20840, Upstream PR #20741, @bmcustodio)
- Fix mtu setting for tunnel interface in init.sh (Backport PR #20840, Upstream PR #20552, @ChengyuanLiCY)
- Fix parsing of string map command line options when more than one separator is present. (Backport PR #20840, Upstream PR #20673, @tklauser)
- Fix the bugs when empty CiliumEndpointSlices were created and leaked. (Backport PR #20840, Upstream PR #20251, @alan-kut)
- Fix bug where Cilium would crash on startup with an error about being unable to delete iptables rules. (Backport PR #20891, Upstream PR #20885, @jibi)
- Fix `subnet_id` label value being empty in IP allocation and interface creation in ENI IPAM metrics (Backport PR #20840, Upstream PR #20449, @wu0407)
- fqdn/dnsproxy: fix test build (Backport PR #20840, Upstream PR #20537, @tklauser)

### 1.11.9

- clustermesh-apiserver: fix key name for delete during k8s->kvstore sync (Backport PR #21139, Upstream PR #21078, @tklauser)
- Fix conflicting routes for multiple ENIs in IPAM mode (Backport PR #21223, Upstream PR #20112, @recollir)
- Fix identity garbage collection in clustermesh environments (#20933, @aanm)
- Fix node label synchronization in the KVStore when IPSec configuration changes (Backport PR #21139, Upstream PR #21087, @aanm)
- Fix regression with cilium-health-probe controller in IPv6-only clusters (Backport PR #20939, Upstream PR #20849, @aanm)
- Fix Wireguard connectivity issues when using kvstore mode (Backport PR #21139, Upstream PR #21080, @aanm)
- Fixed PodCIDR announcement being overwritten by SVC announcement (Backport PR #20880, Upstream PR #20413, @dylandreimerink)
- Fixes typos in enabling fqdn_semaphore_rejected_total metric (Backport PR #20939, Upstream PR #20893, @rahulkjoshi)
- ipcache/kvstore: fix panic when processing ip=<nil> entries (Backport PR #20939, Upstream PR #20706, @ArthurChiao)
- ipsec: Fix incorrect parsing of SPI from mark (Backport PR #20939, Upstream PR #20900, @pchaigno)
- k8s/watchers: fix panic in CiliumEndpoint labels update (Backport PR #21139, Upstream PR #20865, @jaffcheng)
- kvstore/allocator: fix panic on receiving invalid identity entries (Backport PR #21291, Upstream PR #21213, @ArthurChiao)
- pkg/k8s/watcher: fix deadlock crash that occurs when handling endpoint and service updates. (Backport PR #21223, Upstream PR #21093, @tommyp1ckles)
- v1.11: operator: fix key name for delete during k8s->kvstore sync (#20983, @tklauser)
- config: Fix unit tests for native routing CIDR (Backport PR #20939, Upstream PR #20473, @pchaigno)
- k8s: fix test flake in TestGenerateToCIDRFromEndpoint. (Backport PR #21223, Upstream PR #21220, @tommyp1ckles)
- k8s: fix test flake in TestGenerateToCIDRFromEndpoint. (Backport PR #21291, Upstream PR #21220, @tommyp1ckles)
- bgp: Fixed broken bgp speaker unit tests (Backport PR #20880, Upstream PR #20521, @dylandreimerink)
- Fix complaint about nil IP address on restore of cilium_host (Backport PR #20939, Upstream PR #20734, @christarazi)

### 1.11.10

- bugtool: Fix pprof default ports (Backport PR #21633, Upstream PR #21497, @pippolo84)
- daemon: Fix a nil dereference on cleanup when DNS proxy is not enabled (Backport PR #21468, Upstream PR #21365, @joamaki)
- Fix agent deadlock caused by frequent kube-apiserver IP recycling (Backport PR #21564, Upstream PR #21629, @joestringer)
- Fix bug that can cause some traffic covered by an L7 policy to be dropped when IPsec is enabled on EKS. (Backport PR #21642, Upstream PR #21595, @pchaigno)
- Fix bug where traffic sent outside the cluster via ToFQDNs policy would be denied despite a policy that allows it (Backport PR #21564, Upstream PR #20721, @joestringer)
- ipcache: Fix metadata access from CIDR allocation (Backport PR #21564, Upstream PR #21565, @joestringer)
- Fix a typo in the comment example (Backport PR #21468, Upstream PR #21402, @farcaller)
- helm: Fix post-start and pre-stop hooks for cilium-nodeinit on Ubuntu EKS images (Backport PR #21468, Upstream PR #20979, @dctrwatson)
- ipcache: Fix lock leak (Backport PR #21564, Upstream PR #20833, @joestringer)
- ipsec: Fix slightly incorrect assumption in XFRM IN policies (Backport PR #21642, Upstream PR #21621, @pchaigno)

### 1.11.11

- Fix overlapping/duplicate PodCIDR allocation when nodes are added while operator is down (Backport PR #22073, Upstream PR #21526, @dylandreimerink)
- Fixed CCNP garbage collection (Backport PR #21810, Upstream PR #21394, @zuzzas)
- Fixes a deadlock that can be exposed in high-churn clusters when Pods are deleted rapidly. (Backport PR #21810, Upstream PR #21771, @squeed)

### 1.11.12

- Fix bug that could lead to inconsistent pod IP information between agents, sometimes leading to a failure to decrypt IPsec traffic. (Backport PR #22309, Upstream PR #22127, @aanm)
- Fix bug where configuring the API rate limiter options could fail when providing multiple options (Backport PR #22752, Upstream PR #22299, @thorn3r)
- Fix forwarding of the security identity by the DNS proxy which could cause random policy denials (Backport PR #22456, Upstream PR #22361, @aspsk)
- Fix GC of CEPs that were not GCed by kube-apiserver (Backport PR #22309, Upstream PR #22213, @aanm)
- github: fix bpf-checks on ubuntu-latest runner (Backport PR #22329, Upstream PR #22322, @julianwiedmann)

### 1.11.13

- Fix crash of CES queue delay metric when CESTracker is nil (Backport PR #23313, Upstream PR #22884, @dlapcevic)
- Added Agent init check that removes all CiliumEndpoints referencing local Node that are not managed. This fixes issues where sometimes CiliumEndpoints referencing still running Pods can become unmanaged during Cilium restart. (Backport PR #22563, Upstream PR #20350, @tommyp1ckles)
- envoy: Fix regression on passing TLS SNI option to upstream TLS connections (#23031, @jrajahalme)
- Fix a data race in dnsproxy which could lead to DNS requests drops. (Backport PR #23313, Upstream PR #22619, @aspsk)
- test/helpers: Fix retry condition for CiliumExecContext (Backport PR #23313, Upstream PR #22726, @christarazi)
- ci, github: Fix IPv6 conformance test (Backport PR #23055, Upstream PR #22774, @borkmann)
- daemon/cmd: Fix error handling for getting proxy port (Backport PR #22563, Upstream PR #22296, @christarazi)
- vendor: Pick up security fixes (#23215, @michi-covalent)

### 1.11.14

- Added Agent init check that removes all CiliumEndpoints referencing local Node that are not managed. This fixes issues where sometimes CiliumEndpoints referencing still running Pods can become unmanaged during Cilium restart. (Backport PR #23097, Upstream PR #20350, @tommyp1ckles)
- proxy: Fix deadlock in error path of CreateOrUpdateRedirect (Backport PR #23462, Upstream PR #23377, @gandro)
- github/workflows: fix external contribution detection (Backport PR #23462, Upstream PR #23406, @aanm)
- github/workflows: PR labeler fix GH workflow if expression (Backport PR #23627, Upstream PR #23482, @aanm)
- cilium: Fix missing error log dump from compilation (Backport PR #23462, Upstream PR #23339, @borkmann)

### 1.11.15

- agent: fix incorrect deletion of veth host interfaces on bootstrap (Backport PR #23958, Upstream PR #23787, @giorio94)
- clustermesh: fix services cache bloat due to incorrect deletion (Backport PR #24089, Upstream PR #23947, @giorio94)
- Fix connectivity issue upon agent restart in case of ipv6 + direct routing + KPR replacement (Backport PR #23958, Upstream PR #23857, @giorio94)
- Fix enable-stale-cilium-endpoint-cleanup flag not actually disabling the cleanup init set when set to false. This provides a workaround for an existing panic that can occur when running using etcd kvstore. (Backport PR #24308, Upstream PR #23874, @sjdot)
- Fix leaking service backend entries when services with terminating backends were deleted. (#23858, @aditighag)
- ipam/crd: Fix panic due to concurrent map read and map write (Backport PR #23958, Upstream PR #23713, @gandro)
- bpf: Fix usage of tunnel map structs (Backport PR #24089, Upstream PR #23469, @pchaigno)
- Fixed link to broken anchor in RKE doc (Backport PR #23958, Upstream PR #23706, @raphink)
- workflow: fixes LLVM, Clang cache and install path (Backport PR #23958, Upstream PR #23740, @brlbil)

### 1.11.16

- Add missing xfrm-no-track rules for IPv6 IPSec. This fixes a connectivity issue for IPv6 IPSec with externalTrafficPolicy=local. (Backport PR #24604, Upstream PR #24557, @jschwinger233)
- Fix for disabled cloud provider rate limiting (Backport PR #24458, Upstream PR #24413, @hemanthmalla)
- Fix missing delete events on informer re-lists to ensure all delete events are correctly emitted and using the latest known object state, so that all event handlers and stores always reflect the actual apiserver state as best as possible (#24872, @aanm)
- Fixed bug where L7 rules would be incorrectly merged between rules for the same (remote) endpoint. This bug could have caused L7 rules to be bypassed via a wildcard header rule being improperly appended to the set of HTTP rules when both a policy with HTTP header rules applying to multiple endpoints and an allow-all rule for only one of those endpoints are specified. (Backport PR #24852, Upstream PR #24788, @jrajahalme)
- Fix race conditions when deleting CNP / CCNP in e2e tests (Backport PR #24710, Upstream PR #24484, @jschwinger233)
- renovate: Fix Hubble release digest regex (Backport PR #24604, Upstream PR #24477, @gandro)
- Avoid clearing objects in CiliumEndpoint conversion funcs (Backport PR #24931, Upstream PR #24928, @aanm)
- Avoid clearing objects in conversion funcs (Backport PR #24931, Upstream PR #24241, @odinuge)
- checker: Fix incorrect checker for ExportedEqual() (Backport PR #24458, Upstream PR #24373, @christarazi)
- Fix duplicated logs for test-output.log (Backport PR #24458, Upstream PR #24171, @romanspb80)

### 1.11.17

- Fix connectivity issue if nodes share the same name across the clustermesh and wireguard is enabled (Backport PR #25011, Upstream PR #24785, @giorio94)
- Fix incorrect network policy ebpf setup that may lead to incorrect packets denies when CEP is present in multiple CES (Backport PR #25382, Upstream PR #24838, @alan-kut)
- Fix spurious errors containing "Failed to map node IP address to allocated ID". (Backport PR #25382, Upstream PR #25222, @bimmlerd)
- ipsec: Fix packet mark for FWD XFRM policy (Backport PR #25382, Upstream PR #23254, @pchaigno)
- pkg/kvstore: Fix for deadlock in etcd status checker (Backport PR #25011, Upstream PR #24786, @hemanthmalla)
- inctimer: fix test flake where timer does not fire within time. (Backport PR #25349, Upstream PR #25219, @tommyp1ckles)
- vagrant: Bump 4.9 Vagrant box (Linux 4.9.326, to fix a kernel bug) (Backport PR #25247, Upstream PR #21106, @qmonnet)
- [v1.11] contrib/backporting: Fix main branch reference (#25093, @joestringer)
- contrib/backporting: Fix main branch reference (#25141, @sayboras)

### 1.11.18

- Fix a bug due to which we would leak Linux XFRM policies, potentially leading to increased CPU consumption, when IPsec is enabled with Azure or ENI IPAM. (Backport PR #26021, Upstream PR #25784, @pchaigno)
- Fix a bug that would cause connectivity drops of type XfrmInNoStates on upgrade when IPsec is enabled with ENI or Azure IPAM mode. (Backport PR #26021, Upstream PR #25724, @pchaigno)
- Fix a bug that would cause connectivity drops of type XfrmOutPolBlock on upgrade when IPsec is enabled. (Backport PR #26021, Upstream PR #25735, @pchaigno)
- Fix a possible deadlock when using WireGuard transparent encryption. (Backport PR #25935, Upstream PR #25419, @bimmlerd)
- Fix bug affecting EKS installations with IPsec encryption enabled, where Cilium wouldn't attach its IPsec BPF program to new ENI interfaces, resulting in connectivity loss between pods on remote nodes. (Backport PR #26021, Upstream PR #25744, @joamaki)
- Fix false error log message when IPsec is enabled with IPAM modes ENI or Azure and a remote node is deleted. (Backport PR #26021, Upstream PR #26093, @pchaigno)
- Fix incorrect hubble flow data when HTTP requests contain an `x-forwarded-for` header by adding an explicit `use_remote_address: true` config to Envoy HTTP configuration to always use the actual remote address of the incoming connection rather than the value of `x-forwarded-for` header, which may originate from an untrusted source. This change has no effect on Cilium policy enforcement where the source security identity is always resolved before HTTP headers are parsed. Previous Cilium behavior of not adding `x-forwarded-for` headers is retained via an explicit `skip_xff_append: true` config setting, except for Cilium Ingress where the source IP address is now appended to `x-forwarded-for` header. (Backport PR #25733, Upstream PR #25674, @jrajahalme)
- Fix leak of IPsec XFRM FWD policies in IPAM modes `cluster-pool`, `kubernetes`, and `crd` when nodes are deleted. Fix incorrect catch-all default-drop XFRM OUT policy for IPsec IPv6 traffic that could lead to leaking plain-text IPv6 traffic if combined with some other bug. (Backport PR #26021, Upstream PR #25953, @pchaigno)
- Fix three issues in the bug fix to attach IPsec BPF programs to ENI interfaces: do not fatal if loading unexpectedly fails (which may happen if the device is suddenly deleted), ignore veth device changes in order not to reinitialize when new endpoints appear and wait 1 second for further device state changes between reinitializations. (Backport PR #26021, Upstream PR #25936, @joamaki)
- ipsec: Fix cleanup of XFRM states and policies (Backport PR #26021, Upstream PR #26072, @pchaigno)

### 1.11.19

- Fix bug that caused transient IPsec packet drops on upgrades when tunneling is enabled. (Backport PR #26872, Upstream PR #26708, @pchaigno)
- Fix bug where CNI gets installed even if cni.install=false (Backport PR #26419, Upstream PR #26278, @joestringer)
- Fix path asymmetry when using pod-to-pod encryption with IPsec and tunnel mode. (Backport PR #26872, Upstream PR #25440, @pchaigno)
- Fixed Cilium agent crash when policy refers to a non-existing Envoy listener. (Backport PR #26419, Upstream PR #25969, @jrajahalme)
- Fixed proxy redirect policy implementation when any deny rule prevents them. (Backport PR #26752, Upstream PR #26344, @jrajahalme)
- ipsec: Split removeStaleXFRMOnce to fix deprioritization issue (Backport PR #26419, Upstream PR #26113, @jschwinger233)
- Fix "make -C Documentation builder-image" (Backport PR #26917, Upstream PR #26874, @michi-covalent)

### 1.11.20

- Fix a bug that could cause packet drops of type XfrmOutPolBlock when IPsec is enabled and node are recycled
- Fix a bug that could cause IPsec-encrypted packets to be sent to the wrong destination node when node churn is high. (Backport PR #27148, Upstream PR #27029, @pchaigno)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.11.20**, the newest release recorded here for this line.

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
