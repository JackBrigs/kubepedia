---
id: TROUBLE-CILIUM_1_8_DEFECTS
type: troubleshooting
title: "cilium 1.8: defects fixed in the 1.8 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.8.0 <1.9.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.8 known issues
  - cilium 1.8 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.8 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.8: defects fixed in the 1.8 line

## Summary

**292 defects** the project fixed across **14 releases** of the 1.8 line, from 1.8.0 to
1.8.13. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.8.0

- cilium: fix up all --help sections properly (Backport PR #12027, Upstream PR #11007, @soumynathan)
- daemon: Fix detection of BPF/XDP NodePort, BPF masq and host-fw devices (Backport PR #12027, Upstream PR #11894, @brb)
- Avoid duplication of generated toCIDRs when using a toServices based CNP (or CCNP) (Backport PR #11926, Upstream PR #11901, @aanm)
- azure: fix excess/off-by-one addresses allocation (#11669, @bpineau)
- cilium: fix encryption flow labels in ip6 case (Backport PR #12039, Upstream PR #12015, @jrfastab)
- cilium: fix helm usage of enableIdentityMap -> enableIdentityMark (Backport PR #12196, Upstream PR #12194, @jrfastab)
- cli: Fix JSON output for BPF conntrack & NAT tables dump (#10904, @qmonnet)
- daemon: Fix fallback to iptables-based masquerading (Backport PR #12103, Upstream PR #12081, @brb)
- daemon: fix panic when starting Cilium (Backport PR #12173, Upstream PR #12101, @aanm)
- daemon: Fix session affinity map creation (Backport PR #12173, Upstream PR #12134, @brb)
- datapath,daemon: Fix initialization panics when IPv6 is enabled (Backport PR #12203, Upstream PR #12197, @brb)
- datapath: Fix back-edge in bpf_sock for older kernels (#11739, @brb)
- endpoint: Fix data races while accessing GetIdentity() (Backport PR #11984, Upstream PR #11941, @tgraf)
- eni: Fix potential deadlock (Backport PR #11856, Upstream PR #11831, @christarazi)
- Fix Cilium blocking its initialization for nodes where the hostname was different that the Kubernetes node name. (#11717, @aanm)
- Fix datarace issue in spanstat.go (Backport PR #11856, Upstream PR #11615, @sayboras)
- Fix issue when Cilium randomly stops doing service translation in k8s 1.18 (Backport PR #12027, Upstream PR #11947, @aanm)
- Fix leaking endpoint state metric (Backport PR #11937, Upstream PR #11884, @christarazi)
- Fix setting monitorAggregationLevel to max reflects via CLI (Backport PR #12039, Upstream PR #12014, @soumynathan)
- Fix several data races in unit tests (#10602, @tgraf)
- Fix syslog hook missing in DefaultLogger (Backport PR #12216, Upstream PR #12170, @ArthurChiao)
- fix transparent encryption related bugs (Backport PR #12027, Upstream PR #11974, @jrfastab)
- Fix tunneling and ARP resolution when host firewall is enabled. (Backport PR #11893, Upstream PR #11795, @pchaigno)
- Fix up ipcache access in datapath (#11525, @soumynathan)
- Fix: resync IP addresses for instances that have been stopped for more than a minute (#11091, @willdeuschle)
- GKE CI: Fix K8sDatapathConfig* tests (#10259, @tgraf)
- Hubble: fix unknown identities for some CIDR (#11703, @Rolinh)
- ipcache: Fix deadlock when ipcache GC results in datapath reload (Backport PR #11984, Upstream PR #11950, @tgraf)
- loader: Fix tunneling when device is set without NodePort (Backport PR #12027, Upstream PR #11980, @pchaigno)
- nodeinit: Fix for restarting kubenet managed pods (Backport PR #11856, Upstream PR #11779, @dctrwatson)
- operator: fix panic for non existing CEPs (#11749, @aanm)
- service: Fix wrong localEndpoints count in HealthCheckNodePort (Backport PR #11893, Upstream PR #11863, @gandro)
- Correct prometheus template in integration test (#11611, @sayboras)
- eni: Fix node manager test (Backport PR #11856, Upstream PR #11773, @errordeveloper)
- Fix flaky assertion on metrics (Backport PR #11984, Upstream PR #11966, @christarazi)
- Fix gke zone in release cluster script (#10109, @nebril)
- ginkgo-ext: Fix data-race in Writer (Backport PR #12039, Upstream PR #12025, @gandro)
- test,daemon: Fix repeated devices (Backport PR #12196, Upstream PR #12176, @brb)
- github: fix doc links in PR template (#10287, @tklauser)
- travis: fix failure to install clang-10 on Arm64 (#11418, @Jianlin-lv)
- travis: fix issue that etcd exited on Arm64 (#10527, @Jianlin-lv)
- travis:fix test failed caused by timeout (#10656, @Jianlin-lv)
- Add detector and fix write access on read-only structures (#11020, @aanm)
- agent: Fix data race when accessing d.monitorAgent (Backport PR #11856, Upstream PR #11823, @tgraf)
- all: fix remaining prealloc issues (#10913, @tklauser)
- Avoid reallocations in loops (#10224, @tklauser)
- azure/ipam: Fix nil dereference with logger (Backport PR #11856, Upstream PR #11786, @christarazi)
- azure: Fix allocation of addresses (#10815, @tgraf)
- bpf: Fix build warning for unused parameter (#10611, @pchaigno)
- bpf: Fix build warning in conntrack test (#10598, @joestringer)
- bpf: fix circular dependency warning (#11479, @tklauser)
- bpf: Fix name for example map (#10768, @joestringer)
- bpf: Fix pointer-to-int-cast warning in newer Clang (#10522, @pchaigno)
- bpf: Fix race when accessing m.fd (Backport PR #11856, Upstream PR #11812, @tgraf)
- bpf: Fix reversed ENABLE_EXTRA_HOST_DEV condition (#10843, @pchaigno)
- bpf: fix test/bpf/unit-test segfault due to memcmp looping (#11709, @borkmann)
- bpf: various datapath follow-up optimisations and fixes (Backport PR #11984, Upstream PR #11924, @borkmann)
- bpf: xdp asm volatile fix in relation to reg spill (#11152, @borkmann)
- cilium: fix cell alignment in status output (#11031, @tklauser)
- coccinelle: Fix Docker image name printed on errors (#11403, @pchaigno)
- CODEOWNERS: fix path for contribution process docs (#10305, @tklauser)
- contrib, docs: fixes for the backporting guide and script README (#10672, @tklauser)
- contrib/vagrant: Fix warning when K8S is unset (#10280, @pchaigno)
- contrib: Fix submit-backport PR set-labels detection (Backport PR #11926, Upstream PR #11912, @joestringer)
- contrib: Fixes for backporting scripts (#10829, @pchaigno)
- Correct message for kvstore get (consul) (#11568, @sayboras)
- daemon: Fix TriggerReloadWithoutCompile comment (#10954, @joestringer)
- datapath: Fix panic on direct routing config (#11756, @pchaigno)
- Docs fix for mounting bpf fs (#11001, @nathanjsweet)
- endpoint: Fix incorrect warning for stat(2) (#11281, @pchaigno)
- examples/getting-started: fix docker-compose getting started (#10108, @aanm)
- Fix bpf unit test build in dev VM (#10735, @tklauser)
- Fix commands in EKS kube-proxy free GSG (Backport PR #12173, Upstream PR #12174, @tklauser)
- Fix comment typos (#10749, @ungureanuvladvictor)
- Fix corrupted bpf_features.h (#10861, @pchaigno)
- Fix DOCKER_BUILDKIT builds (Backport PR #12216, Upstream PR #12091, @jrajahalme)
- Fix GKE Helm options for CI and docs. (Backport PR #12196, Upstream PR #12087, @jrajahalme)
- Fix hubble metricsServer label in values.yaml (#10908, @soumynathan)
- Fix live preview with Python 3.8 (Backport PR #11893, Upstream PR #11838, @joestringer)
- Fix make generate-k8s-api (#11468, @sayboras)
- Fix missing newlines at end of file (#10334, @maxbischoff)
- Fix missing operator-generic in upstream k8s tests (Backport PR #12039, Upstream PR #12055, @aanm)
- Fix native routing cidr missing flag in daemon (Backport PR #12173, Upstream PR #12180, @aanm)
- Fix off-by-one warning from LGTM and add tests for NodePort range (#10151, @christarazi)
- Fix up install make target (#10320, @joestringer)
- Fix various data races in pkg/aws/eni and pkg/ipam (#11685, @christarazi)
- fix(datarace): Fix possible nil pointer dereference (Backport PR #11856, Upstream PR #11804, @sayboras)
- fix(helm): To fix un-expected {{end}} in helm template (#11400, @sayboras)
- fqdn: Fix missing IsNil checks in unit tests (Backport PR #11984, Upstream PR #11953, @pchaigno)
- helm: fixed hubble servicemonitor matchLabels parameter (Backport PR #11926, Upstream PR #11886, @mvisonneau)
- hubble-proxy: fix completion code (#10631, @Rolinh)
- identity: Recognize host and health identities as fixed (#11583, @pchaigno)
- install: Fix up version/pullPolicy for multiple values files (Backport PR #12027, Upstream PR #12030, @joestringer)
- ipam/types: fix missing deep copy fields (#10500, @aanm)
- k8s: Fix CCNP for host policies (#11638, @pchaigno)
- k8s: Fix data race when setting node address (Backport PR #11893, Upstream PR #11851, @tgraf)
- loader: Fix "Skipping symbol substitution" warnings (#10934, @pchaigno)
- loader: Fix missing dot in assembly output files (#11716, @pchaigno)
- loader: Fixes for map creation from daemon (#10728, @pchaigno)
- make: fix govet target after moving 'common' to 'pkg' (#11406, @tklauser)
- make: fix govet target after renaming hubble-proxy to hubble-relay (#11178, @tklauser)
- make: fix reference to CONTAINER_ENGINE_FULL variable (#11258, @Rolinh)
- monitor: Fix ipcache lookup debug msg (#11745, @pchaigno)
- operator: fix bugs on reading configuration from config-map (#10520, @aanm)
- operator: Fix operator flags (#11270, @tgraf)
- policy: Fix enforcement status for host endpoint (Backport PR #11856, Upstream PR #11759, @pchaigno)
- policy: Fix incorrect comment (#10588, @pchaigno)
- policy: Fix rule translation test flake (Backport PR #11926, Upstream PR #11913, @joestringer)
- README: Fix release date for v1.7.2 (#10868, @joestringer)
- service/test: Fix waiting in testSessionAffinity and regroup affinity match map updates (#11519, @brb)
- Small fixes for BPF dynamic map size flag (#11405, @tklauser)
- Small fixes for docker getting-started example (#11022, @tklauser)
- Small k8s fixes and optimizations (#11545, @aanm)
- test/bpf: Fix BPF unit tests (#11158, @pchaigno)
- vagrant: Fix bootstrap commands (#10777, @gandro)
- vagrant: Fix build in dev. VM (#11388, @pchaigno)
- vagrant: Fix make in net-next dev. VM (Backport PR #12027, Upstream PR #11987, @pchaigno)
- vagrant: Fix missing doc. dependency error (#10562, @pchaigno)

### 1.8.1

- avoid having endpoints in 'restoring' state in case the connectivity with the KVStore is not reliable (Backport PR #12332, Upstream PR #12307, @aanm)
- daemon: fix panic for cilium status in IPv6 only cluster (Backport PR #12265, Upstream PR #12221, @Rolinh)
- Fix bug where etcd session renew would block indefinitely, causing endpoint provision to fail (Backport PR #12332, Upstream PR #12292, @joestringer)
- Fix bug where identity allocation wouldn't cancel from api timeouts (Backport PR #12348, Upstream PR #12328, @joestringer)
- Fix failure to start agent when detected devices don't have hardware addresses (Backport PR #12332, Upstream PR #12321, @pchaigno)
- Fix silent cilium monitor on systems with offline CPUs (Backport PR #12332, Upstream PR #12310, @pchaigno)
- fqdn: Fix panic on MarshalJSON() (Backport PR #12265, Upstream PR #12218, @pchaigno)
- helm/operator: fix IPv6 liveness probe address for operator (Backport PR #12265, Upstream PR #12223, @Rolinh)
- hubble/peer: fix buf.Pop() crash issue (Backport PR #12296, Upstream PR #12257, @Jianlin-lv)
- make: fix LOCKDEBUG env variable reference for docker-plugin-image (Backport PR #12332, Upstream PR #12318, @Rolinh)
- metrics: fix negative identity count (Backport PR #12378, Upstream PR #12313, @ArthurChiao)
- Fix various issues (data races, flakes) related to DaemonSuite and Endpoint related test code (Backport PR #12332, Upstream PR #12195, @christarazi)
- bpf: fix in-cluster connectivity for externalTrafficPolicy=Local (Backport PR #12378, Upstream PR #12311, @borkmann)
- bpf: run kernel's checkpatch.pl locally and as GitHub action, fix style (Backport PR #12378, Upstream PR #11936, @qmonnet)
- contrib: fix branch check in `start-backport` script (Backport PR #12378, Upstream PR #12361, @Rolinh)

### 1.8.2

- avoid performing useless GETs of Cilium Endpoints (Backport PR #12600, Upstream PR #12595, @aanm)
- bpf: Fix BPF masq when running with non-hybrid DSR (Backport PR #12536, Upstream PR #12456, @brb)
- bpf: Fix monitor aggregation for 'from-network' (Backport PR #12536, Upstream PR #12559, @joestringer)
- etcd: Fix session renewal controllers (Backport PR #12600, Upstream PR #12553, @tgraf)
- etcd: Fix several etcd related issues (Backport PR #12627, Upstream PR #12605, @tgraf)
- Fix etcd failure behavior when user or client context ends (Backport PR #12600, Upstream PR #12587, @tgraf)
- Fix potential host firewall drops on egress of the node in case of SNAT (Backport PR #12600, Upstream PR #12345, @pchaigno)
- Fix incorrect host firewall enforcement when used with BPF-based NodePort services (Backport PR #12600, Upstream PR #12345, @pchaigno)
- Fix host firewall ingress bypass on path from pods to local host (Backport PR #12600, Upstream PR #12345, @pchaigno)
- Fix potential ingress host firewall bypass in tunneling mode for remote pods (Backport PR #12600, Upstream PR #12345, @pchaigno)
- Fix handling of ICMPv6 messages by host firewall (Backport PR #12600, Upstream PR #12345, @pchaigno)
- Fix failure to recognize established IPv6 connections on egress of the host firewall (Backport PR #12600, Upstream PR #12345, @pchaigno)
- Fix manual endpoint regeneration via command line (Backport PR #12536, Upstream PR #12524, @christarazi)
- Fix node label initialization with Operator IPAM (Backport PR #12600, Upstream PR #12573, @pchaigno)
- Fix string slice type CLI arguments (Backport PR #12536, Upstream PR #12457, @JieJhih)
- Fix toGroups CRD to address validation errors (Backport PR #12536, Upstream PR #12440, @lbernail)
- Fix RuntimeKVStoreTest flake (Backport PR #12600, Upstream PR #12478, @pchaigno)
- travis:fix up PodCIDRSuite failure on Arm64 (Backport PR #12600, Upstream PR #12504, @Jianlin-lv)
- travis:fix up TestShuffle failure on Arm64 (Backport PR #12600, Upstream PR #12515, @Jianlin-lv)
- cilium: hostport service map fixes (Backport PR #12536, Upstream PR #12446, @borkmann)
- Fixes for EKS NodePort XDP getting started guide (Backport PR #12627, Upstream PR #12623, @tklauser)
- policy: Fix enforcement status of host when PolicyEnforcement=always (Backport PR #12536, Upstream PR #12497, @pchaigno)

### 1.8.3

- Fix bug in ENI environments where connections to NodePort would fail due to asymmetric routing (Backport PR #13060, Upstream PR #12770, @qmonnet)
- Fix bug where cilium-health reports connectivity failures to stale IPs (Backport PR #13060, Upstream PR #12989, @kkourt)
- travis:fix up TestSpanStatRaceCondition failure (Backport PR #12702, Upstream PR #12626, @Jianlin-lv)
- test/K8sServices: Fix externalTrafficPolicy=Local with kube-proxy (on GKE) (Backport PR #12745, Upstream PR #12709, @gandro)
- avoid schedule cilium-operator pods in same node for HA mode (Backport PR #12764, Upstream PR #12771, @aanm)
- bpf,lbmap: Fix affinity v6 map and add runtime check for BPF map representation key/val sizes (Backport PR #12803, Upstream PR #12787, @brb)
- datapath: Fix ICMP ECHO tuple ports (Backport PR #12761, Upstream PR #12729, @brb)
- Fix docs on ipam-crd (Backport PR #12889, Upstream PR #12860, @mmack)
- hubble/relay: fix report of unavailable nodes (Backport PR #12702, Upstream PR #12654, @Rolinh)
- hubble/relay: fix unavailable nodes count on ServerStatus (Backport PR #12702, Upstream PR #12685, @Rolinh)
- operator: Fix non-leader crashing with kvstore (Backport PR #12846, Upstream PR #12825, @christarazi)

### 1.8.4

- bpf: Fix host firewall in presence of kube-proxy masquerading (Backport PR #13184, Upstream PR #13049, @pchaigno)
- daemon: Fix handling of policy call map on upgrades (Backport PR #13100, Upstream PR #13051, @pchaigno)
- Fix agent liveness/readiness probes for IPv6-only environment. (Backport PR #13246, Upstream PR #13203, @tklauser)
- Fix bug in EKS environments where Cilium agents never become ready due to a missing CiliumNode CRD schema property (#13196, @christarazi)
- Fix bug in operator where the operator instances in HA mode can become inconsistent in terms of running mode(HA/non HA), if kube-apiserver is not accessible when deriving k8s capabilities. (Backport PR #13246, Upstream PR #13219, @fristonio)
- Fix bug where Hubble and the Cilium CLI would fail to resolve security identities across a cluster mesh. (Backport PR #13212, Upstream PR #13205, @gandro)
- Fix clustermesh policy with endpoint-routes mode (Backport PR #13184, Upstream PR #12694, @joestringer)
- Fix endpoint selection for a wildcard to/fromEndpoints in CCNP. Cilium will only allow access from Cilium-managed endpoints in such cases instead of allowing traffic from any source. Preflight checks, when following the upgrade guide, have been extended to warn users of the new behavior. (Backport PR #13126, Upstream PR #12890, @fristonio)
- Fix handling of changes to session affinity configuration for Kubernetes services. (Backport PR #13286, Upstream PR #13271, @adamwg)
- Fix issue in NodePort service revnat handling where the interface index was not properly restored from the conntrack state leading to packet redirects to an invalid interface. (Backport PR #13289, Upstream PR #13162, @fristonio)
- Fix panic when restoring services with enable-health-check-nodeport: false (Backport PR #13212, Upstream PR #13190, @gandro)
- Fix the creation of "toGroups" derivative policies for "CiliumClusterwideNetworkPolicies". (Backport PR #13126, Upstream PR #12920, @fristonio)
- Fixes a bug where a Hubble filter on `reply=false` would report flows for which the actual reply state is unknown. (Backport PR #13289, Upstream PR #13248, @gandro)
- helm/azure: Fix fatal error for CNI Azure installation (Backport PR #13100, Upstream PR #13024, @sayboras)
- operator: fix invocation with `--help` option (Backport PR #13212, Upstream PR #13141, @tklauser)
- fix(12664): initialize gops in RootCmd execution function (Backport PR #13212, Upstream PR #12675, @fristonio)
- Prevent Cilium from deleting all custom resources especially CNP & CCNP installed inside the cluster (Backport PR #13289, Upstream PR #13272, @christarazi)

### 1.8.5

- Fix missing policy-verdict event when a session is re-opened. (Backport PR #13438, Upstream PR #13340, @lzang)
- contexthelpers: Fix deadlock when nobody recvs on success channel (Backport PR #13438, Upstream PR #13408, @brb)
- datapath: Fix handling of enable-endpoint-routes (#13448, @errordeveloper)
- Fix 1 potential deadlock in Azure IPAM and 1 other in ENI and Azure IPAM (Backport PR #13564, Upstream PR #13517, @aanm)
- Fix Azure IPAM regression (Backport PR #13421, Upstream PR #13397, @tgraf)
- Fix bug where Cilium leaks a goroutine when an endpoint is deleted. This leak, if left running in a high pod churn environment, can cause Cilium to exceed its memory usage and get OOM killed. (Backport PR #13700, Upstream PR #13683, @christarazi)
- Fix garbage collection of CEPs - delete them in tranches and not every 5 minutes. (Backport PR #13788, Upstream PR #13728, @aanm)
- Fix issue where Hubble did not properly support `--follow` queries with a `--since` filter (Backport PR #13388, Upstream PR #13324, @gandro)
- Fix natting of non-first ipv4 fragments. (Backport PR #13564, Upstream PR #13476, @liuyuan10)
- identity: Fix nil pointer panic in LookupIdentityByID (Backport PR #13594, Upstream PR #13514, @gandro)
- vendor: update arping lib to fix concurrency issues (Backport PR #13510, Upstream PR #13482, @aanm)
- ClusterPool IPAM fixes & cleanups (Backport PR #13459, Upstream PR #13028, @tgraf)
- Fix deadlock on eventqueue when it's being drained when endpoints are being restored (Backport PR #13788, Upstream PR #13716, @christarazi)
- Fix kubectl command in cassandra NetworkPolicy documentation. (Backport PR #13564, Upstream PR #13545, @velp)
- Fix race condition in DeepEqual function (Backport PR #13486, Upstream PR #13472, @aanm)
- Fixes errors "executable file not found" in script examples/kubernetes-cassandra/cass-populate-tables.sh (Backport PR #13564, Upstream PR #13534, @velp)
- Follow-up fixes for the API rate limiter (Backport PR #13486, Upstream PR #13450, @tgraf)
- pkg/k8s: fix race condition (Backport PR #13486, Upstream PR #13471, @aanm)

### 1.8.6

- bpf: Fix --force-local-policy-eval-at-source=false (Backport PR #13875, Upstream PR #13769, @joestringer)
- bpf: fix disable PolicyVerdictNotification broken (Backport PR #13951, Upstream PR #13921, @ArthurChiao)
- Fix bug in cluster-pool IPAM mode where the user is never alerted of a node CIDR allocation failure (Backport PR #14022, Upstream PR #13916, @christarazi)
- Fix bug where Cilium on smaller instance types cannot allocate IPs (Backport PR #14059, Upstream PR #13865, @christarazi)
- Fix dynamic NAT table size calculation if CT map sizes are configured statically. (Backport PR #13875, Upstream PR #13844, @tklauser)
- Fix etcd's auth token invalid after watch reconnects (Backport PR #14249, Upstream PR #14238, @aanm)
- Fix panic on cilium-agent startup when restoring LB source range maps (Backport PR #13875, Upstream PR #13842, @aanm)
- Fixed Goroutine leak for unresponded ARP pings. (Backport PR #14249, Upstream PR #14222, @jrajahalme)
- Fixed installation instructions for K3s and Kubernetes Network Policy enforcement (Backport PR #13875, Upstream PR #13783, @aanm)
- go.mod: update cilium/ipam library with bug fixes (Backport PR #13875, Upstream PR #13810, @aanm)
- hubble: Fix reply state unknown being interpreted as false (Backport PR #13876, Upstream PR #13750, @gandro)
- daemon: Fix netns usage in kpr privileged unit tests (Backport PR #14213, Upstream PR #14171, @brb)
- test/bpf: Fix XDP loading in verifier-test.sh (Backport PR #13951, Upstream PR #13927, @pchaigno)
- bpf: fix session affinity timeout test flake (Backport PR #13875, Upstream PR #13859, @fristonio)
- cilium: fix redirect limits on multi dev case (Backport PR #14087, Upstream PR #13884, @borkmann)
- Documentation: Fix Loadbalancer Guide for Clustermesh (Backport PR #13875, Upstream PR #13822, @nathanjsweet)
- examples: Fix grafana and prometheus (Backport PR #13875, Upstream PR #13860, @nathanjsweet)
- Fix GetFlows Test (Backport PR #13951, Upstream PR #13206, @nathanjsweet)
- fqdn: Fix confusion of ToFQDNs vs. DNS rules. (Backport PR #14087, Upstream PR #14012, @jrajahalme)
- fqdn: Fix unit test (Backport PR #14087, Upstream PR #14085, @jrajahalme)
- helm: Fix format issue for logOptions in ConfigMap (Backport PR #13875, Upstream PR #13837, @sayboras)
- hubble: Fix dropped flows not showing up in Hubble UI (Backport PR #13876, Upstream PR #13796, @gandro)
- node: Fix ineffectual assignment (Backport PR #14249, Upstream PR #14256, @brb)
- pkg/kvstore: fix race in etcd initialization (Backport PR #13875, Upstream PR #13780, @aanm)
- Various fixes for NodePort XDP kube-proxy free guide (Backport PR #13875, Upstream PR #13674, @tklauser)

### 1.8.7

- cilium-cni: Fix error handling for bad netns (Backport PR #14654, Upstream PR #14645, @joestringer)
- Fix a bug that affects connectivity to NodePort service via ExternalIP of the local k8s node. (Backport PR #14953, Upstream PR #14793, @AnishShah)
- Fix a route MTU issue where pods cannot receive large packets from outside the cluster when the sender sets the "don't fragment" (DF) bit. (Backport PR #14740, Upstream PR #14679, @aditighag)
- Fix BPF verifier rejection with IPv6 prefilter (Backport PR #14539, Upstream PR #14447, @pchaigno)
- Fix bug where Cilium would constantly regenerate endpoints in environments with etcd and Linux 4.15 or below. (Backport PR #14441, Upstream PR #14300, @dctrwatson)
- Fix CIDR rule bug potentially dropping allowed traffic or allowing denied traffic for deny policies (beta feature) when using ExceptCIDRs expressions. (Backport PR #14654, Upstream PR #14516, @jrajahalme)
- Fix connectivity to externalTrafficPolicy=Local services when using the host firewall with kube-proxy (Backport PR #14953, Upstream PR #14756, @pchaigno)
- Fix ENI compatibility regression between 1.7 <-> 1.8 (Backport PR #15011, Upstream PR #14991, @tgraf)
- Fix ipsec+vxlan bug where egressing packets would bypass masquerading on their way to remote nodes (Backport PR #14953, Upstream PR #14611, @jrfastab)
- Fix missing packet mark mask that can cause policy deny drops in IPSec configuration. (Backport PR #14441, Upstream PR #14381, @pchaigno)
- Fix pod-to-pod encryption bugs in the IPAM ENI mode. (Backport PR #14953, Upstream PR #14924, @aditighag)
- Fix possible overflow in values presented in the `k8s_event_lag_seconds` metric. (Backport PR #14441, Upstream PR #14313, @aanm)
- Fix potential nil pointer exception for an invalid CCNP in the Cilium Operator (Backport PR #14441, Upstream PR #14375, @aanm)
- Fix potential panic when closing etcd connection on error (Backport PR #14654, Upstream PR #14623, @aanm)
- Fix rare crash on startup when kubernetes initialization occurs before IP address configuration (Backport PR #14539, Upstream PR #14299, @joestringer)
- Fix remote pod connectivity through VIP in tunneling mode with kube-proxy and per-endpoint routes. Fix IPv6 connectivity to BPF HostPort when kube-proxy is installed (Backport PR #14953, Upstream PR #14675, @pchaigno)
- helm: Fix preflight check resource quota conflict (Backport PR #14296, Upstream PR #14295, @gandro)
- iptables: Fix incorrect SNAT bypass with endpoint routes and tunneling (Backport PR #14953, Upstream PR #14913, @pchaigno)
- metricsmap: fix Prometheus exporter (Backport PR #14310, Upstream PR #14220, @jibi)
- node-neigh: Fix node removal and invalid neigh entry due to buggy arping response correlation (Backport PR #14834, Upstream PR #14709, @brb)
- routing: Fix route collisions in AWS ENI (Backport PR #14845, Upstream PR #14269, @christarazi)
- [v1.8] release: Fix script to check presence of docker images (#14779, @joestringer)
- Fix bug Cilium hangs with kvstore configured (#14627, @christarazi)
- Fix upgrade docs link to API ratelimiting page (#14894, @joestringer)
- pkg/node: fix concurrent access of entry node (Backport PR #14654, Upstream PR #14591, @aanm)
- test/vagrant: Fix NFS setup for test VMs (Backport PR #14797, Upstream PR #13527, @pchaigno)
- backport 1.8: vendor: Bump github.com/cilium/arping to fix correlation bug (#14734, @brb)
- v1.8: travis: Fix ineffassign version to avoid breaking change (#14531, @pchaigno)

### 1.8.8

- Avoid an empty instanceID on EC2 (Backport PR #15038, Upstream PR #15012, @kkourt)
- cilium: encryption fix, ipv4-pod-subnets without encryptnode fails (Backport PR #15117, Upstream PR #14999, @jrfastab)
- cilium: encryption, fixes for ENI & Azure mode with shared podIPs and networkIPs (Backport PR #15193, Upstream PR #15048, @jrfastab)
- Fix failing `bpf-map-sync-cilium_snat_v{4,6}_external` controllers when BPF NodePort is disabled (Backport PR #15297, Upstream PR #15175, @pchaigno)
- Fix ICMP Echo ID placement in CT maps (#15273, @brb)
- Fix memory leak on stable policy identity churn. (Backport PR #15046, Upstream PR #15042, @jrajahalme)
- Fix possible deadlock when querying network interfaces for arping (#15225, @brb)
- Fix potential panic on clustermesh environments (Backport PR #15180, Upstream PR #15107, @aanm)
- add GH action to push hot fix images into -dev repositories (#15063, @aanm)

### 1.8.9

- Fix a bug that was causing Azure IPAM to not work when ApplicationSecurityGroups were attached to IPConfigurations of a NIC. (Backport PR #15329, Upstream PR #15194, @AnishShah)
- Fix an issue where packets are dropped when a pod connects to itself via a service clusterIP. (Backport PR #15440, Upstream PR #15321, @aditighag)
- ipam: Fix ENI routing for secondary CIDRs (Backport PR #15329, Upstream PR #15303, @gandro)
- node: Fix CIDR comparison when updating routes (Backport PR #15329, Upstream PR #15263, @brb)
- Remap gops to fixed port to avoid port collision with proxy. (#15634, @tklauser)
- contrib: fix remote overriding (Backport PR #15400, Upstream PR #15328, @kaworu)
- Documentation: fix key rotation command in encryption guide (Backport PR #15400, Upstream PR #15365, @mauriciovasquezbernal)

### 1.8.10

- bpf: Fix defines in policy.h (Backport PR #15764, Upstream PR #15763, @pchaigno)
- cilium: Encryption EKS 4.14 kernel (default) fixes (Backport PR #15602, Upstream PR #15867, @jrfastab)
- eni: Fix Cilium overallocating network interfaces (Backport PR #16015, Upstream PR #15911, @gandro)
- Fix aws-cni integration where pods were not being scheduled (Backport PR #16015, Upstream PR #15915, @aanm)
- Fix channel panic from ipcache kvstore reconnect (Backport PR #15921, Upstream PR #15668, @jomenxiao)
- Fix ethtool issues (Backport PR #15602, Upstream PR #15622, @tklauser)
- kvstore/etcd: fix etcd rate limit (QPS) not working (Backport PR #15921, Upstream PR #15742, @ArthurChiao)
- [v1.8] Fix image digest preparation for release commits (#15839, @joestringer)
- cilium: Fix EKS encryption panic and reinit path and add workflows test (Backport PR #15602, Upstream PR #15669, @jrfastab)
- daemon/cmd: fix Cilium version status output (Backport PR #15921, Upstream PR #15649, @aanm)
- ipsec: Fix routing CIDR iteration on EKS (Backport PR #15602, Upstream PR #15645, @gandro)

### 1.8.11

- bpf: fix hw_csum issue for icmp probe packets (Backport PR #16655, Upstream PR #16604, @borkmann)
- Fixed bug causing policy realization being skipped in some scenarios with endpoint identity churn. (Backport PR #16497, Upstream PR #16271, @jrajahalme)
- pkg/option: Fix default assignment of EnableWellKnownIdentities (Backport PR #16655, Upstream PR #16434, @mauriciovasquezbernal)
- Fix and add more commands in CI sysdumps (Backport PR #16912, Upstream PR #16721, @aanm)
- node-neigh: Fix concurrent arping update unit test flake (Backport PR #16655, Upstream PR #16578, @brb)
- node-neigh: Fix unit test flake (Backport PR #16276, Upstream PR #16072, @brb)
- node: fix arpping test (Backport PR #16497, Upstream PR #16432, @jibi)
- k8s: Fix logging (Backport PR #16655, Upstream PR #16530, @jrajahalme)

### 1.8.12

- Potential deadlock in pod identity updates has been fixed. (Backport PR #17015, Upstream PR #16801, @jrajahalme)
- github: fix GH workflows to handle push events to stable branches (#16978, @aanm)

### 1.8.13

- [v1.8] fix MLH config trigger (#17421, @nbusseneau)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.8.13**, the newest release recorded here for this line.

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
