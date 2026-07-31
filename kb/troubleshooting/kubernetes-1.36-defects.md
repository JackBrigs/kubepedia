---
id: TROUBLE-KUBERNETES_1_36_DEFECTS
type: troubleshooting
title: "kubernetes 1.36: defects fixed in the 1.36 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.36.0 <1.37.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubernetes 1.36 known issues
  - kubernetes 1.36 fixed in
  - is this kubernetes bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubernetes
sources:
  - type: docs
    path: kubernetes/kubernetes release notes for the 1.36 line — bug-fix entries
    url: https://github.com/kubernetes/kubernetes/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubernetes 1.36: defects fixed in the 1.36 line

## Summary

**105 defects** the project fixed across **4 releases** of the 1.36 line, from 1.36.0 to
1.36.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.36.0

- Fixed a bug where pod lifecycle hooks could run for their full duration when pods are terminated. ([#136598](https://github.com/kubernetes/kubernetes/pull/136598), [@dgrisonnet](https://github.com/dgrisonnet)) [SIG API Machinery, Auth, Cloud Provider, Node and Scheduling]
- Fixed `fake.NewClientset()` to work properly with correct schema. ([#131068](https://github.com/kubernetes/kubernetes/pull/131068), [@soltysh](https://github.com/soltysh)) [SIG API Machinery]
- Fixed a few log calls that did not properly format their parameters. ([#137108](https://github.com/kubernetes/kubernetes/pull/137108), [@pohly](https://github.com/pohly)) [SIG API Machinery, Apps, Auth, Cluster Lifecycle, Network, Node, Scheduling and Testing]
- Fixed a potential nil pointer dereference in the scheduler's `NodeResourcesFitArgs` validation when using `RequestedToCapacityRatio` scoring strategy. ([#132120](https://github.com/kubernetes/kubernetes/pull/132120), [@flpanbin](https://github.com/flpanbin)) [SIG Scheduling]
- Fixed an issue in `kube-apiserver`, allowing it to recover from an established connection to an incorrect server that never returns the expected response during APIService availability checks. ([#137157](https://github.com/kubernetes/kubernetes/pull/137157), [@bsalamat](https://github.com/bsalamat)) [SIG API Machinery]
- Fixed missing field conversions (`BindsToNode`, `BindingConditions`, `BindingFailureConditions`, `AllowMultipleAllocations`, `Capacity`) in DRA API `v1beta1` hand-written conversion code. ([#137240](https://github.com/kubernetes/kubernetes/pull/137240), [@yykkibbb](https://github.com/yykkibbb)) [SIG Node]
- Kubelet: Fixed device plugin test failures after kubelet restart. ([#135485](https://github.com/kubernetes/kubernetes/pull/135485), [@saschagrunert](https://github.com/saschagrunert)) [SIG Node and Testing]
- Client-go: Fixed an unlikely deadlock during informer startup. ([#136509](https://github.com/kubernetes/kubernetes/pull/136509), [@pohly](https://github.com/pohly)) [SIG API Machinery]
- CustomResourceDefinitions: Fixed server-side apply field ownership tracking so that metadata ownership is correctly tracked for writes to the `/status` subresource. Custom Resources: Fixed server-side apply field ownership to not update metadata from the `/status` subresource since these writes are wiped for custom resources. ([#137689](https://github.com/kubernetes/kubernetes/pull/137689), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery, Network and Testing]
- DRA BindingConditions: Fixed a panic in the scheduler when the `DRABindingConditions` feature was enabled and the same claim was reused among different Pods while deallocation happened in parallel. ([#137371](https://github.com/kubernetes/kubernetes/pull/137371), [@pohly](https://github.com/pohly)) [SIG Node, Scheduling and Testing]
- Fixed SELinux warning controller to not emit events for completed Pods (Succeeded and Failed states). ([#135629](https://github.com/kubernetes/kubernetes/pull/135629), [@jsafrane](https://github.com/jsafrane)) [SIG Apps, Storage and Testing]
- Fixed StatefulSets to always count `.status.availableReplicas` at the correct time without delay, resulting in faster StatefulSet rollout progress. ([#135428](https://github.com/kubernetes/kubernetes/pull/135428), [@atiratree](https://github.com/atiratree)) [SIG Apps]
- Fixed `DRA manager` not initializing sharedID from cache when `DRAConsumableCapacity` is enabled. ([#136734](https://github.com/kubernetes/kubernetes/pull/136734), [@sunya-ch](https://github.com/sunya-ch)) [SIG Node and Scheduling]
- Fixed `PodCertificateRequest` OwnerReference using incorrect apiVersion "core/v1" instead of "v1", which prevented garbage collection of `PodCertificateRequests` when their owning Pod was deleted. ([#137008](https://github.com/kubernetes/kubernetes/pull/137008), [@srhppr](https://github.com/srhppr)) [SIG Auth and Node]
- Fixed `ReadWriteOncePod` preemption e2e test to run as serial, preventing it from causing other random e2e tests to flake. ([#135623](https://github.com/kubernetes/kubernetes/pull/135623), [@jsafrane](https://github.com/jsafrane)) [SIG Storage and Testing]
- Fixed `container_swap_usage_bytes` in the `/metrics/resource` endpoint to correctly report container-level swap usage instead of always reporting 0. The root cause was missing logic in `addCadvisorContainerCPUAndMemoryStats` to propagate swap stats from cadvisor to the container stats object. ([#137098](https://github.com/kubernetes/kubernetes/pull/137098), [@yuanwang04](https://github.com/yuanwang04)) [SIG Apps, Node and Testing]
- Fixed `event_handling_duration_seconds`, `preemption_goroutines_duration_seconds`, `run_podsandbox_duration_seconds`, and `store_schedule_results_duration_seconds` metrics incorrectly recording near-zero latency values instead of actual durations, caused by premature evaluation of `SinceInSeconds(startTime)` in a deferred call. ([#135749](https://github.com/kubernetes/kubernetes/pull/135749), [@novahe](https://github.com/novahe)) [SIG Architecture, Instrumentation, Node and Scheduling]
- Fixed `kube-apiserver` startup failure during upgrade when `MultiCIDRServiceAllocator` is enabled and the cluster has a large number of namespaces. The IP address repair controller retries on Forbidden errors from admission plugins that are not yet ready. ([#137147](https://github.com/kubernetes/kubernetes/pull/137147), [@haojiwu](https://github.com/haojiwu)) [SIG Testing]
- Fixed `kube-proxy` log spam when all of a Service's endpoints were unready. ([#136743](https://github.com/kubernetes/kubernetes/pull/136743), [@ansilh](https://github.com/ansilh)) [SIG Network]
- Fixed `kubectl delete` to properly handle deletion of multiple StatefulSet pods and exit normally. ([#135563](https://github.com/kubernetes/kubernetes/pull/135563), [@yangjunmyfm192085](https://github.com/yangjunmyfm192085)) [SIG CLI, Network and Node]
- Fixed `kubectl describe node` to correctly display resource requests and limits for Pods using Pod-level resources. ([#137394](https://github.com/kubernetes/kubernetes/pull/137394), [@Nikateen](https://github.com/Nikateen)) [SIG CLI]
- Fixed `kubectl describe` to correctly recognize uppercase acronyms as a single element when displaying Custom Resource field names. ([#135683](https://github.com/kubernetes/kubernetes/pull/135683), [@uozalp](https://github.com/uozalp)) [SIG CLI]
- Fixed `kubectl label` output message to display `modified` when labels are both added and removed. ([#134849](https://github.com/kubernetes/kubernetes/pull/134849), [@tchap](https://github.com/tchap)) [SIG CLI]
- Fixed `kubectl logs -f` to wait for containers to start instead of failing immediately when pods are in ContainerCreating or PodInitializing states. ([#136411](https://github.com/kubernetes/kubernetes/pull/136411), [@olamilekan000](https://github.com/olamilekan000)) [SIG CLI]
- Fixed a `v1.29` regression in the `apiserver_watch_events_sizes` metric to report total outgoing watch traffic again. ([#135367](https://github.com/kubernetes/kubernetes/pull/135367), [@mborsz](https://github.com/mborsz)) [SIG API Machinery]
- Fixed a `v1.34` regression in `ipvs` and `winkernel` `kube-proxy` backends. These backends now revert to their `pre-v1.34` behavior of regularly rechecking all rules even when no Services or EndpointSlices change. ([#135631](https://github.com/kubernetes/kubernetes/pull/135631), [@danwinship](https://github.com/danwinship)) [SIG Network and Windows]
- Fixed a `v1.34` regression when starting pods with environment variables containing a value with `$` followed by a multi-byte character. ([#136325](https://github.com/kubernetes/kubernetes/pull/136325), [@AutuSnow](https://github.com/AutuSnow)) [SIG Architecture]
- Fixed a `v1.35` regression in StatefulSet parallel Pod management by disabling the `MaxUnavailableStatefulSet` feature by default. ([#137904](https://github.com/kubernetes/kubernetes/pull/137904), [@soltysh](https://github.com/soltysh)) [SIG Apps]
- Fixed a bug causing clients to error out when decoding large CBOR encoded lists. ([#135340](https://github.com/kubernetes/kubernetes/pull/135340), [@ricardomaraschini](https://github.com/ricardomaraschini)) [SIG API Machinery]
- Fixed a bug in `DeepEqualWithNilDifferentFromEmpty` where empty slices and maps were incorrectly considered equal to non-empty ones due to using OR (`||`) instead of AND (`&&`) logic. This could cause managed fields timestamps to not update when the only change was adding or removing all elements from a list or map. ([#135636](https://github.com/kubernetes/kubernetes/pull/135636), [@mikecook](https://github.com/mikecook)) [SIG API Machinery]
- Fixed a bug in the `dra_operations_duration_seconds` metric where the `is_error` label was recording inverted values. Error operations now correctly report `is_error=true`, and successful operations report `is_error=false`. ([#135227](https://github.com/kubernetes/kubernetes/pull/135227), [@hime](https://github.com/hime)) [SIG Node]
- Fixed a bug preventing Pods sharing ResourceClaims from being scheduled with GangScheduling. ([#137647](https://github.com/kubernetes/kubernetes/pull/137647), [@nojnhuh](https://github.com/nojnhuh)) [SIG Node, Scheduling and Testing]
- Fixed a bug that caused `EndpointSlice` churn for headless services with no ports defined. ([#136502](https://github.com/kubernetes/kubernetes/pull/136502), [@tzneal](https://github.com/tzneal)) [SIG Network]
- Fixed a bug where `kubectl apply --dry-run=client` would only output server state instead of merged manifest values when the resource already exists. ([#135513](https://github.com/kubernetes/kubernetes/pull/135513), [@grandeit](https://github.com/grandeit)) [SIG CLI]
- Fixed a bug where `kubectl plugin list` failed to detect overshadowed plugins on Windows. ([#136689](https://github.com/kubernetes/kubernetes/pull/136689), [@kfess](https://github.com/kfess)) [SIG CLI]
- Fixed a bug where the Gated pods metric was not updated when a Pod transitioned from Unschedulable to Gated during an update. ([#135368](https://github.com/kubernetes/kubernetes/pull/135368), [@vshkrabkov](https://github.com/vshkrabkov)) [SIG Scheduling]
- Fixed a bug where the `scheduler_unschedulable_pods` metric could be artificially inflated (leak) when a pod fails `PreEnqueue` plugins after being previously marked unschedulable. ([#135981](https://github.com/kubernetes/kubernetes/pull/135981), [@vshkrabkov](https://github.com/vshkrabkov)) [SIG Scheduling]
- Fixed a bug where users could not update HPAv2 resources that use object metrics with `averageValue` via the v1 HPA API. ([#137856](https://github.com/kubernetes/kubernetes/pull/137856), [@adrianmoisey](https://github.com/adrianmoisey)) [SIG Autoscaling]
- Fixed a bug where, after a `kubelet` restart, regular containers in a Pod with a sidecar (initContainer with `restartPolicy`: Always) and a `startupProbe` failed to restart after crashing. Affected Pods remained stuck with `RestartCount: 0` indefinitely. ([#137146](https://github.com/kubernetes/kubernetes/pull/137146), [@george-angel](https://github.com/george-angel)) [SIG Node and Testing]
- Fixed a data race in the `PopulateRefs` function in `k8s.io/apiserver/pkg/cel/openapi/resolver` where concurrent goroutines could simultaneously modify shared pointer fields from a shallow-copied schema struct. ([#136802](https://github.com/kubernetes/kubernetes/pull/136802), [@pohly](https://github.com/pohly)) [SIG API Machinery, Node and Testing]
- Fixed a kubelet device manager bug where topology hint computation enumerated O(2^n) NUMA node combinations using all machine NUMA nodes. On systems with many NUMA nodes that carry no devices (e.g. NVIDIA GB200 with 36 NUMA nodes), this caused kubelet to stall indefinitely during pod admission. The device manager now restricts iteration to NUMA nodes that actually host devices for the requested resource, reducing the search space to O(2^k) where k is typically 1–2. ([#138244](https://github.com/kubernetes/kubernetes/pull/138244), [@fanzhangio](https://github.com/fanzhangio)) [SIG Node]
- Fixed a loophole that allowed users to work around DRA extended resource quota set by system administrators. ([#135434](https://github.com/kubernetes/kubernetes/pull/135434), [@yliaog](https://github.com/yliaog)) [SIG API Machinery, Apps, Node, Scheduling and Testing]
- Fixed a race condition in CEL admission policy compilation that could cause `kube-apiserver` to crash with a `concurrent map read and map write` error under high load. ([#135759](https://github.com/kubernetes/kubernetes/pull/135759), [@Abhigyan-Shekhar](https://github.com/Abhigyan-Shekhar)) [SIG API Machinery and CLI]
- Fixed a race condition in Dynamic Resource Allocation (DRA) where the same device could be allocated twice for different `ResourceClaims` when scheduling many pods very rapidly. Depending on whether DRA drivers check for this during `NodePrepareResources` (they should, but not all may implement this properly), the second pod using the same device could fail to start until the first one is done or (worse) run in parallel. ([#136269](https://github.com/kubernetes/kubernetes/pull/136269), [@pohly](https://github.com/pohly)) [SIG Node, Scheduling and Testing]
- Fixed an issue in the Windows `kube-proxy` (winkernel) where IPv4 and IPv6 Service load balancers could be incorrectly shared, causing broken dual-stack Service behavior. The `kube-proxy` now tracks load balancers per IP family, enabling correct support for `PreferDualStack` and `RequireDualStack` Services on Windows nodes. ([#136241](https://github.com/kubernetes/kubernetes/pull/136241), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]
- Fixed an issue where zero-valued PSI (Pressure Stall Information) metrics were emitted by the `kubelet` when the OS does not support PSI, even if the `KubeletPSI` feature gate was enabled. ([#137326](https://github.com/kubernetes/kubernetes/pull/137326), [@amritansh1502](https://github.com/amritansh1502)) [SIG Node]
- Fixed container restart policy validation error message to correctly show available actions when the `RestartAllContainersOnContainerExits` feature gate is enabled. ([#137369](https://github.com/kubernetes/kubernetes/pull/137369), [@kfess](https://github.com/kfess)) [SIG Apps]
- Fixed erroneously reporting a pod-level resize in progress on Pod creation when the `InPlacePodLevelResourcesVerticalScaling` feature gate is enabled. ([#138049](https://github.com/kubernetes/kubernetes/pull/138049), [@ndixita](https://github.com/ndixita)) [SIG Node and Testing]
- Fixed feature gates `ChangeContainerStatusOnKubeletRestart` and `StatefulSetSemanticRevisionComparison` to be visible in `--help` output across different components. ([#135515](https://github.com/kubernetes/kubernetes/pull/135515), [@dims](https://github.com/dims)) [SIG Architecture]
- Fixed goroutine hot-loop in client-go `StartEventWatcher` when the event broadcaster shuts down before the cancellation context fires. ([#137398](https://github.com/kubernetes/kubernetes/pull/137398), [@Rajneesh180](https://github.com/Rajneesh180)) [SIG API Machinery]
- Fixed how image names are compared to the values from `preloadedImagesVerificationAllowlist` in the `kubelet`'s configuration. Previously, the use of "familiar" image names (e.g. "alpine") from a Pod did not properly match the same name in `preloadedImagesVerificationAllowlist` in the `kubelet`'s configuration. ([#137629](https://github.com/kubernetes/kubernetes/pull/137629), [@stlaz](https://github.com/stlaz)) [SIG Auth, Node and Testing]
- Fixed incorrect behavior when using AllocationModeAll with DRA PrioritizedList that prevented the allocator from successfully allocating a claim even when devices were available. ([#137347](https://github.com/kubernetes/kubernetes/pull/137347), [@mortent](https://github.com/mortent)) [SIG Node]
- Fixed informer-gen to generate SetTransform calls that correctly override per-informer transforms. ([#137473](https://github.com/kubernetes/kubernetes/pull/137473), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery and Scheduling]
- Fixed issues in server side apply and client-go's `Extract{TypeName}()` and `Extract{TypeName}From()` functions where empty arrays and maps were incorrectly treated as absent, and atomic elements from associative lists were incorrectly duplicated. ([#135391](https://github.com/kubernetes/kubernetes/pull/135391), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery, Architecture, Auth, CLI, Cloud Provider, Cluster Lifecycle, Network, Node, Scheduling and Storage]
- Fixed kubeadm to skip appending the client URL of etcd learner members to `c.Endpoints`, since learners do not serve client traffic. ([#137251](https://github.com/kubernetes/kubernetes/pull/137251), [@pacoxu](https://github.com/pacoxu)) [SIG Cluster Lifecycle]
- Fixed link file ownership of projected serviceAccountToken. ([#137332](https://github.com/kubernetes/kubernetes/pull/137332), [@gavinkflam](https://github.com/gavinkflam)) [SIG Storage]
- Fixed log verbosity for non-error messages in the SELinux warning controller so they are no longer logged at error level. ([#136050](https://github.com/kubernetes/kubernetes/pull/136050), [@ShaanveerS](https://github.com/ShaanveerS)) [SIG Apps and Storage]
- Fixed log verbosity for non-error messages in the storage version migrator so they are no longer logged at error level. ([#136046](https://github.com/kubernetes/kubernetes/pull/136046), [@Tanner-Gladson](https://github.com/Tanner-Gladson)) [SIG API Machinery and Apps]
- Fixed queue hint for certain plugins on change to pods with nominated nodes. ([#135392](https://github.com/kubernetes/kubernetes/pull/135392), [@brejman](https://github.com/brejman)) [SIG Scheduling]
- Fixed queue hint for inter-pod anti-affinity in case deleted pod's anti-affinity matched the pending pod, which might have caused delays in scheduling. ([#135325](https://github.com/kubernetes/kubernetes/pull/135325), [@brejman](https://github.com/brejman)) [SIG Scheduling and Testing]
- Fixed queue hint for the `interpodaffinity` plugin in case target pod labels change. ([#135394](https://github.com/kubernetes/kubernetes/pull/135394), [@brejman](https://github.com/brejman)) [SIG Scheduling]
- Fixed redundant SSH command executions in the `etcd` failure e2e test. ([#137001](https://github.com/kubernetes/kubernetes/pull/137001), [@kairosci](https://github.com/kairosci)) [SIG API Machinery and Testing]
- Fixed running of DRA e2e tests in air-gapped clusters or with test images in private registries. ([#138318](https://github.com/kubernetes/kubernetes/pull/138318), [@jsafrane](https://github.com/jsafrane)) [SIG Node and Testing]
- Fixed static pod status displaying `Init:0/1` when unable to retrieve init container status from container runtime. ([#131317](https://github.com/kubernetes/kubernetes/pull/131317), [@bitoku](https://github.com/bitoku)) [SIG Node and Testing]
- Fixed the `lastTerminationStatus` to match the `RestartAllContainers` action if the container was restarted this way. ([#136964](https://github.com/kubernetes/kubernetes/pull/136964), [@yuanwang04](https://github.com/yuanwang04)) [SIG Node]
- Fixed the total Pod resources computation. ([#137683](https://github.com/kubernetes/kubernetes/pull/137683), [@ndixita](https://github.com/ndixita)) [SIG CLI and Node]
- Fixed unsupported `Table` object detection to cover all List and Watch operations, preventing the reflector from incorrectly processing resources returned in `Table` format. ([#136937](https://github.com/kubernetes/kubernetes/pull/136937), [@p0lyn0mial](https://github.com/p0lyn0mial)) [SIG API Machinery and Testing]
- Fixed validation error messages for `restartPolicyRules` and `exitCodes.values` to report "items" instead of "bytes". ([#137136](https://github.com/kubernetes/kubernetes/pull/137136), [@kfess](https://github.com/kfess)) [SIG Apps]
- Kube-apiserver: Fixed request latency annotation `apiserver.latency.k8s.io/total` in the audit log when request took more than `500ms`. ([#135685](https://github.com/kubernetes/kubernetes/pull/135685), [@chaochn47](https://github.com/chaochn47)) [SIG API Machinery]
- Kube-apiserver: Fixed the log verbosity level in the unsafe delete authorization check that was incorrectly using Error level instead of Info level. ([#136229](https://github.com/kubernetes/kubernetes/pull/136229), [@thc1006](https://github.com/thc1006)) [SIG API Machinery]
- Kube-controller-manager: Fixed `VolumeAttachment` cleanup when CSI's `attachRequired` switches from true to false. ([#129664](https://github.com/kubernetes/kubernetes/pull/129664), [@hkttty2009](https://github.com/hkttty2009)) [SIG Storage and Testing]
- Kube-proxy: Fixed nftables mode to work on systems with `nft` `v1.1.3`. ([#137501](https://github.com/kubernetes/kubernetes/pull/137501), [@danwinship](https://github.com/danwinship)) [SIG Network]
- Kubeadm: Fixed a bug where `kubeadm upgrade` failed if the content of the `/var/lib/kubelet/kubeadm-flags.env` file was `KUBELET_KUBEADM_ARGS=""`. ([#136127](https://github.com/kubernetes/kubernetes/pull/136127), [@carlory](https://github.com/carlory)) [SIG Cluster Lifecycle]
- Kubectl: Fixed `kyaml` output of `kubectl get ... --output-watch-events -o kyaml`. ([#136110](https://github.com/kubernetes/kubernetes/pull/136110), [@liggitt](https://github.com/liggitt)) [SIG CLI]
- Kubectl: Fixed a panic in `kubectl exec` when the terminal size queue delegate is uninitialized. ([#135918](https://github.com/kubernetes/kubernetes/pull/135918), [@MarcosDaNight](https://github.com/MarcosDaNight)) [SIG CLI]
- Kubectl: Fixed a panic when processing pods with nil resource requests but populated container status resources. ([#136534](https://github.com/kubernetes/kubernetes/pull/136534), [@dmaizel](https://github.com/dmaizel)) [SIG CLI]
- Kubectl: Fixed an issue where `kubectl run -i/-it` would miss container output written before the attach connection was established. ([#136010](https://github.com/kubernetes/kubernetes/pull/136010), [@olamilekan000](https://github.com/olamilekan000)) [SIG CLI]
- Kubelet: Fixed Dynamic Resource Allocation (DRA) to correctly handle multiple `ResourceClaims` even if one is already prepared. ([#135919](https://github.com/kubernetes/kubernetes/pull/135919), [@rogowski-piotr](https://github.com/rogowski-piotr)) [SIG Node and Testing]
- Kubelet: Fixed a data race in pod allocated resources. ([#136226](https://github.com/kubernetes/kubernetes/pull/136226), [@HirazawaUi](https://github.com/HirazawaUi)) [SIG Node]
- Kubelet: Fixed a data race in the container manager. ([#136206](https://github.com/kubernetes/kubernetes/pull/136206), [@HirazawaUi](https://github.com/HirazawaUi)) [SIG Node]
- Kubelet: Fixed a data race in the status manager. ([#136205](https://github.com/kubernetes/kubernetes/pull/136205), [@HirazawaUi](https://github.com/HirazawaUi)) [SIG Node]
- Kubelet: Fixed a data race in the volume manager's `WaitForAllPodsUnmount` that could cause errors to be lost during concurrent pod unmount operations. ([#135794](https://github.com/kubernetes/kubernetes/pull/135794), [@AutuSnow](https://github.com/AutuSnow)) [SIG Node and Storage]
- Kubelet: Fixed a nil pointer dereference when handling pod updates of mirror pods with the `NodeDeclaredFeatures` feature gate enabled. ([#136037](https://github.com/kubernetes/kubernetes/pull/136037), [@pravk03](https://github.com/pravk03)) [SIG Node]
- Kubelet: Fixed logging to properly respect verbosity levels. Previously, some debug/info messages using `V().Error()` would always be printed regardless of the configured log verbosity. ([#136028](https://github.com/kubernetes/kubernetes/pull/136028), [@thc1006](https://github.com/thc1006)) [SIG Node]
- Kubelet: Fixed preservation of DRA `NodeAllocatableResourceClaimStatuses` in PodStatus. ([#138030](https://github.com/kubernetes/kubernetes/pull/138030), [@askervin](https://github.com/askervin)) [SIG Node]
- Kubelet: Fixed reloading of server certificate files when they are changed on disk and kubelet is dialed by IP address instead of DNS/hostname. ([#133654](https://github.com/kubernetes/kubernetes/pull/133654), [@kwohlfahrt](https://github.com/kwohlfahrt)) [SIG API Machinery, Auth, Node and Testing]
- Client-go: Fixed an issue where Reflector could get confused about the resource version it should use to restart a watch while receiving synthetic ADDED events at the beginning of a watch from `resourceVersion` 0 or empty string (`""`). ([#136583](https://github.com/kubernetes/kubernetes/pull/136583), [@michaelasp](https://github.com/michaelasp)) [SIG API Machinery]
- Fixed DRA device taint eviction controller to avoid confusing intermediate status messages by delaying status updates after pod eviction until the informer cache is updated. ([#135611](https://github.com/kubernetes/kubernetes/pull/135611), [@Karthik-K-N](https://github.com/Karthik-K-N)) [SIG Apps and Scheduling]
- Kubelet: Fixed admission to correctly handle DRA-backed extended resources, allowing Pods to be admitted even when these resources are not present in the node's allocatable capacity. ([#135725](https://github.com/kubernetes/kubernetes/pull/135725), [@bart0sh](https://github.com/bart0sh)) [SIG Node, Scheduling and Testing]

### 1.36.1

- Fixed kubelet failure starting on ZFS due to missing cadvisor plugin. ([#138590](https://github.com/kubernetes/kubernetes/pull/138590), [@BenTheElder](https://github.com/BenTheElder)) [SIG Node]
- Fixed stale remote HNS endpoint cleanup on Windows when a pod IP is reused across nodes in L2Bridge networks, preventing DNS timeouts caused by traffic being routed to the wrong node. ([#138603](https://github.com/kubernetes/kubernetes/pull/138603), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]

### 1.36.2

- Avoid costly comparisons during selinux metric emission. ([#139136](https://github.com/kubernetes/kubernetes/pull/139136), [@gnufied](https://github.com/gnufied)) [SIG Apps and Storage]
- Fixed a Dynamic Resource Allocation scheduler bug that could assign mutually exclusive device partitions to multiple Pods. This affected DRA drivers using `SharedCounters` (`DRAPartitionableDevices`) together with multi-allocatable devices (`DRAConsumableCapacity`). Depending on the device and driver, the incorrect double-allocation could cause workload failures, device conflicts, crashes, or data loss. ([#139211](https://github.com/kubernetes/kubernetes/pull/139211), [@ashvindeodhar](https://github.com/ashvindeodhar)) [SIG Node]
- Fixed a bug where Pods that share multi-node claims and also have per-node claims can get stuck in Pending. ([#139363](https://github.com/kubernetes/kubernetes/pull/139363), [@nojnhuh](https://github.com/nojnhuh)) [SIG Node and Scheduling]
- Fixed a kube-scheduler panic when a DRA ResourceClaim using `allocationMode: All` selects a device that consumes shared counters. ([#138988](https://github.com/kubernetes/kubernetes/pull/138988), [@pohly](https://github.com/pohly)) [SIG Node]
- Fixed a panic in the endpoint controller when processing services with empty IPFamilies field (pre-dual-stack services that were never spec-updated). ([#139233](https://github.com/kubernetes/kubernetes/pull/139233), [@rahulbabu95](https://github.com/rahulbabu95)) [SIG Apps and Network]
- Fixed a regression in 1.36 where modifications to scheduling directives (nodeSelector, tolerations, node affinity) on suspended Jobs were rejected if the JobSuspended condition had not yet been set by the job controller. ([#139329](https://github.com/kubernetes/kubernetes/pull/139329), [@kannon92](https://github.com/kannon92)) [SIG Apps and Testing]
- Fixed an issue where kubelet would delete the CSI mount directory when a periodic NodePublishVolume call (triggered by CSIDriver.spec.requiresRepublish=true) returned an error, leaving the pod with stale volume contents that subsequent successful republishes could not repair. ([#139228](https://github.com/kubernetes/kubernetes/pull/139228), [@aramase](https://github.com/aramase)) [SIG Storage]
- Fixes a 1.34+ regression handling containers with environment values set from Secret API objects containing binary non-utf8 data. ([#139192](https://github.com/kubernetes/kubernetes/pull/139192), [@liggitt](https://github.com/liggitt)) [SIG Node]
- Kubeadm: fixed kubeadm init phase certs --dry-run to correctly copy existing CA files. ([#139445](https://github.com/kubernetes/kubernetes/pull/139445), [@HirazawaUi](https://github.com/HirazawaUi)) [SIG Cluster Lifecycle]

### 1.36.3

- Fixed a bug when the DRADeviceTaintRules feature is enabled that caused kube-scheduler to panic when DeviceTaintRules exist and ResourceSlices are changed or to ignore new changes to DeviceTaintRules. ([#139681](https://github.com/kubernetes/kubernetes/pull/139681), [@nojnhuh](https://github.com/nojnhuh)) [SIG Node and Testing]
- Fixed DRA scheduling bugs where the structured allocator mis-counted a device's shared counters while exploring candidates: it could keep a counter reserved after rejecting or backtracking a candidate, or drop a shared device's in-use marker so a later share was charged the counter twice. Either way the allocator could treat a counter set as exhausted and leave a pod pending on a node that could satisfy it. This affected the allocator used by the default feature configuration. ([#140663](https://github.com/kubernetes/kubernetes/pull/140663), [@thc1006](https://github.com/thc1006)) [SIG Node]
- Fixed a kubelet memory leak regression in 1.36 caused by leaked contexts on every Pod sync. ([#140066](https://github.com/kubernetes/kubernetes/pull/140066), [@compumike](https://github.com/compumike)) [SIG Node]
- Fixes a 1.36 regression in server side apply where patching a container type (list or map) could result in `422 required` errors for apply requests that previously succeeded. ([#140296](https://github.com/kubernetes/kubernetes/pull/140296), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery, Architecture, Auth, CLI, Cloud Provider, Cluster Lifecycle, Network, Node, Scheduling and Storage]
- Kubeadm: fix MemberPromote to skip the etcd promote API call when the member is already a voting member, avoiding unnecessary retries and timeout. ([#138493](https://github.com/kubernetes/kubernetes/pull/138493), [@wgkingk](https://github.com/wgkingk)) [SIG Cluster Lifecycle]


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.36.3**, the newest release recorded here for this line.

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
