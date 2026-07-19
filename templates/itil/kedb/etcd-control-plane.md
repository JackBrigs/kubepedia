# KEDB · etcd & control-plane

_37 известных ошибок. Сгенерировано; не править руками._

### KEDB-001 · apiserver_loadbalancer_domain_name default no longer resolves
- **Симптом:** Kubespray no longer injects `lb-apiserver.kubernetes.local` into `/etc/hosts`, so the previous default did not resolve. The fix defaults to the load-balancer IP if defined, otherwise to the node-local load balancer
- **Затронутые CIs:** —  ·  _>=v2.29.0 <=v2.29.1_
- **Root cause:** Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0` · Confirmed via the merged PR #12872 and the tag code
- **Workaround / fix:** Root cause fixed by PR #12872 (in `roles/kubespray_defaults/defaults/main/main.yml`). Workaround before upgrading: set `apiserver_loadbalancer_domain_name` to a real, resolvable name/IP, or rely on the node-local LB (VARIABLE-LOADBALANCER_APISERVER_LOCALHOST). The durable fix is to upgrade to `v2.30.0` or later
- **Источник:** `kb/troubleshooting/apiserver-lb-domain-default-unresolvable.md`

### KEDB-002 · Cilium hardcoded API server IP breaks HA cluster on first control-plane failure
- **Симптом:** When the first control-plane node was shut down or unreachable, the `cilium-operator` and `cilium-agent` pods lost API access with `dial tcp <first-cp-ip>:6443: connect: no route to host`. Pods went NotReady and cluster networking failed. Working around it via `cilium_config_extra_vars` did not help, because the `KUBERNETES_SERVICE_HOST` environment variable was already baked into the running pods
- **Затронутые CIs:** cilium, ha, apiserver  ·  _v2.29.1_
- **Root cause:** Affected versions: v2.29.1 (and earlier; hardcoded IP of the first control-plane node) · Fixed versions: v2.30.0 · Triggered in HA clusters when the first control-plane node fails/becomes unreachable
- **Workaround / fix:** Root cause: Cilium referenced the IP of only the first control-plane node (`k8sServiceHost`) instead of the local/external apiserver load balancer, so connectivity was lost when that node failed. Fix (breaking change in v2.30.0): PR #12624 (merged 2026-01-01, Issue #12623) makes `k8sServiceHost` / `k8sServicePort` derive from `kube_apiserver_global_endpoint`. Confirmed in tag v2.30.0 `roles/network_plugin/cilium/temp…
- **Источник:** `kb/troubleshooting/cilium-hardcoded-apiserver-ip-ha.md`

### KEDB-003 · Control plane: scheduler / controller-manager restart on lease renewal
- **Симптом:** Logs: `failed to renew lease kube-system/kube-{scheduler,controller-manager}: failed to tryAcquireOrRenew context deadline exceeded` → process restarts · While flapping: scheduling stalls; pending CSRs; node status/eviction not reconciled; workloads not scaled
- **Затронутые CIs:** control-plane, leader-election, scheduler, controller-manager  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35** — both components use the same lease-based leader election, so both fail this way
- **Workaround / fix:** The **etcd defrag/upgrade** briefly stalls in-flight apiserver requests, which can trip a lease renewal — expect a transient re-election during maintenance
- **Источник:** `kb/troubleshooting/control-plane-leader-election.md`

### KEDB-004 · Control-plane cert renewal via the seam (kubeadm certs renew)
- **Симптом:** CP components fail TLS: `x509: certificate has expired or is not yet valid` on apiserver/etcd/ kubelet client certs; `kubectl` stops working after ~1 year with no upgrades · After renewing certs, components still present the **old** cert
- **Затронутые CIs:** kubeadm, certificates, control-plane  ·  _>=v2.29.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies to Kubespray **v2.29.0–v2.31.0** / Kubernetes **1.29–1.35**. kubeadm-managed CP certs live in `/etc/kubernetes/pki`; default validity is **1 year** (the CA is 10 years). PKI layout:
- **Workaround / fix:** **Externally-managed / custom CA:** `kubeadm certs renew` can't renew certs signed by an external CA — re-issue them out-of-band · Let CP certs get close to expiry across all masters and you can lose the whole control plane at once — monitor `check-expiration` or upgrade regularly (each upgrade renews)
- **Источник:** `kb/troubleshooting/kubeadm-cert-renewal.md`

