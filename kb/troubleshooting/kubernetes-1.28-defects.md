---
id: TROUBLE-KUBERNETES_1_28_DEFECTS
type: troubleshooting
title: "kubernetes 1.28: defects fixed in the 1.28 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.28.0 <1.29.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - kubernetes 1.28 known issues
  - kubernetes 1.28 fixed in
  - is this kubernetes bug already fixed
tags:
  - troubleshooting
  - upgrade
  - kubernetes
sources:
  - type: docs
    path: kubernetes/kubernetes release notes for the 1.28 line — bug-fix entries
    url: https://github.com/kubernetes/kubernetes/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# kubernetes 1.28: defects fixed in the 1.28 line

## Summary

**109 defects** the project fixed across **16 releases** of the 1.28 line, from 1.28.0 to
1.28.15. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.28.0

- Fixed the alpha `CloudDualStackNodeIPs` feature. ([#118329](https://github.com/kubernetes/kubernetes/pull/118329), [@danwinship](https://github.com/danwinship))
- Updated cAdvisor to `v0.47.2` and fixed metrics in `cri-o` when a container restarts. ([#118774](https://github.com/kubernetes/kubernetes/pull/118774), [@harche](https://github.com/harche))
- Fixed nil pointer in test AfterEach volumeperf.go for sidecar release. ([#117368](https://github.com/kubernetes/kubernetes/pull/117368), [@sunnylovestiramisu](https://github.com/sunnylovestiramisu))
- Ensure Job status updates are batched by 1s. This fixes an unlikely scenario when a sequence of immediately completing pods could trigger a sequence of non-batched Job status updates. ([#118470](https://github.com/kubernetes/kubernetes/pull/118470), [@mimowo](https://github.com/mimowo)) [SIG Apps]
- Fixed a data race in TopologyCache when `AddHints` and `SetNodes` are called concurrently. ([#117249](https://github.com/kubernetes/kubernetes/pull/117249), [@tnqn](https://github.com/tnqn)) [SIG Apps and Network]
- Fixed a race condition in `kube-proxy` when using LocalModeNodeCIDR, to avoid dropping Services traffic if the object node is recreated when `kube-proxy` is starting. ([#118499](https://github.com/kubernetes/kubernetes/pull/118499), [@aojea](https://github.com/aojea))
- Fixed bug where `listOfStrings.join()` in CEL expressions resulted in an unexpected internal error. ([#117593](https://github.com/kubernetes/kubernetes/pull/117593), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery]
- Fixed incorrect calculation for ResourceQuota with PriorityClass as its scope. ([#117677](https://github.com/kubernetes/kubernetes/pull/117677), [@Huang-Wei](https://github.com/Huang-Wei)) [SIG API Machinery]
- Fix: After a Node is down and take some time to get back to up again, the mount point of the evicted Pods cannot be cleaned up successfully. (#111933) Meanwhile Kubelet will print the log `Orphaned pod "xxx" found, but error not a directory occurred when trying to remove the volumes dir` every 2 seconds. (#105536) ([#116134](https://github.com/kubernetes/kubernetes/pull/116134), [@cvvz](https://github.com/cvvz)) [SIG Node and Storage]
- Fix: The volume is not detached after the pod and PVC objects are deleted. ([#116138](https://github.com/kubernetes/kubernetes/pull/116138), [@cvvz](https://github.com/cvvz)) [SIG Storage]
- Fixed Cronjob `status.lastSuccessfulTime` not populated by a manually triggered ([#118530](https://github.com/kubernetes/kubernetes/pull/118530), [@carlory](https://github.com/carlory))
- Fixed Topology Aware Hints not working when the `topology.kubernetes.io/zone` label is added after Node creation. ([#117245](https://github.com/kubernetes/kubernetes/pull/117245), [@tnqn](https://github.com/tnqn))
- Fixed `creationTimestamp: null` causing unnecessary writes to etcd. ([#116865](https://github.com/kubernetes/kubernetes/pull/116865), [@alexzielenski](https://github.com/alexzielenski))
- Fixed `vSphere` cloud provider not to skip detach volumes from nodes at `kube-controller-startup`. ([#117243](https://github.com/kubernetes/kubernetes/pull/117243), [@jsafrane](https://github.com/jsafrane))
- Fixed a bug at `kube-apiserver` start where `APIService` objects for custom resources could be deleted and recreated. ([#118104](https://github.com/kubernetes/kubernetes/pull/118104), [@liggitt](https://github.com/liggitt))
- Fixed a bug that unintentionally overrides custom Accept headers in http (live-/readiness)-probes if the header is in lowercase. ([#114606](https://github.com/kubernetes/kubernetes/pull/114606), [@tuunit](https://github.com/tuunit))
- Fixed a bug where `kubectl port-forward`, when used with a Deployment, could connect to a terminating pod even when a running pod is also available. ([#119256](https://github.com/kubernetes/kubernetes/pull/119256), [@brianpursley](https://github.com/brianpursley)) [SIG CLI]
- Fixed a bug where pv recycler failed to scrub volume with too many files in the directory due to hitting ARG_MAX limit with rm command (#117189). ([#117283](https://github.com/kubernetes/kubernetes/pull/117283), [@defo89](https://github.com/defo89)) [SIG Cloud Provider and Storage]
- Fixed a memory leak in the Kubernetes API server that occurs during APIService processing. ([#117258](https://github.com/kubernetes/kubernetes/pull/117258), [@enj](https://github.com/enj)) [SIG API Machinery]
- Fixed a race condition between `Run()` and `SetTransform()` and `SetWatchErrorHandler()` in shared informers. ([#117870](https://github.com/kubernetes/kubernetes/pull/117870), [@howardjohn](https://github.com/howardjohn)) [SIG API Machinery]
- Fixed a race condition serving `OpenAPI` content ([#117705](https://github.com/kubernetes/kubernetes/pull/117705), [@Jefftree](https://github.com/Jefftree))
- Fixed a regression in `1.27.0` that resulted in `missing metadata in converted object` errors when modifying objects for multi-version custom resource definitions with a conversion strategy of `None`. ([#117301](https://github.com/kubernetes/kubernetes/pull/117301), [@ncdc](https://github.com/ncdc))
- Fixed a regression in `kubectl` and `client-go` discovery when configured with a server URL other than the root of a server ([#117495](https://github.com/kubernetes/kubernetes/pull/117495), [@ardaguclu](https://github.com/ardaguclu))
- Fixed an issue where the API server did not send impersonated UID to authentication webhooks. ([#116681](https://github.com/kubernetes/kubernetes/pull/116681), [@stlaz](https://github.com/stlaz)) [SIG API Machinery and Auth]
- Fixed bug that caused a resource to include patch directives when using strategic merge patch against a non-existent field. ([#117568](https://github.com/kubernetes/kubernetes/pull/117568), [@alexzielenski](https://github.com/alexzielenski))
- Fixed bug to correctly report `ErrRegistryUnavailable` on pulling container images for remote CRI runtimes. ([#117612](https://github.com/kubernetes/kubernetes/pull/117612), [@saschagrunert](https://github.com/saschagrunert)) [SIG Node]
- Fixed bug where explain was not properly respecting jsonpaths. ([#115694](https://github.com/kubernetes/kubernetes/pull/115694), [@mpuckett159](https://github.com/mpuckett159))
- Fixed bug where using the $deleteFromPrimitiveList directive in a strategic merge patch of certain fields would remove the other values from the list instead of the values specified. ([#110472](https://github.com/kubernetes/kubernetes/pull/110472), [@brianpursley](https://github.com/brianpursley)) [SIG API Machinery]
- Fixed component status calling etcd health endpoint over http which exposed kubernetes to the risk of complete watch starvation and is inconsistent with other etcd probing done by `kube-apiserver`. ([#118460](https://github.com/kubernetes/kubernetes/pull/118460), [@serathius](https://github.com/serathius))
- Fixed computing backoff delay when using Job pod failure policy, by including in the backoff delay calculation pod failures ignored from the backoffLimit counter. ([#119434](https://github.com/kubernetes/kubernetes/pull/119434), [@mimowo](https://github.com/mimowo))
- Fixed cronjob controller handling of complex schedules, like `30 6-16/4 * * 1-5`, for example. ([#118724](https://github.com/kubernetes/kubernetes/pull/118724), [@soltysh](https://github.com/soltysh))
- Fixed deletion of non-admissible pods that are deleted during Kubelet restart. ([#118497](https://github.com/kubernetes/kubernetes/pull/118497), [@mimowo](https://github.com/mimowo))
- Fixed issue where `kubectl-convert` would fail when encountering resources that could not be converted to the specified api version. New behavior is to warn the user of the failed conversions and continue to convert the remaining resources. ([#117002](https://github.com/kubernetes/kubernetes/pull/117002), [@gxwilkerson33](https://github.com/gxwilkerson33))
- Fixed issue where there was no response or error from kubectl rollout status when there were no resources of specified kind. ([#117884](https://github.com/kubernetes/kubernetes/pull/117884), [@gxwilkerson33](https://github.com/gxwilkerson33)) [SIG CLI]
- Fixed kubelet startup getting stuck with `NewVolumeManagerReconstruction` feature enabled and a CSI volume present in /var/lib/kubelet/pods. ([#117804](https://github.com/kubernetes/kubernetes/pull/117804), [@jsafrane](https://github.com/jsafrane)) [SIG Node and Storage]
- Fixed performance regression in scheduler caused by frequent metric lookup on critical code path. ([#117594](https://github.com/kubernetes/kubernetes/pull/117594), [@tosi3k](https://github.com/tosi3k))
- Fixed restricted debug profile. ([#117543](https://github.com/kubernetes/kubernetes/pull/117543), [@mochizuki875](https://github.com/mochizuki875))
- Fixed the `preStop` hook. This will now block the pod termination grace period. ([#115835](https://github.com/kubernetes/kubernetes/pull/115835), [@HirazawaUi](https://github.com/HirazawaUi))
- Fixed the discoverability of `apiregistration.k8s.io` in `openapi/v3` ([#118879](https://github.com/kubernetes/kubernetes/pull/118879), [@atiratree](https://github.com/atiratree))
- Known issue: fixed that the PreEnqueue plugins aren't executed for Pods proceeding to activeQ through backoffQ. ([#117194](https://github.com/kubernetes/kubernetes/pull/117194), [@sanposhiho](https://github.com/sanposhiho)) [SIG Release and Scheduling]
- Resolves a spurious "Unknown discovery response content-type" error in client-go discovery requests by tolerating extra content-type parameters in API responses ([#117571](https://github.com/kubernetes/kubernetes/pull/117571), [@seans3](https://github.com/seans3)) [SIG API Machinery]
- [Dual-stack] Fixed `generateAPIPodStatus()` of kubelet handling Secondary IP. hostIPs order may not be consistent. If secondary IP is before primary one, current logic adds primary IP twice into `PodIPs`, which leads to error: "may specify no more than one IP for each IP family". ([#116879](https://github.com/kubernetes/kubernetes/pull/116879), [@lzhecheng](https://github.com/lzhecheng))
- `kubeadm:` fixed a bug where the static pod changes detection logic is inconsistent with kubelet. ([#118069](https://github.com/kubernetes/kubernetes/pull/118069), [@SataQiu](https://github.com/SataQiu))
- `kubeadm`: fixed a bug where file copy(backup) could not be executed correctly on Windows platform during upgrade. ([#117861](https://github.com/kubernetes/kubernetes/pull/117861), [@SataQiu](https://github.com/SataQiu))
- Fixed dra e2e image build on non-amd64 architectures. ([#117912](https://github.com/kubernetes/kubernetes/pull/117912), [@bart0sh](https://github.com/bart0sh)) [SIG Node and Testing]
- `kubeadm`: Introduced a new feature gate `UpgradeAddonsBeforeControlPlane` to fix a kube-proxy skew policy misalignment. Its default value is `false`. Upgrade of the CoreDNS and kube-proxy addons will now trigger after all the control plane instances have been upgraded, unless the fearure gate is set to true. This feature gate will be removed in a future release. ([#117660](https://github.com/kubernetes/kubernetes/pull/117660), [@pacoxu](https://github.com/pacoxu))

### 1.28.1

- Fixes ability to build 1.28 without network access ([#119982](https://github.com/kubernetes/kubernetes/pull/119982), [@liggitt](https://github.com/liggitt)) [SIG Testing]

### 1.28.2

- Fixed a bug where CEL expressions in CRD validation rules would incorrectly compute a high estimated cost for functions that return strings, lists or maps. The incorrect cost was evident when the result of a function was used in subsequent operations. ([#119807](https://github.com/kubernetes/kubernetes/pull/119807), [@jpbetz](https://github.com/jpbetz)) [SIG API Machinery, Auth and Cloud Provider]
- Fix OpenAPI v3 not being cleaned up after deleting APIServices ([#120108](https://github.com/kubernetes/kubernetes/pull/120108), [@tnqn](https://github.com/tnqn)) [SIG API Machinery and Testing]
- Fix a 1.28 regression in scheduler: a pod with concurrent events could incorrectly get moved to the unschedulable queue where it could got stuck until the next periodic purging after 5 minutes if there was no other event for it. ([#120445](https://github.com/kubernetes/kubernetes/pull/120445), [@pohly](https://github.com/pohly)) [SIG Scheduling]
- Fix a concurrent map access in TopologyCache's `HasPopulatedHints` method. ([#120372](https://github.com/kubernetes/kubernetes/pull/120372), [@Miciah](https://github.com/Miciah)) [SIG Network]
- Fixed a 1.26 regression scheduling bug by ensuring that preemption is skipped when a PreFilter plugin returns `UnschedulableAndUnresolvable` ([#119951](https://github.com/kubernetes/kubernetes/pull/119951), [@sanposhiho](https://github.com/sanposhiho)) [SIG Scheduling]
- Fixed a 1.27 scheduling regression that PostFilter plugin may not function if previous PreFilter plugins return Skip ([#119942](https://github.com/kubernetes/kubernetes/pull/119942), [@Huang-Wei](https://github.com/Huang-Wei)) [SIG Scheduling and Testing]
- Fixed a 1.28 regression around restarting init containers in the right order relative to normal containers ([#120440](https://github.com/kubernetes/kubernetes/pull/120440), [@gjkim42](https://github.com/gjkim42)) [SIG Node and Testing]
- Fixed a regression in default 1.27 configurations in kube-apiserver: fixed the AggregatedDiscoveryEndpoint feature (beta in 1.27+) to successfully fetch discovery information from aggregated API servers that do not check `Accept` headers when serving the `/apis` endpoint ([#120359](https://github.com/kubernetes/kubernetes/pull/120359), [@Jefftree](https://github.com/Jefftree)) [SIG API Machinery]
- Fixes a 1.28 regression handling negative index json patches ([#120329](https://github.com/kubernetes/kubernetes/pull/120329), [@liggitt](https://github.com/liggitt)) [SIG API Machinery]
- Fixes a bug where images pinned by the container runtime can be garbage collected by kubelet. ([#120053](https://github.com/kubernetes/kubernetes/pull/120053), [@ruiwen-zhao](https://github.com/ruiwen-zhao)) [SIG Node]
- Kubeadm: fix nil pointer when etcd member is already removed ([#120010](https://github.com/kubernetes/kubernetes/pull/120010), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]

### 1.28.3

- E2e framework: retrying after intermittent apiserver failures was fixed in WaitForPodsResponding ([#120559](https://github.com/kubernetes/kubernetes/pull/120559), [@pohly](https://github.com/pohly)) [SIG Testing]
- Fix 1.28.0 regression where adding aggregated APIService objects could cause apiserver to panic and affect the health check ([#121040](https://github.com/kubernetes/kubernetes/pull/121040), [@Jefftree](https://github.com/Jefftree)) [SIG API Machinery and Testing]
- Fix a bug in cronjob controller where already created jobs may be missing from the status. ([#120649](https://github.com/kubernetes/kubernetes/pull/120649), [@andrewsykim](https://github.com/andrewsykim)) [SIG Apps]
- Fixed a 1.28.0 regression where kube-controller-manager can crash when StatefulSet with Parallel policy and PVC labels is scaled up. ([#121184](https://github.com/kubernetes/kubernetes/pull/121184), [@aleksandra-malinowska](https://github.com/aleksandra-malinowska)) [SIG Apps]
- Fixed a bug where containers would not start on cgroupv2 systems where swap is disabled. ([#120924](https://github.com/kubernetes/kubernetes/pull/120924), [@klueska](https://github.com/klueska)) [SIG Node]
- Fixed a regression in kube-proxy where it might refuse to start if given single-stack IPv6 configuration options on a node that has both IPv4 and IPv6 IPs. ([#121008](https://github.com/kubernetes/kubernetes/pull/121008), [@danwinship](https://github.com/danwinship)) [SIG Network]
- Fixed an issue to not drain all the pods in a namespace when an empty-selector i.e. "{}" is specified in a Pod Disruption Budget (PDB) ([#121131](https://github.com/kubernetes/kubernetes/pull/121131), [@sairameshv](https://github.com/sairameshv)) [SIG Apps]
- Fixed attaching volumes after detach errors. Now volumes that failed to detach are not treated as attached, Kubernetes will make sure they are fully attached before they can be used by pods. ([#120595](https://github.com/kubernetes/kubernetes/pull/120595), [@jsafrane](https://github.com/jsafrane)) [SIG Apps and Storage]
- Fixed bug to surface events for the following metrics: apiserver_encryption_config_controller_automatic_reload_failures_total, apiserver_encryption_config_controller_automatic_reload_last_timestamp_seconds, apiserver_encryption_config_controller_automatic_reload_success_total ([#120544](https://github.com/kubernetes/kubernetes/pull/120544), [@ritazh](https://github.com/ritazh)) [SIG API Machinery, Auth and Testing]
- Fixes a bug where Services using finalizers may hold onto ClusterIP and/or NodePort allocated resources for longer than expected if the finalizer is removed using the status subresource ([#120654](https://github.com/kubernetes/kubernetes/pull/120654), [@aojea](https://github.com/aojea)) [SIG Testing]
- Fixes an issue where the vsphere cloud provider will not trust a certificate if: The issuer of the certificate is unknown (x509.UnknownAuthorityError) The requested name does not match the set of authorized names (x509.HostnameError) The error surfaced after attempting a connection contains one of the substrings: "certificate is not trusted" or "certificate signed by unknown authority" ([#120768](https://github.com/kubernetes/kubernetes/pull/120768), [@MadhavJivrajani](https://github.com/MadhavJivrajani)) [SIG Architecture and Cloud Provider]

### 1.28.4

- Fix 121094 by re-introducing the readiness predicate for externalTrafficPolicy: Local services. ([#121116](https://github.com/kubernetes/kubernetes/pull/121116), [@alexanderConstantinescu](https://github.com/alexanderConstantinescu)) [SIG Cloud Provider and Network]
- Fixed a regression in default configurations, which enabled PodDisruptionConditions by default, that prevented the control plane's pod garbage collector from deleting pods that contained duplicated field keys (env. variables with repeated keys or container ports). ([#121379](https://github.com/kubernetes/kubernetes/pull/121379), [@mimowo](https://github.com/mimowo)) [SIG Apps, Auth, Node, Scheduling and Testing]
- Fixed the issue where pod with ordinal number lower than the rolling partitioning number was being deleted it was coming up with updated image. ([#120731](https://github.com/kubernetes/kubernetes/pull/120731), [@adilGhaffarDev](https://github.com/adilGhaffarDev)) [SIG Apps and Testing]
- Fixes calculating the requeue time in the cronjob controller, which results in properly handling failed/stuck jobs ([#121327](https://github.com/kubernetes/kubernetes/pull/121327), [@soltysh](https://github.com/soltysh)) [SIG Apps]

### 1.28.5

- Fix panic if there are more terminating pods than active pods ([#122267](https://github.com/kubernetes/kubernetes/pull/122267), [@kannon92](https://github.com/kannon92)) [SIG Apps]
- Fix: statle smb mount issue when smb file share is deleted and then unmount ([#121851](https://github.com/kubernetes/kubernetes/pull/121851), [@andyzhangx](https://github.com/andyzhangx)) [SIG Storage]
- Fixed a regression since 1.27.0 in scheduler framework when running score plugins. The `skippedScorePlugins` number might be greater than `enabledScorePlugins`, so when initializing a slice the cap(len(skippedScorePlugins) - len(enabledScorePlugins)) is negative, which is not allowed. ([#121667](https://github.com/kubernetes/kubernetes/pull/121667), [@kerthcet](https://github.com/kerthcet)) [SIG Scheduling]
- Fixes a kube-apiserver log volume regression bug in default 1.27 configurations (introduced in 1.26, activated by the AggregatedDiscoveryEndpoint feature enablement in 1.27) ([#122096](https://github.com/kubernetes/kubernetes/pull/122096), [@ritazh](https://github.com/ritazh)) [SIG API Machinery]
- Fixes a regression in kube-scheduler memory use in default 1.28 configurations by moving the SchedulerQueueingHints feature gate back to disabled by default. ([#122291](https://github.com/kubernetes/kubernetes/pull/122291), [@sanposhiho](https://github.com/sanposhiho)) [SIG Scheduling]
- Fixes an issue where StatefulSet might not restart a pod after eviction or node failure. ([#121389](https://github.com/kubernetes/kubernetes/pull/121389), [@aleksandra-malinowska](https://github.com/aleksandra-malinowska)) [SIG Apps and Testing]

### 1.28.6

- Fix: Mount point may become local without calling NodePublishVolume after node rebooting. ([#119923](https://github.com/kubernetes/kubernetes/pull/119923), [@cvvz](https://github.com/cvvz)) [SIG Node and Storage]
- Fixed a regression since 1.24 in the scheduling framework when overriding MultiPoint plugins (e.g. default plugins). The incorrect loop logic might lead to a plugin being loaded multiple times, consequently preventing any Pod from being scheduled, which is unexpected. ([#122368](https://github.com/kubernetes/kubernetes/pull/122368), [@caohe](https://github.com/caohe)) [SIG Scheduling]

### 1.28.7

- Fixes a race condition in the iptables mode of kube-proxy in 1.27 and later that could result in some updates getting lost (e.g., when a service gets a new endpoint, the rules for the new endpoint might not be added until much later). ([#122757](https://github.com/kubernetes/kubernetes/pull/122757), [@hakman](https://github.com/hakman)) [SIG Network]
- Kubeadm: fix a bug where the --rootfs global flag does not work with "kubeadm upgrade node" for control plane nodes. ([#123097](https://github.com/kubernetes/kubernetes/pull/123097), [@neolit123](https://github.com/neolit123)) [SIG Cluster Lifecycle]

### 1.28.8

- Fix error when trying to expand a volume that does not require node expansion ([#123055](https://github.com/kubernetes/kubernetes/pull/123055), [@gnufied](https://github.com/gnufied)) [SIG Node and Storage]
- Fixed a bug that an init container with containerRestartPolicy with `Always` cannot update its state from terminated to non-terminated for the pod with restartPolicy with `Never` or `OnFailure`. ([#123710](https://github.com/kubernetes/kubernetes/pull/123710), [@gjkim42](https://github.com/gjkim42)) [SIG Apps]
- Fixed cleanup of Pod volume mounts when a file was used as a subpath. ([#123052](https://github.com/kubernetes/kubernetes/pull/123052), [@jsafrane](https://github.com/jsafrane)) [SIG Node]
- Fixed the disruption controller's PDB status synchronization to maintain all PDB conditions during an update. ([#122056](https://github.com/kubernetes/kubernetes/pull/122056), [@dhenkel92](https://github.com/dhenkel92)) [SIG Apps]
- Fixes an issue calculating total CPU usage reported for Windows nodes ([#122999](https://github.com/kubernetes/kubernetes/pull/122999), [@marosset](https://github.com/marosset)) [SIG Node and Windows]
- Prevent watch cache starvation by moving its watch to separate RPC and add a SeparateCacheWatchRPC feature flag to disable this behavior ([#123694](https://github.com/kubernetes/kubernetes/pull/123694), [@mengqiy](https://github.com/mengqiy)) [SIG API Machinery]

### 1.28.9

- Fix pod restart after node reboot when NewVolumeManagerReconstruction feature gate is enabled and SELinuxMountReadWriteOncePod disabled ([#124141](https://github.com/kubernetes/kubernetes/pull/124141), [@bertinatto](https://github.com/bertinatto)) [SIG Node]
- Kube-apiserver: fixes a 1.27+ regression in watch stability by serving watch requests without a resourceVersion from the watch cache by default, as in <1.27 (disabling the change in #115096 by default). This mitigates the impact of an etcd watch bug (https://github.com/etcd-io/etcd/pull/17555). If the 1.27 change in #115096 to serve these requests from underlying storage is still desired despite the impact on watch stability, it can be re-enabled with a `WatchFromStorageWithoutResourceVersion` feature gate. ([#124006](https://github.com/kubernetes/kubernetes/pull/124006), [@serathius](https://github.com/serathius)) [SIG API Machinery]
- Kubeadm: fix panic in the command "kubeadm certs check-expiration" when "/etc/kubernetes/pki" exists but cannot be read. ([#124124](https://github.com/kubernetes/kubernetes/pull/124124), [@carlory](https://github.com/carlory)) [SIG Cluster Lifecycle]

### 1.28.10

- Fixed PersistentolumeLabel providing wrong topology labels to Azure Disk PersistentVolumes when the external Azure cloud provider is used. ([#124528](https://github.com/kubernetes/kubernetes/pull/124528), [@jsafrane](https://github.com/jsafrane)) [SIG Cloud Provider]
- Fixed a bug that a pod may remain unscheduled if any PreFilter plugin returns nodes that do not exist. ([#124764](https://github.com/kubernetes/kubernetes/pull/124764), [@chengjoey](https://github.com/chengjoey)) [SIG Scheduling and Testing]

### 1.28.11

- Kube-apiserver: fixes a 1.28 regression printing pods with invalid initContainer status ([#124910](https://github.com/kubernetes/kubernetes/pull/124910), [@liggitt](https://github.com/liggitt)) [SIG Node]
- Kube-scheduler: fixes a 1.28.10 regression that can lead to a scheduler crash when processing pods with affinity that doesn't match a real/valid node ([#125042](https://github.com/kubernetes/kubernetes/pull/125042), [@AxeZhan](https://github.com/AxeZhan)) [SIG Scheduling and Testing]
- Reduce critical section in watchcache to fix kube-apiserver scalability under heavy load of list requests ([#122027](https://github.com/kubernetes/kubernetes/pull/122027), [@wojtek-t](https://github.com/wojtek-t)) [SIG API Machinery]

### 1.28.12

- Fix a bug that Pods could stuck in the unschedulable pod pool if they're rejected by PreEnqueue plugins that could change its result by a change in resources apart from Pods
- Fix endpoints status out-of-sync when the pod state changes rapidly ([#125675](https://github.com/kubernetes/kubernetes/pull/125675), [@tnqn](https://github.com/tnqn)) [SIG Apps, Network and Testing]

### 1.28.13

- Fixed a bug in the API server where empty collections of ValidatingAdmissionPolicies did not have an `items` field. ([#126159](https://github.com/kubernetes/kubernetes/pull/126159), [@xyz-li](https://github.com/xyz-li)) [SIG API Machinery]
- Fix the bug where PodIP field is temporarily removed for a terminal pod ([#125404](https://github.com/kubernetes/kubernetes/pull/125404), [@mimowo](https://github.com/mimowo)) [SIG Node and Testing]
- Fixed a bug in ValidatingAdmissionPolicy that caused policies which were using CRD parameters to fail to synchronize ([#123003](https://github.com/kubernetes/kubernetes/pull/123003), [@alexzielenski](https://github.com/alexzielenski)) [SIG API Machinery and Testing]
- Kube-apiserver: fixes a 1.27+ regression watching a single namespace via the deprecated /api/v1/watch/namespaces/$name endpoint where watch events were not delivered after the watch was established ([#126150](https://github.com/kubernetes/kubernetes/pull/126150), [@xyz-li](https://github.com/xyz-li)) [SIG API Machinery and Testing]
- Kube-apiserver: fixes a potential crash serving CustomResourceDefinitions that combine an invalid schema and CEL validation rules. ([#126167](https://github.com/kubernetes/kubernetes/pull/126167), [@cici37](https://github.com/cici37)) [SIG API Machinery and Testing]

### 1.28.14

- Fix a scheduler preemption issue where the victim pod was not deleted due to incorrect status patching. This issue occurred when the preemptor and victim pods had different QoS classes in their status, causing the preemption to fail entirely. ([#126695](https://github.com/kubernetes/kubernetes/pull/126695), [@Huang-Wei](https://github.com/Huang-Wei)) [SIG Scheduling]
- Fix race condition in kube-proxy initialization that could blackhole UDP traffic to service VIP. ([#126692](https://github.com/kubernetes/kubernetes/pull/126692), [@wedaly](https://github.com/wedaly)) [SIG Network]
- Terminated Pods on a node will not be re-admitted on kubelet restart. This fixes the problem of Completed Pods awaiting for the finalizer marked as Failed after the kubelet restart. ([#127210](https://github.com/kubernetes/kubernetes/pull/127210), [@SergeyKanzhelev](https://github.com/SergeyKanzhelev)) [SIG Node and Testing]

### 1.28.15

- Fix a bug on the endpoints controller that does not reconcile the Endpoint object after this is truncated (it gets more than 1000 endpoints addresses) ([#127417](https://github.com/kubernetes/kubernetes/pull/127417), [@aojea](https://github.com/aojea)) [SIG Apps, Network and Testing]
- Kubeadm: fix wrong member list reported when removing an etcd member ([#127963](https://github.com/kubernetes/kubernetes/pull/127963), [@SataQiu](https://github.com/SataQiu)) [SIG Cluster Lifecycle]


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.28.15**, the newest release recorded here for this line.

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
