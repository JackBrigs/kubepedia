---
id: CONCEPT-DESTRUCTIVE_ACTIONS
type: concept
title: "What Kubespray deletes on an ordinary run (destructive actions inventory)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-21"
confidence: verified
aliases:
  - what does kubespray delete
  - kubespray deletes namespace
  - destructive tasks kubespray
  - does cluster.yml remove anything
  - kubespray removed my podman
  - kube-proxy pods force deleted
tags:
  - kubespray
  - operations
  - safety
  - upgrade
sources:
  - type: code
    path: roles/kubernetes-apps/ingress_controller/cert_manager/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/ingress_controller/cert_manager/tasks/main.yml
    note: "'Cert Manager | Remove legacy namespace' runs 'kubectl delete namespace {{ cert_manager_namespace }}' with ignore_errors, tags: upgrade"
  - type: code
    path: roles/kubernetes/kubeadm/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/kubeadm/tasks/main.yml
    note: "'Restart all kube-proxy pods…' = kubectl delete pod -n kube-system -l k8s-app=kube-proxy --force --grace-period=0, run_once, when the kubeadm configmap resource version changed"
  - type: code
    path: roles/kubernetes/control-plane/tasks/pre-upgrade.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/tasks/pre-upgrade.yml
    note: "if etcd_secret_changed: deletes the three control-plane static-pod manifests, then force-removes the containers"
  - type: code
    path: roles/container-engine/docker/tasks/pre-upgrade.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/docker/tasks/pre-upgrade.yml
    note: "on RedHat with docker-ce: removes podman_remove_packages_yum and docker_remove_packages_yum; on Debian docker_remove_packages_apt"
  - type: code
    path: roles/container-engine/runc/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/runc/tasks/main.yml
    note: "removes the distro runc package and the orphaned /usr/bin/runc (skipped on ostree/Flatcar)"
  - type: code
    path: roles/kubernetes-apps/metallb/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes-apps/metallb/tasks/main.yml
    note: "deletes the legacy 'config' ConfigMap in metallb_namespace (state: absent)"
  - type: code
    path: roles/kubernetes/node/tasks/loadbalancer/nginx-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/tasks/loadbalancer/nginx-proxy.yml
    note: "each localhost-LB variant removes the other's static-pod manifest (haproxy.yml / nginx-proxy.yml)"
relations:
  - type: see_also
    target: PRACTICE-CERT_MANAGER_SETUP
  - type: see_also
    target: PRACTICE-ANSIBLE
  - type: see_also
    target: PRACTICE-UPGRADE_PREFLIGHT
  - type: see_also
    target: CONCEPT-ESCAPE_HATCHES
---

# What Kubespray deletes on an ordinary run (destructive actions inventory)

## Summary

`cluster.yml` is a converge, and converging sometimes means **deleting**. Several roles
remove cluster objects, host packages or manifests as a normal part of their work — not only
`reset.yml`. Most are harmless cleanups; two can destroy state you care about. This is the
inventory, verified against the tagged source, so the surprise happens here rather than in
production.

## Context

- Verified at Kubespray `v2.31.0`; the same tasks exist through `v2.29.0`–`v2.31.0` unless
  noted.
- Scope: the **normal** playbooks (`cluster.yml`, `upgrade-cluster.yml`), not `reset.yml`,
  `remove-node.yml` or `recover-control-plane.yml` — those are destructive by contract and
  have their own runbooks.
- A default Ansible run selects **all** tags. Tasks tagged `upgrade` are therefore *not*
  opt-in: they execute unless you actively `--skip-tags upgrade`.