### KEDB-005 · controller-manager: node NotReady not evicted / not deleted / pods stuck
- **Симптом:** Node `NotReady` but the expected `node.kubernetes.io/unreachable:NoExecute` taint is missing → taint-based eviction never fires, pods not rescheduled · Node `Ready=False` yet still renewing its Lease → its pods stay in Endpoints and receive traffic · Cloud VM deleted but the Node object persists NotReady; StatefulSet pods stuck `Terminating` · After a brief node flap, containers keep running `1/1` but pods stay `Read…
- **Затронутые CIs:** controller-manager, nodes, control-plane  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35** (node lifecycle is now via the external CCM for cloud deletion). Volume side-effects:
- **Workaround / fix:** A dead node holding an **RWO volume** additionally causes Multi-Attach errors on the replacement pod
- **Источник:** `kb/troubleshooting/kcm-node-lifecycle.md`

### KEDB-006 · etcd quorum loss — API server down, cluster read-only/unavailable
- **Симптом:** kube-apiserver returns errors like `etcdserver: request timed out` / `context deadline exceeded`; `kubectl` hangs or fails; one or more control-plane nodes are down. With a majority of etcd members gone, quorum is lost
- **Затронутые CIs:** etcd, control-plane, disaster-recovery  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` (stacked or external etcd) · Quorum math: a cluster of `N` members tolerates `floor((N-1)/2)` failures — 3 members tolerate 1, 5 tolerate 2. An even member count gives no extra tolerance, so run an **odd** number · Losing quorum is recoverable **only from a snapshot** if you can't bring members back — hence a working etcd backup is mandatory
- **Workaround / fix:** **Rehearse first.** Break a *clone* of your cluster the same way and practice the recovery before touching production — restore rewinds etcd to snapshot time, losing any writes since · Prefer restoring members over full snapshot-restore when you still have one good member — bringing a member back preserves more recent state than an older snapshot · Keep an **odd** member count and off-node snapshots; a single-member …
- **Источник:** `kb/troubleshooting/etcd-quorum-loss.md`

