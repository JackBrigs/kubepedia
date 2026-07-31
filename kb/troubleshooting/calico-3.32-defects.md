---
id: TROUBLE-CALICO_3_32_DEFECTS
type: troubleshooting
title: "calico 3.32: defects fixed in the 3.32 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.32.0 <3.33.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - calico 3.32 known issues
  - calico 3.32 fixed in
  - is this calico bug already fixed
tags:
  - troubleshooting
  - upgrade
  - calico
sources:
  - type: docs
    path: projectcalico/calico release notes for the 3.32 line — bug-fix entries
    url: https://github.com/projectcalico/calico/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# calico 3.32: defects fixed in the 3.32 line

## Summary

**83 defects** the project fixed across **2 releases** of the 3.32 line, from 3.32.0 to
3.32.1. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.32.0

- Fixes an issue where calico-apiserver generated malformed OpenAPI schema definitions after the Kubernetes 1.35 dependency bump, which could cause ArgoCD and similar tools to fail schema validation. [calico 12637](https://github.com/projectcalico/calico/pull/12637) (@MichalFupso)
- Typha now rejects oversized inbound client gob frames before reading them, preventing a potential denial-of-service caused by excessive memory allocation. [calico 12590](https://github.com/projectcalico/calico/pull/12590) (@Behnam-Shobiri)
- Removed sensitive material (auth tokens, kubeconfig contents, etcd credentials, and inline certificates/keys) from log output. Logs that previously included full client-config or environment-variable dumps now log structured non-secret fields instead. [calico 12588](https://github.com/projectcalico/calico/pull/12588) (@Behnam-Shobiri)
- Fix LoadBalancer IPAM race on kube-controllers startup that could assign multiple addresses to a Service. [calico 12568](https://github.com/projectcalico/calico/pull/12568) (@MichalFupso)
- `calicoctl` no longer logs raw client config on startup, which previously included `K8sAPIToken`, inline kubeconfig, `EtcdPassword`, and inline etcd key/cert material. The replacement log entry reports only non-sensitive fields and boolean "set" indicators for each credential. [calico 12536](https://github.com/projectcalico/calico/pull/12536) (@Behnam-Shobiri)
- app-policy (Dikastes): normalize HTTP request-target before evaluating Application Layer Policy path rules, and reject shapes whose resolved form depends on upstream-specific decoding. Request paths are now RFC 3986 / RFC 7230 normalized (decode percent-escapes once, resolve dot-segments and repeated slashes, fold backslashes, strip matrix parameters per segment) and prefix matches are anchored to path-segment boundaries. Paths whose decoded form still contains percent-encoded path separators (%2e / %2f / %5c), or contains a null byte, are rejected. [calico 12532](https://github.com/projectcalico/calico/pull/12532) (@electricjesus)
- Sanitize CNI plugin log output. [calico 12526](https://github.com/projectcalico/calico/pull/12526) (@Behnam-Shobiri)
- Fixed a Felix eBPF cleanup race condition that could cause a nil-pointer panic when an interface disappeared during TC qdisc cleanup. [calico 12480](https://github.com/projectcalico/calico/pull/12480) (@Behnam-Shobiri)
- Use cryptographically secure random number generator for X.509 certificate serial numbers. [calico 12468](https://github.com/projectcalico/calico/pull/12468) (@Behnam-Shobiri)
- ebpf: Fix conntrack counter accounting for NAT-outgoing flows where bytes_in and packets_in were always zero. [calico 12323](https://github.com/projectcalico/calico/pull/12323) (@lucastigera)
- Fix a data race in Felix's BPF endpoint manager when comparing HostEndpoint protobuf messages, which could cause flaky race-detector failures or subtle logic errors under concurrent access. [calico 12174](https://github.com/projectcalico/calico/pull/12174) (@fasaxc)
- Fix goroutine leak after nflog reader restart. [calico 12159](https://github.com/projectcalico/calico/pull/12159) (@fasaxc)
- Fix a goroutine leak in Felix's interface monitor that could occur on netlink reconnect. [calico 12139](https://github.com/projectcalico/calico/pull/12139) (@fasaxc)
- Fix memory leak in routing table logic. The "interfaces to ARP" set was not properly cleaned out when an interface was removed, resulting in leaving old interface names in the set. [calico 12138](https://github.com/projectcalico/calico/pull/12138) (@fasaxc)
- Fix dikastes L7 application layer policy enforcement being broken since v3.30.0 due to missing ALPCheckProvider registration. [calico 11986](https://github.com/projectcalico/calico/pull/11986) (@electricjesus)
- ebpf: Fix kernel crash on UDP GSO FRAGLIST packets after partial bpf_skb_pull_data by fully linearizing the packet. Auto-detected via kernel version (fixed in 6.16+), overridable via FeatureDetectOverride. [calico 11920](https://github.com/projectcalico/calico/pull/11920) (@tomastigera)
- Fix advertisement of /32 LB IP addresses when not present in the Service Spec [calico 11917](https://github.com/projectcalico/calico/pull/11917) (@caseydavenport)
- LoadBalancer controller prevent nil pointer dereference in handleBlockUpdate [calico 11913](https://github.com/projectcalico/calico/pull/11913) (@MichalFupso)
- Fix calico-kube-controllers IPAM GC controller getting stuck when cleaning up nodes during rapid scale-down. [calico 11906](https://github.com/projectcalico/calico/pull/11906) (@caseydavenport)
- Fix failure to enable ingress bandwidth QoS controls when a non-default qdisc previously existed on the workload interface (handle != 0). [calico 11899](https://github.com/projectcalico/calico/pull/11899) (@coutinhop)
- Fix CNI delete timeout to start after IPAM lock acquisition, preventing "context deadline exceeded" failures during high pod churn [calico 11824](https://github.com/projectcalico/calico/pull/11824) (@sudheernv)
- Fix API server startup failure when configuring TLS 1.3-only cipher suites. The API server now supports the TLS_MIN_VERSION environment variable (values: "1.2" or "1.3") to control the minimum TLS version. Set TLS_MIN_VERSION=1.3 when using TLS 1.3-only cipher suites to avoid HTTP/2 cipher validation errors. [calico 11812](https://github.com/projectcalico/calico/pull/11812) (@KameHameHa21110)
- Fix BGP syncing on Windows [calico 11748](https://github.com/projectcalico/calico/pull/11748) (@rbrtbnfgl)
- Bugfix: fix rendering of NatPortRange option when using nftables. [calico 11736](https://github.com/projectcalico/calico/pull/11736) (@nelljerram)
- Fix that come components would add square brackets to IPv4s when forming host:port addresses (treating them like IPv6 addresses). [calico 11721](https://github.com/projectcalico/calico/pull/11721) (@fasaxc)
- Fix that the CNI plugin installer generated a malformed URL for IPv4 addresses. This bug was exposed by a fix to the golang URL parser. [calico 11713](https://github.com/projectcalico/calico/pull/11713) (@fasaxc)
- ebpf: fix - The eBPF dataplane regressed when switching to the flow based vxlan device and the VNI is always 0 regardless of the actual setting [calico 11692](https://github.com/projectcalico/calico/pull/11692) (@tomastigera)
- ebpf: fixed performance for UDP (QUIC/HTTP3) nodeports [calico 11653](https://github.com/projectcalico/calico/pull/11653) (@tomastigera)
- eBPF: fix that local workload with borrowed IPs lose connectivity [calico 11640](https://github.com/projectcalico/calico/pull/11640) (@fasaxc)
- ebpf - Fixed routing of fragmented packets from a pod with multiple host interfaces. [calico 11616](https://github.com/projectcalico/calico/pull/11616) (@sridhartigera)
- Don't uninstall CNI and kube-proxy service when using non-Calico CNI on Windows with operator install. [calico 11614](https://github.com/projectcalico/calico/pull/11614) (@coutinhop)
- Fix possible segmentation fault in IP address parsing code [calico 11602](https://github.com/projectcalico/calico/pull/11602) (@majiayu000)
- Restrict Calico ML2 leader election participation to the parent Neutron server process, preventing API and worker processes from becoming leader and reducing contention under high API load. [calico 11580](https://github.com/projectcalico/calico/pull/11580) (@chaowang987)
- ebpf: fix bug where ingress and egress policy program indexes were confused, resulting in cleaning up the wrong policy program. [calico 11565](https://github.com/projectcalico/calico/pull/11565) (@fasaxc)
- bpf: Fix IP fragment reassembly between 8,000 and 16,000 bytes. Offsets were miscalculated due to incorrect order of operations. [calico 11557](https://github.com/projectcalico/calico/pull/11557) (@fasaxc)
- Fix potential HEP / WEP chain name conflicts in IPVS mode. [calico 11541](https://github.com/projectcalico/calico/pull/11541) (@terror96)
- Fix race in EndpointSlice logic for BGP service advertisement [calico 11503](https://github.com/projectcalico/calico/pull/11503) (@sergeimonakhov)
- eBPF - Fixed map operations for older kernels. [calico 11482](https://github.com/projectcalico/calico/pull/11482) (@sridhartigera)
- Fix kube-controllers watch handling to avoid leaking watchers when the configuration watch is recreated. [calico 11433](https://github.com/projectcalico/calico/pull/11433) (@fusidic)
- eBPF - Fixed loading connecttime load balancer program in 6.12 kernel [calico 11399](https://github.com/projectcalico/calico/pull/11399) (@sridhartigera)
- Fix: IPPool CIDR Validation Fails on Semantically-Identical IPv6 CIDRs [calico 11385](https://github.com/projectcalico/calico/pull/11385) (@skoryk-oleksandr)
- OpenStack: don't force the MTU to 1500 in IPv6 router advertisements [calico 11380](https://github.com/projectcalico/calico/pull/11380) (@kristiangronas)
- Fix startup failure when using etcdv3 storage without any Kubernetes API server. [calico 11361](https://github.com/projectcalico/calico/pull/11361) (@Nativu5)
- Felix now explicitly sets priority 1024 for IPv6 routes instead of relying on kernel default, ensuring routes round-trip correctly when read from the kernel. [calico 11356](https://github.com/projectcalico/calico/pull/11356) (@Copilot)
- Re-create and swap out Calico ipsets that are not possible to list due to different failures like user-space/kernel incompatibility. [calico 11340](https://github.com/projectcalico/calico/pull/11340) (@mazdakn)
- Fix AllowSpoofedSourcePrefixes for dual stack clusters. [calico 11338](https://github.com/projectcalico/calico/pull/11338) (@sknat)
- OpenStack bugfix: request etcd compaction periodically regardless of how long resync takes, or if periodic resync is disabled. [calico 11306](https://github.com/projectcalico/calico/pull/11306) (@nelljerram)
- Fixes pending policy evaluation race post endpoint deletion [calico 11281](https://github.com/projectcalico/calico/pull/11281) (@dimitri-nicolo)
- ebpf: kube-proxy binds service health probes to node IPs instead of "any" [calico 11280](https://github.com/projectcalico/calico/pull/11280) (@tomastigera)
- Fixed a race in flow log generation that could mis-report service traffic as denied when a backing pod was deleted while the packet was being processed. [calico 11276](https://github.com/projectcalico/calico/pull/11276) (@dimitri-nicolo)
- fix (release-tool): include image tarballs in release archive file [calico 11253](https://github.com/projectcalico/calico/pull/11253) (@radTuti)
- ebpf: Do not adjust gso_size after nodeport tunnel vxlan decap. There is no guarantee that there would be enough data after removing tunnel headers. The packet is shrunk by 50 bytes while the gso_size would grow. Kernel would drop the packet if the original gso packet is too small. [calico 11252](https://github.com/projectcalico/calico/pull/11252) (@juliantaylor)
- Fix BGP advertisement of externalIP addresses on Services with type=ClusterIP. [calico 11204](https://github.com/projectcalico/calico/pull/11204) (@caseydavenport)
- CNI plugin: double-check the IPv6 LL address on the host side of the veth and refresh it if it seems wrong. Sometimes the kernel uses a stale MAC to calculate it. [calico 11182](https://github.com/projectcalico/calico/pull/11182) (@fasaxc)
- Fix IPAM block leak of older blocks when deleting IP pools. [calico 11179](https://github.com/projectcalico/calico/pull/11179) (@caseydavenport)
- ebpf: do not blindly redirect back to the same host iface - fixed regression from 3.29 to 3.30 [calico 11117](https://github.com/projectcalico/calico/pull/11117) (@tomastigera)
- Fix that empty source/destination EntityRules would serialize as '{}' instead of being omitted. Due to change of JSON library, this makes the errors reported for unexpected fields slightly less clear. [calico 11116](https://github.com/projectcalico/calico/pull/11116) (@fasaxc)
- Fix potential nil pointer dereference in load balancer IP allocation controller [calico 11092](https://github.com/projectcalico/calico/pull/11092) (@caseydavenport)
- Bugfix: reinstate support for VMs that are configured not to respond to ARP requests. [calico 11052](https://github.com/projectcalico/calico/pull/11052) (@nelljerram)
- Add missing staged policy permissions to apiserver.yaml [calico 11022](https://github.com/projectcalico/calico/pull/11022) (@caseydavenport)
- Various fixes for 32bit architectures. [calico 11009](https://github.com/projectcalico/calico/pull/11009) (@twz123)
- Fix slow IPAM release performance when releasing IPs from disabled or deleted pools (especially for bulk deletions like those done by IPAM GC). Consider disabled pools as potential IP owners and cache any loaded blocks for fast access. [calico 10973](https://github.com/projectcalico/calico/pull/10973) (@fasaxc)
- Update bundled Istio version to 1.29.2, including CVE fixes for moby/spdystream, prometheus/prometheus, and opentelemetry-go/otel/sdk. [calico 12581](https://github.com/projectcalico/calico/pull/12581) (@radixo)
- Calico now builds and publishes its own customized Istio images (`pilot`, `proxyv2`, `install-cni`, and `ztunnel`) with Calico-specific patches applied (DSCP magic-mark for transparent networking, plus CVE-fix dependency bumps). These were previously available only in Calico Enterprise. [calico 12039](https://github.com/projectcalico/calico/pull/12039) (@radixo)
- Applied code modernization with "go fix", this had a small impact on the Calico v1 APIs due to removing some invalid "omitempty" annotations on JSON fields. [calico 11864](https://github.com/projectcalico/calico/pull/11864) (@fasaxc)
- feat: push helm charts to OCI registry (`quay.io/calico/charts`) fix: use accurate created date for chart entry in helm index [calico 11626](https://github.com/projectcalico/calico/pull/11626) (@radTuti)
- Add support for configurable dnsPolicy in tigera-operator deployment to fix DNS circular dependency issues on AWS EKS. Users can now override the default ClusterFirstWithHostNet behavior by setting dnsPolicy: Default in values.yaml. This change maintains backward compatibility with existing deployments. [calico 11595](https://github.com/projectcalico/calico/pull/11595) (@kalavt)

### 3.32.1

- HELM: Fixes the tigera-operator chart install instructions, which omitted the step to install Calico CRDs from the separate crd.projectcalico.org.v1 chart. [calico 13043](https://github.com/projectcalico/calico/pull/13043) (@caseydavenport)
- Fix manifest-based installs missing kubevirt.io RBAC rules on the calico-cni-plugin and calico-kube-controllers ClusterRoles, which caused KubeVirt VM networking and IPAM garbage collection failures. [calico 12996](https://github.com/projectcalico/calico/pull/12996) (@song-jiang)
- Fixed a bug where Felix's periodic route resync did not detect (and repair) Calico-owned routes that had been modified in place by another process. Fixed unnecessary reprogramming of unchanged IPv6 multi-path routes on resync, and a corner case where removing an IPAM block route could trigger a spurious conntrack cleanup for a workload owning the block's network address. [calico 12958](https://github.com/projectcalico/calico/pull/12958) (@fasaxc)
- [v3.32] fix(felix): exclude LB-only IPPools from BPF in-pool route flag [calico 12953](https://github.com/projectcalico/calico/pull/12953) (@defo89)
- Fixes a NotFound error when using server-side apply (including Helm 4) to create Calico network policies that don't already exist. [calico 12906](https://github.com/projectcalico/calico/pull/12906) (@caseydavenport)
- Fixes a bug in the eBPF dataplane in which deleting and restoring the local Node resource and restarting Felix could leave the node unable to handle network traffic. [calico 12874](https://github.com/projectcalico/calico/pull/12874) (@tomastigera)
- Fix SNAT being skipped for traffic destined to LoadBalancer-only IPPools by excluding them from the all-ipam-pools ipset. [calico 12858](https://github.com/projectcalico/calico/pull/12858) (@defo89)
- ebpf - Fix kube-proxy losing the NodePort externalTrafficPolicy=Local route-fixup trigger after a syncer swap, which could cause stale NAT entries on remote backends. [calico 12743](https://github.com/projectcalico/calico/pull/12743) (@tomastigera)
- Fixes nft binary segfaults in calico/node and the Istio CNI install image when newer nftables is in use elsewhere on the host. [calico 12712](https://github.com/projectcalico/calico/pull/12712) (@caseydavenport)
- Fixed a regression introduced in v3.30 where `RouteSyncDisabled` flag was not being honored by `LinkAddressManager`. [calico 12707](https://github.com/projectcalico/calico/pull/12707) (@mazdakn)
- Fix server-side apply (FluxCD, ArgoCD, `kubectl apply --server-side`) failures on BGPConfiguration resources that set serviceLoadBalancerIPs, serviceExternalIPs, serviceClusterIPs, communities, or prefixAdvertisements. [calico 12705](https://github.com/projectcalico/calico/pull/12705) (@caseydavenport)
- ebpf - Fix transient NodePort connection failures when Felix restarts on a node receiving external NodePort traffic. [calico 12694](https://github.com/projectcalico/calico/pull/12694) (@tomastigera)
- Fixes a Felix panic that could occur when an IP set selector matched both a NetworkSet CIDR and workload IPs contained within it, with nftables as the active dataplane. [calico 12671](https://github.com/projectcalico/calico/pull/12671) (@caseydavenport)
- Fix that certain internal API key types were non-comparable, requiring workarounds in various places. [calico 11958](https://github.com/projectcalico/calico/pull/11958) (@fasaxc)
- Fix panic in calico/node on s390x architecture. [calico 11312](https://github.com/projectcalico/calico/pull/11312) (@vivkong)
- Prevent deletion of built-in tiers in CRD mode. [calico 12982](https://github.com/projectcalico/calico/pull/12982) (@caseydavenport)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.32.1**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `projectcalico/calico`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/calico.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
