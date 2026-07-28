---
id: TROUBLE-TUNED_VM_WARNING_NOISE
type: troubleshooting
title: "tuned on a VM: MSR_IA32_ENERGY_PERF_BIAS and 'instance video: no matching devices' every run"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-28"
confidence: verified
aliases:
  - "your CPU doesn't support MSR_IA32_ENERGY_PERF_BIAS"
  - "instance video: no matching devices available"
  - tuned warnings virtual machine
  - tuned log noise
tags:
  - os
  - tuned
  - virtualization
sources:
  - type: docs
    path: tuned — profiles and plugins
    url: https://tuned-project.org/
    note: "plugin instances are inherited from the parent profile via include= and run even without matching hardware"
relations:
  - type: see_also
    target: CONCEPT-TUNED_UBUNTU
  - type: see_also
    target: TROUBLE-TUNED_MODULES_EMPTY_OPTION
---

# tuned on a VM: MSR_IA32_ENERGY_PERF_BIAS and 'instance video: no matching devices' every run

## Summary

```
WARNING tuned.plugins.plugin_cpu: your CPU doesn't support MSR_IA32_ENERGY_PERF_BIAS, ignoring CPU energy performance bias
WARNING tuned.plugins.base: instance video: no matching devices available
```

Both are expected on a virtual machine and neither affects `tuned-adm verify`. They matter only
because they repeat on every apply and every verify — on a monitored node that is several entries per
check interval, and the log stops being readable exactly when a real failure needs to be found in it.

## Problem

- **`MSR_IA32_ENERGY_PERF_BIAS`** — the CPU plugin tries to set the energy/performance bias through a
  model-specific register the guest CPU does not expose. That part of the tuning is a no-op. The rest
  of a `[cpu]` section (for example `force_latency`) is written to `/dev/cpu_dma_latency`, which
  inside a guest also decides little: C-states belong to the hypervisor.
- **`instance video: no matching devices available`** — the `video` plugin instance comes from the
  parent profile (`include=throughput-performance` and similar) and finds no GPU. Inheritance applies
  the parent's plugins whether or not the hardware exists.

## Context

Any virtualized node running tuned with a profile that inherits a stock performance profile. On a
Kubernetes node the interval is set by whatever runs `tuned-adm verify` — a monitoring item typically
does it every few minutes.

## Diagnostics

```bash
systemd-detect-virt
grep -c 'MSR_IA32_ENERGY_PERF_BIAS\|no matching devices' /var/log/tuned/tuned.log
grep -n 'include=' /etc/tuned/profiles/*/tuned.conf
```

## Known Issues

- **Leave them, or disable the plugin instances.** On some tuned versions a profile can switch off an
  inherited instance:

  ```ini
  [video]
  enabled=false

  [cpu]
  enabled=false
  ```

  Support for `enabled=false` varies by version — after re-applying, confirm the warnings are gone
  **and** that `tuned-adm verify` did not start complaining about something new.
- **Removing `[cpu]` outright is reasonable on a guest**, where neither the energy bias nor
  `force_latency` reaches real hardware. The `video` instance comes from the parent profile and can
  only be disabled, not deleted.
- **Do not treat these as the cause of a failing verify.** They are `WARNING`; a failing verification
  always logs an `ERROR` line naming the key — grep for `verify: failed`
  ([[TROUBLE-TUNED_VERIFY_MISSING_SYSCTL]]).

## References

- tuned plugin/profile inheritance behaviour; observed on Ubuntu Kubernetes guests, verified
  2026-07-28.
- Related noise from the modules plugin: [[TROUBLE-TUNED_MODULES_EMPTY_OPTION]].
