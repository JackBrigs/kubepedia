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

**239 defects** the project fixed across **4 releases** of the 0.12 line, from 0.12.0 to
0.12.3. A cluster running a version below the one an entry sits under still carries that defect.

Use this before reproducing a suspected bug: on this line it is often already named and fixed, and
the remedy is a patch bump rather than an investigation.

## Problem

Entries are grouped by the release that fixed them, oldest first.

## Context

### 0.12.0

- talos-systems/talos@87c258093 fix: allow updating diskSelector option
- talos-systems/talos@eba00723d fix: don't extract nil IPs in the GCP platform
- talos-systems/talos@3a38f0ded fix: properly handle omitempty fields in the validator
- talos-systems/talos@2e220cb65 fix: validate IP address returned as HTTP response in platform code
- talos-systems/talos@b63a2ea0e fix: don't allow bootstrap if etcd data directory is not empty
- talos-systems/talos@cd0532848 fix: cgroup delegate
- talos-systems/talos@e22301e76 chore: fix arm64 reproducibility issues
- talos-systems/talos@e84e2902c fix: don't support cgroups nesting in process runner
- talos-systems/talos@2cf53fb34 fix: do not set KSPP kernel params in container mode
- talos-systems/talos@4bb84ea0c fix: extramount should have `yaml:",inline"` tag
- talos-systems/talos@e948560be fix: don't panic if the machine config doesn't have network (EM)
- talos-systems/talos@67494923b fix: make sure file mode is same (reproducibility issue)
- talos-systems/talos@e6fa401b6 fix: enable seccomp default profile by default
- talos-systems/talos@a15f01844 fix: move etcd PKI under /system/secrets
- talos-systems/talos@eb02afe18 fix: match correctly routes on the address family
- talos-systems/talos@b68ed1eb8 fix: make route resources ID match closer routing table primary key
- talos-systems/talos@585f63371 fix: correctly handle nodoc for struct fields
- talos-systems/talos@5285a46d7 fix: maintenance mode reason message
- talos-systems/talos@1a2e78a24 fix: update go-blockdevice
- talos-systems/talos@3c566dbc3 fix: remove admission plugins enabled by default from the list
- talos-systems/talos@69ead3735 fix: preserve PMBR bootable flag correctly
- talos-systems/talos@dee630517 fix: align partitions with minimal I/O size
- talos-systems/talos@0b8681b4b fix: resolve several issues with Wireguard link specs
- talos-systems/talos@d4f9804f8 chore: fix typos
- talos-systems/talos@df54584a3 fix: drop linux capabilities
- talos-systems/talos@7332d6369 fix: bump pkgs for new kernel 5.10.52
- talos-systems/talos@70d2505b7 fix: do not require ToVersion to be set when detecting version
- talos-systems/talos@b6c47f866 fix: set the /etc/os-release HOME_URL parameter
- talos-systems/talos@da6f786ca fix: kuberentes => kubernetes typo
- talos-systems/talos@2e463348b fix: pass all logs through the options.Log method
- talos-systems/talos@4e9c5afb6 fix: make ethtool optional in link status controller
- talos-systems/talos@bf61c2cc4 fix: write upgrade logs only to the LogOutput if it's defined
- talos-systems/talos@b358a189b fix: correctly pick route scope for link-local destination
- talos-systems/talos@72b76abfd fix: workaround issues when IPv6 is fully or partially disabled
- talos-systems/talos@6fbec9e0c fix: cache etcd client used for healthchecks
- talos-systems/talos@011e2885e fix: validate bond slaves addressing
- talos-systems/talos@10c28758a fix: ignore DeadlineExceeded error correctly on bootstrap
- talos-systems/talos@6b661114d fix: make COSI runtime history depth smaller
- talos-systems/talos@9bf899bdd fix: make forfeit leadership connect to the right node
- talos-systems/talos@6d13d2cf9 fix: close Kubernetes API client
- talos-systems/talos@aaa36f3b4 fix: ignore 'not a leader' error on forfeit leadership
- talos-systems/talos@22a419367 fix: workaround 'Unauthorized' errors when accessing Kubernetes API
- talos-systems/talos@f5721050d fix: controlplane keyusage
- talos-systems/talos@3d7726613 fix: fill uuid argument correctly in the config download URL
- talos-systems/talos@e883c12b3 fix: make output of `upgrade-k8s` command less scary
- talos-systems/talos@7f8e50de4 fix: restart the merge controllers on conflict
- talos-systems/talos@60d736094 fix: ignore deadline exceeded errors on bootstrap
- talos-systems/talos@ee06dd69f fix: don't print git sha of the release twice in the dashboard
- talos-systems/talos@07fb61e5d fix: issue worker apid certs properly on renewal
- talos-systems/talos@2fa54107b chore: fix tests for disabled RBAC
- talos-systems/talos@78583ba98 fix: don't set bond delay options if miimon is not enabled
- talos-systems/talos@5f6ec3ef6 fix: handle cases when merged resource re-appears before being destroyed
- talos-systems/talos@1e9a0e745 fix: documentation typos
- talos-systems/go-blockdevice@fe24303 fix: perform correct PMBR partition calculations
- talos-systems/go-blockdevice@2ec0c3c fix: preserve the PMBR bootable flag when opening GPT partition
- talos-systems/pkgs@7a29722 fix: set iPXE version properly

