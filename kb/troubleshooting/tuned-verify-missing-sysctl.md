---
id: TROUBLE-TUNED_VERIFY_MISSING_SYSCTL
type: troubleshooting
title: "tuned-adm verify fails forever: 'key' = 'None', expected 'value' (kernel does not expose the sysctl)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: null
verified_at: "2026-07-28"
confidence: verified
aliases:
  - "verify: failed: 'kernel.yama.ptrace_scope' = 'None'"
  - tuned verify failed None expected
  - Verification failed, current system settings differ from the preset profile
  - tuned-adm verify always fails
  - tuned ptrace_scope none
tags:
  - os
  - ubuntu
  - tuned
  - sysctl
  - monitoring
sources:
  - type: docs
    path: Ubuntu procps — /etc/sysctl.d/10-ptrace.conf
    url: https://gemfury.com/dcip/deb:procps/procps-2:3.3.10-4ubuntu2.4-amd64/content/etc/sysctl.d/10-ptrace.conf
    note: "Ubuntu default kernel.yama.ptrace_scope = 1, package-owned file"
  - type: docs
    path: Yama LSM — ptrace_scope
    url: https://www.kernel.org/doc/Documentation/security/Yama.txt
    note: "the sysctl exists only when the Yama LSM is built and active"
relations:
  - type: see_also
    target: CONCEPT-TUNED_UBUNTU
  - type: see_also
    target: TROUBLE-TUNED_VERIFY_FLAPS
---

# tuned-adm verify fails forever: 'key' = 'None', expected 'value' (kernel does not expose the sysctl)

## Summary

`tuned-adm verify` exits non-zero on every run, and the log names one key with the read value
**`None`**:

```
ERROR tuned.plugins.base: verify: failed: 'kernel.yama.ptrace_scope' = 'None', expected '2'
```

`None` is not "wrong value" — it means tuned **could not read the key at all**: the running kernel
does not expose it. The profile demands a setting that cannot exist on this node, so verification
can never pass, and the tuning it was supposed to provide is not in effect either.

## Problem

A profile is usually copied between fleets or written against a different kernel build. Any key that
is compiled out, gated behind an LSM that is not active, or renamed by the distribution produces this
permanent failure. Two Ubuntu-specific cases dominate:

- **`kernel.yama.ptrace_scope`** — exists only when the **Yama** LSM is built *and* active. Ubuntu
  ships Yama enabled and sets the value to `1` from the procps-owned file
  `/etc/sysctl.d/10-ptrace.conf`, so on a stock Ubuntu node the key is present. Reading `None`
  therefore means a non-stock kernel or an explicit `lsm=` boot parameter that omits `yama` — worth
  knowing on its own, because it also means **ptrace is unrestricted** while the profile claims
  otherwise.
- **unprivileged user namespaces** — `kernel.unprivileged_userns_clone` is a Debian/Ubuntu-carried
  key; from 23.10 the granular `kernel.apparmor_restrict_unprivileged_userns` was introduced (on by
  default in 24.04). A profile written for one release can name the key the other does not have.

The failure is loud in monitoring and invisible in behaviour, which is why it survives for months: a
`tuned.verify` check reports a problem on a node where nothing is actually broken.

## Context

Applies to any Kubernetes node running tuned; Kubespray does not manage tuned at any tag of the
envelope ([[CONCEPT-TUNED_UBUNTU]]). The failing key is reported once per verify run, so the log
fills at the monitoring interval — often several entries per five minutes, which buries genuinely
useful warnings.

## Diagnostics

```bash
tuned-adm verify; echo "exit=$?"
grep -i 'verify: failed' /var/log/tuned/tuned.log | tail -20      # names the key; 'None' = unreadable

# does the key exist at all?
sysctl kernel.yama.ptrace_scope 2>&1
ls -l /proc/sys/kernel/yama/ptrace_scope 2>&1

# why not — is the LSM active, and was it selected at boot?
cat /sys/kernel/security/lsm
grep -o 'lsm=[^ ]*' /proc/cmdline
grep -i CONFIG_SECURITY_YAMA /boot/config-$(uname -r)
```

If `grep 'verify: failed'` returns nothing while the exit code is non-zero, the failure is not in the
profile: check that the command runs with the privileges it needs (a monitoring agent calling
`tuned-adm` as an unprivileged user gets a non-zero exit regardless of node state).

## Known Issues

- **Decide, do not silence.** Two honest outcomes: make the key real, or drop it from the profile.
  Keeping a line that the kernel ignores is the worst of both — no protection *and* a red monitor.
  - *Make it real:* take the active list from `/sys/kernel/security/lsm`, append `yama`, set it as
    the `lsm=` kernel parameter, rebuild the bootloader config and reboot the node. **Requires a
    reboot — drain first.**
  - *Drop it:* remove the line from the profile source and re-apply
    (`tuned-adm profile <name> && tuned-adm verify`). No reboot, no service impact.
- **Fix the profile at its source.** tuned profiles come from an image, a configuration-management
  repo or a package. Editing `/etc/tuned/profiles/<name>/tuned.conf` on the node fixes the symptom
  until the next rollout re-installs the old file.
- **On Ubuntu the value also has a package owner.** `/etc/sysctl.d/10-ptrace.conf` belongs to procps
  and is replaced on package upgrade; setting `ptrace_scope` in a tuned profile puts two owners on
  one key ([[CONCEPT-TUNED_SYSCTL_OWNERSHIP]]).
- **Verify checks everything, including inherited plugins.** A profile that inherits
  `throughput-performance` also verifies the parent's settings; a key missing there fails the same
  way and is easy to miss because it is not in your file.

## References

- Yama LSM documentation (kernel.org); Ubuntu `procps` `/etc/sysctl.d/10-ptrace.conf`;
  Ubuntu 23.10/24.04 unprivileged user-namespace restriction.
- Ownership map: [[CONCEPT-TUNED_SYSCTL_OWNERSHIP]]; OS layer: [[CONCEPT-TUNED_UBUNTU]].
