# Kubepedia — Backlog

Deferred work items. This is a work-tracking file, not KDS knowledge; the base of
truth about what the KB *contains* is `kb/` + `index/`. Items here are agreed but
not yet implemented. Pull an item into a focused change when ready, then remove it.

## README (public-facing) — FUTURE VERSION (owner deferred 2026-07-17)

The repository has **no README** on purpose right now — the previous drafts were
rejected by the owner. A public README must be **designed separately** (agree the
audience, structure, and tone with the owner first) before re-adding it. Do not
re-create it ad hoc. Owner parked this to a **future version** (2026-07-17).

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

- **Community (category 6) — FUTURE VERSION (owner deferred 2026-07-17; recon + plan below done).**
  Reconnaissance done (GitHub issues/discuss.kubernetes, Habr ×3 + Habr Q&A, CNCF,
  kubernetes.io, cilium.io; note: Stack Overflow & Reddit are blocked to the crawler).
  Per `sources.md`, community is **never authoritative** — every candidate below must be
  **re-verified against code/docs (tag v2.31.0)** before entering the KB, `sources`
  marked "re-verified", lower confidence where inference is involved. Candidates the
  recon surfaced that are **not yet covered** (~14 docs/edits, 8 areas):
  - etcd: `TROUBLE-ETCD_SLOW_APPLY` (apply-took-too-long / disk I/O / defrag);
    note "etcd upgrade briefly stalls in-flight apiserver requests".
  - certs: `TROUBLE-CERT_DIR_SSL_NOT_PKI` (myth — Kubespray sets `certificatesDir=
    /etc/kubernetes/ssl`, already code-verified); `TROUBLE-CERT_100_YEARS_MYTH`
    (old non-kubeadm; now 1yr); enrich `CONCEPT-CLUSTER_PKI` (restart CP after renewal).
  - Cilium: `TROUBLE-CILIUM_PACKET_DROPS` (cilium-dbg monitor drops, identity/kvstore
    propagation, `CT: Map insertion failed` → conntrack `bpf-ct-global-*-max`).
  - runtime/registry: `TROUBLE-CRIO_SHORT_NAME_REGISTRY` (unqualified-search);
    enrich registry doc with insecure-registry (`skip_verify`).
  - networking: `CONFIG-CNI_MTU` (explicit overlay MTU); `TROUBLE-NODE_CANNOT_REACH_APISERVER`
    (localhost-LB / firewall / routing).
  - deploy: `TROUBLE-DEPLOY_HANGS_WAIT_APISERVER` (kubelet/static-pod not up).
  - control-plane: `TROUBLE-REMOVE_DEAD_CONTROL_PLANE_NODE` (offline master removal).
  - security/ops: `PRACTICE-RBAC_LEAST_PRIVILEGE` (no blanket cluster-admin; don't mix
    SSH+API security models); `PRACTICE-MONITORING_BASELINE` (what to watch; Prometheus
    not bundled by Kubespray).
  - Rejected as myths (→ debunk docs above): "copy CA into pki", "certs valid 100 years".
    Skipped: Calico probe-warnings (Calico deferred), external-LB 502 (niche).
- Security (category 4) — LARGELY DONE via the **osv.dev API** (curl POST works;
  authoritative, version-filtered → no fabrication). Per-component CVE matrices
  indexed for: kubernetes, runc, containerd, coredns, cilium, cni-plugins,
  cert-manager, helm; verified clean (0 CVE at shipped versions): etcd, kube-vip,
  metallb, nerdctl, node-feature-discovery. Method: query osv.dev per shipped
  version, record only returned (=affected) vulns. **Remaining:** re-run the
  osv.dev sweep whenever versions change or new CVEs land (it is date-sensitive);
  optionally cover the long tail of minor add-ons and per-K8s-patch versions.
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

DONE (round 2): per-component CVE matrices via osv.dev (security), and 8
verifiable **operational/community** troubleshooting scenarios (CoreDNS loop, etcd
db-space, conntrack full, VXLAN MTU, pod Terminating, pull rate-limit, clock skew,
DiskPressure). Total troubleshooting docs: 50.

**Still optional (return if wanted):**
- component release-note "Known Issues" (etcd/Cilium/containerd/CoreDNS) beyond
  CVEs — web-scraping is unreliable; do per-advisory or from cloned repos;
- deeper **Community** mining (Reddit / SO / Slack) with re-verification;
- curated Kubernetes "Known Issues" / "Urgent Upgrade Notes" per version.

## Node OS & disk encryption — FUTURE (owner requested 2026-07-17)

Add to the base:

- **Talos OS** — the immutable, API-managed Kubernetes OS. Scope note: Talos is **not a
  Kubespray-managed OS** (Kubespray targets traditional distros — Ubuntu/Debian/RHEL-family);
  so this is an adjacent-domain item like the OS layer (`kb/os/`), covering Talos ↔ Kubernetes
  (machine config, no SSH/systemd, immutable rootfs, upgrades, cgroup v2, how it differs from a
  Kubespray node OS). Version-bind to a Talos release when written.
- **Clevis + LUKS2** — automated LUKS2 volume unlock (network-bound disk encryption via Tang,
  or TPM2 binding) for node/data-disk encryption at rest. Cover: LUKS2 vs LUKS1, Clevis pins
  (tang/tpm2/sss), boot-time auto-unlock, relevance to Kubernetes nodes and to encrypted
  storage backends (e.g. Ceph OSD disks, local PVs). Node-OS-level, adjacent domain.

## Possible architecture refinements (only if justified by implementation)

- formalize the D-005 "version envelope in frontmatter, precise per-version facts
  in the body" convention as an addendum in `standards/decisions.md`
  (currently applied consistently but not written down).
