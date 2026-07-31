---
id: TROUBLE-KUBERNETES_1_30_DEFECTS
type: troubleshooting
title: "kubernetes 1.30: defects fixed in the 1.30 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.30.0 <1.31.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubernetes 1.30 known issues
  - kubernetes 1.30 fixed in
  - is this kubernetes bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubernetes
sources:
  - type: docs
    path: kubernetes/kubernetes release notes for the 1.30 line — bug-fix entries
    url: https://github.com/kubernetes/kubernetes/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubernetes 1.30: defects fixed in the 1.30 line

## Summary

**83 defects** the project fixed across **12 releases** of the 1.30 line, from 1.30.0 to
1.30.12. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.30.0

- Allowed container runtimes to fix an image garbage collection bug by adding an `image_id` field to the CRI Container message. ([#123508](https://github.com/kubernetes/kubernetes/pull/123508), [@saschagrunert](https://github.com/saschagrunert))
- Fixed accidental enablement of the new alpha `optionalOldSelf` API field in `CustomResourceDefinition` validation rules, which should only have been allowed to be set when the `CRDValidationRatcheting` feature gate is enabled. ([#122329](https://github.com/kubernetes/kubernetes/pull/122329), [@jpbetz](https://github.com/jpbetz))
- Fixed CEL estimated cost for expressions that perform operations on the result of `map()` operations (e.g., `.map(...).exists(...)` ) to have the correct estimated cost instead of an unbounded cost. ([#123562](https://github.com/kubernetes/kubernetes/pull/123562), [@jpbetz](https://github.com/jpbetz))
- Fixed a `1.27.0+` regression in kubeadm: The kubelet patch configuration will not be uploaded into the `kube-system/kubelet-config` ConfigMap anymore. ([#123093](https://github.com/kubernetes/kubernetes/pull/123093), [@SataQiu](https://github.com/SataQiu))
- Fixed a bug in `ValidatingAdmissionPolicy` that caused policies using CRD parameters to fail to synchronize. ([#123003](https://github.com/kubernetes/kubernetes/pull/123003), [@alexzielenski](https://github.com/alexzielenski))
- Fixed a non-recursive list returning "resource version too high" error when consistent listing from cache is enabled. ([#123674](https://github.com/kubernetes/kubernetes/pull/123674), [@serathius](https://github.com/serathius))
- Fixed a regression in `kube-proxy` introduced in version `1.26.0+` to make externalIPs workwith externalTrafficPolicy: Local. ([#121919](https://github.com/kubernetes/kubernetes/pull/121919), [@uablrek](https://github.com/uablrek))
- Fixed a regression in migration of in-tree vSphere volumes to the CSI driver introduced in version `1.29.0`+. ([#122341](https://github.com/kubernetes/kubernetes/pull/122341), [@jsafrane](https://github.com/jsafrane))
- Fixed a regression since `1.24` in the scheduling framework when overriding MultiPoint plugins (e.g. default plugins). The incorrect loop logic might have led to a plugin being loaded multiple times, consequently preventing any Pod from being scheduled, which was unexpected. ([#122068](https://github.com/kubernetes/kubernetes/pull/122068), [@caohe](https://github.com/caohe))
- Fixed an issue where `AvailableBytes` sometimes did not report correctly on WindowsNodes when the `PodAndContainerStatsFromCRI` feature was enabled. ([#122846](https://github.com/kubernetes/kubernetes/pull/122846), [@marosset](https://github.com/marosset))
- Fixed an issue where mount points could become local without calling `NodePublishVolume` after node rebooting. ([#119923](https://github.com/kubernetes/kubernetes/pull/119923), [@cvvz](https://github.com/cvvz))
- Fixed cleanup of Pod volume mounts when a file was used as a subpath. ([#123052](https://github.com/kubernetes/kubernetes/pull/123052), [@jsafrane](https://github.com/jsafrane))
- Fixed error handling in `EnsureAdminClusterRoleBindingImpl`. ([#122893](https://github.com/kubernetes/kubernetes/pull/122893), [@danwinship](https://github.com/danwinship))
- Fixed incorrect error logging for `syncCronJob`. ([#122493](https://github.com/kubernetes/kubernetes/pull/122493), [@mengjiao-liu](https://github.com/mengjiao-liu))
- Fixed the deprecated version for `pod_scheduling_duration_seconds` that caused the metric to be hidden by default in `1.29`. ([#123038](https://github.com/kubernetes/kubernetes/pull/123038), [@alculquicondor](https://github.com/alculquicondor))
- Fixed the disruption controller's PDB status synchronization to maintain all PDB conditions during an update. ([#122056](https://github.com/kubernetes/kubernetes/pull/122056), [@dhenkel92](https://github.com/dhenkel92))
- kube-proxy: Fixed `LoadBalancerSourceRanges` not working for `nftables` mode. ([#122614](https://github.com/kubernetes/kubernetes/pull/122614), [@tnqn](https://github.com/tnqn))
- kubeadm: fixed a bug where "kubeadm upgrade plan -o yaml|json" included unneeded output and was missing component config information. ([#123492](https://github.com/kubernetes/kubernetes/pull/123492), [@carlory](https://github.com/carlory))
- Fixed Pod stuck in `Terminating` because of `GenerateUnmapVolumeFunc` missing `globalUnmapPath` when kubelet tries to clean up all volumes that failed reconstruction. ([#123032](https://github.com/kubernetes/kubernetes/pull/123032), [@carlory](https://github.com/carlory))
- Fixed Windows credential provider, cannot find binary. Windows credential provider binary path may have ".exe" suffix so it is better to use `LookPath()` to support it flexibly. ([#120291](https://github.com/kubernetes/kubernetes/pull/120291), [@lzhecheng](https://github.com/lzhecheng))
- Fixed `kubectl explain` to show enum for field types if they were defined. ([#123023](https://github.com/kubernetes/kubernetes/pull/123023), [@ah8ad3](https://github.com/ah8ad3))
- Fixed a bug in kubeadm where the `--rootfs` global flag didn't work with "kubeadm upgrade node" for control plane nodes. ([#123077](https://github.com/kubernetes/kubernetes/pull/123077), [@neolit123](https://github.com/neolit123))
- Fixed a bug that an init container with containerRestartPolicy with `Always` cannot update its state from terminated to non-terminated for the pod with restartPolicy with `Never` or `OnFailure`. ([#123323](https://github.com/kubernetes/kubernetes/pull/123323), [@gjkim42](https://github.com/gjkim42))
- Fixed a bug where `kubectl` drain would consider a pod as having been deleted if an error occurs while calling the API. ([#122574](https://github.com/kubernetes/kubernetes/pull/122574), [@brianpursley](https://github.com/brianpursley))
- Fixed a potential data race in DRA with no known real-world implications. ([#123222](https://github.com/kubernetes/kubernetes/pull/123222), [@pohly](https://github.com/pohly))
- Fixed a race condition in the iptables mode of kube-proxy in `1.27` and later that could result in some updates getting lost (e.g., when a service gets a new endpoint, the rules for the new endpoint might not be added until much later). ([#122204](https://github.com/kubernetes/kubernetes/pull/122204), [@danwinship](https://github.com/danwinship))
- Fixed a regression in "kubeadm init" where a user-specified --kubeconfig file was being ignored. ([#122735](https://github.com/kubernetes/kubernetes/pull/122735), [@avorima](https://github.com/avorima))
- Fixed a regression in kubectl version `1.29.0` where the `--attach` flag was not honored. ([#122447](https://github.com/kubernetes/kubernetes/pull/122447), [@ardaguclu](https://github.com/ardaguclu))
- Fixed an error when trying to expand a volume that does not require node expansion. ([#123055](https://github.com/kubernetes/kubernetes/pull/123055), [@gnufied](https://github.com/gnufied))
- Fixed an issue calculating total CPU usage reported for Windows nodes. ([#122999](https://github.com/kubernetes/kubernetes/pull/122999), [@marosset](https://github.com/marosset))
- Fixed an issue to ignore unnecessary node events and improve daemonset controller performance. ([#121669](https://github.com/kubernetes/kubernetes/pull/121669), [@xigang](https://github.com/xigang))
- Fixed an issue where the `configmap`, `secret`, `projected`, and `downwardAPI` volume types didn't create user-visible files after a kubelet restart. This fix ensures data persistence and accessibility after restarts. ([#122807](https://github.com/kubernetes/kubernetes/pull/122807), [@carlory](https://github.com/carlory))
- Fixed bug where health check could pass while APIServices are missing from aggregated discovery. ([#122883](https://github.com/kubernetes/kubernetes/pull/122883), [@Jefftree](https://github.com/Jefftree))
- Fixed bug where providing a FieldPath to a CRD Validation Rule would erroneously affect the reported field path of other unrelated CRD Validation Rules on the same schema. ([#123475](https://github.com/kubernetes/kubernetes/pull/123475), [@alexzielenski](https://github.com/alexzielenski))
- Fixed enabling consistent list from watch cache that used to work for resourceVersion=0 ([#123676](https://github.com/kubernetes/kubernetes/pull/123676), [@serathius](https://github.com/serathius))
- Fixed node lifecycle controller panic when conditionType ready is been patch `nil` by mistake. ([#122874](https://github.com/kubernetes/kubernetes/pull/122874), [@fusida](https://github.com/fusida))
- Fixed panic of Evented `PLEG` during kubelet start-up. ([#122475](https://github.com/kubernetes/kubernetes/pull/122475), [@pacoxu](https://github.com/pacoxu))
- Fixed resource deletion failure caused by quota calculation error when `InPlacePodVerticalScaling` is turned on. ([#122701](https://github.com/kubernetes/kubernetes/pull/122701), [@carlory](https://github.com/carlory))
- Kube-apiserver: Fixed a `1.27`+ regression in watch stability by serving watch requests without a `resourceVersion` from the watch cache by default, as in <`1.27` (disabling the change in PR 115096 by default). This mitigates the impact of an etcd watch bug (https://github.com/etcd-io/etcd/pull/17555). If the 1.27 change in PR 115096 to serve these requests from underlying storage is still desired despite the impact on watch stability, it can be re-enabled with a `WatchFromStorageWithoutResourceVersion` feature gate. ([#123935](https://github.com/kubernetes/kubernetes/pull/123935), [@serathius](https://github.com/serathius))
- Kubeadm: fixed a bug during kubeadm upgrade, where it is not possible to mount a new device and create a symbolic link for /etc/kubernetes (or a sub-directory) so that kubeadm stores its information on the mounted device. ([#123406](https://github.com/kubernetes/kubernetes/pull/123406), [@SataQiu](https://github.com/SataQiu))
- Fixed a bug in scheduler requeueing where registered wildcard cluster event sources didn't work. ([#123117](https://github.com/kubernetes/kubernetes/pull/123117), [@kerthcet](https://github.com/kerthcet))
- Fixed an issue where `kubectl apply` could panic when imported as a library. ([#122346](https://github.com/kubernetes/kubernetes/pull/122346), [@Jefftree](https://github.com/Jefftree))

### 1.30.1

- Fixes a 1.30.0 regression in openapi descriptions of imagePullSecrets and hostAliases fields to mark the fields used as keys in those lists as either defaulted or required. ([#124553](https://github.com/kubernetes/kubernetes/pull/124553), [@pmalek](https://github.com/pmalek)) [SIG API Machinery]
- Expose --applyconfig-openapi-schema flag for client generation and fix applyconfig-gen to not create import cycles ([#124371](https://github.com/kubernetes/kubernetes/pull/124371), [@soltysh](https://github.com/soltysh)) [SIG API Machinery]
- Fix throughput when scheduling daemonset pods to reach 300 pods/s, if the configured qps allows it. ([#124753](https://github.com/kubernetes/kubernetes/pull/124753), [@sanposhiho](https://github.com/sanposhiho)) [SIG Scheduling]
- Fixed PersistentVolumeLabel admission plugin refusing in-tree Azure Disk and vSphere PersistentVolumes. ([#124794](https://github.com/kubernetes/kubernetes/pull/124794), [@jsafrane](https://github.com/jsafrane)) [SIG Cloud Provider and Storage]
- Fixes a 1.29.0 regression that introduced a possible data race that could cause panics in kube-controller-manager and kube-scheduler ([#124517](https://github.com/kubernetes/kubernetes/pull/124517), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery and Scheduling]
- Kubeadm: fix a regression where the KubeletConfiguration is not properly downloaded during "kubeadm upgrade" commands from the kube-system/kubelet-config ConfigMap, resulting in the local '/var/lib/kubelet/config.yaml' file being written as a defaulted config. ([#124497](https://github.com/kubernetes/kubernetes/pull/124497), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]

### 1.30.2

- Kube-apiserver: fixes a 1.28 regression printing pods with invalid initContainer status ([#124908](https://github.com/kubernetes/kubernetes/pull/124908), [@liggitt](https://github.com/liggitt)) [SIG Node]
- Kube-scheduler: fixes a 1.30 regression that can lead to a scheduler crash when processing pods with affinity that doesn't match a real/valid node ([#125039](https://github.com/kubernetes/kubernetes/pull/125039), [@AxeZhan](https://github.com/AxeZhan)) [SIG Scheduling and Testing]

### 1.30.3

- Fix a bug that Pods could stuck in the unschedulable pod pool if they're rejected by PreEnqueue plugins that could change its result by a change in resources apart from Pods
- Fix endpoints status out-of-sync when the pod state changes rapidly ([#125675](https://github.com/kubernetes/kubernetes/pull/125675), [@tnqn](https://github.com/tnqn)) [SIG Apps, Network and Testing]
- Job: Fix a bug that the SuccessCriteriaMet could be added to the Job with successPolicy regardless of the featureGate enabling ([#125455](https://github.com/kubernetes/kubernetes/pull/125455), [@tenzen-y](https://github.com/tenzen-y)) [SIG Apps]

### 1.30.4

- Fixed a bug in the API server where empty collections of ValidatingAdmissionPolicies did not have an `items` field. ([#126146](https://github.com/kubernetes/kubernetes/pull/126146), [@xyz-li](https://github.com/xyz-li)) [SIG API Machinery]
- Fix the bug where PodIP field is temporarily removed for a terminal pod ([#125404](https://github.com/kubernetes/kubernetes/pull/125404), [@mimowo](https://github.com/mimowo)) [SIG Node and Testing]
- Fixed a bug that init containers with `Always` restartPolicy may not terminate gracefully if the pod hasn't initialized yet. ([#126331](https://github.com/kubernetes/kubernetes/pull/126331), [@gjkim42](https://github.com/gjkim42)) [SIG Node and Testing]
- Kube-apiserver: fixes a 1.27+ regression watching a single namespace via the deprecated /api/v1/watch/namespaces/$name endpoint where watch events were not delivered after the watch was established ([#126153](https://github.com/kubernetes/kubernetes/pull/126153), [@xyz-li](https://github.com/xyz-li)) [SIG API Machinery and Testing]
- Kube-apiserver: fixes a potential crash serving CustomResourceDefinitions that combine an invalid schema and CEL validation rules. ([#126167](https://github.com/kubernetes/kubernetes/pull/126167), [@cici37](https://github.com/cici37)) [SIG API Machinery and Testing]
- Kubeadm: fixed a bug on 'kubeadm join' where using patches with a kubeletconfiguration target was not respected when performing the local kubelet healthz check. ([#126251](https://github.com/kubernetes/kubernetes/pull/126251), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]
- Kubeadm: fixed a regression where the JoinConfiguration.discovery.timeout was no longer respected and the value was always hardcoded to "5m" (5 minutes). ([#125481](https://github.com/kubernetes/kubernetes/pull/125481), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]
- Resolve a regression in 1.30 default behavior for kubectl exec, cp, and attach which fail when using an HTTPS proxy. ([#126253](https://github.com/kubernetes/kubernetes/pull/126253), [@seans3](https://github.com/seans3)) [SIG API Machinery and CLI]

### 1.30.5

- Fixes a regression in openapi descriptions of PodIP.IP and HostIP.IP fields to mark the fields used as keys in those lists as required. ([#126666](https://github.com/kubernetes/kubernetes/pull/126666), [@thockin](https://github.com/thockin)) [SIG API Machinery]
- Fix a scheduler preemption issue where the victim pod was not deleted due to incorrect status patching. This issue occurred when the preemptor and victim pods had different QoS classes in their status, causing the preemption to fail entirely. ([#126693](https://github.com/kubernetes/kubernetes/pull/126693), [@Huang-Wei](https://github.com/Huang-Wei)) [SIG Scheduling]
- Fix race condition in kube-proxy initialization that could blackhole UDP traffic to service VIP. ([#126688](https://github.com/kubernetes/kubernetes/pull/126688), [@wedaly](https://github.com/wedaly)) [SIG Network]
- Fixed a bug that doesn't allow to install k8s.io/kube-openapi dependency on execute kube::codegen::gen_openapi. ([#126923](https://github.com/kubernetes/kubernetes/pull/126923), [@kannon92](https://github.com/kannon92)) [SIG API Machinery]
- Fixed a bug where init containers may fail to start due to a temporary container runtime failure. ([#127213](https://github.com/kubernetes/kubernetes/pull/127213), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG Node]
- Fixed a regression in 1.29+ default configurations, where regular init containers may fail to start due to a temporary container runtime failure. ([#127203](https://github.com/kubernetes/kubernetes/pull/127203), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG Node]
- Terminated Pods on a node will not be re-admitted on kubelet restart. This fixes the problem of Completed Pods awaiting for the finalizer marked as Failed after the kubelet restart. ([#127208](https://github.com/kubernetes/kubernetes/pull/127208), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG Node and Testing]

### 1.30.6

- Fix a bug on the endpoints controller that does not reconcile the Endpoint object after this is truncated (it gets more than 1000 endpoints addresses) ([#127417](https://github.com/kubernetes/kubernetes/pull/127417), [@aojea](https://github.com/aojea)) [SIG Apps, Network and Testing]
- Fixes a kubelet and kube-apiserver memory leak in default 1.29 configurations related to tracing. ([#126984](https://github.com/kubernetes/kubernetes/pull/126984), [@dashpole](https://github.com/dashpole)) [SIG API Machinery and Node]
- Fixes a regression introduced in 1.29 where conntrack entries for UDP connections to deleted pods did not get cleaned up correctly, which could (among other things) cause DNS problems when DNS pods were restarted. ([#127807](https://github.com/kubernetes/kubernetes/pull/127807), [@danwinship](https://github.com/danwinship)) [SIG Network]
- Kubeadm: fix wrong member list reported when removing an etcd member ([#127961](https://github.com/kubernetes/kubernetes/pull/127961), [@SataQiu](https://github.com/SataQiu)) [SIG Cluster Lifecycle]

### 1.30.7

- Fix a bug when the hostname label of a node does not match the node name, pods bound to a PV with nodeAffinity using the hostname may be scheduled to the wrong node or experience scheduling failures. ([#127585](https://github.com/kubernetes/kubernetes/pull/127585), [@AxeZhan](https://github.com/AxeZhan)) [SIG Scheduling and Storage]
- Fixed a suboptimal scheduler preemption behavior where potential preemption victims were violating Pod Disruption Budgets. ([#128434](https://github.com/kubernetes/kubernetes/pull/128434), [@NoicFank](https://github.com/NoicFank)) [SIG Scheduling]

### 1.30.9

- Fix kubelet on Windows fails if a pod has SecurityContext with RunAsUser ([#129507](https://github.com/kubernetes/kubernetes/pull/129507), [@carlory](https://github.com/carlory)) [SIG Storage, Testing and Windows]
- Fixed a storage bug around multipath. iSCSI and Fibre Channel devices attached to nodes via multipath now resolve correctly if partitioned. ([#129182](https://github.com/kubernetes/kubernetes/pull/129182), [@RomanBednar](https://github.com/RomanBednar)) [SIG Storage]
- Fixes a panic in kube-controller-manager handling StatefulSet objects when revisionHistoryLimit is negative ([#129324](https://github.com/kubernetes/kubernetes/pull/129324), [@ardaguclu](https://github.com/ardaguclu)) [SIG Apps]
- Kubelet: Fix the volume manager didn't check the device mount state in the actual state of the world before marking the volume as detached. It may cause a pod to be stuck in the Terminating state due to the above issue when it was deleted. ([#129063](https://github.com/kubernetes/kubernetes/pull/129063), [@carlory](https://github.com/carlory)) [SIG Node]

### 1.30.10

- Kubeadm: fixed the bug where the v1beta4 Timeouts.EtcdAPICall field was not respected in etcd client operations, and the default timeout of 2 minutes was always used. ([#129860](https://github.com/kubernetes/kubernetes/pull/129860), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]

### 1.30.11

- Fixes a 1.30+ regression in connection stability for exec / attach / portforward requests initiated using a websocket client ([#130251](https://github.com/kubernetes/kubernetes/pull/130251), [@fuweid](https://github.com/fuweid)) [SIG API Machinery, CLI and Testing]
- Kubeadm: fix panic when no UpgradeConfiguration was found in the config file ([#130314](https://github.com/kubernetes/kubernetes/pull/130314), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]

### 1.30.12

- Fix a bug where kube-apiserver could emit an further watch even even if decryption failed for earlier event and it was not emitted. ([#131161](https://github.com/kubernetes/kubernetes/pull/131161), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery]
- Fix kubelet restart unmounts volumes of running pods if the referenced PVC is being deleted by the user ([#130686](https://github.com/kubernetes/kubernetes/pull/130686), [@carlory](https://github.com/carlory)) [SIG Node, Storage and Testing]


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.30.12**, the newest release recorded here for this line.

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