### 0.12.1

- talos-systems/talos@a72fa2a93 fix: correctly define example for `extraMounts`
- talos-systems/talos@87c258093 fix: allow updating diskSelector option
- talos-systems/talos@eba00723d fix: don't extract nil IPs in the GCP platform
- talos-systems/talos@3a38f0ded fix: properly handle omitempty fields in the validator
- talos-systems/talos@2e220cb65 fix: validate IP address returned as HTTP response in platform code
- talos-systems/talos@b63a2ea0e fix: don't allow bootstrap if etcd data directory is not empty
- talos-systems/talos@cd0532848 fix: cgroup delegate
- talos-systems/talos@e22301e76 chore: fix arm64 reproducibility issues
- talos-systems/talos@e84e2902c fix: don't support cgroups nesting in process runner
- talos-systems/talos@2cf53fb34 fix: do not set KSPP kernel params in container mode
- talos-systems/talos@4bb84ea0c fix: extramount should have `yaml:",inline"` tag
- talos-systems/talos@e948560be fix: don't panic if the machine config doesn't have network (EM)
- talos-systems/talos@67494923b fix: make sure file mode is same (reproducibility issue)
- talos-systems/talos@e6fa401b6 fix: enable seccomp default profile by default
- talos-systems/talos@a15f01844 fix: move etcd PKI under /system/secrets
- talos-systems/talos@eb02afe18 fix: match correctly routes on the address family
- talos-systems/talos@b68ed1eb8 fix: make route resources ID match closer routing table primary key
- talos-systems/talos@585f63371 fix: correctly handle nodoc for struct fields
- talos-systems/talos@5285a46d7 fix: maintenance mode reason message
- talos-systems/talos@1a2e78a24 fix: update go-blockdevice
- talos-systems/talos@3c566dbc3 fix: remove admission plugins enabled by default from the list
- talos-systems/talos@69ead3735 fix: preserve PMBR bootable flag correctly
- talos-systems/talos@dee630517 fix: align partitions with minimal I/O size
- talos-systems/talos@0b8681b4b fix: resolve several issues with Wireguard link specs
- talos-systems/talos@d4f9804f8 chore: fix typos
- talos-systems/talos@df54584a3 fix: drop linux capabilities
- talos-systems/talos@7332d6369 fix: bump pkgs for new kernel 5.10.52
- talos-systems/talos@70d2505b7 fix: do not require ToVersion to be set when detecting version
- talos-systems/talos@b6c47f866 fix: set the /etc/os-release HOME_URL parameter
- talos-systems/talos@da6f786ca fix: kuberentes => kubernetes typo
- talos-systems/talos@2e463348b fix: pass all logs through the options.Log method
- talos-systems/talos@4e9c5afb6 fix: make ethtool optional in link status controller
- talos-systems/talos@bf61c2cc4 fix: write upgrade logs only to the LogOutput if it's defined
- talos-systems/talos@b358a189b fix: correctly pick route scope for link-local destination
- talos-systems/talos@72b76abfd fix: workaround issues when IPv6 is fully or partially disabled
- talos-systems/talos@6fbec9e0c fix: cache etcd client used for healthchecks
- talos-systems/talos@011e2885e fix: validate bond slaves addressing
- talos-systems/talos@10c28758a fix: ignore DeadlineExceeded error correctly on bootstrap
- talos-systems/talos@6b661114d fix: make COSI runtime history depth smaller
- talos-systems/talos@9bf899bdd fix: make forfeit leadership connect to the right node
- talos-systems/talos@6d13d2cf9 fix: close Kubernetes API client
- talos-systems/talos@aaa36f3b4 fix: ignore 'not a leader' error on forfeit leadership
- talos-systems/talos@22a419367 fix: workaround 'Unauthorized' errors when accessing Kubernetes API
- talos-systems/talos@f5721050d fix: controlplane keyusage
- talos-systems/talos@3d7726613 fix: fill uuid argument correctly in the config download URL
- talos-systems/talos@e883c12b3 fix: make output of `upgrade-k8s` command less scary
- talos-systems/talos@7f8e50de4 fix: restart the merge controllers on conflict
- talos-systems/talos@60d736094 fix: ignore deadline exceeded errors on bootstrap
- talos-systems/talos@ee06dd69f fix: don't print git sha of the release twice in the dashboard
- talos-systems/talos@07fb61e5d fix: issue worker apid certs properly on renewal
- talos-systems/talos@2fa54107b chore: fix tests for disabled RBAC
- talos-systems/talos@78583ba98 fix: don't set bond delay options if miimon is not enabled
- talos-systems/talos@5f6ec3ef6 fix: handle cases when merged resource re-appears before being destroyed
- talos-systems/talos@1e9a0e745 fix: documentation typos
- talos-systems/go-blockdevice@fe24303 fix: perform correct PMBR partition calculations
- talos-systems/go-blockdevice@2ec0c3c fix: preserve the PMBR bootable flag when opening GPT partition
- talos-systems/pkgs@7a29722 fix: set iPXE version properly

