---
id: PRACTICE-RUNBOOK_CILIUM_1_15_TO_1_18
type: best_practice
title: "Runbook: upgrade Cilium 1.15.9 → 1.18.4 with Kubespray (consecutive-minor path)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=1.15.9 <=1.18.4"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - cilium upgrade 1.15.9 to 1.18.4 kubespray
  - how to upgrade cilium kubespray step by step
  - cilium consecutive minor upgrade path
  - cilium_version override intermediate 1.16 1.17
  - cilium preflight upgrade runbook
tags:
  - runbook
  - cilium
  - cni
  - upgrade
  - operations
sources:
  - type: docs
    path: Documentation/operations/upgrade.rst
    url: https://github.com/cilium/cilium/blob/v1.18.4/Documentation/operations/upgrade.rst
    note: "Cilium supports upgrades only between consecutive minor releases; pre-flight DaemonSet; per-minor breaking notes"
  - type: code
    path: roles/network_plugin/cilium
    url: https://github.com/kubernetes-sigs/kubespray/tree/v2.29.0/roles/network_plugin/cilium
    note: "Kubespray deploys Cilium at cilium_version; override it to stage intermediate minors"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: depends_on
    target: UPGRADE-CILIUM_1_15_TO_1_19
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: PRACTICE-KERNEL_REQUIREMENTS
  - type: see_also
    target: TROUBLE-CILIUM_KPR_TOGGLES_REMOVED
  - type: see_also
    target: TROUBLE-CILIUM_ENI_MASQUERADE_FLIP
  - type: see_also
    target: TROUBLE-CILIUM_SERVICEACCOUNT_IDENTITY_DROPS
  - type: see_also
    target: TROUBLE-CILIUM_IPSEC_HOST_ROUTING_CVE
---

# Runbook: upgrade Cilium 1.15.9 → 1.18.4 with Kubespray (consecutive-minor path)

## Summary

