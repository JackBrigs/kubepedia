# Project structure

A map of the Kubepedia repository — what each directory holds and which rules govern
it. This is orientation documentation, not KDS knowledge. Counts are indicative
(snapshot 2026-07-17, ~1250 KDS docs).

## Top level

```
CLAUDE.md              Project contract (scope, priorities, execution model, rules).
standards/             The written contract: how to work and how docs must look.
schema/                Machine-checkable KDS schema.
scripts/               Tooling (index generator, validators, upgrade-report generator).
kb/                    THE KDS knowledge base (the product).
index/                 Generated index over kb/ (do not hand-edit).
knowledge-base/        LEGACY 0.1.0 raw source cache — NOT KDS knowledge (see D-011).
reports/               Generated reports (upgrade reports, project report).
BACKLOG.md             Deferred work items (work-tracking, not knowledge).
```

Working material (not part of the base, git-ignored / uncommitted): `kubespray-src/`
(a Kubespray checkout used to verify facts against tags), `.venv/` (Python for the
validator).

## `kb/` — the KDS knowledge base

Atomic, version-aware KDS documents. One entity/fact per doc; stable `TYPE-SLUG` IDs;
typed relations + `[[wiki-links]]`. Subtrees:

```
kb/kubernetes/       (~24)   Kubernetes-layer: feature gates, API removals, KEPs,
                             kubelet config, PodSecurity, audit, per-version changes,
                             cluster networking/PKI/kubeadm-config, CPU isolation, …
kb/kubespray/                Kubespray-layer:
    variables/       (~896)  one doc per Kubespray variable (reference layer)
    ansible-tags/    (~113)  one doc per run-tag
    guides/          (~43)   best-practice / how-to / diagnostic runbooks
    releases/        (~15)   per-tag RELEASE-* and adjacent UPGRADE-* reports
    roles/           (~10)   Ansible roles
    playbooks/       (~6)    playbooks
    operations/      (~6)    HA, node add/replace, recovery, sequential upgrade
kb/components/       (~44)   32 managed components + version-selection / runtimes /
                             container-manager / CSI / helm anchors
kb/troubleshooting/  (~83)   symptom→cause→fix docs + the navigator map + CVE matrices
kb/ecosystem/        (~8)    adjacent domains (D-013): observability, GitOps/ArgoCD,
                             Velero, secrets (external/sealed), external-dns
kb/os/               (~15)   node OS ↔ Kubernetes: Ubuntu 24.04 (+26.04 future),
                             Clevis+LUKS2 disk encryption, and the Talos sub-domain
                             (kb/os/talos/: overview, machine-config, talosctl, upgrades,
                             networking, disk-encryption, system-extensions, provisioning,
                             Talos+Cilium, production guidelines, apid/bootstrap/etcd-restore
                             troubleshooting)
kb/addons/           (~47)   application-platform addon catalog (D-015): CONCEPT-ADDON_*
                             deep docs for ~46 upstream Helm-chart addons + the catalog
                             index; in-house ("собственный") charts stay catalog rows only
```

## `standards/` — the rules

- `project.md` — project-wide standards.
- `kds.md` — **the KDS document specification** (required fields, section profiles per
  type, ID grammar). The authority on what a `kb/` doc must look like.
- `sources.md` — source-priority tiers and confidence policy.
- `validation.md` — what every doc must pass before merge.
- `workflow.md` — the working process.
- `decisions.md` — **append-only decision log** (D-001…). Notably **D-011** (legacy
  cache vs KDS separation), **D-012** (`ansible_tag` type), **D-013** (ecosystem scope
  expansion), **D-014** (version range extended back to v2.27.0), **D-015** (application-
  platform addon catalog under `kb/addons/`).
- `structure.md` — this file.

## `schema/` and `scripts/`

- `schema/kds.schema.json` — JSON-Schema enforcing frontmatter fields/enums.
- `scripts/kdslib.py` — shared KDS library (types, section profiles, index builder).
- `scripts/generate_index.py` — rebuilds `index/` from `kb/`.
- `scripts/validate_kds.py` — validates all docs (schema + sections + ID grammar +
  relation resolution). Merge only on PASS.
- `scripts/upgrade_report.py` — generates the personalized Upgrade & Change Report from
  the RELEASE-*/UPGRADE-*/CONCEPT-* docs.

## `index/` — generated

- `documents.jsonl` — one record per doc (id, type, title, aliases, tags, versions, path).
- `relations.jsonl` — typed edges (source, type, target).
- `ids.txt` — all IDs. Regenerate with `generate_index.py`; never hand-edit.

## `knowledge-base/` — legacy 0.1.0 cache (NOT KDS)

Per **D-011**, this is the raw, pre-analyzed 0.1.0 source cache, organized by **Kubespray
version slices** (`versions/v2.27.0`…`v2.31.0`) plus `troubleshooting/`, `diffs/`,
`reports/`, `unversioned/`. It **accelerates research** but every fact must be
**re-verified against the tag** before becoming a KDS doc under `kb/`. The KDS graph and
the legacy cache **never mix** — a "no Kubernetes section here" observation about
`knowledge-base/` is expected; the Kubernetes KDS base lives in `kb/kubernetes/`.

## Where the rules live (quick answers)

- **Legacy-vs-KDS separation decision** → `standards/decisions.md` D-011 (+ CLAUDE.md
  Baseline).
- **`kb/` document rules** → `standards/kds.md` + `schema/kds.schema.json`, enforced by
  `scripts/validate_kds.py`.
- **Full directory structure** → this file (`standards/structure.md`).