### 0.12.2

- talos-systems/talos@7b4a6b361 fix: patch multi nodes support
- talos-systems/talos@110551865 fix: tear down control plane static pods when etcd is stopped
- talos-systems/talos@5824f5024 fix: completely prevent editing resources other than mc
- talos-systems/talos@5700c81bf fix: write KubernetesCACert chmodded 0400 instead of 0500
- talos-systems/talos@a72fa2a93 fix: correctly define example for `extraMounts`
- talos-systems/talos@87c258093 fix: allow updating diskSelector option
- talos-systems/talos@eba00723d fix: don't extract nil IPs in the GCP platform
- talos-systems/talos@3a38f0ded fix: properly handle omitempty fields in the validator
- talos-systems/talos@2e220cb65 fix: validate IP address returned as HTTP response in platform code
- talos-systems/talos@b63a2ea0e fix: don't allow bootstrap if etcd data directory is not empty
- talos-systems/talos@cd0532848 fix: cgroup delegate
- talos-systems/talos@e22301e76 chore: fix arm64 reproducibility issues
- talos-systems/talos@e84e2902c fix: don't support cgroups nesting in process runner
- talos-systems/talos@2cf53fb34 fix: do not set KSPP kernel params in container mode
- talos-systems/talos@4bb84ea0c fix: extramount should have `yaml:",inline"` tag
- talos-systems/talos@e948560be fix: don't panic if the machine config doesn't have network (EM)
- talos-systems/talos@67494923b fix: make sure file mode is same (reproducibility issue)
- talos-systems/talos@e6fa401b6 fix: enable seccomp default profile by default
- talos-systems/talos@a15f01844 fix: move etcd PKI under /system/secrets
- talos-systems/talos@eb02afe18 fix: match correctly routes on the address family
- talos-systems/talos@b68ed1eb8 fix: make route resources ID match closer routing table primary key
- talos-systems/talos@585f63371 fix: correctly handle nodoc for struct fields
- talos-systems/talos@5285a46d7 fix: maintenance mode reason message
- talos-systems/talos@1a2e78a24 fix: update go-blockdevice
- talos-systems/talos@3c566dbc3 fix: remove admission plugins enabled by default from the list
- talos-systems/talos@69ead3735 fix: preserve PMBR bootable flag correctly
- talos-systems/talos@dee630517 fix: align partitions with minimal I/O size
- talos-systems/talos@0b8681b4b fix: resolve several issues with Wireguard link specs
- talos-systems/talos@d4f9804f8 chore: fix typos
- talos-systems/talos@df54584a3 fix: drop linux capabilities
- talos-systems/talos@7332d6369 fix: bump pkgs for new kernel 5.10.52
- talos-systems/talos@70d2505b7 fix: do not require ToVersion to be set when detecting version
- talos-systems/talos@b6c47f866 fix: set the /etc/os-release HOME_URL parameter
- talos-systems/talos@da6f786ca fix: kuberentes => kubernetes typo
- talos-systems/talos@2e463348b fix: pass all logs through the options.Log method
- talos-systems/talos@4e9c5afb6 fix: make ethtool optional in link status controller
- talos-systems/talos@bf61c2cc4 fix: write upgrade logs only to the LogOutput if it's defined
- talos-systems/talos@b358a189b fix: correctly pick route scope for link-local destination
- talos-systems/talos@72b76abfd fix: workaround issues when IPv6 is fully or partially disabled
- talos-systems/talos@6fbec9e0c fix: cache etcd client used for healthchecks
- talos-systems/talos@011e2885e fix: validate bond slaves addressing
- talos-systems/talos@10c28758a fix: ignore DeadlineExceeded error correctly on bootstrap
- talos-systems/talos@6b661114d fix: make COSI runtime history depth smaller
- talos-systems/talos@9bf899bdd fix: make forfeit leadership connect to the right node
- talos-systems/talos@6d13d2cf9 fix: close Kubernetes API client
- talos-systems/talos@aaa36f3b4 fix: ignore 'not a leader' error on forfeit leadership
- talos-systems/talos@22a419367 fix: workaround 'Unauthorized' errors when accessing Kubernetes API
- talos-systems/talos@f5721050d fix: controlplane keyusage
- talos-systems/talos@3d7726613 fix: fill uuid argument correctly in the config download URL
- talos-systems/talos@e883c12b3 fix: make output of `upgrade-k8s` command less scary
- talos-systems/talos@7f8e50de4 fix: restart the merge controllers on conflict
- talos-systems/talos@60d736094 fix: ignore deadline exceeded errors on bootstrap
- talos-systems/talos@ee06dd69f fix: don't print git sha of the release twice in the dashboard
- talos-systems/talos@07fb61e5d fix: issue worker apid certs properly on renewal
- talos-systems/talos@2fa54107b chore: fix tests for disabled RBAC
- talos-systems/talos@78583ba98 fix: don't set bond delay options if miimon is not enabled
- talos-systems/talos@5f6ec3ef6 fix: handle cases when merged resource re-appears before being destroyed
- talos-systems/talos@1e9a0e745 fix: documentation typos
- talos-systems/go-blockdevice@fe24303 fix: perform correct PMBR partition calculations
- talos-systems/go-blockdevice@2ec0c3c fix: preserve the PMBR bootable flag when opening GPT partition
- talos-systems/pkgs@7a29722 fix: set iPXE version properly

