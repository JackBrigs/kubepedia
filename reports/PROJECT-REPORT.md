# Kubepedia — Global Project Report

_Version 0.2.0 · report date 2026-07-17 · branch `main` (local, unpushed)_

## 1. What Kubepedia is

An **AI-first, version-aware, source-driven** engineering knowledge base for **Kubernetes,
Kubespray, and Kubespray-managed components**. Every technical claim is bound to the
versions it holds for and traced to a source; the strongest evidence is **tagged source
code**. Baseline: Kubespray **v2.29.0**; covered range **v2.29.0 – v2.31.0** (Kubernetes
**1.31 – 1.35**).

## 2. Architecture (KDS)

- **Atomic documents** — one entity/fact per doc, not long-form articles.
- **Stable IDs** (`TYPE-SLUG`) that survive moves/renames/versions; relations use IDs.
- **Version-aware** — every doc carries a version envelope; precise per-version facts in
  the body.
- **Typed relations** graph + `[[wiki-links]]`; a generated index (`index/*.jsonl`).
- **Validation** — `generate_index.py` + `validate_kds.py` (JSON-Schema + section
  profiles + ID grammar + relation resolution). Merge only on PASS.
- **AI-first** — usable by any LLM/tool; simple clients answer from metadata/index without
  an LLM.

## 3. Content by the numbers

| Metric | Value |
|--------|-------|
| Documents | **1231** |
| Relations (typed edges) | 992 |
| Knowledge size (`kb/` + `index/`) | ~5.6 MB |
| Validator | **PASS**, 0 hard failures |

**By type:** variable 896 · ansible_tag 113 · troubleshooting 81 · best_practice 43 ·
component 32 · concept 30 · configuration 11 · role 10 · playbook 6 · release 4 · upgrade 4
· api 1.

**Two layers.** ~82% is the **reference layer** (variable/tag stubs mined bottom-up from
the source); ~18% is the **answer layer** (concept/config/practice/troubleshooting) that
synthesizes references into "how to do / diagnose X". The answer layer is the product; the
reference layer feeds it. All answer-layer docs are connected into the graph — the 439
orphans are exclusively leaf `variable`/`tag` stubs (by design).

## 4. Coverage by domain

- **Kubernetes layer (Stage 1)** — feature gates (from code), API removals, per-version
  operator changes (1.32–1.35), KEP catalog, kubelet configuration, control-plane
  versions, PodSecurity, audit, structured authentication config, dual-stack, CPU
  isolation, cluster networking/PKI/kubeadm-config anchors.
- **Kubespray mapping (Stage 2)** — version→K8s windows, component version-selection
  matrix, per-tag releases, adjacent-version upgrade reports, defaults audit, removed
  add-ons (dashboard/netcheck/ingress-nginx).
- **Managed components (Stage 3)** — 32 components; anchors for container-manager,
  container runtimes, containerd 2.x, etcd (+3.6), CoreDNS (+Corefile), NodeLocal DNS,
  Cilium (datapath/Hubble/encryption/LB), CSI layer, Helm, kube-proxy.
- **Troubleshooting (priority)** — **82 docs** with a symptom-navigator map: full
  pod-lifecycle (Pending→ContainerCreating→CrashLoop→OOMKilled→Terminating), images,
  service/egress/DNS, storage/PVC/mount, access (RBAC/exec-logs/webhook), etcd/certs,
  autoscaling, node/kernel limits, rollout — each symptom→cause→fix, source-verified.
- **Security** — CIS-style hardening checklist, PodSecurity, audit, encryption-at-rest,
  PKI lifecycle, per-component CVE matrices (osv.dev).
- **Operations** — cluster access, graceful upgrade, backup & DR, NTP, proxy, node
  labels/taints, HA endpoints.

## 5. Capstone — Upgrade & Change Report tool

`scripts/upgrade_report.py` turns the base into a **tool**: given `--from/--to` Kubespray
versions it walks the verified UPGRADE-* chain and emits a consolidated report (version
deltas, required actions, breaking changes, compatibility) + a cross-cutting Kubernetes
layer + an auto-harvested **Sources** list (full traceability). With `--inventory` it
**personalizes** — detects the cluster profile (CNI/runtime/proxy + enabled add-ons) and
transparently filters out technologies you don't use.

## 6. Quality & verification

- **Validator:** PASS, 0 hard failures on every change.
- **Accuracy audit:** 393 variable-doc default values verified 1:1 against source
  (0 mismatches); all 1205 code-source paths resolve; 0 broken wiki-links; all relation
  targets resolve.
- **Traceability fixes:** 10 stale source paths corrected; 2 duplicate docs de-duplicated.
- **Retrieval:** realistic operator queries resolve to the right doc top-1/top-3
  (validated repeatedly); the index carries aliases for goal-oriented search.

## 7. Deferred (owner decisions)

- **Calico** — Kubespray's *default* CNI, high-value, parked by owner. The only large
  in-scope content gap (21 vars + component + troubleshooting). All 41 undocumented
  top-level variables are non-Cilium CNI (Calico/flannel/kube-ovn/kube-router/multus).
- **Community sources (category 6)** — reconnaissance + a ~14-item re-verification plan
  are captured in `BACKLOG.md`; scheduled for project end.
- **README** — to be designed with the owner (drafts previously rejected).

## 8. Status

All defined scope (Stages 1–3 + the Upgrade-Report capstone) is **complete and verified**.
The base is content-complete for in-scope technologies, accuracy-audited, fully connected
at the answer layer, and backed by a working personalized upgrade-report tool. Remaining
work is owner-gated (Calico / community / README) or date-sensitive maintenance (re-run the
osv.dev CVE sweep as versions/CVEs change).

_All work is committed on the local `main` branch (nothing pushed). This session: 131
commits._
