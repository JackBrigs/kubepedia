---
id: TROUBLE-TALOS_0_12_DEFECTS
type: troubleshooting
title: "talos 0.12: defects fixed in the 0.12 line"
status: active
kubespray_version: null
kubernetes_version: null
component_version: ">=0.12.0 <0.13.0"
verified_at: "2026-07-31"
confidence: verified
aliases:
  - talos 0.12 known issues
  - talos 0.12 fixed in
  - is this talos bug already fixed
tags:
  - troubleshooting
  - upgrade
  - talos
sources:
  - type: docs
    path: siderolabs/talos release notes for the 0.12 line — bug-fix entries
    url: https://github.com/siderolabs/talos/releases
    note: "machine-extracted by scripts/upstream_issues.py; short and duplicate lines filtered"
relations:
  - type: see_also
    target: CONCEPT-UPGRADE_HORIZON
---

# talos 0.12: defects fixed in the 0.12 line

## Summary

**153 defects** the project fixed across **4 releases** of the 0.12 line, from 0.12.0 to
0.12.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.12.0

- fix: don't extract nil IPs in the GCP platform
- fix: properly handle omitempty fields in the validator
- fix: validate IP address returned as HTTP response in platform code
- fix: don't allow bootstrap if etcd data directory is not empty
- fix: don't support cgroups nesting in process runner
- fix: do not set KSPP kernel params in container mode
- fix: extramount should have `yaml:",inline"` tag
- fix: don't panic if the machine config doesn't have network (EM)
- fix: make sure file mode is same (reproducibility issue)
- fix: enable seccomp default profile by default
- fix: match correctly routes on the address family
- fix: make route resources ID match closer routing table primary key
- fix: correctly handle nodoc for struct fields
- fix: remove admission plugins enabled by default from the list
- fix: resolve several issues with Wireguard link specs
- fix: do not require ToVersion to be set when detecting version
- fix: set the /etc/os-release HOME_URL parameter
- fix: pass all logs through the options.Log method
- fix: make ethtool optional in link status controller
- fix: write upgrade logs only to the LogOutput if it's defined
- fix: correctly pick route scope for link-local destination
- fix: workaround issues when IPv6 is fully or partially disabled
- fix: ignore DeadlineExceeded error correctly on bootstrap
- fix: make forfeit leadership connect to the right node
- fix: ignore 'not a leader' error on forfeit leadership
- fix: workaround 'Unauthorized' errors when accessing Kubernetes API
- fix: fill uuid argument correctly in the config download URL
- fix: make output of `upgrade-k8s` command less scary
- fix: restart the merge controllers on conflict
- fix: ignore deadline exceeded errors on bootstrap
- fix: don't print git sha of the release twice in the dashboard
- fix: issue worker apid certs properly on renewal
- fix: don't set bond delay options if miimon is not enabled
- fix: handle cases when merged resource re-appears before being destroyed
- fix: perform correct PMBR partition calculations
- fix: preserve the PMBR bootable flag when opening GPT partition

### 0.12.1

- fix: correctly define example for `extraMounts`
- fix: don't extract nil IPs in the GCP platform
- fix: properly handle omitempty fields in the validator
- fix: validate IP address returned as HTTP response in platform code
- fix: don't allow bootstrap if etcd data directory is not empty
- fix: don't support cgroups nesting in process runner
- fix: do not set KSPP kernel params in container mode
- fix: extramount should have `yaml:",inline"` tag
- fix: don't panic if the machine config doesn't have network (EM)
- fix: make sure file mode is same (reproducibility issue)
- fix: enable seccomp default profile by default
- fix: match correctly routes on the address family
- fix: make route resources ID match closer routing table primary key
- fix: correctly handle nodoc for struct fields
- fix: remove admission plugins enabled by default from the list
- fix: resolve several issues with Wireguard link specs
- fix: do not require ToVersion to be set when detecting version
- fix: set the /etc/os-release HOME_URL parameter
- fix: pass all logs through the options.Log method
- fix: make ethtool optional in link status controller
- fix: write upgrade logs only to the LogOutput if it's defined
- fix: correctly pick route scope for link-local destination
- fix: workaround issues when IPv6 is fully or partially disabled
- fix: ignore DeadlineExceeded error correctly on bootstrap
- fix: make forfeit leadership connect to the right node
- fix: ignore 'not a leader' error on forfeit leadership
- fix: workaround 'Unauthorized' errors when accessing Kubernetes API
- fix: fill uuid argument correctly in the config download URL
- fix: make output of `upgrade-k8s` command less scary
- fix: restart the merge controllers on conflict
- fix: ignore deadline exceeded errors on bootstrap
- fix: don't print git sha of the release twice in the dashboard
- fix: issue worker apid certs properly on renewal
- fix: don't set bond delay options if miimon is not enabled
- fix: handle cases when merged resource re-appears before being destroyed
- fix: perform correct PMBR partition calculations
- fix: preserve the PMBR bootable flag when opening GPT partition

### 0.12.2

