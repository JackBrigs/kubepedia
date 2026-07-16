---
id: PRACTICE-KUBEADM_JOIN_FAILURES
type: best_practice
title: kubeadm join / control-plane bring-up failures
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - kubeadm join failed
  - node not joining
  - control-plane not coming up
tags:
  - operations
  - kubeadm
  - diagnostics
sources:
  - type: code
    path: roles/kubernetes/kubeadm/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/kubeadm/tasks/main.yml
    note: "node kubeadm bootstrap; control-plane role runs kubeadm init/join"
relations:
  - type: see_also
    target: TAG-KUBEADM
  - type: see_also
    target: TAG-CONTROL_PLANE
  - type: see_also
    target: PRACTICE-CERTIFICATE_EXPIRY
---

# kubeadm join / control-plane bring-up failures

## Summary

Kubespray drives the control plane with the `control-plane` role
([[TAG-CONTROL_PLANE]]) and joins nodes with the `kubeadm` role
([[TAG-KUBEADM]]). Failures show up as the playbook hanging or erroring on
"Joining … kubeadm", or the API server never coming up. This runbook localizes
the cause.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`. The generated kubeadm config is
  `v1beta4` ([[CONFIG-KUBEADM_CONFIG_API_VERSION]]).

## Diagnostics

On the affected node (SSH):

```bash
journalctl -u kubelet -n 100 --no-pager        # kubelet drives the bootstrap
crictl ps -a | grep -E 'apiserver|etcd'        # static pods created?
ls -l /etc/kubernetes/manifests/               # static-pod manifests present?
cat /etc/kubernetes/kubeadm-config.yaml | head # rendered config sane?
```

From a working control-plane node:

```bash
kubectl get nodes                              # did the node partially join?
kubectl -n kube-system get pods -o wide | grep <node>
```

## Implementation

Common Kubespray-specific causes → action:
- **First `kubeadm init` failed, retry loops** — leftovers from the first attempt;
  fixed by newer retry handling (see the `kubeadm-init-retry` troubleshooting
  entry). Workaround: `kubeadm reset` on that node, then re-run.
- **etcd not reachable** — control-plane join needs a healthy etcd
  ([[PRACTICE-ETCD_BACKUP_RESTORE]]); check the `etcd` group first.
- **Expired/invalid certs or bootstrap token** — see
  [[PRACTICE-CERTIFICATE_EXPIRY]]; bootstrap tokens are time-limited.
- **API endpoint unreachable** — the node LB / `apiserver_loadbalancer_domain_name`
  must resolve (see the `apiserver-lb-domain-default` troubleshooting entry);
  firewall on `kube_apiserver_port` (6443).
- **`kube_override_hostname` set** — can break delegation (see the
  `control-plane-override-hostname-delegation` entry).
- **Clock skew** — TLS/bootstrap fails; check `timedatectl`.

## References

- `roles/kubernetes/kubeadm/tasks/main.yml`,
  `roles/kubernetes/control-plane/tasks/`; standard kubeadm.
