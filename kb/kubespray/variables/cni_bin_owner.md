---
id: VARIABLE-CNI_BIN_OWNER
type: variable
title: cni_bin_owner
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-21"
confidence: verified
aliases:
  - cni_bin_owner
  - opt/cni/bin owner variable
  - change cni bin dir ownership without kube_owner
  - narrow fix for cilium mount-cgroup permission denied
tags:
  - network-plugin
  - cni
  - variable
  - permissions
sources:
  - type: code
    path: roles/network_plugin/cni/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cni/defaults/main.yml
    note: "cni_bin_owner: {{ kube_owner }} — same definition at v2.27.0, v2.28.0, v2.29.0, v2.29.1, v2.30.0, v2.31.0"
  - type: code
    path: roles/network_plugin/cni/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cni/tasks/main.yml
    note: "'CNI | make sure /opt/cni/bin exists' (owner: cni_bin_owner, recurse: true) and 'CNI | Copy cni plugins' (same owner) — the only consumers"
  - type: code
    path: playbooks/cluster.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/playbooks/cluster.yml
    note: "kubernetes/preinstall runs in an earlier play than network_plugin — so cni_bin_owner is applied after (and wins over) the preinstall ownership"
relations:
  - type: see_also
    target: VARIABLE-KUBE_OWNER
  - type: see_also
    target: TROUBLE-CILIUM_MOUNT_CGROUP_DENIED
  - type: see_also
    target: PRACTICE-CNI_GENERIC_PLUGIN
---

# cni_bin_owner

## Summary

Owner applied to the host CNI binary directory `/opt/cni/bin` and to the plugin binaries
unpacked into it. Default `{{ kube_owner }}` — i.e. `kube`, not `root`. It is the **narrow**
lever on that directory's ownership: unlike [[VARIABLE-KUBE_OWNER]] it affects nothing else
in the cluster.

## Implementation

Defined once, with the same value at every tag in the indexed range (`v2.27.0`, `v2.28.0`,
`v2.29.0`, `v2.29.1`, `v2.30.0`, `v2.31.0`):

```yaml
# roles/network_plugin/cni/defaults/main.yml
cni_bin_owner: "{{ kube_owner }}"
```

Two tasks consume it (`roles/network_plugin/cni/tasks/main.yml`) — the whole role:

```yaml
- name: CNI | make sure /opt/cni/bin exists
  file: { path: /opt/cni/bin, state: directory, mode: "0755",
          owner: "{{ cni_bin_owner }}", recurse: true }
- name: CNI | Copy cni plugins
  unarchive: { src: "{{ downloads.cni.dest }}", dest: /opt/cni/bin,
               mode: "0755", owner: "{{ cni_bin_owner }}", remote_src: true }
```

`recurse: true` means the ownership is re-applied to **everything already inside** the
directory on each run, not just to the directory itself.

**Ordering matters and is in your favour.** `/opt/cni/bin` is created twice per run:
first by `roles/kubernetes/preinstall/tasks/0050-create_directories.yml` ("Create cni
directories", `owner: {{ kube_owner }}`), then by this role. In `playbooks/cluster.yml`
`kubernetes/preinstall` runs in an earlier play than `network_plugin`, so **`cni_bin_owner`
is the value that survives** for `/opt/cni/bin`. `/etc/cni/net.d` is not touched by this
role and keeps `kube_owner`.

The role runs for every `kube_network_plugin` except `none`
(`roles/network_plugin/tasks/main.yml`), so this applies to Cilium, Calico, Flannel,
kube-ovn, kube-router, macvlan and the bare `cni` value alike
([[PRACTICE-CNI_GENERIC_PLUGIN]]).

## Known Issues

**This is the least invasive durable fix for the Cilium `mount-cgroup` failure.** Cilium's
`mount-cgroup` init container runs as uid 0 without `CAP_DAC_OVERRIDE` and cannot write into
a `kube`-owned `/opt/cni/bin`, so the agent never starts
([[TROUBLE-CILIUM_MOUNT_CGROUP_DENIED]]). Setting

```yaml
cni_bin_owner: root
```

in inventory makes the directory root-owned on the next run and keeps it that way, while
leaving certificates, `kube_config_dir` and every other `kube_owner`-owned path untouched —
in contrast to `kube_owner: root`, which re-owns Kubernetes files across the whole cluster.
It is also durable where a manual `chown` is not: a later run re-applies it instead of
reverting it.

Caveats: it does **not** change `/etc/cni/net.d` (still `kube_owner`), and it is a
Kubespray-specific setting, so upstream Cilium documentation will not mention it. Kubespray's
own Cilium CI files use `kube_owner: root` rather than this variable, so the
`cni_bin_owner: root` combination is not what upstream exercises.

## Compatibility

Kubespray `v2.27.0`–`v2.31.0`, unchanged. Related: [[VARIABLE-KUBE_OWNER]] (its default
value), `kube_cert_group`.

## References

- `roles/network_plugin/cni/defaults/main.yml` and `tasks/main.yml`;
  `roles/network_plugin/tasks/main.yml` (included for every plugin except `none`);
  `roles/kubernetes/preinstall/tasks/0050-create_directories.yml` and `playbooks/cluster.yml`
  (why this value wins). Failure it fixes: [[TROUBLE-CILIUM_MOUNT_CGROUP_DENIED]].
