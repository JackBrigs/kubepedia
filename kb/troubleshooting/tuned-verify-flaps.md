---
id: TROUBLE-TUNED_VERIFY_FLAPS
type: troubleshooting
title: "tuned-adm verify passes, then fails hours later with no change made (another owner rewrote the sysctl)"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-28"
confidence: verified
aliases:
  - tuned verify intermittent failure
  - nf_conntrack_max changed by itself
  - ip_local_reserved_ports reset after ansible
  - tuned settings reverted after kubespray run
  - tuned alert flapping
tags:
  - os
  - tuned
  - sysctl
  - conntrack
  - kube-proxy
  - monitoring
sources:
  - type: code
    path: roles/kubernetes/node/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/node/tasks/main.yml
    note: "'Ensure nodePort range is reserved' rewrites net.ipv4.ip_local_reserved_ports and reloads it"
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/kube-proxy.yml
    note: "conntrack maxPerCore/min applied by kube-proxy at pod start"
relations:
  - type: see_also
    target: CONCEPT-TUNED_SYSCTL_OWNERSHIP
  - type: see_also
    target: TROUBLE-TUNED_VERIFY_MISSING_SYSCTL
---

# tuned-adm verify passes, then fails hours later with no change made (another owner rewrote the sysctl)

## Summary

Verification is green, nobody touches the node, and hours or days later the same check fails — then
goes green again after someone re-applies the profile. The profile is fine. A **second owner** of the
same kernel parameter ran in between: kube-proxy on pod start, or Kubespray on an Ansible run. The
alert is real drift, not a false positive, but the fix is to remove the key from the profile rather
than to keep re-applying it.

## Problem

Two keys account for nearly all of these on a Kubespray node:

- **`nf_conntrack_max`** — kube-proxy sets it at pod start from
  `kube_proxy_conntrack_max_per_core × cores` (floored by `kube_proxy_conntrack_min`), logging
  `"Setting nf_conntrack_max"`. Any pod restart — upgrade, eviction, node reboot, DaemonSet rollout —
  re-establishes kube-proxy's number over the profile's.
- **`net.ipv4.ip_local_reserved_ports`** — Kubespray's *Ensure nodePort range is reserved* task
  writes `kube_apiserver_node_port_range` (default `30000-32767`) into `/etc/sysctl.d/99-sysctl.conf`
  and reloads it. Every run that reaches the node role replaces a longer profile list with just the
  NodePort range.

Both write the live value directly, so the change is instant and silent; nothing in either system
reports a conflict.

## Context

At boot the order favours tuned — `systemd-sysctl` applies `/etc/sysctl.d/*` first, `tuned.service`
starts after — which is why the value looks correct again after a reboot and the incident appears to
"fix itself". During operations the order is reversed. The window between the other owner's write and
the next profile re-apply is exactly when verification fails; nothing re-applies a tuned profile on a
schedule.

Verified against Kubespray **v2.27.0–v2.31.0**; the task and the kube-proxy defaults are unchanged
across the envelope.

## Diagnostics

```bash
grep -i 'verify: failed' /var/log/tuned/tuned.log | tail -20   # which key, and the two values
sysctl net.netfilter.nf_conntrack_max net.ipv4.ip_local_reserved_ports

# who set the conntrack limit, and when
kubectl -n kube-system logs ds/kube-proxy --tail=50 | grep -i conntrack

# did an Ansible run leave its own file behind
grep -rn ip_local_reserved /etc/sysctl.d/
ls -l /etc/sysctl.d/99-sysctl.conf
```

Compare the timestamp of the first failing verify entry with the kube-proxy pod start time or the
last Ansible run — they line up.

## Known Issues

- **Remove the contested key from the profile; set it through its real owner.** For the conntrack
  limit that means `kube_proxy_conntrack_max_per_core` in inventory (`0` hands the limit back to
  whoever else sets it). For the reserved-port list it means accepting Kubespray's value: the
  variable also feeds the apiserver's `--service-node-port-range` and Calico's
  `FELIX_KUBENODEPORTRANGES`, so it cannot be extended with unrelated ports
  ([[CONCEPT-TUNED_SYSCTL_OWNERSHIP]]).
- **Re-applying the profile is not a fix.** `tuned-adm profile <name>` clears the alert until the
  next pod restart or playbook run. If the response to this alert is a re-apply, the loop is
  permanent.
- **The conntrack *timeouts* are usually not in conflict.** Kubespray's kube-proxy defaults
  (`24h0m0s` established, `1h0m0s` close-wait) match what a typical profile sets (`86400`, `3600`),
  so those lines can stay.
- **Sizing check while you are there.** A profile inherited from a large bare-metal fleet can carry
  an `nf_conntrack_max` far above anything the node uses. Compare with reality —
  `sysctl net.netfilter.nf_conntrack_count` — before deciding the value is worth defending; the hash
  table costs 8 bytes per bucket permanently, and the ceiling permits roughly 300 bytes of kernel
  memory per tracked connection.

## References

- `roles/kubernetes/node/tasks/main.yml` (task *Ensure nodePort range is reserved*) and
  `roles/kubernetes/control-plane/defaults/main/kube-proxy.yml` — read at tag **v2.31.0**
  (verified 2026-07-28).
- Ownership map: [[CONCEPT-TUNED_SYSCTL_OWNERSHIP]]; permanent-failure variant:
  [[TROUBLE-TUNED_VERIFY_MISSING_SYSCTL]].
