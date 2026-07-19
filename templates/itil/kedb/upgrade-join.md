# KEDB · upgrade & join

_11 известных ошибок. Сгенерировано; не править руками._

### KEDB-165 · Capsule 0.10→0.13 upgrade: webhooks/CRDs break
- **Симптом:** Tenant operations fail: webhook `x509`/connection errors after the upgrade · New CRD fields/quota features missing; CRDs not updated · Everything tenant-related is blocked because the webhook is unreachable
- **Затронутые CIs:** capsule, multi-tenancy, upgrade  ·  _>=0.13.0 <=0.13.9_
- **Root cause:** Applies to Capsule **0.13.0–0.13.9** (owner spans 0.10.9→0.13.3 — ). The `Tenant` CRD stays `capsule.clastix.io/v1beta2` (no apiVersion bump in this range)
- **Workaround / fix:** **CVE-2026-55636** (`namespace/finalize` typo) affects **0.13.0–0.13.5** — fixed **0.13.6**; upgrade past it. Webhook-unreachable blast radius:
- **Источник:** `kb/troubleshooting/capsule-upgrade-013.md`

### KEDB-166 · Cloud LoadBalancers/node-init stop working — in-tree cloud providers removed, need external CCM
- **Симптом:** After upgrading across this range, `Service type=LoadBalancer` sits `<pending>`; nodes lack `topology.kubernetes.io/zone` / provider IDs; cloud disks fail to attach · kube-controller-manager / kubelet logs show the in-tree cloud provider is gone / `--cloud-provider` external expected
- **Затронутые CIs:** kubernetes, cloud-provider, upgrade  ·  _>=v2.27.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Milestone (`keps/sig-cloud-provider/2395-...` kep.yaml): in-tree provider code removal completes across **1.29–1.31** (`DisableCloudProviders`, `DisableKubeletCloudCredentialProviders`). The external CCM model has been the path for years; this range is when the in-tree fallback disappears · **Kubespray context:** Kubespray already deploys **external cloud providers** (external CCM + CSI) for the supported clouds via …
- **Workaround / fix:** **Fix:** switch to `cloud_provider: external`, deploy the **external CCM** and **CSI driver** for your cloud (Kubespray has roles/vars for the supported clouds), and remove the in-tree `--cloud-provider=<name>` · **Migration order:** install the external CCM/CSI **before or with** the upgrade that removes the in-tree code, or you get a window with no cloud integration · Verify per Kubernetes version which providers w…
- **Источник:** `kb/troubleshooting/in-tree-cloud-provider-removed.md`

### KEDB-167 · Consul-k8s 1.x → 2.x upgrade — lockstep versions, Gateway API bump, string-typed values
- **Симптом:** `helm upgrade` to 2.x fails to render: type errors on strictly-typed string fields that hold booleans (previously accepted) · After upgrade, **API Gateway** resources stop reconciling (Gateway API CRD version mismatch) · `kubectl`/Argo CD hit CRD short-name ambiguity between Consul and Gateway-API HTTPRoute CRDs
- **Затронутые CIs:** consul, upgrade, service-mesh  ·  _>=1.29 <=1.35 / >=1.22.7 <=2.0.2_
- **Root cause:** Applies to the consul-k8s **1.9.x → 2.0.x** transition · **Lockstep versioning:** chart 2.0.2 = Consul 2.0.2 + consul-dataplane 2.0.2 (CHANGELOG@v2.0.2, 2.0.0 NOTE). 1.9.10 = Consul 1.22.7. The chart↔Consul↔K8s compatibility matrix is HashiCorp-hosted docs (external, authoritative) · **2.0.0 BREAKING — API Gateway:** the stable controller moved to `gateway.networking.k8s.io` **v1.5.1** (CHANGELOG@v2.0.2, GH-5181) — t…
- **Workaround / fix:** **Fix (values):** audit your custom `values.yaml` for booleans in string-typed fields (quote them) before upgrading; validate with `helm template` · **Fix (Gateway API):** upgrade the Gateway API CRDs to **v1.5.1** in lockstep with the chart · **Fix (ordering):** treat 1.x → 2.x as a planned migration — read HashiCorp's version-specific upgrade guide, gate the server rollout with `updatePartition`, and re-verify ACLs…
- **Источник:** `kb/components/consul/consul-upgrade-1x-to-2x.md`

