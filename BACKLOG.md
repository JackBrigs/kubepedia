# Kubepedia — Backlog

Deferred work items. This is a work-tracking file, not KDS knowledge; the base of
truth about what the KB *contains* is `kb/` + `index/`. Items here are agreed but
not yet implemented. Pull an item into a focused change when ready, then remove it.

## README (public-facing)

The repository has **no README** on purpose right now — the previous drafts were
rejected by the owner. A public README must be **designed separately** (agree the
audience, structure, and tone with the owner first) before re-adding it. Do not
re-create it ad hoc.

## CNI plugins (other than Cilium)

Per owner decision (2026-07-16), only **Cilium** is indexed for CNI. The following
are deferred:

- **Calico** — note: this is Kubespray's **default** `kube_network_plugin`
  (`calico`), so it is a high-value future item despite being deferred now.
- Flannel
- Kube-OVN
- Kube-router
- Weave
- Macvlan
- Multus (meta-plugin)

## Kubernetes layer (Stage 1 depth)

Beyond version support, the full Kubernetes layer is not yet indexed:

- feature gates (per supported minor)
- API deprecations and removals
- KEPs relevant to 1.31–1.35
- kubelet behavior / generated kubelet configuration
- control-plane component versions (kube-apiserver, controller-manager,
  scheduler — all equal to `kube_version`)

## Managed components (Stage 3, by priority)

- CoreDNS
- ingress / load balancing (ingress-nginx, MetalLB, kube-vip)
- node-local DNS
- remaining managed add-ons

## Ansible run-tags

The `ansible_tag` KDS type exists (D-012). DONE: all run-tags indexed (113) except non-Cilium CNI tags (calico/flannel/weave/kube-ovn/kube-router/canal/custom_cni/macvlan/multus), which are excluded by owner decision. Bulk of the task-level tags were migrated programmatically from the 0.1.0 cache (confidence: verified).

## Sources — categories not yet collected (standards/sources.md)

So far only the strongest tiers are used: tagged Kubespray source code
(`confirmed`) and tag docs (`verified`). Not yet touched:

- **Community (category 6)** — Reddit, Stack Overflow, Server Fault, GitHub
  Discussions, Slack/Discord. **Owner asked to work on this.** Note: per
  `sources.md`, community knowledge is **never authoritative** — every statement
  taken from it must be re-verified against higher-priority sources (code / docs /
  merged PR) before entering the KB, and marked with the appropriate (lower)
  confidence.
- Security (category 4) — CVE / GitHub & Kubernetes Security Advisories per
  component (affected/fixed versions, severity, mitigation). STARTED: verified
  runc CVE-2025-31133 (affects v2.29.0) + CONCEPT-SECURITY_ADVISORIES tracker.
  **Blocker for deeper coverage:** web-scraping GitHub advisories does NOT yield
  reliable affected/fixed version ranges (and recent CVE IDs are unverifiable by
  the model) — do NOT fabricate. Do this properly via a structured source
  (osv.dev API — needs POST, so a small fetch script) or manual per-advisory NVD
  verification, only recording confirmed version-range hits.
- Upstream Kubernetes (category 2, direct) — KEPs, feature gates, API
  deprecations/removals from kubernetes/kubernetes (not via Kubespray).
- Engineering experience (category 5) — CNCF / KubeCon / engineering blogs /
  postmortems.
- GitHub Issues / merged PRs (the troubleshooting layer).

## Troubleshooting — RETURN AT THE END (owner request)

DONE so far: 15 in-range cache entries migrated + 18 mined from Kubespray merged
PRs (33 total) + 5 diagnostic runbooks. The Kubespray git source is exhausted for
the v2.29.0–v2.31.0 range (remaining fix commits are CI/test/docs/typo/niche-OS/
non-Cilium CNI).

**Come back at the end and expand from the remaining sources:**
- component release notes / known issues (etcd, Cilium, containerd, CoreDNS) for
  the versions we ship;
- **Community** (Reddit / Stack Overflow / Slack) — with mandatory re-verification
  and lower confidence (see the Sources section);
- curated Kubernetes "Known Issues" / "Urgent Upgrade Notes" per version (raw
  `kubernetes/kubernetes` issue mining is low-signal and unreliable via web).

## Possible architecture refinements (only if justified by implementation)

- formalize the D-005 "version envelope in frontmatter, precise per-version facts
  in the body" convention as an addendum in `standards/decisions.md`
  (currently applied consistently but not written down).
