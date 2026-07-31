---
id: TROUBLE-KUBERNETES_1_35_DEFECTS
type: troubleshooting
title: "kubernetes 1.35: defects fixed in the 1.35 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.35.0 <1.36.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubernetes 1.35 known issues
  - kubernetes 1.35 fixed in
  - is this kubernetes bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubernetes
sources:
  - type: docs
    path: kubernetes/kubernetes release notes for the 1.35 line — bug-fix entries
    url: https://github.com/kubernetes/kubernetes/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubernetes 1.35: defects fixed in the 1.35 line

## Summary

**80 defects** the project fixed across **6 releases** of the 1.35 line, from 1.35.0 to
1.35.7. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.35.0

- Kube-apiserver: Fixed a `v1.34` regression in `CustomResourceDefinition` handling that incorrectly warned about unrecognized formats on number and integer properties. ([#133896](https://github.com/kubernetes/kubernetes/pull/133896), [@yongruilin](https://github.com/yongruilin)) [SIG API Machinery, Apps, Architecture, Auth, CLI, Cloud Provider, Contributor Experience, Network, Node and Scheduling]
- Kube-apiserver: Fixed a possible panic validating a custom resource whose `CustomResourceDefinition` indicates a status subresource exists, but which does not define a `status` property in the `openAPIV3Schema`. ([#133721](https://github.com/kubernetes/kubernetes/pull/133721), [@fusida](https://github.com/fusida)) [SIG API Machinery, Apps, Architecture, Auth, Autoscaling, CLI, Cloud Provider, Cluster Lifecycle, Etcd, Instrumentation, Network, Node, Release, Scheduling, Storage and Testing]
- Enabled the feature gate `ContainerRestartRules` by default. The `ContainerRestartRules` feature has been promoted to beta. Fixed a bug in this feature that caused probes to continue to run even if the container has terminated and is not restartable. ([#134631](https://github.com/kubernetes/kubernetes/pull/134631), [@yuanwang04](https://github.com/yuanwang04))
- DRA API: Fixed the `tolerations` field in exact and sub requests to drop properly when the `DRADeviceTaints` API is disabled. ([#132927](https://github.com/kubernetes/kubernetes/pull/132927), [@pohly](https://github.com/pohly))
- DRA Device Taints: Fixed toleration of `NoExecute`. Prior to this enhancement, tolerating a `NoExecute` did not work because the scheduler did not inform the eviction controller about the toleration, so the scheduled pod got evicted almost immediately. ([#134479](https://github.com/kubernetes/kubernetes/pull/134479), [@pohly](https://github.com/pohly)) [SIG Apps, Node, Scheduling and Testing]
- Fixed SELinux warning controller not emitting events on some SELinux label conflicts. ([#133425](https://github.com/kubernetes/kubernetes/pull/133425), [@jsafrane](https://github.com/jsafrane)) [SIG Apps, Storage and Testing]
- Fixed `replicaCount` calculation exceeding max `int32`. ([#126979](https://github.com/kubernetes/kubernetes/pull/126979), [@omerap12](https://github.com/omerap12)) [SIG Apps and Autoscaling]
- Fixed a Windows kube-proxy (winkernel) issue where stale `RemoteEndpoints` remained when a Deployment was referenced by multiple Services due to premature clearing of the `terminatedEndpoints` map. ([#135146](https://github.com/kubernetes/kubernetes/pull/135146), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]
- Fixed a bug in `ValidatingAdmissionPolicy` where schemas with `additionalProperties: true` could cause the kube-controller-manager to crash with a nil pointer exception. ([#135155](https://github.com/kubernetes/kubernetes/pull/135155), [@jpbetz](https://github.com/jpbetz))
- Fixed a bug in `kube-proxy` `nftables` mode (GA as of `v1.33`) which fails to determine if traffic originates from a local source on the node. The issue was caused by using the wrong meta `iif` instead of `iifname` for name based matches. ([#134024](https://github.com/kubernetes/kubernetes/pull/134024), [@jack4it](https://github.com/jack4it))
- Fixed a bug in `kube-scheduler` where pending pod preemption caused preemptor pods to be retried more frequently. ([#134245](https://github.com/kubernetes/kubernetes/pull/134245), [@macsko](https://github.com/macsko)) [SIG Scheduling and Testing]
- Fixed a bug that caused apiservers to send an inappropriate Content-Type request header to authorization, token authentication, imagepolicy admission, and audit webhooks when the alpha client-go feature gate "ClientsPreferCBOR" is enabled. ([#132960](https://github.com/kubernetes/kubernetes/pull/132960), [@benluddy](https://github.com/benluddy)) [SIG API Machinery and Node]
- Fixed a bug that caused duplicate validation when updating `PersistentVolumeClaims`, `VolumeAttachments` and `VolumeAttributesClasses`. ([#132549](https://github.com/kubernetes/kubernetes/pull/132549), [@gavinkflam](https://github.com/gavinkflam))
- Fixed a bug that caused duplicate validation when updating `Role` and `RoleBinding` resources. ([#132550](https://github.com/kubernetes/kubernetes/pull/132550), [@gavinkflam](https://github.com/gavinkflam))
- Fixed a bug that prevented allocating the same device that was previously consuming the `CounterSet` when both `DRAConsumableCapacity` and `DRAPartitionableDevices` were enabled. ([#134103](https://github.com/kubernetes/kubernetes/pull/134103), [@sunya-ch](https://github.com/sunya-ch))
- Fixed a bug that prevents scheduling the next pod when using the `DRAConsumableCapacity` feature. ([#133706](https://github.com/kubernetes/kubernetes/pull/133706), [@sunya-ch](https://github.com/sunya-ch))
- Fixed a bug to prevent segmentation fault from occurring when updating deeply nested JSON fields. ([#134381](https://github.com/kubernetes/kubernetes/pull/134381), [@kon-angelo](https://github.com/kon-angelo)) [SIG API Machinery and CLI]
- Fixed a bug where 64-bit IPv6 `ServiceCIDRs` allocated addresses outside the subnet range. ([#134193](https://github.com/kubernetes/kubernetes/pull/134193), [@hoskeri](https://github.com/hoskeri))
- Fixed a bug where Job status updates fail after resuming a Job that was previously started and suspended. The error message was: `status.startTime: Required value: startTime cannot be removed for unsuspended job`. ([#134769](https://github.com/kubernetes/kubernetes/pull/134769), [@dejanzele](https://github.com/dejanzele)) [SIG Apps and Testing]
- Fixed a bug where `AllocationMode: All` would not succeed if a resource pool contained `ResourceSlices` that were not targeting the current node. ([#134466](https://github.com/kubernetes/kubernetes/pull/134466), [@mortent](https://github.com/mortent))
- Fixed a bug where a deleted Pod in the binding phase continued to occupy space on the node in `kube-scheduler`. ([#134157](https://github.com/kubernetes/kubernetes/pull/134157), [@macsko](https://github.com/macsko)) [SIG Scheduling and Testing]
- Fixed a bug where high latency `kube-apiserver` caused scheduling throughput degradation. ([#134154](https://github.com/kubernetes/kubernetes/pull/134154), [@macsko](https://github.com/macsko))
- Fixed a bug where the health of a DRA resource was not reported in the Pod status if the resource claim was generated from a template or used a different local name in the Pod spec. ([#134875](https://github.com/kubernetes/kubernetes/pull/134875), [@Jpsassine](https://github.com/Jpsassine)) [SIG Node and Testing]
- Fixed a long-standing issue where `kubelet` rejected Pods with `NodeAffinityFailed` due to a stale informer cache. ([#134445](https://github.com/kubernetes/kubernetes/pull/134445), [@natasha41575](https://github.com/natasha41575))
- Fixed a panic in `kubectl api-resources` that occurred when the Discovery Client failed. ([#134833](https://github.com/kubernetes/kubernetes/pull/134833), [@rikatz](https://github.com/rikatz))
- Fixed a possible data race during metrics registration. ([#134390](https://github.com/kubernetes/kubernetes/pull/134390), [@liggitt](https://github.com/liggitt)) [SIG Architecture and Instrumentation]
- Fixed a spurious `namespace not found` error in default `v1.30+` configurations when using `ValidatingAdmissionPolicy` or `MutatingAdmissionPolicy` to intercept namespaced objects in newly-created namespaces. ([#135359](https://github.com/kubernetes/kubernetes/pull/135359), [@liggitt](https://github.com/liggitt))
- Fixed a startup probe race condition that caused main containers to remain stuck in "Initializing" state when sidecar containers with startup probes had failed initially but succeeded on restart in pods with `restartPolicy=Never`. ([#133072](https://github.com/kubernetes/kubernetes/pull/133072), [@AadiDev005](https://github.com/AadiDev005)) [SIG Node and Testing]
- Fixed an issue in asynchronous preemption: Scheduler now checks if preemption is ongoing for a Pod before initiating new preemption calls. ([#134730](https://github.com/kubernetes/kubernetes/pull/134730), [@ania-borowiec](https://github.com/ania-borowiec)) [SIG Scheduling and Testing]
- Fixed an issue that prevented restart policies and restart rules from being applied to static pods. ([#135031](https://github.com/kubernetes/kubernetes/pull/135031), [@yuanwang04](https://github.com/yuanwang04))
- Fixed an issue where requests for a config `FromClass` in the `ResourceClaim` status were not referenced. ([#134793](https://github.com/kubernetes/kubernetes/pull/134793), [@LionelJouin](https://github.com/LionelJouin))
- Fixed an issue where the `kubelet` `/configz` endpoint reported an incorrect value for `kubeletconfig.cgroupDriver` when the cgroup driver setting was received from the container runtime. ([#134743](https://github.com/kubernetes/kubernetes/pull/134743), [@marquiz](https://github.com/marquiz))
- Fixed an issue where the default `serviceCIDR` controller did not log events because the event broadcaster was shutdown during initialization. ([#133338](https://github.com/kubernetes/kubernetes/pull/133338), [@aojea](https://github.com/aojea))
- Fixed an issue with setting `distinctAttribute=nil` when the `DRAConsumableCapacity` feature gate is disabled. ([#134962](https://github.com/kubernetes/kubernetes/pull/134962), [@sunya-ch](https://github.com/sunya-ch))
- Fixed broken shell completion for API resources. ([#133771](https://github.com/kubernetes/kubernetes/pull/133771), [@marckhouzam](https://github.com/marckhouzam))
- Fixed incorrect behavior of preemptor pod when preemption of the victim takes long to complete. The preemptor pod should not be circling in scheduling cycles until preemption is finished. ([#134294](https://github.com/kubernetes/kubernetes/pull/134294), [@ania-borowiec](https://github.com/ania-borowiec)) [SIG Scheduling and Testing]
- Fixed missing `kubelet_volume_stats_*` metrics. ([#133890](https://github.com/kubernetes/kubernetes/pull/133890), [@huww98](https://github.com/huww98)) [SIG Instrumentation and Node]
- Fixed occasional schedule delays when a static `PersistentVolume` is created. ([#133929](https://github.com/kubernetes/kubernetes/pull/133929), [@huww98](https://github.com/huww98)) [SIG Scheduling and Storage]
- Fixed resource claims deallocation for extended resource when Pod completes. ([#134312](https://github.com/kubernetes/kubernetes/pull/134312), [@alaypatel07](https://github.com/alaypatel07)) [SIG Apps, Node and Testing]
- Fixed the kubelet to honor the `userNamespaces.idsPerPod` configuration, which was previously ignored. ([#133373](https://github.com/kubernetes/kubernetes/pull/133373), [@AkihiroSuda](https://github.com/AkihiroSuda)) [SIG Node and Testing]
- Fixed the replacement tag in APIs so it no longer acted as a selector for storage version. ([#135197](https://github.com/kubernetes/kubernetes/pull/135197), [@Jefftree](https://github.com/Jefftree))
- Fixed validation error when `ConfigFlags` includes `CertFile` and/or `KeyFile` while the original configuration also contains `CertFileData` and/or `KeyFileData`. ([#133917](https://github.com/kubernetes/kubernetes/pull/133917), [@n2h9](https://github.com/n2h9)) [SIG API Machinery and CLI]
- Kube-apiserver: Fixed a `v1.34` regression with spurious "Error getting keys" log messages. ([#133817](https://github.com/kubernetes/kubernetes/pull/133817), [@serathius](https://github.com/serathius)) [SIG API Machinery and Etcd]
- Kube-apiserver: Fixed a possible `v1.34` performance regression calculating object size statistics for resources not served from the watch cache, typically only `Events`. ([#133873](https://github.com/kubernetes/kubernetes/pull/133873), [@serathius](https://github.com/serathius)) [SIG API Machinery and Etcd]
- Kube-controller-manager: Fixed a possible data race in the garbage collection controller. ([#134379](https://github.com/kubernetes/kubernetes/pull/134379), [@liggitt](https://github.com/liggitt)) [SIG API Machinery and Apps]
- Kubeadm: Fixed `KUBEADM_UPGRADE_DRYRUN_DIR` not honored in upgrade phase when writing kubelet config files. ([#134007](https://github.com/kubernetes/kubernetes/pull/134007), [@carlory](https://github.com/carlory))
- Kubeadm: Fixed a bug where `ClusterConfiguration.APIServer.TimeoutForControlPlane` from `v1beta3` was not respected in newer kubeadm versions where `v1beta4` is the default. ([#133513](https://github.com/kubernetes/kubernetes/pull/133513), [@tom1299](https://github.com/tom1299))
- Kubeadm: Fixed a bug where the node registration information for a given node was not fetched correctly during `kubeadm upgrade node` and the node name can end up being incorrect in cases where the node name is not the same as the host name. ([#134319](https://github.com/kubernetes/kubernetes/pull/134319), [@neolit123](https://github.com/neolit123))
- Kubeadm: Fixed a preflight check that could fail hostname construction in IPv6 setups. ([#134588](https://github.com/kubernetes/kubernetes/pull/134588), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Auth, Cloud Provider, Cluster Lifecycle and Testing]
- Kubelet: Fixed a concurrent map write error when creating a pod with an empty volume while the `LocalStorageCapacityIsolationFSQuotaMonitoring` feature gate is enabled. ([#135174](https://github.com/kubernetes/kubernetes/pull/135174), [@carlory](https://github.com/carlory))
- Kubelet: Fixed an internal deadlock that caused the connection to a DRA driver to become unusable after being idle for 30 minutes. ([#133926](https://github.com/kubernetes/kubernetes/pull/133926), [@pohly](https://github.com/pohly))
- `kube-controller-manager`: Fixed a `v1.34` regression that triggered a spurious rollout of existing StatefulSets when upgrading the control plane from `v1.33` to `v1.34`. This fix is guarded by the `StatefulSetSemanticRevisionComparison` feature gate, which is enabled by default. ([#135017](https://github.com/kubernetes/kubernetes/pull/135017), [@liggitt](https://github.com/liggitt))
- Fixes a bug where `MutatingAdmissionPolicy` would fail to apply to objects with duplicate list items (like env vars). ([#135560](https://github.com/kubernetes/kubernetes/pull/135560), [@lalitc375](https://github.com/lalitc375) [SIG API Machinery]
- K8s.io/client-go: Fixes a regression in 1.34+ which prevented informers from using configured Transformer functions. ([#135580](https://github.com/kubernetes/kubernetes/pull/135580), [@serathius](https://github.com/serathius) [SIG API Machinery]
- Fixed `nfacct` test cases on s390x. ([#133603](https://github.com/kubernetes/kubernetes/pull/133603), [@saisindhuri91](https://github.com/saisindhuri91))
- Kube-apiserver: Fixed an issue where passing invalid `DeleteOptions` incorrectly returned a 500 status instead of 400. ([#133358](https://github.com/kubernetes/kubernetes/pull/133358), [@ostrain](https://github.com/ostrain))
- Fix a bug in the kube-apiserver where a malformed Service without name can cause high CPU usage. The bug is present on the new Cluster IP allocators enabled with the feature MultiCIDRServiceAllocator (enabled by default since 1.33)

### 1.35.1

- Fixed SELinux warning controller not to emit events for completed pods. ([#136098](https://github.com/kubernetes/kubernetes/pull/136098), [@jsafrane](https://github.com/jsafrane)) [SIG Apps, Storage and Testing]
- Fixed a 1.35.0 regression by disabling the `SchedulerAsyncAPICalls` feature gate. The regression was in scheduler performance, triggered by API client throttling. ([#135904](https://github.com/kubernetes/kubernetes/pull/135904), [@macsko](https://github.com/macsko)) [SIG Scheduling]
- Fixed a panic in `kubectl exec` when the terminal size queue delegate is uninitialized. ([#136280](https://github.com/kubernetes/kubernetes/pull/136280), [@seekskyworld](https://github.com/seekskyworld)) [SIG CLI]
- Fixed an issue in the Windows kube-proxy (winkernel) where IPv4 and IPv6 Service load balancers could be incorrectly shared, causing broken dual-stack Service behavior. The kube-proxy now tracks load balancers per IP family, enabling correct support for PreferDualStack and RequireDualStack Services on Windows nodes. ([#136373](https://github.com/kubernetes/kubernetes/pull/136373), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]
- Fixed kubelet logging to properly respect verbosity levels. Previously, some debug/info messages using V().Error() would always be printed regardless of the configured log verbosity. ([#136432](https://github.com/kubernetes/kubernetes/pull/136432), [@thc1006](https://github.com/thc1006)) [SIG Node]
- Fixes a 1.29 regression in the apiserver_watch_events_sizes metric to report total outgoing watch traffic again ([#135815](https://github.com/kubernetes/kubernetes/pull/135815), [@mborsz](https://github.com/mborsz)) [SIG API Machinery]
- Fixes a 1.34 regression starting pods with environment variables with a value containing `$` followed by a multi-byte character ([#136491](https://github.com/kubernetes/kubernetes/pull/136491), [@AutuSnow](https://github.com/AutuSnow)) [SIG Architecture and Node]
- Fixes a 1.34+ regression in ipvs and winkernel kube-proxy backends; these are now reverted back to their pre-1.34 behavior of regularly rechecking all of their rules even when no Services or EndpointSlices change. ([#136122](https://github.com/kubernetes/kubernetes/pull/136122), [@danwinship](https://github.com/danwinship)) [SIG Network, Testing and Windows]
- Kubeadm: fix a bug where kubeadm upgrade is failed if the content of the `kubeadm-flags.env` file is `KUBELET_KUBEADM_ARGS=""` ([#136131](https://github.com/kubernetes/kubernetes/pull/136131), [@carlory](https://github.com/carlory)) [SIG Cluster Lifecycle]

### 1.35.4

- Fixed a bug where, after a kubelet restart, regular containers in a pod with a sidecar (initContainer with restartPolicy: Always) and a startupProbe failed to restart after crashing. Affected pods remained stuck with RestartCount: 0 indefinitely. ([#137885](https://github.com/kubernetes/kubernetes/pull/137885), [@HirazawaUi](https://github.com/HirazawaUi)) [SIG Node and Testing]
- Fixed device plugin test failures after kubelet restart. ([#138042](https://github.com/kubernetes/kubernetes/pull/138042), [@zxqlxy](https://github.com/zxqlxy)) [SIG Node and Testing]
- Fixes a 1.34+ regression reporting apiserver request latency annotation in the audit log when request took more than 500ms ([#136281](https://github.com/kubernetes/kubernetes/pull/136281), [@chaochn47](https://github.com/chaochn47)) [SIG API Machinery]
- Fixes a 1.35 regression in StatefulSet Parallel pod management by disabling the MaxUnavailableStatefulSet feature by default. ([#137926](https://github.com/kubernetes/kubernetes/pull/137926), [@soltysh](https://github.com/soltysh)) [SIG Apps]
- Fixes kube-proxy's nftables mode to work on systems with nft 1.1.3. ([#137807](https://github.com/kubernetes/kubernetes/pull/137807), [@danwinship](https://github.com/danwinship)) [SIG Network]

### 1.35.5

- Fixed a scheduler bug where replacing a Pod with the same name during a failed scheduling attempt could leave stale in-flight queue state and unbounded growth of in-flight event tracking. The scheduler now clears in-flight state using the UID from the scheduling attempt, not only the UID on the refreshed Pod object. ([#138434](https://github.com/kubernetes/kubernetes/pull/138434), [@Argh4k](https://github.com/Argh4k)) [SIG Scheduling]
- Fixed stale remote HNS endpoint cleanup on Windows when a pod IP is reused across nodes in L2Bridge networks, preventing DNS timeouts caused by traffic being routed to the wrong node. ([#138602](https://github.com/kubernetes/kubernetes/pull/138602), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]

### 1.35.6

- Fixed a bug where Pods that share multi-node claims and also have per-node claims can get stuck in Pending. ([#139362](https://github.com/kubernetes/kubernetes/pull/139362), [@nojnhuh](https://github.com/nojnhuh)) [SIG Node and Scheduling]
- Fixed a kube-scheduler panic when a DRA ResourceClaim using `allocationMode: All` selects a device that consumes shared counters. ([#138989](https://github.com/kubernetes/kubernetes/pull/138989), [@pohly](https://github.com/pohly)) [SIG Node]
- Fixed a panic in the endpoint controller when processing services with empty IPFamilies field (pre-dual-stack services that were never spec-updated). ([#139234](https://github.com/kubernetes/kubernetes/pull/139234), [@rahulbabu95](https://github.com/rahulbabu95)) [SIG Apps and Network]
- Fixed an issue where kubelet would delete the CSI mount directory when a periodic NodePublishVolume call (triggered by CSIDriver.spec.requiresRepublish=true) returned an error, leaving the pod with stale volume contents that subsequent successful republishes could not repair. ([#139229](https://github.com/kubernetes/kubernetes/pull/139229), [@aramase](https://github.com/aramase)) [SIG Storage]
- Fixes a 1.34+ regression handling containers with environment values set from Secret API objects containing binary non-utf8 data. ([#139193](https://github.com/kubernetes/kubernetes/pull/139193), [@liggitt](https://github.com/liggitt)) [SIG Node]
- Kubeadm: fixed kubeadm init phase certs --dry-run to correctly copy existing CA files. ([#139447](https://github.com/kubernetes/kubernetes/pull/139447), [@HirazawaUi](https://github.com/HirazawaUi)) [SIG Cluster Lifecycle]

### 1.35.7

- Kubeadm: fix MemberPromote to skip the etcd promote API call when the member is already a voting member, avoiding unnecessary retries and timeout. ([#138492](https://github.com/kubernetes/kubernetes/pull/138492), [@wgkingk](https://github.com/wgkingk)) [SIG Cluster Lifecycle]


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.35.7**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `kubernetes/kubernetes`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/kubernetes.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
