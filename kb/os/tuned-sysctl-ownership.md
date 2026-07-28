---
id: CONCEPT-TUNED_SYSCTL_OWNERSHIP
type: concept
title: "Who owns a sysctl on a Kubespray node — tuned, Kubespray, or kube-proxy"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-28"
confidence: verified
aliases:
  - sysctl ownership kubernetes node
  - who sets nf_conntrack_max
  - ip_local_reserved_ports kubespray
  - tuned vs kube-proxy sysctl
  - sysctl overwritten after ansible run
tags:
  - os
  - sysctl
  - tuned
  - kube-proxy
  - conntrack
  - nodes
sources:
  - type: code
    path: roles/kubernetes/node/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/tasks/main.yml
    note: "task 'Ensure nodePort range is reserved' writes net.ipv4.ip_local_reserved_ports = kube_apiserver_node_port_range into sysctl_file_path with reload"
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "kube_proxy_conntrack_max_per_core 32768, min 131072, tcp_close_wait 1h0m0s, tcp_established 24h0m0s"
  - type: code
    path: roles/kubernetes/node/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/defaults/main.yml
    note: "kube_apiserver_node_port_range 30000-32767; sysctl_file_path /etc/sysctl.d/99-sysctl.conf"
relations:
  - type: see_also
    target: CONCEPT-TUNED_UBUNTU
  - type: see_also
    target: TROUBLE-TUNED_VERIFY_FLAPS
  - type: see_also
    target: CONCEPT-KUBE_PROXY
---

# Who owns a sysctl on a Kubespray node — tuned, Kubespray, or kube-proxy

## Summary

Three independent systems write kernel parameters on a Kubespray-managed node, none of them aware of
the others. When two of them claim the same key, the effective value is decided by **who ran last**,
and it changes silently on ordinary events — a pod restart, an Ansible run, a reboot. This map says
which key belongs to whom, so a setting can be placed with its real owner instead of being fought
over.

## Context

**kube-proxy owns the conntrack limits.** Kubespray renders them into the kubeadm config from these
defaults (v2.31.0):

| Variable | Default | Effect |
|---|---|---|
| `kube_proxy_conntrack_max_per_core` | `32768` | `nf_conntrack_max` = value × CPU cores; `0` leaves the limit untouched |
| `kube_proxy_conntrack_min` | `131072` | floor for the computed value |
| `kube_proxy_conntrack_tcp_close_wait_timeout` | `1h0m0s` | `nf_conntrack_tcp_timeout_close_wait` |
| `kube_proxy_conntrack_tcp_established_timeout` | `24h0m0s` | `nf_conntrack_tcp_timeout_established` |

kube-proxy applies these **at pod start**, logging `"Setting nf_conntrack_max"`. On a 16-core node
the result is `32768 × 16 = 524288`. To hand the limit to someone else, set
`kube_proxy_conntrack_max_per_core: 0` — that is the documented opt-out, and it also disables the
`min` floor.

**Kubespray owns the reserved-port list.** `roles/kubernetes/node/tasks/main.yml`, task *Ensure
nodePort range is reserved*, writes

```
net.ipv4.ip_local_reserved_ports = {{ kube_apiserver_node_port_range }}   # default 30000-32767
```

into `sysctl_file_path` (`/etc/sysctl.d/99-sysctl.conf`) with `sysctl_set: true` and `reload: true`,
under the `kube-proxy` tag. The value cannot be extended with unrelated ports: the same variable
feeds the apiserver's `--service-node-port-range` in the kubeadm config and Calico's
`FELIX_KUBENODEPORTRANGES`, so widening it changes Service behaviour.

**The distribution owns its hardening defaults.** On Ubuntu, `kernel.yama.ptrace_scope` comes from a
procps-owned file — see [[CONCEPT-TUNED_UBUNTU]].

**Everything else is free for tuned**: network buffers, TCP timers and backlogs, `vm.*`, inotify
limits, `fs.nr_open`, the conntrack *timeouts* (Kubespray's kube-proxy values and a typical profile
agree at `86400` / `3600`, so they coexist), scheduler and I/O knobs.

**How the flip happens.** At boot `systemd-sysctl` runs before `tuned.service`, so tuned's value
survives. Afterwards the order reverses: a kube-proxy pod restart re-applies the conntrack limit, and
an Ansible run rewrites and reloads its sysctl file — both land after tuned and hold until the profile
is re-applied. Nothing logs a conflict; the only witness is `tuned-adm verify`, and only on its next
run ([[TROUBLE-TUNED_VERIFY_FLAPS]]).

**Deciding ownership.** For each key in a profile ask whether kube-proxy or Kubespray also writes it.
If yes, remove it from the profile and set it through that component's own variable — the value then
lives in inventory, under review, instead of being re-established by whichever process restarted
last.

## References

- `roles/kubernetes/node/tasks/main.yml`, `roles/kubernetes/node/defaults/main.yml`,
  `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml` — read at tag **v2.31.0**
  (verified 2026-07-28).
- OS side: [[CONCEPT-TUNED_UBUNTU]]; symptom: [[TROUBLE-TUNED_VERIFY_FLAPS]].
