# KEDB · networking & CNI

_45 известных ошибок. Сгенерировано; не править руками._

### KEDB-063 · Calico: calico-node CrashLoop / node NotReady / no pod networking
- **Симптом:** `calico-node` `CrashLoopBackOff` / readiness failing; nodes `NotReady` (`cni plugin not initialized`) · Cross-node pod traffic times out (same-node works); intermittent large-packet drops · BGP sessions never establish (BGP mode)
- **Затронутые CIs:** calico, cni, networking  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35 / >=3.30.3 <=3.31.5_
- **Root cause:** Applies to Calico **3.30.x–3.31.x** (per Kubespray tag; 3.30.3 @ v2.29.0 → 3.31.5 @ v2.31.0; Kubespray default CNI — ); dataplane modes in
- **Workaround / fix:** Switching dataplane/encapsulation on a live cluster is disruptive — a half-applied switch leaves mixed-mode nodes that can't talk · Large clusters without **Typha** put heavy watch load on the API server — enable `typha_enabled` past a few hundred nodes
- **Источник:** `kb/troubleshooting/calico-node-issues.md`

### KEDB-064 · Cilium 1.18 on AWS ENI — enableIPv4Masquerade default flips true→false, egress SNAT changes
- **Симптом:** After the Kubespray v2.28.0 → v2.29.0 upgrade on an **AWS ENI** Cilium cluster, pod **egress to external endpoints** behaves differently — connections that worked via node-IP SNAT now use the pod ENI IP (or vice-versa), breaking IP-allow-listed destinations or NAT expectations
- **Затронутые CIs:** cilium, aws, upgrade  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35 / >=1.18.2 <=1.19.3_
- **Root cause:** Applies to Cilium **1.18+** in **ENI mode** → Kubespray **v2.29.0** . Only relevant when `ipam.mode=eni` / `eni` datapath is in use (AWS); non-ENI clusters are unaffected · The default change is in `values.yaml@v1.18.2` and called out in `upgrade.rst@v1.18.2`: in `eni` mode `enableIPv4Masquerade` now defaults **false**
- **Workaround / fix:** **Fix (keep old behavior):** set **`enableIPv4Masquerade: true`** explicitly, or use `upgradeCompatibility<1.18`, to retain node-IP SNAT for pod egress · **Fix (adopt new default):** if pods should egress with their own ENI IPs (the AWS-native model), leave it `false` and ensure security groups / NAT / allow-lists accept the pod ENI IPs · **Pre-upgrade:** decide the egress model **before** v2.29.0 on AWS ENI clusters…
- **Источник:** `kb/troubleshooting/cilium-eni-masquerade-flip.md`

### KEDB-065 · Cilium 1.18 upgrade causes transient packet drops — serviceaccount added to identity labels
- **Симптом:** During/just after the Kubespray v2.28.0 → v2.29.0 upgrade (Cilium 1.17→1.18), you see a **spike in Cilium identities** and **short-lived denied/dropped** connections between policy-selected pods · Metrics show identity allocation churn; Hubble shows brief policy drops that clear on their own
- **Затронутые CIs:** cilium, identity, upgrade  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35 / >=1.18.2 <=1.19.3_
- **Root cause:** Applies to Cilium **1.18+** → Kubespray **v2.29.0** . The new label in the identity set means pods that previously shared an identity now split by ServiceAccount, so every affected endpoint regenerates its identity once (`upgrade.rst`@v1.18.2) · Identities drive policy enforcement ; a mass re-identity briefly widens the window where an endpoint's new identity isn't yet reflected in all policy maps → drops
- **Workaround / fix:** **Fix (accept, default):** the churn is **transient** — let identities settle; drops clear within the regeneration window. Schedule the upgrade in a maintenance window and expect a brief blip for policy-selected traffic · **Fix (avoid the change):** if you do **not** want ServiceAccount in identities, exclude it with a label filter (`!io\.cilium\.k8s\.policy\.serviceaccount`) so identities don't split — set before th…
- **Источник:** `kb/troubleshooting/cilium-serviceaccount-identity-drops.md`

### KEDB-066 · Cilium 1.19 BGP stops working — BGPv1 (CiliumBGPPeeringPolicy) removed, migrate to v2
- **Симптом:** After upgrading to Kubespray v2.31.0 (Cilium 1.19.3), BGP peers **drop** / routes are **no longer advertised**; LoadBalancer/pod-CIDR routes vanish from the fabric · `CiliumBGPPeeringPolicy` resources are ignored or rejected; the BGP control plane appears inactive
- **Затронутые CIs:** cilium, bgp, upgrade  ·  _>=v2.30.0 <=v2.31.0 / >=1.33 <=1.35 / >=1.18.2 <=1.19.3_
- **Root cause:** Applies to Cilium **1.19+** → Kubespray **v2.31.0** (, ). The `v2alpha1` BGP CRDs were **deprecated in 1.18** and the whole **BGPv1** path (`CiliumBGPPeeringPolicy`) **removed in 1.19** (`upgrade.rst`@v1.19.3) · The modern API is the **BGPv2** resource set under `cilium.io/v2`; it separates cluster config, peer config, advertisements, and per-node config
- **Workaround / fix:** **Fix:** migrate BGP config from `CiliumBGPPeeringPolicy` to the **v2** CRDs **before** the v2.30.0 → v2.31.0 upgrade — translate peers/advertisements into `CiliumBGPClusterConfig` + `CiliumBGPPeerConfig` + `CiliumBGPAdvertisement`. Validate BGP sessions come up on a canary before rolling · **Also removed earlier:** `metallb-bgp` support was removed back in **1.17** (Kubespray v2.28.0) — Cilium BGP control plane is t…
- **Источник:** `kb/troubleshooting/cilium-bgp-v1-removed.md`

