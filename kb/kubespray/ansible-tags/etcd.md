---
id: TAG-ETCD
type: ansible_tag
title: etcd (Ansible run-tag)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: 2026-07-16
confidence: confirmed
aliases:
  - etcd
  - --tags etcd
tags:
  - ansible-tag
  - etcd
sources:
  - type: code
    path: playbooks/install_etcd.yml
    lines: "15,24-26"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/install_etcd.yml
    note: "role: etcd tagged etcd; group_by on kube_node tagged etcd; when etcd_deployment_type != kubeadm"
  - type: code
    path: playbooks/scale.yml
    lines: "35"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/scale.yml
    note: "role: etcd tagged etcd"
  - type: code
    path: roles/etcd/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/etcd/tasks/main.yml
    note: "the etcd role body; cert tasks additionally carry etcd-secrets"
relations:
  - type: see_also
    target: COMPONENT-ETCD
  - type: see_also
    target: TAG-ETCD_SECRETS
  - type: see_also
    target: VARIABLE-ETCD_DEPLOYMENT_TYPE
---

# etcd (Ansible run-tag)

## Summary

`etcd` is the run-tag that deploys and configures the etcd cluster: it runs the
whole `etcd` role — certificate generation, binary/image download, systemd (or
container) setup, and cluster health checks. `etcd-secrets` (see
[[TAG-ETCD_SECRETS]]) is a **subset** of `etcd`: the cert tasks carry both tags,
so `--tags etcd` also (re)generates certificates, while `--tags etcd-secrets`
runs only the certificate step.

## Context

- **Playbooks:** `cluster.yml` (through `playbooks/install_etcd.yml`) and
  `scale.yml`.
- **Affected host groups:** `etcd` and `kube_control_plane` (server/peer members),
  plus `kube_node` hosts that need etcd **client** certificates when the CNI
  requires etcd (`flannel`, `canal`, `cilium`, or `calico` with
  `calico_datastore: etcd`).
- **Condition:** the etcd role play runs only when
  `etcd_deployment_type != "kubeadm"` (for kubeadm-managed etcd it is skipped —
  see [[VARIABLE-ETCD_DEPLOYMENT_TYPE]]).

## Implementation

The tag is applied at the play/role level, so it is added to every task in the
`etcd` role:

```yaml
# playbooks/install_etcd.yml
- hosts: etcd:kube_control_plane:_kubespray_needs_etcd
  roles:
    - role: etcd
      tags: etcd
      when: etcd_deployment_type != "kubeadm"
```

A first play (`hosts: kube_node`, also tagged `etcd`) uses `group_by` to add
worker nodes to the `_kubespray_needs_etcd` group when their CNI needs etcd
client certs. `scale.yml` applies the `etcd` tag the same way.

Because the role is tagged as a whole, the etcd role's certificate tasks
(`check_certs.yml`, `gen_certs_script.yml`, `upd_ca_trust.yml`) run under both
`etcd` and `etcd-secrets`. Deploy the component with [[COMPONENT-ETCD]].

## Compatibility

- Kubespray `v2.29.0`–`v2.31.0`: the `etcd` tag deploys the etcd role via
  `install_etcd.yml`/`scale.yml`, gated on `etcd_deployment_type != "kubeadm"`.
- **Standalone-run safety: risky.** Requires gathered facts and downloaded
  binaries/images; re-running reconfigures etcd and, on certificate or config
  change, restarts etcd. Safe for convergence, but not a no-op.

## References

- `playbooks/install_etcd.yml:15,24-26` — `etcd` tag on the etcd role and the
  worker group_by.
- `playbooks/scale.yml:35` — `etcd` tag on scale.
- `roles/etcd/tasks/main.yml` — role body; cert tasks also tagged `etcd-secrets`.
- Verified on tags v2.29.0 `9991412`, v2.29.1 `0c6a295`, v2.30.0 `f4ccdb5`,
  v2.31.0 `1c9add4`.
