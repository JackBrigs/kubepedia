# KEDB · addons

_13 известных ошибок. Сгенерировано; не править руками._

### KEDB-176 · Argo CD 2.12+ redis/haproxy moved DockerHub→ECR — pull fails in air-gapped/mirrored clusters
- **Симптом:** After upgrading Argo CD (Kubespray v2.27.0 → v2.28.0+, i.e. 2.11 → 2.14.x), `argocd-redis-ha-*` and `argocd-redis-ha-haproxy-*` pods are `ImagePullBackOff` / `ErrImagePull` · Or the pods are **rejected at admission** by an image-signature / approved-registry policy that doesn't include AWS ECR · Argo CD itself (server/repo-server/controller) may be up, but sync/HA is degraded because Redis HA is down
- **Затронутые CIs:** argocd, offline, registry  ·  _>=v2.28.0 <=v2.31.0 / >=1.29 <=1.35 / >=2.12.0 <=2.14.21_
- **Root cause:** Applies to Argo CD **2.12+** (so Kubespray **v2.28.0–v2.31.0**, which ships 2.14.x — / ). Kubespray pins Argo CD 2.11.0 in v2.27.0 where the images were still on DockerHub; the move bites on the jump to v2.28.0+ · Root cause: the bundled `redis-ha` Helm chart bump changed the default image registry for the redis and haproxy images to ECR (`docs/operator-manual/upgrading/2.11-2.12.md`@v2.12.0). Non-HA mode (single `ar…
- **Workaround / fix:** **Fix (mirrored/offline — ):** mirror the ECR redis-ha images into your private registry **before** upgrading, and override the chart image registry/repository so the pods pull from the mirror ( for the general mirror/override pattern) · **Fix (policy-restricted):** add the AWS ECR registry to the Cosign / approved-registry allow-list before upgrading, or re-sign the mirrored images under your own registry · **Pre-up…
- **Источник:** `kb/troubleshooting/argocd-redis-ecr-airgap.md`

### KEDB-177 · ArgoCD Application stuck OutOfSync / Progressing / sync fails
- **Симптом:** `kubectl -n argocd get application <app>` (or the UI) shows `OutOfSync`, `SyncFailed`, or `Progressing`/`Degraded` that never settles; the sync operation errors or loops
- **Затронутые CIs:** gitops, argocd, deployment  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` with ArgoCD (, ) · ArgoCD applies manifests **as its own ServiceAccount** and then evaluates health — a failure at either step surfaces as "not synced"
- **Workaround / fix:** **`SyncFailed: forbidden`** — the ArgoCD application-controller SA lacks RBAC to create that resource/kind. Grant it (least-privilege) · **`failed calling webhook`** — an admission webhook rejects/blocks the applied objects · **CRD ordering (`no matches for kind`)** — the CR is applied before its CRD exists. Use **sync waves** / `Replace=true` / apply the CRD first, or enable `ServerSideApply` · **Perpetual OutOfSync…
- **Источник:** `kb/ecosystem/argocd-app-outofsync.md`

### KEDB-178 · Dragonfly operator: failover data loss / replica readiness / auth / TLS
- **Симптом:** Data lost after a master pod termination / node drain · Replica shows Ready while still doing a full sync · Pods fail health checks after an operator upgrade (wrong port) · `NOAUTH Authentication required` on internal `SLAVE OF NO ONE` · TLS port logs flooded with `ssl3_get_record:wrong version number`
- **Затронутые CIs:** dragonfly, data, cache  ·  _>=1.29 <=1.35 / >=1.28.1_
- **Root cause:** Applies to dragonfly-operator ≥1.1.x / datastore **≥1.28.1** (owner runs op 1.1.11 / db 1.28.1 — )
- **Workaround / fix:** **Datastore 1.28.1 is affected by 3 CVEs** (CVE-2026-62357/-54341/-47206) — override `spec.image` to ≥1.40 · **Future landmines:** datastore **1.31.0** memory-growth/OOM regression; **1.35.0** restart loop (`accept system:22`) — avoid those versions
- **Источник:** `kb/troubleshooting/dragonfly-failover-dataloss.md`

### KEDB-179 · ECK/Elasticsearch: stuck ApplyingChanges, watermark, OOM, master election
- **Симптом:** `Elasticsearch` phase stuck `ApplyingChanges`; pods never roll · Writes fail with `index has read-only-allow-delete block` / `TOO_MANY_REQUESTS/12` · ES pods `OOMKilled` (exit 137); or the **operator itself** OOMKills on large clusters · `master not discovered or elected yet`
- **Затронутые CIs:** elasticsearch, eck, data  ·  _>=1.29 <=1.33 / >=3.0.0 <=3.4.1_
- **Root cause:** Applies to ECK **3.0–3.4** managing Elasticsearch 8.x/9.x (owner runs 3.1.0 — )
- **Workaround / fix:** **Upgrade ordering:** ES Stack 9.0.0 needs ECK ≥3.0.0 and must pass through 8.18 (validation-enforced); downgrades blocked (recover via `eck.k8s.elastic.co/disable-downgrade-validation=true`) · Expired **custom transport CA** causes an endless cert-rotation loop (`x509: certificate has expired`) — update the CA secret (issue #8952) · Elasticsearch 8.x/9.x carry their own ESA advisories (Tika XXE ESA-2025-14, PKI-real…
- **Источник:** `kb/troubleshooting/elasticsearch-eck-cluster.md`

### KEDB-180 · Gateway API v1.4.1: download fails due to a checksum mismatch
- **Симптом:** With `gateway_api_enabled: true`, installation or upgrade to v2.30.0 fails at the `download` stage because the pinned checksum for the Gateway API v1.4.1 `standard-install.yaml` manifest no longer matches the downloaded artifact
- **Затронутые CIs:** gateway-api, download  ·  _v2.30.0_
- **Root cause:** Affected versions: v2.30.0 (when `gateway_api_enabled: true`) · Fixed versions: v2.31.0 (master). The backport merged into the release-2.30 branch (to ship in a future v2.30.1 — not yet released at time of this entry) · Trigger: `gateway_api_enabled: true` while downloading the Gateway API v1.4.1 manifest
- **Workaround / fix:** Root cause: the upstream Gateway API v1.4.1 release artifact was rewritten AFTER the v2.30.0 tag was cut, so the checksum baked into Kubespray became invalid. Fix: PR #13006 "Fix Gateway API v1.4.1 unexpected checksum change" (master → v2.31.0), backport to the release-2.30 branch PR #13010. Issue #13122. Workaround on v2.30.0: pin `gateway_api_version: "1.4.0"` in inventory (the 1.4.0 artifact is unaffected), or dis…
- **Источник:** `kb/troubleshooting/gateway-api-1.4.1-checksum-mismatch.md`

### KEDB-181 · GitLab Agent (agentk): not connecting to KAS — token, KAS address/wss, egress/proxy, config project
- **Симптом:** The agent shows **not connected** in GitLab; `agentk` logs repeat connection/handshake errors; GitOps syncs and CI cluster access don't work
- **Затронутые CIs:** —  ·  _>=1.33 <=1.35 / >=18.11.0_
- **Root cause:** GitLab Agent `agentk 18.11.0` ; pull-based GitOps + CI tunnel · **Token:** agentk registers with a token from the agent's record; a revoked/rotated/wrong token → auth failure on connect · **KAS address:** the `--kas-address` (wss URL, e.g. `wss://kas.gitlab.example.com`) must be correct and TLS-valid; self-hosted GitLab must have KAS enabled and exposed · **Egress/proxy:** the tunnel is a long-lived **WebSocket**; a …
- **Workaround / fix:** **Token — fix:** re-create the agent token in GitLab and update the agent's secret; each agentk uses its own token · **KAS address — fix:** set the correct `wss://` KAS URL with a valid cert; confirm KAS is enabled on self-hosted GitLab · **Egress — fix:** allow wss egress to KAS; set proxy vars; ensure idle-timeouts don't cut the tunnel · **Config — fix:** add `.gitlab/agents/<name>/config.yaml` to the agent's proje…
- **Источник:** `kb/troubleshooting/gitlab-agent-connection.md`

### KEDB-182 · GitLab Runner (Kubernetes executor): job pods fail/pending/OOM
- **Симптом:** `prepare environment: context deadline exceeded` / `timed out waiting for pod to start` · `ErrImagePull`/`ImagePullBackOff` for job/service images despite secrets · `pods is forbidden: ... serviceaccount:<ns>:default cannot create pods` · Helper/build container `OOMKilled` (137); or OOM pod **hangs** until timeout · `Could not resolve host`; DIND `SSL_connect: SSL_ERROR_SYSCALL`
- **Затронутые CIs:** gitlab-runner, ci  ·  _>=1.29 <=1.35 / >=16.10.0 <=18.4.0_
- **Root cause:** Applies to Runner **16.10–18.4** (owner runs 18.4.0 and 16.10.0 — )
- **Workaround / fix:** Chart 0.81.0 bumped `ExternalSecret` to `v1` (external-secrets operator must support it) · The **Ubuntu helper image ships a vulnerable git** (**CVE-2025-48384**, HIGH) — update the helper git (issue #39046). "runner" CVEs in GitLab server releases are a different product
- **Источник:** `kb/troubleshooting/gitlab-runner-k8s-executor.md`

### KEDB-183 · ImagePullBackOff / ErrImagePull (triage)
- **Симптом:** `kubectl get pod` shows `ErrImagePull`/`ImagePullBackOff`; `kubectl describe pod` → `Failed to pull image "…": … <reason>`. The pod stays `ContainerCreating` meanwhile
- **Затронутые CIs:** images, registry, pods  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` (`container_manager: containerd` — same triage for CRI-O/Docker with runtime-specific config) · The kubelet asks the CRI to pull; registry resolution/auth/TLS use the runtime's config
- **Workaround / fix:** **`manifest unknown` / `not found` / `repository does not exist`** — wrong image name, tag, or registry host; the tag/digest doesn't exist. Fix the reference. (A private image can also masquerade as "not found" when auth is missing — check auth too.) · **`unauthorized` / `pull access denied` / `401`/`403`** — the registry needs credentials. Add an `imagePullSecret` to the pod's ServiceAccount, or configure runtime-le…
- **Источник:** `kb/troubleshooting/imagepullbackoff.md`

### KEDB-184 · k8up: stale restic locks, false success, permission/empty backups
- **Симптом:** `unable to create lock in backend: repository is already locked exclusively by PID <n>` · Backup pod stuck `1/2 Ready` though logs say "finished successfully" · Backup marked `Succeeded` while logs show `exit code 1 / source file could not be read` · Backup pod `Pending`: `node(s) had volume node affinity conflict` · Snapshot created but empty / `Permission denied` on the app's mount afterwards
- **Затронутые CIs:** k8up, backup, restic  ·  _>=1.29 <=1.35 / >=2.12.0 <=2.15.0_
- **Root cause:** Applies to k8up app **2.12–2.15** (owner runs chart 4.8.4 / app 2.12.0 — )
- **Workaround / fix:** **CRDs are not installed by the chart** — install/upgrade them separately (the `k8upcrd` chart) · **Future landmine:** k8up **4.9.0** switches pod-exec SPDY→WebSocket (app-aware backups) — set `INSECURE_ALLOW_PODEXEC_SPDY_FALLBACK=true` if needed (PR #1183)
- **Источник:** `kb/troubleshooting/k8up-backup-issues.md`

### KEDB-185 · Prometheus targets DOWN on a Kubespray cluster (control-plane / kubelet / etcd)
- **Симптом:** In Prometheus/VM, `up == 0` for `kube-controller-manager`, `kube-scheduler`, `kubelet`, `etcd`, or `kube-proxy` targets; errors like `connection refused`, `x509: certificate signed by unknown authority`, or `server returned HTTP 401`
- **Затронутые CIs:** observability, prometheus, monitoring  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` · Relevant Kubespray wiring: with hardening, `kube_controller_manager_bind_address` / `kube_scheduler_bind_address` = **`127.0.0.1`** ; the kubelet serves metrics over TLS with a (default) self-signed cert; etcd metrics are TLS-protected
- **Workaround / fix:** **CM / scheduler DOWN (`connection refused`)** — they're bound to `127.0.0.1`, so a Prometheus pod elsewhere can't reach them. Options: bind them to a routable address (`kube_controller_manager_bind_address` / `kube_scheduler_bind_address` = `0.0.0.0` or the node IP), or scrape via a node-local sidecar / hostNetwork. Weigh the security trade-off ( hardened them on purpose) · **kubelet DOWN (`x509`)** — the scrape doe…
- **Источник:** `kb/ecosystem/prometheus-target-down.md`

### KEDB-186 · RabbitMQ operator: cluster not forming / pods not joining
- **Симптом:** `RabbitmqCluster` stuck not-ready; pods `0/1` or restarting · Nodes run standalone instead of clustering; `rabbitmqctl cluster_status` shows one node · Quorum queues unavailable after losing nodes
- **Затронутые CIs:** rabbitmq, messaging  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to the official operator and the Bitnami-packaged one
- **Workaround / fix:** Bitnami chart 3.7.0 images moved to `bitnamilegacy` → `ImagePullBackOff` if not repointed; its broker 3.11.21 has CVE-2023-46118. Official operator's default broker 4.x has its own 3→4 constraints
- **Источник:** `kb/troubleshooting/rabbitmq-cluster-not-forming.md`

### KEDB-187 · VictoriaMetrics: vmagent not ingesting / remote-write backlog
- **Симптом:** Dashboards show gaps / no data for some targets · `vmagent` persistent queue (`-remoteWrite.tmpDataPath`) grows; `vmagent_remotewrite_*` error metrics rise · vmstorage/vmsingle OOM or rejecting samples
- **Затронутые CIs:** victoriametrics, observability, metrics  ·  _>=1.100.0 <=1.147.0_
- **Root cause:** Applies to the VM stack **1.100–1.147** (owner runs 1.115.0 — , )
- **Workaround / fix:** VM **1.115.0** is affected by a low-severity Snappy-decoder DoS (**CVE-2025-65942**, fixed 1.122.8)
- **Источник:** `kb/troubleshooting/vmagent-remote-write-failing.md`

### KEDB-188 · Zalando postgres-operator: cluster not ready / failover issues
- **Симптом:** `postgresql` resource never reaches `Running`; pods `0/1` or `CrashLoopBackOff` · No primary after a node failure (all replicas, no leader) · Connections refused / read-only
- **Затронутые CIs:** postgresql, zalando, data  ·  _>=1.29 <=1.35 / >=1.13.0 <=1.15.1_
- **Root cause:** Applies to postgres-operator **1.13–1.15** (owner runs 1.14.0 — ). Manages PostgreSQL 13–17 (PG12 dropped in 1.14)
- **Workaround / fix:** 1.14.0 changed SYNC/UPDATE **log message format** — log-based alerting may need updating · The Spilo (PostgreSQL) image carries its own CVE stream — track image updates separately from the operator
- **Источник:** `kb/troubleshooting/postgres-operator-cluster-not-ready.md`