### KEDB-067 · Cilium 1.19 breaks cross-cluster traffic — policy-default-local-cluster now on by default
- **Симптом:** After upgrading to Kubespray v2.31.0, pods that talk **across clusters** in a ClusterMesh start getting **denied** by network policy; same-cluster traffic is fine · CiliumNetworkPolicies that intended to allow remote-cluster endpoints no longer do
- **Затронутые CIs:** cilium, clustermesh, upgrade  ·  _>=v2.30.0 <=v2.31.0 / >=1.33 <=1.35 / >=1.18.2 <=1.19.3_
- **Root cause:** Applies to Cilium **1.19+** → Kubespray **v2.31.0** (, ). The `policy-default-local-cluster` flag existed in **1.18** (default kept all-cluster selection) and **flips to on** in **1.19** (`upgrade.rst`@v1.19.3) · Rationale: safer default (a policy shouldn't accidentally select the whole mesh); but it changes the semantics of existing policies in a multi-cluster deployment
- **Workaround / fix:** **Fix (keep old behavior):** set `policy-default-local-cluster=false` (Helm `clustermesh.policyDefaultLocalCluster` / config) to restore all-cluster selection, then plan a proper migration. Apply via a canary before rolling · **Fix (adopt new default):** update CiliumNetworkPolicies that must allow remote endpoints to explicitly select across clusters (per-cluster selectors), then leave the default on · **Pre-upgrade…
- **Источник:** `kb/troubleshooting/cilium-clustermesh-local-policy.md`

### KEDB-068 · Cilium 1.19 forwards mutual-auth traffic unauthenticated — mesh-auth now disabled by default
- **Симптом:** After upgrading to Kubespray v2.31.0, CiliumNetworkPolicies with `authentication.mode: required` no longer enforce mutual auth; traffic flows without the expected authentication · Cilium logs/policy status show a **warning** that mesh authentication is not enabled
- **Затронутые CIs:** cilium, security, upgrade  ·  _>=v2.31.0 <=v2.31.0 / >=1.33 <=1.35 / >=1.19.3 <=1.19.3_
- **Root cause:** Applies to Cilium **1.19** → Kubespray **v2.31.0** . The mutual-auth subsystem (mTLS-style identity handshake, related to SPIFFE/`encryption` — ) ships **off by default** in 1.19 where it was previously enabled (`upgrade.rst`@v1.19.3) · This is one of the three ClusterMesh/security default flips in the 1.18→1.19 jump (with policy-default-local-cluster on, and mesh-auth off)
- **Workaround / fix:** **Fix:** if you use mutual auth in policies, **re-enable** it explicitly — set `authentication.enabled=true` (Helm) / `mesh-auth-enabled=true` — and verify enforcement on a canary before rolling. Do this as part of the v2.30.0 → v2.31.0 upgrade plan · **If you don't use mutual auth:** no action; the default-off simply matches your usage · Treat as a **security-posture** change, not a connectivity break — traffic stil…
- **Источник:** `kb/troubleshooting/cilium-mesh-auth-disabled.md`

### KEDB-069 · Cilium 1.19 IPsec + KPR + BPF masquerade auto-enables eBPF host routing — CVE-2025-37959 kernel fix required
- **Симптом:** After upgrading to Kubespray v2.31.0 with IPsec + KPR + BPF masquerade enabled, encrypted traffic misbehaves / packets are mishandled on nodes whose kernel lacks the CVE-2025-37959 fix · The change is implicit: you did not turn on eBPF Host Routing — Cilium 1.19 enabled it because the feature combination is present
- **Затронутые CIs:** cilium, ipsec, security, cve  ·  _>=v2.31.0 <=v2.31.0 / >=1.33 <=1.35 / >=1.19.3 <=1.19.3_
- **Root cause:** Applies to Cilium **1.19** → Kubespray **v2.31.0** . Trigger is the **specific combination**: `encryption.type=ipsec` **+** `kube-proxy-replacement=true` **+** BPF masquerading. Any one absent → eBPF Host Routing is not auto-enabled by this rule (`upgrade.rst`@v1.19.3) · eBPF Host Routing bypasses the host network stack for performance; with IPsec it needs the kernel fix referenced by CVE-2025-37959
- **Workaround / fix:** **Fix (preferred):** patch node kernels to a version containing the CVE-2025-37959 fix before/at the v2.31.0 upgrade · **Fix (workaround):** set **`--enable-host-legacy-routing=true`** (Helm `bpf.hostLegacyRouting=true`) to keep legacy host routing and avoid the IPsec + eBPF-host-routing path until kernels are patched · Track alongside other Cilium CVEs for the shipped version
- **Источник:** `kb/troubleshooting/cilium-ipsec-host-routing-cve.md`

### KEDB-070 · Cilium 1.19 won't start / features off — piecemeal kube-proxy-replacement toggles removed
- **Симптом:** After upgrading to Kubespray v2.31.0 (Cilium 1.19.3), `cilium-agent` **crash-loops** with an unknown/removed flag error naming one of the `--enable-*` toggles · Or the agent starts but a service feature (NodePort, HostPort, ExternalIPs, session affinity) **doesn't work as before**, because it is now gated solely on `kube-proxy-replacement=true`
- **Затронутые CIs:** cilium, upgrade, kube-proxy-replacement  ·  _>=v2.30.0 <=v2.31.0 / >=1.34 <=1.35 / >=1.18.2 <=1.19.3_
- **Root cause:** Applies to Cilium **1.19+** → Kubespray **v2.31.0** . The flags were **deprecated in 1.18** (Kubespray v2.29.0/v2.30.0 — still accepted, warned) and **removed in 1.19** (`Documentation/operations/upgrade.rst`@v1.19.3). This is a two-step trap: it "works" on v2.29/2.30 and breaks on v2.31.0 · Consolidation rule: with `kube-proxy-replacement=true`, NodePort / HostPort / ExternalIPs / session-affinity / internal-traffic…
- **Workaround / fix:** **Fix:** remove the individual `--enable-*` toggles from cilium config / Helm values and rely on **`kube-proxy-replacement`** (set `true` for the KPR feature set, `false` to run alongside kube-proxy). Do this **before** the v2.30.0 → v2.31.0 upgrade · **If you ran kube-proxy-less** with these toggles individually enabled, confirm `kube-proxy-replacement=true` covers your set — most standalone features are now uncondi…
- **Источник:** `kb/troubleshooting/cilium-kpr-toggles-removed.md`

### KEDB-071 · Cilium config validation aborts the deploy
- **Симптом:** The run stops during the Cilium role on a task like `Stop if bad Cilium …` / `Check Cilium encryption …`, with a message naming a `cilium_*` variable, before the CNI is installed
- **Затронутые CIs:** cilium, cni, preflight  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` with `kube_network_plugin: cilium` (or `cilium_deploy_additionally`) · Cilium is the only CNI indexed in this KB (owner decision); other plugins have their own `check.yml`
- **Workaround / fix:** `cilium_hubble_event_buffer_capacity` must be a **power of two minus one** — a value like `10000` fails; use the nearest `2^n − 1` (e.g. `8191`) · The kernel checks parse `ansible_kernel` up to the first `-`; back-ported distro kernels can report a misleadingly low base version · These are config-validation guards, not runtime diagnostics — for a deployed Cilium that misbehaves, see the Cilium diagnostics runbook and…
- **Источник:** `kb/troubleshooting/cilium-config-validation.md`

### KEDB-072 · Cilium install fails: Helm can't adopt existing resource (invalid ownership metadata)
- **Симптом:** The Cilium deploy fails with (example seen on a real upgrade): ``` Unable to install Cilium: Unable to continue with install: Role "cilium-operator-tlsinterception-secrets" in namespace "cilium-secrets" exists and cannot be imported into the current release: invalid ownership metadata; label validation error: missing key "app.kubernetes.io/managed-by": must be set to "Helm"; annotation validation error: missing key "…
- **Затронутые CIs:** cilium, helm, upgrade, cni  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` with `kube_network_plugin: cilium` (Helm-based Cilium install) · **What this specific object is (verified from the Cilium chart).** `cilium-operator-tlsinterception-secrets` is a namespaced **`Role`** the Cilium chart (`cilium-operator/role.yaml`) creates so the **cilium-operator** can `create/delete/ update/patch` **secrets** in the TLS secrets namespace (`tls.secretsNamespac…
- **Workaround / fix:** **Values come from the error, not from this doc** — use whatever `kind/name`, `release-name`, and `release-namespace` Helm printed. Different feature/version → different object name (e.g. other `cilium-*` Roles/Secrets/ServiceAccounts) · **Alternative:** delete the conflicting object and let Helm recreate it (`kubectl -n cilium-secrets delete role cilium-operator-tlsinterception-secrets`). Adoption (label/annotate) i…
- **Источник:** `kb/troubleshooting/cilium-helm-ownership-adopt.md`

### KEDB-073 · Cilium IPsec breaks on upgrade — single-key removed, per-tunnel keys mandatory (1.16 dep., 1.17 removed)
- **Симптом:** After the Kubespray v2.27.0 → v2.28.0 upgrade (Cilium 1.15→1.17), IPsec-encrypted pod traffic **drops** / nodes can't establish encrypted tunnels · The `cilium-ipsec-keys` secret is in the old single-key format (no `+`), which 1.17 no longer accepts
- **Затронутые CIs:** cilium, ipsec, upgrade  ·  _>=v2.28.0 <=v2.31.0 / >=1.29 <=1.35 / >=1.17.3 <=1.19.3_
- **Root cause:** Applies to Cilium **1.16+** (mandatory) / **1.17+** (single-key removed) → Kubespray **v2.28.0+** (, ). Because Kubespray v2.27.0→v2.28.0 crosses **both** 1.16 and 1.17, the deprecation and removal land in one jump · Per-tunnel keys derive a distinct key per node pair (better security/rotation); the secret format encodes this with the `+` marker in the key spec (`upgrade.rst`@v1.16.19/@v1.17.3)
- **Workaround / fix:** **Fix:** recreate the `cilium-ipsec-keys` secret in the **per-tunnel** format (include the `+` so keys are per node pair) **before** the v2.27.0 → v2.28.0 upgrade, following the current IPsec key format . Rotate keys via the documented IPsec key-rotation procedure · **Also note (1.17→1.18):** the IPsec upgrade needs special attention and, on GKE, firewall rules must allow **ESP** — plan IPsec upgrades carefully acros…
- **Источник:** `kb/troubleshooting/cilium-ipsec-per-tunnel-keys.md`

### KEDB-074 · Cilium loadBalancer.mode not applied due to lowercase helm-values key
- **Симптом:** When installing Cilium through Kubespray, the configured balancing mode (`cilium_loadbalancer_mode`, e.g. `dsr` or `hybrid`) was not actually applied — Cilium kept running in the default mode (`snat`) despite the inventory setting
- **Затронутые CIs:** cilium, loadbalancer  ·  _v2.29.0_
- **Root cause:** Affected versions: v2.29.0 · Fixed versions: v2.29.1 · Users of v2.29.0 who set `cilium_loadbalancer_mode` should upgrade to v2.29.1
- **Workaround / fix:** Root cause: in the Cilium helm-values template the section key was written as `loadbalancer:` (lowercase `b`). The Cilium helm chart expects the camelCase key `loadBalancer:`, so the entire section (including `mode`) was silently ignored. File: `roles/network_plugin/cilium/templates/values.yaml.j2`. Fix: original Issue #12666. PR #12705 (cherry-pick of the original #12701 "Fixes #12666", commit `3c0cff983`) corrected…
- **Источник:** `kb/troubleshooting/cilium-loadbalancer-mode-not-rendered.md`

### KEDB-075 · Cilium operator image mismatch in offline registry (operator vs operator-generic)
- **Симптом:** On an offline / air-gapped deployment the `cilium-operator` pod fails to start and loops in CrashLoopBackOff because the container command `cilium-operator-generic` is not found. This happens because the image actually pulled does not contain the generic operator binary the chart expects
- **Затронутые CIs:** cilium, offline, registry  ·  _>=v2.30.0 <=v2.31.0_
- **Root cause:** Affected Kubespray versions: v2.30.0, v2.31.0 · Fixed versions: none released yet — the fix was merged to master after the v2.31.0 tag and will land in a future release (v2.31.1 / v2.32.0). Not fixed in v2.31.0 · Trigger conditions: deploying Cilium from an offline registry (non-cloud install path where the Helm chart adds the `-generic` suffix)
- **Workaround / fix:** Root cause: Kubespray syncs the `quay.io/cilium/operator` image into the offline registry, but the Cilium Helm chart for non-cloud installations automatically appends the `-generic` suffix and requests `cilium/operator-generic`, which was never mirrored · Fix: PR #13270 (merged 2026-06-22, after the v2.31.0 tag) changes `cilium_operator_image_repo` to `cilium/operator-generic` and adds `operator.image.override` to th…
- **Источник:** `kb/troubleshooting/cilium-operator-generic-offline-registry.md`

### KEDB-076 · Cilium/Hubble flow export settings ignored after Cilium 1.18 schema change
- **Симптом:** When Hubble flow export was enabled, the static exporter settings (file rotation / size) did not take effect, because Cilium 1.18 relocated them into helm-values under the `hubble.export.static` key while Kubespray generated values using the old schema
- **Затронутые CIs:** cilium, hubble  ·  _v2.29.0_
- **Root cause:** Affected versions: v2.29.0 (Cilium 1.18 with Hubble export) · Fixed versions: v2.29.1 · In v2.29.1 the default Cilium version is 1.18.4, so the new schema applies
- **Workaround / fix:** Root cause: Kubespray built the Hubble export helm-values using the pre-Cilium-1.18 schema, tied to the upstream schema change (cilium/cilium#36974). Fix: PR #12665 (master) aligned the values to the new `hubble.export.static` schema. Backport into release-2.29: PR #12718, commit `a04592de1`. Confirmed in tag v2.29.1 `roles/network_plugin/cilium/templates/values.yaml.j2`, which contains the new schema: ```yaml export…
- **Источник:** `kb/troubleshooting/cilium-hubble-export-schema.md`

### KEDB-077 · Cilium: empty-string defaults render as null in Helm values
- **Симптом:** Unquoted empty defaults in `values.yaml.j2` produced `null` instead of an empty string; the fix quotes them. Can cause Cilium install/config errors depending on the option
- **Затронутые CIs:** —  ·  _v2.30.0_
- **Root cause:** Affected Kubespray: `v2.30.0`. Fixed in: `v2.31.0` · Confirmed via merged PR #13109 and the tag code
- **Workaround / fix:** Fixed by PR #13109 (in `roles/network_plugin/cilium/templates/values.yaml.j2`). Workaround before upgrading: explicitly set the affected Cilium options (avoid empty), or upgrade to v2.31.0. Durable fix: upgrade to `v2.31.0` or later
- **Источник:** `kb/troubleshooting/cilium-empty-string-null-helm-values.md`

### KEDB-078 · Cilium: hostPort/portmap handled via extra conflist instead of Cilium
- **Симптом:** Kubespray shipped a `000-cilium-portmap.conflist` and install step for hostPort; the fix removes it and enables portmap through Cilium's Helm values instead, aligning hostPort handling with Cilium
- **Затронутые CIs:** —  ·  _>=v2.29.0 <=v2.29.1_
- **Root cause:** Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0` · Confirmed via the merged PR #12814 and the tag code
- **Workaround / fix:** Root cause fixed by PR #12814 (in `roles/network_plugin/cilium/templates/values.yaml.j2`). Workaround before upgrading: enable hostPort via Cilium values rather than the extra conflist. The durable fix is to upgrade to `v2.30.0` or later
- **Источник:** `kb/troubleshooting/cilium-portmap-hostport.md`

### KEDB-079 · cilium: known CVEs by shipped version (osv.dev)
- **Симптом:** Each shipped cilium version carries the CVEs listed below (osv.dev returns only vulnerabilities that affect the queried version, so this is authoritative affectedness)
- **Затронутые CIs:** security, cve, cilium  ·  _>=v2.27.0 <=v2.31.0 / >=1.15.9 <=1.19.3_
- **Root cause:** | Component version | Kubespray | # CVEs | CVEs | |---|---|---|---| | 1.15.9 | v2.27.0 / v2.27.1 | 20 | oldest shipped — largest exposure (query osv.dev for the full list) | | 1.17.3 | v2.28.0 | 10 | 1.17.x line (query osv.dev for the full list) | | 1.17.7 | v2.28.1 | 10 | 1.17.x line (query osv.dev for the full list) | | 1.18.2 | v2.29.0 | 6 | CVE-2025-64715, CVE-2026-26963, CVE-2026-33726, CVE-2026-41520, CVE-2026-…
- **Workaround / fix:** **CVE-2025-64715** [CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N] — Cilium with misconfigured toGroups in policies can lead to unrestricted egress traffic — fixed in: `1.16.17, 1.17.10, 1.18.4` · **CVE-2026-26963** [CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:N] — Cilium may not enforce host firewall policies when Native Routing, WireGuard and Node Encryption are enabled — fixed in: `1.18.6` · **CVE-2026-33726** [CVSS…
- **Источник:** `kb/troubleshooting/cilium-known-cves.md`

### KEDB-080 · Cilium: packet drops (identity, CT map full, policy)
- **Симптом:** Intermittent drops/timeouts; `cilium-dbg monitor --type drop` shows `Policy denied`, `Stale or unroutable IP`, or `CT: Map insertion failed` · Distinct from a total connectivity break
- **Затронутые CIs:** cilium, networking, cni  ·  _>=1.29 <=1.35 / >=1.18.0 <=1.19.6_
- **Root cause:** Applies to Cilium **1.18–1.19.6**
- **Workaround / fix:** Bumping BPF map sizes increases memory per node — size to the real connection count, don't over-allocate
- **Источник:** `kb/troubleshooting/cilium-packet-drops.md`

### KEDB-081 · Cilium: pod-to-pod / cross-node connectivity broken
- **Симптом:** Cross-node pod-to-pod traffic times out (same-node works) · New pods stuck without an IP / `NetworkNotReady` · Intermittent drops; DNS or service VIPs unreachable
- **Затронутые CIs:** cilium, networking, cni  ·  _>=1.18.0 <=1.19.6_
- **Root cause:** Applies to Cilium **1.18–1.19.6** (base ≤1.19.3 — )
- **Workaround / fix:** A second CNI or leftover iptables/CNI config from a previous plugin causes partial connectivity — ensure only Cilium manages the datapath · Cilium 1.18–1.19 patches close several CVEs — stay current within the minor
- **Источник:** `kb/troubleshooting/cilium-pod-connectivity.md`

### KEDB-082 · Cilium: undefined variable error for CiliumBGPAdvertisement labels
- **Симптом:** The `cilium-bgp-advertisement.yml.j2` template referenced a label variable that could be undefined; the fix guards it. Only affects clusters using Cilium BGP
- **Затронутые CIs:** —  ·  _v2.30.0_
- **Root cause:** Affected Kubespray: `v2.30.0`. Fixed in: `v2.31.0` · Confirmed via merged PR #13149 and the tag code
- **Workaround / fix:** Fixed by PR #13149 (in `roles/network_plugin/cilium/templates/cilium/cilium-bgp-advertisement.yml.j2`). Workaround before upgrading: avoid Cilium BGP advertisement config until upgrading, or define the missing labels. Durable fix: upgrade to `v2.31.0` or later
- **Источник:** `kb/troubleshooting/cilium-bgp-advertisement-labels-undefined.md`

### KEDB-083 · cilium_enable_prometheus had no effect (not wired to Helm values)
- **Симптом:** The variable existed in defaults/sample inventory but `prometheus.enabled` was missing from `values.yaml.j2`, making the flag a no-op. The fix adds the field so the flag works
- **Затронутые CIs:** —  ·  _>=v2.29.0 <=v2.30.0_
- **Root cause:** Affected Kubespray: `>=v2.29.0 <=v2.30.0`. Fixed in: `v2.31.0` · Confirmed via merged PR #13142 and the tag code
- **Workaround / fix:** Fixed by PR #13142 (in `roles/network_plugin/cilium/templates/values.yaml.j2`). Workaround before upgrading: enable Cilium metrics directly via Helm values / a Cilium ConfigMap patch, or upgrade to v2.31.0. Durable fix: upgrade to `v2.31.0` or later
- **Источник:** `kb/troubleshooting/cilium-enable-prometheus-noop.md`

### KEDB-084 · Cluster traffic blocked by a firewall (required ports)
- **Симптом:** Intermittent or one-directional cluster failures with no obvious app cause: nodes flap `NotReady`; `kubectl logs`/`exec`/`port-forward` hang or `timeout` (kubelet `10250`); API/etcd unreachable from some nodes; pods on node A can't reach pods/DNS on node B; NodePort services unreachable; Cilium health checks / Hubble failing. Often appears only between certain nodes or after enabling a host firewall
- **Затронутые CIs:** networking, firewall, ports, preflight  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0`. Kubespray configures no firewall rules — the host firewall is the operator's responsibility · Required ports (from `docs/operations/port-requirements.md`, tag `v2.31.0`):
- **Workaround / fix:** **Fix:** either disable the host firewall (Kubespray's recommendation for simplicity) or open the ports above between the relevant host groups. On RHEL-family this is the single most common cause of a partially-working cluster · **Direction matters:** control-plane ports must be reachable **from** worker nodes and vice-versa; overlay (VXLAN `8472`) must be open **both** ways between all nodes · Cloud environments enf…
- **Источник:** `kb/troubleshooting/firewall-ports-blocked.md`

### KEDB-085 · cni-plugins: known CVEs by shipped version (osv.dev)
- **Симптом:** Each shipped cni-plugins version carries the CVEs below (osv.dev returns only vulns affecting the queried version — authoritative affectedness)
- **Затронутые CIs:** security, cve, cni  ·  _>=v2.27.0 <=v2.31.0 / >=1.4.0 <=1.9.1_
- **Root cause:** | Version | Kubespray | # | CVEs | |---|---|---|---| | 1.4.0 | v2.27.0 | 0 | — (osv.dev reports none) | | 1.4.1 | v2.27.1-v2.28.1 | 0 | — (osv.dev reports none) | | 1.8.0 | v2.29.0-v2.30.0 | 1 | CVE-2025-67499 | | 1.9.1 | v2.31.0 | 0 | — |
- **Workaround / fix:** **CVE-2025-67499** [CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:L/I:L/A:H] — CNA Plugins Portmap nftables backend can intercept non-local traffic — fixed in: `1.9.0`
- **Источник:** `kb/troubleshooting/cni-plugins-known-cves.md`

### KEDB-086 · containerd NO_PROXY rendered as a character array behind a proxy
- **Симптом:** The `no_proxy` value ends up rendered as a character array, e.g.: ``` "NO_PROXY=['1', '7', '2', '.', '3', '1', '.', '1', '3', '2', '.', '8', '8', ...]" ``` instead of the expected: ``` "NO_PROXY=172.31.132.88,...,svc,svc.cluster.local" ``` Because the malformed value is written into the containerd systemd drop-in unit, proxying for containerd is misconfigured
- **Затронутые CIs:** containerd, proxy, no-proxy  ·  _>=v2.29.0 <=v2.30.0_
- **Root cause:** Affected Kubespray versions: v2.29.0, v2.29.1, v2.30.0 · Fixed versions: v2.29.2 (release-2.29 backport) and v2.31.0 (master) · Not fixed in v2.30.0 — the master fix #12981 was merged after the v2.30.0 tag (2026-01-30) and there is no backport to release-2.30 · Trigger conditions: a proxy is configured and the effective `no_proxy` is assembled by Kubespray; whether it manifests depends on the native-Jinja templating …
- **Workaround / fix:** Root cause: `no_proxy` is built by a custom Jinja loop in `roles/network_facts/tasks/no_proxy.yml` (fact `no_proxy_prepare`, folded scalar `>-` with a `for item in ...` loop, then `delegate_to: localhost`). Under the native-Jinja templating of newer Ansible versions the result is in some cases interpreted as an iterable string (a character array) rather than a single string. Per the fix author, the problem appears "s…
- **Источник:** `kb/troubleshooting/containerd-no-proxy-char-array.md`

### KEDB-087 · containerd: stale sandbox / reserved name after crash or disk-full
- **Симптом:** Pods stuck `Terminating`; kubelet: `StopPodSandbox from runtime service failed: ... failed to destroy network for sandbox "...": ... decoding version from network config: unexpected end of JSON input` · `CreateContainerError: failed to reserve container name "..."`; on startup: `failed to recover state: ... name xxx is reserved for xxx`
- **Затронутые CIs:** containerd, runtime, cni  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35** on containerd . Namespace-stuck is a related terminating class
- **Workaround / fix:** Alert on `StopPodSandbox` failures — they silently pile up stuck pods. Upstream plans to tolerate `ENOSPC` during restart recovery
- **Источник:** `kb/troubleshooting/containerd-stale-sandbox-recovery.md`

### KEDB-088 · controller-manager: EndpointSlice churn / stale endpoints
- **Симптом:** Warning `EndpointSlice informer cache is out of date`; endpoints rebalanced between slices with no pod change; CoreDNS returns NXDOMAIN intermittently · Recovered pods stuck under `notReadyAddresses`; Endpoints controller logs `the object has been modified; please apply your changes to the latest version and try again`
- **Затронутые CIs:** controller-manager, endpointslice, networking  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35**, worse for Services above the **100-endpoints-per-slice** threshold. Distinct from "no endpoints at all"
- **Workaround / fix:** This is load-sensitive — watch the `EndpointSlice informer cache is out of date` warning as an early signal under scale
- **Источник:** `kb/troubleshooting/kcm-endpointslice-churn.md`

### KEDB-089 · Cross-node pod traffic hangs — VXLAN/overlay MTU mismatch
- **Симптом:** The default Cilium datapath is VXLAN (`cilium_tunnel_mode: vxlan`), which adds ~50 bytes of encapsulation. If the pod MTU is not reduced accordingly (or the underlay blocks large frames / has jumbo-frame mismatch), fragmented/large packets are dropped
- **Затронутые CIs:** operations, networking  ·  _>=v2.29.0 <=v2.31.0_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` clusters. This is a general Kubernetes/component operational issue (not tied to one Kubespray version); the relevant tunables are noted in Known Issues
- **Workaround / fix:** Ensure the effective pod MTU accounts for the VXLAN overhead (Cilium auto-detects, but verify), align underlay MTU/jumbo-frame settings across nodes, or use native routing instead of VXLAN. See PRACTICE-CILIUM_DIAGNOSTICS
- **Источник:** `kb/troubleshooting/vxlan-mtu-mismatch.md`

### KEDB-090 · Empty Cilium native_routing_cidr renders as null in Helm values
- **Симптом:** With Cilium native routing enabled (notably an IPv4-only-stack Cluster mesh), helm-values generation breaks due to `null` values. It manifests when `cilium_native_routing_cidr` / `cilium_native_routing_cidr_ipv6` are not set explicitly
- **Затронутые CIs:** cilium, native-routing, helm-values  ·  _>=v2.29.1 <=v2.30.0_
- **Root cause:** Affected versions: v2.29.1, v2.30.0 (vulnerable code confirmed in both tags) · Fixed versions: v2.31.0 only. There is no backport to release-2.29 / release-2.30 — the problem is NOT resolved in v2.29.x and v2.30.x; use the workaround · Triggered when native routing is enabled and the CIDR variables are left at their empty-string defaults
- **Workaround / fix:** Root cause: in `roles/network_plugin/cilium/templates/values.yaml.j2` the keys `ipv4NativeRoutingCIDR` / `ipv6NativeRoutingCIDR` substitute the variables without quotes. With the empty-string default value, the YAML key gets an empty value that Helm interprets as `null` (rather than an empty string). Fix: PR #13109 quotes both substitutions: ```diff -ipv4NativeRoutingCIDR: {{ cilium_native_routing_cidr }} -ipv6Native…
- **Источник:** `kb/troubleshooting/cilium-native-routing-cidr-null.md`

### KEDB-091 · ingress-nginx: 502 Bad Gateway / 504 Gateway Timeout
- **Симптом:** Clients get 502/504 from the ingress for a specific host/path · Intermittent 502s under load
- **Затронутые CIs:** ingress-nginx, ingress, networking  ·  _>=1.29 <=1.35 / >=1.11.0 <=1.15.1_
- **Root cause:** Applies to controller **1.11–1.15** (owner deploys 1.12.0 — )
- **Workaround / fix:** 1.12.0 tightened **annotation validation** (High) — snippet annotations may be silently dropped ; and 1.12.0 is IngressNightmare- affected (patch to 1.12.1)
- **Источник:** `kb/troubleshooting/ingress-nginx-502-504.md`

### KEDB-092 · ingress-nginx: annotation rejected / Ingress fails after upgrade
- **Симптом:** `admission webhook "validate.nginx.ingress.kubernetes.io" denied the request: annotation ... contains invalid value` when applying a previously-accepted Ingress · Configuration-snippet / server-snippet annotations no longer take effect · Metrics scraping breaks (metric endpoint/metric removed)
- **Затронутые CIs:** ingress-nginx, ingress, upgrade  ·  _>=1.12.0 <=1.15.1_
- **Root cause:** Applies to controller **1.12.0–1.15.1** (owner deploys 1.12.0 — ) · Part of the ingress-nginx hardening after the 2025 IngressNightmare CVEs
- **Workaround / fix:** **Do not stay on 1.12.0** — it is IngressNightmare-affected (**CVE-2025-1974**, 9.8); fixed in controller **1.12.1**. Restrict access to the admission webhook until patched
- **Источник:** `kb/troubleshooting/ingress-nginx-annotation-rejected.md`

### KEDB-093 · ingress2gateway: converted Gateway API objects incomplete — provider annotations not translated (one-shot CLI)
- **Симптом:** The generated `HTTPRoute`/`Gateway` lacks behavior the original Ingress had (rewrites, TLS, auth), or some Ingresses aren't converted
- **Затронутые CIs:** networking, gateway-api, migration  ·  _>=1.29 <=1.35_
- **Root cause:** ingress2gateway ; output consumed by a Gateway API controller · **Annotations don't map:** controller-specific Ingress annotations are not part of the Gateway API spec; the tool translates the standard parts and skips the rest · **One-shot:** it's a migration aid, not a running component — re-run it as source Ingresses change
- **Workaround / fix:** **Incomplete output — fix:** manually add the missing behavior as Gateway API constructs (filters, policies) supported by your controller; the tool only covers the standard mapping · **Missing conversions — fix:** ensure the provider/IngressClass is one the tool supports; convert unsupported ones by hand
- **Источник:** `kb/troubleshooting/ingress2gateway-conversion.md`

### KEDB-094 · kube-proxy nftables mode requires kernel >= 5.13
- **Симптом:** Preinstall aborts on the task `Stop if kernel version is too low for nftables` when `kube_proxy_mode: nftables` is set and the node kernel is `< 5.13`
- **Затронутые CIs:** kube-proxy, nftables, kernel, preflight  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` · The check: `ansible_kernel.split('-')[0] is version('5.13', '>=')`, guarded by `when: kube_proxy_mode == 'nftables'` and `not ignore_assert_errors` · Upstream kube-proxy nftables itself wants a reasonably recent kernel; 5.13 is the floor Kubespray enforces. nftables is GA since Kubernetes `1.33` ; `ipvs` deprecated in `1.35`
- **Workaround / fix:** **Fix options:** upgrade the node kernel to `>= 5.13`, or keep `kube_proxy_mode: ipvs` / `iptables` on older kernels (both remain supported in-range; `ipvs` is deprecated upstream from `1.35` but still functional) · The kernel version is parsed from `ansible_kernel` up to the first `-`; distro back-ported kernels reporting an old base version can trip the check even if nftables would work — verify the effective nft/k…
- **Источник:** `kb/troubleshooting/nftables-kernel-too-low.md`

### KEDB-095 · kubectl exec / logs / port-forward fails (kubelet reachability)
- **Симптом:** `kubectl exec/logs/port-forward <pod>` returns `Error from server: error dialing backend: …` / `unable to upgrade connection` / `remote error: tls: …` / a timeout — often for pods on **specific** nodes only
- **Затронутые CIs:** kubectl, kubelet, networking  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` · The apiserver connects to the kubelet's HTTPS API on **`10250`** to stream these commands. Anything blocking or breaking that hop fails all four verbs
- **Workaround / fix:** **`error dialing backend` / timeout** — apiserver can't reach kubelet `10250`: host firewall or security-group blocking the port between control-plane and node , or the node is down/NotReady · **`x509` / `tls`** — kubelet serving-cert trust: the default self-signed kubelet cert isn't verifiable if strict verification is on; use the rotated/CSR-approved serving cert or the insecure-tls path as appropriate · **`unable …
- **Источник:** `kb/troubleshooting/kubectl-exec-logs-fails.md`

### KEDB-096 · kubelet: node NotReady — CNI not initialized (cni plugin not initialized)
- **Симптом:** Node condition `Ready=False`, reason `KubeletNotReady` · kubelet log: `"Container runtime network not ready" networkReady="NetworkReady=false reason:NetworkPluginNotReady message:Network plugin returns error: cni plugin not initialized"`
- **Затронутые CIs:** kubelet, cni, nodes  ·  _>=1.29 <=1.35_
- **Root cause:** Applies to Kubernetes **1.29–1.35**. **Expected transient** right after `kubeadm init`/join until the CNI comes up; **persistent** = the CNI is broken
- **Workaround / fix:** A half-installed CNI (config present but agent crashlooping) shows the same message — always check both the config file **and** the CNI pod health
- **Источник:** `kb/troubleshooting/kubelet-node-notready-cni.md`

### KEDB-097 · MetalLB L2: EXTERNAL-IP assigned but unreachable — kube-proxy IPVS needs strictARP
- **Симптом:** `kubectl get svc` shows a real `EXTERNAL-IP` (not `<pending>`), but `curl`/ping to it from **off the cluster** times out or is intermittent · ARP for the LB IP resolves to the **wrong MAC** (a node's `kube-ipvs0`, or flapping), not the MetalLB speaker's node
- **Затронутые CIs:** networking, metallb, kube-proxy, interaction  ·  _>=v2.27.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies across **v2.27.0–v2.31.0**. Triggered specifically by **MetalLB L2 + `kube_proxy_mode: ipvs`** (, ) · **Why:** IPVS mode creates the `kube-ipvs0` dummy interface and binds all Service (including LoadBalancer) IPs to it. Without `strictARP`, the node replies to ARP requests for those IPs on every interface, so the LAN sees ARP answers from nodes that shouldn't own the LB IP — competing with MetalLB's L2 speake…
- **Workaround / fix:** **Fix (Kubespray):** set **`kube_proxy_strict_arp: true`** and re-converge, so kube-proxy only answers ARP for IPs actually local to the interface — MetalLB's L2 speaker then owns the LB IP's ARP. This is a **required** setting for MetalLB L2 on IPVS · **Verify after:** the kube-proxy ConfigMap shows `strictARP: true`, kube-proxy pods restarted, and `arping` returns a single stable MAC · **Alternative:** MetalLB **BG…
- **Источник:** `kb/troubleshooting/metallb-l2-strictarp-unreachable.md`

### KEDB-098 · MetalLB: BGP session not established / routes not advertised
- **Симптом:** Service external IP assigned but not routable from outside · BGP session stuck `Idle`/`Connect`/`Active` (never `Established`) · Some pools advertised, others not
- **Затронутые CIs:** metallb, bgp, networking  ·  _>=0.13.0 <=0.16.1_
- **Root cause:** Applies to MetalLB **0.13–0.16** (base 0.13.9 — ). Config is CRD-only
- **Workaround / fix:** FRR vs native mode must match your CRs and be chosen at install ; the newer `FRR-K8s` mode changes how BGP config is delivered
- **Источник:** `kb/troubleshooting/metallb-bgp-session-down.md`

### KEDB-099 · MetalLB: config ignored (ConfigMap→CRD) / FRR mode
- **Симптом:** `LoadBalancer` Services stay `<pending>` (no IP assigned) · A `config` ConfigMap is present but has no effect · BGP sessions don't come up after choosing the FRR implementation
- **Затронутые CIs:** metallb, networking, loadbalancer, upgrade  ·  _>=0.13.0 <=0.16.1_
- **Root cause:** Applies to MetalLB **0.13.0–0.16.1** (base: 0.13.9 — )
- **Workaround / fix:** Across 0.13→0.16, validate the CR set and the chosen BGP mode after upgrade; confirm exact per-release changes against the MetalLB release notes for your target patch
- **Источник:** `kb/troubleshooting/metallb-config-crd-frr.md`

### KEDB-100 · MetalLB: LoadBalancer service stuck EXTERNAL-IP <pending>
- **Симптом:** `kubectl get svc` shows a LoadBalancer service with `EXTERNAL-IP` = `<pending>` indefinitely; the service never gets an IP, so it's unreachable from outside the cluster
- **Затронутые CIs:** metallb, load-balancer, networking  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0`. Defaults: `metallb_enabled: false`, `metallb_speaker_enabled: "{{ metallb_enabled }}"`, `metallb_namespace: metallb-system`. Default mode is **Layer2** (BGP optional) · **Layer2 prerequisite:** `kube_proxy_strict_arp: true` — required so kube-proxy's `kube-ipvs0` interface doesn't answer ARP for the VIPs. Without it, Layer2 announcement doesn't work · Address pools are declar…
- **Workaround / fix:** **Enable MetalLB:** `metallb_enabled: true` (also enables the speaker) · **Layer2 prerequisite:** `kube_proxy_strict_arp: true` — without it Layer2 silently fails to announce. Applies to the kube-proxy config, so it needs kube-proxy re-applied · **Define a pool:** add `metallb_config.address_pools.<name>.ip_range` (range or CIDR) and attach it: `metallb_config.layer2: [<name>]` for Layer2 (or a BGP peer block) · **Po…
- **Источник:** `kb/troubleshooting/metallb-service-pending.md`

### KEDB-101 · Neighbour table overflow at scale — raise net.ipv4.neigh gc_thresh (ARP/NDP cache)
- **Симптом:** `dmesg` / kernel log spams `neighbour: arp_cache: neighbor table overflow!` (or `ndisc_cache` for IPv6) · Pod-to-pod or node-to-node traffic is **intermittently dropped**; latency spikes; some flows work, others don't, seemingly at random — and it correlates with cluster size/connection count
- **Затронутые CIs:** networking, scale, kernel  ·  _>=v2.27.0 <=v2.31.0 / >=1.29 <=1.35_
- **Root cause:** Applies across **v2.27.0–v2.31.0**; a **scale** failure, not a version bug · **Why:** the ARP/NDP cache has three thresholds — `gc_thresh1` (below which entries are never GC'd, default 128), `gc_thresh2` (soft cap, default 512), `gc_thresh3` (hard cap, default 1024). A node that must track more than ~`gc_thresh3` neighbours (large flat networks, many pods per node with routed/overlay CNIs, Calico/kube-router with man…
- **Workaround / fix:** **Fix — raise the thresholds** on every affected node (persist via `/etc/sysctl.d/`), scaled to the neighbour count you expect: · **Size it right:** the hard cap should comfortably exceed peak neighbours (roughly nodes × pods-seen + gateways); leave headroom · **Reduce pressure alternatively:** a dataplane that tunnels/encapsulates remote pods (or aggregates routes) shrinks the neighbour set — a design lever if bumpi…
- **Источник:** `kb/troubleshooting/arp-neigh-table-overflow.md`

### KEDB-102 · nf_conntrack table full — dropped packets / intermittent timeouts
- **Симптом:** Every tracked connection consumes a conntrack slot; high connection churn (many short-lived connections) can exhaust `nf_conntrack_max`. kube-proxy sizes this, but very busy nodes can still fill it
- **Затронутые CIs:** operations, networking  ·  _>=v2.29.0 <=v2.31.0_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` clusters. This is a general Kubernetes/component operational issue (not tied to one Kubespray version); the relevant tunables are noted in Known Issues
- **Workaround / fix:** Raise `nf_conntrack_max` (via kube-proxy conntrack settings or a sysctl in `additional_sysctl`), reduce connection churn (keep-alive/pooling), and check for connection leaks. With Cilium kube-proxy replacement the datapath differs (see PRACTICE-CILIUM_DIAGNOSTICS)
- **Источник:** `kb/troubleshooting/conntrack-table-full.md`

### KEDB-103 · node haproxy: wrong IPv6 bind syntax in haproxy.cfg
- **Симптом:** `haproxy.cfg.j2` rendered an invalid IPv6 `bind` line; on dual-stack/IPv6 nodes haproxy could not bind the API frontend, breaking the local apiserver LB
- **Затронутые CIs:** —  ·  _>=v2.29.0 <=v2.29.1_
- **Root cause:** Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0` · Confirmed via the merged PR #12862 and the tag code
- **Workaround / fix:** Root cause fixed by PR #12862 (in `roles/kubernetes/node/templates/loadbalancer/haproxy.cfg.j2`). Workaround before upgrading: correct the haproxy bind line manually, or switch the local LB type. The durable fix is to upgrade to `v2.30.0` or later
- **Источник:** `kb/troubleshooting/haproxy-ipv6-binding-syntax.md`

### KEDB-104 · node.status kubeProxyVersion is empty — field deprecated and no longer populated (K8s 1.33)
- **Симптом:** `kubectl get node -o jsonpath='{.status.nodeInfo.kubeProxyVersion}'` returns **empty** · A monitoring/inventory tool that displayed "kube-proxy version" now shows blank / null for all nodes · Alerts or reports keyed on that field fire falsely
- **Затронутые CIs:** kubernetes, kube-proxy, upgrade  ·  _>=v2.27.0 <=v2.31.0 / >=1.33 <=1.35_
- **Root cause:** The `DisableNodeKubeProxyVersion` gate went **on by default in K8s 1.33** (`keps/sig-network/4004-...`). In the Kubespray range that is **v2.31.0** (K8s 1.33+); earlier Kubespray tags (K8s ≤1.32) still populate it · Why: the field was set by the **kubelet** to the kubelet/node version, never to the actual kube-proxy version — it was misleading and is being removed rather than fixed
- **Workaround / fix:** **Fix:** update tooling to **stop reading** `status.nodeInfo.kubeProxyVersion`; derive the version from the kube-proxy DaemonSet image or `kube-proxy --version` instead · **Cilium/kube-proxy-free clusters:** the field was already meaningless there (no kube-proxy) — this just makes it empty everywhere consistently · This is a **silent, non-breaking** change ; the risk is only false alerts from tooling. There is no sup…
- **Источник:** `kb/troubleshooting/kubeproxyversion-field-removed.md`

### KEDB-105 · Pod stuck in ContainerCreating (CNI / sandbox / mount)
- **Симптом:** `kubectl get pods` shows `ContainerCreating` (or `0/1` never becoming Ready) for a long time; the node may report `NetworkPluginNotReady` / `container runtime network not ready: cni plugin not initialized`
- **Затронутые CIs:** pods, cni, networking  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` · The kubelet marks the node `NetworkReady=false` until a CNI writes its config into `/etc/cni/net.d/` and its pods are running — new/all Pods on that node stay `ContainerCreating` until then
- **Workaround / fix:** **Network / CNI not ready** (`cni plugin not initialized`, `NetworkPluginNotReady`) — the CNI DaemonSet isn't healthy on that node. Check Cilium/CNI pods and their logs; a bad Cilium config aborts before it's ready ; a blocked overlay port (VXLAN 8472) also breaks it · **Image pull** (`ErrImagePull`/`ImagePullBackOff` shown alongside) — registry/mirror/ auth (, ) · **Volume / mount** (`unbound PersistentVolumeClaims`…
- **Источник:** `kb/troubleshooting/pod-containercreating.md`

### KEDB-106 · Pods can't reach the internet / external IPs (egress, masquerade)
- **Симптом:** From a pod, `wget/curl <external-ip>` or `ping 1.1.1.1` times out, while `<service>.<ns>` / other pods work. External name resolution may or may not work separately
- **Затронутые CIs:** networking, egress, cni  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` · Pod IPs come from `kube_pods_subnet` — **not routable** on your LAN. To leave the cluster they must be SNAT'd to the node IP. Which addresses get masqueraded depends on the CNI's masquerade config
- **Workaround / fix:** **Masquerade disabled/misconfigured** — pod IPs leave un-SNAT'd and replies never return. Ensure masquerade is on for external destinations; with native routing set `cilium_native_routing_cidr` correctly (empty/wrong = the classic mis-render, ) · **Egress NetworkPolicy** — a policy selects the pod and denies egress; add an allow rule (and allow DNS to kube-dns, or name resolution also breaks) · **Node-level firewall …
- **Источник:** `kb/troubleshooting/pod-egress-internet.md`

### KEDB-107 · Service unreachable / has no endpoints
- **Симптом:** Connecting to a Service (ClusterIP:port, or `svc.ns.svc.cluster.local`) times out or gives `connection refused`, while the backing pods themselves are up
- **Затронутые CIs:** service, networking, kube-proxy  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` · Traffic path: **Service → EndpointSlice (ready pods) → kube-proxy/CNI rules → pod**. A break anywhere makes the Service unreachable; isolate *which* hop
- **Workaround / fix:** **Selector mismatch** — the Service `selector` doesn't match the pods' labels (typo, wrong label, wrong namespace). Fix the selector or the pod labels · **No Ready pods** — pods exist but fail readiness → not added to endpoints. Fix the readiness probe / the app · **Wrong `targetPort`** — endpoints exist but point at a port nothing listens on · **kube-proxy not programming rules** — kube-proxy pod down, or in a mode …
- **Источник:** `kb/troubleshooting/service-no-endpoints.md`

