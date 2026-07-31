---
id: TROUBLE-KUBERNETES_1_33_DEFECTS
type: troubleshooting
title: "kubernetes 1.33: defects fixed in the 1.33 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.33.0 <1.34.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubernetes 1.33 known issues
  - kubernetes 1.33 fixed in
  - is this kubernetes bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubernetes
sources:
  - type: docs
    path: kubernetes/kubernetes release notes for the 1.33 line — bug-fix entries
    url: https://github.com/kubernetes/kubernetes/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubernetes 1.33: defects fixed in the 1.33 line

## Summary

**72 defects** the project fixed across **12 releases** of the 1.33 line, from 1.33.0 to
1.33.13. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.33.0

- Added the ability to reduce both the initial delay and the maximum delay accrued between container restarts for a node for containers in `CrashLoopBackOff` across the cluster to the recommended values of `1s` initial delay and `60s` maximum delay. To set this for a node, turn on the feature gate `ReduceDefaultCrashLoopBackOffDecay`. If you are also using the feature gate `KubeletCrashLoopBackOffMax` with a configured per-node `CrashLoopBackOff.MaxContainerRestartPeriod`, the effective kubelet configuration will follow the conflict resolution policy described further in the documentation [here](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#reduced-container-restart-delay). ([#130711](https://github.com/kubernetes/kubernetes/pull/130711), [@lauralorenz](https://github.com/lauralorenz)) [SIG Node and Testing] [
- ] CSI drivers that call IsLikelyNotMountPoint should not assume false means that the path is a mount point. Each CSI driver needs to make sure correct usage of return value of IsLikelyNotMountPoint because if the file is an irregular file but not a mount point is acceptable ([#129370](https://github.com/kubernetes/kubernetes/pull/129370), [@andyzhangx](https://github.com/andyzhangx)) [SIG Storage and Windows] Fixed the behavior of the `KUBE_PROXY_NFTABLES_SKIP_KERNEL_VERSION_CHECK` environment variable in the nftables proxier. The kernel version check is now skipped only when this variable is explicitly set to a non-empty value. To skip the check, set the `KUBE_PROXY_NFTABLES_SKIP_KERNEL_VERSION_CHECK` environment variable. ([#130401](https://github.com/kubernetes/kubernetes/pull/130401), [@ryota-sakamoto](https://github.com/ryota-sakamoto)) Renamed `UpdatePodTolerations` action type to `UpdatePodToleration`
- for custom plugin developers to update their code to follow the rename. ([#129023](https://github.com/kubernetes/kubernetes/pull/129023), [@zhifei92](https://github.com/zhifei92)) [SIG Scheduling and Testing]
- Fixed `SELinuxWarningController` defaults when running kube-controller-manager in a container. ([#130037](https://github.com/kubernetes/kubernetes/pull/130037), [@jsafrane](https://github.com/jsafrane)) [SIG Apps and Storage]
- Fixed a bug to ensure container-level swap metrics are collected. ([#129486](https://github.com/kubernetes/kubernetes/pull/129486), [@iholder101](https://github.com/iholder101)) [SIG Node and Testing]
- Fix: Adopted go1.23 behavior change in mount point parsing on Windows. ([#129368](https://github.com/kubernetes/kubernetes/pull/129368), [@andyzhangx](https://github.com/andyzhangx)) [SIG Storage and Windows]
- Fixed `kubectl wait --for=create` behavior with label selectors, to properly wait for resources with matching labels to appear. ([#128662](https://github.com/kubernetes/kubernetes/pull/128662), [@omerap12](https://github.com/omerap12)) [SIG CLI and Testing]
- Fixed a bug in HorizontalPodAutoscaler. HPAs with `ContainerResource` metrics no longer return an error when container metrics are missing. Instead they use the same logic as `Resource` metrics to perform calculations. ([#127193](https://github.com/kubernetes/kubernetes/pull/127193), [@DP19](https://github.com/DP19)) [SIG Apps and Autoscaling]
- Fixed a bug in the exclusive assignment availability check for the `InPlacePodVerticalScalingExclusiveCPUs` feature gate. ([#130559](https://github.com/kubernetes/kubernetes/pull/130559), [@esotsal](https://github.com/esotsal))
- Fixed a bug where adding an ephemeral container to a pod which references a new secret or config map doesn't give the pod access to that new secret or config map. (#114984, @cslink) ([#129670](https://github.com/kubernetes/kubernetes/pull/129670), [@cslink](https://github.com/cslink)) [SIG Auth]
- Fixed a bug where kube-apiserver could emit a subsequent watch event even if the previous event failed to decrypt and was not emitted. ([#131020](https://github.com/kubernetes/kubernetes/pull/131020), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery and Etcd]
- Fixed a bug where the kube-proxy `EndpointSliceCache` memory experienced a leak. ([#128929](https://github.com/kubernetes/kubernetes/pull/128929), [@orange30](https://github.com/orange30))
- Fixed a data race that could occur when a single Go type was serialized to CBOR concurrently for the first time within a program. ([#129170](https://github.com/kubernetes/kubernetes/pull/129170), [@benluddy](https://github.com/benluddy)) [SIG API Machinery]
- Fixed a panic in kube-controller-manager handling StatefulSet objects when `revisionHistoryLimit` is negative. ([#129301](https://github.com/kubernetes/kubernetes/pull/129301), [@ardaguclu](https://github.com/ardaguclu))
- Fixed a regression in 1.32 that prevented pods with `postStart` hooks from starting. ([#129946](https://github.com/kubernetes/kubernetes/pull/129946), [@alex-petrov-vt](https://github.com/alex-petrov-vt))
- Fixed a regression in 1.32 where nodes could fail to report status and renew serving certificates after the kubelet restarted. ([#130348](https://github.com/kubernetes/kubernetes/pull/130348), [@aojea](https://github.com/aojea))
- Fixed a regression with the `ServiceAccountNodeAudienceRestriction` feature where `azureFile` volumes encountered 'failed to get service account token attributes' errors. ([#129993](https://github.com/kubernetes/kubernetes/pull/129993), [@aramase](https://github.com/aramase)) [SIG Auth and Testing]
- Fixed a storage bug related to multipath. iSCSI and Fibre Channel devices attached to nodes via multipath now resolve correctly when partitioned. ([#128086](https://github.com/kubernetes/kubernetes/pull/128086), [@RomanBednar](https://github.com/RomanBednar))
- Fixed a test failure in `TestSetVolumeOwnershipOwner` for `fsGroup=3000` and symlink cases in `volume_linux_test.go`. The tests were failing due to invalid ownership verification and the issue has been resolved by adjusting file permission change handling, ensuring correct behavior when run as root. ([#130616](https://github.com/kubernetes/kubernetes/pull/130616), [@gnufied](https://github.com/gnufied))
- Fixed an issue in register-gen where imports for k8s.io/apimachinery/pkg/runtime and k8s.io/apimachinery/pkg/runtime/schema were missing. ([#129307](https://github.com/kubernetes/kubernetes/pull/129307), [@LionelJouin](https://github.com/LionelJouin)) [SIG API Machinery]
- Fixed an issue in the CEL CIDR library where subnets contained within another CIDR were incorrectly rejected as not being contained. ([#130450](https://github.com/kubernetes/kubernetes/pull/130450), [@JoelSpeed](https://github.com/JoelSpeed))
- Fixed an issue where kubelet would unmount volumes of running pods upon restart if the referenced PVC was being deleted by the user. ([#130335](https://github.com/kubernetes/kubernetes/pull/130335), [@carlory](https://github.com/carlory)) [SIG Node, Storage and Testing]
- Fixed an issue where pods did not correctly have a pending phase after the node reboot. ([#128516](https://github.com/kubernetes/kubernetes/pull/128516), [@gjkim42](https://github.com/gjkim42)) [SIG Node and Testing]
- Fixed an issue with Kubernetes-style sidecar containers (in other words: init containers
- Fixed compressed kubelet log file permissions to use uncompressed kubelet log file permissions. ([#129893](https://github.com/kubernetes/kubernetes/pull/129893), [@simonfogliato](https://github.com/simonfogliato)) [SIG Node]
- Fixed in-tree to CSI migration for Portworx volumes, in clusters where Portworx security feature is enabled (it's a Portworx feature, not Kubernetes feature). It required secret data from the secret mentioned in-tree SC, to be passed in CSI requests which was not happening before this fix. ([#129630](https://github.com/kubernetes/kubernetes/pull/129630), [@gohilankit](https://github.com/gohilankit)) [SIG Storage]
- Fixed a rare and sporadic network issues that occurred when the host was under heavy load. ([#130256](https://github.com/kubernetes/kubernetes/pull/130256), [@adrianmoisey](https://github.com/adrianmoisey))
- Fixed the bug where Events failed to be created when the referenced object name was not a valid Event name. Now, a UUID is used as the name instead of the referenced object name and the timestamp suffix. ([#129790](https://github.com/kubernetes/kubernetes/pull/129790), [@aojea](https://github.com/aojea))
- Fixed a 1.32 regression kube-proxy, when using a Service with External or LoadBalancer IPs on UDP services , was consuming a large amount of CPU because it was not filtering by the Service destination port and trying to delete all the UDP entries associated to the service. ([#130484](https://github.com/kubernetes/kubernetes/pull/130484), [@aojea](https://github.com/aojea)) [SIG Network]
- kube-apiserver: Fixed a bug where the `ResourceQuota` admission plugin did not respect any scope changes when a resource was updated, such as setting or unsetting the `terminationGracePeriodSeconds` field of an existing pod. ([#130060](https://github.com/kubernetes/kubernetes/pull/130060), [@carlory](https://github.com/carlory)) [SIG API Machinery, Scheduling and Testing]
- kube-proxy: Fixed a potential memory leak that could occur in clusters with a high volume of UDP workflows. ([#130032](https://github.com/kubernetes/kubernetes/pull/130032), [@aroradaman](https://github.com/aroradaman))
- kubeadm: fixed a bug where an image is not pulled if there is an error with the sandbox image from CRI. ([#129594](https://github.com/kubernetes/kubernetes/pull/129594), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]
- kubeadm: fixed a bug where the `node.skipPhases` in UpgradeConfiguration is not respected by the `kubeadm upgrade node` subcommand. ([#129452](https://github.com/kubernetes/kubernetes/pull/129452), [@SataQiu](https://github.com/SataQiu))
- kubeadm: fixed panic when no UpgradeConfiguration was found in the config file. ([#130202](https://github.com/kubernetes/kubernetes/pull/130202), [@SataQiu](https://github.com/SataQiu))
- kubeadm: fixed the bug where the `v1beta4` `Timeouts.EtcdAPICall` field was not respected in etcd client operations, and the default timeout of 2 minutes was always used. ([#129859](https://github.com/kubernetes/kubernetes/pull/129859), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]
- Resolved a performance regression in default 1.31+ configurations, related to the `ConsistentListFromCache` feature, where rapid create/update API requests across different namespaces encounter increased latency. ([#130113](https://github.com/kubernetes/kubernetes/pull/130113), [@AwesomePatrol](https://github.com/AwesomePatrol))
- When `cpu-manager-policy=static` is configured, containers meeting the qualifications for static cpu assignment (i.e. Containers with integer CPU `requests` in pods with `Guaranteed` QOS) will not have cfs quota enforced. Because this fix changes a long-established behavior, users observing a regressions can use the `DisableCPUQuotaWithExclusiveCPUs` feature gate (enabled by default) to restore the previous behavior. Please file an issue if you encounter problems and have to use the Feature Gate. ([#127525](https://github.com/kubernetes/kubernetes/pull/127525), [@scott-grimes](https://github.com/scott-grimes)) [SIG Node and Testing]
- kube-apiserver: Fixes an issue updating the default ServiceCIDR API object and creating dual-stack Service API objects when `--service-cluster-ip-range` flag passed to kube-apiserver is changed from single-stack to dual-stack. ([#131263](https://github.com/kubernetes/kubernetes/pull/131263), [@aojea](https://github.com/aojea)) [SIG API Machinery, Network and Testing]
- Fixed a linting issue in `TestNodeDeletionReleaseCIDR`. ([#128856](https://github.com/kubernetes/kubernetes/pull/128856), [@adrianmoisey](https://github.com/adrianmoisey)) [SIG Apps and Network]

### 1.33.1

- Fixed a panic issue related to kubectl revision history kubernetes/kubectl#1724 ([#131496](https://github.com/kubernetes/kubernetes/pull/131496), [@tahacodes](https://github.com/tahacodes)) [SIG CLI]
- Kubelet: fix a bug where the unexpected NodeResizeError condition was in PVC status when the csi driver does not support node volume expansion and the pvc has the ReadWriteMany access mode. ([#131523](https://github.com/kubernetes/kubernetes/pull/131523), [@carlory](https://github.com/carlory)) [SIG Storage]
- Resolve a regression introduced in version 1.31 on Windows Proxy, where the creation of HNS endpoints fails if remote HNS endpoints with the same IP address have already been created. ([#131427](https://github.com/kubernetes/kubernetes/pull/131427), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]

### 1.33.2

- Fixes an issue where Windows kube-proxy's ModifyLoadBalancer API updates did not match HNS state in version 15.4. ModifyLoadBalancer policy is supported from Kubernetes 1.31+. ([#131649](https://github.com/kubernetes/kubernetes/pull/131649), [@princepereira](https://github.com/princepereira)) [SIG Windows]

### 1.33.3

- Fix a bug causing unexpected delay of creating pods for newly created jobs ([#132158](https://github.com/kubernetes/kubernetes/pull/132158), [@linxiulei](https://github.com/linxiulei)) [SIG Apps and Testing]
- Fix regression introduced in 1.33 - where some Paginated LIST calls are falling back to etcd instead of serving from cache. ([#132337](https://github.com/kubernetes/kubernetes/pull/132337), [@hakuna-matatah](https://github.com/hakuna-matatah)) [SIG API Machinery]
- Fix validation for Job with suspend=true, and completions=0 to set the Complete condition. ([#132728](https://github.com/kubernetes/kubernetes/pull/132728), [@mimowo](https://github.com/mimowo)) [SIG Apps and Testing]
- Kubeadm: fixed issue where etcd member promotion fails with an error saying the member was already promoted ([#132280](https://github.com/kubernetes/kubernetes/pull/132280), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]

### 1.33.4

- Fixes a 1.33 regression that can cause a nil panic in kube-scheduler when aggregating resource requests across container's spec and status. ([#133285](https://github.com/kubernetes/kubernetes/pull/133285), [@yue9944882](https://github.com/yue9944882)) [SIG Node and Scheduling]

### 1.33.5

- Fixed SELinux warning controller not emitting events on some SELinux label conflicts. ([#133746](https://github.com/kubernetes/kubernetes/pull/133746), [@jsafrane](https://github.com/jsafrane)) [SIG Apps, Storage and Testing]
- Kubeadm: fixed bug where v1beta3's ClusterConfiguration.APIServer.TimeoutForControlPlane is not respected in newer versions of kubeadm where v1beta4 is the default. ([#133754](https://github.com/kubernetes/kubernetes/pull/133754), [@HirazawaUi](https://github.com/HirazawaUi)) [SIG Cluster Lifecycle]

### 1.33.6

- Fix Windows kube-proxy (winkernel) issue where stale RemoteEndpoints remained when a Deployment was referenced by multiple Services due to premature clearing of the terminatedEndpoints map. ([#135171](https://github.com/kubernetes/kubernetes/pull/135171), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]
- Fix Windows kube-proxy to prevent intermittent deletion of ClusterIP load balancers in HNS when internalTrafficPolicy=Local, ensuring stable service connectivity. ([#134032](https://github.com/kubernetes/kubernetes/pull/134032), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]
- Fix the bug which could result in Job status updates failing with the error: status.startTime: Required value: startTime cannot be removed for unsuspended job The error could be raised after a Job is resumed, if started and suspended previously. ([#135129](https://github.com/kubernetes/kubernetes/pull/135129), [@dejanzele](https://github.com/dejanzele)) [SIG Apps and Testing]
- Fix: The requests for a config FromClass in the status of a ResourceClaim were not referenced. ([#135105](https://github.com/kubernetes/kubernetes/pull/135105), [@LionelJouin](https://github.com/LionelJouin)) [SIG Node]
- Fixed a bug in kube-proxy nftables mode (GA as of 1.33) that fails to determine if traffic originates from a local source on the node. The issue was caused by using the wrong meta `iif` instead of `iifname` for name based matches. ([#134099](https://github.com/kubernetes/kubernetes/pull/134099), [@aroradaman](https://github.com/aroradaman)) [SIG Network]
- Fixed a startup probe race condition that caused main containers to remain stuck in "Initializing" state when sidecar containers with startup probes failed initially but succeeded on restart in pods with restartPolicy=Never. ([#134801](https://github.com/kubernetes/kubernetes/pull/134801), [@yuanwang04](https://github.com/yuanwang04)) [SIG Node and Testing]
- Fixed race-condition in service allocation logic which leads to spurious IPAddressWrongReference warnings impacting performance ([#133954](https://github.com/kubernetes/kubernetes/pull/133954), [@aroradaman](https://github.com/aroradaman)) [SIG Network]
- Fixes spammy incorrect "Ignoring same-zone topology hints for service since no hints were provided for zone" messages in the kube-proxy logs. ([#133527](https://github.com/kubernetes/kubernetes/pull/133527), [@danwinship](https://github.com/danwinship)) [SIG Network]
- Kube-controller-manager: Fixes a 1.33 regression in daemonset handling of orphaned pods ([#134652](https://github.com/kubernetes/kubernetes/pull/134652), [@liggitt](https://github.com/liggitt)) [SIG Apps]
- Kubeadm: fixed a bug where the node registration information for a given node was not fetched correctly during "kubeadm upgrade node" and the node name can end up being incorrect in cases where the node name is not the same as the host name. ([#134363](https://github.com/kubernetes/kubernetes/pull/134363), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]
- Kubeadm: fixes a preflight check that can fail hostname construction in IPV6 setups ([#134590](https://github.com/kubernetes/kubernetes/pull/134590), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Auth, Cloud Provider, Cluster Lifecycle and Testing]

### 1.33.7

- Fixed a data race in the ResolverTypeProvider that caused indeterministic behavior in ValidatingAdmissionPolicy (VAP) and MutatingAdmissionPolicy (MAP). ([#135328](https://github.com/kubernetes/kubernetes/pull/135328), [@lalitc375](https://github.com/lalitc375)) [SIG API Machinery]
- Fixes a spurious "namespace not found" error possible in default configurations in 1.30+ when using ValidatingAdmissionPolicy or MutatingAdmissionPolicy to intercept namespaced objects in newly-created namespaces ([#135443](https://github.com/kubernetes/kubernetes/pull/135443), [@lalitc375](https://github.com/lalitc375)) [SIG API Machinery]
- Kube-apiserver: fix a possible panic validating a custom resource whose CustomResourceDefinition indicates a status subresource exists, but which does not define a `status` property in the `openAPIV3Schema` ([#135362](https://github.com/kubernetes/kubernetes/pull/135362), [@fusida](https://github.com/fusida)) [SIG API Machinery]
- Make / build: fix docker IP address detection ([#135577](https://github.com/kubernetes/kubernetes/pull/135577), [@BenTheElder](https://github.com/BenTheElder)) [SIG Release and Testing]

### 1.33.8

- Fixed SELinux warning controller not to emit events for completed pods. ([#136172](https://github.com/kubernetes/kubernetes/pull/136172), [@jsafrane](https://github.com/jsafrane)) [SIG Apps, Storage and Testing]
- Fixed an issue in the Windows kube-proxy (winkernel) where IPv4 and IPv6 Service load balancers could be incorrectly shared, causing broken dual-stack Service behavior. The kube-proxy now tracks load balancers per IP family, enabling correct support for PreferDualStack and RequireDualStack Services on Windows nodes. ([#136375](https://github.com/kubernetes/kubernetes/pull/136375), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]
- Fixed kubelet logging to properly respect verbosity levels. Previously, some debug/info messages using V().Error() would always be printed regardless of the configured log verbosity. ([#136434](https://github.com/kubernetes/kubernetes/pull/136434), [@thc1006](https://github.com/thc1006)) [SIG Node]

### 1.33.10

- Fix bug in ValidatingAdmissionPolicy where a object schema with additionalProperties:true would crash the kube-controller-manager with a nil pointer exception. ([#136958](https://github.com/kubernetes/kubernetes/pull/136958), [@lalitc375](https://github.com/lalitc375)) [SIG API Machinery]

### 1.33.11

- Fix apiserver startup failure during upgrade when MultiCIDRServiceAllocator is enabled and the cluster has a large number of namespaces. The IP address repair controller now retries on Forbidden errors from admission plugins that are not yet ready. ([#137677](https://github.com/kubernetes/kubernetes/pull/137677), [@haojiwu](https://github.com/haojiwu)) [SIG Network]
- Fixes kube-proxy's nftables mode to work on systems with nft 1.1.3. ([#137809](https://github.com/kubernetes/kubernetes/pull/137809), [@danwinship](https://github.com/danwinship)) [SIG Network]

### 1.33.13

- Fixed a panic in the endpoint controller when processing services with empty IPFamilies field (pre-dual-stack services that were never spec-updated). ([#139236](https://github.com/kubernetes/kubernetes/pull/139236), [@rahulbabu95](https://github.com/rahulbabu95)) [SIG Apps and Network]


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.33.13**, the newest release recorded here for this line.

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
