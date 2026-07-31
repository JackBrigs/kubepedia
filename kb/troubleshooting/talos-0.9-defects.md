---
id: TROUBLE-TALOS_0_9_DEFECTS
type: troubleshooting
title: "talos 0.9: defects fixed in the 0.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.9.0 <0.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 0.9 known issues
  - talos 0.9 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 0.9 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 0.9: defects fixed in the 0.9 line

## Summary

**345 defects** the project fixed across **4 releases** of the 0.9 line, from 0.9.0 to
0.9.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.9.0

- [`c6f7c7f36`](https://github.com/talos-systems/talos/commit/c6f7c7f3643b0514fc2f085ad772317edc994585) fix: command `etcd remove-member` shouldn't remove etcd data directory
- [`26c924619`](https://github.com/talos-systems/talos/commit/26c9246197d88ae6a355a72d0edc9ecfda90b7de) fix: upgrade-k8s bug with empty config values and provision script
- [`9d3605361`](https://github.com/talos-systems/talos/commit/9d36053616a9976f82d90158cb834aa66ae9545b) fix: talosctl health should not check kube-proxy when it is disabled
- [`5bf28b8c8`](https://github.com/talos-systems/talos/commit/5bf28b8c811135241713c4d4da9f52eefb13904f) fix: properly format spec comments in the resources
- [`6d7b0efc6`](https://github.com/talos-systems/talos/commit/6d7b0efc6083cc458f406b9d3a62e42aef70a2f0) fix: don't touch any partitions on upgrade with --preserve
- [`96477d249`](https://github.com/talos-systems/talos/commit/96477d24920e35d27b076d1874729a4faf5b4737) chore: fix provision tests after changes to build-container
- [`67e0317b9`](https://github.com/talos-systems/talos/commit/67e0317b9d0ad5cbe167e150b9ea61e97f47bf15) fix: update output of `convert-k8s` command
- [`51f59f435`](https://github.com/talos-systems/talos/commit/51f59f435192e9d1ec976121a0ddd3cc8a1a4416) fix: move containerd CRI config files under `/var/`
- [`c2e353d6a`](https://github.com/talos-systems/talos/commit/c2e353d6afa38d8a3af533b10c9b4bdf0ef3412d) fix: do not print out help string if the parameters are correct
- [`49853fc2e`](https://github.com/talos-systems/talos/commit/49853fc2ecb846898d66d90fc76e6d875b775901) fix: mkdir source of the extra mounts for the kubelet
- [`e8e91d643`](https://github.com/talos-systems/talos/commit/e8e91d6434968bbcc52e832a4eb4ee87de09e228) fix: properly propagate nameservers to provisioned docker clusters
- [`81acadf34`](https://github.com/talos-systems/talos/commit/81acadf345d00a30f26cdc979dd06e7dd0086c7c) fix: ignore connection refused errors when updating/converting cp
- [`db3785b93`](https://github.com/talos-systems/talos/commit/db3785b9301b1ce7772ea90eace093f13ae45db7) fix: align partition start to the physical sector size
- [`df52c1358`](https://github.com/talos-systems/talos/commit/df52c135817639b9408ac34b81781ce8a6dcb1b5) chore: fix //nolint directives
- [`7e8f13652`](https://github.com/talos-systems/talos/commit/7e8f13652ce57797252804891952049c66c43f6e) chore: fix upgrade tests by bumping 0.9 to alpha.5
- [`044fb7708`](https://github.com/talos-systems/talos/commit/044fb7708cc7786e8620403e14f680b47a8e6907) fix: chmod etcd PKI path to fix virtual IP for upgrades with persistence
- [`8ffb55943`](https://github.com/talos-systems/talos/commit/8ffb55943c71a100c0b1fd53c5520b2cf3ec72b8) fix: ignore 'ENOENT' (no such file directory) on mount
- [`561f8aa15`](https://github.com/talos-systems/talos/commit/561f8aa15eb47f5a7f329ede2190748ca4ee8ee3) fix: move etcd to `cri` containerd runner
- [`31e56e63d`](https://github.com/talos-systems/talos/commit/31e56e63db24efba88a10d4b0c4190aeebbb125b) fix: update in-cluster kubeconfig validity to match other certs
- [`c2f7a4b6f`](https://github.com/talos-systems/talos/commit/c2f7a4b6f883870d1c94621a4f88520916f7647f) fix: add ApplyDynamicConfig call in the apply-config --immediate mode
- [`5ae315f49`](https://github.com/talos-systems/talos/commit/5ae315f493f6585b24cf2e55ef8ef009170c07ee) fix: set hdmi_safe=1 on Raspberry Pi for maximum HDMI compatibility
- [`c7ee23908`](https://github.com/talos-systems/talos/commit/c7ee2390877ef40883384ec6540bacc2dd9bd709) fix: show stopped/exited containers via CRI inspector
- [`63160277d`](https://github.com/talos-systems/talos/commit/63160277d6fbcd5a262239e99d6f4512fd4941b8) fix: make ApplyDynamicConfig idempotent
- [`779ac74a0`](https://github.com/talos-systems/talos/commit/779ac74a08ae1384875e1db0e98ff346ba24fd03) fix: improve the drain function
- [`f24c81537`](https://github.com/talos-systems/talos/commit/f24c815373c0e249c80186939574e62ccc8c82e7) fix: correctly set service state in the resource
- [`589d01892`](https://github.com/talos-systems/talos/commit/589d01892cb3e80dda92364495513eafe4b4f0fa) fix: update the layout of the Disks API to match proxying requirements
- [`09369fedb`](https://github.com/talos-systems/talos/commit/09369fedba9535cd7105bc2e2b934063a807f47f) fix: stop and clean up installer container correctly
- [`1a491ee85`](https://github.com/talos-systems/talos/commit/1a491ee85e20469fefa42a0b29cdb29b2a03c1df) fix: sanitize volume name better in static pod extra volumes
- [`e355d4fae`](https://github.com/talos-systems/talos/commit/e355d4faedeaa3248c37e57de28754a93e50dd55) fix: redirect warnings in manifest apply k8s client
- [`41430e72d`](https://github.com/talos-systems/talos/commit/41430e72d22f1e9828ad5704b6ef0a6b1be99ce1) fix: handle case when kubelet serving certificates are issued
- [`7a6e0cd3e`](https://github.com/talos-systems/talos/commit/7a6e0cd3e51750821d4647de2bedd544dc127dff) fix: correctly escape extra args in kube-proxy manifest
- [`d2d5c72bb`](https://github.com/talos-systems/talos/commit/d2d5c72bb5454bcb09149e0ffe7e3d844aa98a2d) fix: skip empty manifest YAML sub-documents
- [`254e0e91e`](https://github.com/talos-systems/talos/commit/254e0e91e1b05c35878c39fc2eddde8002088609) fix: correctly unwrap responses for etcd commands
- [`292bc3968`](https://github.com/talos-systems/talos/commit/292bc396817328d6212e190e39e13f9c814c42b9) chore(ci): fix schedules in Drone pipelines
- [`162d8b6be`](https://github.com/talos-systems/talos/commit/162d8b6bef5fc155a7f337371ca1358c36c4ab89) fix: drop cri dependency on etcd
- [`9205870ee`](https://github.com/talos-systems/talos/commit/9205870ee6949196d4043912be2b1c8a0efe3246) fix: move versions to annotations in control plane static pods
- [`8d7a36cc0`](https://github.com/talos-systems/talos/commit/8d7a36cc0cc22cb26cb3bbbe656a3ec5e33b87fb) fix: find master node IPs correctly in health checks
- [`6791036cf`](https://github.com/talos-systems/talos/commit/6791036cfa94566f0f947f95effa8a43ddfd0f92) fix: add 3 seconds grub boot timeout
- [`ffe34ec10`](https://github.com/talos-systems/talos/commit/ffe34ec100b1a2e1969f15c0dc3c39e5e75ace2e) fix: don't use filename from URL when downloading manifest
- [`1111edfc7`](https://github.com/talos-systems/talos/commit/1111edfc7681f2634d43c061a0f9f5bcfe56db4e) fix: pass attributes when adding routes
- [`d99a016af`](https://github.com/talos-systems/talos/commit/d99a016af2382e6ba22877c2dcc87af610c0c1f3) fix: correct response structure for GenerateConfig API
- [`df0099036`](https://github.com/talos-systems/talos/commit/df0099036c4f47ef262d846dbe7db9ecdd16ead3) fix: correctly extract wrapped error messages
- [`1a32d55e4`](https://github.com/talos-systems/talos/commit/1a32d55e4053045b70922b40dd6f0c54770118df) fix: prevent crash in machined on apid service stop
- [`3aaa888f9`](https://github.com/talos-systems/talos/commit/3aaa888f9a91b84446db3b1fc2f57cfeae67968e) docs: fix typos
- [`85ae9f75e`](https://github.com/talos-systems/talos/commit/85ae9f75e91f7ac557ad1cef1ae9e49919decd8f) fix: wait for time sync before generating Kubernetes certificates
- [`b526c2cc3`](https://github.com/talos-systems/talos/commit/b526c2cc33bc5cf9adfcbe6ad994e6391d0a1869) fix: set proper hostname on docker nodes
- [`a07cfbd5a`](https://github.com/talos-systems/talos/commit/a07cfbd5a42318be189fd7a6c0fb1ab1707528dd) fix: mount kubelet secrets from system instead of ephemeral
- [`33de89ef9`](https://github.com/talos-systems/talos/commit/33de89ef90bd2c26014dfeea999eaf49b4c99733) fix: allow loading of empty config files
- [`757cc204e`](https://github.com/talos-systems/talos/commit/757cc204ecc434736d584441f45d2571f2f342ef) fix: prefer configured nameservers, fix DHCP6 in container
- [`5855b8d53`](https://github.com/talos-systems/talos/commit/5855b8d532def16b5bc49fa0c692d5c2fc8cc3f4) fix: refresh control plane endpoints on worker apids on schedule
- [`47c260e36`](https://github.com/talos-systems/talos/commit/47c260e365a3da294761eabc2a4611670228f2f3) fix: update DHCP client to use Request-Ack sequence after an Offer
- [`9947ec84d`](https://github.com/talos-systems/talos/commit/9947ec84d70b477e9173447bad59fce029f22fa4) fix: use hugetlbfs instead of none
- [`389349c02`](https://github.com/talos-systems/talos/commit/389349c02bf38ca4d8eca9a30aaf703d707db9d6) fix: use grpc load-balancing when connecting to trustd
- [`512c79e8d`](https://github.com/talos-systems/talos/commit/512c79e8d646f38699f7cb69e99d7a1643d86f8a) fix: lower memory usage a bit by disabling memory profiling
- [`1cded4d33`](https://github.com/talos-systems/talos/commit/1cded4d33ee5506ce7241ba828dcbbb550c88190) chore: fix import path for fsnotify
- [`064d33229`](https://github.com/talos-systems/talos/commit/064d33229879165a73656dcf59d50e385c814bfb) fix: don't probe disks in container mode
- [`1051d2ab6`](https://github.com/talos-systems/talos/commit/1051d2ab654c70a66c1370dd093e3a53a6a1128a) fix: prefix rendered Talos-owned static pod manifests
- [`7be3a8609`](https://github.com/talos-systems/talos/commit/7be3a860917323d7f5986c04d61c9b8681731186) fix: bump timeout for worker apid waiting for kubelet client config
- [`76a679443`](https://github.com/talos-systems/talos/commit/76a6794436c072150f27b7ab0a45ae738a1e8bd8) fix: kill all processes and umount all disk on reboot/shutdown
- [`18db20dbc`](https://github.com/talos-systems/talos/commit/18db20dbc2318647da2639b548a0101a85268420) fix: open blockdevices with exclusive flock for partitioning
- [`d515613bb`](https://github.com/talos-systems/talos/commit/d515613bb7862f15ef68da57cdde7130624dbc03) fix: list command unlimited recursion default behavior
- [`af5c34b34`](https://github.com/talos-systems/talos/commit/af5c34b340f1143abc848388eadad96834f16df5) fix: pick first interface valid hostname (vs. last one)
- [`d19486afa`](https://github.com/talos-systems/talos/commit/d19486afaa79cd8dbc223246ed8bb86a7dff9e12) fix: allow 'console' argument in kernel args to be always overridden
- [`5325a66e3`](https://github.com/talos-systems/talos/commit/5325a66e3e3bc4ae648e38ff60bfbf9a261caeea) fix: bring up bonded interfaces correctly on packet
- [`a8dd2ff30`](https://github.com/talos-systems/talos/commit/a8dd2ff30d36b248eb5789b9c9dc67df62970ee8) fix: checkpoint controller-manager and scheduler
- [`11229a018`](https://github.com/talos-systems/talos/commit/11229a0180c58655a8ab6f63fd12bd2b3405da9b) docs: fix latest docs
- [`6a0e652f0`](https://github.com/talos-systems/talos/commit/6a0e652f0c0ca7ccee58b8e7eaf5c0553963a201) fix: correctly transport gRPC errors from apid
- [`47fb7d26e`](https://github.com/talos-systems/talos/commit/47fb7d26e0a2887a524802788523ec5ff9ad3af6) fix: use SetAll instead of AppendAll when building kernel args
- [`b4ddfbfe9`](https://github.com/talos-systems/talos/commit/b4ddfbfe9bec8d4fc7e8e68a112b62e583860f23) fix: add more dependencies for bootstrap services
- [`73c81c501`](https://github.com/talos-systems/talos/commit/73c81c501e239f06df23731df21d53125f570fa7) fix: pass disk image flags to e2e-qemu cluster create command
- [`5e3b8ee09`](https://github.com/talos-systems/talos/commit/5e3b8ee099f8b3d2d2d37e507b7eb3a064894cd7) fix: ignore pods spun up from checkpoints in health checks
- [`e75bb27cf`](https://github.com/talos-systems/talos/commit/e75bb27cf4c3a828ac8a6e70603257dc075a49be) fix: leave etcd for staged upgrades
- [`f1964aab5`](https://github.com/talos-systems/talos/commit/f1964aab5314f9d8e1106f68611aec666463dd30) fix: ignore errors on stopping/removing pod sandboxes
- [`14b43068d`](https://github.com/talos-systems/talos/commit/14b43068d04673a143783fa0143d907b0d900c9b) docs: fix SBC docs to point to beta.0 instead of beta.1
- [`941556cff`](https://github.com/talos-systems/talos/commit/941556cffbcadcb4c3334d0da30c4e9077e91ab5) fix: use the correct console on Banana Pi M64
- [`e791e7dca`](https://github.com/talos-systems/talos/commit/e791e7dca95175671e058c9cc72e280b681b7bc1) fix: don't run LabelNodeAsMaster in two sequences
- [`c6f7c7f3`](https://github.com/talos-systems/talos/commit/c6f7c7f3643b0514fc2f085ad772317edc994585) fix: command `etcd remove-member` shouldn't remove etcd
- [`26c92461`](https://github.com/talos-systems/talos/commit/26c9246197d88ae6a355a72d0edc9ecfda90b7de) fix: upgrade-k8s bug with empty config values and provis
- [`cf75519`](https://github.com/talos-systems/crypto/commit/cf75519cab82bd1b128ae9b45107c6bb422bd96a) fix: function NewKeyPair should create certificate with proper subject
- [`bb3ad73`](https://github.com/talos-systems/go-blockdevice/commit/bb3ad73f69836acc2785ec659435e24a531359e7) fix: align partition start to physical sector size
- [`1cf7f25`](https://github.com/talos-systems/go-blockdevice/commit/1cf7f252c38cf11ef07723de2debc27d1da6b520) fix: properly handle no child processes error from cmd.Wait
- [`b8955a5`](https://github.com/talos-systems/os-runtime/commit/b8955a5475fe7b6c436757477c887ed7ef82eee7) fix: attach stack trace to panic error message
- [`98acf0d`](https://github.com/talos-systems/os-runtime/commit/98acf0d2d3321a088e05f2d12c4c0ca00cbe3de0) fix: preserve original YAML formatting in resource.Any

### 0.9.1

- [`be149162b`](https://github.com/talos-systems/talos/commit/be149162bb5ceb3ac8e65f27043d4ac5c73aa1b6) fix: prevent panic in validate config if `machine.install` is missing
- [`a8cf70cf5`](https://github.com/talos-systems/talos/commit/a8cf70cf563e0a9de253299bf80cc52ff234d4e0) fix: allow `convert-k8s --remove-initialized-keys` with K8s cp is down
- [`41cf6c1c4`](https://github.com/talos-systems/talos/commit/41cf6c1c45d2ced55037ee920eb5f1c87d9ec86f) fix: get rid of data race in encoder and fix concurrent map access
- [`5772e7ff6`](https://github.com/talos-systems/talos/commit/5772e7ff6b5c28f015a8b48860240863776ba5bc) fix: resolve the issue with DHCP lease not being renewed
- [`c6f7c7f36`](https://github.com/talos-systems/talos/commit/c6f7c7f3643b0514fc2f085ad772317edc994585) fix: command `etcd remove-member` shouldn't remove etcd data directory
- [`26c924619`](https://github.com/talos-systems/talos/commit/26c9246197d88ae6a355a72d0edc9ecfda90b7de) fix: upgrade-k8s bug with empty config values and provision script
- [`9d3605361`](https://github.com/talos-systems/talos/commit/9d36053616a9976f82d90158cb834aa66ae9545b) fix: talosctl health should not check kube-proxy when it is disabled
- [`5bf28b8c8`](https://github.com/talos-systems/talos/commit/5bf28b8c811135241713c4d4da9f52eefb13904f) fix: properly format spec comments in the resources
- [`6d7b0efc6`](https://github.com/talos-systems/talos/commit/6d7b0efc6083cc458f406b9d3a62e42aef70a2f0) fix: don't touch any partitions on upgrade with --preserve
- [`96477d249`](https://github.com/talos-systems/talos/commit/96477d24920e35d27b076d1874729a4faf5b4737) chore: fix provision tests after changes to build-container
- [`67e0317b9`](https://github.com/talos-systems/talos/commit/67e0317b9d0ad5cbe167e150b9ea61e97f47bf15) fix: update output of `convert-k8s` command
- [`51f59f435`](https://github.com/talos-systems/talos/commit/51f59f435192e9d1ec976121a0ddd3cc8a1a4416) fix: move containerd CRI config files under `/var/`
- [`c2e353d6a`](https://github.com/talos-systems/talos/commit/c2e353d6afa38d8a3af533b10c9b4bdf0ef3412d) fix: do not print out help string if the parameters are correct
- [`49853fc2e`](https://github.com/talos-systems/talos/commit/49853fc2ecb846898d66d90fc76e6d875b775901) fix: mkdir source of the extra mounts for the kubelet
- [`e8e91d643`](https://github.com/talos-systems/talos/commit/e8e91d6434968bbcc52e832a4eb4ee87de09e228) fix: properly propagate nameservers to provisioned docker clusters
- [`81acadf34`](https://github.com/talos-systems/talos/commit/81acadf345d00a30f26cdc979dd06e7dd0086c7c) fix: ignore connection refused errors when updating/converting cp
- [`db3785b93`](https://github.com/talos-systems/talos/commit/db3785b9301b1ce7772ea90eace093f13ae45db7) fix: align partition start to the physical sector size
- [`df52c1358`](https://github.com/talos-systems/talos/commit/df52c135817639b9408ac34b81781ce8a6dcb1b5) chore: fix //nolint directives
- [`7e8f13652`](https://github.com/talos-systems/talos/commit/7e8f13652ce57797252804891952049c66c43f6e) chore: fix upgrade tests by bumping 0.9 to alpha.5
- [`044fb7708`](https://github.com/talos-systems/talos/commit/044fb7708cc7786e8620403e14f680b47a8e6907) fix: chmod etcd PKI path to fix virtual IP for upgrades with persistence
- [`8ffb55943`](https://github.com/talos-systems/talos/commit/8ffb55943c71a100c0b1fd53c5520b2cf3ec72b8) fix: ignore 'ENOENT' (no such file directory) on mount
- [`561f8aa15`](https://github.com/talos-systems/talos/commit/561f8aa15eb47f5a7f329ede2190748ca4ee8ee3) fix: move etcd to `cri` containerd runner
- [`31e56e63d`](https://github.com/talos-systems/talos/commit/31e56e63db24efba88a10d4b0c4190aeebbb125b) fix: update in-cluster kubeconfig validity to match other certs
- [`c2f7a4b6f`](https://github.com/talos-systems/talos/commit/c2f7a4b6f883870d1c94621a4f88520916f7647f) fix: add ApplyDynamicConfig call in the apply-config --immediate mode
- [`5ae315f49`](https://github.com/talos-systems/talos/commit/5ae315f493f6585b24cf2e55ef8ef009170c07ee) fix: set hdmi_safe=1 on Raspberry Pi for maximum HDMI compatibility
- [`c7ee23908`](https://github.com/talos-systems/talos/commit/c7ee2390877ef40883384ec6540bacc2dd9bd709) fix: show stopped/exited containers via CRI inspector
- [`63160277d`](https://github.com/talos-systems/talos/commit/63160277d6fbcd5a262239e99d6f4512fd4941b8) fix: make ApplyDynamicConfig idempotent
- [`779ac74a0`](https://github.com/talos-systems/talos/commit/779ac74a08ae1384875e1db0e98ff346ba24fd03) fix: improve the drain function
- [`f24c81537`](https://github.com/talos-systems/talos/commit/f24c815373c0e249c80186939574e62ccc8c82e7) fix: correctly set service state in the resource
- [`589d01892`](https://github.com/talos-systems/talos/commit/589d01892cb3e80dda92364495513eafe4b4f0fa) fix: update the layout of the Disks API to match proxying requirements
- [`09369fedb`](https://github.com/talos-systems/talos/commit/09369fedba9535cd7105bc2e2b934063a807f47f) fix: stop and clean up installer container correctly
- [`1a491ee85`](https://github.com/talos-systems/talos/commit/1a491ee85e20469fefa42a0b29cdb29b2a03c1df) fix: sanitize volume name better in static pod extra volumes
- [`e355d4fae`](https://github.com/talos-systems/talos/commit/e355d4faedeaa3248c37e57de28754a93e50dd55) fix: redirect warnings in manifest apply k8s client
- [`41430e72d`](https://github.com/talos-systems/talos/commit/41430e72d22f1e9828ad5704b6ef0a6b1be99ce1) fix: handle case when kubelet serving certificates are issued
- [`7a6e0cd3e`](https://github.com/talos-systems/talos/commit/7a6e0cd3e51750821d4647de2bedd544dc127dff) fix: correctly escape extra args in kube-proxy manifest
- [`d2d5c72bb`](https://github.com/talos-systems/talos/commit/d2d5c72bb5454bcb09149e0ffe7e3d844aa98a2d) fix: skip empty manifest YAML sub-documents
- [`254e0e91e`](https://github.com/talos-systems/talos/commit/254e0e91e1b05c35878c39fc2eddde8002088609) fix: correctly unwrap responses for etcd commands
- [`292bc3968`](https://github.com/talos-systems/talos/commit/292bc396817328d6212e190e39e13f9c814c42b9) chore(ci): fix schedules in Drone pipelines
- [`162d8b6be`](https://github.com/talos-systems/talos/commit/162d8b6bef5fc155a7f337371ca1358c36c4ab89) fix: drop cri dependency on etcd
- [`9205870ee`](https://github.com/talos-systems/talos/commit/9205870ee6949196d4043912be2b1c8a0efe3246) fix: move versions to annotations in control plane static pods
- [`8d7a36cc0`](https://github.com/talos-systems/talos/commit/8d7a36cc0cc22cb26cb3bbbe656a3ec5e33b87fb) fix: find master node IPs correctly in health checks
- [`6791036cf`](https://github.com/talos-systems/talos/commit/6791036cfa94566f0f947f95effa8a43ddfd0f92) fix: add 3 seconds grub boot timeout
- [`ffe34ec10`](https://github.com/talos-systems/talos/commit/ffe34ec100b1a2e1969f15c0dc3c39e5e75ace2e) fix: don't use filename from URL when downloading manifest
- [`1111edfc7`](https://github.com/talos-systems/talos/commit/1111edfc7681f2634d43c061a0f9f5bcfe56db4e) fix: pass attributes when adding routes
- [`d99a016af`](https://github.com/talos-systems/talos/commit/d99a016af2382e6ba22877c2dcc87af610c0c1f3) fix: correct response structure for GenerateConfig API
- [`df0099036`](https://github.com/talos-systems/talos/commit/df0099036c4f47ef262d846dbe7db9ecdd16ead3) fix: correctly extract wrapped error messages
- [`1a32d55e4`](https://github.com/talos-systems/talos/commit/1a32d55e4053045b70922b40dd6f0c54770118df) fix: prevent crash in machined on apid service stop
- [`3aaa888f9`](https://github.com/talos-systems/talos/commit/3aaa888f9a91b84446db3b1fc2f57cfeae67968e) docs: fix typos
- [`85ae9f75e`](https://github.com/talos-systems/talos/commit/85ae9f75e91f7ac557ad1cef1ae9e49919decd8f) fix: wait for time sync before generating Kubernetes certificates
- [`b526c2cc3`](https://github.com/talos-systems/talos/commit/b526c2cc33bc5cf9adfcbe6ad994e6391d0a1869) fix: set proper hostname on docker nodes
- [`a07cfbd5a`](https://github.com/talos-systems/talos/commit/a07cfbd5a42318be189fd7a6c0fb1ab1707528dd) fix: mount kubelet secrets from system instead of ephemeral
- [`33de89ef9`](https://github.com/talos-systems/talos/commit/33de89ef90bd2c26014dfeea999eaf49b4c99733) fix: allow loading of empty config files
- [`757cc204e`](https://github.com/talos-systems/talos/commit/757cc204ecc434736d584441f45d2571f2f342ef) fix: prefer configured nameservers, fix DHCP6 in container
- [`5855b8d53`](https://github.com/talos-systems/talos/commit/5855b8d532def16b5bc49fa0c692d5c2fc8cc3f4) fix: refresh control plane endpoints on worker apids on schedule
- [`47c260e36`](https://github.com/talos-systems/talos/commit/47c260e365a3da294761eabc2a4611670228f2f3) fix: update DHCP client to use Request-Ack sequence after an Offer
- [`9947ec84d`](https://github.com/talos-systems/talos/commit/9947ec84d70b477e9173447bad59fce029f22fa4) fix: use hugetlbfs instead of none
- [`389349c02`](https://github.com/talos-systems/talos/commit/389349c02bf38ca4d8eca9a30aaf703d707db9d6) fix: use grpc load-balancing when connecting to trustd
- [`512c79e8d`](https://github.com/talos-systems/talos/commit/512c79e8d646f38699f7cb69e99d7a1643d86f8a) fix: lower memory usage a bit by disabling memory profiling
- [`1cded4d33`](https://github.com/talos-systems/talos/commit/1cded4d33ee5506ce7241ba828dcbbb550c88190) chore: fix import path for fsnotify
- [`064d33229`](https://github.com/talos-systems/talos/commit/064d33229879165a73656dcf59d50e385c814bfb) fix: don't probe disks in container mode
- [`1051d2ab6`](https://github.com/talos-systems/talos/commit/1051d2ab654c70a66c1370dd093e3a53a6a1128a) fix: prefix rendered Talos-owned static pod manifests
- [`7be3a8609`](https://github.com/talos-systems/talos/commit/7be3a860917323d7f5986c04d61c9b8681731186) fix: bump timeout for worker apid waiting for kubelet client config
- [`76a679443`](https://github.com/talos-systems/talos/commit/76a6794436c072150f27b7ab0a45ae738a1e8bd8) fix: kill all processes and umount all disk on reboot/shutdown
- [`18db20dbc`](https://github.com/talos-systems/talos/commit/18db20dbc2318647da2639b548a0101a85268420) fix: open blockdevices with exclusive flock for partitioning
- [`d515613bb`](https://github.com/talos-systems/talos/commit/d515613bb7862f15ef68da57cdde7130624dbc03) fix: list command unlimited recursion default behavior
- [`af5c34b34`](https://github.com/talos-systems/talos/commit/af5c34b340f1143abc848388eadad96834f16df5) fix: pick first interface valid hostname (vs. last one)
- [`d19486afa`](https://github.com/talos-systems/talos/commit/d19486afaa79cd8dbc223246ed8bb86a7dff9e12) fix: allow 'console' argument in kernel args to be always overridden
- [`5325a66e3`](https://github.com/talos-systems/talos/commit/5325a66e3e3bc4ae648e38ff60bfbf9a261caeea) fix: bring up bonded interfaces correctly on packet
- [`a8dd2ff30`](https://github.com/talos-systems/talos/commit/a8dd2ff30d36b248eb5789b9c9dc67df62970ee8) fix: checkpoint controller-manager and scheduler
- [`11229a018`](https://github.com/talos-systems/talos/commit/11229a0180c58655a8ab6f63fd12bd2b3405da9b) docs: fix latest docs
- [`6a0e652f0`](https://github.com/talos-systems/talos/commit/6a0e652f0c0ca7ccee58b8e7eaf5c0553963a201) fix: correctly transport gRPC errors from apid
- [`47fb7d26e`](https://github.com/talos-systems/talos/commit/47fb7d26e0a2887a524802788523ec5ff9ad3af6) fix: use SetAll instead of AppendAll when building kernel args
- [`b4ddfbfe9`](https://github.com/talos-systems/talos/commit/b4ddfbfe9bec8d4fc7e8e68a112b62e583860f23) fix: add more dependencies for bootstrap services
- [`73c81c501`](https://github.com/talos-systems/talos/commit/73c81c501e239f06df23731df21d53125f570fa7) fix: pass disk image flags to e2e-qemu cluster create command
- [`5e3b8ee09`](https://github.com/talos-systems/talos/commit/5e3b8ee099f8b3d2d2d37e507b7eb3a064894cd7) fix: ignore pods spun up from checkpoints in health checks
- [`e75bb27cf`](https://github.com/talos-systems/talos/commit/e75bb27cf4c3a828ac8a6e70603257dc075a49be) fix: leave etcd for staged upgrades
- [`f1964aab5`](https://github.com/talos-systems/talos/commit/f1964aab5314f9d8e1106f68611aec666463dd30) fix: ignore errors on stopping/removing pod sandboxes
- [`14b43068d`](https://github.com/talos-systems/talos/commit/14b43068d04673a143783fa0143d907b0d900c9b) docs: fix SBC docs to point to beta.0 instead of beta.1
- [`941556cff`](https://github.com/talos-systems/talos/commit/941556cffbcadcb4c3334d0da30c4e9077e91ab5) fix: use the correct console on Banana Pi M64
- [`e791e7dca`](https://github.com/talos-systems/talos/commit/e791e7dca95175671e058c9cc72e280b681b7bc1) fix: don't run LabelNodeAsMaster in two sequences
- [`cf75519`](https://github.com/talos-systems/crypto/commit/cf75519cab82bd1b128ae9b45107c6bb422bd96a) fix: function NewKeyPair should create certificate with proper subject
- [`bb3ad73`](https://github.com/talos-systems/go-blockdevice/commit/bb3ad73f69836acc2785ec659435e24a531359e7) fix: align partition start to physical sector size
- [`1cf7f25`](https://github.com/talos-systems/go-blockdevice/commit/1cf7f252c38cf11ef07723de2debc27d1da6b520) fix: properly handle no child processes error from cmd.Wait
- [`b8955a5`](https://github.com/talos-systems/os-runtime/commit/b8955a5475fe7b6c436757477c887ed7ef82eee7) fix: attach stack trace to panic error message
- [`98acf0d`](https://github.com/talos-systems/os-runtime/commit/98acf0d2d3321a088e05f2d12c4c0ca00cbe3de0) fix: preserve original YAML formatting in resource.Any

### 0.9.2

- [`cb82fb58c`](https://github.com/talos-systems/talos/commit/cb82fb58cea7247606d215c820d7816a30dfe58d) fix: zero out manifest contents before setting new value
- [`702661bca`](https://github.com/talos-systems/talos/commit/702661bcad4a7a6c0a2ccd980551e2430e894c46) fix: print task failure error immediately
- [`948ae7bac`](https://github.com/talos-systems/talos/commit/948ae7bac81adc5a4aba545f01d12d1ed3e949a8) fix: ignore EOF errors from Kubernetes API when converting control plane
- [`be149162b`](https://github.com/talos-systems/talos/commit/be149162bb5ceb3ac8e65f27043d4ac5c73aa1b6) fix: prevent panic in validate config if `machine.install` is missing
- [`a8cf70cf5`](https://github.com/talos-systems/talos/commit/a8cf70cf563e0a9de253299bf80cc52ff234d4e0) fix: allow `convert-k8s --remove-initialized-keys` with K8s cp is down
- [`41cf6c1c4`](https://github.com/talos-systems/talos/commit/41cf6c1c45d2ced55037ee920eb5f1c87d9ec86f) fix: get rid of data race in encoder and fix concurrent map access
- [`5772e7ff6`](https://github.com/talos-systems/talos/commit/5772e7ff6b5c28f015a8b48860240863776ba5bc) fix: resolve the issue with DHCP lease not being renewed
- [`c6f7c7f36`](https://github.com/talos-systems/talos/commit/c6f7c7f3643b0514fc2f085ad772317edc994585) fix: command `etcd remove-member` shouldn't remove etcd data directory
- [`26c924619`](https://github.com/talos-systems/talos/commit/26c9246197d88ae6a355a72d0edc9ecfda90b7de) fix: upgrade-k8s bug with empty config values and provision script
- [`9d3605361`](https://github.com/talos-systems/talos/commit/9d36053616a9976f82d90158cb834aa66ae9545b) fix: talosctl health should not check kube-proxy when it is disabled
- [`5bf28b8c8`](https://github.com/talos-systems/talos/commit/5bf28b8c811135241713c4d4da9f52eefb13904f) fix: properly format spec comments in the resources
- [`6d7b0efc6`](https://github.com/talos-systems/talos/commit/6d7b0efc6083cc458f406b9d3a62e42aef70a2f0) fix: don't touch any partitions on upgrade with --preserve
- [`96477d249`](https://github.com/talos-systems/talos/commit/96477d24920e35d27b076d1874729a4faf5b4737) chore: fix provision tests after changes to build-container
- [`67e0317b9`](https://github.com/talos-systems/talos/commit/67e0317b9d0ad5cbe167e150b9ea61e97f47bf15) fix: update output of `convert-k8s` command
- [`51f59f435`](https://github.com/talos-systems/talos/commit/51f59f435192e9d1ec976121a0ddd3cc8a1a4416) fix: move containerd CRI config files under `/var/`
- [`c2e353d6a`](https://github.com/talos-systems/talos/commit/c2e353d6afa38d8a3af533b10c9b4bdf0ef3412d) fix: do not print out help string if the parameters are correct
- [`49853fc2e`](https://github.com/talos-systems/talos/commit/49853fc2ecb846898d66d90fc76e6d875b775901) fix: mkdir source of the extra mounts for the kubelet
- [`e8e91d643`](https://github.com/talos-systems/talos/commit/e8e91d6434968bbcc52e832a4eb4ee87de09e228) fix: properly propagate nameservers to provisioned docker clusters
- [`81acadf34`](https://github.com/talos-systems/talos/commit/81acadf345d00a30f26cdc979dd06e7dd0086c7c) fix: ignore connection refused errors when updating/converting cp
- [`db3785b93`](https://github.com/talos-systems/talos/commit/db3785b9301b1ce7772ea90eace093f13ae45db7) fix: align partition start to the physical sector size
- [`df52c1358`](https://github.com/talos-systems/talos/commit/df52c135817639b9408ac34b81781ce8a6dcb1b5) chore: fix //nolint directives
- [`7e8f13652`](https://github.com/talos-systems/talos/commit/7e8f13652ce57797252804891952049c66c43f6e) chore: fix upgrade tests by bumping 0.9 to alpha.5
- [`044fb7708`](https://github.com/talos-systems/talos/commit/044fb7708cc7786e8620403e14f680b47a8e6907) fix: chmod etcd PKI path to fix virtual IP for upgrades with persistence
- [`8ffb55943`](https://github.com/talos-systems/talos/commit/8ffb55943c71a100c0b1fd53c5520b2cf3ec72b8) fix: ignore 'ENOENT' (no such file directory) on mount
- [`561f8aa15`](https://github.com/talos-systems/talos/commit/561f8aa15eb47f5a7f329ede2190748ca4ee8ee3) fix: move etcd to `cri` containerd runner
- [`31e56e63d`](https://github.com/talos-systems/talos/commit/31e56e63db24efba88a10d4b0c4190aeebbb125b) fix: update in-cluster kubeconfig validity to match other certs
- [`c2f7a4b6f`](https://github.com/talos-systems/talos/commit/c2f7a4b6f883870d1c94621a4f88520916f7647f) fix: add ApplyDynamicConfig call in the apply-config --immediate mode
- [`5ae315f49`](https://github.com/talos-systems/talos/commit/5ae315f493f6585b24cf2e55ef8ef009170c07ee) fix: set hdmi_safe=1 on Raspberry Pi for maximum HDMI compatibility
- [`c7ee23908`](https://github.com/talos-systems/talos/commit/c7ee2390877ef40883384ec6540bacc2dd9bd709) fix: show stopped/exited containers via CRI inspector
- [`63160277d`](https://github.com/talos-systems/talos/commit/63160277d6fbcd5a262239e99d6f4512fd4941b8) fix: make ApplyDynamicConfig idempotent
- [`779ac74a0`](https://github.com/talos-systems/talos/commit/779ac74a08ae1384875e1db0e98ff346ba24fd03) fix: improve the drain function
- [`f24c81537`](https://github.com/talos-systems/talos/commit/f24c815373c0e249c80186939574e62ccc8c82e7) fix: correctly set service state in the resource
- [`589d01892`](https://github.com/talos-systems/talos/commit/589d01892cb3e80dda92364495513eafe4b4f0fa) fix: update the layout of the Disks API to match proxying requirements
- [`09369fedb`](https://github.com/talos-systems/talos/commit/09369fedba9535cd7105bc2e2b934063a807f47f) fix: stop and clean up installer container correctly
- [`1a491ee85`](https://github.com/talos-systems/talos/commit/1a491ee85e20469fefa42a0b29cdb29b2a03c1df) fix: sanitize volume name better in static pod extra volumes
- [`e355d4fae`](https://github.com/talos-systems/talos/commit/e355d4faedeaa3248c37e57de28754a93e50dd55) fix: redirect warnings in manifest apply k8s client
- [`41430e72d`](https://github.com/talos-systems/talos/commit/41430e72d22f1e9828ad5704b6ef0a6b1be99ce1) fix: handle case when kubelet serving certificates are issued
- [`7a6e0cd3e`](https://github.com/talos-systems/talos/commit/7a6e0cd3e51750821d4647de2bedd544dc127dff) fix: correctly escape extra args in kube-proxy manifest
- [`d2d5c72bb`](https://github.com/talos-systems/talos/commit/d2d5c72bb5454bcb09149e0ffe7e3d844aa98a2d) fix: skip empty manifest YAML sub-documents
- [`254e0e91e`](https://github.com/talos-systems/talos/commit/254e0e91e1b05c35878c39fc2eddde8002088609) fix: correctly unwrap responses for etcd commands
- [`292bc3968`](https://github.com/talos-systems/talos/commit/292bc396817328d6212e190e39e13f9c814c42b9) chore(ci): fix schedules in Drone pipelines
- [`162d8b6be`](https://github.com/talos-systems/talos/commit/162d8b6bef5fc155a7f337371ca1358c36c4ab89) fix: drop cri dependency on etcd
- [`9205870ee`](https://github.com/talos-systems/talos/commit/9205870ee6949196d4043912be2b1c8a0efe3246) fix: move versions to annotations in control plane static pods
- [`8d7a36cc0`](https://github.com/talos-systems/talos/commit/8d7a36cc0cc22cb26cb3bbbe656a3ec5e33b87fb) fix: find master node IPs correctly in health checks
- [`6791036cf`](https://github.com/talos-systems/talos/commit/6791036cfa94566f0f947f95effa8a43ddfd0f92) fix: add 3 seconds grub boot timeout
- [`ffe34ec10`](https://github.com/talos-systems/talos/commit/ffe34ec100b1a2e1969f15c0dc3c39e5e75ace2e) fix: don't use filename from URL when downloading manifest
- [`1111edfc7`](https://github.com/talos-systems/talos/commit/1111edfc7681f2634d43c061a0f9f5bcfe56db4e) fix: pass attributes when adding routes
- [`d99a016af`](https://github.com/talos-systems/talos/commit/d99a016af2382e6ba22877c2dcc87af610c0c1f3) fix: correct response structure for GenerateConfig API
- [`df0099036`](https://github.com/talos-systems/talos/commit/df0099036c4f47ef262d846dbe7db9ecdd16ead3) fix: correctly extract wrapped error messages
- [`1a32d55e4`](https://github.com/talos-systems/talos/commit/1a32d55e4053045b70922b40dd6f0c54770118df) fix: prevent crash in machined on apid service stop
- [`3aaa888f9`](https://github.com/talos-systems/talos/commit/3aaa888f9a91b84446db3b1fc2f57cfeae67968e) docs: fix typos
- [`85ae9f75e`](https://github.com/talos-systems/talos/commit/85ae9f75e91f7ac557ad1cef1ae9e49919decd8f) fix: wait for time sync before generating Kubernetes certificates
- [`b526c2cc3`](https://github.com/talos-systems/talos/commit/b526c2cc33bc5cf9adfcbe6ad994e6391d0a1869) fix: set proper hostname on docker nodes
- [`a07cfbd5a`](https://github.com/talos-systems/talos/commit/a07cfbd5a42318be189fd7a6c0fb1ab1707528dd) fix: mount kubelet secrets from system instead of ephemeral
- [`33de89ef9`](https://github.com/talos-systems/talos/commit/33de89ef90bd2c26014dfeea999eaf49b4c99733) fix: allow loading of empty config files
- [`757cc204e`](https://github.com/talos-systems/talos/commit/757cc204ecc434736d584441f45d2571f2f342ef) fix: prefer configured nameservers, fix DHCP6 in container
- [`5855b8d53`](https://github.com/talos-systems/talos/commit/5855b8d532def16b5bc49fa0c692d5c2fc8cc3f4) fix: refresh control plane endpoints on worker apids on schedule
- [`47c260e36`](https://github.com/talos-systems/talos/commit/47c260e365a3da294761eabc2a4611670228f2f3) fix: update DHCP client to use Request-Ack sequence after an Offer
- [`9947ec84d`](https://github.com/talos-systems/talos/commit/9947ec84d70b477e9173447bad59fce029f22fa4) fix: use hugetlbfs instead of none
- [`389349c02`](https://github.com/talos-systems/talos/commit/389349c02bf38ca4d8eca9a30aaf703d707db9d6) fix: use grpc load-balancing when connecting to trustd
- [`512c79e8d`](https://github.com/talos-systems/talos/commit/512c79e8d646f38699f7cb69e99d7a1643d86f8a) fix: lower memory usage a bit by disabling memory profiling
- [`1cded4d33`](https://github.com/talos-systems/talos/commit/1cded4d33ee5506ce7241ba828dcbbb550c88190) chore: fix import path for fsnotify
- [`064d33229`](https://github.com/talos-systems/talos/commit/064d33229879165a73656dcf59d50e385c814bfb) fix: don't probe disks in container mode
- [`1051d2ab6`](https://github.com/talos-systems/talos/commit/1051d2ab654c70a66c1370dd093e3a53a6a1128a) fix: prefix rendered Talos-owned static pod manifests
- [`7be3a8609`](https://github.com/talos-systems/talos/commit/7be3a860917323d7f5986c04d61c9b8681731186) fix: bump timeout for worker apid waiting for kubelet client config
- [`76a679443`](https://github.com/talos-systems/talos/commit/76a6794436c072150f27b7ab0a45ae738a1e8bd8) fix: kill all processes and umount all disk on reboot/shutdown
- [`18db20dbc`](https://github.com/talos-systems/talos/commit/18db20dbc2318647da2639b548a0101a85268420) fix: open blockdevices with exclusive flock for partitioning
- [`d515613bb`](https://github.com/talos-systems/talos/commit/d515613bb7862f15ef68da57cdde7130624dbc03) fix: list command unlimited recursion default behavior
- [`af5c34b34`](https://github.com/talos-systems/talos/commit/af5c34b340f1143abc848388eadad96834f16df5) fix: pick first interface valid hostname (vs. last one)
- [`d19486afa`](https://github.com/talos-systems/talos/commit/d19486afaa79cd8dbc223246ed8bb86a7dff9e12) fix: allow 'console' argument in kernel args to be always overridden
- [`5325a66e3`](https://github.com/talos-systems/talos/commit/5325a66e3e3bc4ae648e38ff60bfbf9a261caeea) fix: bring up bonded interfaces correctly on packet
- [`a8dd2ff30`](https://github.com/talos-systems/talos/commit/a8dd2ff30d36b248eb5789b9c9dc67df62970ee8) fix: checkpoint controller-manager and scheduler
- [`11229a018`](https://github.com/talos-systems/talos/commit/11229a0180c58655a8ab6f63fd12bd2b3405da9b) docs: fix latest docs
- [`6a0e652f0`](https://github.com/talos-systems/talos/commit/6a0e652f0c0ca7ccee58b8e7eaf5c0553963a201) fix: correctly transport gRPC errors from apid
- [`47fb7d26e`](https://github.com/talos-systems/talos/commit/47fb7d26e0a2887a524802788523ec5ff9ad3af6) fix: use SetAll instead of AppendAll when building kernel args
- [`b4ddfbfe9`](https://github.com/talos-systems/talos/commit/b4ddfbfe9bec8d4fc7e8e68a112b62e583860f23) fix: add more dependencies for bootstrap services
- [`73c81c501`](https://github.com/talos-systems/talos/commit/73c81c501e239f06df23731df21d53125f570fa7) fix: pass disk image flags to e2e-qemu cluster create command
- [`5e3b8ee09`](https://github.com/talos-systems/talos/commit/5e3b8ee099f8b3d2d2d37e507b7eb3a064894cd7) fix: ignore pods spun up from checkpoints in health checks
- [`e75bb27cf`](https://github.com/talos-systems/talos/commit/e75bb27cf4c3a828ac8a6e70603257dc075a49be) fix: leave etcd for staged upgrades
- [`f1964aab5`](https://github.com/talos-systems/talos/commit/f1964aab5314f9d8e1106f68611aec666463dd30) fix: ignore errors on stopping/removing pod sandboxes
- [`14b43068d`](https://github.com/talos-systems/talos/commit/14b43068d04673a143783fa0143d907b0d900c9b) docs: fix SBC docs to point to beta.0 instead of beta.1
- [`941556cff`](https://github.com/talos-systems/talos/commit/941556cffbcadcb4c3334d0da30c4e9077e91ab5) fix: use the correct console on Banana Pi M64
- [`e791e7dca`](https://github.com/talos-systems/talos/commit/e791e7dca95175671e058c9cc72e280b681b7bc1) fix: don't run LabelNodeAsMaster in two sequences
- [`cf75519`](https://github.com/talos-systems/crypto/commit/cf75519cab82bd1b128ae9b45107c6bb422bd96a) fix: function NewKeyPair should create certificate with proper subject
- [`bb3ad73`](https://github.com/talos-systems/go-blockdevice/commit/bb3ad73f69836acc2785ec659435e24a531359e7) fix: align partition start to physical sector size
- [`1cf7f25`](https://github.com/talos-systems/go-blockdevice/commit/1cf7f252c38cf11ef07723de2debc27d1da6b520) fix: properly handle no child processes error from cmd.Wait
- [`b8955a5`](https://github.com/talos-systems/os-runtime/commit/b8955a5475fe7b6c436757477c887ed7ef82eee7) fix: attach stack trace to panic error message
- [`98acf0d`](https://github.com/talos-systems/os-runtime/commit/98acf0d2d3321a088e05f2d12c4c0ca00cbe3de0) fix: preserve original YAML formatting in resource.Any

### 0.9.3

- [`c7e3ccef2`](https://github.com/talos-systems/talos/commit/c7e3ccef22aceb11a0c72d08fccd21b04ba8b0e5) fix: check if OVF env is empty
- [`cb82fb58c`](https://github.com/talos-systems/talos/commit/cb82fb58cea7247606d215c820d7816a30dfe58d) fix: zero out manifest contents before setting new value
- [`702661bca`](https://github.com/talos-systems/talos/commit/702661bcad4a7a6c0a2ccd980551e2430e894c46) fix: print task failure error immediately
- [`948ae7bac`](https://github.com/talos-systems/talos/commit/948ae7bac81adc5a4aba545f01d12d1ed3e949a8) fix: ignore EOF errors from Kubernetes API when converting control plane
- [`be149162b`](https://github.com/talos-systems/talos/commit/be149162bb5ceb3ac8e65f27043d4ac5c73aa1b6) fix: prevent panic in validate config if `machine.install` is missing
- [`a8cf70cf5`](https://github.com/talos-systems/talos/commit/a8cf70cf563e0a9de253299bf80cc52ff234d4e0) fix: allow `convert-k8s --remove-initialized-keys` with K8s cp is down
- [`41cf6c1c4`](https://github.com/talos-systems/talos/commit/41cf6c1c45d2ced55037ee920eb5f1c87d9ec86f) fix: get rid of data race in encoder and fix concurrent map access
- [`5772e7ff6`](https://github.com/talos-systems/talos/commit/5772e7ff6b5c28f015a8b48860240863776ba5bc) fix: resolve the issue with DHCP lease not being renewed
- [`c6f7c7f36`](https://github.com/talos-systems/talos/commit/c6f7c7f3643b0514fc2f085ad772317edc994585) fix: command `etcd remove-member` shouldn't remove etcd data directory
- [`26c924619`](https://github.com/talos-systems/talos/commit/26c9246197d88ae6a355a72d0edc9ecfda90b7de) fix: upgrade-k8s bug with empty config values and provision script
- [`9d3605361`](https://github.com/talos-systems/talos/commit/9d36053616a9976f82d90158cb834aa66ae9545b) fix: talosctl health should not check kube-proxy when it is disabled
- [`5bf28b8c8`](https://github.com/talos-systems/talos/commit/5bf28b8c811135241713c4d4da9f52eefb13904f) fix: properly format spec comments in the resources
- [`6d7b0efc6`](https://github.com/talos-systems/talos/commit/6d7b0efc6083cc458f406b9d3a62e42aef70a2f0) fix: don't touch any partitions on upgrade with --preserve
- [`96477d249`](https://github.com/talos-systems/talos/commit/96477d24920e35d27b076d1874729a4faf5b4737) chore: fix provision tests after changes to build-container
- [`67e0317b9`](https://github.com/talos-systems/talos/commit/67e0317b9d0ad5cbe167e150b9ea61e97f47bf15) fix: update output of `convert-k8s` command
- [`51f59f435`](https://github.com/talos-systems/talos/commit/51f59f435192e9d1ec976121a0ddd3cc8a1a4416) fix: move containerd CRI config files under `/var/`
- [`c2e353d6a`](https://github.com/talos-systems/talos/commit/c2e353d6afa38d8a3af533b10c9b4bdf0ef3412d) fix: do not print out help string if the parameters are correct
- [`49853fc2e`](https://github.com/talos-systems/talos/commit/49853fc2ecb846898d66d90fc76e6d875b775901) fix: mkdir source of the extra mounts for the kubelet
- [`e8e91d643`](https://github.com/talos-systems/talos/commit/e8e91d6434968bbcc52e832a4eb4ee87de09e228) fix: properly propagate nameservers to provisioned docker clusters
- [`81acadf34`](https://github.com/talos-systems/talos/commit/81acadf345d00a30f26cdc979dd06e7dd0086c7c) fix: ignore connection refused errors when updating/converting cp
- [`db3785b93`](https://github.com/talos-systems/talos/commit/db3785b9301b1ce7772ea90eace093f13ae45db7) fix: align partition start to the physical sector size
- [`df52c1358`](https://github.com/talos-systems/talos/commit/df52c135817639b9408ac34b81781ce8a6dcb1b5) chore: fix //nolint directives
- [`7e8f13652`](https://github.com/talos-systems/talos/commit/7e8f13652ce57797252804891952049c66c43f6e) chore: fix upgrade tests by bumping 0.9 to alpha.5
- [`044fb7708`](https://github.com/talos-systems/talos/commit/044fb7708cc7786e8620403e14f680b47a8e6907) fix: chmod etcd PKI path to fix virtual IP for upgrades with persistence
- [`8ffb55943`](https://github.com/talos-systems/talos/commit/8ffb55943c71a100c0b1fd53c5520b2cf3ec72b8) fix: ignore 'ENOENT' (no such file directory) on mount
- [`561f8aa15`](https://github.com/talos-systems/talos/commit/561f8aa15eb47f5a7f329ede2190748ca4ee8ee3) fix: move etcd to `cri` containerd runner
- [`31e56e63d`](https://github.com/talos-systems/talos/commit/31e56e63db24efba88a10d4b0c4190aeebbb125b) fix: update in-cluster kubeconfig validity to match other certs
- [`c2f7a4b6f`](https://github.com/talos-systems/talos/commit/c2f7a4b6f883870d1c94621a4f88520916f7647f) fix: add ApplyDynamicConfig call in the apply-config --immediate mode
- [`5ae315f49`](https://github.com/talos-systems/talos/commit/5ae315f493f6585b24cf2e55ef8ef009170c07ee) fix: set hdmi_safe=1 on Raspberry Pi for maximum HDMI compatibility
- [`c7ee23908`](https://github.com/talos-systems/talos/commit/c7ee2390877ef40883384ec6540bacc2dd9bd709) fix: show stopped/exited containers via CRI inspector
- [`63160277d`](https://github.com/talos-systems/talos/commit/63160277d6fbcd5a262239e99d6f4512fd4941b8) fix: make ApplyDynamicConfig idempotent
- [`779ac74a0`](https://github.com/talos-systems/talos/commit/779ac74a08ae1384875e1db0e98ff346ba24fd03) fix: improve the drain function
- [`f24c81537`](https://github.com/talos-systems/talos/commit/f24c815373c0e249c80186939574e62ccc8c82e7) fix: correctly set service state in the resource
- [`589d01892`](https://github.com/talos-systems/talos/commit/589d01892cb3e80dda92364495513eafe4b4f0fa) fix: update the layout of the Disks API to match proxying requirements
- [`09369fedb`](https://github.com/talos-systems/talos/commit/09369fedba9535cd7105bc2e2b934063a807f47f) fix: stop and clean up installer container correctly
- [`1a491ee85`](https://github.com/talos-systems/talos/commit/1a491ee85e20469fefa42a0b29cdb29b2a03c1df) fix: sanitize volume name better in static pod extra volumes
- [`e355d4fae`](https://github.com/talos-systems/talos/commit/e355d4faedeaa3248c37e57de28754a93e50dd55) fix: redirect warnings in manifest apply k8s client
- [`41430e72d`](https://github.com/talos-systems/talos/commit/41430e72d22f1e9828ad5704b6ef0a6b1be99ce1) fix: handle case when kubelet serving certificates are issued
- [`7a6e0cd3e`](https://github.com/talos-systems/talos/commit/7a6e0cd3e51750821d4647de2bedd544dc127dff) fix: correctly escape extra args in kube-proxy manifest
- [`d2d5c72bb`](https://github.com/talos-systems/talos/commit/d2d5c72bb5454bcb09149e0ffe7e3d844aa98a2d) fix: skip empty manifest YAML sub-documents
- [`254e0e91e`](https://github.com/talos-systems/talos/commit/254e0e91e1b05c35878c39fc2eddde8002088609) fix: correctly unwrap responses for etcd commands
- [`292bc3968`](https://github.com/talos-systems/talos/commit/292bc396817328d6212e190e39e13f9c814c42b9) chore(ci): fix schedules in Drone pipelines
- [`162d8b6be`](https://github.com/talos-systems/talos/commit/162d8b6bef5fc155a7f337371ca1358c36c4ab89) fix: drop cri dependency on etcd
- [`9205870ee`](https://github.com/talos-systems/talos/commit/9205870ee6949196d4043912be2b1c8a0efe3246) fix: move versions to annotations in control plane static pods
- [`8d7a36cc0`](https://github.com/talos-systems/talos/commit/8d7a36cc0cc22cb26cb3bbbe656a3ec5e33b87fb) fix: find master node IPs correctly in health checks
- [`6791036cf`](https://github.com/talos-systems/talos/commit/6791036cfa94566f0f947f95effa8a43ddfd0f92) fix: add 3 seconds grub boot timeout
- [`ffe34ec10`](https://github.com/talos-systems/talos/commit/ffe34ec100b1a2e1969f15c0dc3c39e5e75ace2e) fix: don't use filename from URL when downloading manifest
- [`1111edfc7`](https://github.com/talos-systems/talos/commit/1111edfc7681f2634d43c061a0f9f5bcfe56db4e) fix: pass attributes when adding routes
- [`d99a016af`](https://github.com/talos-systems/talos/commit/d99a016af2382e6ba22877c2dcc87af610c0c1f3) fix: correct response structure for GenerateConfig API
- [`df0099036`](https://github.com/talos-systems/talos/commit/df0099036c4f47ef262d846dbe7db9ecdd16ead3) fix: correctly extract wrapped error messages
- [`1a32d55e4`](https://github.com/talos-systems/talos/commit/1a32d55e4053045b70922b40dd6f0c54770118df) fix: prevent crash in machined on apid service stop
- [`3aaa888f9`](https://github.com/talos-systems/talos/commit/3aaa888f9a91b84446db3b1fc2f57cfeae67968e) docs: fix typos
- [`85ae9f75e`](https://github.com/talos-systems/talos/commit/85ae9f75e91f7ac557ad1cef1ae9e49919decd8f) fix: wait for time sync before generating Kubernetes certificates
- [`b526c2cc3`](https://github.com/talos-systems/talos/commit/b526c2cc33bc5cf9adfcbe6ad994e6391d0a1869) fix: set proper hostname on docker nodes
- [`a07cfbd5a`](https://github.com/talos-systems/talos/commit/a07cfbd5a42318be189fd7a6c0fb1ab1707528dd) fix: mount kubelet secrets from system instead of ephemeral
- [`33de89ef9`](https://github.com/talos-systems/talos/commit/33de89ef90bd2c26014dfeea999eaf49b4c99733) fix: allow loading of empty config files
- [`757cc204e`](https://github.com/talos-systems/talos/commit/757cc204ecc434736d584441f45d2571f2f342ef) fix: prefer configured nameservers, fix DHCP6 in container
- [`5855b8d53`](https://github.com/talos-systems/talos/commit/5855b8d532def16b5bc49fa0c692d5c2fc8cc3f4) fix: refresh control plane endpoints on worker apids on schedule
- [`47c260e36`](https://github.com/talos-systems/talos/commit/47c260e365a3da294761eabc2a4611670228f2f3) fix: update DHCP client to use Request-Ack sequence after an Offer
- [`9947ec84d`](https://github.com/talos-systems/talos/commit/9947ec84d70b477e9173447bad59fce029f22fa4) fix: use hugetlbfs instead of none
- [`389349c02`](https://github.com/talos-systems/talos/commit/389349c02bf38ca4d8eca9a30aaf703d707db9d6) fix: use grpc load-balancing when connecting to trustd
- [`512c79e8d`](https://github.com/talos-systems/talos/commit/512c79e8d646f38699f7cb69e99d7a1643d86f8a) fix: lower memory usage a bit by disabling memory profiling
- [`1cded4d33`](https://github.com/talos-systems/talos/commit/1cded4d33ee5506ce7241ba828dcbbb550c88190) chore: fix import path for fsnotify
- [`064d33229`](https://github.com/talos-systems/talos/commit/064d33229879165a73656dcf59d50e385c814bfb) fix: don't probe disks in container mode
- [`1051d2ab6`](https://github.com/talos-systems/talos/commit/1051d2ab654c70a66c1370dd093e3a53a6a1128a) fix: prefix rendered Talos-owned static pod manifests
- [`7be3a8609`](https://github.com/talos-systems/talos/commit/7be3a860917323d7f5986c04d61c9b8681731186) fix: bump timeout for worker apid waiting for kubelet client config
- [`76a679443`](https://github.com/talos-systems/talos/commit/76a6794436c072150f27b7ab0a45ae738a1e8bd8) fix: kill all processes and umount all disk on reboot/shutdown
- [`18db20dbc`](https://github.com/talos-systems/talos/commit/18db20dbc2318647da2639b548a0101a85268420) fix: open blockdevices with exclusive flock for partitioning
- [`d515613bb`](https://github.com/talos-systems/talos/commit/d515613bb7862f15ef68da57cdde7130624dbc03) fix: list command unlimited recursion default behavior
- [`af5c34b34`](https://github.com/talos-systems/talos/commit/af5c34b340f1143abc848388eadad96834f16df5) fix: pick first interface valid hostname (vs. last one)
- [`d19486afa`](https://github.com/talos-systems/talos/commit/d19486afaa79cd8dbc223246ed8bb86a7dff9e12) fix: allow 'console' argument in kernel args to be always overridden
- [`5325a66e3`](https://github.com/talos-systems/talos/commit/5325a66e3e3bc4ae648e38ff60bfbf9a261caeea) fix: bring up bonded interfaces correctly on packet
- [`a8dd2ff30`](https://github.com/talos-systems/talos/commit/a8dd2ff30d36b248eb5789b9c9dc67df62970ee8) fix: checkpoint controller-manager and scheduler
- [`11229a018`](https://github.com/talos-systems/talos/commit/11229a0180c58655a8ab6f63fd12bd2b3405da9b) docs: fix latest docs
- [`6a0e652f0`](https://github.com/talos-systems/talos/commit/6a0e652f0c0ca7ccee58b8e7eaf5c0553963a201) fix: correctly transport gRPC errors from apid
- [`47fb7d26e`](https://github.com/talos-systems/talos/commit/47fb7d26e0a2887a524802788523ec5ff9ad3af6) fix: use SetAll instead of AppendAll when building kernel args
- [`b4ddfbfe9`](https://github.com/talos-systems/talos/commit/b4ddfbfe9bec8d4fc7e8e68a112b62e583860f23) fix: add more dependencies for bootstrap services
- [`73c81c501`](https://github.com/talos-systems/talos/commit/73c81c501e239f06df23731df21d53125f570fa7) fix: pass disk image flags to e2e-qemu cluster create command
- [`5e3b8ee09`](https://github.com/talos-systems/talos/commit/5e3b8ee099f8b3d2d2d37e507b7eb3a064894cd7) fix: ignore pods spun up from checkpoints in health checks
- [`e75bb27cf`](https://github.com/talos-systems/talos/commit/e75bb27cf4c3a828ac8a6e70603257dc075a49be) fix: leave etcd for staged upgrades
- [`f1964aab5`](https://github.com/talos-systems/talos/commit/f1964aab5314f9d8e1106f68611aec666463dd30) fix: ignore errors on stopping/removing pod sandboxes
- [`14b43068d`](https://github.com/talos-systems/talos/commit/14b43068d04673a143783fa0143d907b0d900c9b) docs: fix SBC docs to point to beta.0 instead of beta.1
- [`941556cff`](https://github.com/talos-systems/talos/commit/941556cffbcadcb4c3334d0da30c4e9077e91ab5) fix: use the correct console on Banana Pi M64
- [`e791e7dca`](https://github.com/talos-systems/talos/commit/e791e7dca95175671e058c9cc72e280b681b7bc1) fix: don't run LabelNodeAsMaster in two sequences
- [`cf75519`](https://github.com/talos-systems/crypto/commit/cf75519cab82bd1b128ae9b45107c6bb422bd96a) fix: function NewKeyPair should create certificate with proper subject
- [`bb3ad73`](https://github.com/talos-systems/go-blockdevice/commit/bb3ad73f69836acc2785ec659435e24a531359e7) fix: align partition start to physical sector size
- [`1cf7f25`](https://github.com/talos-systems/go-blockdevice/commit/1cf7f252c38cf11ef07723de2debc27d1da6b520) fix: properly handle no child processes error from cmd.Wait
- [`b8955a5`](https://github.com/talos-systems/os-runtime/commit/b8955a5475fe7b6c436757477c887ed7ef82eee7) fix: attach stack trace to panic error message
- [`98acf0d`](https://github.com/talos-systems/os-runtime/commit/98acf0d2d3321a088e05f2d12c4c0ca00cbe3de0) fix: preserve original YAML formatting in resource.Any


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.9.3**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `siderolabs/talos`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/talos.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