### KEDB-168 · Envoy Gateway 1.6 upgrade: upstream TLS breaks (SNI/SAN)
- **Симптом:** Backend TLS handshake failures to upstreams after the upgrade (cert/SNI errors) · Chart upgrade fails because Gateway API CRDs are the old version · OIDC sessions behave differently (unexpected token refresh)
- **Затронутые CIs:** envoy, gateway-api, tls, upgrade  ·  _>=1.6.0 <=1.8.2_
- **Root cause:** Applies to Envoy Gateway **1.6.0–1.8.2** (owner spans 1.4.1→1.6.0 — ). v1.6.0 implements **Gateway API v1.4.0**
- **Workaround / fix:** **v1.6.0 is affected by RCE CVE-2026-22771** (EnvoyExtensionPolicy Lua) — fixed **1.6.2**. Bundled Envoy 1.36.4 also has fixes in 1.36.5/1.36.9. Upgrade to EG ≥1.6.2
- **Источник:** `kb/troubleshooting/envoy-gateway-backend-tls-sni.md`

### KEDB-169 · Helm 3→4 upgrade: CLI/SDK/plugin breaks
- **Симптом:** Scripts/CI that parse `helm` CLI output or rely on specific flags fail · Custom plugins or **post-renderers** stop working · Go programs embedding the Helm SDK don't compile / behave differently · Install/upgrade behaviour shifts because **server-side apply** is now used
- **Затронутые CIs:** helm, upgrade  ·  _>=4.0.0 <=4.2.3_
- **Root cause:** Applies to Helm **4.0.0–4.2.3** (base: Helm 3.18.4 — ) · Scope is smaller than the v2→v3 jump — "the majority of workflows remain compatible."
- **Workaround / fix:** Because SSA changes field ownership, resources co-managed by operators may see field-manager conflicts on first 4.x upgrade — plan a test upgrade in staging
- **Источник:** `kb/troubleshooting/helm-3-to-4-upgrade.md`

