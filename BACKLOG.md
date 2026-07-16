# Kubepedia — Backlog

Deferred work items. This is a work-tracking file, not KDS knowledge; the base of
truth about what the KB *contains* is `kb/` + `index/`. Items here are agreed but
not yet implemented. Pull an item into a focused change when ready, then remove it.

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

## Troubleshooting

- migrate the 34 confirmed troubleshooting entries from the 0.1.0 raw cache
  (`knowledge-base/troubleshooting/`) into KDS `troubleshooting` documents, one at
  a time, re-verified against the tag.

## Possible architecture refinements (only if justified by implementation)

- formalize the D-005 "version envelope in frontmatter, precise per-version facts
  in the body" convention as an addendum in `standards/decisions.md`
  (currently applied consistently but not written down).