- fix: tear down control plane static pods when etcd is stopped
- fix: completely prevent editing resources other than mc
- fix: write KubernetesCACert chmodded 0400 instead of 0500
- fix: correctly define example for `extraMounts`
- fix: don't extract nil IPs in the GCP platform
- fix: properly handle omitempty fields in the validator
- fix: validate IP address returned as HTTP response in platform code
- fix: don't allow bootstrap if etcd data directory is not empty
- fix: don't support cgroups nesting in process runner
- fix: do not set KSPP kernel params in container mode
- fix: extramount should have `yaml:",inline"` tag
- fix: don't panic if the machine config doesn't have network (EM)
- fix: make sure file mode is same (reproducibility issue)
- fix: enable seccomp default profile by default
- fix: match correctly routes on the address family
- fix: make route resources ID match closer routing table primary key
- fix: correctly handle nodoc for struct fields
- fix: remove admission plugins enabled by default from the list
- fix: resolve several issues with Wireguard link specs
- fix: do not require ToVersion to be set when detecting version
- fix: set the /etc/os-release HOME_URL parameter
- fix: pass all logs through the options.Log method
- fix: make ethtool optional in link status controller
- fix: write upgrade logs only to the LogOutput if it's defined
- fix: correctly pick route scope for link-local destination
- fix: workaround issues when IPv6 is fully or partially disabled
- fix: ignore DeadlineExceeded error correctly on bootstrap
- fix: make forfeit leadership connect to the right node
- fix: ignore 'not a leader' error on forfeit leadership
- fix: workaround 'Unauthorized' errors when accessing Kubernetes API
- fix: fill uuid argument correctly in the config download URL
- fix: make output of `upgrade-k8s` command less scary
- fix: restart the merge controllers on conflict
- fix: ignore deadline exceeded errors on bootstrap
- fix: don't print git sha of the release twice in the dashboard
- fix: issue worker apid certs properly on renewal
- fix: don't set bond delay options if miimon is not enabled
- fix: handle cases when merged resource re-appears before being destroyed
- fix: perform correct PMBR partition calculations
- fix: preserve the PMBR bootable flag when opening GPT partition

### 0.12.3

- fix: tear down control plane static pods when etcd is stopped
- fix: completely prevent editing resources other than mc
- fix: write KubernetesCACert chmodded 0400 instead of 0500
- fix: correctly define example for `extraMounts`
- fix: don't extract nil IPs in the GCP platform
- fix: properly handle omitempty fields in the validator
- fix: validate IP address returned as HTTP response in platform code
- fix: don't allow bootstrap if etcd data directory is not empty
- fix: don't support cgroups nesting in process runner
- fix: do not set KSPP kernel params in container mode
- fix: extramount should have `yaml:",inline"` tag
- fix: don't panic if the machine config doesn't have network (EM)
- fix: make sure file mode is same (reproducibility issue)
- fix: enable seccomp default profile by default
- fix: match correctly routes on the address family
- fix: make route resources ID match closer routing table primary key
- fix: correctly handle nodoc for struct fields
- fix: remove admission plugins enabled by default from the list
- fix: resolve several issues with Wireguard link specs
- fix: do not require ToVersion to be set when detecting version
- fix: set the /etc/os-release HOME_URL parameter
- fix: pass all logs through the options.Log method
- fix: make ethtool optional in link status controller
- fix: write upgrade logs only to the LogOutput if it's defined
- fix: correctly pick route scope for link-local destination
- fix: workaround issues when IPv6 is fully or partially disabled
- fix: ignore DeadlineExceeded error correctly on bootstrap
- fix: make forfeit leadership connect to the right node
- fix: ignore 'not a leader' error on forfeit leadership
- fix: workaround 'Unauthorized' errors when accessing Kubernetes API
- fix: fill uuid argument correctly in the config download URL
- fix: make output of `upgrade-k8s` command less scary
- fix: restart the merge controllers on conflict
- fix: ignore deadline exceeded errors on bootstrap
- fix: don't print git sha of the release twice in the dashboard
- fix: issue worker apid certs properly on renewal
- fix: don't set bond delay options if miimon is not enabled
- fix: handle cases when merged resource re-appears before being destroyed
- fix: perform correct PMBR partition calculations
- fix: preserve the PMBR bootable flag when opening GPT partition


## Diagnostics

```bash
kubectl get nodes -o wide      # node-level components
helm list -A                   # chart-deployed components
```

Compare the running version against **0.12.3**, the newest release recorded here for this line.

## Known Issues

The list is machine-extracted from upstream release notes: lines shorter than 45 characters and
duplicates are dropped, since headings and list fragments reach the extractor looking like entries.
Treat it as an index into upstream notes, not as a substitute for them — a defect that matters gets
its own analysed document with sources, diagnostics and a remedy.

Behaviour changes for the same component are tracked separately, in its breaking-changes document:
they are not defects and do not disappear with an upgrade.

## References

- Upstream releases of `siderolabs/talos`, extracted 2026-07-31 by `scripts/upstream_issues.py`;
  raw data in `reports/upstream/talos.json`.
- Upgrade planning: [[CONCEPT-UPGRADE_HORIZON]].