### KEDB-170 · kubeadm init retry always fails on leftovers from the first try
- **Симптом:** The retry did not tolerate remnants (already-created files/ports) from the first `kubeadm init`; the fix ignores the related preflight/leftover errors on retry so it can proceed
- **Затронутые CIs:** —  ·  _>=v2.29.0 <=v2.29.1_
- **Root cause:** Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0` · Confirmed via the merged PR #12785 and the tag code
- **Workaround / fix:** Root cause fixed by PR #12785 (in `roles/kubernetes/control-plane/tasks/kubeadm-setup.yml`). Workaround before upgrading: clean up the failed init (`kubeadm reset` on that node) before re-running, or upgrade for the automatic retry handling. The durable fix is to upgrade to `v2.30.0` or later
- **Источник:** `kb/troubleshooting/kubeadm-init-retry-fails.md`

### KEDB-171 · kubeadm preflight errors (upgrade / init / join)
- **Симптом:** `[preflight] Some fatal errors occurred:` — e.g. `Port 6443 is in use`, `/etc/kubernetes/… already exists`, `unsupported ... version`, CRI-socket ambiguity, cgroup/swap, kernel module, or a failed connectivity check
- **Затронутые CIs:** kubeadm, preflight, upgrade  ·  _>=v2.29.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies to Kubespray **v2.29.0–v2.31.0** / Kubernetes **1.29–1.35**. Kubespray calls `kubeadm init/join --ignore-preflight-errors={{ ... }}` (setup/kubeadm role) — so anything still fatal is not on the ignore list
- **Workaround / fix:** Preflight failures on a **re-run** are usually leftovers from a **first failed try**, not a new problem
- **Источник:** `kb/troubleshooting/kubeadm-preflight.md`

### KEDB-172 · kubeadm version skew: can't skip a minor / kubelet too old
- **Симптом:** `kubeadm upgrade`: `specified version to upgrade to "v1.3X.0" is too high; ... can only upgrade to the next minor` (or similar version-skew preflight error) · After a big `kube_version` bump, `kubeadm upgrade apply` refuses
- **Затронутые CIs:** kubeadm, upgrade, version  ·  _>=v2.29.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies to Kubespray **v2.29.0–v2.31.0** / Kubernetes **1.29–1.35**. Each Kubespray tag also supports only a **3-minor window** , reinforcing this
- **Workaround / fix:** The `kube_version` you set must be one Kubespray's tag actually supports — an out-of-window version fails download **and** the kubeadm version check
- **Источник:** `kb/troubleshooting/kubeadm-version-skew.md`

### KEDB-173 · Myth: 'copy CA into /etc/kubernetes/pki' — Kubespray uses /etc/kubernetes/ssl
- **Симптом:** You hit a stuck deploy (e.g. "kubeadm | Initialize first control plane") or a certificate error and find advice online to `mkdir /etc/kubernetes/pki` and copy the CA there. You're unsure whether Kubespray is misconfigured
- **Затронутые CIs:** certificates, kubeadm, myth  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` · Kubespray's `kube_cert_dir` default is **`{{ kube_config_dir }}/ssl`** = `/etc/kubernetes/ssl`, and the generated **kubeadm config** sets `certificatesDir: {{ kube_cert_dir }}` — i.e. kubeadm is explicitly pointed at `/etc/kubernetes/ssl`. There is no mismatch; kubeadm and Kubespray agree on `ssl`
- **Workaround / fix:** **Do not** create `/etc/kubernetes/pki` and copy the CA there to "fix" a stuck init — it addresses a non-problem and can leave stale/duplicate certs. Kubespray manages certs in `ssl/` · If the first-control-plane init is genuinely stuck, the cause is elsewhere — the kubelet not coming up, a failed preflight, a runtime issue, etc. . Diagnose that, not the cert directory · Vanilla kubeadm (outside Kubespray) does defau…
- **Источник:** `kb/troubleshooting/cert-dir-ssl-not-pki.md`

### KEDB-174 · Registry (distribution) 2→3: config/driver breaks
- **Симптом:** Registry pod crashloops after the v3 image bump: config file not found · Startup fails because the storage backend uses the removed **oss** (Alibaba) or **swift** (OpenStack) driver · Tooling importing `manifest.Versioned` breaks (deprecated)
- **Затронутые CIs:** registry, distribution, upgrade  ·  _>=3.0.0 <=3.1.1_
- **Root cause:** Applies to distribution **3.0.0–3.1.1** (base: registry 2.8.1 — )
- **Workaround / fix:** If upgrading from a v2.x that used release candidates, review the v2.x deprecations first — some were finalized in v3
- **Источник:** `kb/troubleshooting/registry-2-to-3-migration.md`

### KEDB-175 · Velero 1.17 upgrade: CRD / sequential-version errors
- **Симптом:** Backups/restores fail or the controller crashloops after the chart bump to 1.17 · New CRD fields missing / schema validation errors · Restores report fake "completed" notifications, or backups queue up
- **Затронутые CIs:** velero, backup, upgrade  ·  _>=1.17.0 <=1.18.2_
- **Root cause:** Applies to Velero **1.17.0–1.18.2** (owner runs chart 11.4.0 / app 1.17.1 — ; operational hub )
- **Workaround / fix:** 1.17.1 fixes the prior failure modes: fake completion notifications from repeated PodVolumeRestore updates (#9365); schedule-controller queue build-up; VolumeSnapshot-field races in multi-threaded backups; backupPVC attaching to the source node (#9229)
- **Источник:** `kb/troubleshooting/velero-upgrade-117.md`

