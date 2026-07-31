---
id: TROUBLE-CILIUM_1_9_DEFECTS
type: troubleshooting
title: "cilium 1.9: defects fixed in the 1.9 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=1.9.0 <1.10.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - cilium 1.9 known issues
  - cilium 1.9 fixed in
  - is this cilium bug already fixed
tags:
  - troubleshooting
  - upgrade
  - cilium
sources:
  - type: docs
    path: cilium/cilium release notes for the 1.9 line — bug-fix entries
    url: https://github.com/cilium/cilium/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# cilium 1.9: defects fixed in the 1.9 line

## Summary

**214 defects** the project fixed across **17 releases** of the 1.9 line, from 1.9.0 to
1.9.18. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 1.9.0

- fix(3891): mirror parent pod labels to cilium endpoints (#12406, @fristonio)
- fix(9966): fix creation of multiple KVStore watchers for CNPs and CCNPs (#12323, @fristonio)
- agent: fix panic when clustermesh not set and cluster-id is non-zero (#12944, @ArthurChiao)
- bpf: Fix --force-local-policy-eval-at-source=false (Backport PR #13812, Upstream PR #13769, @joestringer)
- bpf: fix disable PolicyVerdictNotification broken (Backport PR #13941, Upstream PR #13921, @ArthurChiao)
- Fix bug in cluster-pool IPAM mode where the user is never alerted of a node CIDR allocation failure (Backport PR #13957, Upstream PR #13916, @christarazi)
- Fix bug where Cilium leaks a goroutine when an endpoint is deleted. This leak, if left running in a high pod churn environment, can cause Cilium to exceed its memory usage and get OOM killed. (Backport PR #13720, Upstream PR #13683, @christarazi)
- Fix bug where events cannot be enqueued during endpoint restoration (#13608, @christarazi)
- Fix dynamic NAT table size calculation if CT map sizes are configured statically. (Backport PR #13903, Upstream PR #13844, @tklauser)
- Fix garbage collection of CEPs - delete them in tranches and not every 5 minutes. (Backport PR #13751, Upstream PR #13728, @aanm)
- Fix panic on cilium-agent startup when restoring LB source range maps (Backport PR #13856, Upstream PR #13842, @aanm)
- Fix potential bug in ENI IPAM when multiple updates at the same time are performed to the a CiliumNode resource (Backport PR #13688, Upstream PR #13612, @christarazi)
- Fixed installation instructions for K3s and Kubernetes Network Policy enforcement (Backport PR #13812, Upstream PR #13783, @aanm)
- Fixes panic when setting up encryption with azure IPAM (#13593, @aanm)
- go.mod: update cilium/ipam library with bug fixes (Backport PR #13856, Upstream PR #13810, @aanm)
- hubble: Fix reply state unknown being interpreted as false (Backport PR #13786, Upstream PR #13750, @gandro)
- k8s/watchers: fix data race in (*K8sWatcher).addK8sServiceV1 (Backport PR #13688, Upstream PR #13604, @tklauser)
- lock: fix data race in (*SemaphoredMutexSuite).TestParallelism() (#13570, @tklauser)
- ci/gke: Fix Hubble Relay on GKE (#13025, @gandro)
- Fix focus in jenkinsfile (Backport PR #13812, Upstream PR #13791, @nebril)
- Fix overall races in the Cilium code base (#12789, @aanm)
- Fix upgrade testing for v1.9-dev (#12309, @aanm)
- Fixes LRP service deletion/restoration and adds e2e tests for LRP. (#13360, @Weil0ng)
- images: Fix handing of dev suffix when tag is used (cilium/image-tools#76) (Backport PR #13688, Upstream PR #13639, @errordeveloper)
- images: Fix handling of git tags (#13602, @errordeveloper)
- test/bpf: Fix XDP loading in verifier-test.sh (Backport PR #13941, Upstream PR #13927, @pchaigno)
- travis: Fix probes_test failure on Arm64 (#12335, @Jianlin-lv)
- add_vagrant_box.sh: fix and document the script (#12264, @qmonnet)
- allocator/podcidr: fix race conditions in tests (#13567, @aanm)
- Avoid loops with local-redirect service translation (#13287, @aditighag)
- bpf: fix session affinity timeout test flake (Backport PR #13903, Upstream PR #13859, @fristonio)
- bpf: fix up lrp for v4-in-v6 sockets (Backport PR #13688, Upstream PR #13638, @borkmann)
- bpf: redirect fixes and follow-ups (Backport PR #13688, Upstream PR #13646, @borkmann)
- bpf: redirect_neigh signature fix (Backport PR #13786, Upstream PR #13747, @borkmann)
- certloader: Fix reload on K8s Secret/ConfigMap update (Backport PR #13751, Upstream PR #13636, @gandro)
- cocci: Fix false positive in null.cocci (#12422, @pchaigno)
- CODEOWNERS: fix owner assignment for hubble related helm charts (#13540, @Rolinh)
- connectivity-check: Fix YAML inconsistency (#13073, @joestringer)
- connectivity-check: Fix YAML inconsistency (#13075, @sayboras)
- contrib/checkpr.sh: fix job name (#12236, @qmonnet)
- contrib: Use fixed string search in grep (#12634, @christarazi)
- Correct help string for kubernetes_events_received_total metric (#12316, @ungureanuvladvictor)
- docs/gettingstarted: Fix minor issues in Metrics guide (Backport PR #13720, Upstream PR #13668, @twpayne)
- Documentation: Fix Loadbalancer Guide for Clustermesh (Backport PR #13856, Upstream PR #13822, @nathanjsweet)
- examples: Fix grafana and prometheus (Backport PR #13903, Upstream PR #13860, @nathanjsweet)
- Fix bug in EKS environments where Cilium agents never become ready due to the CiliumNode CRD disallowing updates (#13195, @christarazi)
- Fix controller-tools module (#13055, @christarazi)
- Fix deadlock on eventqueue when it's being drained when endpoints are being restored (Backport PR #13751, Upstream PR #13716, @christarazi)
- Fix extraction of manifest for OpenShift (#13598, @errordeveloper)
- Fix Helm upgrade compatibility (Backport PR #13720, Upstream PR #13691, @joestringer)
- Fix install/ version update scripts (Backport PR #13861, Upstream PR #13858, @joestringer)
- Fix install/kubernetes update-versions make target (#13523, @joestringer)
- Fix render-docs build again (#13158, @joestringer)
- Fix some word errors in the annotations (#12414, @TrevorTaoARM)
- Fix Spelling Errors for endpoint pkg (#12394, @TrevorTaoARM)
- fix: fix missing arguments declaration funcs in pkg/node/address_darwin (#13481, @genbit)
- Fixed encryption + VXLAN example, added encryption + Direct Routing example for GKE. (Backport PR #13903, Upstream PR #13806, @ti-mo)
- Fixes for troubleshooting guide re. Hubble/Hubble Relay (Backport PR #13688, Upstream PR #13644, @tklauser)
- helm: Fix format issue for logOptions in ConfigMap (Backport PR #13903, Upstream PR #13837, @sayboras)
- hubble/parser: Fix data race in L7 parser (#13467, @gandro)
- hubble/relay: fix warning about missing config file (#13110, @kAworu)
- hubble: Fix dropped flows not showing up in Hubble UI (Backport PR #13812, Upstream PR #13796, @gandro)
- install/kubernetes: Fix experimental-install.yaml for Hubble (Backport PR #13812, Upstream PR #13782, @gandro)
- k8s: Fix parsing of CCNPs (#12851, @pchaigno)
- make: Fix dev-docker-image make target (Backport PR #13968, Upstream PR #13956, @joestringer)
- Misc: fix up spelling mistake (#12488, @Jianlin-lv)
- operator: Fix CEP owner type (Backport PR #13688, Upstream PR #13550, @jrajahalme)
- pkg/azure/ipam: fix data race in (*Node).PopulateStatusFields (#13581, @tklauser)
- pkg/envoy: Fix Envoy MySQL test (#12790, @christarazi)
- pkg/idpool: fix test for race detector (#13562, @aanm)
- pkg/kvstore: fix race in etcd initialization (Backport PR #13812, Upstream PR #13780, @aanm)
- pkg/redirectpolicy Fix frontend-backend ipv6 mapping (#13494, @aditighag)
- Prevent leak of AWS-related environment variables in `cilium-operator` deployment definition when deploying the operator in Azure mode. (#12411, @ungureanuvladvictor)
- README: Fix the versions listing (#13365, @joestringer)
- test/vagrant: Fix NFS setup for test VMs (#13527, @pchaigno)
- Various fixes for NodePort XDP kube-proxy free guide (Backport PR #13751, Upstream PR #13674, @tklauser)

### 1.9.1

- helm: fix usage of `hostPath` and add `hostPathType` in `extraHostPathMounts` (Backport PR #14212, Upstream PR #14134, @errordeveloper)
- Fix bug where Cilium on smaller instance types cannot allocate IPs (Backport PR #14060, Upstream PR #13865, @christarazi)
- Fix etcd's auth token invalid after watch reconnects (Backport PR #14270, Upstream PR #14238, @aanm)
- Fixed Goroutine leak for unresponded ARP pings. (Backport PR #14246, Upstream PR #14222, @jrajahalme)
- metricsmap: fix Prometheus exporter (Backport PR #14270, Upstream PR #14220, @jibi)
- daemon: Fix netns usage in kpr privileged unit tests (Backport PR #14212, Upstream PR #14171, @brb)
- bpf: Fix IS_BPF_HOST macro (Backport PR #14270, Upstream PR #14255, @pchaigno)
- bpf: Fix program size issue with host firewall in IPv4-only mode (Backport PR #14246, Upstream PR #14232, @pchaigno)
- cilium: fix redirect limits on multi dev case (Backport PR #14060, Upstream PR #13884, @borkmann)
- fqdn: Fix confusion of ToFQDNs vs. DNS rules. (Backport PR #14088, Upstream PR #14012, @jrajahalme)
- fqdn: Fix unit test (Backport PR #14116, Upstream PR #14085, @jrajahalme)
- helm/hubble-relay: fixed indentation error (Backport PR #14088, Upstream PR #14029, @PranaviRoy)
- helm/hubble-ui: fixed ingress configuration on EKS clusters (Backport PR #14060, Upstream PR #14023, @mvisonneau)
- helm: Fix description for clustermesh (Backport PR #14212, Upstream PR #14163, @joestringer)
- node: Fix ineffectual assignment (Backport PR #14270, Upstream PR #14256, @brb)
- Fix potential panic in Hubble when applying time range on non-flow events, e.g. LostEvent. (#14197, @tklauser)

### 1.9.2

- bpf: fix misconfigured nat to 0.0.0.0 on !masquerade config (Backport PR #14613, Upstream PR #14596, @borkmann)
- cilium, gops: remap to fixed port to avoid collision with nodeport range (Backport PR #14419, Upstream PR #14329, @borkmann)
- Fix BPF verifier rejection with IPv6 prefilter (Backport PR #14538, Upstream PR #14447, @pchaigno)
- Fix bug where CCNPs are not validated properly in preflight (Backport PR #14613, Upstream PR #14557, @christarazi)
- Fix bug where Cilium would constantly regenerate endpoints in environments with etcd and Linux 4.15 or below. (Backport PR #14405, Upstream PR #14300, @dctrwatson)
- Fix CIDR rule bug potentially dropping allowed traffic or allowing denied traffic for deny policies (beta feature) when using ExceptCIDRs expressions. (Backport PR #14613, Upstream PR #14516, @jrajahalme)
- Fix clustermesh-apiserver dependencies on pkg/option (Backport PR #14613, Upstream PR #14577, @tgraf)
- Fix missing packet mark mask that can cause policy deny drops in IPSec configuration. (Backport PR #14419, Upstream PR #14381, @pchaigno)
- Fix possible overflow in values presented in the `k8s_event_lag_seconds` metric. (Backport PR #14405, Upstream PR #14313, @aanm)
- Fix potential nil pointer exception for an invalid CCNP in the Cilium Operator (Backport PR #14405, Upstream PR #14375, @aanm)
- Fix potential panic when closing etcd connection on error (Backport PR #14644, Upstream PR #14623, @aanm)
- Fix rare crash on startup when kubernetes initialization occurs before IP address configuration (Backport PR #14405, Upstream PR #14299, @joestringer)
- helm: Fix preflight check resource quota conflict (Backport PR #14308, Upstream PR #14295, @gandro)
- Fix bug Cilium hangs with kvstore configured (#14629, @aanm)
- helm: fix TLS cert server name for cluster names containing dots (Backport PR #14538, Upstream PR #14413, @kaworu)
- helm: fix TLS cert server name for cluster names containing dots with certgen (Backport PR #14538, Upstream PR #14416, @kaworu)
- microk8s: fix add-on-command for enabling cilium (Backport PR #14405, Upstream PR #14325, @brandshaide)
- pkg/datapath: fix arp ping handling (Backport PR #14613, Upstream PR #14501, @aanm)
- pkg/node: fix concurrent access of entry node (Backport PR #14613, Upstream PR #14591, @aanm)

### 1.9.4

- cilium-cni: Fix error handling for bad netns (Backport PR #14783, Upstream PR #14645, @joestringer)
- Fix a route MTU issue where pods cannot receive large packets from outside the cluster when the sender sets the "don't fragment" (DF) bit. (Backport PR #14783, Upstream PR #14679, @aditighag)
- Fix bug where Cilium did not respect `--bpf-lb-map-max` and wouldn't update the maximum size of BPF LB maps (Backport PR #14798, Upstream PR #14607, @christarazi)
- Fix missing loopback CNI plugin in multi-arch images (Backport PR #14839, Upstream PR #14828, @aanm)
- node-neigh: Fix node removal and invalid neigh entry due to buggy arping response correlation (Backport PR #14839, Upstream PR #14709, @brb)
- routing: Fix route collisions in AWS ENI (Backport PR #14846, Upstream PR #14269, @christarazi)
- [v1.9] release: Fix script to check presence of docker images (#14780, @joestringer)
- Fix wrong url (Backport PR #14839, Upstream PR #14818, @manuelbuil)
- backport 1.9: vendor: Bump github.com/cilium/arping to fix correlation bug (#14733, @brb)

### 1.9.5

- helm: Fix and add missing podLabels (Backport PR #15104, Upstream PR #14943, @Subreptivus)
- [1.9] doc: Fix masquerade option in AKS/Azure guides (#15245, @tgraf)
- Avoid an empty instanceID on EC2 (Backport PR #15047, Upstream PR #15012, @kkourt)
- bpf: Fix bpf masquerade issue when host connecting to remote pod (Backport PR #15243, Upstream PR #15206, @borkmann)
- cilium: encryption fix, ipv4-pod-subnets without encryptnode fails (Backport PR #15164, Upstream PR #14999, @jrfastab)
- cilium: encryption, fixes for ENI & Azure mode with shared podIPs and networkIPs (Backport PR #15164, Upstream PR #15048, @jrfastab)
- Fix a bug that affects connectivity to NodePort service via ExternalIP of the local k8s node. (Backport PR #14961, Upstream PR #14793, @AnishShah)
- Fix bug where PolicyAuditMode could not be changed at runtime if it was enabled at startup (Backport PR #15243, Upstream PR #15218, @ArthurChiao)
- Fix connectivity to externalTrafficPolicy=Local services when using the host firewall with kube-proxy (Backport PR #14961, Upstream PR #14756, @pchaigno)
- Fix ENI compatibility regression between 1.7 <-> 1.8 (Backport PR #15006, Upstream PR #14991, @tgraf)
- Fix failing `bpf-map-sync-cilium_snat_v{4,6}_external` controllers when BPF NodePort is disabled (Backport PR #15298, Upstream PR #15175, @pchaigno)
- Fix ICMP Echo ID placement in CT maps (#15274, @brb)
- Fix ipsec+vxlan bug where egressing packets would bypass masquerading on their way to remote nodes (Backport PR #14961, Upstream PR #14611, @jrfastab)
- Fix memory leak on stable policy identity churn. (Backport PR #15047, Upstream PR #15042, @jrajahalme)
- Fix possible deadlock when querying network interfaces for arping (#15227, @brb)
- Fix potential panic on clustermesh environments (Backport PR #15164, Upstream PR #15107, @aanm)
- Fix remote pod connectivity through VIP in tunneling mode with kube-proxy and per-endpoint routes. Fix IPv6 connectivity to BPF HostPort when kube-proxy is installed (Backport PR #14961, Upstream PR #14675, @pchaigno)
- iptables: Fix incorrect SNAT bypass with endpoint routes and tunneling (Backport PR #14961, Upstream PR #14913, @pchaigno)
- add GH action to push hot fix images into -dev repositories (#15062, @aanm)
- Fix BPF map handling on upgrade when disabling the preallocation of BPF maps (Backport PR #15099, Upstream PR #14853, @christarazi)

### 1.9.6

- cilium: Fix EKS encryption panic and reinit path and add workflows test (Backport PR #15726, Upstream PR #15669, @jrfastab)
- Fix a bug that was causing Azure IPAM to not work when ApplicationSecurityGroups were attached to IPConfigurations of a NIC. (Backport PR #15331, Upstream PR #15194, @AnishShah)
- Fix a bug that was causing Azure IPAM with multiple pod subnets to not work. (Backport PR #15331, Upstream PR #15182, @AnishShah)
- Fix bug where `enable-endpoint-routes` change required all pods to restart to take effect (Backport PR #15399, Upstream PR #15228, @pchaigno)
- Fix bug where any non-leader Operator in HA mode would crash updating CRDs (Backport PR #15588, Upstream PR #15544, @christarazi)
- Fix ethtool issues (Backport PR #15673, Upstream PR #15622, @tklauser)
- ipam: Fix ENI routing for secondary CIDRs (Backport PR #15331, Upstream PR #15303, @gandro)
- node: Fix CIDR comparison when updating routes (Backport PR #15331, Upstream PR #15263, @brb)
- contrib: fix remote overriding (Backport PR #15399, Upstream PR #15328, @kaworu)
- Documentation: fix key rotation command in encryption guide (Backport PR #15399, Upstream PR #15365, @mauriciovasquezbernal)
- Fix BPF_JMP_MAP_ID on tail call toy example. (Backport PR #15588, Upstream PR #15576, @yiannisy)
- install/kubernetes: Fix incorrect commands for digest generation (Backport PR #15312, Upstream PR #15311, @christarazi)
- ipam: Fix empty interface number in Azure (Backport PR #15597, Upstream PR #15533, @christarazi)
- ipsec: Fix routing CIDR iteration on EKS (Backport PR #15726, Upstream PR #15645, @gandro)

### 1.9.7

- bpf: Fix defines in policy.h (Backport PR #15830, Upstream PR #15763, @pchaigno)
- bpf: fix map_array_get_16 backend retrieval (Backport PR #15830, Upstream PR #15808, @borkmann)
- cilium: Encryption EKS 4.14 kernel (default) fixes (Backport PR #16048, Upstream PR #15867, @jrfastab)
- eni: Fix Cilium overallocating network interfaces (Backport PR #16035, Upstream PR #15911, @gandro)
- Fix an issue where packets are dropped when a pod connects to itself via a service clusterIP. (Backport PR #15709, Upstream PR #15321, @aditighag)
- Fix aws-cni integration where pods were not being scheduled (Backport PR #16048, Upstream PR #15915, @aanm)
- Fix bug where L7 ingress policies with IPsec dropped traffic in tunneling mode (Backport PR #16114, Upstream PR #16057, @christarazi)
- Fix channel panic from ipcache kvstore reconnect (Backport PR #15830, Upstream PR #15668, @jomenxiao)
- Fix panic when accounting for certain metrics in BPF map operations (#15866, @aanm)
- Fix the initialization of host endpoint labels (Backport PR #15837, Upstream PR #15780, @pchaigno)
- kvstore/etcd: fix etcd rate limit (QPS) not working (Backport PR #15830, Upstream PR #15742, @ArthurChiao)
- [v1.9] Fix image digest preparation for release commits (#15817, @joestringer)
- bwm: queue mapping & cong fixes (Backport PR #16048, Upstream PR #15964, @borkmann)
- daemon/cmd: fix Cilium version status output (Backport PR #15830, Upstream PR #15649, @aanm)
- daemon: Fix the init of the endpoints' datapath config (Backport PR #15830, Upstream PR #15785, @pchaigno)

### 1.9.8

- Fixed bug causing policy realization being skipped in some scenarios with endpoint identity churn. (Backport PR #16339, Upstream PR #16271, @jrajahalme)
- node-neigh: Fix unit test flake (Backport PR #16224, Upstream PR #16072, @brb)

### 1.9.9

- Fixes connectivity issues when kube-proxy replacement is enabled, caused by ineffective socket based load balancing (aka host reachable services) in the private cgroup namespace mode of container runtimes (e.g., docker cgroupv2 configuration). (Backport PR #16676, Upstream PR #16259, @aditighag)
- bpf: fix hw\_csum issue for icmp probe packets (Backport PR #16615, Upstream PR #16604, @borkmann)
- bpf: fix iptables masquerading for node -> remote pod traffic (Backport PR #16781, Upstream PR #16136, @jibi)
- daemon, node: Fix faulty router IP restoration logic (Backport PR #16569, Upstream PR #16672, @christarazi)
- Envoy configuration with `--proxy-prometheus-port` is fixed. (Backport PR #16903, Upstream PR #16834, @jrajahalme)
- Fix 5.10+ complexity issue with `kubeProxyReplacement=disabled` (Backport PR #16568, Upstream PR #16084, @pchaigno)
- Fix bug where Cilium allocates a new router (`cilium_host`) IP upon node reboot, breaking connectivity especially with IPsec (Backport PR #16569, Upstream PR #16307, @christarazi)
- ipsec: Fix logging of SPI after key rotations (Backport PR #16615, Upstream PR #16557, @pchaigno)
- pkg/option: Fix default assignment of EnableWellKnownIdentities (Backport PR #16615, Upstream PR #16434, @mauriciovasquezbernal)
- Potential deadlock in pod identity updates has been fixed. (Backport PR #16903, Upstream PRs #16529, #16769, #16801, @jrajahalme)
- Fix and add more commands in CI sysdumps (Backport PR #16779, Upstream PR #16721, @aanm)
- node-neigh: Fix concurrent arping update unit test flake (Backport PR #16615, Upstream PR #16578, @brb)
- node: fix arpping test (Backport PR #16568, Upstream PR #16432, @jibi)
- Fix flag in minikube guide (#16347, @aditighag)
- k8s: Fix logging (Backport PR #16615, Upstream PR #16530, @jrajahalme)

### 1.9.10

- Fix a crash where user specifies incorrect service name in a local redirect policy config, or policy selected service is added after the policy is added. (Backport PR #17175, Upstream PR #16216, @aditighag)
- Fix Linux slave interface detection (Backport PR #17175, Upstream PR #17189, @pchaigno)
- routing: Fix incorrect interface selection for egress pod routes (Backport PR #17175, Upstream PR #17169, @pchaigno)
- hubble/relay: Fix close of closed channel in unit test (Backport PR #16994, Upstream PR #16958, @gandro)
- github: fix GH workflows to handle push events to stable branches (#16980, @aanm)

### 1.9.11

- Fix bug where timers used for retries sometimes fired immediately (Backport PR #17398, Upstream PR #16955, @gandro)
- Fix transient policy deny during agent restart (Backport PR #17390, Upstream PR #17115, @jaffcheng)
- [v1.9] fix MLH config trigger (#17422, @nbusseneau)

### 1.9.12

- bug/pkg/health: Fix Nil Address Issue in Node Update Mechanism (Backport PR #17835, Upstream PR #17667, @nathanjsweet)
- bugtool: fix data race occurring when running commands (Backport PR #18025, Upstream PR #17916, @rolinh)
- bugtool: fix IP route debug gathering commands (Backport PR #18070, Upstream PR #18059, @tklauser)
- Fix issue where local host IPs may be briefly associated with the remote-node identity, causing policy drops when policy should allow traffic from the host. (Backport PR #17835, Upstream PR #17836, @joestringer)
- Fix several complexity and program size issues when only one of IPv4/IPv6 is enabled. (Backport PR #17835, Upstream PR #17573, @pchaigno)
- Fixes for IPsec and endpoint routes (Backport PR #18025, Upstream PR #17865, @kkourt)
- Fixes hubble-ui-backend image deployment (#17989, @aanm)
- bpf: Reset Pod's queue mapping in host veth to fix phys dev mq selection (Backport PR #18419, Upstream PR #18388, @borkmann)
- install: Fix hubble-ui image references (Backport PR #18234, Upstream PR #18209, @joestringer)
- v1.9: docs: Fix cilium-runtime image bump instructions (#18491, @joestringer)

### 1.9.13

- Fix bug where Cilium drops traffic from remote nodes in etcd mode, despite policy that allows the traffic (Backport PR #18802, Upstream PR #18777, @joestringer)
- Fix connectivity outage periods with ENI IPAM mode and IPsec enabled when nodes are deleted from the cluster (Backport PR #18847, Upstream PR #18827, @christarazi)
- contrib: Fix backport submission for own PRs (Backport PR #18666, Upstream PR #17988, @joestringer)

### 1.9.14

- Fix IPsec in Azure's IPAM mode (Backport PR #18986, Upstream PR #18911, @pchaigno)
- Fix issue where StatefulSet pod restarts could trigger persistent connectivity issues for the pods due to overzealous CiliumEndpoint resource removal by cilium-agent instances (Backport PR #19154, Upstream PR #18864, @timoreimann)

### 1.9.15

- Fix a bug where a backend pod can be selected by a local redirect policy deployed in a different namespace if the local redirect policy was deployed first. (Backport PR #19252, Upstream PR #19193, @aditighag)
- test/helpers: Fix incorrect count of endpoints (Backport PR #19373, Upstream PR #16437, @pchaigno)

### 1.9.17

- ipsec: Fix off-by-one error on max keyID (Backport PR #20016, Upstream PR #16647, @pchaigno)

### 1.9.18

- Fix agent panic in some cases when service matcher local redirect policy was deployed prior to the selected service. (Backport PR #20180, Upstream PR #19522, @aditighag)
- Fix memory leak in the DNS cache when a long-lived endpoint makes many unique DNS lookups over time (Backport PR #20180, Upstream PR #19925, @christarazi)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **1.9.18**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `cilium/cilium`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/cilium.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
