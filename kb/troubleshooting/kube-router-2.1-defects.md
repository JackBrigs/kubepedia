---
id: TROUBLE-KUBE_ROUTER_2_1_DEFECTS
type: troubleshooting
title: "kube-router 2.1: defects fixed in the 2.1 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=2.1.0 <2.2.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kube-router 2.1 known issues
  - kube-router 2.1 fixed in
  - is this kube-router bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kube-router
sources:
  - type: docs
    path: cloudnativelabs/kube-router release notes for the 2.1 line — bug-fix entries
    url: https://github.com/cloudnativelabs/kube-router/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kube-router 2.1: defects fixed in the 2.1 line

## Summary

**31 defects** the project fixed across **4 releases** of the 2.1 line, from 2.1.0 to
2.1.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 2.1.0

- kube-router's init container now installs CNI plugins when they are missing. The location for these plugins can be controlled by setting the environment variable `HOST_BIN_PATH` within the init container, but will default to `/opt/cni/bin`. This is something that all major Kubernetes networking providers do, but kube-router has not done in the past. For more information on CNI plugins, please see: https://github.com/containernetworking/plugins
- kube-router now implements `.spec.healthCheckNodePort` which has long been a part of the [Kubernetes service specification](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.29/#servicespec-v1-core), but kube-router hasn't implemented it until now. This port is meant to give visibility about whether or not an endpoint for a service exists on a node to workloads outside the Kubernetes cluster. If a service endpoint is on the node, then this port returns a 200 HTTP response, otherwise it returns a 503 HTTP response if no endpoint exists on the node. By choosing a node that contains an endpoint, a client can ensure [source IP preservation](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/#preserving-the-client-source-ip)
- Hairpinning in kube-router is now fixed. kube-router now has a dedicated controller to ensuring that the `veth` interface inside the container is in promiscuous mode. This used to be handled by `kubelet` and then it was handled by `docker-shim` and then it was removed entirely. As far as I can tell, it was never ported to `containerd` or `cri-o`. Without this functionality, return traffic ends up getting black-holed before it is routed outside of the container. For more details see: https://github.com/cloudnativelabs/kube-router/commit/0f3714b9b758f24de0b1911c148bdba8d87de9b6
- Users can now specify `--metrics-addr` to choose the IP address that kube-router listens on when providing Prometheus metrics
- Users can now specify custom protocol timeouts for IPVS services exposed by kube-router `--service-tcp-timeout` - (default: `0s` preserves system value, typically 900 seconds) `--service-tcpfin-timeout` - (default: `0s` preserves system value, typically 120 seconds) `--service-udp-timeout` - (default: `0s` preserves system value, typically 300 seconds)
- kube-router now abides by the service label `service.kubernetes.io/service-proxy-name`. Setting this label to something other than `kube-router` will result in kube-router ignoring the service
- kube-router now honors `spec.internalTrafficPolicy` and implements `spec.externalTrafficPolicy` correctly. For more information see: https://kubernetes.io/docs/reference/networking/virtual-ips/#traffic-policies for more information
- - fix(manifests): add hostPID for hairpin `<Aaron U'Ren>`
- - fix(NSC): handle endpoint slice ready nil `<Aaron U'Ren>`
- - fix(hairpin): set hairpin_mode for veth iface `<Aaron U'Ren>`

### 2.1.1

- Fixes IPv6 network policy which has been substantially broken since v2.0.0. When IPv6 network policy was introduced, it was missed that iptables statements need to reference these sets via the `inet6` prefix in order to use them correctly. As such, most network policies were not correctly applying
- Fixes `--cleanup-config` mode which has been broken since v2.0.0 (please see docs for updated examples of how to run this from within a container)
- - fix(hairpin): rely on CNI hairpin mode `<Aaron U'Ren>`
- - fix(service_endpoints_sync): bail out of DSR when HostNetwork detected `<Aaron U'Ren>`
- - fix(linux_networking): add more information to errors `<Aaron U'Ren>`
- - fix(user-guide.md): update cleanup example `<Aaron U'Ren>`
- - fix(cleanup): add missing handlers for cleanup `<Aaron U'Ren>`
- - fix(node.go): improve logic for GetNodeObject `<Aaron U'Ren>`
- - fix(policy): generate ipv6 names correctly `<Aaron U'Ren>`
- - fix(policy.go): use new utility method ipSetName `<Aaron U'Ren>`
- - fix: wrong ipset name used by ip6tables. `<xujunjie-cover>`
- - fix(service_endpoints_sync.go): error to be indicative of failure type `<Aaron U'Ren>`
- - fix(DSR): setup DSR inside pod on local eps only `<Aaron U'Ren>`
- - fix: rt_tables -> rt-tables in daemonset examples `<Aaron U'Ren>`
- - fix(rt_tables): add path fallback logic `<Aaron U'Ren>`
- - doc(CONTRIBUTING.md): fix relative link `<Aaron U'Ren>`

### 2.1.2

- - fix(ipset): reset ipset handler before use `<Aaron U'Ren>`
- - fix(ipset.go): make IP families distinct in ipset handler `<Aaron U'Ren>`

### 2.1.3

- - fix(nsc): remove previous TCPMSS rules during setting up DSR `<Richard Kojedzinszky>`
- - fix(nsc): remove previous TCPMSS rules `<Aaron U'Ren>`
- - fix(nsc): TCPMSS rules are created per-service and for reply packets only `<Richard Kojedzinszky>`


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **2.1.3**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `cloudnativelabs/kube-router`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kube-router.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
