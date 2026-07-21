---
id: PRACTICE-RUNBOOK_INGRESS_NGINX_DETACH
type: best_practice
title: "Runbook: take ingress-nginx off Kubespray before v2.31.0"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: "1.13.3"
verified_at: "2026-07-21"
confidence: verified
aliases:
  - ingress-nginx removed in v2.31.0 what to do
  - migrate ingress-nginx to helm kubespray
  - ingress_nginx_enabled no longer works
  - self-manage ingress controller kubespray
  - ingress nginx orphaned after upgrade
tags:
  - runbook
  - operations
  - ingress
  - upgrade
sources:
  - type: code
    path: roles/kubernetes-apps/ingress_controller/ingress_nginx/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubernetes-apps/ingress_controller/ingress_nginx/tasks/main.yml
    note: "the exact object list Kubespray applies (namespace, cm, sa, (cluster)role(binding), ingressclass, DaemonSet, svc, optional admission webhook)"
  - type: code
    path: roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubernetes-apps/ingress_controller/ingress_nginx/defaults/main.yml
    note: "namespace ingress-nginx, service_type LoadBalancer, class nginx, ingress_nginx_default false, ingress_nginx_webhook_enabled false"
  - type: code
    path: roles/kubernetes-apps/ingress_controller/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ingress_controller/meta/main.yml
    note: "at v2.31.0 the ingress_controller role depends only on cert_manager and alb_ingress_controller — the nginx sub-role is gone from the tree"
relations:
  - type: part_of
    target: CONCEPT-RUNBOOKS_INDEX
  - type: depends_on
    target: COMPONENT-INGRESS_NGINX
  - type: see_also
    target: UPGRADE-V2_30_0__V2_31_0
  - type: see_also
    target: TROUBLE-CILIUM_HELM_OWNERSHIP_ADOPT
  - type: see_also
    target: TROUBLE-INGRESS_NGINX_ANNOTATION_REJECTED
  - type: see_also
    target: PRACTICE-UPGRADE_PREFLIGHT
---

# Runbook: take ingress-nginx off Kubespray before v2.31.0

## Summary

Kubespray managed ingress-nginx through `v2.30.0` and **deleted the role outright in `v2.31.0`**
(upstream PR #12767, "Deprecate Ingress-Nginx from kubernetes-apps" — one commit, no deprecation
release in between). Nothing in `v2.31.0` removes what is already deployed and nothing warns you:
`ingress_nginx_enabled: true` simply stops meaning anything. Your ingress controller keeps serving
traffic while becoming **unmanaged** — no re-render, no image bump, no CVE patching. Do the
hand-over deliberately, before the upgrade.

## Context

- **Managed range:** `v2.29.0`–`v2.30.0`, controller `1.13.3` ([[COMPONENT-INGRESS_NGINX]]).
  **Gone:** `v2.31.0` — role directory, `ingress_nginx_enabled`, `ingress_nginx_version`, the
  download entry and the docs page all removed in one commit.
- **What Kubespray created** (`…/ingress_nginx/tasks/main.yml`, `defaults/main.yml`@v2.30.0), all
  applied with the `kube` module at `state: latest` on `kube_control_plane[0]`:
  namespace `ingress-nginx`; ConfigMaps `ingress-nginx`, `tcp-services`, `udp-services`;
  ServiceAccount, Role/RoleBinding, ClusterRole/ClusterRoleBinding; **IngressClass `nginx`**
  (`ingress_nginx_class`, `ingress_nginx_default: false`); a **DaemonSet**
  `ingress-nginx-controller`; the Service (`ingress_nginx_service_type: LoadBalancer` by default);
  and — only if `ingress_nginx_webhook_enabled: true`, which is **`false` by default** — the
  admission webhook objects.
- **Two shape mismatches with the upstream Helm chart** make this more than `helm install`:
  Kubespray runs the controller as a **DaemonSet** while the chart defaults to a **Deployment**, and
  Kubespray leaves the **admission webhook off** while the chart enables it. Both differences change
  behaviour on the day you switch, not later.
- **`ingress_nginx_without_class: true`** in Kubespray means the controller also serves Ingresses
  that carry no class — a chart install with default settings does not, so unlabelled Ingresses can
  go dark.
- Applies whether or not you have already upgraded: after `v2.31.0` the same objects are simply
  orphaned, so the procedure is the same, only without the safety net of being able to re-render.

