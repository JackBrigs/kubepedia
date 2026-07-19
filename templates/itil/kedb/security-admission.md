# KEDB · security & admission

_30 известных ошибок. Сгенерировано; не править руками._

### KEDB-108 · Admission webhook blocks all creates/updates (failed calling webhook)
- **Симптом:** `kubectl apply`/`create`/`scale` (or the controllers doing it) fail with `Internal error occurred: failed calling webhook "<name>": … context deadline exceeded` / `connection refused` / `x509`, sometimes for unrelated resources
- **Затронутые CIs:** admission, webhook, api  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0`. Webhooks come from add-ons you install (cert-manager, ingress admission, Kyverno/OPA, service meshes) — not from Kubespray core · Each `ValidatingWebhookConfiguration`/`MutatingWebhookConfiguration` has `rules` (which resources/verbs it intercepts), a `clientConfig` (the backend Service + `caBundle`), a `failurePolicy` (`Fail`/`Ignore`), a `timeoutSeconds`, and a `namespaceSe…
- **Workaround / fix:** **Webhook backend down** — restart/repair its Deployment; the webhook recovers once the Service answers. This is the usual case after a bad rollout or node drain that took the webhook's only replica · **Bad `caBundle` / `x509`** — refresh the CA bundle (cert-manager `ca-injector` normally does this; if it's stalled, reconcile it) · **Blocking during outage — emergency unblock:** temporarily set `failurePolicy: Ignore…
- **Источник:** `kb/troubleshooting/admission-webhook-blocking.md`

### KEDB-109 · Admission webhooks fail when cert-manager isn't ready first (ordering)
- **Симптом:** Right after a bulk install/bootstrap, tenant/CR operations fail with webhook `x509` or "connection refused" errors · An operator's own CRs can't be created because its webhook has no serving cert · Removing cert-manager (or a cert-manager outage) breaks multiple unrelated operators at once
- **Затронутые CIs:** cross-component, webhooks, cert-manager  ·  _>=1.29 <=1.35_
- **Root cause:** Affects any component whose webhook certs come from cert-manager: (0.13 defaults to cert-manager), the OpenTelemetry Operator which **requires** cert-manager, vault-secrets-webhook , and cert-manager's own webhook
- **Workaround / fix:** A cert-manager **upgrade** that briefly restarts the webhook can flap dependent operators — upgrade cert-manager in a low-traffic window · Capsule 0.13 moved webhook certs to cert-manager by default; without it, re-enable Capsule's own TLS controller
- **Источник:** `kb/troubleshooting/webhook-cert-manager-ordering.md`

### KEDB-110 · AppArmor annotations deprecated — move to securityContext.appArmorProfile (API GA 1.31)
- **Симптом:** Deprecation warnings on pods carrying `container.apparmor.security.beta.kubernetes.io/*` annotations · Planning forward: unsure how to declare an AppArmor profile without the annotation · A Pod Security / policy tool flags the annotation as outdated
- **Затронутые CIs:** kubernetes, security, node  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Milestone (`keps/sig-node/24-apparmor` kep.yaml): AppArmor API **GA 1.31** (Kubespray v2.29.0+); the annotation is the pre-GA form and is deprecated · **New form:** `securityContext.appArmorProfile: { type: RuntimeDefault | Localhost | Unconfined, localhostProfile: <name> }` at pod or container level. Requires AppArmor-enabled nodes (kernel LSM)
- **Workaround / fix:** **Fix:** replace the annotation with `securityContext.appArmorProfile` in pod specs / templates (Deployments, StatefulSets, Helm charts). A pod using `RuntimeDefault` is the common baseline · **PSA/hardening:** AppArmor is part of a hardened node posture (, ); the GA field is the supported way to require it going forward · **Timeline:** the annotation still works across the current range but treat it as tech debt to …
- **Источник:** `kb/troubleshooting/apparmor-annotations-deprecated.md`

### KEDB-111 · Argo CD 2→3 upgrade: users lose access / permission denied
- **Симптом:** Users who could act before now get `permission denied` on sync/delete · Application resource trees show fewer resources, or "logs" tab is empty/denied · Apps show as OutOfSync/unknown because tracking labels changed to annotations
- **Затронутые CIs:** argocd, gitops, upgrade, rbac  ·  _>=3.0.0 <=3.4.5_
- **Root cause:** Applies to Argo CD **3.0.0–3.4.5** (owner runs 3.1.7 — ) · The 3.0 major deliberately changed RBAC and tracking; the chart upgrade alone does not warn you interactively
- **Workaround / fix:** Also on 3.1.x: **CVE-2025-55191** (DoS via repo-credentials race) affects ≤3.1.7 — fixed 3.1.8. Bundle the security bump with the RBAC fix. General RBAC-denial triage:
- **Источник:** `kb/troubleshooting/argocd-upgrade-3-rbac.md`

### KEDB-112 · cert-manager: Certificate stuck not-ready (ACME challenge)
- **Симптом:** `kubectl get certificate` shows `READY: False` for a long time · The referenced TLS secret is missing or empty; Ingress serves the default cert
- **Затронутые CIs:** cert-manager, certificates, acme  ·  _>=1.15.0 <=1.21.0_
- **Root cause:** Applies to cert-manager **1.15–1.21** (Kubespray 1.15.3 / addon 1.18.2 — , )
- **Workaround / fix:** The **webhook** must be reachable or Certificate/Issuer admission fails · Addon cert-manager **1.18.0–1.18.4** has a controller DoS CVE (fixed 1.18.5)
- **Источник:** `kb/troubleshooting/cert-manager-certificate-not-ready.md`

### KEDB-113 · cert-manager: known CVEs by shipped version (osv.dev)
- **Симптом:** Each shipped cert-manager version carries the CVEs below (osv.dev returns only vulns affecting the queried version — authoritative affectedness)
- **Затронутые CIs:** security, cve, cert-manager  ·  _>=v2.29.0 <=v2.31.0 / >=1.15.3 <=1.15.3_
- **Root cause:** | Version | Kubespray | # | CVEs | |---|---|---|---| | 1.15.3 | v2.29.0-v2.31.0 | 1 | CVE-2024-12401 |
- **Workaround / fix:** **CVE-2024-12401** [CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:L/SC:N/SI:N/SA:N] — cert-manager ha a potential slowdown / DoS when parsing specially crafted PEM inputs — fixed in: `1.12.14, 1.15.4, 1.16.2`
- **Источник:** `kb/troubleshooting/cert-manager-known-cves.md`

### KEDB-114 · Consul ACL bootstrap brittleness (server-acl-init) — can't re-bootstrap, policies overwritten
- **Симптом:** `server-acl-init` Job fails; component pods (connect-injector, sync-catalog, etc.) loop on `Permission denied` / ACL errors · After restoring servers from a snapshot or losing the bootstrap Secret: `ACL bootstrap no longer allowed` · After a `helm upgrade`: manual edits to Consul ACL policies silently reverted
- **Затронутые CIs:** consul, acl, security  ·  _>=1.29 <=1.35 / >=1.22.7 <=2.0.2_
- **Root cause:** Applies to consul-k8s **1.9.x–2.0.x** . The bootstrap token Secret default is `<global.name>-bootstrap-acl-token` (key `token`); its empty-vs-populated state decides whether the Job bootstraps (`values.yaml`@v2.0.2 L424/L438-464) · **Template `fail` traps:** supplying only one of `bootstrapToken.secretName`/`secretKey` (or the `replicationToken` pair) **hard-fails** the render; the removed `global.bootstrapACLs` hard…
- **Workaround / fix:** **Fix (re-bootstrap after data loss):** because a restored leader has no ACL state, you must reset the ACL bootstrap on the servers (write the reset index Consul reports into `acl-bootstrap-reset` on each server), then let the Job repopulate the Secret. The chart only supports the "empty Secret → bootstrap" path; the reset procedure is a Consul-server operation, not a chart value. *(Exact reset steps are a Consul ser…
- **Источник:** `kb/components/consul/consul-acl-bootstrap.md`

### KEDB-115 · Consul connect-inject webhook blocks all pod scheduling (failurePolicy: Fail)
- **Симптом:** New pods stuck failing admission: `failed calling webhook ...-connect-injector...` / `context deadline exceeded` — cluster-wide, not just mesh namespaces · Even system/infra workloads can't be created if their namespace isn't excluded · In Kind, `Fail` "may prevent volume provisioner pods from running which can lead to hangs" (`values.yaml`@v2.0.2 L2830-2835)
- **Затронутые CIs:** consul, admission, service-mesh  ·  _>=1.29 <=1.35 / >=1.22.7 <=2.0.2_
- **Root cause:** Applies to consul-k8s **1.9.x–2.0.x** . The `pods` webhook is the last core webhook in `connect-inject-mutatingwebhookconfiguration.yaml`@v2.0.2 with `failurePolicy` templated from `connectInject.failurePolicy` — default **`"Fail"`** (`values.yaml`@v2.0.2 L2836) · **Built-in blast-radius limiters (know these):** · `objectSelector` excludes Consul's own pods (`app NotIn consul`) so Consul can still self-heal · `namesp…
- **Workaround / fix:** **Fix (availability):** raise `connectInject.replicas` (>1) and keep `connectInject.disruptionBudget.enabled: true` (auto `maxUnavailable = (n/2)-1`) so the injector survives node loss (`values.yaml`@v2.0.2 L2419/L2450-2461) · **Fix (scope):** exclude infra namespaces via `namespaceSelector` / `k8sDenyNamespaces` so a webhook outage can't block system workloads · **Fix (trade-off):** set `connectInject.failurePolicy:…
- **Источник:** `kb/components/consul/consul-connect-inject-webhook.md`

### KEDB-116 · containerd: known CVEs by shipped version (osv.dev)
- **Симптом:** Each shipped containerd version carries the CVEs listed below (osv.dev returns only vulnerabilities that affect the queried version, so this is authoritative affectedness)
- **Затронутые CIs:** security, cve, containerd  ·  _>=v2.27.0 <=v2.31.0 / >=1.7.24 <=2.2.3_
- **Root cause:** | Component version | Kubespray | # CVEs | CVEs | |---|---|---|---| | 1.7.24 | v2.27.0 | 13 | 1.7.x line — larger set (query osv.dev for the full list) | | 1.7.27 | v2.27.1 | 13 | 1.7.x line — larger set (query osv.dev for the full list) | | 2.0.5 | v2.28.0 | 3 | GO-2026-5064, GO-2026-5338, GO-2026-5622 | | 2.0.6 | v2.28.1 | 3 | GO-2026-5064, GO-2026-5338, GO-2026-5622 | | 2.1.4 | v2.29.0 | 3 | CVE-2026-50195, CVE-20…
- **Workaround / fix:** **CVE-2026-50195** — containerd: CRI checkpoint import allows local image tag poisoning in github.com/containerd/containerd — fixed in: `—` · **CVE-2026-53489** — Arbitrary host CRI log file read via symlink following in CRI checkpoint restore in github.com/containerd/containerd — fixed in: `—` · **CVE-2026-53492** — containerd CRI checkpoint restore CDI annotation smuggling in github.com/containerd/containerd — fixe…
- **Источник:** `kb/troubleshooting/containerd-known-cves.md`

### KEDB-117 · Error from server (Forbidden) — RBAC denies the request
- **Симптом:** `kubectl` (or an app using a ServiceAccount) returns `… is forbidden: User "…" cannot list resource "pods" in API group "" in the namespace "x"` — authentication worked (you're identified) but the action is denied
- **Затронутые CIs:** rbac, authorization, security  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0`; `authorization_modes` is `['Node','RBAC']` (hardened) — RBAC is the effective authorizer · Authorization is **additive-deny-by-default**: nothing is allowed unless a Role/ ClusterRole grants it and a binding attaches it to the subject
- **Workaround / fix:** **A user/group needs access** — bind an appropriate (Cluster)Role: `kubectl create rolebinding dev-view --clusterrole=view --user=<u> -n <ns>` (namespaced), or a ClusterRoleBinding for cluster-wide. Prefer the built-in `view`/`edit`/`admin` ClusterRoles over `cluster-admin` · **A ServiceAccount (app) needs access** — create a Role/ClusterRole with the exact verbs+resources and bind it to `system:serviceaccount:<ns>:<…
- **Источник:** `kb/troubleshooting/rbac-forbidden.md`

### KEDB-118 · helm: known CVEs by shipped version (osv.dev)
- **Симптом:** Each shipped helm version carries the CVEs below (osv.dev returns only vulns affecting the queried version — authoritative affectedness)
- **Затронутые CIs:** security, cve, helm  ·  _>=v2.29.0 <=v2.31.0 / >=3.18.4 <=3.18.4_
- **Root cause:** | Version | Kubespray | # | CVEs | |---|---|---|---| | 3.18.4 | v2.29.0-v2.31.0 | 3 | CVE-2025-55198, CVE-2025-55199, CVE-2026-35206 |
- **Workaround / fix:** **CVE-2025-55198** [CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H] — Helm May Panic Due To Incorrect YAML Content — fixed in: `3.18.5` · **CVE-2025-55199** [CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H] — Helm Charts with Specific JSON Schema Values Can Cause Memory Exhaustion — fixed in: `3.18.5` · **CVE-2026-35206** [CVSS:4.0/AV:L/AC:L/AT:N/PR:N/UI:P/VC:N/VI:L/VA:L/SC:N/SI:N/SA:N] — Helm Chart extraction output dire…
- **Источник:** `kb/troubleshooting/helm-known-cves.md`

### KEDB-119 · KMS v1 encryption provider deprecated — migrate to KMS v2 (GA 1.29)
- **Симптом:** apiserver logs a **deprecation warning** for KMS provider `apiVersion: v1` · Planning to keep encryption working long-term but the config still references the v1 KMS plugin · High KMS call volume / latency on Secret reads (v1 calls KMS per object; v2 caches a local KEK)
- **Затронутые CIs:** kubernetes, security, encryption  ·  _>=v2.27.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Milestone (`keps/sig-auth/3299-...` kep.yaml): `KMSv2` **stable 1.29** (with `KMSv2KDF`). v1 remains functional but deprecated across the Kubespray range (K8s 1.29–1.35) · v2 changes the on-disk envelope (DEK-per-write encrypted by a cached KEK) — **migration re-encrypts data**, so it follows the same rewrite discipline as enabling encryption
- **Workaround / fix:** **Fix (migration):** deploy a **v2-capable** KMS plugin, add the **v2** provider **first** in the providers list (writes use the first provider) while keeping the v1 provider in the list for **reads**, then **re-encrypt all Secrets** (`kubectl get secrets -A -o json | kubectl replace -f -`), and only then remove the v1 provider — the same order-sensitive procedure as · **Snapshot etcd first** — you are changing how c…
- **Источник:** `kb/troubleshooting/kms-v1-deprecated.md`

### KEDB-120 · Kubernetes Dashboard: login/access issues and the retired-upstream caveat (oauth2-proxy, RBAC)
- **Симптом:** Can't log in, or the UI loads but shows **forbidden**/empty for namespaces
- **Затронутые CIs:** ui, dashboard, security  ·  _>=1.29 <=1.35 / 7.6.1_
- **Root cause:** Dashboard `7.6.1` ; 7.x requires the Kong/oauth2-proxy front, not the old bearer-token-only flow · **RBAC:** the viewer identity must have read RBAC; the UI mirrors it exactly · **Security:** the archived upstream means no new fixes — treat exposure conservatively
- **Workaround / fix:** **Access — fix:** grant the identity the needed RBAC; confirm oauth2-proxy is configured (issuer/client) and healthy · **Retirement — plan:** migrate to a maintained UI (Headlamp) since the dashboard repo is archived
- **Источник:** `kb/troubleshooting/kubernetes-dashboard-access.md`

