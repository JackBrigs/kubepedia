---
id: TROUBLE-CILIUM_1_10_DEFECTS
type: troubleshooting
title: "cilium 1.10: defects fixed in the 1.10 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.10.0 <1.11.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.10 known issues
  - cilium 1.10 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.10 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.10: defects fixed in the 1.10 line

## Summary

**207 defects** the project fixed across **21 releases** of the 1.10 line, from 1.10.0 to
1.10.20. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.10.0

- wireguard: Add pod2pod encryption support in tunnel mode and fix IPv6 for direct routing mode (#15716, @brb)
- Avoid exposing full Cilium API in LB-only mode (#14098, @christarazi)
- cilium: Encryption EKS 4.14 kernel (default) fixes (Backport PR #16049, Upstream PR #15867, @jrfastab)
- eni: Fix Cilium overallocating network interfaces (Backport PR #16049, Upstream PR #15911, @gandro)
- Fix 5.10+ complexity issue with `kubeProxyReplacement=disabled` (Backport PR #16150, Upstream PR #16084, @pchaigno)
- Fix aws-cni integration where pods were not being scheduled (Backport PR #16049, Upstream PR #15915, @aanm)
- Fix backwards compatibility of status API (#15143, @tgraf)
- Fix bug where L7 ingress policies with IPsec dropped traffic in tunneling mode (Backport PR #16103, Upstream PR #16057, @christarazi)
- Fix ICMP Echo ID placement in CT maps (#15275, @brb)
- Fix rounding behavior when specifying a capacity for Hubble's buffer. (#13894, @rolinh)
- hubble: Fix numeric identity lookup for FQDN identities (#14477, @gandro)
- ipam/aws: fixed a bug causing the operator to hang indefinitely when the ENI limits for an instance type could not be determined (#14905, @mvisonneau)
- kvstore: Fix aborted delayed delete warning (#15409, @tgraf)
- ui envoy: fix config to keep grpc conn (Backport PR #16049, Upstream PR #15938, @geakstr)
- wireguard: Fix traffic counters in `cilium debuginfo` (Backport PR #16210, Upstream PR #16178, @gandro)
- github: fix kind GH action for encryption e2e tests (#15731, @aanm)
- bpf: Fix compilation of bpf_ct_tests (#14862, @pchaigno)
- jenkinsfiles: fix race detector pipelines (Backport PR #16103, Upstream PR #16056, @nbusseneau)
- labelsfilter: Fix test for default filters (#15024, @pchaigno)
- node-neigh: Fix unit test flake (Backport PR #16150, Upstream PR #16072, @brb)
- test/helpers: fix GetBPFPacketsCount (#14663, @jibi)
- wireguard: Fix timeout in unit test (Backport PR #16049, Upstream PR #16001, @gandro)
- workflows: fix EKS encryption testing not using aws operator image (#15745, @nbusseneau)
- workflows: fix GKE `if` condition (#15788, @nbusseneau)
- workflows: fix schedule triggers (#15813, @nbusseneau)
- workflows: small fixes to Kind (#15658, @nbusseneau)
- github: Fix cilium project management for v1.9 (#14065, @joestringer)
- github: fix correct sha for images build (#15065, @aanm)
- add GH action to push hot fix images into -dev repositories (#15061, @aanm)
- Add hubble relay docker images + fix k8s version for eks in contrib testing script (#14478, @ungureanuvladvictor)
- add_vagrant_box.sh: Fix download issue and update help message (#14553, @qmonnet)
- add_vagrant_box.sh: Fix incorrect vagrant box updates (#14527, @pchaigno)
- azure: Fix API rate limit test (#15493, @twpayne)
- bpf: datapath: Fix fetching configured base devices (#14456, @mrostecki)
- bpf: fix health cilium_ipip6 collect_md mode (#15281, @borkmann)
- bpf: fixes for host routing (#15240, @borkmann)
- bwm: queue mapping & cong fixes (Backport PR #16049, Upstream PR #15964, @borkmann)
- cilium/cmd: Fix skipping of .git directories (#13760, @twpayne)
- contrib: Fix scripts for v1.10 (Backport PR #15919, Upstream PR #15898, @joestringer)
- crypto/certloader: fix tests comparing crypto/x509.CertPool for Go 1.16 (#14789, @tklauser)
- daemon_main: fix comments error (#14194, @lrouter)
- datapath/linux: Fix clang version regex check (#14742, @christarazi)
- datapath/loader: fix privileged test build (#14335, @tklauser)
- Fix a typo in terminology documentation (#14181, @didier-durand)
- fix broken link on readme (#13981, @kaitoii11)
- Fix encryption getting started guides for v1.10 (Backport PR #16049, Upstream PR #15961, @jibi)
- Fix error propagation in (*K8sWatcher).addK8sPodV1 (#14864, @tklauser)
- Fix logging for expired FQDN IPs (Backport PR #16210, Upstream PR #16030, @youssefazrak)
- Fix rawgit links in README.rst (#14092, @vignesh-codes)
- install/kubernetes: fix upgrade envoy to 1.18.2 for Hubble UI (#15879, @kaworu)
- issue_14922: Fixed the 429 response code handling (Backport PR #15919, Upstream PR #15760, @Maddy007-maha)
- k8s: Fix Wireguard with IPAM != ClusterPool (#15784, @gandro)
- kvstore: Fix event watcher serialization (#14101, @joestringer)
- Minor fixes for OKD GSG (Backport PR #16049, Upstream PR #16000, @errordeveloper)
- pkg/k8s: fix concurrent access in CNP field (#15518, @aanm)
- ui deployment: upgrade envoy to 1.18.2, fix config (#15847, @geakstr)
- Various documentation / comments fixes and improvements (#14439, @kaworu)
- wireguard: Fix rp_filter setting (#15542, @brb)
- workflows: fix image workflows for v1.10 (#16009, @nbusseneau)

### 1.10.1

- alibabacloud: fix race (Backport PR #16269, Upstream PR #16175, @l1b0k)
- Fix "unable to update ipcache map entry on pod add" harmless log warnings (Backport PR #16384, Upstream PR #16286, @aanm)
- Fix bug where Cilium allocates a new router (`cilium_host`) IP upon node reboot, breaking connectivity especially with IPsec (Backport PR #16438, Upstream PR #16307, @christarazi)
- Fix bug where users were unable to use node-selectors in the BGP configuration when using BGP support (Backport PR #16521, Upstream PR #16341, @christarazi)
- Fix bug with Helm chart where a user could not enable BGP and set Operator resources. (Backport PR #16438, Upstream PR #16273, @rkage)
- Fixed bug causing policy realization being skipped in some scenarios with endpoint identity churn. (Backport PR #16384, Upstream PR #16271, @jrajahalme)
- helm: Fix patch failure when updating `hubble-generate-certs` (Backport PR #16438, Upstream PR #16373, @gandro)
- ipam: fix crd mode (Backport PR #16521, Upstream PR #16493, @joamaki)
- github: Fix concurrency group comment triggers (Backport PR #16384, Upstream PR #16310, @pchaigno)
- github: Fix error triggered by large comments (Backport PR #16438, Upstream PR #16360, @pchaigno)
- github: Fix scheduled end-to-end tests (Backport PR #16384, Upstream PR #16274, @pchaigno)
- node: fix arpping test (Backport PR #16521, Upstream PR #16432, @jibi)
- test/helpers: Fix incorrect count of endpoints (Backport PR #16521, Upstream PR #16437, @pchaigno)
- Update base image to fix potential security vulnerabilities detected by image scanners. (#16527, @aanm)

### 1.10.2

- Fix connectivity issues when kube-proxy replacement is enabled, caused by ineffective socket-based load balancing (aka host reachable services) in the private cgroup namespace mode of container runtimes (e.g., docker cgroupv2 configuration)
- Fix hw_csum dmesg message for ICMP probe packets
- Fixes connectivity issues when kube-proxy replacement is enabled, caused by ineffective socket based load balancing (aka host reachable services) in the private cgroup namespace mode of container runtimes (e.g., docker cgroupv2 configuration). (Backport PR #16671, Upstream PR #16259, @aditighag)
- bpf: fix iptables masquerading for node -> remote pod traffic (Backport PR #16654, Upstream PR #16136, @jibi)
- bpf: fix hw_csum issue for icmp probe packets (Backport PR #16614, Upstream PR #16604, @borkmann)
- daemon, node: Fix faulty router IP restoration logic (Backport PR #16675, Upstream PR #16672, @christarazi)
- Fix issue where generating Hubble certs were broken (Backport PR #16614, Upstream PR #16509, @alex1989hu)
- ipsec: Fix logging of SPI after key rotations (Backport PR #16614, Upstream PR #16557, @pchaigno)
- Potential deadlock in pod identity updates has been fixed. (Backport PR #16614, Upstream PR #16529, @jrajahalme)
- pkg/option: Fix default assignment of EnableWellKnownIdentities (Backport PR #16614, Upstream PR #16434, @mauriciovasquezbernal)
- node-neigh: Fix concurrent arping update unit test flake (Backport PR #16614, Upstream PR #16578, @brb)
- k8s: Fix logging (Backport PR #16614, Upstream PR #16530, @jrajahalme)

### 1.10.3

- Fix 1.10.2 regression where Cilium would not start in certain environments
- Envoy configuration with `--proxy-prometheus-port` is fixed. (Backport PR #16829, Upstream PR #16834, @jrajahalme)
- Potential deadlock in pod identity updates has been fixed. (Backport PR #16829, Upstream PR #16801, @jrajahalme)
- ci/conformance: Various image-related fixes (Backport PR #16829, Upstream PR #16715, @gandro)
- Fix and add more commands in CI sysdumps (Backport PR #16774, Upstream PR #16721, @aanm)
- workflows: fix concurrency group names (Backport PR #16829, Upstream PR #16711, @nbusseneau)
- workflows: fix L4LB test missing PR reporting on issue_comment (Backport PR #16829, Upstream PR #16830, @nbusseneau)
- workflows: fix Relay pgrep check when using additional flags (Backport PR #16829, Upstream PR #16831, @nbusseneau)
- workflows: various fixes & consistency passes (Backport PR #16829, Upstream PR #16787, @nbusseneau)
- [v1.10] fix condition for running documentation GitHub action on Helm updates (#16747, @qmonnet)

### 1.10.4

- Fix a crash where user specifies incorrect service name in a local redirect policy config, or policy selected service is added after the policy is added. (Backport PR #17183, Upstream PR #16216, @aditighag)
- Fix bug where timers used for retries sometimes fired immediately (Backport PR #17011, Upstream PR #16955, @gandro)
- Fix Linux slave interface detection (Backport PR #17216, Upstream PR #17189, @pchaigno)
- Fix transient policy deny during agent restart (Backport PR #17216, Upstream PR #17115, @jaffcheng)
- hubble/recorder: Refactor service implementation to fix multiple races (Backport PR #17011, Upstream PR #16472, @gandro)
- policy: Fix `cilium policy trace` output when only deny rules are applied (Backport PR #17119, Upstream PR #16991, @chez-shanpu)
- routing: Fix incorrect interface selection for egress pod routes (Backport PR #17183, Upstream PR #17169, @pchaigno)
- hubble/relay: Fix close of closed channel in unit test (Backport PR #16993, Upstream PR #16958, @gandro)
- Avoid transitive dependency on github.com/miekg/dns in policy API (Backport PR #16960, Upstream PR #16806, @tklauser)
- install: Fix README links to getting started guides (Backport PR #17119, Upstream PR #16947, @joestringer)
- proxylib/test: fix data race between StartAccessLogServer and Close (Backport PR #17216, Upstream PR #16298, @tklauser)
- proxylib: Fix data races in unit tests (Backport PR #17216, Upstream PR #17141, @gandro)
- github: fix GH workflows to handle push events to stable branches (#16979, @aanm)

### 1.10.5

- egress gateway: fix non-tunnel (direct routing) mode (Backport PR #17582, Upstream PR #17517, @kkourt)
- Fix bug where IP addresses of devices in unknown state are resolved as remote-node (Backport PR #17495, Upstream PR #17418, @jibi)
- Fix memory leak that can occur with the presence of FQDN policies (Backport PR #17495, Upstream PR #17432, @aanm)
- node: Fix race condition on labels' getter/setter (Backport PR #17313, Upstream PR #17217, @pchaigno)
- [v1.10] fix MLH config trigger (#17423, @nbusseneau)
- fix(docs): bandwidth-manager install error (Backport PR #17392, Upstream PR #17338, @withlin)

### 1.10.6

- bug/pkg/health: Fix Nil Address Issue in Node Update Mechanism (Backport PR #17861, Upstream PR #17667, @nathanjsweet)
- bugtool: fix data race occurring when running commands (Backport PR #17985, Upstream PR #17916, @rolinh)
- bugtool: fix IP route debug gathering commands (Backport PR #18066, Upstream PR #18059, @tklauser)
- egressgateway: fix manager logic (Backport PR #18082, Upstream PR #17813, @jibi)
- Fix bug where the agents would silently skip all IPv6 masquerading due to an incorrect configuration. (Backport PR #17985, Upstream PR #17906, @pchaigno)
- Fix identity leak via FQDN selectors (Backport PR #17861, #17987, #18189, Upstream PRs #17699, #17788, #18166, @joestringer)
- Fix incorrect application of egress gateway policy to internal cluster traffic. Require a 5.2 kernel or later for the egress gateway policy feature. (Backport PR #17861, Upstream PR #17639, @kkourt)
- Fix issue where local host IPs may be briefly associated with the remote-node identity, causing policy drops when policy should allow traffic from the host. (Backport PR #17861, Upstream PR #17836, @joestringer)
- Fix several complexity and program size issues when only one of IPv4/IPv6 is enabled. (Backport PR #17652, Upstream PR #17573, @pchaigno)
- Fixes an issue which can cause traffic to be dropped when running Cilium in ENI mode due to the presence of iptables rules left over by the AWS VPC CNI plugin. Notable features that could be impacted include the egress gateway functionality. (Backport PR #17985, Upstream PR #17845, @bmcustodio)
- Fixes for IPsec and endpoint routes (Backport PR #17985, Upstream PR #17865, @kkourt)
- github: Fix codeQL workflow skip logic (Backport PR #17625, Upstream PR #17587, @joestringer)
- aks: fix AKS cluster creation following new taint limitations (Backport PR #17625, Upstream PR #17529, @nbusseneau)
- k8sT/Egress: fixes (Backport PR #17625, Upstream PR #17581, @kkourt)
- workflows: Fix use of paths-filter on master pushes (Backport PR #17652, Upstream PR #16507, @pchaigno)
- Fix documented EC2 IAM action (Backport PR #18066, Upstream PR #17958, @austince)

### 1.10.7

- daemon: Fix multi-dev XDP check (Backport PR #18365, Upstream PR #18305, @brb)
- egressgateway: fix initial reconciliation (Backport PR #18461, Upstream PR #18325, @jibi)
- Fix an issue where the tunnel map sync controller causes errors even though tunneling is disabled. (Backport PR #18276, Upstream PR #18247, @tklauser)
- Fix crash on startup if proxy is disabled (Backport PR #18276, Upstream PR #18198, @chaosbox)
- Fix possible IP leak in case ENI's are not present in the CN yet (Backport PR #18487, Upstream PR #18352, @codablock)
- Fix TCP connectivity issues in the DSR mode when conntrack entries with missing DSR flag are reused. (Backport PR #18276, Upstream PR #18041, @Inode1)
- hubble: Fix misclassification of `to-network` reply packets (Backport PR #18276, Upstream PR #18196, @gandro)
- bpf: Reset Pod's queue mapping in host veth to fix phys dev mq selection (Backport PR #18487, Upstream PR #18388, @borkmann)

### 1.10.8

- clustermesh-apiserver: fix cmd-line args processing (Backport PR #18724, Upstream PR #18277, @abocim)
- cmd: Fix issue reading string map type via config map (Backport PR #18724, Upstream PR #18478, @sayboras)
- Fix a bug with local redirect policies selecting host networked pods as local endpoints not taking effect. (Backport PR #18724, Upstream PR #18563, @aditighag)
- Fix bug where Cilium drops traffic from remote nodes in etcd mode, despite policy that allows the traffic (Backport PR #18801, Upstream PR #18777, @joestringer)
- test/runtime: fix flake on non-ready endpoints (Backport PR #18668, Upstream PR #18627, @tklauser)
- contrib: Fix backport submission for own PRs (Backport PR #18668, Upstream PR #17988, @joestringer)

### 1.10.9

- Prevent unmanaged pods in GKE's containerd flavors. (Backport PR #18835, Upstream PR #18486, @bmcustodio) Important:* Users should update their node taints from `node.cilium.io/agent-not-ready=true:NoSchedule` to `node.cilium.io/agent-not-ready=true:NoExecute`. Important:* During the first node reboot after the fix is applied pods may still get IPs from the default CNI as cilium-node-init is only run later in the node startup process. The fix will then be in place for all subsequent reboots
- Fix 'node-init' in GKE's 'cos' images. (Backport PR #19062, Upstream PR #19017, @bmcustodio)
- Fix concurrency issue while waiting for node-init DaemonSet to be ready (Backport PR #19062, Upstream PR #18897, @aanm)
- Fix connectivity outage periods with ENI IPAM mode and IPsec enabled when nodes are deleted from the cluster (Backport PR #19023, Upstream PR #18827, @christarazi)
- Fix IPsec in Azure's IPAM mode (Backport PR #19023, Upstream PR #18911, @pchaigno)
- Fix issue where StatefulSet pod restarts could trigger persistent connectivity issues for the pods due to overzealous CiliumEndpoint resource removal by cilium-agent instances (Backport PR #19127, Upstream PR #18864, @timoreimann)
- ipam/crd: Fix spurious "Unable to update CiliumNode custom resource" failures in cilium-agent (Backport PR #19062, Upstream PR #17856, @gandro)
- Fix EncryptStatusSuite.TestCountUniqueIPsecKeys (Backport PR #19023, Upstream PR #18506, @tklauser)
- Alibabacloud fixes (Backport PR #18835, Upstream PR #18762, @jaffcheng)
- pkg/maps: Fix data races around accessing nat maps (Backport PR #19023, Upstream PR #18952, @aditighag)

### 1.10.10

- cmd: Fix issue where a ConfigMap value of `{}` was parsed as `map["{}":""]`. (Backport PR #19254, Upstream PR #19172, @gandro)
- Fix a bug where a backend pod can be selected by a local redirect policy deployed in a different namespace if the local redirect policy was deployed first. (Backport PR #19254, Upstream PR #19193, @aditighag)
- Fix bug that would cause some pod traffic to leave through the wrong interface if --aws-release-excess-ips is used and masquerading disabled. (Backport PR #19296, Upstream PR #19162, @pchaigno)
- Fix bug where FQDN policy calculation could trigger a deadlock in cilium-agent (Backport PR #19254, Upstream PR #19031, @joestringer)
- Fix bug where the Cilium DNS proxy slows down significantly (and even OOMs) due to lock contention from spawning many goroutines when handling bursty DNS traffic (Backport PR #19416, Upstream PR #19336, @nebril)
- Fixed node init in RKE (Backport PR #19416, Upstream PR #19286, @raphink)
- wireguard: Fix invalid bits when agent init (Backport PR #19254, Upstream PR #19118, @Junnplus)

### 1.10.11

- Fixed Cilium agent regression causing a crash due to ipcache controller being scheduled too soon. (Backport PR #19574, Upstream PR #19501, @jrajahalme)

### 1.10.12

- Fix memory leak in the DNS cache when a long-lived endpoint makes many unique DNS lookups over time (Backport PR #20100, Upstream PR #19925, @christarazi)
- Fix race condition leading to inconsistent CiliumNode that can cause the agent to fatal. (Backport PR #20110, Upstream PR #19923, @pchaigno)
- ipsec: Fix off-by-one error on max keyID (Backport PR #20015, Upstream PR #16647, @pchaigno)
- bug: Fix Hubble Peer Service Helm File Location (#19912, @nathanjsweet)
- metrics: Fix NaN value for cilium metrics list CLI (Backport PR #20100, Upstream PR #19987, @sayboras)

### 1.10.13

- bug: Fixed a rare CiliumIdentity race deletion. (Backport PR #20330, Upstream PR #19936, @nathanjsweet)
- cilium: fix conflicting iptables-legacy and iptables-nft rules (Backport PR #20139, Upstream PR #20123, @jrfastab)
- daemon: Fix issue where stale router IPs were not cleaned up (Backport PR #20509, Upstream PR #20389, @gandro)
- datapath: Fix security ID propagation in tunnel header for NodePort BPF forwarded requests (Backport PR #20327, Upstream PR #19061, @brb)
- Fix agent panic in some cases when service matcher local redirect policy was deployed prior to the selected service. (Backport PR #20179, Upstream PR #19522, @aditighag)
- Fix Azure IPAM 403 errors for Azure instances using Azure Compute Gallery images (Backport PR #20330, Upstream PR #19697, @andrew-bulford-form3)
- Fixed SystemD >=245 sysctl(`rp_filter`) config incompatibility (Backport PR #20232, Upstream PR #20072, @dylandreimerink)
- helm: Fix cluster-id arguments in clustermesh deployment (Backport PR #20330, Upstream PR #20312, @sayboras)
- ipsec: fix stale keys reclaim logic (Backport PR #20127, Upstream PR #19932, @jibi)
- jenkinsfiles: fix docker manifest inspect commands in GKE pipeline (Backport PR #20330, Upstream PR #20325, @tklauser)

### 1.10.14

- Fix bug where network policies that select namespace labels may incorrectly select identities ([Advisory](https://github.com/cilium/cilium/security/advisories/GHSA-pfhr-pccp-hwmh), commit 5cacb1bbb9e4)
- Fix ineffective post-start hook in ENI mode (Backport PR #20838, Upstream PR #20741, @bmcustodio)
- Fix parsing of string map command line options when more than one separator is present. (Backport PR #20838, Upstream PR #20673, @tklauser)
- Fix bug where Cilium would crash on startup with an error about being unable to delete iptables rules. (Backport PR #20892, Upstream PR #20885, @jibi)
- Fix `subnet_id` label value being empty in IP allocation and interface creation in ENI IPAM metrics (Backport PR #20838, Upstream PR #20449, @wu0407)
- fqdn/dnsproxy: fix test build (Backport PR #20620, Upstream PR #20537, @tklauser)

### 1.10.15

- Fix conflicting routes for multiple ENIs in IPAM mode (Backport PR #21221, Upstream PR #20112, @recollir)
- ipcache/kvstore: fix panic when processing ip=<nil> entries (Backport PR #20937, Upstream PR #20706, @ArthurChiao)
- ipsec: Fix incorrect parsing of SPI from mark (Backport PR #20937, Upstream PR #20900, @pchaigno)
- k8s/watchers: fix panic in CiliumEndpoint labels update (Backport PR #21054, Upstream PR #20865, @jaffcheng)
- Fix complaint about nil IP address on restore of cilium_host (Backport PR #20937, Upstream PR #20734, @christarazi)

### 1.10.16

- daemon: Fix a nil dereference on cleanup when DNS proxy is not enabled (Backport PR #21469, Upstream PR #21365, @joamaki)
- Fix bug that can cause some traffic covered by an L7 policy to be dropped when IPsec is enabled on EKS. (Backport PR #21641, Upstream PR #21595, @pchaigno)
- Fix bug where traffic sent outside the cluster via ToFQDNs policy would be denied despite a policy that allows it (Backport PR #21563, Upstream PR #20721, @joestringer)
- Fix a typo in the comment example (Backport PR #21469, Upstream PR #21402, @farcaller)
- helm: Fix post-start and pre-stop hooks for cilium-nodeinit on Ubuntu EKS images (Backport PR #21469, Upstream PR #20979, @dctrwatson)
- ipcache: Fix lock leak (Backport PR #21563, Upstream PR #20833, @joestringer)
- ipsec: Fix slightly incorrect assumption in XFRM IN policies (Backport PR #21641, Upstream PR #21621, @pchaigno)

### 1.10.17

- Fixed CCNP garbage collection (Backport PR #21811, Upstream PR #21394, @zuzzas)
- Fixes a deadlock that can be exposed in high-churn clusters when Pods are deleted rapidly. (Backport PR #21811, Upstream PR #21771, @squeed)

### 1.10.18

- Fix bug that could lead to inconsistent pod IP information between agents, sometimes leading to a failure to decrypt IPsec traffic. (Backport PR #22310, Upstream PR #22127, @aanm)
- Fix bug where configuring the API rate limiter options could fail when providing multiple options (Backport PR #22753, Upstream PR #22299, @thorn3r)
- Fix forwarding of the security identity by the DNS proxy which could cause random policy denials (Backport PR #22454, Upstream PR #22361, @aspsk)
- Fix GC of CEPs that were not GCed by kube-apiserver (Backport PR #22310, Upstream PR #22213, @aanm)
- github: fix bpf-checks on ubuntu-latest runner (Backport PR #22330, Upstream PR #22322, @julianwiedmann)
- daemon/cmd: Fix error handling for getting proxy port (Backport PR #22582, Upstream PR #22296, @christarazi)

### 1.10.19

- envoy: Fix regression on passing TLS SNI option to upstream TLS connections (#23036, @jrajahalme)
- v1.10: install: fix TerminationMessagePolicy for the Hubble Relay deployment (#23089, @rolinh)

### 1.10.20

- Fix a data race in dnsproxy which could lead to DNS requests drops. (Backport PR #23422, Upstream PR #22619, @aspsk)
- github/workflows: fix external contribution detection (Backport PR #23422, Upstream PR #23406, @aanm)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.10.20**, the newest release recorded here for this line.

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
