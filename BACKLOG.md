# Kubepedia — Backlog

Deferred work items. This is a work-tracking file, not KDS knowledge; the base of
truth about what the KB *contains* is `kb/` + `index/`. Items here are agreed but
not yet implemented. Pull an item into a focused change when ready, then remove it.

Reconciled 2026-07-17 (v0.3.0): the Stage 1 Kubernetes layer, Stage 3 managed
components, ansible run-tags, the addon catalog, the OS domain (Ubuntu/Talos/Clevis),
the upgrade-horizon + CVE-remediation layer, and the large troubleshooting layer
(~160 docs, incl. the recon'd community set and the Kubespray↔kubeadm seam) are
**done** and were removed from this file. Only genuine open/deferred items remain.

## Open — deferred by owner (future version)

- **Access interfaces ("ручки") over the KB — start extracting value** — the knowledge is built and
  machine-retrievable (`index/documents.jsonl`, `relations.jsonl`, `tags.jsonl`, `aliases.jsonl` —
  [[CONCEPT-KB_NAVIGATION]]), but there is **no consumer surface** yet. Build the access handles so the
  base actually produces value: a **query/retrieval API** over `index/` (facet + graph + version
  filter), an **Upgrade & Change Report intake** (inventory `hosts.yaml` + current/target version →
  the existing `scripts/upgrade_report.py` output), and an **MCP server / connector** so AI clients
  answer version-accurate questions from the KB. This is the bridge from "knowledge base" to "usable
  product" (see the monetization directions discussed 2026-07-17). **Future version.** (added
  2026-07-18)
- **README (public-facing)** — the repo has **no README** on purpose; previous drafts were
  rejected. Must be **designed separately** (audience/structure/tone agreed with owner) before
  re-adding. Do not create ad hoc. Parked to a future version (2026-07-17).
- **Community sources — deep mining (sources.md category 6)** — the recon'd, code-verifiable
  candidates are now written; what remains is **deep community mining** (Reddit / Stack Overflow
  — blocked to the crawler — / Slack / engineering blogs / postmortems) with per-item
  re-verification against tagged code/docs. Never authoritative; lower confidence. Deferred.

## CNI plugins — DONE (2026-07-17)

All shipped CNI plugins are now indexed as `COMPONENT-*`: Cilium, Calico (default), **Flannel**
(0.28.4), **Kube-OVN** (1.12.21), **Kube-router** (2.1.1), **Macvlan**, and the meta-plugin
**Multus** (4.2.2). **Weave was removed upstream** — no `weave` role at v2.31.0 (noted in
[[VARIABLE-KUBE_NETWORK_PLUGIN]]). Remaining (niche, deferred): `custom_cni` (bring-your-own
manifests) and `ovn4nfv`; and the CNI-specific ansible run-tags (still excluded from the tag
index — low value).

## Open — periodic / maintenance

- **osv.dev CVE re-sweep** — the per-component CVE matrices and the upgrade-horizon are
  **date-sensitive**; re-run the osv.dev sweep and refresh `verified_at` when component versions
  change or new CVEs land. Optionally extend to the long tail of minor add-ons / per-K8s-patch
  versions.
- **New Kubespray release** — v2.31.0 is the current ceiling. When a newer tag ships, add its
  RELEASE + UPGRADE docs, advance the K8s window, and refresh the component/addon versions
  (nightly-update workflow, separate PR).

## Open — optional depth (only if wanted)

- **Calico depth** — BGP-peering config, IP pools/IPAM, Typha at scale, the `calico/rr`
  route-reflector role, a per-tag version table. (Owner said further Calico info is not needed
  right now.)
- **Core-component depth** — coredns/kube-proxy deeper, cloud-controller-manager / CSI
  controllers, beyond the current issue-mined set.
- **Talos depth** — `talosctl cluster` (local dev), Omni / Cluster API, exact Talos↔K8s
  support-matrix numbers.
- Curated Kubernetes "Known Issues" / "Urgent Upgrade Notes" per version.

## Possible architecture refinements

- **DONE (2026-07-17):** the "version envelope in frontmatter, precise per-version facts in the
  body" convention is now formalized as **D-017** in `standards/decisions.md`.
