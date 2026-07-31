---
id: TROUBLE-CILIUM_1_19_DEFECTS
type: troubleshooting
title: "cilium 1.19: defects fixed in the 1.19 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.19.0 <1.20.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.19 known issues
  - cilium 1.19 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.19 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.19: defects fixed in the 1.19 line

## Summary

**134 defects** the project fixed across **6 releases** of the 1.19 line, from 1.19.1 to
1.19.6. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.19.1

- clustermesh: fix CRD update permission for MCS-API CRD install (Backport PR cilium/cilium#44280, Upstream PR cilium/cilium#44224, @Preisschild)
- Fix panic during datapath reinitialization if DirectRouting device is required but missing (Backport PR cilium/cilium#44280, Upstream PR cilium/cilium#44219, @fristonio)
- helm: Fixed RBAC errors with `operator.enabled=false` by aligning cilium-tlsinterception-secrets Role/RoleBinding conditionals (Backport PR cilium/cilium#44280, Upstream PR cilium/cilium#44159, @puwun)
- Policy Tiers: feature-flagging, add fuzzer, fix corner cases (Backport PR cilium/cilium#44267, Upstream PR cilium/cilium#43893, @jrajahalme)
- Policy: Fix rule origin for ordered policies (Backport PR cilium/cilium#44280, Upstream PR cilium/cilium#44178, @jrajahalme)

### 1.19.2

- cilium-dbg: fix seg-fault `ip get -l reserved:host` (Backport PR cilium/cilium#44517, Upstream PR cilium/cilium#44443, @aanm)
- clustermesh: fix a few minor typo/issues in the MCS-API documentation (Backport PR cilium/cilium#44398, Upstream PR cilium/cilium#44299, @MrFreezeex)
- clustermesh: fix a goroutine leak related to EndpointSliceSync when removing cluster (Backport PR cilium/cilium#44517, Upstream PR cilium/cilium#44444, @MrFreezeex)
- clustermesh: fix a race condition where EndpointSlices created just before a cluster is removed could be left uncleaned (Backport PR cilium/cilium#44517, Upstream PR cilium/cilium#44503, @MrFreezeex)
- Fix a bug where node IPv6 updates and deletes were not correctly propagated to the Linux kernel neighbor subsystem. (Backport PR cilium/cilium#44593, Upstream PR cilium/cilium#44540, @tklauser)
- Fix bug where more Helm options were gated by `loadbalancer` option than intended (Backport PR cilium/cilium#44699, Upstream PR cilium/cilium#42916, @mliner)
- Fix envoy admin socket being created as world-accessible (Backport PR cilium/cilium#44593, Upstream PR cilium/cilium#44512, @0xch4z)
- Fix IPSec key rotation race condition where packets were dropped due to XFRM states not being ready when peers started using the new key. Also adds logging for key rotation flow. (Backport PR cilium/cilium#44699, Upstream PR cilium/cilium#44335, @daanvinken)
- Fix tearing down wrong pod's veth in aws-cni chaining when using deterministic pod names (Backport PR cilium/cilium#44517, Upstream PR cilium/cilium#44494, @aanm)
- Fixed a bug in service load balancing where backend slot assignments could have gaps when maintenance backends exist, potentially causing traffic misrouting. (Backport PR cilium/cilium#44398, Upstream PR cilium/cilium#43902, @Aman-Cool)
- Fixed a bug where bandwidth priority updates were not applied when only the priority annotation was changed on a Pod. (Backport PR cilium/cilium#44517, Upstream PR cilium/cilium#44329, @zbb88888)
- Fixed an issue where wildcard FQDN network policy identities were not correctly pushed to Envoy when using SNI-based policies. (Backport PR cilium/cilium#44517, Upstream PR cilium/cilium#44462, @liyihuang)
- Fixed VTEP ARP responses returning 00:00:00:00:00:00 MAC due to interface MAC missing from eBPF Overlay configuration. (Backport PR cilium/cilium#44699, Upstream PR cilium/cilium#44513, @akos011221)
- gateway-api: Fix hostname intersection bug that was preventing cert-manager challenges from working correctly. (Backport PR cilium/cilium#44517, Upstream PR cilium/cilium#44492, @youngnick)
- gateway-api: Fixed some issues with TLSRoute attachment that will be covered by new conformance tests soon. (Backport PR cilium/cilium#44517, Upstream PR cilium/cilium#44397, @youngnick)
- ipam: Fix concurrent map access to multipool map (Backport PR cilium/cilium#44517, Upstream PR cilium/cilium#44150, @christarazi)
- l7lb: fix bypassing ingress policies for local backends (Backport PR cilium/cilium#44800, Upstream PR cilium/cilium#44693, @smagnani96)
- github/workflows: eks-cluster-pool-manager: fix race condition and c… (Backport PR cilium/cilium#44398, Upstream PR cilium/cilium#44283, @aanm)
- [v1.19] fix: add Documentation/cmdref/cilium-dbg_policy_subject-selectors.md (cilium/cilium#44644, @jingyuanliang)
- fix(deps): update all-dependencies (v1.19) (cilium/cilium#44471, @cilium-renovate[bot])
- fix(deps): update k8s.io patch updates stable (v1.19) (cilium/cilium#44474, @cilium-renovate[bot])
- fix(deps): update k8s.io patch updates stable to 0f775a3 (v1.19) (cilium/cilium#44570, @cilium-renovate[bot])
- fix(deps): update k8s.io patch updates stable to v0.35.2 (v1.19) (patch) (cilium/cilium#44571, @cilium-renovate[bot])
- fix(deps): update sigs.k8s.io/mcs-api/controllers digest to 15301c2 (v1.19) (cilium/cilium#44785, @cilium-renovate[bot])
- fix(deps): update sigs.k8s.io/mcs-api/controllers digest to 6a4a49e (v1.19) (cilium/cilium#44672, @cilium-renovate[bot])
- fix: helm value rendering bug for operator.unmanagedPodWatcher.intervalSeconds (Backport PR cilium/cilium#44517, Upstream PR cilium/cilium#44211, @jayl1e)

### 1.19.3

- Fix performance bug in L7 policy proxy redirect handling (Backport PR cilium/cilium#44828, Upstream PR cilium/cilium#44613, @fristonio)
- Fixes issue where the Cilium agent fails to initialise when using KVStore identity mode with etcd behind a K8s Service (Backport PR cilium/cilium#44828, Upstream PR cilium/cilium#44653, @41ks)
- [v1.19] Fix incorrect policy service selector handling (cilium/cilium#44888, @fristonio)
- bgp: Fix potential race in service advertisements upon error retry (Backport PR cilium/cilium#45211, Upstream PR cilium/cilium#45049, @rastislavs)
- clustermesh: fix a bug in the MCS-API CRD installl that could attempt a CRD downgrade when the version label is higher (Backport PR cilium/cilium#44828, Upstream PR cilium/cilium#44738, @MrFreezeex)
- envoy: Fix xds server npds listeners accounting (Backport PR cilium/cilium#45217, Upstream PR cilium/cilium#44830, @fristonio)
- Fix a slow memory leak triggered by incremental policy updates (Backport PR cilium/cilium#44994, Upstream PR cilium/cilium#44328, @odinuge)
- Fix endpoints for static pods stuck in init identity (Backport PR cilium/cilium#45211, Upstream PR cilium/cilium#45016, @aaroniscode)
- Fix in-cluster NodePort connectivity failure in DSR mode when SocketLB is disabled. When a pod accesses a NodePort service via a remote node's IP (instead of the ClusterIP) and the selected backend resides on the same node as the client, the connection fails due to missing reverse NAT on the reply path. (Backport PR cilium/cilium#44968, Upstream PR cilium/cilium#41963, @gyutaeb)
- Fix memory leak triggered by policies being created and deleted (Backport PR cilium/cilium#44828, Upstream PR cilium/cilium#44724, @odinuge)
- Fix panic in Hubble Relay when new peer address is unresolvable (Backport PR cilium/cilium#45211, Upstream PR cilium/cilium#45021, @pesarkhobeee)
- fix(datapath): ignore link-local IPv6 addresses for NodePort binding (Backport PR cilium/cilium#44974, Upstream PR cilium/cilium#44778, @Bigdelle)
- Fixed a bug in dual-stack cluster-pool IPAM where an operator restart with a pre-existing duplicate IPv6 PodCIDR could cause the affected node's IPv4 PodCIDR to be incorrectly freed and reassigned to another node. (Backport PR cilium/cilium#44866, Upstream PR cilium/cilium#44832, @christarazi)
- Fixed an issue where policy update ack is never completed after endpoint deletion. (Backport PR cilium/cilium#44818, Upstream PR cilium/cilium#44754, @jrajahalme)
- Fixed ipcache identity update hang when last proxy listener is removed. (Backport PR cilium/cilium#45217, Upstream PR cilium/cilium#44597, @jrajahalme)
- Fixes GRPCRoute being silently excluded from Envoy config when a Gateway listener explicitly sets allowedRoutes.kinds. (Backport PR cilium/cilium#44974, Upstream PR cilium/cilium#44826, @eufriction)
- Fixes increased CPU usage in `hubble observe` caused by log coloring feature, even when coloring was disabled (Backport PR cilium/cilium#44828, Upstream PR cilium/cilium#44119, @tporeba)
- lb: fix panic in orphan backend cleanup when addr is zero-value (Backport PR cilium/cilium#44994, Upstream PR cilium/cilium#44853, @vipul-21)
- operator/identitygc: fix nil pointer dereference on shutdown (Backport PR cilium/cilium#45211, Upstream PR cilium/cilium#45091, @tsotne95)
- Fix some test-e2e-upgrade issues (Backport PR cilium/cilium#45211, Upstream PR cilium/cilium#45075, @aanm)
- fix: escape $ character in regex to prevent injection (Backport PR cilium/cilium#44828, Upstream PR cilium/cilium#44638, @peoyekunle)
- fix: harden k8s apiserver endpoint access (Backport PR cilium/cilium#44994, Upstream PR cilium/cilium#44863, @sekhar-isovalent)
- Fix EKS workflows misc errors (Backport PR cilium/cilium#45052, Upstream PR cilium/cilium#45023, @aanm)
- fix(deps): update k8s.io patch updates stable to v0.35.3 (v1.19) (patch) (cilium/cilium#44933, @cilium-renovate[bot])
- fix(deps): update k8s.io/utils digest to 28399d8 (v1.19) (cilium/cilium#44928, @cilium-renovate[bot])
- fix(deps): update sigs.k8s.io/mcs-api/controllers digest to 4b9911b (v1.19) (cilium/cilium#45177, @cilium-renovate[bot])
- fix: using a local action needs checkout in eks-cluster-delete (Backport PR cilium/cilium#44994, Upstream PR cilium/cilium#44890, @sekhar-isovalent)
- loadbalancer: Fix issue in resynchronization of state from api-server which may have left stale backends around until an updated EndpointSlice was received (cilium/cilium#45198, @joamaki)

### 1.19.4

- bpf: host: fix source identity for IPsec trace in to-netdev (Backport PR cilium/cilium#45594, Upstream PR cilium/cilium#45588, @julianwiedmann)
- cilium: Fix incorrect IPv6 BIG TCP display (Backport PR cilium/cilium#45630, Upstream PR cilium/cilium#45529, @pchaigno)
- clustermesh: Fix Helm typo preventing to add annotations when setting `clustermesh.apiserver.tls.auto.method: certmanager` (Backport PR cilium/cilium#45630, Upstream PR cilium/cilium#45576, @owayss)
- Fix cilium-agent crash when a transient network error occurs during CiliumNode update. The agent now retries instead of calling Fatal. (Backport PR cilium/cilium#45673, Upstream PR cilium/cilium#44526, @nebojsaj1726)
- Fix CiliumLocalRedirectPolicy addressMatcher overriding an existing Service's frontend when its backend pods are not yet Ready. (Backport PR cilium/cilium#45584, Upstream PR cilium/cilium#45522, @ysksuzuki)
- Fix dedicated Ingress reconciliation panic on invalid TLS passthrough rules (Backport PR cilium/cilium#45888, Upstream PR cilium/cilium#45737, @weizhoublue)
- Fix host L7 policy operation (Backport PR cilium/cilium#45496, Upstream PR cilium/cilium#45030, @atykhyy)
- Fix IPsec packet drops during rolling restart with key rotation by deferring SPI advertisement until XFRM states are ready (Backport PR cilium/cilium#45630, Upstream PR cilium/cilium#44701, @hbangT)
- Fix issue where datapath reinitialization may get stuck when triggered from the local API (Backport PR cilium/cilium#45630, Upstream PR cilium/cilium#45557, @jrife)
- Fix missing global service backends in Cluster Mesh when multiple service ports point to the same target port. (Backport PR cilium/cilium#45356, Upstream PR cilium/cilium#45179, @RiccardoAtzori91)
- fix(egressGateway): skip unmatched gateways when using multiple gateway (Backport PR cilium/cilium#45630, Upstream PR cilium/cilium#44705, @ieth0)
- fix(gateway-api): prevent silent disable on CRD discovery timeout (Backport PR cilium/cilium#45630, Upstream PR cilium/cilium#44662, @aslafy-z)
- fix(ipsec): panic in parseSPI on malformed input (Backport PR cilium/cilium#45496, Upstream PR cilium/cilium#44815, @isoyuki)
- Fixed intermittent ARP failures for LoadBalancer services caused by pointer reuse during BPF map iteration in the L2 responder reconciler. (Backport PR cilium/cilium#45673, Upstream PR cilium/cilium#45197, @Krishnachaitanyakc)
- Fixed SocketLB returning EPERM instead of EHOSTUNREACH when a Service has no backends. (Backport PR cilium/cilium#45673, Upstream PR cilium/cilium#45185, @chez-shanpu)
- Fixes an issue where L7 LoadBalancer and Ingress traffic would be dropped on certain kernel versions when Cilium is attached to a bridge network device. (Backport PR cilium/cilium#45755, Upstream PR cilium/cilium#45582, @liyihuang)
- Fixes dropped packets on ingress when full header not in linear skb area (Backport PR cilium/cilium#45496, Upstream PR cilium/cilium#45195, @javiercardona-work)
- hubble-relay: fix TLS config variable shadowing preventing cleanup on shutdown (Backport PR cilium/cilium#45630, Upstream PR cilium/cilium#45085, @Aprazor)
- policy: Fix CCG matching for duplicate label keys (Backport PR cilium/cilium#45356, Upstream PR cilium/cilium#45225, @christarazi)
- Fix Endpoint regeneration health reporting (Backport PR cilium/cilium#45630, Upstream PR cilium/cilium#45011, @fristonio)
- fix(deps): update k8s.io patch updates stable to v0.35.4 (v1.19) (patch) (cilium/cilium#45465, @cilium-renovate[bot])
- [v1.19] ipam: fix data race in MultiPoolManager node update (cilium/cilium#45521, @Kunalbehbud)

### 1.19.5

- wireguard:mtu: fix mtu calculation with potential padding (Backport PR cilium/cilium#46170, Upstream PR cilium/cilium#45940, @smagnani96)
- Always add cluster label to node when `nodeSelectorLabels` is enabled to fix CiliumNetworkPolicy with `fromNodes`/`toNodes` with `policy-default-local-cluster` enabled (enabled by default in 1.19+) (Backport PR cilium/cilium#46170, Upstream PR cilium/cilium#46068, @MrFreezeex)
- azure: Fix public IP reassignment failure loop on operator restart (Backport PR cilium/cilium#46289, Upstream PR cilium/cilium#46240, @HadrienPatte)
- bgp: Reduce amount of soft peer resets by service reconciliation and fix potentially missed incorrect metadata update upon failed reconciliation. (Backport PR cilium/cilium#46245, Upstream PR cilium/cilium#45927, @rastislavs)
- bpf: fix host proxy packet routing to pods (Backport PR cilium/cilium#46024, Upstream PR cilium/cilium#45916, @atykhyy)
- bug: fixed weighted backend traffic splitting for TLSRoute passthrough listeners in Gateway API (Backport PR cilium/cilium#46170, Upstream PR cilium/cilium#45937, @nickolaev)
- Fix a bug that causes the NamespaceSelector field in a CiliumEgressGatewayPolicy to be corrupted, and no longer effective. (Backport PR cilium/cilium#46024, Upstream PR cilium/cilium#45926, @julianwiedmann)
- Fix a rare bug in clustermesh-apiserver that triggers incorrect deletion of a valid endpoint entry from the etcd under high pod churn (Backport PR cilium/cilium#46170, Upstream PR cilium/cilium#45780, @adamwathieu)
- Fix BGP PeerConfig status cleanup so it no longer times out when there are no managed conditions to remove. (Backport PR cilium/cilium#46170, Upstream PR cilium/cilium#45967, @ysksuzuki)
- Fix bug that would disrupt node connectivity when ClusterIP/LoadBalancer VIPs overlapped with node-local IP addresses. (Backport PR cilium/cilium#46024, Upstream PR cilium/cilium#45572, @ajmmm)
- Fix TLS passthrough routes failing silently when a gateway has mixed HTTP, HTTPS, and TLS listeners and a TLSRoute with no sectionName. (Backport PR cilium/cilium#45966, Upstream PR cilium/cilium#45371, @syedazeez337)
- Fix wildcard namespace bypass for selectorless ipBlock rules (Backport PR cilium/cilium#46456, Upstream PR cilium/cilium#46305, @TheBeeZee)
- fix(gateway-api): Prevent controller panic during Gateway reconciliation when GatewayClass has an invalid or malformed spec.parametersRef. (Backport PR cilium/cilium#46400, Upstream PR cilium/cilium#46340, @arybolovlev)
- fix(gateway-api): set ready condition in endpointSlice to true (Backport PR cilium/cilium#46400, Upstream PR cilium/cilium#46237, @ulrichgiraud)
- fix: nil pointer dereference panic due to uninitialized logger (Backport PR cilium/cilium#46170, Upstream PR cilium/cilium#45782, @weizhoublue)
- Fixed a race where a reused endpoint ID could have its BPF state directory removed by the outgoing endpoint (Backport PR cilium/cilium#46554, Upstream PR cilium/cilium#46091, @eyupcanakman)
- Fixed unsolicited IPv6 L2 announcements ignored by receiving hosts, as not conformant to RFC 4861 (Backport PR cilium/cilium#46170, Upstream PR cilium/cilium#46079, @giorio94)
- Fixes a bug where policymap pressure was incorrectly being reported as 0. (Backport PR cilium/cilium#46024, Upstream PR cilium/cilium#45791, @squeed)
- gateway-api: fix GatewayClass field index (Backport PR cilium/cilium#46289, Upstream PR cilium/cilium#46127, @thorn3r)
- multipool: Fix retries for CiliumNode Get errors (Backport PR cilium/cilium#46408, Upstream PR cilium/cilium#46124, @pippolo84)
- sockets: fix nil pointer dereference in filterAndDestroySockets (Backport PR cilium/cilium#46024, Upstream PR cilium/cilium#44843, @umut-polat)
- fix the race condition for the TestRouterIDAllocation bgp test case (Backport PR cilium/cilium#46289, Upstream PR cilium/cilium#44545, @liyihuang)
- [v1.19] Backport health command fixes from 46102 (cilium/cilium#46250, @joamaki)
- Fix broken gateway-api documentation links (Backport PR cilium/cilium#46554, Upstream PR cilium/cilium#46527, @0xch4z)
- Fix pointer-address comparison for Gateway API Route ParentReference status handling (Backport PR cilium/cilium#46400, Upstream PR cilium/cilium#46355, @weizhoublue)
- fix(deps): update k8s.io patch updates stable to v0.35.5 (v1.19) (cilium/cilium#46140, @cilium-renovate[bot])
- fix(deps): update k8s.io patch updates stable to v0.35.5 (v1.19) (patch) (cilium/cilium#46015, @cilium-renovate[bot])
- fix(deps): update k8s.io patch updates stable to v0.35.6 (v1.19) (cilium/cilium#46562, @cilium-renovate[bot])
- fix(deps): update k8s.io/utils digest to ff6756f (v1.19) (cilium/cilium#45996, @cilium-renovate[bot])

### 1.19.6

- [v1.19] Fix policy service label selector handling (cilium/cilium#46946, @fristonio)
- bpf: fix ipv6 neighbor solicitation handling in host firewall (Backport PR cilium/cilium#46669, Upstream PR cilium/cilium#46325, @atykhyy)
- endpoint: Fix race when reading endpoint properties (Backport PR cilium/cilium#47181, Upstream PR cilium/cilium#46991, @gandro)
- Fix `cilium_operator_unmanaged_pods` gauge reporting 0 on reconcile cycles where an unmanaged pod is restarted. (Backport PR cilium/cilium#46975, Upstream PR cilium/cilium#46668, @Suyash1700)
- Fix a bug which could lead to stale hostport entries if a pod was deleted and immediately recreated in host network. (Backport PR cilium/cilium#46793, Upstream PR cilium/cilium#46747, @giorio94)
- Fix a regression that could cause established connections to a Pod to be briefly dropped during Cilium agent restart, upgrade, or downgrade, while the agent was restoring the Pod's network policy. (Backport PR cilium/cilium#46974, Upstream PR cilium/cilium#46927, @aanm)
- Fix allowedRoute namespace and kind restrictions on multi-listener Gateways. (Backport PR cilium/cilium#46826, Upstream PR cilium/cilium#45693, @eufriction)
- Fix bug that left the host firewall enabled in the live ConfigMap when disabling hostFirewall.enabled (toggling it from true to false) via Helm. (Backport PR cilium/cilium#46669, Upstream PR cilium/cilium#44748, @shibaPuppy)
- Fix ClusterMesh service affinity annotation `service.cilium.io/affinity: "none"` incorrectly dropping all remote backends, causing traffic blackhole when no local endpoints exist. (Backport PR cilium/cilium#46691, Upstream PR cilium/cilium#46635, @mkamadeus)
- Fix ctmap gc duration metric recording (Backport PR cilium/cilium#46975, Upstream PR cilium/cilium#46873, @fristonio)
- Fix incorrect policy denials for traffic to L7 load balanced services when remote identity changes (Backport PR cilium/cilium#47002, Upstream PR cilium/cilium#46821, @fristonio)
- Fix potential hangs caused by Netlink errors in filterAndDestroySockets. (Backport PR cilium/cilium#47181, Upstream PR cilium/cilium#46967, @ysksuzuki)
- Fix regression preventing Cilium from starting when configured in kvstore mode with KPR enabled, if etcd is behind a Kubernetes service (Backport PR cilium/cilium#47181, Upstream PR cilium/cilium#46444, @giorio94)
- Fix the UDP tunnel check in the BIG TCP probe. (Backport PR cilium/cilium#46793, Upstream PR cilium/cilium#46710, @gentoo-root)
- Fixes a bug where Hubble policy correlation does not work for port ranges. (Backport PR cilium/cilium#46793, Upstream PR cilium/cilium#46643, @squeed)
- operator: Fix nil-pointer panic in CiliumNode GC (Backport PR cilium/cilium#47181, Upstream PR cilium/cilium#47127, @HadrienPatte)
- Fix workflow change detection for single-commit PRs to main (Backport PR cilium/cilium#46793, Upstream PR cilium/cilium#46684, @Demiserular)
- Further GC ratchet test fix races (Backport PR cilium/cilium#47224, Upstream PR cilium/cilium#43075, @tommyp1ckles)
- bgp: fix status condition reporting: update reasons to accurately reflect current condition state (Backport PR cilium/cilium#46920, Upstream PR cilium/cilium#46383, @martonra)
- Fix instance of cilium having incorrect specified policy_change_total failure label "failure" value which caused unnecessary warnings. (Backport PR cilium/cilium#46793, Upstream PR cilium/cilium#46388, @tommyp1ckles)
- fix(deps): update k8s.io/utils digest to be93311 (v1.19) (cilium/cilium#46907, @cilium-renovate[bot])
- fix(deps): update k8s.io/utils digest to cf1189d (v1.19) (cilium/cilium#47115, @cilium-renovate[bot])
- Fixed Gateway API reconciler incorrectly reporting "Accepted HTTPRoute" in the status condition message for GRPCRoute and TLSRoute resources. (Backport PR cilium/cilium#46826, Upstream PR cilium/cilium#44962, @eufriction)
- v1.19: gateway-api: fix sds secrets in golden tests (cilium/cilium#47229, @0xch4z)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.19.6**, the newest release recorded here for this line.

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