### KEDB-007 · etcd-defrag-controller: latency spikes / defrag not reclaiming space — stop-the-world, one member at a time
- **Симптом:** etcd/API **latency spikes** correlated with defrag runs, or the etcd DB **doesn't shrink** despite the controller running
- **Затронутые CIs:** etcd, maintenance  ·  _>=1.29 <=1.35 / 0.0.7_
- **Root cause:** etcd-defrag-controller `0.0.7` over etcd · **Blocking op:** each member is unavailable during its own defrag; the controller should defrag **one member at a time**, never simultaneously, and ideally off leader/peak · **Space only frees after compaction:** defrag reclaims what compaction freed — if the DB is genuinely full of live keys, defrag won't shrink it
- **Workaround / fix:** **Latency — fix:** ensure serialized, one-member-at-a-time defrag; schedule off-peak; keep the interval sane (defrag isn't needed constantly) · **No shrink — fix:** confirm compaction runs first (auto-compaction retention); defrag after compaction actually reclaims. If the DB is space-exceeded from live data, address quota/keys
- **Источник:** `kb/troubleshooting/etcd-defrag-controller.md`

### KEDB-008 · etcd: mvcc database space exceeded (NOSPACE alarm)
- **Симптом:** `kubectl apply`/writes fail cluster-wide; reads still work · API server logs `mvcc: database space exceeded` · `etcdctl endpoint status` shows the DB size near `--quota-backend-bytes`
- **Затронутые CIs:** etcd, control-plane  ·  _>=3.5.0 <=3.7.0_
- **Root cause:** Applies to etcd **3.5.x–3.7.0** (base ships 3.5.23–3.6.10 via Kubespray — ) · Default quota is modest (historically ~2 GiB, often raised to 8 GiB). Space grows from keyspace history that hasn't been compacted, plus fragmentation
- **Workaround / fix:** Defrag on all members simultaneously can drop quorum — always **one member at a time**, off-peak · A full disk is a different, harder failure — free disk before compaction can help
- **Источник:** `kb/troubleshooting/etcd-database-space-exceeded.md`

### KEDB-009 · etcd: remove-node.yml is not idempotent and fails if the etcd member is already gone
- **Симптом:** A repeated or "after the fact" node removal run fails with a templating (undefined) error when the corresponding member is already absent from the etcd cluster. It breaks while computing the member ID: ``` {{ '%x' | format(((etcd_members.stdout | from_json).members | selectattr('peerURLs.0', '==', etcd_peer_url))[0].ID) }} ``` If `etcd_peer_url` is not in the member list, `selectattr(...)` returns an empty list, the …
- **Затронутые CIs:** etcd, remove-node, idempotency  ·  _>=v2.29.0 <=v2.30.0_
- **Root cause:** Affected versions: v2.29.0, v2.29.1, v2.30.0 · Fixed versions: v2.29.2 and v2.30.1. The release-2.29 backport (#12960) merged 2026-02-05, which is AFTER the v2.29.1 tag (2025-12-11) and after v2.30.0 (2026-01-30) — so the fix is NOT present in v2.29.1 or v2.30.0 themselves; it lands in the future patches v2.29.2 and v2.30.1 · Trigger: removal run where `etcd_peer_url` is no longer present in `etcdctl member list`
- **Workaround / fix:** Root cause: the "Remove member from cluster" task (`roles/remove-node/remove-etcd-node/tasks/main.yml`) does not check whether the etcd member is present in the cluster before computing its ID and calling `etcdctl member remove`. There is no `when` condition handling the already-removed-member case. Fix: PR #12949 (merged to master, "Fixes #12947") makes etcd member removal idempotent. Backport to release-2.29 is PR …
- **Источник:** `kb/troubleshooting/etcd-remove-node-not-idempotent.md`

### KEDB-010 · etcd: removing an external (non-stacked) member aborts the remove-node playbook
- **Симптом:** When removing an etcd node that is deployed standalone (external etcd, the host is not part of the Kubernetes cluster), the removal playbook fails: the "Lookup node IP in kubernetes" task aborts the whole run, and the etcd member is not removed
- **Затронутые CIs:** etcd, remove-node  ·  _v2.29.0_
- **Root cause:** Affected versions: v2.29.0 (when removing an external-etcd node) · Fixed versions: v2.29.1 · Trigger: the etcd node being removed is not a Kubernetes node, so the IP-to-node match finds no correspondence
- **Workaround / fix:** "{{ '%x' | format(((etcd_members.stdout | from_json).members | selectattr('peerURLs.0', '==', etcd_peer_url))[0].ID) }}" ```
- **Источник:** `kb/troubleshooting/etcd-remove-external-member-fails.md`

### KEDB-011 · Flatcar: apiserver wait skipped after DNS handler caused flakiness
- **Симптом:** The wait handler excluded Flatcar/FCOS and used a Flatcar-specific notify channel; the fix removes the exclusion and unifies the notify channel so the apiserver wait runs on those OSes too
- **Затронутые CIs:** —  ·  _v2.30.0_
- **Root cause:** Affected Kubespray: `v2.30.0`. Fixed in: `v2.31.0` · Confirmed via merged PR #13063 and the tag code
- **Workaround / fix:** Fixed by PR #13063 (in `roles/kubernetes/preinstall/handlers/main.yml`). Workaround before upgrading: re-run the playbook (often transient), or upgrade to v2.31.0 for the consistent wait. Durable fix: upgrade to `v2.31.0` or later
- **Источник:** `kb/troubleshooting/flatcar-apiserver-wait-dns-handler.md`

### KEDB-012 · Inverted ignore_errors condition for etcd-events service startup causes false failures
- **Симптом:** False failures of the playbook when adding / scaling control-plane nodes with `etcd_events_cluster_setup: true` enabled. The `etcd-events` service startup task reports an error even though the etcd-events cluster is healthy
- **Затронутые CIs:** etcd, scale, control-plane  ·  _>=v2.29.1 <=v2.31.0_
- **Root cause:** Affected Kubespray versions: v2.29.1, v2.30.0, v2.31.0 (all indexed versions) · Fixed versions: none released yet. The fix is in master and will land in the next tag after v2.31.0 · Trigger conditions: scaling / adding control-plane nodes with `etcd_events_cluster_setup: true`
- **Workaround / fix:** Root cause: in `roles/etcd/tasks/configure.yml`, the `ignore_errors` condition for the etcd-events service is inverted relative to the parallel main-etcd task: · main etcd (correct): `ignore_errors: "{{ etcd_cluster_is_healthy.rc == 0 }}"` — errors are ignored when the cluster is already healthy (rc == 0) · etcd-events (bug): `ignore_errors: "{{ etcd_events_cluster_is_healthy.rc != 0 }}"` — uses `!= 0`, so on a healt…
- **Источник:** `kb/troubleshooting/etcd-events-inverted-ignore-errors.md`

### KEDB-013 · kube-apiserver: HTTP 429 from API Priority & Fairness (APF)
- **Симптом:** `429` responses; `kubectl` retries with backoff. Response headers `X-Kubernetes-PF-FlowSchema-UID` / `X-Kubernetes-PF-PriorityLevel-UID` identify the mapping · Metrics: **`apiserver_flowcontrol_rejected_requests_total`** (per FlowSchema/PriorityLevel), `apiserver_flowcontrol_current_inqueue_requests`, `apiserver_flowcontrol_request_wait_duration_seconds`
- **Затронутые CIs:** apiserver, apf, control-plane  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35** (APF stable). (The metric is `apiserver_flowcontrol_rejected_requests_total`, not `apf_rejected_requests_total`.)
- **Workaround / fix:** Latency inflation alone (slow etcd/admission) makes requests hold seats longer and can trip APF cluster-wide — fix the underlying latency · Expensive LISTs are both an APF and a memory problem
- **Источник:** `kb/troubleshooting/apiserver-apf-429.md`

### KEDB-014 · kube-apiserver: latency/timeouts cascading from slow etcd
- **Симптом:** `kubectl` slow/timeouts; writes fail. apiserver logs `etcdserver: request timed out`, `context deadline exceeded` · 429/408/503 rise (APF backpressure from held seats)
- **Затронутые CIs:** apiserver, etcd, latency  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35**. Related etcd docs: space and quorum
- **Workaround / fix:** etcd **defrag** briefly blocks that member — do one member at a time; a defrag can transiently spike apiserver latency
- **Источник:** `kb/troubleshooting/apiserver-etcd-latency.md`

### KEDB-015 · kube-apiserver: OOM / memory growth from LISTs & relists
- **Симптом:** apiserver memory jumps after a few large LISTs and stays high; concurrent large LISTs OOM-kill it (e.g. a 20 MB CRD dataset: 10 LISTs → ~8 GB, 20 → ~12 GB; 100 watches → only ~3 GB) · Memory rises as objects are created and **stays high after deletion** (CRD parsing/conversion cache; ~10k objects of a 5-version CRD ≈ 2 GB retained) · After a CRD spec change / apiserver restart, watchers get `too old resource version`…
- **Затронутые CIs:** apiserver, memory, scale  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35** (larger clusters / big CRD datasets). Companion to APF
- **Workaround / fix:** These are **design/behaviour** issues, not CVEs — no upstream "fix" for the LIST-memory retention itself; a restart reclaims memory
- **Источник:** `kb/troubleshooting/apiserver-memory-lists.md`

### KEDB-016 · kube-apiserver: request latency from audit / admission
- **Симптом:** All create/update requests slow; latency localized to audit or admission (not etcd) · In `blocking` audit mode, response is delayed until the audit event is processed; in `batch` mode, audit events silently drop on buffer overflow
- **Затронутые CIs:** apiserver, audit, admission, latency  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35**. Webhook **blocking** (fail-closed) is a separate class ; this doc is about **latency**
- **Workaround / fix:** A slow webhook is both a latency source *and* (fail-closed) an availability risk — see
- **Источник:** `kb/troubleshooting/apiserver-request-latency.md`

### KEDB-017 · kube-scheduler: pod Pending / FailedScheduling (taints, resources, volume, GPU)
- **Симптом:** `kubectl get pod` → `Pending`; `describe` shows `FailedScheduling`, e.g. `0/5 nodes are available: 3 Insufficient cpu, 2 node(s) had untolerated taint {...}` · Or `... node(s) had volume node affinity conflict` · Or `Insufficient nvidia.com/gpu` despite GPU nodes · Or the pod is `Pending` with **no `FailedScheduling` event at all**
- **Затронутые CIs:** scheduler, scheduling, control-plane  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35** (message formats stable). Topology-spread and preemption/gates are separate docs (, )
- **Workaround / fix:** The `preemption:` tail of the message matters: `No preemption victims found` / `Preemption is not helpful for scheduling` explain why eviction won't rescue the pod
- **Источник:** `kb/troubleshooting/scheduler-pod-pending.md`

### KEDB-018 · kube-scheduler: PodTopologySpread keeps pods Pending / skew regressions
- **Симптом:** `FailedScheduling ... node(s) didn't match pod topology spread constraints`; pods Pending when one domain (zone/node) is full · Spread suddenly behaves differently right after upgrading to 1.33/1.34
- **Затронутые CIs:** scheduler, topology-spread, scheduling  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35**. Companion to
- **Workaround / fix:** Combining tight `maxSkew: 1` + `DoNotSchedule` + few domains is the classic "won't schedule" trap — loosen `maxSkew` or use `ScheduleAnyway`
- **Источник:** `kb/troubleshooting/scheduler-topology-spread.md`

### KEDB-019 · kube-scheduler: preemption not happening / SchedulingGated forever
- **Симптом:** High-priority pod Pending; `preemption: ... No preemption victims found` / `Preemption is not helpful for scheduling` · A high-priority pod jumps the queue but **never evicts** running pods · `kubectl get pod` STATUS `SchedulingGated`, never progresses
- **Затронутые CIs:** scheduler, preemption, scheduling  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35**. Pod Scheduling Readiness is GA in **1.30** (beta 1.27). Companion:
- **Workaround / fix:** A gate-owning controller that upgrades independently (e.g. Kueue vs Kubernetes 1.30) can start failing to remove gates after a cluster upgrade — a stuck `SchedulingGated` fleet often means that controller broke, not the scheduler · `preemptionPolicy: Never` + high priority is a subtle starvation trap for batch workloads
- **Источник:** `kb/troubleshooting/scheduler-preemption-gates.md`

### KEDB-020 · kube-scheduler: slow scheduling / clumped placement / requeue OOM
- **Симптом:** High scheduling latency / throughput bottleneck on large clusters · Pods clump onto few nodes instead of spreading · Scheduler memory spikes / OOM, or unschedulable pods requeue slowly
- **Затронутые CIs:** scheduler, performance, scale  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35** (large clusters). Companion:
- **Workaround / fix:** Aggressively lowering `percentageOfNodesToScore` trades placement quality for speed — verify spread/utilization after tuning
- **Источник:** `kb/troubleshooting/scheduler-performance.md`

### KEDB-021 · kube-vip control-plane VIP does not come up
- **Симптом:** The control-plane VIP (`kube_vip_address`) is unreachable: `kubectl`/join through the VIP times out, the API endpoint doesn't answer on the VIP even though individual control-plane node IPs work, or the VIP never appears on any node's interface
- **Затронутые CIs:** kube-vip, control-plane, load-balancer, ha  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0`. kube-vip runs as a static pod on control-plane nodes (`roles/kubernetes/node/tasks/loadbalancer/kube-vip.yml`) · Relevant defaults (all **off/empty** unless set): · `kube_vip_enabled: false` — master switch · `kube_vip_address:` — the VIP (must be set, and free on the subnet) · `kube_vip_controlplane_enabled: false` — advertise the **API** VIP · `kube_vip_services_enabled: fa…
- **Workaround / fix:** **No mode selected:** `kube_vip_enabled: true` with a VIP but **neither** `kube_vip_arp_enabled` **nor** `kube_vip_bgp_enabled` → the VIP is never advertised. Enable the mode that fits your network · **Control-plane VIP not enabled:** set `kube_vip_controlplane_enabled: true` for the API VIP (separate from `kube_vip_services_enabled`) · **Wrong mode for the network:** ARP requires all control-plane nodes on the **sam…
- **Источник:** `kb/troubleshooting/kube-vip-vip-not-up.md`

### KEDB-022 · kube-vip: control-plane VIP not reachable / not failing over
- **Симптом:** `kubectl`/kubelets can't reach the API VIP (timeouts) · On leader node failure the VIP doesn't migrate; API stays down until manual action · VIP flaps between nodes
- **Затронутые CIs:** kube-vip, control-plane, ha, networking  ·  _>=0.8.0 <=1.2.1_
- **Root cause:** Applies to kube-vip **0.8–1.2.1** (base ≤1.0.3 — ). Runs as a static pod / DaemonSet on control-plane nodes
- **Workaround / fix:** Mixing kube-vip ARP with a cloud that filters MAC/ARP silently fails — confirm the platform supports layer2 VIPs before choosing ARP mode
- **Источник:** `kb/troubleshooting/kube-vip-control-plane-vip.md`

### KEDB-023 · kubeadm task fails when cilium_identity_allocation_mode is undefined
- **Симптом:** The task in the `kubernetes/kubeadm` role fails with `'cilium_identity_allocation_mode' is undefined`. It manifests when a non-Cilium CNI is chosen (`kube_network_plugin != cilium`) and/or during a partial role run (`--tags`) where the Cilium role defaults are not loaded
- **Затронутые CIs:** cilium, kubeadm, etcd  ·  _>=v2.29.0 <=v2.30.0_
- **Root cause:** Affected versions: v2.29.0, v2.29.1, v2.30.0 (the condition was introduced by PR #12565, which landed in v2.29.0) · Fixed versions: v2.31.0 · Triggered when `kube_network_plugin != cilium`, or when partial `--tags` runs skip loading the Cilium role defaults
- **Workaround / fix:** Root cause: the etcd-certificate-extraction skip condition in `roles/kubernetes/kubeadm/tasks/main.yml` (introduced by PR #12565) unconditionally reads `cilium_identity_allocation_mode`, but that variable is defined only in `roles/network_plugin/cilium/defaults/main.yml`, not in the shared defaults. When Cilium is not selected the variable is undefined and the condition evaluation fails. The `or` condition still eval…
- **Источник:** `kb/troubleshooting/cilium-identity-allocation-mode-undefined.md`

### KEDB-024 · kubeadm upgrade apply/node fails (config, etcd, addons, certs)
- **Симптом:** `kubeadm upgrade apply` returns non-zero; `error execution phase …`; config/addon errors · `kube-proxy`/`coredns`/etcd re-apply step fails; certs not renewed
- **Затронутые CIs:** kubeadm, upgrade, control-plane  ·  _>=v2.29.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies to Kubespray **v2.29.0–v2.31.0** / Kubernetes **1.29–1.35**. Kubespray's `kubeadm-upgrade.yml` runs `upgrade apply/node`, then `kubeadm init phase upload-config all`, `addon kube-proxy`, `etcd local`, `control-plane all` (some with retries)
- **Workaround / fix:** If `upgrade apply` succeeds but the component then won't come healthy, that's the **health check** class, not the apply
- **Источник:** `kb/troubleshooting/kubeadm-upgrade-apply.md`

### KEDB-025 · kubeadm upgrade: health-check fails (static control plane won't come up)
- **Симптом:** kubeadm: `[upgrade/health] FATAL`, or `[upgrade/staticpods] Waiting for the kubelet to boot up the control plane as static Pods …` that never completes; `context deadline exceeded` · Kubespray's own `check-api.yml` then times out: `/healthz` never returns 200 (60×5 s) · `kubeadm upgrade apply` returns non-zero and Ansible reports the wrapped stderr
- **Затронутые CIs:** kubeadm, upgrade, control-plane  ·  _>=v2.29.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies to Kubespray **v2.29.0–v2.31.0** / Kubernetes **1.29–1.35**. kubeadm upgrades a CP component by writing a new manifest to `/etc/kubernetes/manifests`, waiting for the kubelet to restart the static pod, then health-checking it
- **Workaround / fix:** Kubespray tolerates `field is immutable` on `kubeadm upgrade` (`failed_when: rc != 0 and "field is immutable" not in stderr`) — that specific message is **not** the health-check failure; a genuine health failure has a different stderr
- **Источник:** `kb/troubleshooting/kubeadm-upgrade-health-check.md`

### KEDB-026 · kubeadm: устаревшие kubeadm_patches не удаляются при изменении inventory
- **Симптом:** Роль записи патчей только создаёт каталог и копирует патчи из текущего `kubeadm_patches`, но не удаляет с файловой системы патчи, отсутствующие в текущем значении переменной. В результате удалённые или изменённые патчи продолжают действовать
- **Затронутые CIs:** kubeadm, control-plane  ·  _>=v2.29.0 <=v2.30.0_
- **Root cause:** Затронуто: v2.29.0, v2.29.1, v2.30.0 (уязвимый код одинаков во всех) · Исправлено: v2.31.0 (master). Бэкпорт в release-2.30 — PR #13020 (будущий v2.30.1, тег не выпущен). Для линии release-2.29 также существует бэкпорт (#13021) · Условие срабатывания: изменение или удаление патчей в `kubeadm_patches` без ручной очистки каталога `kubeadm_patches_dir`
- **Workaround / fix:** Корневая причина: роль не удаляет устаревшие файлы патчей с узлов. Исправление — PR [#13019](https://github.com/kubernetes-sigs/kubespray/pull/13019) (master -> v2.31.0), бэкпорт в release-2.30 — PR #13020: логика фикса удаляет с узлов файлы патчей, которых нет в текущем `kubeadm_patches`. Обходной путь на v2.30.0: вручную удалять устаревшие файлы патчей из каталога `kubeadm_patches_dir` на control-plane узлах
- **Источник:** `kb/troubleshooting/kubeadm-patches-not-removed.md`

### KEDB-027 · kubectl exec/port-forward/cp fails through a proxy — SPDY→WebSockets transition (on-by-default 1.31)
- **Симптом:** `kubectl exec`/`attach` returns an error or hangs; `port-forward` won't establish; `kubectl cp` stalls — specifically **through a proxy**, while direct-to-apiserver works · Errors mentioning WebSocket `Upgrade`, `101 Switching Protocols` not completing, or connection reset on the streamed channel
- **Затронутые CIs:** kubernetes, apiserver, kubectl  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Milestone (`keps/sig-api-machinery/4006-...` kep.yaml): alpha **1.29**, beta/on-by-default **1.31**. `kubectl` prefers WebSockets and **falls back** to SPDY only against **old servers** — but once the server is ≥1.31 the WebSocket path is used, exposing proxies that don't support it · Common culprits: an L7 proxy/WAF, an ingress in front of the apiserver, or an old `kubectl`-proxy/bastion that terminates and re-origi…
- **Workaround / fix:** **Fix (correct):** configure the proxy/LB to support **WebSocket** upgrades for the apiserver path (enable Upgrade header passthrough; raise idle timeouts for long-lived streams). This is the durable fix — SPDY is going away · **Temporary:** newer `kubectl` still negotiates; keeping the server path WebSocket-capable is required. Do not rely on SPDY-only middleboxes long-term · **Pre-upgrade check:** before moving to …
- **Источник:** `kb/troubleshooting/spdy-to-websockets.md`

### KEDB-028 · kubelet: static pod won't restart after manifest edit + kubelet restart
- **Симптом:** A control-plane static pod (apiserver/etcd/etc.) doesn't return after a manifest change + kubelet restart · kubelet log: `Pod worker has been requested for removal but is still not fully terminated`; containers killed but the **sandbox stays live**; mirror pod stuck
- **Затронутые CIs:** kubelet, static-pods, control-plane  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35** (race confirmed on 1.22.8; the code path persists; PR #106394 addressed related handling but not this — issue #109596 closed not-planned)
- **Workaround / fix:** This affects the **control plane** (static pods are how kubeadm/Kubespray run apiserver/etcd), so a stuck static pod can take a control-plane node's component down — recover promptly
- **Источник:** `kb/troubleshooting/kubelet-static-pod-stuck.md`

### KEDB-029 · Kubespray deploy hangs waiting for the API server (init)
- **Симптом:** Ansible stuck on `Kubeadm | Check api is up` then `FAILED (retries exhausted)` · `kubeadm init` completed (or is stuck) but `/healthz` never healthy
- **Затронутые CIs:** kubespray, control-plane, deploy  ·  _>=v2.29.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies to Kubespray **v2.29.0–v2.31.0**. After `kubeadm init` writes the control-plane static-pod manifests, the **kubelet** must start them; `check-api.yml` waits for the API to be healthy
- **Workaround / fix:** This is almost always a **kubelet / static-pod / etcd** problem, not Ansible — the Ansible timeout is just the messenger
- **Источник:** `kb/troubleshooting/deploy-hangs-wait-apiserver.md`

### KEDB-030 · Kyverno: reports/UpdateRequests flood etcd (read-only / OOM)
- **Симптом:** reports-controller floods the apiserver with expensive `List` calls; heavy etcd load (worse with many namespaces) · etcd hits its quota and goes read-only (writes fail cluster-wide) · Background controller OOM-crashloops; `UpdateRequest` count explodes
- **Затронутые CIs:** kyverno, etcd, scale, policy  ·  _>=1.29 <=1.35 / >=1.10.0 <=1.18.2_
- **Root cause:** Applies to Kyverno **1.10–1.18** at scale . etcd-full generic handling:
- **Workaround / fix:** **1.12.0 specifically** has ephemeralreports/etcd-growth bugs — upgrade straight to **1.12.4+**
- **Источник:** `kb/troubleshooting/kyverno-reports-etcd-scale.md`

### KEDB-031 · Node can't reach the API server (localhost LB / nginx-proxy)
- **Симптом:** `kubelet` logs `connection refused`/`i/o timeout` to the apiserver; node `NotReady`; pods can't reach the in-cluster API
- **Затронутые CIs:** control-plane, networking, kubespray  ·  _>=v2.29.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies to Kubespray **v2.29.0–v2.31.0**. Default **`loadbalancer_apiserver_localhost: true`** (when no external `loadbalancer_apiserver` is defined), **`loadbalancer_apiserver_type: nginx`** — non-CP nodes talk to the API via the local proxy, not directly
- **Workaround / fix:** Adding/removing control-plane nodes changes the upstream list — the local proxies must be reconfigured (a Kubespray run does this); a manual CP change without re-running leaves stale proxy configs
- **Источник:** `kb/troubleshooting/node-cannot-reach-apiserver.md`

### KEDB-032 · Recursive 0700 perms on etcd cert dir break Calico in etcd datastore mode
- **Симптом:** Clusters running Calico in **etcd datastore** mode with dedicated etcd nodes failed during upgrade / control-plane rotation: `calico-kube-controllers` could not read the certificates needed to access etcd. The root change concerns etcd certificate handling (and explains the removal of the `etcd_cert_dir_mode` variable in v2.30.0), even though the visible failure is on Calico
- **Затронутые CIs:** etcd, certificates  ·  _v2.29.1_
- **Root cause:** Affected Kubespray version (within scope): v2.29.1. The cache notes the recursive behavior applied to versions ≤ v2.29.1 · Fixed in v2.30.0 (with backports to release-2.27/2.28/2.29) · Trigger conditions: Calico in etcd datastore mode, dedicated etcd nodes, upgrade or control-plane rotation
- **Workaround / fix:** Root cause: `0700` permissions were applied **recursively** to `/etc/ssl/etcd/ssl`, stripping group permissions from the certificate files that Calico relies on · Fix (breaking change in v2.30.0): PR [#12908](https://github.com/kubernetes-sigs/kubespray/pull/12908) (merged 2026-01-27) removed the `etcd_cert_dir_mode` variable (the directory mode is now always `0700`) and applies the directory permissions **non-recurs…
- **Источник:** `kb/troubleshooting/etcd-cert-dir-recursive-perms-calico.md`

### KEDB-033 · Remove a dead control-plane node (etcd member + reset)
- **Симптом:** A dead CP node still counts toward etcd quorum; the cluster is fragile (a second failure loses quorum). Node stays `NotReady`; pods may hang
- **Затронутые CIs:** control-plane, etcd, kubespray, operations  ·  _>=v2.29.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies to Kubespray **v2.29.0–v2.31.0**. Etcd is usually Kubespray's own host etcd , so member removal is via `etcdctl`
- **Workaround / fix:** Removing an etcd member **before** the node is truly gone (it comes back) causes a split — only remove members for genuinely dead nodes · Restoring/replacing a lost majority is a different, harder procedure (restore from snapshot) — keep etcd snapshots
- **Источник:** `kb/troubleshooting/remove-dead-control-plane-node.md`

### KEDB-034 · Talos: control plane won't come up (bootstrap / etcd)
- **Симптом:** `talosctl health` never passes; kube-apiserver static pod not up · `talosctl -n <cp> get members` shows no/partial etcd members · API VIP unreachable; workers can't join
- **Затронутые CIs:** talos, control-plane, etcd  ·  _>=1.29 <=1.35 / 1.13.6_
- **Root cause:** Applies to Talos **1.13.x** . etcd + control-plane components run as Talos-managed static pods
- **Workaround / fix:** If `talosctl` itself can't connect at all, fix connectivity first · Restoring etcd from a snapshot requires the **same secrets bundle** — another reason to back it up
- **Источник:** `kb/os/talos/talos-cp-bootstrap.md`

### KEDB-035 · Talos: recover the control plane / etcd from a snapshot (DR)
- **Симптом:** Majority of control-plane nodes lost → etcd has no quorum → API read-only/down · A single control-plane node died and needs replacing
- **Затронутые CIs:** talos, etcd, backup, disaster-recovery  ·  _>=1.29 <=1.35 / 1.13.6_
- **Root cause:** Applies to Talos **1.13.x**. Precondition: you have a recent **etcd snapshot** and the **secrets bundle** + machine configs
- **Workaround / fix:** **No secrets bundle = no recovery** — a snapshot alone can't rebuild the cluster without the matching CAs/keys. Store both · Take snapshots **before every upgrade / risky change** ; a snapshot is only as good as its age · Don't run `bootstrap`/`--recover-from` on more than one node (split etcd)
- **Источник:** `kb/os/talos/talos-etcd-restore.md`

### KEDB-036 · Undefined apiserver_loadbalancer_domain_name breaks apiserver_sans generation
- **Симптом:** In the `_apiserver_sans` fact assembly, the value `apiserver_loadbalancer_domain_name` is appended to the SAN list without an `undefined` guard (unlike the neighboring `loadbalancer_apiserver.address | d('')`). If the variable is not set, templating fails before the `select` filter
- **Затронутые CIs:** control-plane, certificates, kubeadm  ·  _>=v2.30.0 <v2.31.0_
- **Root cause:** Affected Kubespray versions: v2.30.0 · Fixed versions: v2.31.0 (master). Backported to release-2.30 (future v2.30.1, tag not released) · Trigger conditions: deploying without an external LB, or regenerating certificates during an upgrade, while `apiserver_loadbalancer_domain_name` is left undefined
- **Workaround / fix:** Root cause: `apiserver_loadbalancer_domain_name` is added to the SAN list without a `default('')` / undefined guard, so an undefined value breaks Jinja templating of `apiserver_sans`. Workaround on v2.30.0: explicitly set `apiserver_loadbalancer_domain_name` in inventory (e.g., the domain name of the first control-plane node even without an external LB), or build the role from the release-2.30 branch. Fix: PR [#13009…
- **Источник:** `kb/troubleshooting/apiserver-sans-undefined-lb-domain.md`

### KEDB-037 · x509: certificate is valid for … not <address> (apiserver cert SAN)
- **Симптом:** `kubectl`, a load balancer health check, or an in-cluster client fails with: ``` x509: certificate is valid for kubernetes, kubernetes.default, …, 10.233.0.1, <cp-node-ips>, not <the address you connected through> ``` Public API images/endpoints work from the control-plane nodes themselves but not via the external endpoint
- **Затронутые CIs:** control-plane, certificates, apiserver, load-balancer  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` (kubeadm-issued apiserver cert) · Kubespray builds `certSANs` from `apiserver_sans` (`roles/kubernetes/control-plane/tasks/kubeadm-setup.yml`), which **already** includes: `kubernetes[.default[.svc[.<dns_domain>]]]`, the API service IP (`kube_apiserver_ip`), `localhost`/`127.0.0.1`/`::1`, `apiserver_loadbalancer_domain_name`, `loadbalancer_apiserver.address`, `supplementary_ad…
- **Workaround / fix:** Plan SANs **before** install when you know the external endpoint — adding them later forces a cert regeneration and apiserver restart · IPv6/dual-stack: include the IPv6 address too if clients reach the API over IPv6 · Changing SANs does not change the CA — clients that already trust the cluster CA keep working once the leaf cert includes their address
- **Источник:** `kb/troubleshooting/apiserver-cert-san.md`

