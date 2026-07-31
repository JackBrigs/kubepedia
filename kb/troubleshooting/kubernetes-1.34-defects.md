---
id: TROUBLE-KUBERNETES_1_34_DEFECTS
type: troubleshooting
title: "kubernetes 1.34: defects fixed in the 1.34 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.34.0 <1.35.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubernetes 1.34 known issues
  - kubernetes 1.34 fixed in
  - is this kubernetes bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubernetes
sources:
  - type: docs
    path: kubernetes/kubernetes release notes for the 1.34 line — bug-fix entries
    url: https://github.com/kubernetes/kubernetes/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubernetes 1.34: defects fixed in the 1.34 line

## Summary

**79 defects** the project fixed across **9 releases** of the 1.34 line, from 1.34.0 to
1.34.10. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.34.0

- Fixed a 1.33 regression that causes a nil panic in kube-scheduler when aggregating resource requested across container's spec and status. ([#132895](https://github.com/kubernetes/kubernetes/pull/132895), [@yue9944882](https://github.com/yue9944882)) [SIG Node and Scheduling]
- Fixed prerelease lifecycle for `PodCertificateRequest`. ([#133350](https://github.com/kubernetes/kubernetes/pull/133350), [@carlory](https://github.com/carlory))
- DRA kubelet: Fixed the kubelet to also clean up `ResourceSlices` in some additional failure scenarios (driver was removed forcibly or crashed and did not restart). ([#132058](https://github.com/kubernetes/kubernetes/pull/132058), [@pohly](https://github.com/pohly)) [SIG Node and Testing]
- Fixed recording the `kubelet_container_resize_requests_total` metric to include all resize-related updates. ([#133060](https://github.com/kubernetes/kubernetes/pull/133060), [@natasha41575](https://github.com/natasha41575))
- Kubeadm: Fixed an issue where etcd member promotion failed with an error indicating the member was already promoted. ([#130782](https://github.com/kubernetes/kubernetes/pull/130782), [@BernardMC](https://github.com/BernardMC))
- DRA driver helper: Fixed handling of apiserver restart when running on a Kubernetes version which did not support the `resource.k8s.io` version used by the DRA driver. ([#133076](https://github.com/kubernetes/kubernetes/pull/133076), [@pohly](https://github.com/pohly)) [SIG Node and Testing]
- Fixed e2e test "[Driver: csi-hostpath] [Testpattern: Dynamic PV (filesystem volmode)] volumeLimits should support volume limits" not to leak Pods and namespaces. ([#132674](https://github.com/kubernetes/kubernetes/pull/132674), [@jsafrane](https://github.com/jsafrane)) [SIG Storage and Testing]
- DRA: Ensured that ResourceClaims requesting a fixed number of devices with `adminAccess` were no longer allocated the same device multiple times. ([#131299](https://github.com/kubernetes/kubernetes/pull/131299), [@nojnhuh](https://github.com/nojnhuh))
- Fixed API response for `StorageClassList` queries to return a graceful error message, if the provided `ResourceVersion` is too large. ([#132374](https://github.com/kubernetes/kubernetes/pull/132374), [@PatrickLaabs](https://github.com/PatrickLaabs)) [SIG API Machinery and Etcd]
- Fixed ReplicationController reconciliation when the `DeploymentReplicaSetTerminatingReplicas` feature gate was enabled. ([#131822](https://github.com/kubernetes/kubernetes/pull/131822), [@atiratree](https://github.com/atiratree))
- Fixed a bug in CEL's common.UnstructuredToVal where `==` evaluates to false for identical objects when a field is present but the value is null. This bug does not impact the Kubernetes API. ([#131559](https://github.com/kubernetes/kubernetes/pull/131559), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery]
- Fixed a bug in the Job controller that could result in creating unnecessary Pods for Jobs already marked as finished (either successful or failed). ([#130333](https://github.com/kubernetes/kubernetes/pull/130333), [@kmala](https://github.com/kmala)) [SIG Apps and Testing]
- Fixed a bug that caused an unexpected delay in creating Pods for newly created Jobs. ([#132109](https://github.com/kubernetes/kubernetes/pull/132109), [@linxiulei](https://github.com/linxiulei)) [SIG Apps and Testing]
- Fixed a bug that caused duplicate validation when updating a ReplicaSet. ([#131873](https://github.com/kubernetes/kubernetes/pull/131873), [@gavinkflam](https://github.com/gavinkflam)) [SIG Apps]
- Fixed a bug that fails to create a replica set when a deployment name is too long. ([#132560](https://github.com/kubernetes/kubernetes/pull/132560), [@hdp617](https://github.com/hdp617)) [SIG API Machinery and Apps]
- Fixed a bug that the async preemption feature keeps preemptor pods unnecessarily in the queue. ([#133167](https://github.com/kubernetes/kubernetes/pull/133167), [@sanposhiho](https://github.com/sanposhiho)) [SIG Scheduling]
- Fixed a panic issue related to kubectl revision history kubernetes/kubectl#1724 ([#130503](https://github.com/kubernetes/kubernetes/pull/130503), [@tahacodes](https://github.com/tahacodes)) [SIG CLI]
- Fixed a possible deadlock in the watch client that could happen if the watch was not stopped. ([#131266](https://github.com/kubernetes/kubernetes/pull/131266), [@karlkfi](https://github.com/karlkfi)) [SIG API Machinery]
- Fixed a regression introduced in 1.33 where some paginated LIST calls fell back to `etcd` instead of being served from cache. ([#132244](https://github.com/kubernetes/kubernetes/pull/132244), [@hakuna-matatah](https://github.com/hakuna-matatah))
- Fixed an incorrect reference to `JoinConfigurationKind` in the error message when no ResetConfiguration is found during `kubeadm reset` with the `--config` flag. ([#132258](https://github.com/kubernetes/kubernetes/pull/132258), [@J3m3](https://github.com/J3m3)) [SIG Cluster Lifecycle]
- Fixed an issue that allowed Custom Resources to be created using Server-Side Apply even when their `CustomResourceDefinition` was terminating. ([#132467](https://github.com/kubernetes/kubernetes/pull/132467), [@sdowell](https://github.com/sdowell))
- Fixed an issue where Windows kube-proxy’s `ModifyLoadBalancer` API updates did not match the HNS state in version 15.4. Support for `ModifyLoadBalancer` policy began with Kubernetes 1.31+. ([#131506](https://github.com/kubernetes/kubernetes/pull/131506), [@princepereira](https://github.com/princepereira))
- Fixed an issue where `insufficientResources` was logged as a pointer during pod preemption, making logs more readable. ([#132183](https://github.com/kubernetes/kubernetes/pull/132183), [@chrisy-x](https://github.com/chrisy-x)) [SIG Node]
- Fixed an issue where the kubelet token cache returned stale tokens when service accounts were recreated with the same name. The cache is now UID-aware. Additionally, the new `TokenRequestServiceAccountUIDValidation` feature gate (Beta, enabled by default) ensures the `TokenRequest` UID matches the service account UID when set. ([#132803](https://github.com/kubernetes/kubernetes/pull/132803), [@aramase](https://github.com/aramase)) [SIG API Machinery, Auth, Node and Testing]
- Fixed bug that prevented the alpha feature `PodTopologyLabelAdmission` from working due to checking for the incorrect label key when copying topology labels. This bug delayed the graduation of the feature to beta by an additional release to allow time for meaningful feedback. ([#132462](https://github.com/kubernetes/kubernetes/pull/132462), [@munnerz](https://github.com/munnerz))
- Fixed incorrect behavior for AllocationMode: All in ResourceClaim when used in subrequests. ([#131660](https://github.com/kubernetes/kubernetes/pull/131660), [@mortent](https://github.com/mortent)) [SIG Node]
- Fixed misleading response codes in admission control metrics. ([#132165](https://github.com/kubernetes/kubernetes/pull/132165), [@gavinkflam](https://github.com/gavinkflam)) [SIG API Machinery, Architecture and Instrumentation]
- Fixed runtime cost estimation for `x-int-or-string` custom resource schemas with maximum lengths. ([#132837](https://github.com/kubernetes/kubernetes/pull/132837), [@JoelSpeed](https://github.com/JoelSpeed))
- Fixed the `allocatedResourceStatuses` field name mismatch in PVC status validation. ([#131213](https://github.com/kubernetes/kubernetes/pull/131213), [@carlory](https://github.com/carlory))
- Fixed the `observedGeneration` field in pod resize conditions to accurately reflect the associated pod generation when both `InPlacePodVerticalScaling` and `PodObservedGenerationTracking` feature gates are enabled. ([#131157](https://github.com/kubernetes/kubernetes/pull/131157), [@natasha41575](https://github.com/natasha41575))
- Fixed the bug when swap related metrics were not available in `/metrics/resource` endpoint. ([#132065](https://github.com/kubernetes/kubernetes/pull/132065), [@yuanwang04](https://github.com/yuanwang04)) [SIG Node and Testing]
- Fixed the problem of validation error when specifying resource requirements at the container level for a resource not supported at the pod level. It implicitly interpreted the pod-level value as 0. ([#132551](https://github.com/kubernetes/kubernetes/pull/132551), [@chao-liang](https://github.com/chao-liang)) [SIG Apps]
- Fixed validation for Job with `suspend=true`, and `completions=0` to set the Complete condition. ([#132614](https://github.com/kubernetes/kubernetes/pull/132614), [@mimowo](https://github.com/mimowo)) [SIG Apps and Testing]
- Kube-apiserver: Fixed OIDC discovery document publishing when external service account token signing was enabled. ([#131493](https://github.com/kubernetes/kubernetes/pull/131493), [@hoskeri](https://github.com/hoskeri)) [SIG API Machinery, Auth and Testing]
- Kubeadm: Fixed a bug where the default args for etcd were not correct when a local etcd image was used and the etcd version was less than 3.6.0. ([#133023](https://github.com/kubernetes/kubernetes/pull/133023), [@carlory](https://github.com/carlory))
- Kubelet: Fixed a bug that caused an unexpected `NodeResizeError` condition to appear in the PVC status when the CSI driver did not support node volume expansion and the PVC had the `ReadWriteMany` access mode. ([#131495](https://github.com/kubernetes/kubernetes/pull/131495), [@carlory](https://github.com/carlory))
- Resolved a bug where DaemonSet updates unnecessarily triggered duplicate validation due to overlapping calls to `ValidateDaemonSet` and ValidateDaemonSetUpdate. This redundancy has been removed to prevent repeated validation runs. ([#132548](https://github.com/kubernetes/kubernetes/pull/132548), [@gavinkflam](https://github.com/gavinkflam))
- Fixed some missing white spaces in the flag descriptions and logs. ([#131562](https://github.com/kubernetes/kubernetes/pull/131562), [@logica0419](https://github.com/logica0419)) [SIG Network]
- Kubeadm: fixed missing space when printing the warning about pause image mismatch. ([#131563](https://github.com/kubernetes/kubernetes/pull/131563), [@logica0419](https://github.com/logica0419)) [SIG Cluster Lifecycle]

### 1.34.1

- Fixed SELinux warning controller not emitting events on some SELinux label conflicts. ([#133745](https://github.com/kubernetes/kubernetes/pull/133745), [@jsafrane](https://github.com/jsafrane)) [SIG Apps, Storage and Testing]
- Fixed broken shell completion for api resources. ([#133783](https://github.com/kubernetes/kubernetes/pull/133783), [@vpnachev](https://github.com/vpnachev)) [SIG CLI]
- Kube-apiserver: Fixed a 1.34 regression in CustomResourceDefinition handling that incorrectly warned about unrecognized formats on number and integer properties ([#133901](https://github.com/kubernetes/kubernetes/pull/133901), [@yongruilin](https://github.com/yongruilin)) [SIG API Machinery]
- Kube-apiserver: Fixes a 1.34 regression with spurious "Error getting keys" log messages ([#133866](https://github.com/kubernetes/kubernetes/pull/133866), [@serathius](https://github.com/serathius)) [SIG API Machinery and Etcd]
- Kube-apiserver: Fixes a possible 1.34 performance regression calculating object size statistics for resources not served from the watch cache, typically only Events ([#133879](https://github.com/kubernetes/kubernetes/pull/133879), [@serathius](https://github.com/serathius)) [SIG API Machinery and Etcd]
- Kubeadm: fixed bug where v1beta3's ClusterConfiguration.APIServer.TimeoutForControlPlane is not respected in newer versions of kubeadm where v1beta4 is the default. ([#133753](https://github.com/kubernetes/kubernetes/pull/133753), [@HirazawaUi](https://github.com/HirazawaUi)) [SIG Cluster Lifecycle]

### 1.34.2

- Fix Windows kube-proxy (winkernel) issue where stale RemoteEndpoints remained when a Deployment was referenced by multiple Services due to premature clearing of the terminatedEndpoints map. ([#135170](https://github.com/kubernetes/kubernetes/pull/135170), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]
- Fix Windows kube-proxy to prevent intermittent deletion of ClusterIP load balancers in HNS when internalTrafficPolicy=Local, ensuring stable service connectivity. ([#134031](https://github.com/kubernetes/kubernetes/pull/134031), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]
- Fix missing kubelet_volume_stats_* metrics ([#133905](https://github.com/kubernetes/kubernetes/pull/133905), [@huww98](https://github.com/huww98)) [SIG Instrumentation and Node]
- Fix panic on kubectl api-resources ([#134912](https://github.com/kubernetes/kubernetes/pull/134912), [@rikatz](https://github.com/rikatz)) [SIG CLI]
- Fix the bug which could result in Job status updates failing with the error: status.startTime: Required value: startTime cannot be removed for unsuspended job The error could be raised after a Job is resumed, if started and suspended previously. ([#135130](https://github.com/kubernetes/kubernetes/pull/135130), [@dejanzele](https://github.com/dejanzele)) [SIG Apps and Testing]
- Fix: The requests for a config FromClass in the status of a ResourceClaim were not referenced. ([#135098](https://github.com/kubernetes/kubernetes/pull/135098), [@LionelJouin](https://github.com/LionelJouin)) [SIG Node]
- Fixed a bug in kube-proxy nftables mode (GA as of 1.33) that fails to determine if traffic originates from a local source on the node. The issue was caused by using the wrong meta `iif` instead of `iifname` for name based matches. ([#134118](https://github.com/kubernetes/kubernetes/pull/134118), [@jack4it](https://github.com/jack4it)) [SIG Network]
- Fixed a bug in kube-scheduler where pending pod preemption caused preemptor pods to be retried more frequently. ([#134247](https://github.com/kubernetes/kubernetes/pull/134247), [@macsko](https://github.com/macsko)) [SIG Scheduling and Testing]
- Fixed a startup probe race condition that caused main containers to remain stuck in "Initializing" state when sidecar containers with startup probes failed initially but succeeded on restart in pods with restartPolicy=Never. ([#134800](https://github.com/kubernetes/kubernetes/pull/134800), [@yuanwang04](https://github.com/yuanwang04)) [SIG Node and Testing]
- Kube-controller-manager: Fixes a 1.34 regression, which triggered a spurious rollout of existing statefulsets when upgrading the control plane from 1.33 → 1.34. This fix is guarded by a `StatefulSetSemanticRevisionComparison` feature gate, which is enabled by default. ([#135087](https://github.com/kubernetes/kubernetes/pull/135087), [@liggitt](https://github.com/liggitt)) [SIG Apps]
- Kubeadm: fixed a bug where the node registration information for a given node was not fetched correctly during "kubeadm upgrade node" and the node name can end up being incorrect in cases where the node name is not the same as the host name. ([#134362](https://github.com/kubernetes/kubernetes/pull/134362), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]
- Kubeadm: fixes a preflight check that can fail hostname construction in IPV6 setups ([#134589](https://github.com/kubernetes/kubernetes/pull/134589), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Auth, Cloud Provider, Cluster Lifecycle and Testing]

### 1.34.3

- Fixes a spurious "namespace not found" error possible in default configurations in 1.30+ when using ValidatingAdmissionPolicy or MutatingAdmissionPolicy to intercept namespaced objects in newly-created namespaces ([#135442](https://github.com/kubernetes/kubernetes/pull/135442), [@lalitc375](https://github.com/lalitc375)) [SIG API Machinery]
- K8s.io/client-go: Fixes a regression in 1.34+ which prevented informers from using configured Transformer functions ([#135592](https://github.com/kubernetes/kubernetes/pull/135592), [@serathius](https://github.com/serathius)) [SIG API Machinery]
- Kube-apiserver: Fixes spurious warning log messages about enabled alpha APIs while starting API server ([#135343](https://github.com/kubernetes/kubernetes/pull/135343), [@michaelasp](https://github.com/michaelasp)) [SIG API Machinery]
- Make / build: fix docker IP address detection ([#135576](https://github.com/kubernetes/kubernetes/pull/135576), [@BenTheElder](https://github.com/BenTheElder)) [SIG Release and Testing]

### 1.34.4

- Fixed SELinux warning controller not to emit events for completed pods. ([#136099](https://github.com/kubernetes/kubernetes/pull/136099), [@jsafrane](https://github.com/jsafrane)) [SIG Apps, Storage and Testing]
- Fixed an issue in the Windows kube-proxy (winkernel) where IPv4 and IPv6 Service load balancers could be incorrectly shared, causing broken dual-stack Service behavior. The kube-proxy now tracks load balancers per IP family, enabling correct support for PreferDualStack and RequireDualStack Services on Windows nodes. ([#136374](https://github.com/kubernetes/kubernetes/pull/136374), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]
- Fixed kubelet logging to properly respect verbosity levels. Previously, some debug/info messages using V().Error() would always be printed regardless of the configured log verbosity. ([#136433](https://github.com/kubernetes/kubernetes/pull/136433), [@thc1006](https://github.com/thc1006)) [SIG Node]
- Fixes a 1.29 regression in the apiserver_watch_events_sizes metric to report total outgoing watch traffic again ([#135816](https://github.com/kubernetes/kubernetes/pull/135816), [@mborsz](https://github.com/mborsz)) [SIG API Machinery]
- Fixes a 1.34 regression starting pods with environment variables with a value containing `$` followed by a multi-byte character ([#136490](https://github.com/kubernetes/kubernetes/pull/136490), [@AutuSnow](https://github.com/AutuSnow)) [SIG Architecture and Node]
- Fixes a 1.34+ regression in ipvs and winkernel kube-proxy backends; these are now reverted back to their pre-1.34 behavior of regularly rechecking all of their rules even when no Services or EndpointSlices change. ([#136123](https://github.com/kubernetes/kubernetes/pull/136123), [@danwinship](https://github.com/danwinship)) [SIG Network and Windows]
- Kube-apiserver: fix a possible panic validating a custom resource whose CustomResourceDefinition indicates a status subresource exists, but which does not define a `status` property in the `openAPIV3Schema` ([#135363](https://github.com/kubernetes/kubernetes/pull/135363), [@fusida](https://github.com/fusida)) [SIG API Machinery]

### 1.34.7

- Fixes a 1.34+ regression reporting apiserver request latency annotation in the audit log when request took more than 500ms ([#136282](https://github.com/kubernetes/kubernetes/pull/136282), [@chaochn47](https://github.com/chaochn47)) [SIG API Machinery]
- Fixes kube-proxy's nftables mode to work on systems with nft 1.1.3. ([#137808](https://github.com/kubernetes/kubernetes/pull/137808), [@danwinship](https://github.com/danwinship)) [SIG Network]
- Fixed device plugin test failures after kubelet restart. ([#138027](https://github.com/kubernetes/kubernetes/pull/138027), [@zxqlxy](https://github.com/zxqlxy)) [SIG Node and Testing]

### 1.34.8

- Fixed a bug where 64 bit IPv6 ServiceCIDRs allocated addresses outside the subnet range. ([#138385](https://github.com/kubernetes/kubernetes/pull/138385), [@hoskeri](https://github.com/hoskeri)) [SIG Network]
- Fixed a scheduler bug where replacing a Pod with the same name during a failed scheduling attempt could leave stale in-flight queue state and unbounded growth of in-flight event tracking. The scheduler now clears in-flight state using the UID from the scheduling attempt, not only the UID on the refreshed Pod object. ([#138435](https://github.com/kubernetes/kubernetes/pull/138435), [@Argh4k](https://github.com/Argh4k)) [SIG Scheduling]
- Fixed stale remote HNS endpoint cleanup on Windows when a pod IP is reused across nodes in L2Bridge networks, preventing DNS timeouts caused by traffic being routed to the wrong node. ([#138601](https://github.com/kubernetes/kubernetes/pull/138601), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]

### 1.34.9

- Fixed a panic in the endpoint controller when processing services with empty IPFamilies field (pre-dual-stack services that were never spec-updated). ([#139235](https://github.com/kubernetes/kubernetes/pull/139235), [@rahulbabu95](https://github.com/rahulbabu95)) [SIG Apps and Network]
- Fixed an issue where kubelet would delete the CSI mount directory when a periodic NodePublishVolume call (triggered by CSIDriver.spec.requiresRepublish=true) returned an error, leaving the pod with stale volume contents that subsequent successful republishes could not repair. ([#139230](https://github.com/kubernetes/kubernetes/pull/139230), [@aramase](https://github.com/aramase)) [SIG Storage]
- Fixes a 1.34+ regression handling containers with environment values set from Secret API objects containing binary non-utf8 data. ([#139194](https://github.com/kubernetes/kubernetes/pull/139194), [@liggitt](https://github.com/liggitt)) [SIG Node]
- Kubeadm: fixed kubeadm init phase certs --dry-run to correctly copy existing CA files. ([#139448](https://github.com/kubernetes/kubernetes/pull/139448), [@HirazawaUi](https://github.com/HirazawaUi)) [SIG Cluster Lifecycle]

### 1.34.10

- Kubeadm: fix MemberPromote to skip the etcd promote API call when the member is already a voting member, avoiding unnecessary retries and timeout. ([#138491](https://github.com/kubernetes/kubernetes/pull/138491), [@wgkingk](https://github.com/wgkingk)) [SIG Cluster Lifecycle]


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.34.10**, the newest release recorded here for this line.

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
