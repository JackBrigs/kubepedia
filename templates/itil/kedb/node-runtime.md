# KEDB · node & runtime

_25 известных ошибок. Сгенерировано; не править руками._

### KEDB-138 · Add-node gotchas — new node stays empty/NotReady (facts not run, taint, CNI, podCIDR exhausted, version skew)
- **Симптом:** New worker is `Ready` but **no pods schedule** onto it · New node stuck **`NotReady`** ("network plugin not ready" / no CNI) · New node never gets a **podCIDR**; its pods stay `Pending` · New node joined on a **different Kubernetes patch** than the rest
- **Затронутые CIs:** node, scaling, add-node  ·  _>=v2.27.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies across **v2.27.0–v2.31.0**. Worker add = `scale.yml`, control-plane add = `cluster.yml` (, ) · **Facts not refreshed first:** `scale.yml --limit=<new>` converges only the new node, but existing nodes' hostvars must already know it (cert SANs, `/etc/hosts`, etcd/nginx-proxy endpoint lists). If you skip the **facts** pass, the new node can join with an incomplete view. Kubespray's guidance is to run **`playbook…
- **Workaround / fix:** **Empty node, has a taint — fix:** expected for control-plane; for workers, remove the stray taint (`kubectl taint node <new> <key>-`) or add a matching toleration. Not a scheduler fault · **NotReady / no CNI — fix:** ensure the CNI image is reachable from the node (mirror/registry for air-gap); check the CNI DaemonSet rolled a pod onto it; re-run the CNI tag if needed · **No podCIDR (block exhausted) — fix:** this n…
- **Источник:** `kb/troubleshooting/add-node-gotchas.md`

### KEDB-139 · cgroup driver mismatch (containerd SystemdCgroup vs kubelet cgroupDriver)
- **Симптом:** Symptoms of a driver mismatch: pods stuck `ContainerCreating`, kubelet logs such as `failed to get cgroup stats` / `Failed to start ContainerManager` / `cgroup ... not found`, nodes flapping `NotReady`, or broken CPU/memory limits — after changing cgroup-related settings or joining a node configured differently
- **Затронутые CIs:** containerd, kubelet, cgroups  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` with containerd · Defaults that keep the two in sync: · containerd: `containerd_use_systemd_cgroup: true` → `SystemdCgroup = true` in `config.toml` · kubelet: `cgroupDriver: systemd` (template default; see ) · **cgroup v2 requires the systemd driver** — this is another reason the systemd default matters (and why Kubernetes `1.35` forces cgroup v2 by default, see / the 1.35 cha…
- **Workaround / fix:** **Fix:** make both sides agree — keep `containerd_use_systemd_cgroup: true` **and** kubelet `cgroupDriver: systemd` (the Kubespray defaults). Don't flip only one. After changing, re-run the relevant roles so both configs and both services restart · Don't set `cgroupfs` on a cgroup v2 host — v2 needs the systemd driver; combined with the 1.35 cgroup-v1 removal, `systemd` is the only forward-looking choice · Joining a …
- **Источник:** `kb/troubleshooting/cgroup-driver-mismatch.md`

### KEDB-140 · Container OOMKilled (exit 137) / node memory pressure
- **Симптом:** `kubectl get pod` shows restarts; `kubectl describe pod` shows `Last State: Terminated, Reason: OOMKilled, Exit Code: 137`. Or nodes flap and multiple pods restart/evict under memory pressure
- **Затронутые CIs:** memory, resources, nodes  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` · **Container OOM:** the container's `resources.limits.memory` was exceeded — the cgroup OOM-kills that container only · **Node OOM / pressure:** total usage exceeds capacity minus reservations; the kubelet evicts pods on `MemoryPressure`, and the kernel may OOM-kill before that. Kubespray's `kube_reserved`/`system_reserved` (off by default) carve out memory for the kubelet an…
- **Workaround / fix:** **Right-size the container:** raise `resources.limits.memory` (and set a realistic `requests.memory` so the scheduler places it correctly). A limit set too low for the real working set guarantees repeated OOM kills · **Reserve node headroom:** enable `kube_reserved` / `system_reserved` so the kubelet and OS keep memory, preventing node-wide OOM · **Add capacity / spread load:** more/larger nodes, or anti-affinity to …
- **Источник:** `kb/troubleshooting/oomkilled.md`

### KEDB-141 · containerd can't pull from a private/mirror registry (hosts.toml / certs.d)
- **Симптом:** Pods stay in `ImagePullBackOff`/`ErrImagePull` for images from a private registry or an intended mirror; `crictl pull <image>` fails with TLS errors (`x509: certificate signed by unknown authority`), auth errors (`401 Unauthorized`/`403`), or connection errors — while public images pull fine
- **Затронутые CIs:** containerd, registry, image-pull  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` with `container_manager: containerd` · Registry config lives under `containerd_cfg_dir/certs.d` (default **`/etc/containerd/certs.d`**); the CRI plugin reads a per-registry `hosts.toml` · Kubespray renders these from inventory variables — the two you need: · **`containerd_registries_mirrors`** — list of `{prefix, mirrors:[{host, capabilities, skip_verify, override_path, ca, cl…
- **Workaround / fix:** **Self-signed / private CA (`x509`):** add `ca` (path to the CA cert on the node) to the mirror entry, or `skip_verify: true` for a lab (insecure — disables TLS verification) · **Private registry auth (`401/403`):** add an entry to `containerd_registry_auth` with `registry`, `username`, `password` · **Mirror / pull-through cache:** add the upstream under `containerd_registries_mirrors` with the mirror `host` and `cap…
- **Источник:** `kb/troubleshooting/containerd-registry-config.md`

### KEDB-142 · containerd: failed to create shim task (runc create failed)
- **Симптом:** `... runc create failed: unable to start container process: can't get final child's PID from pipe: EOF: unknown` · Or (~1% under churn): `... unable to create new parent process: namespace path: lstat /proc/0/ns/ipc: no such file or directory: unknown`
- **Затронутые CIs:** containerd, runtime, runc  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35** on containerd (Kubespray's default runtime — )
- **Workaround / fix:** Both surface as `CrashLoopBackOff`/`RunContainerError` at the kubelet level ; check the containerd/`crictl` logs for the exact runc string
- **Источник:** `kb/troubleshooting/containerd-shim-task-create.md`

### KEDB-143 · containerd: image pull / CRI sandbox failures
- **Симптом:** `kubelet` events: `failed to pull and unpack image ...`, `failed to resolve reference` · `RunPodSandbox` / `CreateContainer` errors; pods stuck `ContainerCreating` · Private-registry images fail with `401/403`
- **Затронутые CIs:** containerd, runtime, cri  ·  _>=2.0.0 <=2.3.3_
- **Root cause:** Applies to containerd **2.0–2.3.3** (base ≤2.2.3 — ). General image-pull triage:
- **Workaround / fix:** containerd 2.x carries known CVEs at the shipped patch levels — see the containerd CVE matrix. GPU nodes: the Container Toolkit overwrites top-level `imports`
- **Источник:** `kb/troubleshooting/containerd-image-pull-cri.md`

### KEDB-144 · containerd: no runtime configured for RuntimeClass handler (gVisor/Kata)
- **Симптом:** `no runtime for "runsc" is configured` (gVisor) / `no runtime for "kata-qemu" is configured` (Kata) when creating a pod with that `runtimeClassName`
- **Затронутые CIs:** containerd, runtimeclass, runtime  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35** on containerd (, ). Common on k3s/minikube where the managed `config.toml` isn't edited by the runtime installer
- **Workaround / fix:** A version mismatch between the shim binary and the `runtime_type` also fails here — install the matching shim (`containerd-shim-runsc-v1` / `containerd-shim-kata-v2`) on PATH
- **Источник:** `kb/troubleshooting/containerd-runtime-handler.md`

### KEDB-145 · containerd: shim/daemon memory leak (reaper deadlock, exec streams)
- **Симптом:** Shim processes grow to **20 GB+** RSS; containers show `UNKNOWN` in `crictl`; `context deadline exceeded` in logs; a shim with no children won't exit · containerd RSS climbs on exec-heavy nodes; goroutine dump shows accumulating `wsstream.(*Conn).Open` / `createWebSocketStreams`
- **Затронутые CIs:** containerd, memory, runtime  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35** on containerd . The kubelet may OOM as a downstream effect
- **Workaround / fix:** `containers UNKNOWN` in `crictl` is the tell that shims are wedged — a containerd restart is the reliable recovery
- **Источник:** `kb/troubleshooting/containerd-shim-memory-leak.md`

### KEDB-146 · Controller using node credentials gets Forbidden — Node authorizer tightened with selectors (GA 1.34)
- **Симптом:** After upgrading to K8s 1.34 (Kubespray v2.31.0), a workload authenticating as a **node identity** (`system:node:<name>`, group `system:nodes`) gets `Forbidden` on LIST/GET it previously could do · A controller running under a node's kubelet credentials can no longer enumerate Secrets/ConfigMaps/ Pods it doesn't "own"
- **Затронутые CIs:** kubernetes, auth, node  ·  _>=v2.31.0 <=v2.31.0 / >=1.34 <=1.35_
- **Root cause:** Milestone (`keps/sig-auth/4601-...` kep.yaml): alpha **1.31**, beta **1.32**, stable **1.34**. The restriction becomes fully enforced at GA · Intent: a compromised node should only reach **its own** objects (the pods scheduled to it and their Secrets/ConfigMaps), not the whole cluster — a real security hardening · The break is only for things **abusing node credentials**; normal kubelet operation is unaffected (kubel…
- **Workaround / fix:** **Fix (correct):** give the controller its **own ServiceAccount + RBAC** with exactly the access it needs — do not run workloads under node/kubelet credentials · **Do not** try to broaden the Node authorizer; it is intentionally selector-scoped. The gate (`AuthorizeNodeWithSelectors`) exists transitionally but the hardening is the intended end state · **Pre-upgrade audit:** before v2.31.0, grep audit logs for `system…
- **Источник:** `kb/troubleshooting/node-authorizer-selectors.md`

### KEDB-147 · CRI-O: duplicate top-level auths keys make registry config invalid JSON
- **Симптом:** The `config.json.j2` template emitted one `{"auths": {...}}` per entry instead of merging them into a single `auths` map, so the JSON had duplicate top-level keys and image pulls from authenticated registries failed
- **Затронутые CIs:** —  ·  _>=v2.29.0 <=v2.29.1_
- **Root cause:** Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0` · Confirmed via the merged PR #12845 and the tag code
- **Workaround / fix:** Root cause fixed by PR #12845 (in `roles/container-engine/cri-o/templates/config.json.j2`). Workaround before upgrading: define a single merged `crio_registry_auth` structure, or patch the auth file by hand. The durable fix is to upgrade to `v2.30.0` or later
- **Источник:** `kb/troubleshooting/crio-registry-auths-duplicate.md`

### KEDB-148 · CRI-O: short-name image pull fails (unqualified-search-registries)
- **Симптом:** `ErrImagePull`: `short-name ... did not resolve to an alias and no unqualified-search registries are defined` (or a short-name prompt in strict mode)
- **Затронутые CIs:** cri-o, registry, runtime  ·  _>=v2.29.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies to Kubespray **v2.29.0–v2.31.0** with CRI-O . Kubespray writes registry config to **`/etc/containers/registries.conf.d/`** from the **`crio_registries`** variable, including `01-unqualified.conf` for entries flagged `unqualified: true`
- **Workaround / fix:** This is a **CRI-O-vs-containerd difference** — manifests that "just worked" on containerd (which defaults to docker.io) break on CRI-O. Prefer fully-qualified names for portability
- **Источник:** `kb/troubleshooting/crio-short-name-registry.md`

### KEDB-149 · GPU Operator upgrade: management pods lose GPUs (CDI default-on)
- **Симптом:** GPU management/tooling pods using `NVIDIA_VISIBLE_DEVICES` no longer get devices injected · Operator/components fail to schedule or are unsupported on **K8s 1.29** nodes · On OpenShift, CDI is not enabled after upgrade even though it should be
- **Затронутые CIs:** gpu, nvidia, upgrade  ·  _>=25.10.0_
- **Root cause:** Applies to gpu-operator **≥25.10** (owner runs 25.10.1; latest 26.3.3 — )
- **Workaround / fix:** CRI-O pods stuck `Init:RunContainerError`/`CreateContainerError` on install/upgrade; the Container Toolkit overwrites `imports` in the top-level containerd config; on 25.10.1 with SELinux enforcing, MIG Manager scheduling fails via GFD permissions (use the Node Feature API as a workaround)
- **Источник:** `kb/troubleshooting/gpu-operator-cdi-runtimeclass.md`

### KEDB-150 · ImagePullBackOff: 429 Too Many Requests (registry rate limit)
- **Симптом:** Public registries rate-limit anonymous/low-tier pulls. Large clusters pulling the same public image on many nodes hit the limit
- **Затронутые CIs:** operations, containerd  ·  _>=v2.29.0 <=v2.31.0_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` clusters. This is a general Kubernetes/component operational issue (not tied to one Kubespray version); the relevant tunables are noted in Known Issues
- **Workaround / fix:** Use an authenticated pull (image pull secret / registry auth), mirror images into an internal registry (PRACTICE-OFFLINE_ENVIRONMENT), or use `download_run_once` so images are fetched once and distributed. Avoid `imagePullPolicy: Always` for public images at scale
- **Источник:** `kb/troubleshooting/image-pull-rate-limit.md`

### KEDB-151 · kubeadm join fails (token, discovery CA hash, API reachability)
- **Симптом:** `kubeadm join` errors: `couldn't validate the identity of the API Server`, `token … not found` / `token has expired`, `could not find a JWS signature`, discovery timeout · The new node never appears / stays `NotReady`
- **Затронутые CIs:** kubeadm, nodes, join  ·  _>=v2.29.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies to Kubespray **v2.29.0–v2.31.0** / Kubernetes **1.29–1.35**. Kubespray generates a fresh bootstrap token per run, so token-expiry is rarely the issue on a normal re-run
- **Workaround / fix:** Re-joining a node that was removed without cleanup fails on leftovers in `/etc/kubernetes` and `/var/lib/etcd` — reset the node first
- **Источник:** `kb/troubleshooting/kubeadm-join-node.md`

### KEDB-152 · kubectl top / metrics-server x509 on the kubelet serving certificate
- **Симптом:** `kubectl top nodes` / `kubectl top pods` → `Metrics API not available` / `error: metrics not available yet` · metrics-server logs: `x509: cannot validate certificate for <node-ip> because it doesn't contain any IP SANs`, or `certificate signed by unknown authority` · Or, after enabling server-cert rotation: kubelet has no serving cert and `CertificateSigningRequest`s sit **Pending**
- **Затронутые CIs:** kubelet, certificates, metrics-server, tls  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0`. Relevant defaults: · `kubelet_rotate_server_certificates: false` — kubelet does **not** request a cluster-signed serving cert; it self-signs (`serverTLSBootstrap` unset in the kubelet config — see ) · `metrics_server_kubelet_insecure_tls: true` — metrics-server skips kubelet cert verification, so `kubectl top` works despite the self-signed cert · `kubelet_csr_approver_enabled…
- **Workaround / fix:** **Don't enable `serverTLSBootstrap` by hand** without an approver — the kubelet's serving CSRs stay `Pending`, the kubelet has no serving cert, and `kubectl logs/exec`, metrics, and probes to the kubelet break. Use `kubelet_rotate_server_certificates`, which brings the approver with it · The self-signed kubelet cert has **no IP SANs**, which is exactly why strict verification fails — verification requires the rotated…
- **Источник:** `kb/troubleshooting/kubelet-serving-cert-tls.md`

### KEDB-153 · kubelet crash-loop после апгрейда: неверный отступ server: в kubelet.conf
- **Симптом:** Задача `lineinfile` в `roles/kubernetes/kubeadm/tasks/main.yml` записывает строку `server:` с жёстко заданным отступом в 4 пробела, из-за чего поле оказывается вне вложенного блока `cluster:` в `kubelet.conf` (kubeadm-стиль требует 8 пробелов для вложенных полей). kubelet не находит server для кластера. Проявляется при включённом локальном балансировщике apiserver (localhost LB)
- **Затронутые CIs:** kubelet, kubeadm, upgrade  ·  _v2.31.0 / >=v1.35_
- **Root cause:** Затронуто: v2.31.0 (прямая связь с дефолтным Kubernetes 1.35 и localhost LB) · Исправлено: пока нет (PR #13284 открыт). Держать на контроле · Условие срабатывания: апгрейд на Kubernetes 1.35+ при включённом localhost LB
- **Workaround / fix:** Корневая причина: задача `lineinfile` жёстко задаёт отступ 4 пробела для строки `server:`, что выводит поле за пределы вложенного блока `cluster:`. Предложенный фикс — PR [#13284](https://github.com/kubernetes-sigs/kubespray/pull/13284) (использует `backrefs: true` с сохранением исходного отступа). PR открыт, не влит — исправления в релизе пока нет. Issue [#13277](https://github.com/kubernetes-sigs/kubespray/issues/1…
- **Источник:** `kb/troubleshooting/kubelet-conf-server-indent-crashloop.md`

### KEDB-154 · kubelet fails to start after upgrade — removed flags (--keep-terminated-pod-volumes 1.31, --cloud-config 1.34, --pod-infra-container-image 1.35)
- **Симптом:** After a Kubespray upgrade, a node goes `NotReady`; `systemctl status kubelet` / the kubelet log shows **`unknown flag: --<name>`** or `failed to parse kubelet flag` · The node's kubelet won't come up until the offending flag is removed
- **Затронутые CIs:** kubernetes, kubelet, upgrade  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Removed flags by version (Urgent Upgrade Notes — ): · **`--keep-terminated-pod-volumes`** — removed **K8s 1.31** (Kubespray v2.29.0) (#122082) · **`--cloud-config`** — removed **K8s 1.34** (#130161) · **`--pod-infra-container-image`** — removed **K8s 1.35** (#133779). kubeadm does **not** strip it if it was passed as an extra kubelet arg · Kubespray sets kubelet flags via named vars and the `kubelet_custom_flags` / e…
- **Workaround / fix:** **Fix:** remove the dropped flag from inventory (`kubelet_custom_flags` / any `*_extra_args`) and from the node's kubelet env, then restart kubelet / re-run the node. For `--pod-infra-container-image`, the equivalent is now the runtime's sandbox image config (containerd `sandbox_image`), not a kubelet flag · **Pre-upgrade audit (the real fix):** before crossing 1.31 / 1.34 / 1.35, grep the inventory for these flags a…
- **Источник:** `kb/troubleshooting/kubelet-removed-flags.md`

### KEDB-155 · kubelet: image GC can't reclaim disk — 'freed 0 bytes'
- **Симптом:** kubelet: `failed to garbage collect required amount of images. Wanted to free … bytes, but freed 0 bytes`; node stays under `nodefs` pressure; DiskPressure taint/evictions
- **Затронутые CIs:** kubelet, disk, nodes  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35**. Governed by `imageGCHighThresholdPercent` / `imageGCLowThresholdPercent` (defaults **85 / 80**)
- **Workaround / fix:** `freed 0 bytes` is a **symptom of misattribution** — chasing image GC when logs/emptyDir are the culprit wastes time. Measure first
- **Источник:** `kb/troubleshooting/kubelet-image-gc.md`

### KEDB-156 · kubelet: memory leak / systemd resets kubepods.slice limit → OOM
- **Симптом:** kubelet RSS grows over days; workloads get OOM-killed while kubelet survives; `kubectl top nodes` = `<unknown>`, `crictl stats` hangs · With `--kube-reserved`/`--system-reserved` + systemd driver, the enforced limit on `kubepods.slice` intermittently **jumps to full RAM** → pods/daemons OOM-killed
- **Затронутые CIs:** kubelet, memory, cgroup  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35**. Related: PLEG stalls , cgroup driver
- **Workaround / fix:** Because kubelet has a protective OOM score, node memory pressure manifests as **workload** OOM-kills, masking the real culprit — check kubelet's own RSS trend
- **Источник:** `kb/troubleshooting/kubelet-memory-oom.md`

### KEDB-157 · kubelet: PLEG is not healthy → node flaps NotReady / mount timeouts
- **Симптом:** `PLEG is not healthy: pleg was last seen active 3m5s ago; threshold is 3m0s` (delta grows); node flaps NotReady · Pods stuck `ContainerCreating` 5–6 min: `Unable to attach or mount volumes ...: timed out waiting for the condition`, then `MountVolume.SetUp succeeded` minutes later
- **Затронутые CIs:** kubelet, nodes, runtime  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35** on containerd . A **1.33.7 vs 1.32.5 regression** stretched PLEG-unhealthy recovery (~900 pods, 3-node reboot) from ~30 min to ~90 min with no CPU/mem/IO pressure (issue #137798)
- **Workaround / fix:** No merged fix for the 1.33.7 recovery regression — reduce density/churn and speed up the runtime as mitigation
- **Источник:** `kb/troubleshooting/kubelet-pleg-not-healthy.md`

### KEDB-158 · kubelet: serving cert rotation silently skipped → :10250 TLS failures
- **Симптом:** `kubelet_certificate_manager_server_rotation_seconds_count` stays **0** for 38+ days on some nodes; no `kubelet-serving` CSR submitted; then serving-cert expiry → x509 on :10250
- **Затронутые CIs:** kubelet, certificates, tls  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35** (reported 1.34.4, EKS/Bottlerocket, ~15–20% of long-lived nodes; **root cause not maintainer-confirmed** — `confidence: probable`, issue #138763). The x509-at-use symptom overlaps
- **Workaround / fix:** Distinct from the metrics-server x509 caused by an **unsigned/self-signed** serving cert — here the cert simply **expired** because rotation stalled
- **Источник:** `kb/troubleshooting/kubelet-serving-cert-rotation.md`

### KEDB-159 · Node memory below Kubespray minimum (1500/1024 MB)
- **Симптом:** Preinstall stops on `Stop if memory is too small for control plane nodes` or `Stop if memory is too small for nodes` because `ansible_memtotal_mb` is below the threshold for that host's role
- **Затронутые CIs:** preflight, resources, memory  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0`; defaults `minimal_master_memory_mb: 1500`, `minimal_node_memory_mb: 1024` · The control-plane check runs for hosts in `kube_control_plane`; the node check for hosts in `kube_node`. A host in both groups must clear the higher (control-plane) bar · `ansible_memtotal_mb` is total physical memory as seen by Ansible facts
- **Workaround / fix:** **Fix:** resize the VM/host to meet the floor (≥1500 MB control-plane, ≥1024 MB worker). Plan for real headroom — reserve capacity with `kube_reserved` / `system_reserved` (see ) · The thresholds are overridable (`minimal_master_memory_mb` / `minimal_node_memory_mb`) but lowering them only defers the problem — the control plane (etcd, apiserver) is memory-hungry and will OOM or thrash on undersized nodes · Facts must…
- **Источник:** `kb/troubleshooting/node-memory-too-small.md`

### KEDB-160 · node-feature-discovery: feature labels not applied
- **Симптом:** Nodes lack `feature.node.kubernetes.io/...` labels · GPU/feature-gated pods stay `Pending` (nodeSelector/affinity unmatched) · Some nodes labeled, others not
- **Затронутые CIs:** node-feature-discovery, scheduling, nodes  ·  _>=1.29 <=1.35 / >=0.16.0 <=0.19.0_
- **Root cause:** Applies to NFD **0.16–0.19** (base 0.16.4 — ). The GPU Operator bundles its own NFD — watch for **two NFD instances**
- **Workaround / fix:** Label prefix/namespace changes across NFD versions can break selectors after an upgrade — confirm the label key the current version emits
- **Источник:** `kb/troubleshooting/nfd-labels-missing.md`

### KEDB-161 · Spegel: image pulls not served by the mirror
- **Симптом:** Image pulls hit the external registry despite Spegel running; no P2P traffic between nodes · Registry-outage doesn't fall back to peers as expected
- **Затронутые CIs:** spegel, registry, containerd  ·  _>=0.0.1 <=0.7.4_
- **Root cause:** Applies across Spegel **0.0.1–0.7.4** (owner pins 0.0.1; current 0.7.4 — ). Spegel gates on **containerd**, not the K8s version
- **Workaround / fix:** Huge version gap (0.0.1 → 0.7.4): upgrading brings the containerd-2.1 requirement and config changes — validate `certs.d` and `discard_unpacked_layers` after any bump
- **Источник:** `kb/troubleshooting/spegel-mirror-not-used.md`

### KEDB-162 · too many open files / inotify watch exhaustion (kernel limits at scale)
- **Симптом:** Pods/containers log `too many open files`, `inotify_add_watch … No space left on device`, `failed to create fsnotify watcher`, or `pipe2: too many open files`; controllers/log agents crash under load. Nodes at high pod density are the usual place
- **Затронутые CIs:** kernel, sysctl, scale, nodes  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` · The relevant kernel knobs: · `fs.inotify.max_user_instances` — inotify instances per user (Kubespray sets **8192**) · `fs.inotify.max_user_watches` — total watches per user (default distro value is often too low for dense nodes) · `fs.file-max` / `fs.nr_open` — system/per-process open file descriptors · `nofile` ulimit — per-process FD limit (systemd `LimitNOFILE`, container…
- **Workaround / fix:** **inotify watches:** add to inventory ```yaml additional_sysctl: · { name: fs.inotify.max_user_watches, value: 524288 } · { name: fs.inotify.max_user_instances, value: 8192 } ``` `additional_sysctl` is applied by the preinstall role, so the values survive reboots and re-runs (don't hand-edit `/etc/sysctl.conf` — Kubespray manages it) · **file descriptors:** raise `fs.file-max`/`fs.nr_open` via `additional_sysctl`, an…
- **Источник:** `kb/troubleshooting/inotify-file-limits.md`

