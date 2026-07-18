---
id: TROUBLE-CILIUM_IPSEC_HOST_ROUTING_CVE
type: troubleshooting
title: "Cilium 1.19 IPsec + KPR + BPF masquerade auto-enables eBPF host routing — CVE-2025-37959 kernel fix required"
status: active
kubespray_version: ">=v2.31.0 <=v2.31.0"
kubernetes_version: ">=1.33 <=1.35"
component_version: ">=1.19.3 <=1.19.3"
verified_at: "2026-07-18"
confidence: confirmed
aliases:
  - CVE-2025-37959
  - cilium ipsec bpf host routing
  - enable-host-legacy-routing ipsec
  - cilium 1.19 ipsec kernel bug
  - ebpf host routing ipsec cve
tags:
  - cilium
  - troubleshooting
  - ipsec
  - security
  - cve
sources:
  - type: docs
    path: Documentation/operations/upgrade.rst
    url: https://github.com/cilium/cilium/blob/v1.19.3/Documentation/operations/upgrade.rst
    note: "1.19: IPsec+KPR+BPF masquerade auto-enables eBPF Host Routing; requires kernel fix CVE-2025-37959 or --enable-host-legacy-routing=true"
relations:
  - type: see_also
    target: CONCEPT-CILIUM_ENCRYPTION
  - type: see_also
    target: TROUBLE-CILIUM_KNOWN_CVES
  - type: see_also
    target: PRACTICE-KERNEL_REQUIREMENTS
  - type: see_also
    target: UPGRADE-CILIUM_1_15_TO_1_19
---

# Cilium 1.19 IPsec + KPR + BPF masquerade auto-enables eBPF host routing — CVE-2025-37959 kernel fix required

## Summary

In Cilium **1.19**, a cluster running **IPsec encryption + kube-proxy-replacement (KPR) + BPF
masquerading** **automatically enables eBPF Host Routing**. Running eBPF Host Routing together with
IPsec depends on a **kernel bugfix tracked as CVE-2025-37959** — on an unpatched kernel this
combination can misbehave. When Kubespray moves Cilium to **1.19.3 (v2.31.0)**, ensure node kernels are
patched, or disable the auto-enabled path with `--enable-host-legacy-routing=true`.

## Problem

- After upgrading to Kubespray v2.31.0 with IPsec + KPR + BPF masquerade enabled, encrypted traffic
  misbehaves / packets are mishandled on nodes whose kernel lacks the CVE-2025-37959 fix.
- The change is implicit: you did not turn on eBPF Host Routing — Cilium 1.19 enabled it because the
  feature combination is present.

## Context

- Applies to Cilium **1.19** → Kubespray **v2.31.0** ([[UPGRADE-CILIUM_1_15_TO_1_19]]). Trigger is the
  **specific combination**: `encryption.type=ipsec` ([[CONCEPT-CILIUM_ENCRYPTION]]) **+**
  `kube-proxy-replacement=true` **+** BPF masquerading. Any one absent → eBPF Host Routing is not
  auto-enabled by this rule (`upgrade.rst`@v1.19.3).
- eBPF Host Routing bypasses the host network stack for performance; with IPsec it needs the kernel fix
  referenced by CVE-2025-37959.

## Diagnostics

- Confirm the combination: `cilium config view | grep -Ei "enable-ipsec|kube-proxy-replacement|masquerade|host-routing"`
  (or the `cilium-config` ConfigMap).
- Check node kernel version/patch level against your distro's advisory for **CVE-2025-37959**
  ([[PRACTICE-KERNEL_REQUIREMENTS]]).

## Known Issues

- **Fix (preferred):** patch node kernels to a version containing the CVE-2025-37959 fix before/at the
  v2.31.0 upgrade.
- **Fix (workaround):** set **`--enable-host-legacy-routing=true`** (Helm
  `bpf.hostLegacyRouting=true`) to keep legacy host routing and avoid the IPsec + eBPF-host-routing
  path until kernels are patched.
- Track alongside other Cilium CVEs for the shipped version ([[TROUBLE-CILIUM_KNOWN_CVES]]).

## References

- Cilium `Documentation/operations/upgrade.rst`@v1.19.3 (IPsec + eBPF Host Routing / CVE-2025-37959).
  Encryption [[CONCEPT-CILIUM_ENCRYPTION]]; CVE matrix [[TROUBLE-CILIUM_KNOWN_CVES]]; kernel
  [[PRACTICE-KERNEL_REQUIREMENTS]]; full jump [[UPGRADE-CILIUM_1_15_TO_1_19]].
