---
id: TROUBLE-CALICO_3_27_DEFECTS
type: troubleshooting
title: "calico 3.27: defects fixed in the 3.27 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=3.27.0 <3.28.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - calico 3.27 known issues
  - calico 3.27 fixed in
  - is this calico bug already fixed
tags:
  - troubleshooting
  - upgrade
  - calico
sources:
  - type: docs
    path: projectcalico/calico release notes for the 3.27 line — bug-fix entries
    url: https://github.com/projectcalico/calico/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# calico 3.27: defects fixed in the 3.27 line

## Summary

**14 defects** the project fixed across **1 releases** of the 3.27 line, from 3.27.0 to
3.27.0. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 3.27.0

- Prevent IPAM garbage collection from freezing when under high load [calico #8154](https://github.com/projectcalico/calico/pull/8154) (@JuoCode)
- Correct policy for OpenStack sec group with no remote\_ip\_prefix [calico #8026](https://github.com/projectcalico/calico/pull/8026) (@nelljerram)
- Fixed AWS ec2 detection not working with imdsv2 on Calico for Windows. [calico #7970](https://github.com/projectcalico/calico/pull/7970) (@davidgiga1993)
- Fix panic when running 'calicoctl get nodes' when ASNumber was not present in the default BGPConfiguration. [calico #7858](https://github.com/projectcalico/calico/pull/7858) (@coutinhop)
- Fix a few instances where KUBECONFIG was not respected [calico #7796](https://github.com/projectcalico/calico/pull/7796) (@skmatti)
- Fix helm chart rendering multiple image pull secrets incorrectly [calico #7752](https://github.com/projectcalico/calico/pull/7752) (@oxr463)
- Fix YAML injection vulnerabilities due to unsafe templating [calico #7642](https://github.com/projectcalico/calico/pull/7642) (@skmatti)
- Fix 'error while loading shared libraries: libresolv.so.2: cannot open shared object file' on csi-node-driver-registrar. [calico #7586](https://github.com/projectcalico/calico/pull/7586) (@coutinhop)
- Fix a divide-by-zero panic in Typha if it received a SIGTERM when it had no active connections. Since Typha exits in either case, the impact was limited to a scary panic log. [calico #7585](https://github.com/projectcalico/calico/pull/7585) (@fasaxc)
- eBPF: fixed host access to self and a service that redirects to self without CTLB [calico #8189](https://github.com/projectcalico/calico/pull/8189) (@tomastigera)
- Fix incorrect conversion to 16-bit offset in the BPF assembler. Fail if the value would wrap. [calico #8176](https://github.com/projectcalico/calico/pull/8176) (@fasaxc)
- BPF mode: fix that netlink IP sets were programmed even in BPF mode until the first policy/endpoint deletion event. [calico #8101](https://github.com/projectcalico/calico/pull/8101) (@fasaxc)
- eBPF: fixes felix panic upon restart in debug mode when there are existing policy counters [calico #7797](https://github.com/projectcalico/calico/pull/7797) (@tomastigera)
- eBPF: fix applyOnforward=false in global policies [calico #7707](https://github.com/projectcalico/calico/pull/7707) (@tomastigera)


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **3.27.0**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `projectcalico/calico`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/calico.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
