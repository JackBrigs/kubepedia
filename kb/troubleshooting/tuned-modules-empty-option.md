---
id: TROUBLE-TUNED_MODULES_EMPTY_OPTION
type: troubleshooting
title: "tuned: 'unrecognized module option for module X:' with nothing after the colon"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-28"
confidence: verified
aliases:
  - "unrecognized module option for module 'nf_conntrack'"
  - unrecognized module option tuned
  - tuned plugin_modules warning
  - tuned modules section empty value
tags:
  - os
  - ubuntu
  - tuned
  - conntrack
sources:
  - type: docs
    path: tuned — modules plugin
    url: https://tuned-project.org/
    note: "the [modules] section takes 'module=option=value ...'; an empty option string does not parse"
relations:
  - type: see_also
    target: CONCEPT-TUNED_UBUNTU
  - type: see_also
    target: TROUBLE-TUNED_VM_WARNING_NOISE
---

# tuned: 'unrecognized module option for module X:' with nothing after the colon

## Summary

```
WARNING tuned.plugins.plugin_modules: unrecognized module option for module 'nf_conntrack':
```

The `[modules]` section of the profile declares a module with an **empty value**. The plugin tries to
parse the option string as `name=value`, gets nothing, and warns. It is printed on every profile
apply *and* every verify, so on a monitored node it repeats at the check interval and buries real
messages in the log.

## Problem

The profile contains:

```ini
[modules]
nf_conntrack=
```

The intent is usually "make sure this module is loaded" — but the plugin's syntax is
`module=option=value ...`, so an empty right-hand side is meaningless rather than a no-op. Nothing
breaks: the module is loaded (on a Kubernetes node Kubespray runs `modprobe nf_conntrack` itself in
`roles/kubernetes/node/tasks/main.yml`), and any real tuning of it comes from elsewhere in the
profile — typically a `[sysfs]` write of `hashsize`.

The warning does **not** affect `tuned-adm verify`: the modules plugin reports
`verify: passed: 'module 'nf_conntrack' is loaded'` alongside it. A node can log this every five
minutes for a year while verification is green.

## Context

Any node running tuned; seen on Ubuntu Kubernetes nodes with a hand-written `kubernetes` profile.
Kubespray does not manage tuned, so the profile comes from the OS image or a separate
configuration-management repo ([[CONCEPT-TUNED_UBUNTU]]).

## Diagnostics

```bash
grep -n -A3 '^\[modules\]' /etc/tuned/profiles/*/tuned.conf /usr/lib/tuned/profiles/*/tuned.conf 2>/dev/null
grep -c 'unrecognized module option' /var/log/tuned/tuned.log
lsmod | grep nf_conntrack
```

## Known Issues

- **Fix: delete the empty entry** (usually the whole two-line `[modules]` section), then re-apply:
  `tuned-adm profile <name> && tuned-adm verify`. No service impact — removing the entry does not
  unload the module.
- **If a module option was genuinely intended**, write it properly — `nf_conntrack=hashsize=131072` —
  and know that module parameters apply at **load** time. The plugin can force a reload with the
  `+r` prefix, and reloading `nf_conntrack` **flushes the connection-tracking table**: on a node
  carrying traffic that breaks established NAT'd flows, i.e. Service traffic. Drain first, or set
  the value at runtime through `[sysfs]` instead.
- **Do not confuse module parameters with sysctls.** `nf_conntrack_max` is a sysctl, not a module
  option; the only common module parameter here is `hashsize`. Putting the former in `[modules]`
  produces this same warning.
- **Fix it at the profile's source**, not on the node — the next rollout restores the old file.

## References

- tuned modules plugin syntax; Kubespray `roles/kubernetes/node/tasks/main.yml` (task *Modprobe
  conntrack module*, tag v2.31.0) — verified 2026-07-28.
- Related log noise: [[TROUBLE-TUNED_VM_WARNING_NOISE]].