### 0.12.3

- talos-systems/talos@07c87a1b6 fix: check trustd API CA on worker nodes
- talos-systems/talos@ce1226b2f fix: check for existence of dhcp6 FQDN first
- talos-systems/talos@ed94d504a fix: containerd log symlink
- talos-systems/talos@7e63e43eb fix: don't marshal clock with SecretsBundle
- talos-systems/talos@7b4a6b361 fix: patch multi nodes support
- talos-systems/talos@110551865 fix: tear down control plane static pods when etcd is stopped
- talos-systems/talos@5824f5024 fix: completely prevent editing resources other than mc
- talos-systems/talos@5700c81bf fix: write KubernetesCACert chmodded 0400 instead of 0500
- talos-systems/talos@a72fa2a93 fix: correctly define example for `extraMounts`
- talos-systems/talos@87c258093 fix: allow updating diskSelector option
- talos-systems/talos@eba00723d fix: don't extract nil IPs in the GCP platform
- talos-systems/talos@3a38f0ded fix: properly handle omitempty fields in the validator
- talos-systems/talos@2e220cb65 fix: validate IP address returned as HTTP response in platform code
- talos-systems/talos@b63a2ea0e fix: don't allow bootstrap if etcd data directory is not empty
- talos-systems/talos@cd0532848 fix: cgroup delegate
- talos-systems/talos@e22301e76 chore: fix arm64 reproducibility issues
- talos-systems/talos@e84e2902c fix: don't support cgroups nesting in process runner
- talos-systems/talos@2cf53fb34 fix: do not set KSPP kernel params in container mode
- talos-systems/talos@4bb84ea0c fix: extramount should have `yaml:",inline"` tag
- talos-systems/talos@e948560be fix: don't panic if the machine config doesn't have network (EM)
- talos-systems/talos@67494923b fix: make sure file mode is same (reproducibility issue)
- talos-systems/talos@e6fa401b6 fix: enable seccomp default profile by default
- talos-systems/talos@a15f01844 fix: move etcd PKI under /system/secrets
- talos-systems/talos@eb02afe18 fix: match correctly routes on the address family
- talos-systems/talos@b68ed1eb8 fix: make route resources ID match closer routing table primary key
- talos-systems/talos@585f63371 fix: correctly handle nodoc for struct fields
- talos-systems/talos@5285a46d7 fix: maintenance mode reason message
- talos-systems/talos@1a2e78a24 fix: update go-blockdevice
- talos-systems/talos@3c566dbc3 fix: remove admission plugins enabled by default from the list
- talos-systems/talos@69ead3735 fix: preserve PMBR bootable flag correctly
- talos-systems/talos@dee630517 fix: align partitions with minimal I/O size
- talos-systems/talos@0b8681b4b fix: resolve several issues with Wireguard link specs
- talos-systems/talos@d4f9804f8 chore: fix typos
- talos-systems/talos@df54584a3 fix: drop linux capabilities
- talos-systems/talos@7332d6369 fix: bump pkgs for new kernel 5.10.52
- talos-systems/talos@70d2505b7 fix: do not require ToVersion to be set when detecting version
- talos-systems/talos@b6c47f866 fix: set the /etc/os-release HOME_URL parameter
- talos-systems/talos@da6f786ca fix: kuberentes => kubernetes typo
- talos-systems/talos@2e463348b fix: pass all logs through the options.Log method
- talos-systems/talos@4e9c5afb6 fix: make ethtool optional in link status controller
- talos-systems/talos@bf61c2cc4 fix: write upgrade logs only to the LogOutput if it's defined
- talos-systems/talos@b358a189b fix: correctly pick route scope for link-local destination
- talos-systems/talos@72b76abfd fix: workaround issues when IPv6 is fully or partially disabled
- talos-systems/talos@6fbec9e0c fix: cache etcd client used for healthchecks
- talos-systems/talos@011e2885e fix: validate bond slaves addressing
- talos-systems/talos@10c28758a fix: ignore DeadlineExceeded error correctly on bootstrap
- talos-systems/talos@6b661114d fix: make COSI runtime history depth smaller
- talos-systems/talos@9bf899bdd fix: make forfeit leadership connect to the right node
- talos-systems/talos@6d13d2cf9 fix: close Kubernetes API client
- talos-systems/talos@aaa36f3b4 fix: ignore 'not a leader' error on forfeit leadership
- talos-systems/talos@22a419367 fix: workaround 'Unauthorized' errors when accessing Kubernetes API
- talos-systems/talos@f5721050d fix: controlplane keyusage
- talos-systems/talos@3d7726613 fix: fill uuid argument correctly in the config download URL
- talos-systems/talos@e883c12b3 fix: make output of `upgrade-k8s` command less scary
- talos-systems/talos@7f8e50de4 fix: restart the merge controllers on conflict
- talos-systems/talos@60d736094 fix: ignore deadline exceeded errors on bootstrap
- talos-systems/talos@ee06dd69f fix: don't print git sha of the release twice in the dashboard
- talos-systems/talos@07fb61e5d fix: issue worker apid certs properly on renewal
- talos-systems/talos@2fa54107b chore: fix tests for disabled RBAC
- talos-systems/talos@78583ba98 fix: don't set bond delay options if miimon is not enabled
- talos-systems/talos@5f6ec3ef6 fix: handle cases when merged resource re-appears before being destroyed
- talos-systems/talos@1e9a0e745 fix: documentation typos
- talos-systems/go-blockdevice@fe24303 fix: perform correct PMBR partition calculations
- talos-systems/go-blockdevice@2ec0c3c fix: preserve the PMBR bootable flag when opening GPT partition
- talos-systems/pkgs@7a29722 fix: set iPXE version properly


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
