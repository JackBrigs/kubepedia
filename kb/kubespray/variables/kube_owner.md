---
id: VARIABLE-KUBE_OWNER
type: variable
title: kube_owner
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-21"
confidence: verified
aliases:
  - kube_owner
  - kube_owner root or kube
  - opt/cni/bin owner
  - cni directory ownership kubespray
  - cilium needs kube_owner root
tags:
  - security
  - permissions
  - cni
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "Defines kube_owner default kube (system user owning Kubernetes files)"
  - type: code
    path: roles/kubernetes/preinstall/tasks/0050-create_directories.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/preinstall/tasks/0050-create_directories.yml
    note: "'Create cni directories' (L68-86) creates /etc/cni/net.d and /opt/cni/bin with owner: {{ kube_owner }}, mode 0755"
  - type: docs
    path: docs/CNI/cilium.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/CNI/cilium.md
    note: "'Unprivileged agent configuration': Cilium requires kube_owner: root — this section exists only from v2.30.0"
  - type: code
    path: roles/network_plugin/calico/templates/calico-node.yml.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/calico/templates/calico-node.yml.j2
    note: "install-cni / upgrade-ipam run privileged: true — evidence Calico is unaffected by a kube-owned bin dir"
  - type: code
    path: roles/network_plugin/flannel/templates/cni-flannel.yml.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/flannel/templates/cni-flannel.yml.j2
    note: "install-cni-plugin / install-cni declare NO securityContext — they rely on the runtime default capability set"
relations:
  - type: see_also
    target: TROUBLE-CILIUM_MOUNT_CGROUP_DENIED
  - type: see_also
    target: VARIABLE-CNI_BIN_OWNER
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: PRACTICE-CLUSTER_HARDENING
---

# kube_owner

## Summary
Name of the system user that owns Kubernetes configuration and certificate files and directories on the nodes. Default is `kube`. The `adduser` role creates this user, and other roles use it for file ownership.

## Implementation
Defined with the same value `kube` in several places (all unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0):

```yaml
kube_owner: kube
```

- `roles/kubespray_defaults/defaults/main/main.yml`
- `roles/adduser/defaults/main.yml`
- `roles/kubernetes/preinstall/defaults/main.yml`

It is also exposed (uncommented, same value) in `inventory/sample/group_vars/k8s_cluster/k8s-cluster.yml`.

Beyond certificates and config, `kube_owner` also owns the **host CNI directories**:
`roles/kubernetes/preinstall/tasks/0050-create_directories.yml` ("Create cni directories",
L68-86) creates `/etc/cni/net.d` and `/opt/cni/bin` with `owner: {{ kube_owner }}`, mode
`0755`, whenever `kube_network_plugin` is one of `calico`, `flannel`, `cilium`, `kube-ovn`,
`kube-router`, `macvlan`. That is the coupling behind the hazard below.

## Known Issues

**The default `kube` breaks stock Cilium.** Cilium's `mount-cgroup` init container runs as
uid 0 but, since Cilium v1.12, with a reduced capability set that drops `CAP_DAC_OVERRIDE`.
Against a `kube`-owned `0755` `/opt/cni/bin` it is a plain non-owner, so its `cp` fails with
`Permission denied` and the agent never starts — full write-up and fixes in
[[TROUBLE-CILIUM_MOUNT_CGROUP_DENIED]]. Kubespray's own Cilium CI files
(`tests/files/debian12-cilium.yml`, `debian13-cilium.yml`, `rockylinux9/10-cilium.yml`,
`ubuntu24-cilium-sep.yml`, `debian12-cilium-svc-proxy.yml`) and the hardening guide
(`docs/operations/hardening.md`) all pin `kube_owner: root`, so the shipped default is never
exercised with Cilium.

**Upstream only documents this from v2.30.0.** `docs/CNI/cilium.md` gained the
"Unprivileged agent configuration" section (`kube_owner: root` required) in **v2.30.0**,
together with the note above `kube_owner: kube` in the sample inventory. On **v2.27.0–v2.29.1
there is no warning anywhere in the tree** — a cluster built on those tags with Cilium hits
the failure with nothing pointing at the cause.

**For the CNI bin dir there is a narrower lever.** `/opt/cni/bin` is re-created later in the
run by `roles/network_plugin/cni` with `owner: {{ cni_bin_owner }}` (default
`{{ kube_owner }}`), so [[VARIABLE-CNI_BIN_OWNER]] overrides the ownership of that one
directory without touching anything else — prefer it over `kube_owner: root` when the only
problem is the CNI bin dir.

**Changing `kube_owner` is cluster-wide, not per-node.** It re-owns Kubernetes config,
certificate and CNI paths on every node in `k8s_cluster`, so it must be set in inventory and
rolled out with a full `cluster.yml` run — a one-node `chown` is reverted by the next
preinstall run.

**Neighbouring CNI plugins on a `kube`-owned `/opt/cni/bin`** (from the DaemonSet templates
at v2.31.0 — same shape at v2.29.0):

| CNI | Container writing to the host bin dir | securityContext | Effect |
|-----|--------------------------------------|-----------------|--------|
| Calico | `upgrade-ipam`, `install-cni` | `privileged: true` | unaffected |
| kube-ovn | `install-cni` | `runAsUser: 0`, `privileged: true` | unaffected |
| Multus | `install-multus-binary` | `privileged: true` | unaffected |
| kube-router | main container (writes cni-conf-dir only) | `privileged: true` | unaffected |
| Flannel | `install-cni-plugin`, `install-cni` | **none declared** | works on the runtime default capability set (which includes `CAP_DAC_OVERRIDE`), but fails the same way if a policy drops that capability or forces `runAsNonRoot` |
| Cilium | `mount-cgroup` | uid 0, reduced caps, no `CAP_DAC_OVERRIDE` | **fails** |

So Cilium is the only plugin that breaks on the shipped default, and Flannel is the only
fragile neighbour — its init containers inherit privileges rather than declaring them.

## Compatibility
Kubespray v2.29.0 through v2.31.0. Related variables: `kube_cert_group`, `kube_config_dir`. Consumed by the `adduser` role to create the user.

## References
- roles/kubespray_defaults/defaults/main/main.yml
- roles/adduser/defaults/main.yml
- roles/kubernetes/preinstall/defaults/main.yml
- CNI dir ownership: roles/kubernetes/preinstall/tasks/0050-create_directories.yml (L68-86).
- Upstream requirement (v2.30.0+): docs/CNI/cilium.md "Unprivileged agent configuration";
  CI pins: tests/files/*cilium*.yml, docs/operations/hardening.md.
- Failure mode and fixes: [[TROUBLE-CILIUM_MOUNT_CGROUP_DENIED]]; CNI: [[COMPONENT-CILIUM]];
  hardening: [[PRACTICE-CLUSTER_HARDENING]].
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