| What is deleted | Where | When | Blast radius |
|---|---|---|---|
| **The whole `cert-manager` namespace** (`kubectl delete namespace`, `ignore_errors`) | `kubernetes-apps/ingress_controller/cert_manager` | every run with `cert_manager_enabled: true` (tag `upgrade`) | **High** — Issuers, Certificates, CertificateRequests and the `ca-key-pair` Secret go with it ([[PRACTICE-CERT_MANAGER_SETUP]]) |
| **All `kube-proxy` pods, force-deleted at once** (`--force --grace-period=0`, `run_once`) | `kubernetes/kubeadm` | only when the kubeadm ConfigMap's resourceVersion changed and the apiserver endpoint/LB condition matches | **Medium** — every node's service proxy restarts simultaneously, brief cluster-wide gap in Service routing |
| The three control-plane **static-pod manifests**, then the containers force-removed | `kubernetes/control-plane` (`pre-upgrade.yml`) | only when `etcd_secret_changed` | **Medium** — API plane restarts on that node |
| The **`config` ConfigMap** in the MetalLB namespace | `kubernetes-apps/metallb` | every run with MetalLB enabled | Low — legacy layer2/3 config; current config lives in CRs |
| The **distro `runc` package** and an orphaned `/usr/bin/runc` | `container-engine/runc` | every run (skipped on ostree / Flatcar) | Low–Medium — anything outside Kubernetes relying on the distro runc loses it |
| **podman** and old Docker packages (RedHat), old Docker packages (Debian) | `container-engine/docker` (`pre-upgrade.yml`) | when `container_manager: docker` with a `docker-ce` version | **Medium** — podman is uninstalled from the host without asking |
| The *other* localhost-LB's static-pod manifest (`haproxy.yml` ↔ `nginx-proxy.yml`) | `kubernetes/node` (`loadbalancer/*`) | every run | Low — intended switch-over cleanup |
| The CNI conflist of the plugin's own handler (`10-calico.conflist`, `10-kuberouter.conf`) | `network_plugin/calico`, `network_plugin/kube-router` | on config change (handler) | Low — recreated immediately |
| Add-on staging dirs under `{{ kube_config_dir }}/addons/…` | `metrics_server`, `cert_manager` | tag `upgrade` | None — host-side scratch only |

## Known Issues

- **cert-manager is the one to plan around.** It is the only entry here that deletes a
  namespace, and namespaces take their contents with them. If cert-manager holds your CA key
  pair or hand-made Issuers, back them up (or keep them in Git) before any run that includes
  this role, and consider `--skip-tags upgrade` for that run.
- **The kube-proxy delete is not a rolling restart.** It is a single `kubectl delete pod -l
  k8s-app=kube-proxy --force --grace-period=0` from one control-plane node, so every node's
  kube-proxy goes away at the same moment and comes back as the DaemonSet recreates it.
  Expect a short, cluster-wide window where Service/NodePort routing is being reprogrammed.
  Clusters running Cilium with kube-proxy replacement do not have these pods at all.
- **Host package removals surprise mixed-use nodes.** `podman` on RHEL-family hosts and the
  distro `runc` are removed to keep the container stack consistent; if operators use podman
  on those nodes for anything else, that breaks on the next run, not at install time.
- **`--skip-tags upgrade` is a blunt instrument.** It suppresses these cleanups but also
  suppresses genuine upgrade steps in other roles — use it deliberately, for a single run,
  not as a standing setting ([[PRACTICE-ANSIBLE]]).

## References

- Verified at tag `v2.31.0`:
  `roles/kubernetes-apps/ingress_controller/cert_manager/tasks/main.yml`,
  `roles/kubernetes/kubeadm/tasks/main.yml`,
  `roles/kubernetes/control-plane/tasks/pre-upgrade.yml`,
  `roles/container-engine/{docker/tasks/pre-upgrade.yml,runc/tasks/main.yml}`,
  `roles/kubernetes-apps/metallb/tasks/main.yml`,
  `roles/kubernetes/node/tasks/loadbalancer/{haproxy,nginx-proxy}.yml`,
  `roles/network_plugin/{calico/handlers,kube-router/tasks}/main.yml`,
  `roles/kubernetes-apps/metrics_server/tasks/main.yml`.
- Related: [[PRACTICE-CERT_MANAGER_SETUP]], [[PRACTICE-UPGRADE_PREFLIGHT]],
  [[PRACTICE-ANSIBLE]], [[CONCEPT-ESCAPE_HATCHES]].
