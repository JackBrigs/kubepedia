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

The `ansible_tag` KDS type exists (D-012). Indexed (24): `etcd-secrets`, `etcd`,
`control-plane`, `download`, `preinstall`, `container-engine`, `node`, `kubeadm`,
`network`, `apps`, `client`, `cluster-roles`, `node-label`, `node-taint`,
`resolvconf`, `reset`, `pre-upgrade`, `system-upgrade`, `post-upgrade`, `etcdctl`,
`ingress-controller`, `policy-controller`, `external-provisioner`,
`external-cloud-controller`. Core layer complete.

Verified NON-tags (do not create): `kubelet`, `remove-node`, `upgrade` are not
standalone role tags (`upgrade` is split into pre/system/post-upgrade;
`remove-node` is a playbook); `bootstrap-os` is not exposed as a run-tag in
v2.29.0–v2.31.0. Minor remaining tags if needed: `calico_rr`, `win_nodes`,
`kubelet-csr-approver`, and the granular `preinstall`/task-level tags.

## Troubleshooting

- migrate the 34 confirmed troubleshooting entries from the 0.1.0 raw cache
  (`knowledge-base/troubleshooting/`) into KDS `troubleshooting` documents, one at
  a time, re-verified against the tag.

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
  component (affected/fixed versions, severity, mitigation).
- Upstream Kubernetes (category 2, direct) — KEPs, feature gates, API
  deprecations/removals from kubernetes/kubernetes (not via Kubespray).
- Engineering experience (category 5) — CNCF / KubeCon / engineering blogs /
  postmortems.
- GitHub Issues / merged PRs (the troubleshooting layer).

## Possible architecture refinements (only if justified by implementation)

- formalize the D-005 "version envelope in frontmatter, precise per-version facts
  in the body" convention as an addendum in `standards/decisions.md`
  (currently applied consistently but not written down).
