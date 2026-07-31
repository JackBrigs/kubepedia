---
id: TROUBLE-KUBERNETES_1_29_DEFECTS
type: troubleshooting
title: "kubernetes 1.29: defects fixed in the 1.29 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.29.0 <1.30.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubernetes 1.29 known issues
  - kubernetes 1.29 fixed in
  - is this kubernetes bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubernetes
sources:
  - type: docs
    path: kubernetes/kubernetes release notes for the 1.29 line — bug-fix entries
    url: https://github.com/kubernetes/kubernetes/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubernetes 1.29: defects fixed in the 1.29 line

## Summary

**108 defects** the project fixed across **13 releases** of the 1.29 line, from 1.29.0 to
1.29.13. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.29.0

- Fixed a bug where CEL expressions in CRD validation rules would incorrectly compute a high estimated cost for functions that return strings, lists or maps. The incorrect cost was evident when the result of a function was used in subsequent operations. ([#119800](https://github.com/kubernetes/kubernetes/pull/119800), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery, Auth and Cloud Provider]
- Fixed the API comments for the Job `Ready` field in status. ([#121765](https://github.com/kubernetes/kubernetes/pull/121765), [@mimowo](https://github.com/mimowo))
- Fixed the API comments for the `FailIndex` Job pod failure policy action. ([#121764](https://github.com/kubernetes/kubernetes/pull/121764), [@mimowo](https://github.com/mimowo))
- Fixed `kube-proxy` panicking on exit when the `Node` object changed its `PodCIDR`. ([#120375](https://github.com/kubernetes/kubernetes/pull/120375), [@pegasas](https://github.com/pegasas))
- Fixed bugs in handling of server-side apply, create, and update API requests for objects containing duplicate items in keyed lists. A `create` or `update` API request with duplicate items in a keyed list no longer wipes out managedFields. Examples include env var entries with the same name, or port entries with the same containerPort in a pod spec. A server-side apply request that makes unrelated changes to an object which has duplicate items in a keyed list no longer fails, and leaves the existing duplicate items as-is. A server-side apply request that changes an object which has duplicate items in a keyed list, and modifies the duplicated item removes the duplicates and replaces them with the single item contained in the server-side apply request. ([#121575](https://github.com/kubernetes/kubernetes/pull/121575), [@apelisse](https://github.com/apelisse))
- Fixed overriding default `KubeletConfig` fields in drop-in configs if not set. ([#121193](https://github.com/kubernetes/kubernetes/pull/121193), [@sohankunkerkar](https://github.com/sohankunkerkar))
- DRA: when the scheduler had to deallocate a claim after a node became unsuitable for a pod, it might have needed more attempts than really necessary. This was fixed by first disabling allocations. ([#120428](https://github.com/kubernetes/kubernetes/pull/120428), [@pohly](https://github.com/pohly))
- E2e framework: retrying after intermittent `apiserver` failures was fixed in `WaitForPodsResponding` ([#120559](https://github.com/kubernetes/kubernetes/pull/120559), [@pohly](https://github.com/pohly))
- Fixed CEL estimated cost of `replace()` to handle a zero length replacement string correctly. Previously this would cause the estimated cost to be higher than it should be. ([#120097](https://github.com/kubernetes/kubernetes/pull/120097), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery]
- Fixed OpenAPI v3 not being cleaned up after deleting `APIServices`. ([#120108](https://github.com/kubernetes/kubernetes/pull/120108), [@tnqn](https://github.com/tnqn))
- Fixed [121094](https://github.com/kubernetes/kubernetes/issues/121094) by re-introducing the readiness predicate for `externalTrafficPolicy: Local` services. ([#121116](https://github.com/kubernetes/kubernetes/pull/121116), [@alexanderConstantinescu](https://github.com/alexanderConstantinescu))
- Fixed `kubectl events` not filtering events by `GroupVersion` for resources with a full name. ([#120119](https://github.com/kubernetes/kubernetes/pull/120119), [@Ithrael](https://github.com/Ithrael))
- Fixed `systemLogQuery` service name matching. ([#120678](https://github.com/kubernetes/kubernetes/pull/120678), [@rothgar](https://github.com/rothgar))
- Fixed a `1.27` scheduling regression that `PostFilter` plugin may not function if previous `PreFilter` plugins return `Skip`. ([#119769](https://github.com/kubernetes/kubernetes/pull/119769), [@Huang-Wei](https://github.com/Huang-Wei))
- Fixed a `v1.26` regression scheduling bug by ensuring that preemption is skipped when a `PreFilter` plugin returns `UnschedulableAndUnresolvable`. ([#119778](https://github.com/kubernetes/kubernetes/pull/119778), [@sanposhiho](https://github.com/sanposhiho))
- Fixed a `v1.28.0` regression where `kube-controller-manager` can crash when `StatefulSet` with `Parallel` policy and PVC labels are scaled up. ([#121142](https://github.com/kubernetes/kubernetes/pull/121142), [@aleksandra-malinowska](https://github.com/aleksandra-malinowska))
- Fixed a `v1.28` regression around restarting init containers in the right order relative to normal containers. ([#120281](https://github.com/kubernetes/kubernetes/pull/120281), [@gjkim42](https://github.com/gjkim42))
- Fixed a `v1.28` regression handling negative index json patches. ([#120327](https://github.com/kubernetes/kubernetes/pull/120327), [@liggitt](https://github.com/liggitt))
- Fixed a `v1.28` regression in scheduler: a pod with concurrent events could incorrectly get moved to the unschedulable queue where it could get stuck until the next periodic purging after 5 minutes, if there was no other event for it. ([#120413](https://github.com/kubernetes/kubernetes/pull/120413), [@pohly](https://github.com/pohly))
- Fixed a bug around restarting init containers in the right order relative to normal containers with `SidecarContainers` feature enabled. ([#120269](https://github.com/kubernetes/kubernetes/pull/120269), [@gjkim42](https://github.com/gjkim42))
- Fixed a bug in the cronjob controller where already created jobs might be missing from the status. ([#120649](https://github.com/kubernetes/kubernetes/pull/120649), [@andrewsykim](https://github.com/andrewsykim))
- Fixed a bug where `Services` using finalizers may hold onto `ClusterIP` and/or `NodePort` allocated resources for longer than expected if the finalizer is removed using the status subresource. ([#120623](https://github.com/kubernetes/kubernetes/pull/120623), [@aojea](https://github.com/aojea))
- Fixed a bug where an API group's path was not unregistered from the API server's root paths when the group was deleted. ([#121283](https://github.com/kubernetes/kubernetes/pull/121283), [@tnqn](https://github.com/tnqn)) [SIG API Machinery and Testing]
- Fixed a bug where containers would not start on `cgroupv2` systems where `swap` is disabled. ([#120784](https://github.com/kubernetes/kubernetes/pull/120784), [@elezar](https://github.com/elezar))
- Fixed a bug where the CPU set allocated to an init container, with containerRestartPolicy of `Always`, were erroneously reused by a regular container. ([#119447](https://github.com/kubernetes/kubernetes/pull/119447), [@gjkim42](https://github.com/gjkim42)) [SIG Node and Testing]
- Fixed a bug where the device resources allocated to an init container, with `containerRestartPolicy` of `Always`, were erroneously reused by a regular container. ([#120461](https://github.com/kubernetes/kubernetes/pull/120461), [@gjkim42](https://github.com/gjkim42))
- Fixed a bug where the memory resources allocated to an init container, with containerRestartPolicy of `Always`, were erroneously reused by a regular container. ([#120715](https://github.com/kubernetes/kubernetes/pull/120715), [@gjkim42](https://github.com/gjkim42)) [SIG Node]
- Fixed a concurrent map access in `TopologyCache`'s `HasPopulatedHints` method. ([#118189](https://github.com/kubernetes/kubernetes/pull/118189), [@Miciah](https://github.com/Miciah))
- Fixed a regression (`CLIENTSET_PKG: unbound variable`) when invoking deprecated `generate-groups.sh` script. ([#120877](https://github.com/kubernetes/kubernetes/pull/120877), [@soltysh](https://github.com/soltysh))
- Fixed a regression in `kube-proxy` where it might refuse to start if given single-stack `IPv6` configuration options on a node that has both `IPv4` and `IPv6` IPs. ([#121008](https://github.com/kubernetes/kubernetes/pull/121008), [@danwinship](https://github.com/danwinship))
- Fixed a regression in default configurations, which enabled `PodDisruptionConditions` by default, that prevented the control plane's pod garbage collector from deleting pods that contained duplicated field keys (environmental variables with repeated keys or container ports). ([#121103](https://github.com/kubernetes/kubernetes/pull/121103), [@mimowo](https://github.com/mimowo))
- Fixed a regression in the default `v1.27` configurations in `kube-apiserver`: fixed the `AggregatedDiscoveryEndpoint` feature (`beta` in `v1.27+`) to successfully fetch discovery information from aggregated API servers that do not check `Accept` headers when serving the `/apis` endpoint. ([#119870](https://github.com/kubernetes/kubernetes/pull/119870), [@Jefftree](https://github.com/Jefftree))
- Fixed a regression in the kubelet's behavior while creating a container when the `EventedPLEG` feature gate is enabled. ([#120942](https://github.com/kubernetes/kubernetes/pull/120942), [@sairameshv](https://github.com/sairameshv))
- Fixed a regression since `v1.27.0` in the scheduler framework when running score plugins. The `skippedScorePlugins` number might be greater than `enabledScorePlugins`, so when initializing a slice the `cap(len(skippedScorePlugins) - len(enabledScorePlugins))` is negative, which is not allowed. ([#121632](https://github.com/kubernetes/kubernetes/pull/121632), [@kerthcet](https://github.com/kerthcet))
- Fixed a situation when, sometimes, the scheduler incorrectly placed a pod in the `unschedulable` queue instead of the `backoff` queue. This happened when some plugin previously declared the pod as `unschedulable` and then in a later attempt encounters some other error. Scheduling of that pod then got delayed by up to five minutes, after which periodic flushing moved the pod back into the `active` queue. ([#120334](https://github.com/kubernetes/kubernetes/pull/120334), [@pohly](https://github.com/pohly))
- Fixed an issue related to not draining all the pods in a namespace when an empty selector, i.e., "{}," is specified in a Pod Disruption Budget (PDB). ([#119732](https://github.com/kubernetes/kubernetes/pull/119732), [@sairameshv](https://github.com/sairameshv))
- Fixed an issue where `StatefulSet` might not restart a pod after eviction or node failure. ([#120398](https://github.com/kubernetes/kubernetes/pull/120398), [@aleksandra-malinowska](https://github.com/aleksandra-malinowska))
- Fixed an issue where a `CronJob` could fail to clean up Jobs when the `ResourceQuota` for `Jobs` had been reached. ([#119776](https://github.com/kubernetes/kubernetes/pull/119776), [@ASverdlov](https://github.com/ASverdlov))
- Fixed an issue where a `StatefulSet` might not restart a pod after eviction or node failure. ([#121389](https://github.com/kubernetes/kubernetes/pull/121389), [@aleksandra-malinowska](https://github.com/aleksandra-malinowska))
- Fixed an issue with the `garbagecollection` controller registering duplicate event handlers if discovery requests failed. ([#117992](https://github.com/kubernetes/kubernetes/pull/117992), [@liggitt](https://github.com/liggitt))
- Fixed attaching volumes after detach errors. Now volumes that failed to detach are not treated as attached. Kubernetes will make sure they are fully attached before they can be used by pods. ([#120595](https://github.com/kubernetes/kubernetes/pull/120595), [@jsafrane](https://github.com/jsafrane))
- Fixed bug that kubelet resource metric `container_start_time_seconds` had timestamp equal to container start time. ([#120518](https://github.com/kubernetes/kubernetes/pull/120518), [@saschagrunert](https://github.com/saschagrunert)) [SIG Instrumentation, Node and Testing]
- Fixed inconsistency in the calculation of number of nodes that have an image, which affect the scoring in the `ImageLocality` plugin. ([#116938](https://github.com/kubernetes/kubernetes/pull/116938), [@olderTaoist](https://github.com/olderTaoist))
- Fixed issue with incremental id generation for `loadbalancer` and `endpoint` in `kubeproxy` mock test framework. ([#120723](https://github.com/kubernetes/kubernetes/pull/120723), [@princepereira](https://github.com/princepereira))
- Fixed panic in Job controller when `podRecreationPolicy: Failed` is used, and the number of terminating pods exceeds parallelism. ([#121147](https://github.com/kubernetes/kubernetes/pull/121147), [@kannon92](https://github.com/kannon92))
- Fixed regression with adding aggregated `APIservices` panicking and affected health check introduced in release `v1.28.0`. ([#120814](https://github.com/kubernetes/kubernetes/pull/120814), [@Jefftree](https://github.com/Jefftree))
- Fixed some invalid and unimportant log calls. ([#121249](https://github.com/kubernetes/kubernetes/pull/121249), [@pohly](https://github.com/pohly)) [SIG Cloud Provider, Cluster Lifecycle and Testing]
- Fixed stale SMB mount issue when SMB file share is deleted and then unmounted. ([#121851](https://github.com/kubernetes/kubernetes/pull/121851), [@andyzhangx](https://github.com/andyzhangx))
- Fixed the bug where images that were pinned by the container runtime could be garbage collected by `kubelet`. ([#119986](https://github.com/kubernetes/kubernetes/pull/119986), [@ruiwen-zhao](https://github.com/ruiwen-zhao))
- Fixed the bug where kubelet couldn't output logs after log file rotated when `kubectl logs POD_NAME -f` is running. ([#115702](https://github.com/kubernetes/kubernetes/pull/115702), [@xyz-li](https://github.com/xyz-li))
- Fixed the calculation of the requeue time in the cronjob controller, resulting in proper handling of failed/stuck jobs. ([#121327](https://github.com/kubernetes/kubernetes/pull/121327), [@soltysh](https://github.com/soltysh))
- Fixed the issue where pod with ordinal number lower than the rolling partitioning number was being deleted. It was coming up with updated image. ([#120731](https://github.com/kubernetes/kubernetes/pull/120731), [@adilGhaffarDev](https://github.com/adilGhaffarDev))
- Fixed tracking of terminating Pods in the Job status. The field was not updated unless there were other changes to apply. ([#121342](https://github.com/kubernetes/kubernetes/pull/121342), [@dejanzele](https://github.com/dejanzele))
- KCCM: fixed transient node addition and removal caused by #121090 while syncing load balancers on large clusters with a lot of churn. ([#121091](https://github.com/kubernetes/kubernetes/pull/121091), [@alexanderConstantinescu](https://github.com/alexanderConstantinescu))
- `kubeadm`: Fixed the bug where it always did CRI detection when `--config` was passed, even if it is not required by the subcommand. ([#120828](https://github.com/kubernetes/kubernetes/pull/120828), [@SataQiu](https://github.com/SataQiu))
- `kubeadm`: fixed `nil` pointer when `etcd` member is already removed. ([#119753](https://github.com/kubernetes/kubernetes/pull/119753), [@pacoxu](https://github.com/pacoxu))
- `kubeadm`: fixed the bug where `--image-repository` flag is missing for some init phase sub-commands. ([#120072](https://github.com/kubernetes/kubernetes/pull/120072), [@SataQiu](https://github.com/SataQiu))
- `scheduler`: Fixed missing field `apiVersion` from events reported by the taint manager. ([#114095](https://github.com/kubernetes/kubernetes/pull/114095), [@aimuz](https://github.com/aimuz))
- Fixed an issue where the `vsphere` cloud provider would not trust a certificate if: The issuer of the certificate was unknown (`x509.UnknownAuthorityError`) The requested name did not match the set of authorized names (`x509.HostnameError`) The error surfaced after attempting a connection contained one of the substrings: "certificate is not trusted" or "certificate signed by unknown authority". ([#120736](https://github.com/kubernetes/kubernetes/pull/120736), [@MadhavJivrajani](https://github.com/MadhavJivrajani))
- Fixed bug where `Adding GroupVersion` log line was constantly repeated without any group version changes. ([#119825](https://github.com/kubernetes/kubernetes/pull/119825), [@Jefftree](https://github.com/Jefftree))

### 1.29.1

- Fixes accidental enablement of the new alpha `optionalOldSelf` API field in CustomResourceDefinition validation rules, which should only be allowed to be set when the CRDValidationRatcheting feature gate is enabled. Existing CustomResourceDefinition objects which have the field set will retain it on update, but new CustomResourceDefinition objects will not be permitted to set the field while the CRDValidationRatcheting feature gate is disabled. ([#122343](https://github.com/kubernetes/kubernetes/pull/122343), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery]
- Fix an issue where kubectl apply could panic when imported as a library ([#122559](https://github.com/kubernetes/kubernetes/pull/122559), [@Jefftree](https://github.com/Jefftree)) [SIG CLI]
- Fix: Mount point may become local without calling NodePublishVolume after node rebooting. ([#119923](https://github.com/kubernetes/kubernetes/pull/119923), [@cvvz](https://github.com/cvvz)) [SIG Node and Storage]
- Fixed a regression since 1.24 in the scheduling framework when overriding MultiPoint plugins (e.g. default plugins). The incorrect loop logic might lead to a plugin being loaded multiple times, consequently preventing any Pod from being scheduled, which is unexpected. ([#122366](https://github.com/kubernetes/kubernetes/pull/122366), [@caohe](https://github.com/caohe)) [SIG Scheduling]
- Fixed migration of in-tree vSphere volumes to the CSI driver. ([#122341](https://github.com/kubernetes/kubernetes/pull/122341), [@jsafrane](https://github.com/jsafrane)) [SIG Storage]

### 1.29.2

- Fix deprecated version for pod_scheduling_duration_seconds that caused the metric to be hidden by default in 1.29. ([#123042](https://github.com/kubernetes/kubernetes/pull/123042), [@alculquicondor](https://github.com/alculquicondor)) [SIG Instrumentation and Scheduling]
- Fixed a bug in ValidatingAdmissionPolicy that caused policies which were using CRD parameters to fail to synchronize ([#123080](https://github.com/kubernetes/kubernetes/pull/123080), [@alexzielenski](https://github.com/alexzielenski)) [SIG API Machinery and Testing]
- Fixes a 1.29 regression in "kubeadm init" that caused a user-specified --kubeconfig file to be ignored. ([#122792](https://github.com/kubernetes/kubernetes/pull/122792), [@avorima](https://github.com/avorima)) [SIG Cluster Lifecycle]
- Fixes a race condition in the iptables mode of kube-proxy in 1.27 and later that could result in some updates getting lost (e.g., when a service gets a new endpoint, the rules for the new endpoint might not be added until much later). ([#122756](https://github.com/kubernetes/kubernetes/pull/122756), [@hakman](https://github.com/hakman)) [SIG Network]
- Kubeadm: fix a bug where the --rootfs global flag does not work with "kubeadm upgrade node" for control plane nodes. ([#123096](https://github.com/kubernetes/kubernetes/pull/123096), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]

### 1.29.3

- Fix error when trying to expand a volume that does not require node expansion ([#123055](https://github.com/kubernetes/kubernetes/pull/123055), [@gnufied](https://github.com/gnufied)) [SIG Node and Storage]
- Fixed a bug that an init container with containerRestartPolicy with `Always` cannot update its state from terminated to non-terminated for the pod with restartPolicy with `Never` or `OnFailure`. ([#123709](https://github.com/kubernetes/kubernetes/pull/123709), [@gjkim42](https://github.com/gjkim42)) [SIG Apps]
- Fixed cleanup of Pod volume mounts when a file was used as a subpath. ([#123052](https://github.com/kubernetes/kubernetes/pull/123052), [@jsafrane](https://github.com/jsafrane)) [SIG Node]
- Fixed the disruption controller's PDB status synchronization to maintain all PDB conditions during an update. ([#122056](https://github.com/kubernetes/kubernetes/pull/122056), [@dhenkel92](https://github.com/dhenkel92)) [SIG Apps]
- Fixes an issue calculating total CPU usage reported for Windows nodes ([#122999](https://github.com/kubernetes/kubernetes/pull/122999), [@marosset](https://github.com/marosset)) [SIG Node and Windows]
- Prevent watch cache starvation by moving its watch to separate RPC and add a SeparateCacheWatchRPC feature flag to disable this behavior ([#123693](https://github.com/kubernetes/kubernetes/pull/123693), [@mengqiy](https://github.com/mengqiy)) [SIG API Machinery]

### 1.29.4

- Fix pod restart after node reboot when NewVolumeManagerReconstruction feature gate is enabled and SELinuxMountReadWriteOncePod disabled ([#124140](https://github.com/kubernetes/kubernetes/pull/124140), [@bertinatto](https://github.com/bertinatto)) [SIG Node]
- Kube-apiserver: fixes a 1.27+ regression in watch stability by serving watch requests without a resourceVersion from the watch cache by default, as in <1.27 (disabling the change in #115096 by default). This mitigates the impact of an etcd watch bug (https://github.com/etcd-io/etcd/pull/17555). If the 1.27 change in #115096 to serve these requests from underlying storage is still desired despite the impact on watch stability, it can be re-enabled with a `WatchFromStorageWithoutResourceVersion` feature gate. ([#123973](https://github.com/kubernetes/kubernetes/pull/123973), [@serathius](https://github.com/serathius)) [SIG API Machinery]
- Kubeadm: fix panic in the command "kubeadm certs check-expiration" when "/etc/kubernetes/pki" exists but cannot be read. ([#124124](https://github.com/kubernetes/kubernetes/pull/124124), [@carlory](https://github.com/carlory)) [SIG Cluster Lifecycle]

### 1.29.5

- Fixed a bug that a pod may remain unscheduled if any PreFilter plugin returns nodes that do not exist. ([#124559](https://github.com/kubernetes/kubernetes/pull/124559), [@chengjoey](https://github.com/chengjoey)) [SIG Scheduling and Testing]
- Fixes a 1.29.0 regression that introduced a possible data race that could cause panics in kube-controller-manager and kube-scheduler ([#124518](https://github.com/kubernetes/kubernetes/pull/124518), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery and Scheduling]
- Kubeadm: fix a bug when using external CA mode and trying to upgrade to 1.29 using "kubeadm upgrade apply". Show a warning that kubeadm cannot sign the new "super-admin.conf" as the host does not have a CA and show some instructions on how to manually migrate to the separate "admin.conf" and "super-admin.conf" kubeconfig files. ([#124682](https://github.com/kubernetes/kubernetes/pull/124682), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]

### 1.29.6

- Fixed PersistentolumeLabel providing wrong topology labels to Azure Disk PersistentVolumes when the external Azure cloud provider is used. ([#124528](https://github.com/kubernetes/kubernetes/pull/124528), [@jsafrane](https://github.com/jsafrane)) [SIG Cloud Provider]
- Kube-apiserver: fixes a 1.28 regression printing pods with invalid initContainer status ([#124909](https://github.com/kubernetes/kubernetes/pull/124909), [@liggitt](https://github.com/liggitt)) [SIG Node]
- Kube-scheduler: fixes a 1.29.5 regression that can lead to a scheduler crash when processing pods with affinity that doesn't match a real/valid node ([#125041](https://github.com/kubernetes/kubernetes/pull/125041), [@AxeZhan](https://github.com/AxeZhan)) [SIG Scheduling and Testing]
- Reduce critical section in watchcache to fix kube-apiserver scalability under heavy load of list requests ([#122027](https://github.com/kubernetes/kubernetes/pull/122027), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery]

### 1.29.7

- Fix a bug that Pods could stuck in the unschedulable pod pool if they're rejected by PreEnqueue plugins that could change its result by a change in resources apart from Pods
- Fix endpoints status out-of-sync when the pod state changes rapidly ([#125675](https://github.com/kubernetes/kubernetes/pull/125675), [@tnqn](https://github.com/tnqn)) [SIG Apps, Network and Testing]

### 1.29.8

- Fixed a bug in the API server where empty collections of ValidatingAdmissionPolicies did not have an `items` field. ([#126157](https://github.com/kubernetes/kubernetes/pull/126157), [@xyz-li](https://github.com/xyz-li)) [SIG API Machinery]
- Fix the bug where PodIP field is temporarily removed for a terminal pod ([#125404](https://github.com/kubernetes/kubernetes/pull/125404), [@mimowo](https://github.com/mimowo)) [SIG Node and Testing]
- Fixed a bug that init containers with `Always` restartPolicy may not terminate gracefully if the pod hasn't initialized yet. ([#126332](https://github.com/kubernetes/kubernetes/pull/126332), [@gjkim42](https://github.com/gjkim42)) [SIG Node and Testing]
- Kube-apiserver: fixes a 1.27+ regression watching a single namespace via the deprecated /api/v1/watch/namespaces/$name endpoint where watch events were not delivered after the watch was established ([#126151](https://github.com/kubernetes/kubernetes/pull/126151), [@xyz-li](https://github.com/xyz-li)) [SIG API Machinery and Testing]
- Kube-apiserver: fixes a potential crash serving CustomResourceDefinitions that combine an invalid schema and CEL validation rules. ([#126167](https://github.com/kubernetes/kubernetes/pull/126167), [@cici37](https://github.com/cici37)) [SIG API Machinery and Testing]

### 1.29.9

- Fix a scheduler preemption issue where the victim pod was not deleted due to incorrect status patching. This issue occurred when the preemptor and victim pods had different QoS classes in their status, causing the preemption to fail entirely. ([#126694](https://github.com/kubernetes/kubernetes/pull/126694), [@Huang-Wei](https://github.com/Huang-Wei)) [SIG Scheduling]
- Fix race condition in kube-proxy initialization that could blackhole UDP traffic to service VIP. ([#126689](https://github.com/kubernetes/kubernetes/pull/126689), [@wedaly](https://github.com/wedaly)) [SIG Network]
- Fixed a bug where init containers may fail to start due to a temporary container runtime failure. ([#127214](https://github.com/kubernetes/kubernetes/pull/127214), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG Node]
- Fixed a regression in 1.29+ default configurations, where regular init containers may fail to start due to a temporary container runtime failure. ([#127204](https://github.com/kubernetes/kubernetes/pull/127204), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG Node]
- Terminated Pods on a node will not be re-admitted on kubelet restart. This fixes the problem of Completed Pods awaiting for the finalizer marked as Failed after the kubelet restart. ([#127209](https://github.com/kubernetes/kubernetes/pull/127209), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG Node and Testing]

### 1.29.10

- Fix a bug on the endpoints controller that does not reconcile the Endpoint object after this is truncated (it gets more than 1000 endpoints addresses) ([#127417](https://github.com/kubernetes/kubernetes/pull/127417), [@aojea](https://github.com/aojea)) [SIG Apps, Network and Testing]
- Fixes a kubelet and kube-apiserver memory leak in default 1.29 configurations related to tracing. ([#126985](https://github.com/kubernetes/kubernetes/pull/126985), [@dashpole](https://github.com/dashpole)) [SIG API Machinery and Node]
- Fixes a regression introduced in 1.29 where conntrack entries for UDP connections to deleted pods did not get cleaned up correctly, which could (among other things) cause DNS problems when DNS pods were restarted. ([#127808](https://github.com/kubernetes/kubernetes/pull/127808), [@danwinship](https://github.com/danwinship)) [SIG Network]
- Kubeadm: fix wrong member list reported when removing an etcd member ([#127962](https://github.com/kubernetes/kubernetes/pull/127962), [@SataQiu](https://github.com/SataQiu)) [SIG Cluster Lifecycle]

### 1.29.11

- Fix a bug when the hostname label of a node does not match the node name, pods bound to a PV with nodeAffinity using the hostname may be scheduled to the wrong node or experience scheduling failures. ([#127586](https://github.com/kubernetes/kubernetes/pull/127586), [@AxeZhan](https://github.com/AxeZhan)) [SIG Scheduling and Storage]
- Fixed a suboptimal scheduler preemption behavior where potential preemption victims were violating Pod Disruption Budgets. ([#128435](https://github.com/kubernetes/kubernetes/pull/128435), [@NoicFank](https://github.com/NoicFank)) [SIG Scheduling]

### 1.29.13

- Fix kubelet on Windows fails if a pod has SecurityContext with RunAsUser ([#129508](https://github.com/kubernetes/kubernetes/pull/129508), [@carlory](https://github.com/carlory)) [SIG Storage, Testing and Windows]
- Fixed a storage bug around multipath. iSCSI and Fibre Channel devices attached to nodes via multipath now resolve correctly if partitioned. ([#129183](https://github.com/kubernetes/kubernetes/pull/129183), [@RomanBednar](https://github.com/RomanBednar)) [SIG Storage]
- Fixes a panic in kube-controller-manager handling StatefulSet objects when revisionHistoryLimit is negative ([#129325](https://github.com/kubernetes/kubernetes/pull/129325), [@ardaguclu](https://github.com/ardaguclu)) [SIG Apps]
- Kubelet: Fix the volume manager didn't check the device mount state in the actual state of the world before marking the volume as detached. It may cause a pod to be stuck in the Terminating state due to the above issue when it was deleted. ([#129064](https://github.com/kubernetes/kubernetes/pull/129064), [@carlory](https://github.com/carlory)) [SIG Node]


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.29.13**, the newest release recorded here for this line.

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
