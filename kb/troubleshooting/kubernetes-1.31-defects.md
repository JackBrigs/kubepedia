---
id: TROUBLE-KUBERNETES_1_31_DEFECTS
type: troubleshooting
title: "kubernetes 1.31: defects fixed in the 1.31 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.31.0 <1.32.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubernetes 1.31 known issues
  - kubernetes 1.31 fixed in
  - is this kubernetes bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubernetes
sources:
  - type: docs
    path: kubernetes/kubernetes release notes for the 1.31 line — bug-fix entries
    url: https://github.com/kubernetes/kubernetes/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubernetes 1.31: defects fixed in the 1.31 line

## Summary

**91 defects** the project fixed across **13 releases** of the 1.31 line, from 1.31.0 to
1.31.14. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.31.0

- Fixed a 1.30.0 regression in OpenAPI descriptions of the `imagePullSecrets` and `hostAliases` fields to mark the fields used as keys in those lists as either defaulted or required. ([#124553](https://github.com/kubernetes/kubernetes/pull/124553), [@pmalek](https://github.com/pmalek))
- Fixed a 1.30.0 regression in openapi descriptions of `PodIP.IP` and `HostIP.IP` fields to mark the fields used as keys in those lists as required. ([#126057](https://github.com/kubernetes/kubernetes/pull/126057), [@thockin](https://github.com/thockin))
- Fixed a bug in the API server where empty collections of ValidatingAdmissionPolicies did not have an `items` field. ([#124568](https://github.com/kubernetes/kubernetes/pull/124568), [@xyz-li](https://github.com/xyz-li)) [SIG API Machinery]
- Fixed a deep copy issue when retrieving the controller reference. ([#124116](https://github.com/kubernetes/kubernetes/pull/124116), [@HiranmoyChowdhury](https://github.com/HiranmoyChowdhury)) [SIG API Machinery and Release]
- Fixed code-generator client-gen to work with `api/v1`-like package structure. ([#125162](https://github.com/kubernetes/kubernetes/pull/125162), [@sttts](https://github.com/sttts)) [SIG API Machinery and Apps]
- Fixed incorrect "v1 Binding is deprecated in v1.6+" warning in kube-scheduler log. ([#125540](https://github.com/kubernetes/kubernetes/pull/125540), [@pohly](https://github.com/pohly)) [SIG API Machinery]
- Fixed the comment for the Job's managedBy field. ([#124793](https://github.com/kubernetes/kubernetes/pull/124793), [@mimowo](https://github.com/mimowo)) [SIG API Machinery and Apps]
- Fixed the documentation for the default value of the `procMount` entry in `securityContext` within a Pod. The documentation was previously using the name of the internal variable `DefaultProcMount`, rather than the actual value, "Default". ([#125782](https://github.com/kubernetes/kubernetes/pull/125782), [@aborrero](https://github.com/aborrero)) [SIG Apps and Node]
- Fixed a missing behavior where Windows nodes did not implement memory-pressure eviction. ([#122922](https://github.com/kubernetes/kubernetes/pull/122922), [@marosset](https://github.com/marosset)) [SIG Node, Testing and Windows]
- Fixed bug in kubelet if the `SplitImageFilesystem` feature gate is turned on but the container runtime is not configured. ([#126335](https://github.com/kubernetes/kubernetes/pull/126335), [@kannon92](https://github.com/kannon92))
- Fixed issue where following Windows container logs would prevent container log rotation. ([#124444](https://github.com/kubernetes/kubernetes/pull/124444), [@claudiubelu](https://github.com/claudiubelu)) [SIG Node, Testing and Windows]
- "Fixed the ResourceClaim controller forgetting to wait for `podSchedulingSynced` and `templatesSynced`." ([#124589](https://github.com/kubernetes/kubernetes/pull/124589), [@carlory](https://github.com/carlory)) [SIG Apps and Node]
- 'kubeadm: fixed a regression where the KubeletConfiguration is not properly downloaded during "kubeadm upgrade" command from the kube-system/kubelet-config ConfigMap, resulting in the local ''/var/lib/kubelet/config.yaml'' file being written as a defaulted config.' ([#124480](https://github.com/kubernetes/kubernetes/pull/124480), [@neolit123](https://github.com/neolit123))
- Client-go/tools/record.Broadcaster: Fixed automatic shutdown on WithContext cancellation. ([#124635](https://github.com/kubernetes/kubernetes/pull/124635), [@pohly](https://github.com/pohly))
- Fix a bug that when PodTopologySpread rejects Pods, they may be stuck in Pending state for 5 min in a worst case scenario. The same problem could happen with custom plugins which have Pod/Add or Pod/Update in EventsToRegister, which is also solved with this PR, but only when the feature flag SchedulerQueueingHints is enabled. ([#122627](https://github.com/kubernetes/kubernetes/pull/122627), [@sanposhiho](https://github.com/sanposhiho)) [SIG Scheduling and Testing]
- Fix bug where Server Side Apply causing spurious resourceVersion bumps on no-op patches containing empty maps. ([#125317](https://github.com/kubernetes/kubernetes/pull/125317), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery and Testing]
- Fix endpoints status out-of-sync when the pod state changes rapidly ([#125675](https://github.com/kubernetes/kubernetes/pull/125675), [@tnqn](https://github.com/tnqn)) [SIG Apps, Network and Testing]
- Fix the bug where PodIP field is temporarily removed for a terminal pod ([#125404](https://github.com/kubernetes/kubernetes/pull/125404), [@mimowo](https://github.com/mimowo)) [SIG Node and Testing]
- Fixed "-kube-test-repo-list" e2e flag may not take effect. ([#123587](https://github.com/kubernetes/kubernetes/pull/123587), [@huww98](https://github.com/huww98)) [SIG API Machinery, Apps, Autoscaling, CLI, Network, Node, Scheduling, Storage, Testing and Windows]
- Fixed EDITOR/KUBE_EDITOR with double-quoted paths with spaces when on Windows cmd.exe. ([#112104](https://github.com/kubernetes/kubernetes/pull/112104), [@oldium](https://github.com/oldium)) [SIG CLI and Windows]
- Fixed a bug in storage-version-migrator-controller that would cause migration attempts to fail if resources were deleted when the migration was in progress. ([#126107](https://github.com/kubernetes/kubernetes/pull/126107), [@enj](https://github.com/enj)) [SIG API Machinery, Apps, Auth and Testing]
- Fixed a bug in the JSON frame reader that could cause it to retain a reference to the underlying array of the byte slice passed to read. ([#123620](https://github.com/kubernetes/kubernetes/pull/123620), [@benluddy](https://github.com/benluddy))
- Fixed a bug in the scheduler where it would crash when prefilter returns a non-existent node. ([#124933](https://github.com/kubernetes/kubernetes/pull/124933), [@AxeZhan](https://github.com/AxeZhan)) [SIG Scheduling and Testing]
- Fixed a bug that Pods could stuck in the unschedulable pod pool if they're rejected by PreEnqueue plugins that could change its result by a change in resources apart from Pods
- Fixed a bug that init containers with `Always` restartPolicy may not terminate gracefully if the pod hasn't initialized yet. ([#125935](https://github.com/kubernetes/kubernetes/pull/125935), [@gjkim42](https://github.com/gjkim42)) [SIG Node and Testing]
- Fixed a bug where `kubectl describe` incorrectly displayed NetworkPolicy port ranges (showing only the starting port). ([#123316](https://github.com/kubernetes/kubernetes/pull/123316), [@jcaamano](https://github.com/jcaamano))
- Fixed a bug where hard evictions due to resource pressure allowed pods to use the full termination grace period instead of shutting down instantly. This bug also affected force deleted pods. Both cases now receive a termination grace period of 1 second. ([#124063](https://github.com/kubernetes/kubernetes/pull/124063), [@olyazavr](https://github.com/olyazavr))
- Fixed a bug where the Kubelet miscalculated the process usage of pods, causing pods to never get evicted for PID usage. ([#124101](https://github.com/kubernetes/kubernetes/pull/124101), [@haircommander](https://github.com/haircommander)) [SIG Node and Testing]
- Fixed a missing status prefix in custom resource validation error messages. ([#123822](https://github.com/kubernetes/kubernetes/pull/123822), [@JoelSpeed](https://github.com/JoelSpeed))
- Fixed a race condition in kube-controller-manager and the scheduler, caused by a bug in the transforming informer during the Resync operation, by making the transforming function idempotent. ([#124352](https://github.com/kubernetes/kubernetes/pull/124352), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery and Scheduling]
- Fixed a race condition in the transforming informer that occurred when objects were accessed during the Resync operation. ([#124344](https://github.com/kubernetes/kubernetes/pull/124344), [@wojtek-t](https://github.com/wojtek-t))
- Fixed a regression where `kubelet --hostname-override` no longer worked correctly with an external cloud provider. ([#124516](https://github.com/kubernetes/kubernetes/pull/124516), [@danwinship](https://github.com/danwinship))
- Fixed an issue that prevents the linking of trace spans for requests that are proxied through kube-aggregator. ([#124189](https://github.com/kubernetes/kubernetes/pull/124189), [@toddtreece](https://github.com/toddtreece))
- Fixed an issue where kubelet on Windows would fail if a pod had a SecurityContext with `RunAsUser`. ([#125040](https://github.com/kubernetes/kubernetes/pull/125040), [@carlory](https://github.com/carlory)) [SIG Storage, Testing and Windows]
- Fixed an issue where the Service LoadBalancer controller was not correctly considering the `service.Status new IPMode` field and excluding the Ports when checking if the status was changed, resulting in the changed field potentially not to update the `service.Status` correctly. ([#125225](https://github.com/kubernetes/kubernetes/pull/125225), [@aojea](https://github.com/aojea)) [SIG Apps, Cloud Provider and Network]
- Fixed bug where Server Side Apply causes spurious resourceVersion bumps on no-op patches to custom resources. ([#125263](https://github.com/kubernetes/kubernetes/pull/125263), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery and Testing]
- Fixed bug where kubectl get with --sort-by flag does not sort strings alphanumerically. ([#124514](https://github.com/kubernetes/kubernetes/pull/124514), [@brianpursley](https://github.com/brianpursley))
- Fixed fake clientset ApplyScale subresource from `status` to `scale`. ([#126073](https://github.com/kubernetes/kubernetes/pull/126073), [@a7i](https://github.com/a7i))
- Fixed kubelet so it would no longer crash when a DRA(Dynamic Resource Allocation) driver returns a nil as part of the Node(Un)PrepareResources response instead of an empty struct (Did not affect drivers written in Go, first showed up with a driver written in Rust). returns a nil as part of the Node(Un)PrepareResources response instead of an empty struct (did not affect drivers written in Go, first showed up with a driver written in Rust). ([#124091](https://github.com/kubernetes/kubernetes/pull/124091), [@bitoku](https://github.com/bitoku))
- Fixed node reporting "notReady" with the reason 'container runtime status check may not have completed yet' after kubelet restart. ([#124430](https://github.com/kubernetes/kubernetes/pull/124430), [@AllenXu93](https://github.com/AllenXu93))
- Fixed null `lastTransitionTime` in Pod condition when setting the scheduling gate. ([#122636](https://github.com/kubernetes/kubernetes/pull/122636), [@lianghao208](https://github.com/lianghao208)) [SIG Node and Scheduling]
- Fixed recursive LIST from watch cache returning object matching key. ([#125584](https://github.com/kubernetes/kubernetes/pull/125584), [@serathius](https://github.com/serathius)) [SIG API Machinery and Testing]
- Fixed sample-cli-plugin help text to be consistent and always use `kubectl ns`. ([#125641](https://github.com/kubernetes/kubernetes/pull/125641), [@nirs](https://github.com/nirs))
- Fixed the bug where if Endpointslices mirrored from Endpoints by the EndpointSliceMirroring controller they would not reconcile if modified. were not reconciled if modified ([#124131](https://github.com/kubernetes/kubernetes/pull/124131), [@zyjhtangtang](https://github.com/zyjhtangtang)) [SIG Apps and Network]
- Fixed the format of the error indicating that a user does not have permission on the object referenced by paramRef in ValidatingAdmissionPolicyBinding. ([#124653](https://github.com/kubernetes/kubernetes/pull/124653), [@m1kola](https://github.com/m1kola))
- Fixed throughput when scheduling DaemonSet pods to reach 300 pods/s, if the configured QPS allows it. ([#124714](https://github.com/kubernetes/kubernetes/pull/124714), [@sanposhiho](https://github.com/sanposhiho))
- Fixed: during the kube-controller-manager restart, when the corresponding Endpoints resource was manually deleted and recreated, causing the endpointslice to fail to be created normally. ([#125359](https://github.com/kubernetes/kubernetes/pull/125359), [@yangjunmyfm192085](https://github.com/yangjunmyfm192085)) [SIG Apps and Network]
- Kube-apiserver: fixed a 1.27+ regression watching a single namespace via the deprecated /api/v1/watch/namespaces/$name endpoint where watch events were not delivered after the watch was established. ([#125145](https://github.com/kubernetes/kubernetes/pull/125145), [@xyz-li](https://github.com/xyz-li)) [SIG API Machinery, Node and Testing]
- Kube-apiserver: fixed a 1.28 regression printing pods with invalid initContainer status. ([#124906](https://github.com/kubernetes/kubernetes/pull/124906), [@liggitt](https://github.com/liggitt))
- Kube-apiserver: fixed a potential crash serving CustomResourceDefinitions that combine an invalid schema and CEL validation rules. ([#126167](https://github.com/kubernetes/kubernetes/pull/126167), [@cici37](https://github.com/cici37)) [SIG API Machinery and Testing]
- Kubeadm: Fixed a bug where the PublicKeysECDSA feature gate was not respected when generating kubeconfig files. ([#125388](https://github.com/kubernetes/kubernetes/pull/125388), [@neolit123](https://github.com/neolit123))
- Kubeadm: Fixed a regression where the JoinConfiguration.discovery.timeout was no longer respected and the value was always hardcoded to "5m" (5 minutes). ([#125480](https://github.com/kubernetes/kubernetes/pull/125480), [@neolit123](https://github.com/neolit123))
- Kubeadm: fixed a bug on 'kubeadm join' where using patches with a kubeletconfiguration target was not respected when performing the local kubelet healthz check. ([#126224](https://github.com/kubernetes/kubernetes/pull/126224), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]
- Kubeadm: fixed a bug where the path of the manifest can not be specified when `kubeadm upgrade diff` specified a config file, and the `--api-server-manifest`, `--controller-manager-manifest` and `--scheduler-manifest` flags of `kubeadm upgrade diff` are marked as deprecated and will be removed in a future release. ([#125779](https://github.com/kubernetes/kubernetes/pull/125779), [@SataQiu](https://github.com/SataQiu))
- `Job`: Fixed a bug where `SuccessCriteriaMet` could be added to the Job with `successPolicy` regardless of the `featureGate` being enabled. ([#125429](https://github.com/kubernetes/kubernetes/pull/125429), [@tenzen-y](https://github.com/tenzen-y))
- Dynamic Resource Allocation (DRA): fixed some small, unlikely race condition during pod scheduling. ([#124595](https://github.com/kubernetes/kubernetes/pull/124595), [@pohly](https://github.com/pohly)) [SIG Node, Scheduling and Testing]
- Fixed a typo in the help text for the pod_scheduling_sli_duration_seconds metric in kube-scheduler. ([#124221](https://github.com/kubernetes/kubernetes/pull/124221), [@arturhoo](https://github.com/arturhoo)) [SIG Instrumentation, Scheduling and Testing]

### 1.31.1

- Fix a scheduler preemption issue where the victim pod was not deleted due to incorrect status patching. This issue occurred when the preemptor and victim pods had different QoS classes in their status, causing the preemption to fail entirely. ([#126691](https://github.com/kubernetes/kubernetes/pull/126691), [@Huang-Wei](https://github.com/Huang-Wei)) [SIG Scheduling]
- Fix race condition in kube-proxy initialization that could blackhole UDP traffic to service VIP. ([#126687](https://github.com/kubernetes/kubernetes/pull/126687), [@wedaly](https://github.com/wedaly)) [SIG Network]
- Fixed a bug where init containers may fail to start due to a temporary container runtime failure. ([#127212](https://github.com/kubernetes/kubernetes/pull/127212), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG Node]
- Fixed a regression in 1.29+ default configurations, where regular init containers may fail to start due to a temporary container runtime failure. ([#127202](https://github.com/kubernetes/kubernetes/pull/127202), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG Node]
- Kube-apiserver: Fixes a 1.31 regression that stopped honoring build ID overrides with the --version flag ([#126670](https://github.com/kubernetes/kubernetes/pull/126670), [@liggitt](https://github.com/liggitt)) [SIG API Machinery]
- Terminated Pods on a node will not be re-admitted on kubelet restart. This fixes the problem of Completed Pods awaiting for the finalizer marked as Failed after the kubelet restart. ([#127207](https://github.com/kubernetes/kubernetes/pull/127207), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG Node and Testing]

### 1.31.2

- Fix a bug on the endpoints controller that does not reconcile the Endpoint object after this is truncated (it gets more than 1000 endpoints addresses) ([#127417](https://github.com/kubernetes/kubernetes/pull/127417), [@aojea](https://github.com/aojea)) [SIG Apps, Network and Testing]
- Fixes a 1.31 regression with API emulation versioning honors cohabitating resources ([#127328](https://github.com/kubernetes/kubernetes/pull/127328), [@xuzhenglun](https://github.com/xuzhenglun)) [SIG API Machinery]
- Fixes a kubelet and kube-apiserver memory leak in default 1.29 configurations related to tracing. ([#126983](https://github.com/kubernetes/kubernetes/pull/126983), [@dashpole](https://github.com/dashpole)) [SIG API Machinery and Node]
- Fixes a regression introduced in 1.29 where conntrack entries for UDP connections to deleted pods did not get cleaned up correctly, which could (among other things) cause DNS problems when DNS pods were restarted. ([#127806](https://github.com/kubernetes/kubernetes/pull/127806), [@danwinship](https://github.com/danwinship)) [SIG Network]
- Kubeadm: fix wrong member list reported when removing an etcd member ([#127960](https://github.com/kubernetes/kubernetes/pull/127960), [@SataQiu](https://github.com/SataQiu)) [SIG Cluster Lifecycle]

### 1.31.3

- Fix a bug when the hostname label of a node does not match the node name, pods bound to a PV with nodeAffinity using the hostname may be scheduled to the wrong node or experience scheduling failures. ([#127584](https://github.com/kubernetes/kubernetes/pull/127584), [@AxeZhan](https://github.com/AxeZhan)) [SIG Scheduling and Storage]
- Fixed a suboptimal scheduler preemption behavior where potential preemption victims were violating Pod Disruption Budgets. ([#128431](https://github.com/kubernetes/kubernetes/pull/128431), [@NoicFank](https://github.com/NoicFank)) [SIG Scheduling]
- Fixes 1.31 regression that can crash kube-controller-manager's service-lb-controller loop ([#128236](https://github.com/kubernetes/kubernetes/pull/128236), [@carlory](https://github.com/carlory)) [SIG API Machinery, Cloud Provider and Network]

### 1.31.4

- Fix bug where PodCIDR was released before node was deleted ([#128806](https://github.com/kubernetes/kubernetes/pull/128806), [@adrianmoisey](https://github.com/adrianmoisey)) [SIG Apps and Network]

### 1.31.5

- Fixed a storage bug around multipath. iSCSI and Fibre Channel devices attached to nodes via multipath now resolve correctly if partitioned. ([#129181](https://github.com/kubernetes/kubernetes/pull/129181), [@RomanBednar](https://github.com/RomanBednar)) [SIG Storage]
- Fixes a panic in kube-controller-manager handling StatefulSet objects when revisionHistoryLimit is negative ([#129323](https://github.com/kubernetes/kubernetes/pull/129323), [@ardaguclu](https://github.com/ardaguclu)) [SIG Apps]
- Kubeadm: fix a bug where the 'node.skipPhases' in UpgradeConfiguration is not respected by 'kubeadm upgrade node' command ([#129454](https://github.com/kubernetes/kubernetes/pull/129454), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]
- Kubelet: Fix the volume manager didn't check the device mount state in the actual state of the world before marking the volume as detached. It may cause a pod to be stuck in the Terminating state due to the above issue when it was deleted. ([#129062](https://github.com/kubernetes/kubernetes/pull/129062), [@carlory](https://github.com/carlory)) [SIG Node]

### 1.31.6

- Fix nil pointer panic in BuildOpenAPIV2 and BuildOpenAPIV3 utilities, used by kube-apiserver's openAPI controller, when a CRD is missing version the requested version. ([#128940](https://github.com/kubernetes/kubernetes/pull/128940), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery]
- Fixed in-tree to CSI migration for Portworx volumes, in clusters where Portworx security feature is enabled (it's a Portworx feature, not Kubernetes feature). It required secret data from the secret mentioned in-tree SC, to be passed in CSI requests which was not happening before this fix. ([#129675](https://github.com/kubernetes/kubernetes/pull/129675), [@gohilankit](https://github.com/gohilankit)) [SIG Storage]
- Kubeadm: fixed a bug where an image is not pulled if there is an error with the sandbox image from CRI. ([#129607](https://github.com/kubernetes/kubernetes/pull/129607), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]
- Kubeadm: fixed the bug where the v1beta4 Timeouts.EtcdAPICall field was not respected in etcd client operations, and the default timeout of 2 minutes was always used. ([#129861](https://github.com/kubernetes/kubernetes/pull/129861), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]

### 1.31.7

- Fixes a 1.30+ regression in connection stability for exec / attach / portforward requests initiated using a websocket client ([#130252](https://github.com/kubernetes/kubernetes/pull/130252), [@fuweid](https://github.com/fuweid)) [SIG API Machinery, CLI and Testing]
- Kubeadm: fix panic when no UpgradeConfiguration was found in the config file ([#130312](https://github.com/kubernetes/kubernetes/pull/130312), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]
- Resolves a performance regression in default 1.31+ configurations, related to the ConsistentListFromCache feature, where rapid create / update API requests across different namespaces encounter increased latency. ([#130156](https://github.com/kubernetes/kubernetes/pull/130156), [@AwesomePatrol](https://github.com/AwesomePatrol)) [SIG API Machinery]

### 1.31.8

- Fix a bug where kube-apiserver could emit an further watch even even if decryption failed for earlier event and it was not emitted. ([#131160](https://github.com/kubernetes/kubernetes/pull/131160), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery and Etcd]
- Fix kubelet restart unmounts volumes of running pods if the referenced PVC is being deleted by the user ([#130685](https://github.com/kubernetes/kubernetes/pull/130685), [@carlory](https://github.com/carlory)) [SIG Node, Storage and Testing]

### 1.31.9

- Resolve a regression introduced in version 1.31 on Windows Proxy, where the creation of HNS endpoints fails if remote HNS endpoints with the same IP address have already been created. ([#131429](https://github.com/kubernetes/kubernetes/pull/131429), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]

### 1.31.11

- Fix a bug causing unexpected delay of creating pods for newly created jobs ([#132109](https://github.com/kubernetes/kubernetes/pull/132109), [@linxiulei](https://github.com/linxiulei)) [SIG Apps and Testing]
- Kubeadm: fixed issue where etcd member promotion fails with an error saying the member was already promoted ([#132282](https://github.com/kubernetes/kubernetes/pull/132282), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]

### 1.31.13

- Kubeadm: fixed bug where v1beta3's ClusterConfiguration.APIServer.TimeoutForControlPlane is not respected in newer versions of kubeadm where v1beta4 is the default. ([#133776](https://github.com/kubernetes/kubernetes/pull/133776), [@HirazawaUi](https://github.com/HirazawaUi)) [SIG Cluster Lifecycle]

### 1.31.14

- Fix Windows kube-proxy to prevent intermittent deletion of ClusterIP load balancers in HNS when internalTrafficPolicy=Local, ensuring stable service connectivity. ([#134034](https://github.com/kubernetes/kubernetes/pull/134034), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]
- Kubeadm: fixes a preflight check that can fail hostname construction in IPV6 setups ([#134592](https://github.com/kubernetes/kubernetes/pull/134592), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Auth, Cloud Provider, Cluster Lifecycle and Testing]


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.31.14**, the newest release recorded here for this line.

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