## Implementation

**Step 0 — Freeze and capture.** Snapshot etcd ([[PRACTICE-RUNBOOK_ETCD_BACKUP]]) and export what is
running, because this is your only record of the rendered configuration once the role is gone:

```bash
kubectl -n ingress-nginx get all,cm,sa,ingressclass,validatingwebhookconfiguration -o yaml \
  > ingress-nginx-asdeployed.yaml
kubectl get ingressclass nginx -o yaml
kubectl get ingress -A -o custom-columns='NS:.metadata.namespace,NAME:.metadata.name,CLASS:.spec.ingressClassName'
```

The last command matters: every Ingress with an **empty** class column depends on
`ingress_nginx_without_class` and needs an explicit `ingressClassName: nginx` before you switch.

**Step 1 — Decide the target** while still on `v2.30.0`: the upstream ingress-nginx Helm chart
(most common), a different controller, or a Gateway API implementation. Pin the chart version whose
`controller.image.tag` matches or exceeds `1.13.3` so the hand-over is not also a version jump.

**Step 2 — Label the Ingresses** that relied on class-less matching:

```bash
kubectl -n <ns> patch ingress <name> --type=merge -p '{"spec":{"ingressClassName":"nginx"}}'
```

Do this first and verify traffic is unaffected — it is reversible and independent of the migration.

**Step 3 — Stop Kubespray from re-applying.** Set `ingress_nginx_enabled: false` in inventory. Note
this **does not delete** anything: the role only ever applies, it has no removal path
([[CONCEPT-DESTRUCTIVE_ACTIONS]] — ingress-nginx is not in the delete inventory). The objects stay,
now inert.

**Step 4 — Hand the objects over.** Either

- **adopt** the existing objects into a Helm release — every adopted object needs
  `app.kubernetes.io/managed-by: Helm` plus the `meta.helm.sh/release-name` and
  `meta.helm.sh/release-namespace` annotations, or the install fails with an ownership error (same
  failure mode as [[TROUBLE-CILIUM_HELM_OWNERSHIP_ADOPT]]); the DaemonSet cannot be adopted into a
  chart that renders a Deployment — delete it as part of the cut-over; or
- **install alongside** with a second IngressClass and a second Service address, move DNS/LB
  targets over, then remove the Kubespray-era objects. Slower, but each step is reversible.

**Step 5 — Cut over and verify:** the new controller pods are ready on every node that needs them,
`kubectl get ingressclass` shows exactly the classes you intend, an end-to-end HTTP **and** HTTPS
request through each hostname succeeds, and the LoadBalancer/NodePort address serving your DNS is
the one you expect. If the chart enabled the admission webhook, re-apply one existing Ingress of
each shape — the webhook validates on write and rejects annotations the old, webhook-less setup
accepted ([[TROUBLE-INGRESS_NGINX_ANNOTATION_REJECTED]]).

**Step 6 — Only then upgrade** to `v2.31.0` ([[UPGRADE-V2_30_0__V2_31_0]],
[[PRACTICE-UPGRADE_PREFLIGHT]]), and remove `ingress_nginx_*` variables from inventory so nothing
suggests they still do something.

**Rollback.** Before Step 4 everything is reversible: set `ingress_nginx_enabled: true` and re-run
`cluster.yml --tags ingress-controller` (AWX: job tag `ingress-controller`) to re-render the
Kubespray objects — **but only while still on `v2.30.0` or older**. After the cut-over, or after the
upgrade to `v2.31.0`, that path no longer exists and rollback means re-applying your Step 0 export
by hand. That asymmetry is the reason to do this before the Kubespray upgrade, not after.

## References

- Removal: upstream PR #12767 (`cleanup: Deprecate Ingress-Nginx from kubernetes-apps`), tree state
  verified at `v2.31.0` (`roles/kubernetes-apps/ingress_controller/` contains only
  `alb_ingress_controller`, `cert_manager`, `meta`; `docs/ingress/ingress_nginx.md` gone;
  `ingress_nginx_enabled` survives only in `tests/files/ubuntu24-flannel-ha-once.yml`).
  Object list and defaults read at `v2.30.0`. Component: [[COMPONENT-INGRESS_NGINX]]; index:
  [[CONCEPT-RUNBOOKS_INDEX]].
