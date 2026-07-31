---
id: TROUBLE-KUBERNETES_1_32_DEFECTS
type: troubleshooting
title: "kubernetes 1.32: defects fixed in the 1.32 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.32.0 <1.33.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubernetes 1.32 known issues
  - kubernetes 1.32 fixed in
  - is this kubernetes bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubernetes
sources:
  - type: docs
    path: kubernetes/kubernetes release notes for the 1.32 line — bug-fix entries
    url: https://github.com/kubernetes/kubernetes/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubernetes 1.32: defects fixed in the 1.32 line

## Summary

**86 defects** the project fixed across **11 releases** of the 1.32 line, from 1.32.0 to
1.32.11. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.32.0

- Fixed a bug in the `NestedNumberAsFloat64` Unstructured field accessor that could have caused it to return rounded float64 values instead of errors when accessing very large int64 values. ([#128099](https://github.com/kubernetes/kubernetes/pull/128099), [@benluddy](https://github.com/benluddy))
- Fixed the bug where `spec.terminationGracePeriodSeconds` of the pod will always be overwritten by the MaxPodGracePeriodSeconds of the soft eviction, you can enable the `AllowOverwriteTerminationGracePeriodSeconds` feature gate, which will restore the previous behavior. If you do need to set this, please file an issue with the Kubernetes project to help contributors understand why you needed it. ([#122890](https://github.com/kubernetes/kubernetes/pull/122890), [@HirazawaUi](https://github.com/HirazawaUi)) [SIG API Machinery, Architecture, Node and Testing]
- Fixed: Avoid overwriting in-pod vertical scaling updates on systemd daemon reloads when using systemd ([#124216](https://github.com/kubernetes/kubernetes/pull/124216), [@iholder101](https://github.com/iholder101)) [SIG Node]
- Fixed an issue where kubectl doesn't print image volume when kubectl describe a pod with that volume. ([#126706](https://github.com/kubernetes/kubernetes/pull/126706), [@carlory](https://github.com/carlory))
- Fixed documentation for the `apiserver_admission_webhook_fail_open_count` and `apiserver_admission_webhook_request_total` metrics. The `type` label can have a value of "admit", not "mutating". ([#127898](https://github.com/kubernetes/kubernetes/pull/127898), [@modulitos](https://github.com/modulitos))
- kubeadm: fixed a misleading output (typo) about control-plane joining instructions when executing the "kubeadm init" command. ([#128118](https://github.com/kubernetes/kubernetes/pull/128118), [@amaddio](https://github.com/amaddio))
- 1. When the kubelet constructs the CRI mounts for the container which references an `image` volume source type, it passes the missing mount attributes to the CRI implementation, including `readOnly`, `propagation`, and `recursiveReadOnly`. When the readOnly field of the containerMount is explicitly set to false, the kubelet will now take the `readOnly`as true to the CRI implementation because the image volume plugin requires the mount to be read-only. 2. Fixed a bug where the pod is unexpectedly running when the `image` volume source type is used and mounted to `/etc/hosts` in the container. ([#126806](https://github.com/kubernetes/kubernetes/pull/126806), [@carlory](https://github.com/carlory)) [SIG Node and Storage]
- DRA: fixed several issues related to `allocationMode: all`. ([#127565](https://github.com/kubernetes/kubernetes/pull/127565), [@pohly](https://github.com/pohly))
- Fixed 1.31 regression that can crash kube-controller-manager's service-lb-controller loop. ([#128182](https://github.com/kubernetes/kubernetes/pull/128182), [@carlory](https://github.com/carlory)) [SIG API Machinery, Cloud Provider and Network]
- Fixed a 1.31 regression starting kubelet on Windows: Revert "fix: handle socket file detection on Windows". ([#126976](https://github.com/kubernetes/kubernetes/pull/126976), [@jsturtevant](https://github.com/jsturtevant))
- Fixed a 1.31 regression with API emulation versioning honors cohabitating resources. ([#127239](https://github.com/kubernetes/kubernetes/pull/127239), [@xuzhenglun](https://github.com/xuzhenglun))
- Fixed a bug in the endpoints controller that failed to reconcile the Endpoint object after it was truncated (when it received more than 1000 endpoint addresses). ([#127417](https://github.com/kubernetes/kubernetes/pull/127417), [@aojea](https://github.com/aojea)) [SIG Apps, Network and Testing]
- Fixed a bug in the garbage collector controller which could block indefinitely due to a cache sync failure. This fix allows the garbage collector to eventually continue garbage collecting other resources if a given resource cannot be listed or watched. Any objects in the unsynced resource type with owner references with `blockOwnerDeletion: true` will not be known to the garbage collector. Use of `blockOwnerDeletion` has always been best-effort and racy on startup and object creation. With this fix, it continues to be best-effort for resources that cannot be synced by the garbage collector controller. ([#125796](https://github.com/kubernetes/kubernetes/pull/125796), [@haorenfsa](https://github.com/haorenfsa)) [SIG API Machinery, Apps and Testing]
- Fixed a bug that occurred when the hostname label of a node did not match the node name, pods bound to a PersistentVolume with `nodeAffinity` using the hostname may be scheduled to the wrong node or experience scheduling failures. ([#125398](https://github.com/kubernetes/kubernetes/pull/125398), [@AxeZhan](https://github.com/AxeZhan)) [SIG Scheduling and Storage]
- Fixed a bug where `podCIDR` was released before node was deleted. ([#128305](https://github.com/kubernetes/kubernetes/pull/128305), [@adrianmoisey](https://github.com/adrianmoisey)) [SIG Apps and Network]
- Fixed a bug where the kubelet ephemerally failed with `failed to initialize top level QOS containers: root container [kubepods] doesn't exist`, due to the cpuset cgroup being deleted on cgroup v2 with systemd cgroup manager. ([#125923](https://github.com/kubernetes/kubernetes/pull/125923), [@haircommander](https://github.com/haircommander)) [SIG Node and Testing]
- Fixed a bug where the pod(with regular init containers)'s phase was not pending when the regular init container had not finished running after a node restart. ([#126653](https://github.com/kubernetes/kubernetes/pull/126653), [@zhifei92](https://github.com/zhifei92)) [SIG Node and Testing]
- Fixed a bug which the scheduler didn't correctly tell plugins Node deletion. This bug could impact all scheduler plugins subscribing to Node/Delete event, making the queue keep the Pods rejected by those plugins incorrectly at Node deletion. Among the in-tree plugins, PodTopologySpread is the only victim. ([#127464](https://github.com/kubernetes/kubernetes/pull/127464), [@sanposhiho](https://github.com/sanposhiho)) [SIG Scheduling and Testing]
- Fixed a bug with dual stack clusters using the beta feature MultiCIDRServiceAllocator which could not create dual stack Services or Services with IPs in the secondary range. Users who wanted to use this feature in version 1.30 with dual stack clusters could work around the issue by setting the feature gate DisableAllocatorDualWrite to true. ([#127598](https://github.com/kubernetes/kubernetes/pull/127598), [@aojea](https://github.com/aojea)) [SIG Network and Testing]
- Fixed a possible memory leak in the QueueingHint (alpha feature). ([#126962](https://github.com/kubernetes/kubernetes/pull/126962), [@sanposhiho](https://github.com/sanposhiho))
- Fixed a potential memory leak in QueueingHint (alpha feature). ([#127016](https://github.com/kubernetes/kubernetes/pull/127016), [@sanposhiho](https://github.com/sanposhiho))
- Fixed a race condition in the kube-proxy initialization that could cause UDP traffic to service VIP. ([#126532](https://github.com/kubernetes/kubernetes/pull/126532), [@wedaly](https://github.com/wedaly))
- Fixed a race condition that could result in erroneous volume unmounts for flex volume plugins during kubelet restart. ([#127669](https://github.com/kubernetes/kubernetes/pull/127669), [@olyazavr](https://github.com/olyazavr))
- Fixed a regression in 1.29+ default configurations, where regular init containers may fail to start due to a temporary container runtime failure. ([#127162](https://github.com/kubernetes/kubernetes/pull/127162), [@gjkim42](https://github.com/gjkim42)) [SIG Node]
- Fixed a regression in default 1.29 configurations with the `SidecarContainers` feature enabled, where init containers may fail to start due to a temporary container runtime failure. ([#126543](https://github.com/kubernetes/kubernetes/pull/126543), [@gjkim42](https://github.com/gjkim42))
- Fixed a regression introduced in v1.29 where conntrack entries for UDP connections to deleted pods did not get cleaned up correctly, which could (among other things) cause DNS problems when DNS pods were restarted. ([#127780](https://github.com/kubernetes/kubernetes/pull/127780), [@danwinship](https://github.com/danwinship))
- Fixed a scheduler preemption issue where the victim pod was not deleted due to incorrect status patching. This issue occurred when the preemptor and victim pods had different QoS classes in their status, causing the preemption to fail entirely. ([#126644](https://github.com/kubernetes/kubernetes/pull/126644), [@Huang-Wei](https://github.com/Huang-Wei))
- Fixed a suboptimal scheduler preemption behavior where potential preemption victims were violating Pod Disruption Budgets. ([#128307](https://github.com/kubernetes/kubernetes/pull/128307), [@NoicFank](https://github.com/NoicFank)) [SIG Scheduling]
- Fixed an issue in the kubelet that showed when writeable layers and read-only layers were at different paths within the same mount. Kubernetes was previously detecting that the image filesystem was split, even when that was not really the case ([#128344](https://github.com/kubernetes/kubernetes/pull/128344), [@kannon92](https://github.com/kannon92)) [SIG Node]
- Fixed an issue where eviction manager was not deleting unused images or containers. ([#127874](https://github.com/kubernetes/kubernetes/pull/127874), [@AnishShah](https://github.com/AnishShah))
- Fixed an issue where requests sent by the KMSv2 service would be rejected due to having an invalid authority header. ([#126930](https://github.com/kubernetes/kubernetes/pull/126930), [@Ruddickmg](https://github.com/Ruddickmg)) [SIG API Machinery and Auth]
- Fixed data race in kubelet/volumemanager. ([#127919](https://github.com/kubernetes/kubernetes/pull/127919), [@carlory](https://github.com/carlory)) [SIG Apps, Node and Storage]
- Fixed fake client to accept request without metadata.name to better emulate behavior of actual client. ([#126727](https://github.com/kubernetes/kubernetes/pull/126727), [@jpbetz](https://github.com/jpbetz))
- Fixed the ability to set the `resolvConf` option in drop-in kubelet configuration files, which validates that drop-in kubelet configuration files are in a supported version. ([#127421](https://github.com/kubernetes/kubernetes/pull/127421), [@liggitt](https://github.com/liggitt))
- Fixed the bug in `NodeUnschedulable` that only happens with QHint enabled, which the scheduler might miss some updates for the Pods rejected by NodeUnschedulable plugin and put the Pods in the queue for a longer time than needed. ([#127427](https://github.com/kubernetes/kubernetes/pull/127427), [@sanposhiho](https://github.com/sanposhiho))
- Fixed the estimated cost in CEL for expressions that perform equality checks on IPs, CIDRs, Quantities, Formats and URLs. ([#126359](https://github.com/kubernetes/kubernetes/pull/126359), [@jpbetz](https://github.com/jpbetz))
- Fixed the incorrect help message of a metric "graceful_shutdown_end_time_seconds". Fixed incorrect value set for metrics "graceful_shutdown_start_time_seconds" and "graceful_shutdown_end_time_seconds" in certain cases during graceful node shutdown. ([#128189](https://github.com/kubernetes/kubernetes/pull/128189), [@zylxjtu](https://github.com/zylxjtu)) [SIG Node]
- Fixed the reporting of elapsed times during evaluation of `ValidatingAdmissionPolicy` decisions and annotations. The apiserver_validating_admission_policy_check_duration metrics will now show elapsed times and no longer be zero. ([#128463](https://github.com/kubernetes/kubernetes/pull/128463), [@knrc](https://github.com/knrc))
- Fixed the wrong hierarchical structure for both the child span and the parent span (i.e. `SerializeObject` and `List`). In the past, some children's spans appeared parallel to their parents. ([#127551](https://github.com/kubernetes/kubernetes/pull/127551), [@carlory](https://github.com/carlory)) [SIG API Machinery and Instrumentation]
- Fixed: dynamic client-go can now handle subresources with an UnstructuredList response ([#126809](https://github.com/kubernetes/kubernetes/pull/126809), [@ryantxu](https://github.com/ryantxu)) [SIG API Machinery]
- Fixed a bug where restartable and non-restartable init containers were not accounted for in the message and annotations of eviction event. ([#124947](https://github.com/kubernetes/kubernetes/pull/124947), [@toVersus](https://github.com/toVersus)) [SIG Node]
- Fixed a kubelet and kube-apiserver memory leak in default 1.29 configurations related to tracing. ([#126957](https://github.com/kubernetes/kubernetes/pull/126957), [@dashpole](https://github.com/dashpole)) [SIG API Machinery, Architecture, Instrumentation and Node]
- Fixed the bug in PodTopologySpread that only happens with QHint enabled, which the scheduler might miss some updates for the Pods rejected by PodTopologySpread plugin and put the Pods in the queue for a longer time than needed. ([#127447](https://github.com/kubernetes/kubernetes/pull/127447), [@sanposhiho](https://github.com/sanposhiho)) [SIG Scheduling]
- kube-apiserver: fixed a 1.31 regression that stopped honoring build ID overrides with the --version flag ([#126665](https://github.com/kubernetes/kubernetes/pull/126665), [@liggitt](https://github.com/liggitt)) [SIG API Machinery]
- kubeadm: fixed an issue where the wrong member list was being reported when removing an etcd member. ([#127650](https://github.com/kubernetes/kubernetes/pull/127650), [@SataQiu](https://github.com/SataQiu))
- kubelet: Fix - the volume manager didn't check the device mount state in the actual state of the world before marking the volume as detached. It may cause a pod to be stuck in the Terminating state due to the above issue when it was deleted. ([#128219](https://github.com/kubernetes/kubernetes/pull/128219), [@carlory](https://github.com/carlory))
- kubelet: Fixed a bug where kubelet wrongly drops the QOSClass field of the Pod's status when it rejects a Pod. ([#128083](https://github.com/kubernetes/kubernetes/pull/128083), [@carlory](https://github.com/carlory)) [SIG Node and Testing]
- Terminated Pods on a node will not be re-admitted on kubelet restart. This fixes the problem of Completed Pods awaiting for the finalizer marked as Failed after the kubelet restart. ([#126343](https://github.com/kubernetes/kubernetes/pull/126343), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG Node and Testing]
- Fixed problem with named ports not being available when specified in sidecar containers. ([#127976](https://github.com/kubernetes/kubernetes/pull/127976), [@chengjoey](https://github.com/chengjoey))
- Fixed a warning message about the gce in-tree cloud provider state. ([#126773](https://github.com/kubernetes/kubernetes/pull/126773), [@carlory](https://github.com/carlory))
- Fixed spacing in `--validate flag` description in kubectl. ([#128081](https://github.com/kubernetes/kubernetes/pull/128081), [@soltysh](https://github.com/soltysh))
- Fixes a bug in the `k8s.io/cloud-provider/service` controller, it may panic when a service is updated because the event recorder was used before it was initialized. All cloud providers should using the `v1.31.0` cloud provider service controller must ensure that the controllers is initialized before the informer start to process events or update it to the version 1.32.0. ([#128179](https://github.com/kubernetes/kubernetes/pull/128179), [@carlory](https://github.com/carlory)) [SIG API Machinery, Cloud Provider, Network and Testing]
- kubelet: fixed an issue mounting CSI volumes on Windows nodes in 1.32.0 release candidates. ([#129083](https://github.com/kubernetes/kubernetes/pull/129083) [liggitt](https://github.com/liggitt)) [SIG API Machinery, architecture, auth, cli, cloud-provider, cluster-lifecycle, instrumentation,network,node, release, storage, windows ]

### 1.32.1

- Fixed a storage bug around multipath. iSCSI and Fibre Channel devices attached to nodes via multipath now resolve correctly if partitioned. ([#129180](https://github.com/kubernetes/kubernetes/pull/129180), [@RomanBednar](https://github.com/RomanBednar)) [SIG Storage]
- Fixes a panic in kube-controller-manager handling StatefulSet objects when revisionHistoryLimit is negative ([#129322](https://github.com/kubernetes/kubernetes/pull/129322), [@ardaguclu](https://github.com/ardaguclu)) [SIG Apps]
- Kubeadm: fix a bug where the 'node.skipPhases' in UpgradeConfiguration is not respected by 'kubeadm upgrade node' command ([#129455](https://github.com/kubernetes/kubernetes/pull/129455), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]

### 1.32.2

- Fixed in-tree to CSI migration for Portworx volumes, in clusters where Portworx security feature is enabled (it's a Portworx feature, not Kubernetes feature). It required secret data from the secret mentioned in-tree SC, to be passed in CSI requests which was not happening before this fix. ([#129674](https://github.com/kubernetes/kubernetes/pull/129674), [@gohilankit](https://github.com/gohilankit)) [SIG Storage]
- Fixes a 1.32 regression in with the ServiceAccountNodeAudienceRestriction feature where `azureFile` volumes encounter "failed to get service accoount token attributes" errors. Reverts the `ServiceAccountNodeAudienceRestriction` feature to disabled in v1.32. Refer to https://github.com/kubernetes/kubernetes/issues/129935 for more details. If you're using in-tree inline volumes or in-tree persistent volumes whose CSI drivers depend on service account tokens, do not enable this feature in the 1.32 release. ([#130015](https://github.com/kubernetes/kubernetes/pull/130015), [@aramase](https://github.com/aramase)) [SIG Auth]
- Kubeadm: fixed a bug where an image is not pulled if there is an error with the sandbox image from CRI. ([#129608](https://github.com/kubernetes/kubernetes/pull/129608), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]
- Kubeadm: fixed the bug where the v1beta4 Timeouts.EtcdAPICall field was not respected in etcd client operations, and the default timeout of 2 minutes was always used. ([#129862](https://github.com/kubernetes/kubernetes/pull/129862), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]

### 1.32.3

- Fixed an issue in register-gen where imports for k8s.io/apimachinery/pkg/runtime and k8s.io/apimachinery/pkg/runtime/schema were missing. ([#130392](https://github.com/kubernetes/kubernetes/pull/130392), [@mrIncompetent](https://github.com/mrIncompetent)) [SIG API Machinery]
- Fixes a 1.30+ regression in connection stability for exec / attach / portforward requests initiated using a websocket client ([#130253](https://github.com/kubernetes/kubernetes/pull/130253), [@fuweid](https://github.com/fuweid)) [SIG API Machinery, CLI and Testing]
- Fixes a 1.32 regression starting pods with postStart hooks specified ([#130496](https://github.com/kubernetes/kubernetes/pull/130496), [@sreeram-venkitesh](https://github.com/sreeram-venkitesh)) [SIG Node]
- Fixes a 1.32 regression where nodes may fail to report status and renew serving certificates after the kubelet restarts ([#130356](https://github.com/kubernetes/kubernetes/pull/130356), [@aojea](https://github.com/aojea)) [SIG Node]
- Kube-apiserver: fixes a 1.32+ regression validating OIDC and anonymous authentication flags are mutually exclusive to authentication configuration. Fixes an issue where the kube-apiserver `/flagz` endpoint would not respond correctly with parsed flags value. ([#130332](https://github.com/kubernetes/kubernetes/pull/130332), [@richabanker](https://github.com/richabanker)) [SIG API Machinery and Testing]
- Kube-proxy: fixes a 1.32 regression with a potential memory leak which can occur in clusters with high volume of UDP workflows ([#130034](https://github.com/kubernetes/kubernetes/pull/130034), [@aroradaman](https://github.com/aroradaman)) [SIG Network]
- Kubeadm: fix panic when no UpgradeConfiguration was found in the config file ([#130313](https://github.com/kubernetes/kubernetes/pull/130313), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]
- Resolves a performance regression in default 1.31+ configurations, related to the ConsistentListFromCache feature, where rapid create / update API requests across different namespaces encounter increased latency. ([#130136](https://github.com/kubernetes/kubernetes/pull/130136), [@AwesomePatrol](https://github.com/AwesomePatrol)) [SIG API Machinery]

### 1.32.4

- Fix a bug where kube-apiserver could emit an further watch even even if decryption failed for earlier event and it was not emitted. ([#131159](https://github.com/kubernetes/kubernetes/pull/131159), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery and Etcd]
- Fix kubelet restart unmounts volumes of running pods if the referenced PVC is being deleted by the user ([#130684](https://github.com/kubernetes/kubernetes/pull/130684), [@carlory](https://github.com/carlory)) [SIG Node, Storage and Testing]
- Fixes an issue in the CEL CIDR library where subnets contained within another CIDR were incorrectly rejected as not contained ([#130773](https://github.com/kubernetes/kubernetes/pull/130773), [@JoelSpeed](https://github.com/JoelSpeed)) [SIG API Machinery]

### 1.32.5

- Kubelet: fix a bug where the unexpected NodeResizeError condition was in PVC status when the csi driver does not support node volume expansion and the pvc has the ReadWriteMany access mode. ([#131524](https://github.com/kubernetes/kubernetes/pull/131524), [@carlory](https://github.com/carlory)) [SIG Storage]
- Resolve a regression introduced in version 1.31 on Windows Proxy, where the creation of HNS endpoints fails if remote HNS endpoints with the same IP address have already been created. ([#131428](https://github.com/kubernetes/kubernetes/pull/131428), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]

### 1.32.6

- Fixes an issue where Windows kube-proxy's ModifyLoadBalancer API updates did not match HNS state in version 15.4. ModifyLoadBalancer policy is supported from Kubernetes 1.31+. ([#131652](https://github.com/kubernetes/kubernetes/pull/131652), [@princepereira](https://github.com/princepereira)) [SIG Windows]

### 1.32.7

- Fix a bug causing unexpected delay of creating pods for newly created jobs ([#132159](https://github.com/kubernetes/kubernetes/pull/132159), [@linxiulei](https://github.com/linxiulei)) [SIG Apps and Testing]
- Fix validation for Job with suspend=true, and completions=0 to set the Complete condition. ([#132727](https://github.com/kubernetes/kubernetes/pull/132727), [@mimowo](https://github.com/mimowo)) [SIG Apps and Testing]
- Kubeadm: fixed issue where etcd member promotion fails with an error saying the member was already promoted ([#132281](https://github.com/kubernetes/kubernetes/pull/132281), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]

### 1.32.9

- Kubeadm: fixed bug where v1beta3's ClusterConfiguration.APIServer.TimeoutForControlPlane is not respected in newer versions of kubeadm where v1beta4 is the default. ([#133755](https://github.com/kubernetes/kubernetes/pull/133755), [@HirazawaUi](https://github.com/HirazawaUi)) [SIG Cluster Lifecycle]

### 1.32.10

- Fix Windows kube-proxy (winkernel) issue where stale RemoteEndpoints remained when a Deployment was referenced by multiple Services due to premature clearing of the terminatedEndpoints map. ([#135172](https://github.com/kubernetes/kubernetes/pull/135172), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]
- Fix Windows kube-proxy to prevent intermittent deletion of ClusterIP load balancers in HNS when internalTrafficPolicy=Local, ensuring stable service connectivity. ([#134033](https://github.com/kubernetes/kubernetes/pull/134033), [@princepereira](https://github.com/princepereira)) [SIG Network and Windows]
- Fix the bug which could result in Job status updates failing with the error: status.startTime: Required value: startTime cannot be removed for unsuspended job The error could be raised after a Job is resumed, if started and suspended previously. ([#135128](https://github.com/kubernetes/kubernetes/pull/135128), [@dejanzele](https://github.com/dejanzele)) [SIG Apps and Testing]
- Fix: The requests for a config FromClass in the status of a ResourceClaim were not referenced. ([#135109](https://github.com/kubernetes/kubernetes/pull/135109), [@LionelJouin](https://github.com/LionelJouin)) [SIG Node]
- Kubeadm: fixed a bug where the node registration information for a given node was not fetched correctly during "kubeadm upgrade node" and the node name can end up being incorrect in cases where the node name is not the same as the host name. ([#134364](https://github.com/kubernetes/kubernetes/pull/134364), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]
- Kubeadm: fixes a preflight check that can fail hostname construction in IPV6 setups ([#134591](https://github.com/kubernetes/kubernetes/pull/134591), [@liggitt](https://github.com/liggitt)) [SIG API Machinery, Auth, Cloud Provider, Cluster Lifecycle and Testing]

### 1.32.11

- Fixes a spurious "namespace not found" error possible in default configurations in 1.30+ when using ValidatingAdmissionPolicy or MutatingAdmissionPolicy to intercept namespaced objects in newly-created namespaces ([#135444](https://github.com/kubernetes/kubernetes/pull/135444), [@lalitc375](https://github.com/lalitc375)) [SIG API Machinery]
- Make / build: fix docker IP address detection ([#135578](https://github.com/kubernetes/kubernetes/pull/135578), [@BenTheElder](https://github.com/BenTheElder)) [SIG Release and Testing]


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.32.11**, the newest release recorded here for this line.

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
