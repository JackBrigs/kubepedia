# KEDB · other

_35 известных ошибок. Сгенерировано; не править руками._

### KEDB-189 · 1Password Connect: secrets not served / sync failing — credentials JSON, Connect token, vault scope
- **Симптом:** Consumers get `401/403` from Connect, `connect-sync` crashloops or can't authenticate, or external- secrets reports the 1Password provider unauthorized
- **Затронутые CIs:** —  ·  _>=1.29 <=1.35 / >=1.7.3_
- **Root cause:** 1Password Connect `1.7.3` ; part of the secrets layer · **Credentials JSON:** connect-sync needs the `1password-credentials.json` (from `op connect server create`) mounted as a Secret; missing/base64-mangled → sync won't start · **Connect token:** clients (external-secrets) authenticate with a **Connect token** issued for that Connect server; a wrong/expired token → 401 · **Vault scope:** the token is scoped to speci…
- **Workaround / fix:** **Credentials — fix:** recreate the `1password-credentials.json` secret exactly as produced by `op connect server create` (don't re-encode); restart connect-sync · **Token — fix:** issue a fresh Connect token for this server and update the consumer's secret · **Vault scope — fix:** grant the token access to the vault holding the item (scopes are per-vault)
- **Источник:** `kb/troubleshooting/1password-connect-sync.md`

### KEDB-190 · Alertmanager: alerts not notifying / silences not silencing / config not reloading / duplicate pages (HA)
- **Симптом:** Prometheus shows an alert `FIRING`, but **no email/Slack/PagerDuty** notification is delivered · A **silence** is created but the alert **still notifies** · You edit the Alertmanager config, but behaviour **doesn't change** · With 2+ replicas, a single alert **notifies twice** (duplicate pages)
- **Затронутые CIs:** observability, alerting, alertmanager  ·  _>=1.29 <=1.35 / >=0.25.0_
- **Root cause:** Applies to Alertmanager `>=0.25.0` (the addon chart, ); part of the observability stack · **Routing tree:** an alert walks the `route` tree; the **first matching** route wins unless `continue: true`. A too-greedy top route or a receiver with **no notifier configured** (a "null" receiver) silently swallows alerts · **Grouping/timing:** `group_wait`, `group_interval`, `repeat_interval` **delay** and **batch** notificat…
- **Workaround / fix:** **No notification — fix:** run `amtool config routes test` with the alert's labels to see the actual receiver; confirm that receiver has a real notifier (not a null receiver) and that a parent route isn't catching it first without `continue`. Account for `group_wait`/`repeat_interval` before declaring it lost. Check receiver auth/TLS (SMTP creds, Slack webhook URL, proxy) · **Silence not silencing — fix:** copy the a…
- **Источник:** `kb/troubleshooting/alertmanager-notifications.md`

### KEDB-191 · AWX Operator: AWX instance stuck deploying — Postgres PVC, migrations, admin secret, resources
- **Симптом:** After creating an `AWX` CR, the instance never becomes ready: `awx-*` pods `Pending`/`CrashLoop`, the operator reconcile loops, or the web UI never serves
- **Затронутые CIs:** automation, awx, operator  ·  _>=1.29 <=1.35 / >=24.6.1_
- **Root cause:** AWX Operator `2.19.1` → AWX `24.6.1` ; defaults to **PostgreSQL 15** + Redis 7 · **Postgres storage:** the managed Postgres needs a **PVC** that binds; no default StorageClass or a `Pending` PVC stalls the whole instance (AWX won't start without its DB) · **Migrations:** the operator runs a **migration** step against Postgres; if Postgres isn't ready or creds mismatch, the task/web pods crashloop waiting on the schem…
- **Workaround / fix:** **Postgres PVC — fix:** ensure a default/working StorageClass so the DB PVC binds; the instance can't progress until Postgres is `Running` · **Migrations/crashloop — fix:** confirm Postgres is up and the DB creds secret matches; the task/web pods recover once migrations complete · **Admin login — fix:** read the generated `<name>-admin-password` secret (or set your own before apply); don't recreate it after first dep…
- **Источник:** `kb/troubleshooting/awx-operator-issues.md`

### KEDB-192 · bastion-ssh-config: misspelled variable ssh_bastion_confing__name
- **Симптом:** A typo in the variable name meant any override of the intended `ssh_bastion_config_name` was ignored. The fix renames it to `ssh_bastion_config_name`
- **Затронутые CIs:** —  ·  _>=v2.29.0 <=v2.30.0_
- **Root cause:** Affected Kubespray: `>=v2.29.0 <=v2.30.0`. Fixed in: `v2.31.0` · Confirmed via merged PR #13046 and the tag code
- **Workaround / fix:** Fixed by PR #13046 (in `roles/bastion-ssh-config/defaults/main.yml`). Workaround before upgrading: use the misspelled name to match the old code, or upgrade to v2.31.0 and use `ssh_bastion_config_name`. Durable fix: upgrade to `v2.31.0` or later
- **Источник:** `kb/troubleshooting/ssh-bastion-config-name-typo.md`

### KEDB-193 · control-plane: k8s-certs-renew script broken by bad quoting
- **Симптом:** In `k8s-certs-renew.sh.j2` an unquoted assignment made the shell try to execute it as a command; the variable was unused, so the fix simply removed the line. The broken line could make the renew timer/script error out
- **Затронутые CIs:** —  ·  _>=v2.29.0 <=v2.29.1_
- **Root cause:** Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0` · Confirmed via the merged PR #12876 and the tag code
- **Workaround / fix:** Root cause fixed by PR #12876 (in `roles/kubernetes/control-plane/templates/k8s-certs-renew.sh.j2`). Workaround before upgrading: renew certs manually with `kubeadm certs renew all` (see PRACTICE-CERTIFICATE_EXPIRY). The durable fix is to upgrade to `v2.30.0` or later
- **Источник:** `kb/troubleshooting/k8s-certs-renew-broken-script.md`

### KEDB-194 · control-plane: kube_override_hostname breaks first-control-plane delegation
- **Симптом:** Kubespray resolved the first control-plane node from kubectl output, which does not match `inventory_hostname` when `kube_override_hostname` is used; the fix stops depending on that mapping
- **Затронутые CIs:** —  ·  _>=v2.29.0 <=v2.29.1_
- **Root cause:** Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0` · Confirmed via the merged PR #12636 and the tag code
- **Workaround / fix:** Root cause fixed by PR #12636 (in `roles/kubernetes/control-plane/tasks/main.yml`). Workaround before upgrading: avoid `kube_override_hostname`, or upgrade so delegation no longer relies on the kubectl-to-inventory mapping. The durable fix is to upgrade to `v2.30.0` or later
- **Источник:** `kb/troubleshooting/control-plane-override-hostname-delegation.md`

### KEDB-195 · controller-manager: GC stuck (foregroundDeletion) / quota monitor not synced
- **Симптом:** An object deleted with `propagationPolicy=Foreground` keeps `finalizers: [foregroundDeletion]` + `deletionTimestamp` forever; dependents not collected · `ResourceQuota.status.used` stops updating → admission wrongly blocks (`exceeded quota`) or wrongly admits. Logs: `timed out waiting for quota monitor sync`, `quota monitor not synced`, `Failed to watch *v1.PartialObjectMetadata: ... operation not supported`
- **Затронутые CIs:** controller-manager, garbage-collection, resource-quota  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35**. Namespace-stuck-Terminating is a related finalizer/GC class
- **Workaround / fix:** Stripping a finalizer manually skips the intended cleanup — only do it when the owner/GC is genuinely wedged
- **Источник:** `kb/troubleshooting/kcm-reconcile-stalls.md`

### KEDB-196 · Deployment rollout stuck / not progressing
- **Симптом:** `kubectl rollout status deploy/<name>` never completes; `kubectl get deploy` shows `UP-TO-DATE`/`AVAILABLE` stuck below desired; `describe deploy` shows `ProgressDeadlineExceeded` or `ReplicaSetUpdated` not advancing
- **Затронутые CIs:** deployment, rollout, workloads  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` (Kubernetes-native rollout behaviour) · A `RollingUpdate` brings up new pods (up to `maxSurge`) and removes old ones (down to `maxUnavailable`) **only as new pods become Ready**. If new pods never go Ready, the rollout can't proceed; `progressDeadlineSeconds` (default 600s) then marks it failed
- **Workaround / fix:** **New pods failing** — the update shipped a bad image/config/probe; the new RS pods crash/can't pull/can't schedule. Fix the root (linked hubs above) or `kubectl rollout undo deploy/<name>` to revert while you investigate · **Readiness probe never passes** — pods run but never Ready (wrong path/port, too-short `initialDelaySeconds`); the rollout waits forever. Fix the probe · **`maxUnavailable: 0` + no room** — with …
- **Источник:** `kb/troubleshooting/rollout-stuck.md`

### KEDB-197 · Dex: OIDC login fails (redirect / connector / issuer)
- **Симптом:** Login returns `redirect_uri did not match` or `invalid client` · Blank page / connector error after choosing an identity provider · Tokens rejected by the relying app (issuer/audience mismatch)
- **Затронутые CIs:** dex, oidc, sso  ·  _>=1.29 <=1.35 / >=2.42.0 <=2.45.1_
- **Root cause:** Applies to Dex **2.42–2.45** (owner runs 2.42.0 — ). Often multiple Dex versions run (e.g. bundled with envoy-xds-controller) — keep issuer/config consistent
- **Workaround / fix:** Image scanners flag transitive CVE-2024-45338 in the 2.42.0 image (not a Dex-app CVE) — can fail CI gates
- **Источник:** `kb/troubleshooting/dex-oidc-login-fails.md`

### KEDB-198 · DiskPressure: pods evicted, images garbage-collected
- **Симптом:** kubelet enforces eviction thresholds; when the node/imagefs free space drops below them it evicts pods and garbage-collects images. Common on nodes with small `/var/lib/containerd` or heavy log/image churn
- **Затронутые CIs:** operations, operations  ·  _>=v2.29.0 <=v2.31.0_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` clusters. This is a general Kubernetes/component operational issue (not tied to one Kubespray version); the relevant tunables are noted in Known Issues
- **Workaround / fix:** Free space / grow the disk; prune unused images; set/verify `system_reserved` and eviction thresholds; move container/kubelet dirs to a larger volume. See PRACTICE-NODE_NOT_READY
- **Источник:** `kb/troubleshooting/disk-pressure-eviction.md`

### KEDB-199 · Download fails during deploy (binary/image/checksum)
- **Симптом:** A task like `Download_file | Download item` or `Download_container | …` fails with: connection timeout / `Failed to connect`, `certificate verify failed`, `HTTP Error 403/429`, or `Checksum mismatch` / `does not match` for a binary or image
- **Затронутые CIs:** download, offline, deploy  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0`. Relevant defaults: · `download_retries: 4` — retry count for downloads · `download_validate_certs: true` — verify TLS on downloads · `download_force_cache: false`, `download_run_once: false`, `download_localhost: false` — caching/delegation behaviour · Binaries come from `*_download_url` (default upstream: `dl.k8s.io`, GitHub, etc.); images from `*_image_repo` (default `regis…
- **Workaround / fix:** **Transient network / rate limit:** raise `download_retries`; for registry 429s use a mirror/pull-through · **TLS interception / self-signed proxy:** point downloads at a trusted mirror, or (lab only) `download_validate_certs: false` · **Checksum mismatch:** use a version Kubespray has checksums for; if a proxy corrupts/ replaces the file, fix the proxy. Do **not** blindly disable checksum verification — it protects …
- **Источник:** `kb/troubleshooting/download-fails.md`

### KEDB-200 · envoy-xds-controller: Envoy not receiving config — CRD errors, node-id mismatch, ADS connection, dex
- **Симптом:** Envoy comes up but serves nothing (no listeners), or `503`/`no healthy upstream`; the controller logs reject a CRD, or the Envoy logs can't reach the xDS server
- **Затронутые CIs:** —  ·  _>=1.29 <=1.35 / >=0.17.1_
- **Root cause:** envoy-xds-controller `0.17.1` ; related to Envoy control-plane concepts ( covers Envoy internals). Runs in multiple envs (exc/exc-stage/ exc-test), each paired with dex for the UI · **CRD invalid:** a bad VirtualService/Listener/Cluster CRD is dropped by the controller, so that config never reaches Envoy · **node-id mismatch:** Envoy identifies with a **node id/cluster**; the controller only sends config matching a k…
- **Workaround / fix:** **CRD invalid — fix:** `describe` the rejected CRD; correct the schema/reference so the controller includes it in the snapshot · **node-id — fix:** align Envoy's `--service-node`/`--service-cluster` with the controller's expected node id · **ADS — fix:** point Envoy's bootstrap xDS cluster at the controller's gRPC endpoint (address + TLS); confirm `config_dump` starts populating · **Data-plane image — fix:** supply a…
- **Источник:** `kb/troubleshooting/envoy-xds-controller-config.md`

### KEDB-201 · external-secrets: ExternalSecret not syncing to a Secret
- **Симптом:** Target `Secret` missing or empty; workload can't mount it · `ExternalSecret` shows `SecretSyncedError` / `Ready: False` · Values don't update after rotation in the backend
- **Затронутые CIs:** external-secrets, secrets  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to the external-secrets operator ; providers include Vault , 1Password, cloud secret managers
- **Workaround / fix:** The controller needs network egress to the provider — a blocked egress or a webhook/CA issue looks like an auth failure
- **Источник:** `kb/troubleshooting/external-secrets-not-syncing.md`

### KEDB-202 · Feast Operator: FeatureStore not reconciling — install needs Server-Side Apply, online/offline store, registry
- **Симптом:** `kubectl apply` of the operator manifests fails (`metadata.annotations: Too long`), or a `FeatureStore` stays not-ready with the operator reconcile erroring
- **Затронутые CIs:** —  ·  _>=1.29 <=1.35 / >=0.64.0_
- **Root cause:** Feast Operator `0.64.0` ; ships from the feast monorepo (no separate operator tag), installed via **kustomize + Server-Side Apply** · **Plain apply fails:** the CRDs exceed the client-side-apply annotation limit; you must use `kubectl apply --server-side` (or `kubectl apply -k ... --server-side`) · **Store connectivity:** a FeatureStore references an **online store** (e.g. Redis) and **offline store** + **registry**;…
- **Workaround / fix:** **Install fails — fix:** apply with **`--server-side`**: `kubectl apply -k <feast-operator-kustomize> --server-side --force-conflicts` · **FeatureStore not ready — fix:** `describe` for the failing store; fix the online (Redis)/offline/ registry connection strings and secrets · **Upgrades:** keep applying server-side to avoid field-manager conflicts on the big CRDs
- **Источник:** `kb/troubleshooting/feast-operator-featurestore.md`

### KEDB-203 · Flagger: canary stuck / rolls back — metrics provider, mesh/Gateway provider, MetricTemplate, webhooks
- **Симптом:** A `Canary` sits at weight 0 / "waiting", never promotes, or **rolls back** every attempt with "Halt advancement"
- **Затронутые CIs:** —  ·  _>=1.29 <=1.35 / >=1.40.0_
- **Root cause:** Flagger `1.40.0` . It needs (1) a **traffic provider** (Istio/Linkerd/NGINX/ Gateway API) to shift weight, and (2) a **metrics provider** (Prometheus by default) to judge success · **No metrics:** if the Prometheus URL is wrong or the query returns empty, Flagger treats it as a failed check and halts — "no values found" is a stall, not a pass · **No traffic shift:** a mesh/provider mismatch means weight never moves; …
- **Workaround / fix:** **No metrics — fix:** point Flagger at the right Prometheus (`--metrics-server` / provider address); test the query returns data for the canary's labels · **No traffic — fix:** confirm the mesh/Gateway provider matches the Canary `spec.provider` and the target Service/route exists · **MetricTemplate — fix:** validate the PromQL and threshold; loosen `interval`/`thresholdRange` while debugging · **Webhook — fix:** mak…
- **Источник:** `kb/troubleshooting/flagger-canary-stuck.md`

### KEDB-204 · Gigapipe/qryn: reads return nothing / writes rejected — ClickHouse backend, reader/writer split
- **Симптом:** Queries return **no data** though ingestion looks fine, or writes are **rejected** / dropped
- **Затронутые CIs:** observability, qryn, clickhouse  ·  _>=1.29 <=1.35 / 4.1.6_
- **Root cause:** Gigapipe `4.1.6` ; part of the observability layer · **Stateless over ClickHouse:** all state is in ClickHouse; if reader and writer point at different DBs/tables, the reader sees nothing the writer wrote · **ClickHouse health:** wrong DSN/creds, or an overloaded/misconfigured ClickHouse, breaks both read and write
- **Workaround / fix:** **No data — fix:** ensure reader and writer use the **same** ClickHouse DB/tables and that the writer's inserts succeed (check its logs) · **ClickHouse — fix:** correct the DSN/credentials; verify ClickHouse is reachable and healthy; create the schema if missing
- **Источник:** `kb/troubleshooting/gigapipe-qryn.md`

### KEDB-205 · Headlamp: can't log in / empty cluster view — token/OIDC auth and RBAC of the viewer
- **Симптом:** Login fails, or the UI loads but shows **no/partial resources**
- **Затронутые CIs:** ui, headlamp  ·  _>=1.29 <=1.35 / 0.43.0_
- **Root cause:** Headlamp `0.43.0`; a modern replacement for the retired kubernetes-dashboard · **Identity = RBAC:** Headlamp queries the API **as** the token/OIDC user; it can only show what that subject may `get`/`list`. An empty namespace list = missing RBAC, not a UI fault · **OIDC:** issuer/client/redirect misconfig blocks login entirely
- **Workaround / fix:** **Empty view — fix:** grant the viewer identity the needed (Cluster)RoleBinding; the UI reflects RBAC exactly · **Login — fix:** correct OIDC issuer/client/redirect, or use a valid ServiceAccount token; ensure the token isn't expired
- **Источник:** `kb/troubleshooting/headlamp-access.md`

### KEDB-206 · Karma: no alerts shown — can't reach Alertmanager instances / OAuth in front
- **Симптом:** Karma UI is empty / shows an Alertmanager as down, even though alerts are firing
- **Затронутые CIs:** observability, karma, alerting  ·  _>=1.29 <=1.35 / 0.121_
- **Root cause:** Karma `v0.121` , typically behind oauth2-proxy · **Upstream reachability:** Karma polls each Alertmanager's API; a wrong URL, network policy, or a down AM yields no alerts · **OAuth:** the fronting proxy can block the UI or the upstream calls if misconfigured
- **Workaround / fix:** **No alerts — fix:** correct the Alertmanager URI(s) in Karma's config and ensure network reachability; verify the AM itself is healthy · **OAuth — fix:** fix the proxy so it neither blocks the UI nor the upstream Alertmanager calls
- **Источник:** `kb/troubleshooting/karma-alertmanager-dashboard.md`

### KEDB-207 · kube-vip: excessive capabilities and version/tag mismatch
- **Симптом:** The manifest dropped/added capabilities incorrectly and the image tag was a literal rather than `v{{ kube_vip_version }}`; from the fix, capabilities are minimized and the tag derives from `kube_vip_version` (see COMPONENT-KUBE_VIP)
- **Затронутые CIs:** —  ·  _>=v2.29.0 <=v2.29.1_
- **Root cause:** Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0` · Confirmed via the merged PR #12835 and the tag code
- **Workaround / fix:** Root cause fixed by PR #12835 (in `roles/kubernetes/node/templates/manifests/kube-vip.manifest.j2`). Workaround before upgrading: pin `kube_vip_version` and verify the deployed image tag matches (see COMPONENT-KUBE_VIP). The durable fix is to upgrade to `v2.30.0` or later
- **Источник:** `kb/troubleshooting/kube-vip-capabilities-and-version.md`

### KEDB-208 · Kubespray preflight assertion fails ("Stop if …")
- **Симптом:** The playbook fails early (during `validate_inventory` or `preinstall`) with a task called `Stop if <something>` and an `assertion failed` / custom message, before any cluster changes are made
- **Затронутые CIs:** preflight, preinstall, inventory  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` · Two assertion stages run: **`validate_inventory`** (inventory-level, `run_once`) and **`kubernetes/preinstall` `0040-verify-settings.yml`** (per-host) · Most per-host checks are guarded by `when: not ignore_assert_errors`. Setting `ignore_assert_errors: true` **bypasses** them — an emergency escape hatch, not a fix; you then own the consequences (e.g. an under-provisioned or…
- **Workaround / fix:** `ignore_assert_errors: true` silences per-host checks globally — convenient for labs, dangerous in production (you can deploy onto an unsupported/undersized host that later fails in subtle ways). Prefer fixing the precondition · The `--limit` facts-cache check is easy to hit in CI: always run the `facts.yml` playbook first, or don't use `--limit` on the first run · CNI-specific asserts (cilium/calico/flannel) live in…
- **Источник:** `kb/troubleshooting/kubespray-preflight-fails.md`

### KEDB-209 · KVM device plugin: devices.kubevirt.io/kvm not schedulable — node not KVM-capable, plugin not registered
- **Симптом:** VM pods `Pending` with `Insufficient devices.kubevirt.io/kvm`, or the resource shows `0` on nodes
- **Затронутые CIs:** virtualization, device-plugin  ·  _>=1.29 <=1.35_
- **Root cause:** KVM device plugin ; no fixed public Helm chart version — verify the running image · **Node capability:** `/dev/kvm` must exist — bare-metal with VT-x/AMD-V, or a VM with **nested virtualization** enabled. Without it the plugin advertises nothing · **Registration:** the plugin DaemonSet must run on the node and register with the kubelet device-plugin socket
- **Workaround / fix:** **No /dev/kvm — fix:** enable virtualization/nested-virt on the node (BIOS or cloud instance setting); `/dev/kvm` must be present · **Not registered — fix:** ensure the plugin DaemonSet is scheduled on KVM nodes and healthy; restart it so it re-registers with the kubelet
- **Источник:** `kb/troubleshooting/kvm-device-plugin.md`

### KEDB-210 · Legacy ServiceAccount token secrets auto-invalidated/deleted (1.29+)
- **Симптом:** Auth failures for a workload that mounted a classic SA token Secret · kcm log: `"Delete auto-generated service account token" secret="<ns>/<name>"` — sometimes for a secret still referenced by an active pod
- **Затронутые CIs:** controller-manager, serviceaccount, auth  ·  _>=1.29 <=1.35_
- **Root cause:** `LegacyServiceAccountTokenCleanUp` is **beta and on by default from 1.29**. On upgrade, unused legacy token secrets get labeled `kubernetes.io/legacy-token-invalid-since` and are later deleted
- **Workaround / fix:** CI/integrations that hardcode a specific SA token Secret name are the usual victims — move them to bound tokens or an explicitly-created, `kubernetes.io/service-account-token` Secret you manage
- **Источник:** `kb/troubleshooting/kcm-sa-token-cleanup.md`

### KEDB-211 · Namespace stuck in Terminating
- **Симптом:** `kubectl get ns` shows a namespace `Terminating` indefinitely; `kubectl delete ns` hangs or returns but the namespace never disappears
- **Затронутые CIs:** namespace, finalizers, api  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` · The namespace controller deletes all contained objects, then removes the namespace's own `kubernetes` finalizer. It won't finish while (a) an object still has a **finalizer** pending, or (b) it **cannot list** a resource type because that API is down
- **Workaround / fix:** **Unavailable APIService** — restore or **delete** the broken APIService (`kubectl delete apiservice <name>`). A stale metrics-server / webhook API left registered after the backend is gone is the classic case; once discovery succeeds the namespace finishes on its own · **Stuck finalizer on an object** — the owning controller/operator is gone, so the finalizer is never cleared. Restore the controller, or remove the f…
- **Источник:** `kb/troubleshooting/namespace-stuck-terminating.md`

### KEDB-212 · OCI external cloud controller: wrong template filename in lookup
- **Симптом:** The OCI CCM task referenced a template name that did not match the actual file, so templating failed on OCI clusters. The fix corrects the filename
- **Затронутые CIs:** —  ·  _v2.30.0_
- **Root cause:** Affected Kubespray: `v2.30.0`. Fixed in: `v2.31.0` · Confirmed via merged PR #13151 and the tag code
- **Workaround / fix:** Fixed by PR #13151 (in `roles/kubernetes-apps/external_cloud_controller/oci/tasks/main.yml`). Workaround before upgrading: n/a beyond upgrading — it is an internal filename fix; upgrade to v2.31.0. Durable fix: upgrade to `v2.31.0` or later
- **Источник:** `kb/troubleshooting/oci-ccm-template-filename.md`

### KEDB-213 · OLM: Subscription/CSV stuck — CatalogSource unhealthy, InstallPlan needs approval, OperatorGroup
- **Симптом:** An operator installed via OLM never becomes ready: the `Subscription` shows no `installedCSV`, the `CSV` is stuck `Pending`/`InstallReady`, or `kubectl get installplan` shows one waiting
- **Затронутые CIs:** operators, olm, lifecycle  ·  _>=1.29 <=1.35 / >=0.32.0_
- **Root cause:** OLM v0 `0.32.0` : install flows **CatalogSource → Subscription → InstallPlan → CSV**. A stall at any hop blocks the operator · **CatalogSource unhealthy:** the catalog is served by a registry **pod**; if it's `ImagePullBackOff` (air-gap/rate limit — ) or crashing, the Subscription has no source to resolve from (`connecting`/`LastObservedState: TRANSIENT_FAILURE`) · **InstallPlan approval:** a Subscription with `insta…
- **Workaround / fix:** **CatalogSource — fix:** get the registry pod running (mirror the catalog image for air-gap); the Subscription re-resolves once the source is `READY` · **Manual approval — fix:** `kubectl patch installplan <ip> -n <ns> --type merge -p '{"spec":{"approved":true}}'` (or set `installPlanApproval: Automatic`) · **OperatorGroup — fix:** create a single OperatorGroup with the right target namespaces; remove duplicates · **…
- **Источник:** `kb/troubleshooting/olm-subscription-issues.md`

### KEDB-214 · openEuler: broken package metalink URL during bootstrap
- **Симптом:** The openEuler bootstrap task used a broken metalink URL; the fix corrects the repo configuration. openEuler-specific
- **Затронутые CIs:** —  ·  _v2.30.0_
- **Root cause:** Affected Kubespray: `v2.30.0`. Fixed in: `v2.31.0` · Confirmed via merged PR #13144 and the tag code
- **Workaround / fix:** Fixed by PR #13144 (in `roles/bootstrap_os/tasks/openEuler.yml`). Workaround before upgrading: fix the openEuler repo URL manually, or upgrade to v2.31.0. Durable fix: upgrade to `v2.31.0` or later
- **Источник:** `kb/troubleshooting/openeuler-metalink-url.md`

### KEDB-215 · Pod in CrashLoopBackOff (container keeps restarting)
- **Симптом:** `kubectl get pod` shows `CrashLoopBackOff` with a climbing `RESTARTS` count; `describe` shows `Back-off restarting failed container` and a `Last State: Terminated` with an exit code
- **Затронутые CIs:** pods, crashloopbackoff, lifecycle  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` (this is Kubernetes-native behaviour) · The back-off grows (10s → 20s → … capped at 5m by default). Kubernetes 1.32+ can tune this per node via `KubeletCrashLoopBackOffMax` (`CrashLoopBackOff.MaxContainerRestartPeriod`, `1s`–`300s`) — see ; tuning the delay does **not** fix the crash, it only paces restarts
- **Workaround / fix:** **App error / bad config** (exit 1/2, error in `--previous` logs) — fix the config (env vars, mounted ConfigMap/Secret values), missing files, or a bad command/entrypoint · **Missing dependency at start** (DB/service not reachable yet) — the container exits before its dependency is up. Add readiness gating / init-containers / retry, or fix the dependency ( if it's name resolution) · **OOMKilled** (exit 137) — raise t…
- **Источник:** `kb/troubleshooting/crashloopbackoff.md`

### KEDB-216 · Pod Pending / Unschedulable (scheduler can't place it)
- **Симптом:** `kubectl get pod` shows `Pending`; `kubectl describe pod` Events show `0/N nodes are available: …` with per-node reasons (e.g. `Insufficient cpu`, `node(s) had untolerated taint`, `node(s) didn't match Pod's node affinity/selector`)
- **Затронутые CIs:** scheduling, pods, resources  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` · The scheduler **filters** nodes by: resource **requests** (not limits) vs Allocatable, **taints** vs the Pod's tolerations , `nodeSelector` / node **affinity**, **topology spread**, and volume/zone constraints · The `describe` message aggregates why *each* node was rejected — read it literally
- **Workaround / fix:** **`Insufficient cpu` / `memory`** — the Pod's **requests** exceed free Allocatable on every node. Lower requests, add/enlarge nodes, or free capacity. Remember Allocatable is Capacity minus `kube_reserved`/`system_reserved` · **`untolerated taint`** — add the matching toleration to the Pod, or remove/adjust the taint . Control-plane nodes are tainted by default — apps need a toleration to land there · **`didn't match…
- **Источник:** `kb/troubleshooting/pod-pending-unschedulable.md`

### KEDB-217 · Pod stuck in Terminating
- **Симптом:** Usual causes: a **finalizer** that never completes, a **lost node** (kubelet gone, so it cannot confirm deletion), or a container that ignores SIGTERM until the grace period. On a lost node, the pod is not force-deleted automatically
- **Затронутые CIs:** operations, operations  ·  _>=v2.29.0 <=v2.31.0_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` clusters. This is a general Kubernetes/component operational issue (not tied to one Kubespray version); the relevant tunables are noted in Known Issues
- **Workaround / fix:** If a node is gone, cordon/remove it (PRACTICE-NODE_NOT_READY / PLAYBOOK-REMOVE_NODE) so pods reschedule. Remove a stuck finalizer only when you understand the controller. Force delete as a last resort: `kubectl delete pod <p> --grace-period=0 --force` (does NOT clean up on a dead node)
- **Источник:** `kb/troubleshooting/pod-stuck-terminating.md`

### KEDB-218 · Pyrra: SLO rules not generated / not evaluated — CRD errors, Prometheus not loading the rules
- **Симптом:** The Pyrra UI/SLO shows no data, or burn-rate alerts never fire
- **Затронутые CIs:** observability, slo, pyrra  ·  _>=1.29 <=1.35 / 0.9.4_
- **Root cause:** Pyrra `0.9.4` over Prometheus · **CRD → rules:** an invalid SLO (bad indicator query/objective) makes Pyrra emit nothing · **Prometheus pickup:** the generated PrometheusRule must be selected by Prometheus's `ruleSelector` (Prometheus Operator label match) — otherwise the rules exist but Prometheus ignores them
- **Workaround / fix:** **No rules — fix:** `describe` the SLO CR; correct the indicator query/objective so Pyrra generates rules · **Not loaded — fix:** ensure the generated PrometheusRule carries the labels Prometheus's `ruleSelector` expects (Prometheus Operator), so it's loaded and evaluated
- **Источник:** `kb/troubleshooting/pyrra-slo-rules.md`

### KEDB-219 · release-watcher: no notifications — source/API rate limits, credentials, notifier config
- **Симптом:** No new-release notifications arrive though releases clearly happened
- **Затронутые CIs:** tooling, notifications  ·  _>=1.29 <=1.35_
- **Root cause:** release-watcher ; niche/effectively-undocumented — verify the running image tag · **Source rate limit/auth:** unauthenticated GitHub API is throttled; without a token, polling silently fails/backs off · **Notifier:** a wrong/blocked webhook means it detects releases but can't tell you
- **Workaround / fix:** **Rate limit — fix:** give it an authenticated source token (GitHub PAT) so polling isn't throttled · **Notifier — fix:** correct the webhook/Slack endpoint and ensure egress to it; test with a known release
- **Источник:** `kb/troubleshooting/release-watcher.md`

### KEDB-220 · ServiceAccount has no Secret / token — auto-generated SA token Secrets removed (K8s 1.24+, cleanup GA 1.30)
- **Симптом:** A newly created ServiceAccount has **no** `*-token-*` Secret; `kubectl get secrets` shows nothing for it · Automation that read a token from `secret/<sa>-token-xxxx` gets `NotFound` · After a cluster upgrade, previously-present legacy SA token Secrets **disappear** (auto-cleaned if unused) · CI/external systems using a static SA token Secret suddenly fail auth
- **Затронутые CIs:** kubernetes, auth, serviceaccount  ·  _>=v2.27.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** The auto-generation of a Secret per ServiceAccount was turned off by default in **K8s 1.24** (`LegacyServiceAccountTokenNoAutoGeneration`); the **cleanup** of unused legacy token Secrets reached **GA in 1.30** (`LegacyServiceAccountTokenCleanUp`). Both are fully in effect across the Kubespray range (K8s 1.29–1.35). `keps/sig-auth/2799-...` · Pods don't need the Secret: kubelet mounts a **projected, short-lived** toke…
- **Workaround / fix:** **Fix (in-cluster consumers):** use the **projected token** — mount a `serviceAccountToken` projected volume, or call the **TokenRequest** API; don't rely on a Secret · **Fix (external/long-lived need — e.g. a CI system):** explicitly create a **manually-managed** token Secret with `type: kubernetes.io/service-account-token` and the `kubernetes.io/service-account.name` annotation — this is still supported but is opt-…
- **Источник:** `kb/troubleshooting/sa-secret-token-removed.md`

### KEDB-221 · Setting timezone fails under SELinux
- **Симптом:** The NTP/timezone task did not account for SELinux; the fix handles SELinux context so the timezone can be set. Affects RHEL-family nodes with SELinux enforcing
- **Затронутые CIs:** —  ·  _>=v2.29.0 <=v2.29.1_
- **Root cause:** Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0` · Confirmed via merged PR #12436 and the tag code
- **Workaround / fix:** Fixed by PR #12436 (in `roles/kubernetes/preinstall/tasks/0081-ntp-configurations.yml`). Workaround before upgrading: temporarily set SELinux permissive or set the timezone manually, or upgrade to v2.30.0. Durable fix: upgrade to `v2.30.0` or later
- **Источник:** `kb/troubleshooting/timezone-under-selinux.md`

### KEDB-222 · Talos: talosctl can't reach the node (apid / certs / endpoints)
- **Симптом:** `talosctl ...` → `connection refused` / `context deadline exceeded` / `certificate signed by unknown authority` / `x509` · Commands hang or hit the wrong node
- **Затронутые CIs:** talos, operations  ·  _>=1.29 <=1.35 / 1.13.6_
- **Root cause:** Applies to Talos **1.13.x** . apid listens on **TCP 50000**, mTLS
- **Workaround / fix:** Large client↔node **version skew** can make some commands/resources unavailable — match `talosctl` to the node's Talos minor
- **Источник:** `kb/os/talos/talos-apid-unreachable.md`

### KEDB-223 · vector-operator: logs not flowing — invalid pipeline CRD -> bad Vector config, image, sink auth
- **Симптом:** No logs reach the sink; the Vector pod is `CrashLoopBackOff` ("configuration error"), or a pipeline CR shows a not-valid status
- **Затронутые CIs:** —  ·  _>=1.28 <=1.31 / >=0.3.3_
- **Root cause:** vector-operator `0.3.3` ; K8s window **1.28–1.31** (older — check compatibility on newer clusters). The managed **Vector image is user-supplied via the CRD**, not pinned by the chart · **Bad pipeline → bad config:** the operator merges all pipelines; one invalid source/transform/sink makes the whole generated config fail validation, so Vector won't start (all pipelines down, not just the broken one) · **Sink auth:** …
- **Workaround / fix:** **Invalid pipeline — fix:** `describe` the pipeline CR for the validation error; fix the offending source/transform/sink — one bad CR blocks the merged config · **Image — fix:** set a valid Vector image/tag in the CRD (the operator doesn't pin one) · **Sink auth — fix:** correct the sink endpoint and credentials secret; watch the Vector pod logs for delivery errors
- **Источник:** `kb/troubleshooting/vector-operator-pipeline.md`