The **step-by-step** procedure to take Cilium from **1.15.9 to 1.18.4** on a Kubespray-managed
cluster. The one rule that shapes everything: **Cilium only supports upgrades between *consecutive*
minor releases** — you must go **1.15 → 1.16 → 1.17 → 1.18**, never skipping. Kubespray's default tag
progression **skips 1.16** (v2.27.0's 1.15.9 jumps straight to v2.28.0's 1.17.3), so this runbook
stages the missing minor by **overriding `cilium_version`** and converging with `cluster.yml` at each
hop. The *what-changes-at-each-minor* detail lives in the reference doc
([[UPGRADE-CILIUM_1_15_TO_1_19]]); this is the *how-to-run-it* procedure. `1.18.4` is a patch within
1.18 (Kubespray's own pins are 1.18.2/1.18.6), reached by pinning `cilium_version: "1.18.4"`.

## Context

- **Path (4 hops):** `1.15.9 → 1.16.z → 1.17.z → 1.18.4`. Use the **latest patch** of each intermediate
  minor (e.g. a recent `1.16.x`, then a recent `1.17.x`) so you carry that minor's fixes forward.
- **Kubespray angle (how it actually applies):** the `network_plugin/cilium` role runs the **`cilium`
  CLI** from the **first control-plane node** — `cilium install` (first time) or `cilium upgrade` (Helm
  under the hood) — with the rendered `cilium-values.yaml`. It applies **cluster-wide at once**, **not**
  node-by-node with drain. To stage an intermediate minor, set `cilium_version` in `group_vars` and
  re-converge; keep the cluster on its current Kubespray tag (you move only the CNI version).
- **⚠ DISRUPTIVE on prod — treat as a CNI reinstall, not a seamless rolling restart.** `cilium upgrade`
  rolls the **agent DaemonSet cluster-wide** (every node's agent restarts). Worse: if
  **`cilium_remove_old_resources: true`** (the manifest→Helm migration path, e.g. crossing into v2.29's
  install method), Kubespray **`kubectl delete`s the entire Cilium** — DaemonSet, `cilium-operator`,
  `cilium-config`, ClusterRole/Binding, ServiceAccounts, Hubble, secrets — and then **reinstalls** it.
  During that window the **CNI is torn down**: new pods get no networking and existing dataplane traffic
  can drop. **Expect real network downtime.** Schedule a proper maintenance window, and for critical
  workloads drain/relocate or roll zone-by-zone before each hop.
- **Pre-reqs before starting:**
  - **Kernel ≥ 5.10 on every node** — a **hard requirement from 1.18** ([[PRACTICE-KERNEL_REQUIREMENTS]]);
    verify now so the 1.17→1.18 hop doesn't strand nodes.
  - Confirm you're on **≥1.15.6** (you are, at 1.15.9) — required before the 1.16 `toFQDNs` overhaul.
  - Read the per-minor breaking actions in [[UPGRADE-CILIUM_1_15_TO_1_19]] and pre-stage the inventory
    changes each hop needs (below).

## Implementation

**Step 0 — Baseline health & backup.** Confirm Cilium is healthy and capture current config:

```bash
kubectl -n kube-system exec ds/cilium -- cilium status --brief
kubectl -n kube-system exec ds/cilium -- cilium status --verbose | sed -n '1,40p'
cilium connectivity test            # if the cilium CLI is installed; else skip
kubectl -n kube-system get cm cilium-config -o yaml > cilium-config.$(date +%F).bak.yaml
kubectl get crd | grep cilium       # note CRD versions (BGP/IPPool) for the migration hops
```

**Step 1 — Pre-flight for the NEXT minor (repeat each hop).** Cilium ships a pre-flight DaemonSet that
pre-pulls the target image and validates that existing `CiliumNetworkPolicy`/CRDs parse under the new
version — run it **before** each cutover and wait for it to be Ready:

```bash
# TARGET = the next hop's version, e.g. 1.16.z (then 1.17.z, then 1.18.4)
helm install cilium-preflight cilium/cilium --version <TARGET> \
  --namespace kube-system \
  --set preflight.enabled=true --set agent=false --set operator.enabled=false
kubectl -n kube-system rollout status ds/cilium-pre-flight-check
kubectl -n kube-system get ciliumnetworkpolicies -A     # confirm no validation errors were logged
helm uninstall cilium-preflight -n kube-system
```

**Step 2 — Hop 1.15.9 → 1.16.z.** Pre-stage the 1.16 breaking actions in `group_vars`, then converge.
Key ones ([[UPGRADE-CILIUM_1_15_TO_1_19]] has the full list): Envoy DaemonSet turns on by default;
`CiliumLoadBalancerIPPool.spec.cidrs` is **removed** → use `.blocks`; several policy-empty-selector
semantics flip to deny; a batch of flags/Helm keys are removed. Hold old defaults with
`upgradeCompatibility`:

```yaml
# inventory/<cluster>/group_vars/k8s_cluster/k8s-net-cilium.yml
cilium_version: "1.16.19"                 # latest 1.16 patch
# hold 1.15 defaults across the jump, then remove after validating:
cilium_extra_values:
  upgradeCompatibility: "1.15"      # -> Helm upgradeCompatibility=1.15
```

```bash
ansible-playbook -i inventory/<cluster>/hosts.yaml kubespray/cluster.yml -b --tags=cilium
# (or a full cluster.yml run if your workflow requires it)
kubectl -n kube-system rollout status ds/cilium
kubectl -n kube-system exec ds/cilium -- cilium status --brief
cilium connectivity test        # validate before the next hop
```

**Step 3 — Hop 1.16.z → 1.17.z.** Pre-stage 1.17 actions: **Consul / Cilium-managed etcd / `metallb-bgp`
removed** (move BGP to Cilium's BGP control plane), service protocol-differentiation on by default,
IPsec single-key removed. Then:

```yaml
cilium_version: "1.17.6"                  # latest 1.17 patch
cilium_extra_values:
  upgradeCompatibility: "1.16"
```

Re-run the Step 1 pre-flight (TARGET=1.17.z), converge as in Step 2, validate.

**Step 4 — Hop 1.17.z → 1.18.4 (the target).** This hop has the **hard requirements** — do the
pre-checks first:

- **Kernel ≥ 5.10** on all nodes ([[PRACTICE-KERNEL_REQUIREMENTS]]) — a node below this will fail.
- **ENI masquerade default flips `true → false`** — if you run the ENI IPAM datapath, set
  `enableIPv4Masquerade` explicitly or you lose SNAT ([[TROUBLE-CILIUM_ENI_MASQUERADE_FLIP]]).
- **`serviceaccount` identity label** joins the default set → transient identity churn/drops during the
  hop; exclude it if you don't use it ([[TROUBLE-CILIUM_SERVICEACCOUNT_IDENTITY_DROPS]]).
- **BGP CRDs `v2alpha1 → v2`** — migrate BGP config before this hop if you use BGP.
- **KPR piecemeal toggles are deprecated** here (removed in 1.19) — if your inventory sets
  `--enable-node-port`/`-host-port`/`-external-ips`/session-affinity individually, migrate to a single
  `kube_proxy_replacement` now ([[TROUBLE-CILIUM_KPR_TOGGLES_REMOVED]]).
- **IPsec + KPR + BPF-masquerade:** eBPF host-routing auto-enables and needs a patched kernel
  (CVE-2025-37959) — patch the kernel or set `--enable-host-legacy-routing=true`
  ([[TROUBLE-CILIUM_IPSEC_HOST_ROUTING_CVE]]).

```yaml
cilium_version: "1.18.4"
cilium_extra_values:
  upgradeCompatibility: "1.17"      # remove once validated on 1.18.4
# set any of the above explicitly, e.g. for ENI:
# cilium_enable_ipv4_masquerade: true
```

Pre-flight (TARGET=1.18.4), converge, then validate thoroughly:

```bash
kubectl -n kube-system rollout status ds/cilium ds/cilium-envoy deploy/cilium-operator
kubectl -n kube-system exec ds/cilium -- cilium status --verbose
kubectl -n kube-system exec ds/cilium -- cilium-dbg status --all-health
cilium connectivity test
kubectl get ciliumendpoints -A | head        # identities stable, no mass drops
```

**Step 5 — Finalize.** Once 1.18.4 is validated and stable, **remove `upgradeCompatibility (cilium_extra_values)`**
(so you adopt 1.18 defaults) and re-converge; re-run `cilium connectivity test`. Update the inventory
comment noting you're intentionally pinning `cilium_version: 1.18.4` above Kubespray's tag default.

**Rollback.** Per hop, before removing `upgradeCompatibility`, a bad hop can be rolled back by
resetting `cilium_version` to the previous minor's patch and re-converging — but **once CRDs are
migrated (BGP v2, IPPool) or identities have churned, rollback is not clean**. Treat each hop's
validation gate as the go/no-go; keep the Step 0 `cilium-config` backup, and for a stuck agent use
[[COMPONENT-CILIUM]] / the Cilium troubleshooting docs before forcing anything.

## References

- Cilium `Documentation/operations/upgrade.rst`@v1.18.4 (consecutive-minor rule, pre-flight);
  Kubespray `network_plugin/cilium` role. Breaking-change reference per minor:
  [[UPGRADE-CILIUM_1_15_TO_1_19]]; component [[COMPONENT-CILIUM]]; kernel floor
  [[PRACTICE-KERNEL_REQUIREMENTS]]; KPR [[TROUBLE-CILIUM_KPR_TOGGLES_REMOVED]]; ENI masquerade
  [[TROUBLE-CILIUM_ENI_MASQUERADE_FLIP]]; identity churn
  [[TROUBLE-CILIUM_SERVICEACCOUNT_IDENTITY_DROPS]]; IPsec/host-routing CVE
  [[TROUBLE-CILIUM_IPSEC_HOST_ROUTING_CVE]]; index [[CONCEPT-RUNBOOKS_INDEX]].