### KEDB-121 · kubernetes-mcp-server: LLM can't act / over-broad access — MCP auth, RBAC scope, open-webui link
- **Симптом:** open-webui/LLM can't run cluster actions (tools error), or conversely the MCP SA is far more privileged than intended
- **Затронутые CIs:** ai, mcp, security  ·  _>=1.29 <=1.35 / 0.0.56_
- **Root cause:** kubernetes-mcp-server `0.0.56` ; **pre-1.0**, expect churn · **RBAC = capability:** the server acts as its **ServiceAccount**; whatever RBAC that SA has is what the LLM can do. Cluster-admin here means the LLM is cluster-admin · **MCP link:** open-webui must be pointed at the mcp-server endpoint with valid auth or tools won't register
- **Workaround / fix:** **Can't act — fix:** connect open-webui to the MCP endpoint; grant the SA the **minimum** RBAC for the intended actions · **Over-broad — fix:** scope the SA down from cluster-admin to only what's needed; this is a real security exposure
- **Источник:** `kb/troubleshooting/kubernetes-mcp-server.md`

### KEDB-122 · kubernetes: known CVEs by shipped version (osv.dev)
- **Симптом:** Each shipped kubernetes version carries the CVEs below (osv.dev returns only vulns affecting the queried version — authoritative affectedness)
- **Затронутые CIs:** security, cve, k8s  ·  _>=v2.29.0 <=v2.31.0 / >=1.33 <=1.35_
- **Root cause:** | Version | Kubespray | # | CVEs | |---|---|---|---| | 1.33.5 | v2.29.0 | 3 | CVE-2024-7598, CVE-2025-13281, CVE-2025-1767 | | 1.33.7 | v2.29.1 | 2 | CVE-2024-7598, CVE-2025-1767 | | 1.34.3 | v2.30.0 | 2 | CVE-2024-7598, CVE-2025-1767 | | 1.35.4 | v2.31.0 | 2 | CVE-2024-7598, CVE-2025-1767 |
- **Workaround / fix:** **CVE-2024-7598** — Kubernetes kube-apiserver Vulnerable to Race Condition in k8s.io/kubernetes — fixed in: `—` · **CVE-2025-13281** [CVSS:3.1/AV:N/AC:H/PR:H/UI:N/S:C/C:H/I:N/A:N] — kube-controller-manager is vulnerable to half-blind Server Side Request Forgery through in-tree Portworx StorageClass — fixed in: `1.32.10, 1.33.6, 1.34.2` · **CVE-2025-1767** — Kubernetes GitRepo Volume Inadvertent Local Repository Acces…
- **Источник:** `kb/troubleshooting/kubernetes-known-cves.md`

