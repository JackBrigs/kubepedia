---
id: TROUBLE-CILIUM_1_7_DEFECTS
type: troubleshooting
title: "cilium 1.7: defects fixed in the 1.7 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.7.0 <1.8.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.7 known issues
  - cilium 1.7 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.7 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.7: defects fixed in the 1.7 line

## Summary

**83 defects** the project fixed across **12 releases** of the 1.7 line, from 1.7.5 to
1.7.16. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.7.5

- Avoid duplication of generated toCIDRs when using a toServices based CNP (or CCNP) (Backport PR #11971, Upstream PR #11901, @aanm)
- endpoint: Fix data races while accessing GetIdentity() (Backport PR #11971, Upstream PR #11941, @tgraf)
- Fix issue when Cilium randomly stops doing service translation in k8s 1.18 (Backport PR #12019, Upstream PR #11947, @aanm)
- Fix issue where Cilium-agent fails to start on nodes without a default gateway (Backport PR #11855, Upstream PR #11632, @soumynathan)
- Fix issue where traffic from a pod could be dropped despite allow policy when DNS L7 rules are used (Backport PR #11855, Upstream PR #11764, @joestringer)
- Fix leaking endpoint state metric (Backport PR #11930, Upstream PR #11884, @christarazi)
- Fix pre-flight deployment for users upgrading from < 1.7 (Backport PR #11630, Upstream PR #11599, @aanm)
- fix transparent encryption related bugs (Backport PR #12019, Upstream PR #11974, @jrfastab)
- ipcache: Fix deadlock when ipcache GC results in datapath reload (Backport PR #11971, Upstream PR #11950, @tgraf)
- service: Fix wrong localEndpoints count in HealthCheckNodePort (Backport PR #11906, Upstream PR #11863, @gandro)
- Fix flaky assertion on metrics (Backport PR #11971, Upstream PR #11966, @christarazi)
- agent: Fix data race when accessing d.monitorAgent (Backport PR #11855, Upstream PR #11823, @tgraf)
- Correct cidr input in linuxRouting.NewRoutingInfo (Backport PR #11855, Upstream PR #11569, @sayboras)
- Fix various data races in pkg/aws/eni and pkg/ipam (Backport PR #11766, Upstream PR #11685, @christarazi)
- install: Fix erroneous comment (Backport PR #11855, Upstream PR #11603, @joestringer)
- policy: Fix rule translation test flake (Backport PR #11971, Upstream PR #11913, @joestringer)

### 1.7.6

- avoid having endpoints in 'restoring' state in case the connectivity with the KVStore is not reliable (Backport PR #12333, Upstream PR #12307, @aanm)
- cilium: fix encryption flow labels in ip6 case (Backport PR #12056, Upstream PR #12015, @jrfastab)
- Fix bug where etcd session renew would block indefinitely, causing endpoint provision to fail (Backport PR #12333, Upstream PR #12292, @joestringer)
- Fix bug where identity allocation wouldn't cancel from api timeouts (Backport PR #12350, Upstream PR #12328, @joestringer)
- Fix setting monitorAggregationLevel to max reflects via CLI (Backport PR #12333, Upstream PR #12014, @soumynathan)
- Fix silent cilium monitor on systems with offline CPUs (Backport PR #12363, Upstream PR #12310, @pchaigno)
- Fix syslog hook missing in DefaultLogger (Backport PR #12333, Upstream PR #12170, @ArthurChiao)
- helm/operator: fix IPv6 liveness probe address for operator (Backport PR #12333, Upstream PR #12223, @Rolinh)
- make: fix LOCKDEBUG env variable reference for docker-plugin-image (Backport PR #12333, Upstream PR #12318, @Rolinh)
- ginkgo-ext: Fix data-race in Writer (Backport PR #12333, Upstream PR #12025, @gandro)
- Fix GKE Helm options for CI and docs. (Backport PR #12333, Upstream PR #12087, @jrajahalme)
- Fix native routing cidr missing flag in daemon (Backport PR #12354, Upstream PR #12180, @aanm)
- fqdn: Fix panic on MarshalJSON (#12224, @tklauser)

### 1.7.7

- Fix issue where Cilium could crash on startup with "can't create perf event: no such device". (Backport PR #12459, Upstream PR #12068, @tklauser)
- bpf: Fix monitor aggregation for 'from-network' (Backport PR #12613, Upstream PR #12559, @joestringer)
- cilium: fix helm usage of enableIdentityMap -> enableIdentityMark (Backport PR #12458, Upstream PR #12194, @jrfastab)
- etcd: Fix firstSession error handling (Backport PR #12774, Upstream PR #12773, @tgraf)
- etcd: Fix session renewal controllers (Backport PR #12613, Upstream PR #12553, @tgraf)
- etcd: Fix several etcd related issues (Backport PR #12622, Upstream PR #12605, @tgraf)
- Fix etcd failure behavior when user or client context ends (Backport PR #12613, Upstream PR #12587, @tgraf)
- Fix manual endpoint regeneration via command line (Backport PR #12613, Upstream PR #12524, @christarazi)
- Fix string slice type CLI arguments (Backport PR #12613, Upstream PR #12457, @JieJhih)
- Fix toGroups CRD to address validation errors (Backport PR #12622, Upstream PR #12440, @lbernail)
- travis:fix up TestShuffle failure on Arm64 (Backport PR #12613, Upstream PR #12515, @Jianlin-lv)
- contrib: fix branch check in `start-backport` script (Backport PR #12458, Upstream PR #12361, @Rolinh)
- contrib: Fix submit-backport PR set-labels detection (Backport PR #12723, Upstream PR #11912, @joestringer)
- ipcache: Fix unit test flake (#12734, @joestringer)

### 1.7.8

- fix: node-init restartPods should use docker if /etc/crictl.yaml not found (Backport PR #12992, Upstream PR #12894, @UnwashedMeme)
- avoid schedule cilium-operator pods in same node for HA mode (Backport PR #12760, Upstream PR #12771, @aanm)
- datapath: Fix ICMP ECHO tuple ports (Backport PR #12760, Upstream PR #12729, @brb)
- Fix bug in ENI environments where connections to NodePort would fail due to asymmetric routing (Backport PR #13010, Upstream PR #12770, @qmonnet)
- Fix bug where cilium-health reports connectivity failures to stale IPs (Backport PR #13002, Upstream PR #12989, @kkourt)
- operator: Fix non-leader crashing with kvstore (Backport PR #12838, Upstream PR #12825, @christarazi)
- Fix packet loss issues when running Cilium v1.6 and v1.7 in the same cluster concurrently with --enable-remote-node-identity=false (#12999, @joestringer)
- v1.7 doc: hubble namespace fix for GKE (#12966, @kAworu)

### 1.7.9

- Fix v1.7.7 upgrade, add flags to help hitless upgrade from v1.6.x to v1.7.x (#13038, @joestringer)

### 1.7.10

- daemon: Fix handling of policy call map on downgrades (#13052, @pchaigno)
- Fix bug in operator where the operator instances in HA mode can become inconsistent in terms of running mode(HA/non HA), if kube-apiserver is not accessible when deriving k8s capabilities. (Backport PR #13247, Upstream PR #13219, @fristonio)
- Fix bug where Hubble and the Cilium CLI would fail to resolve security identities across a cluster mesh. (Backport PR #13209, Upstream PR #13205, @gandro)
- Fix endpoint selection for a wildcard to/fromEndpoints in CCNP. Cilium will only allow access from Cilium-managed endpoints in such cases instead of allowing traffic from any source. Preflight checks, when following the upgrade guide, have been extended to warn users of the new behavior. (Backport PR #13127, Upstream PR #12890, @fristonio)
- Fix panic when restoring services with enable-health-check-nodeport: false (Backport PR #13209, Upstream PR #13190, @gandro)
- Fix the creation of "toGroups" derivative policies for "CiliumClusterwideNetworkPolicies". (Backport PR #13127, Upstream PR #12920, @fristonio)
- operator: fix invocation with `--help` option (Backport PR #13209, Upstream PR #13141, @tklauser)
- fix(12664): initialize gops in RootCmd execution function (Backport PR #13209, Upstream PR #12675, @fristonio)
- Prevent Cilium from deleting all custom resources especially CNP & CCNP installed inside the cluster (Backport PR #13292, Upstream PR #13272, @christarazi)

### 1.7.11

- contexthelpers: Fix deadlock when nobody recvs on success channel (Backport PR #13441, Upstream PR #13408, @brb)
- Fix bug where Cilium leaks a goroutine when an endpoint is deleted. This leak, if left running in a high pod churn environment, can cause Cilium to exceed its memory usage and get OOM killed. (Backport PR #13690, Upstream PR #13683, @christarazi)
- identity: Fix nil pointer panic in LookupIdentityByID (Backport PR #13595, Upstream PR #13514, @gandro)
- metrics: fix negative identity count (Backport PR #13721, Upstream PR #12313, @ArthurChiao)
- Fix race condition in DeepEqual function (Backport PR #13491, Upstream PR #13472, @aanm)
- Follow-up fixes for the API rate limiter (Backport PR #13477, Upstream PR #13450, @tgraf)

### 1.7.12

- Fixed Goroutine leak for unresponded ARP pings. (Backport PR #14247, Upstream PR #14222, @jrajahalme)
- fqdn: Fix confusion of ToFQDNs vs. DNS rules. (Backport PR #14068, Upstream PR #14012, @jrajahalme)

### 1.7.13

- routing: Fix route collisions in AWS ENI (#14337, @christarazi)
- cilium-cni: Fix error handling for bad netns (Backport PR #14669, Upstream PR #14645, @joestringer)
- Fix bug where Cilium endpoints are not cleaned up, eventually leading to IP exhaustion despite a small number of endpoints on the node. (#14541, @joestringer)
- Fix bug where Cilium would constantly regenerate endpoints in environments with etcd and Linux 4.15 or below. (Backport PR #14440, Upstream PR #14300, @dctrwatson)
- Fix CIDR rule bug potentially dropping allowed traffic when using ExceptCIDRs expressions. (Backport PR #14669, Upstream PR #14516, @jrajahalme)
- Fix possible overflow in values presented in the `k8s_event_lag_seconds` metric. (Backport PR #14440, Upstream PR #14313, @aanm)

### 1.7.14

- Fix memory leak on stable policy identity churn. (Backport PR #15045, Upstream PR #15042, @jrajahalme)
- [v1.7] release: Fix script to check presence of docker images (#14777, @joestringer)
- add GH action to push hot fix images into -dev repositories (#15064, @aanm)

### 1.7.15

- Fix ICMP Echo ID placement in CT maps (#15271, @brb)

### 1.7.16

- Fix possible deadlock when querying network interfaces for arping (#15430, @brb)
- Fix channel panic from ipcache kvstore reconnect (Backport PR #15767, Upstream PR #15668, @jomenxiao)
- contrib: fix remote overriding (Backport PR #15401, Upstream PR #15328, @kaworu)
- Documentation: fix key rotation command in encryption guide (Backport PR #15401, Upstream PR #15365, @mauriciovasquezbernal)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.7.16**, the newest release recorded here for this line.

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