### KEDB-123 · Kyverno down → whole cluster (incl. kube-system) can't create/update; only Kyverno's ns spared
- **Симптом:** Kyverno pods unhealthy → **everything** fails admission (`failed calling webhook ...kyverno...`), including control-plane/system workloads in `kube-system` · You had `kube-system` in `resourceFilters` and expected it to be safe — it isn't · The cluster can't self-heal because even system pods can't be (re)created
- **Затронутые CIs:** kyverno, admission, policy  ·  _>=1.29 <=1.35 / 1.18.2_
- **Root cause:** Applies to Kyverno **1.18.x** (chart 3.0.0) · The chart injects a **single** `namespaceSelector` `matchExpressions` entry: `kubernetes.io/metadata.name NotIn <kyverno-ns>` (`_helpers.tpl`@v1.18.2, `kyverno.config.webhooks`). That's the *only* namespace the API server won't route to the webhook · `config.resourceFilters` (which does list `kube-system`, `kube-public`, etc. — `values.yaml`@v1.18.2 L331-348) is a **polic…
- **Workaround / fix:** **Recover now (outage):** flip all Kyverno webhooks to Ignore — set `features.forceFailurePolicyIgnore.enabled: true` / start with `--forceFailurePolicyIgnore` (`values.yaml`@v1.18.2 L794-796) — or delete the ValidatingWebhookConfiguration to unblock, then fix Kyverno · **Prevent:** run Kyverno **HA** (multiple admission replicas + PDB — ); for critical webhooks weigh `failurePolicy: Ignore` (availability > guarantee…
- **Источник:** `kb/troubleshooting/kyverno-failurepolicy-system-ns.md`

### KEDB-124 · Kyverno image verification blocks pods — Sigstore/TUF unreachable or keyless misconfig
- **Симптом:** Pods rejected with image-verification errors (signature/attestation could not be verified) even though the image is legitimately signed · Intermittent failures correlated with Rekor/Fulcio/TUF availability (public Sigstore outages, egress blocked, air-gapped clusters) · Keyless verification fails on identity/issuer or certificate-chain mismatch
- **Затронутые CIs:** kyverno, image-verification, supply-chain  ·  _>=1.29 <=1.35 / 1.18.2_
- **Root cause:** Applies to Kyverno **1.18.x** (, ) · `attestors` demand **`cosign`** or **`notary`**, with `ctlog`/`rekor` public-key settings, TUF/Rekor URLs, and `insecureIgnoreTlog`/`insecureIgnoreSCT` toggles (`imagevalidatingpolicies.yaml`@v1.18.2 L89-183). Verification reaches out to Rekor (transparency log), Fulcio (keyless CA), and a TUF mirror · **Air-gapped / restricted egress** is the classic failure: the public Sigstore …
- **Workaround / fix:** **Fix (air-gapped / restricted):** stand up a **private Sigstore** (self-hosted Rekor/Fulcio + TUF mirror) and point Kyverno at it via `--tufRoot`/`--tufMirror`; or use **key-based** cosign attestors instead of keyless (no Fulcio/TUF dependency) · **Fix (availability trade-off):** for non-critical enforcement, use `Audit`/`Warn` instead of a hard `Deny`/`Fail` so a Sigstore outage doesn't block scheduling; or `insecu…
- **Источник:** `kb/troubleshooting/kyverno-image-verification-blocks.md`

### KEDB-125 · Kyverno PolicyException ignored — feature off by default and namespace-restricted
- **Симптом:** A `PolicyException` is created, no errors, but the target policy still blocks/flags the resource · Exceptions work in one namespace but not another
- **Затронутые CIs:** kyverno, policy, exceptions  ·  _>=1.29 <=1.35 / 1.18.2_
- **Root cause:** Applies to Kyverno **1.18.x** · **Off by default:** `--enablePolicyException` defaults to **false**; `--exceptionNamespace` defaults to **empty** (`cmd/internal/flag.go`@v1.18.2 L138-139). The chart mirrors this: `policyExceptions.enabled: false` with a single-namespace restriction (`values.yaml`@v1.18.2 L823-826) · **Namespace gating:** with a namespace set, exceptions are honored **only** in that namespace; set to …
- **Workaround / fix:** **Fix:** enable the feature (`policyExceptions.enabled: true` / `--enablePolicyException`) **and** set the exception namespace appropriately (`policyExceptions.namespace` or `--exceptionNamespace`, `*` for cluster-wide), then place your `PolicyException` objects there · **Security note:** enabling exceptions cluster-wide (`*`) lets anyone who can create a `PolicyException` in any namespace bypass policy — scope the n…
- **Источник:** `kb/troubleshooting/kyverno-policy-exception-not-applying.md`

### KEDB-126 · Kyverno silently deletes any resource labeled cleanup.kyverno.io/ttl
- **Симптом:** Resources disappear on a schedule with no CleanupPolicy pointing at them · A label accidentally carried by a manifest template / Helm chart / a Kyverno `generate` rule causes unexpected deletions · Deletion cascades (or doesn't) unexpectedly depending on the propagation label
- **Затронутые CIs:** kyverno, cleanup, data-loss  ·  _>=1.29 <=1.35 / 1.18.2_
- **Root cause:** Applies to Kyverno **1.18.x** ; the TTL controller is a distinct component · The trigger is purely the label **`cleanup.kyverno.io/ttl`** (`LabelCleanupTtl`, `api/kyverno/constants.go`@v1.18.2 L9) — **no CleanupPolicy needed** · The value parses as a **Go duration** (`24h`), an **ISO-8601 datetime**, or a **date** (`pkg/controllers/ttl/controller.go`@v1.18.2 L140-149; utils L54-63). Reconcile interval `ttlController.…
- **Workaround / fix:** **Fix:** remove the `cleanup.kyverno.io/ttl` label from anything that shouldn't auto-delete; audit templates and generate rules that might propagate it · **Intended use:** set it deliberately (e.g. on ephemeral test resources) with a clear duration and a `propagation-policy` label if children should go too · **Distinct from CleanupPolicy:** scheduled deletion via `CleanupPolicy`/`DeletingPolicy` objects is a separate…
- **Источник:** `kb/troubleshooting/kyverno-ttl-label-cleanup.md`

### KEDB-127 · Kyverno upgrade: no raw-YAML path, CRD limits, breaking field moves
- **Симптом:** Helm fails: `clusterpolicies.kyverno.io is invalid: metadata.annotations: Too long: must have at most 262144 bytes` · Controllers silently hit stale/renamed CRD fields after an upgrade · After bumping, policies stop enforcing or reports vanish · etcd grows uncontrollably right after upgrading to 1.12.0
- **Затронутые CIs:** kyverno, upgrade, policy  ·  _>=1.29 <=1.35 / >=1.10.0 <=1.18.2_
- **Root cause:** Applies to Kyverno **1.10–1.18** ; the upgrade-horizon layer is
- **Workaround / fix:** Leftover webhook configs after a failed/ArgoCD uninstall deadlock the cluster · Upgrading also closes the large 1.15–1.18 CVE wave — run the newest patch ( / )
- **Источник:** `kb/troubleshooting/kyverno-upgrade.md`

### KEDB-128 · Kyverno: mutate/generate/verifyImages policy not applying
- **Симптом:** A mutate policy doesn't modify pre-existing objects until each is manually edited · `generate` + `synchronize: true` downstream isn't updated on policy change, or is updated in an infinite loop; cloned downstream is orphaned after the source is deleted · `verifyImages` fails (`UNAUTHORIZED`, Sigstore TUF timeout) or the admission-controller **panics/crashes** and denies all admission · With `kind: "*"`, a new CR of a…
- **Затронутые CIs:** kyverno, policy  ·  _>=1.29 <=1.35 / >=1.10.0 <=1.18.2_
- **Root cause:** Applies to Kyverno **1.10–1.18**
- **Workaround / fix:** **1.15** renamed the CEL `image()` function to **`parseImageReference`** — policies using the old name break. **1.13** moved `validationFailureAction` to the **rule level** (`spec.rules.validate.failureAction`)
- **Источник:** `kb/troubleshooting/kyverno-policy-not-applying.md`

### KEDB-129 · Kyverno: webhook blocks cluster / latency / HA leader flapping
- **Симптом:** All API operations rejected when Kyverno pods are unavailable (`failurePolicy: Fail`) · Admission latency jumps (>3s), webhook timeouts, apiserver `context deadline exceeded` under load spikes · After a node/network outage, `node.kubernetes.io/unreachable` taints never clear (bootstrap deadlock) · Controllers CrashLoopBackOff with `leadership lost, stopped leading`
- **Затронутые CIs:** kyverno, webhooks, policy  ·  _>=1.29 <=1.35 / >=1.10.0 <=1.18.2_
- **Root cause:** Applies to Kyverno **1.10–1.18** ; a specialization of the webhook blast radius
- **Workaround / fix:** **Uninstall/upgrade leftovers:** webhook configs can remain after uninstall (esp. ArgoCD, which ignores Helm `pre-delete` hooks) → fail-closed deadlock. Modern charts ship empty (`webhooks: []`) configs so they're GC'd; emergency `--forceFailurePolicyIgnore` or manual delete (issues #9551/#8390)
- **Источник:** `kb/troubleshooting/kyverno-webhook-ha.md`

### KEDB-130 · OpenTelemetry Operator: Collector not reconciled / auto-instrumentation not injecting (cert-manager, webhook)
- **Симптом:** An `OpenTelemetryCollector` CR is created but **no Collector pod appears**, or the operator logs webhook/TLS errors · **Auto-instrumentation** doesn't happen — pods start without the injected init container / SDK env
- **Затронутые CIs:** observability, opentelemetry, admission  ·  _>=1.25 <=1.35 / >=0.156.0_
- **Root cause:** OTel Operator `v0.156.0` ; supports K8s 1.25–1.35 · **cert-manager dependency:** by default the operator's admission/conversion webhooks get TLS from **cert-manager** . If cert-manager isn't installed/ready, the webhook has no serving cert → the operator can't validate/convert CRs → Collectors aren't reconciled. This is the classic cert-manager↔webhook ordering seam (, ) · **Auto-instrumentation** is opt-in per pod v…
- **Workaround / fix:** **Webhook/TLS — fix:** install and make cert-manager healthy **before** the operator (or configure a non-cert-manager cert source); confirm the webhook `Certificate` is `Ready` and the webhookconfiguration `caBundle` is populated · **Collector not created — fix:** with the webhook healthy, `kubectl describe` the CR for admission errors (invalid config/mode); the operator only builds the Collector once the CR validate…
- **Источник:** `kb/troubleshooting/otel-operator-issues.md`

### KEDB-131 · PodSecurity 'restricted' rejects a privileged CNI/CSI/agent DaemonSet — needs namespace label / exemption
- **Симптом:** A DaemonSet/Deployment shows **0 pods**; its controller events read `forbidden: violates PodSecurity "restricted:latest": host namespaces / privileged / hostPath ...` · Happens right after enabling `restricted` enforcement, or when deploying a privileged addon into a namespace that inherits the restricted default
- **Затронутые CIs:** security, pod-security, admission, interaction  ·  _>=v2.27.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies across **v2.27.0–v2.31.0**; PSA is built in (PodSecurityPolicy is long gone). Kubespray sets a cluster-wide default via `kube_pod_security_default_enforce` and exemptions via `kube_pod_security_exemptions_namespaces` · **Why:** PSA enforces the level configured for the pod's **namespace** (label `pod-security.kubernetes.io/enforce`), falling back to the cluster default. `restricted` forbids privileged, host n…
- **Workaround / fix:** **Fix (label the infra namespace):** for a namespace that legitimately runs privileged agents, set `kubectl label ns <ns> pod-security.kubernetes.io/enforce=privileged --overwrite` (and `warn`/`audit` to match). Keep application namespaces at `restricted` · **Fix (Kubespray, persistent):** add the namespace to `kube_pod_security_exemptions_namespaces` so the setting survives re-converge — don't hand-label and let the…
- **Источник:** `kb/troubleshooting/psa-blocks-privileged-workload.md`

### KEDB-132 · runc container escape (CVE-2025-31133 et al.) affects Kubespray v2.29.0
- **Симптом:** A malicious container image/config can exploit runc mount handling to escape to the host. runc `1.3.2` falls in the affected range `>=1.3.0-rc.1 <1.3.3`
- **Затронутые CIs:** security, cve, runc  ·  _v2.29.0 / 1.3.2_
- **Root cause:** **Affected:** Kubespray `v2.29.0` (runc `1.3.2`) · **Not affected:** `v2.29.1` / `v2.30.0` (runc `1.3.4` ≥ 1.3.3) and `v2.31.0` (runc `1.4.2`). See · CVE-2025-31133 verified against NVD; the two coordinated CVEs were fixed in the same runc releases
- **Workaround / fix:** Root cause: runc mount-race gadgets (masked paths, `/dev/console`, procfs write redirects). Fixed in runc `1.2.8` / `1.3.3` / `1.4.0-rc.3` · **Fix / mitigation:** upgrade runc to `≥1.3.3`. On Kubespray this means moving off `v2.29.0` (→ `v2.29.1`+, runc `1.3.4`), or pinning `runc_version` to a fixed release and re-running the `container-engine` role. As always, only run trusted images and enforce least-privilege (dro…
- **Источник:** `kb/troubleshooting/runc-container-escape-nov2025.md`

### KEDB-133 · runc: known CVEs by shipped version (osv.dev)
- **Симптом:** Each shipped runc version carries the CVEs listed below (osv.dev returns only vulnerabilities that affect the queried version, so this is authoritative affectedness)
- **Затронутые CIs:** security, cve, runc  ·  _>=v2.27.0 <=v2.31.0 / >=1.2.3 <=1.4.2_
- **Root cause:** | Component version | Kubespray | # CVEs | CVEs | |---|---|---|---| | 1.2.3 | v2.27.0 | 8 | superset — incl. the runc container-escape set + older CVEs (query osv.dev for the full list) | | 1.2.6 | v2.27.1 / v2.28.0 / v2.28.1 | 8 | (as above) | | 1.3.2 | v2.29.0 | 4 | CVE-2025-31133, CVE-2025-52565, CVE-2025-52881, CVE-2026-41579 | | 1.3.4 | v2.29.1 / v2.30.0 | 1 | CVE-2026-41579 | | 1.4.2 | v2.31.0 | 1 | CVE-2026-41…
- **Workaround / fix:** **CVE-2025-31133** [CVSS:4.0/AV:L/AC:L/AT:P/PR:L/UI:A/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H] — runc container escape via "masked path" abuse due to mount race conditions — fixed in: `1.2.8, 1.3.3, 1.4.0-rc.3` · **CVE-2025-52565** [CVSS:4.0/AV:L/AC:L/AT:P/PR:L/UI:A/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H] — runc container escape with malicious config due to /dev/console mount and related races — fixed in: `1.2.8, 1.3.3, 1.4.0-rc.3` · *…
- **Источник:** `kb/troubleshooting/runc-known-cves.md`

### KEDB-134 · tbot (Teleport Machine ID): certs not issued/renewed — join token, proxy address, role/output config
- **Симптом:** Workloads get auth failures because tbot isn't producing/renewing certs; tbot logs join or renewal errors
- **Затронутые CIs:** security, teleport, certificates  ·  _>=1.29 <=1.35 / 18.7.4_
- **Root cause:** tbot `18.x` ; verify the exact running image (some inventory-pinned tags may not exist) · **Join token:** tbot authenticates to Teleport with a join method/token; expired/wrong token → it can't start the identity · **Proxy/auth address:** the `--proxy-server`/auth address must be correct and reachable with valid TLS · **Output/role:** the bot's role must permit the requested certs, and the output destination (dir/sec…
- **Workaround / fix:** **Join — fix:** issue a valid join token / configure the join method; restart tbot to re-establish identity · **Address — fix:** set the correct Teleport proxy/auth address with a trusted cert and network reachability · **Role/output — fix:** grant the bot role the needed cert permissions and ensure the output destination is writable
- **Источник:** `kb/troubleshooting/tbot-machine-id.md`

### KEDB-135 · vault-secrets-webhook: pods blocked or secrets not injected — webhook down (failurePolicy), Vault auth, annotations
- **Симптом:** Two opposite symptoms: **pods can't be created at all** (`Internal error occurred: failed calling webhook ... connection refused`), or pods start but the **Vault secrets aren't injected** (env still holds the literal `vault:...` reference)
- **Затронутые CIs:** security, vault, admission  ·  _>=1.29 <=1.35 / >=1.21.4_
- **Root cause:** bank-vaults `vault-secrets-webhook` `v1.21.4` ; a **mutating admission webhook** that rewrites pods to run a `vault-env` init/sidecar which fetches secrets from Vault · **Webhook down blocks creates (the seam):** if the webhook's `failurePolicy` is `Fail` and its pod is down/unreachable, the API server **refuses to create matching pods** — cluster-wide if the selector is broad (, ) · **No injection:** injection only …
- **Workaround / fix:** **Pods blocked — fix:** restore the webhook pod; if it's an outage, scope `failurePolicy`/selector so only intended namespaces are gated (a broad `Fail` webhook is a cluster-wide risk). Exempt system namespaces from the selector · **No injection — fix:** confirm the namespace/pod matches the webhook selector and carries the expected `vault:` refs/annotations; injection is at pod creation, so recreate the workload aft…
- **Источник:** `kb/troubleshooting/vault-secrets-webhook-issues.md`

### KEDB-136 · Vault: pods 0/1, cluster sealed after restart
- **Симптом:** Vault pods `0/1 Running`, readiness never passes · `vault status` shows `Sealed: true` · Apps using the Agent Injector don't get secrets (Vault unavailable)
- **Затронутые CIs:** vault, secrets  ·  _>=1.15.0 <=1.23.0_
- **Root cause:** Applies to Vault **1.15–1.23** via the Helm chart (owner runs 1.21.2 — ). Readiness intentionally fails while sealed
- **Workaround / fix:** **Do not lose the unseal keys / recovery keys** — without them a sealed Vault (or KMS outage with Transit unseal) is unrecoverable. Keep a break-glass copy · The **Agent Injector** webhook TLS/CA must be correct or injection silently fails even once Vault is unsealed
- **Источник:** `kb/troubleshooting/vault-pods-sealed.md`

### KEDB-137 · x509 / TLS errors from node clock skew
- **Симптом:** TLS validates certificate NotBefore/NotAfter against the local clock. A node with significant clock skew (NTP not running/synced) rejects otherwise-valid certificates and can fail kubeadm join / API access
- **Затронутые CIs:** operations, security  ·  _>=v2.29.0 <=v2.31.0_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` clusters. This is a general Kubernetes/component operational issue (not tied to one Kubespray version); the relevant tunables are noted in Known Issues
- **Workaround / fix:** Enable/verify NTP (`ntp_enabled`, see the ntp run-tag/variables) and let clocks sync; then retry. Certificate expiry itself is covered by PRACTICE-CERTIFICATE_EXPIRY
- **Источник:** `kb/troubleshooting/clock-skew-tls-errors.md`

