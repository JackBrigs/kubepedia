---
id: CONCEPT-TALOS_LOCAL_CLUSTER
type: concept
title: "talosctl cluster — local dev clusters (Docker & QEMU)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: "1.13.6"
verified_at: "2026-07-18"
confidence: verified
aliases:
  - talosctl cluster create
  - talos local dev cluster
  - talos docker cluster
  - talos qemu cluster
  - talosctl cluster destroy
tags:
  - talos
  - development
  - local
sources:
  - type: docs
    path: public/talos/v1.13/talos-guides/install/local-platforms/docker.mdx
    url: https://github.com/siderolabs/docs/blob/main/public/talos/v1.13/talos-guides/install/local-platforms/docker.mdx
    note: "talosctl cluster create docker; auto-writes talosconfig+kubeconfig; container caveats (siderolabs/docs @59a5195)"
  - type: docs
    path: public/talos/v1.13/reference/cli.mdx
    url: https://github.com/siderolabs/talos/blob/v1.13.6/website/content/v1.13/reference/cli.md
    note: "talosctl cluster create flags; --kubernetes-version default 1.36.0, --talos-version v1.13.0"
relations:
  - type: see_also
    target: CONCEPT-TALOS_PROVISIONING
  - type: see_also
    target: CONCEPT-TALOS_TALOSCTL_WORKFLOW
  - type: see_also
    target: CONCEPT-TALOS_K8S_MATRIX
---

# talosctl cluster — local dev clusters (Docker & QEMU)

## Summary

`talosctl cluster create` spins up a full **Talos + Kubernetes** cluster **locally** — for CI, quick
testing, and developing against the exact production Talos version. Two provisioners: **`docker`**
(lightweight, containers) and **`qemu`** (VMs, closer to real Talos). It auto-wires `~/.talos/config`
and `~/.kube/config` at the new cluster. This is the Talos analog of a throwaway kind/minikube — but
running real Talos.

## Context

**Docker provisioner** (`talosctl cluster create docker`):

- Needs Docker ≥18.03 + a recent `talosctl`. On success it points **talosconfig + kubeconfig** at the
  cluster; Talos/K8s APIs map to **random host ports** (`talosctl cluster show`, `talosctl config info`).
- **Caveats:** Talos runs in a container, so node-lifecycle APIs (`upgrade`, `reset`) **don't apply**;
  on macOS/Docker, **VIPs aren't supported**; enable `machine.features.hostDNS.forwardKubeDNSToHost`;
  Flannel-in-Docker may need `sudo modprobe br_netfilter`.

**QEMU provisioner** (`sudo --preserve-env=HOME talosctl cluster create qemu`):

- Linux needs **KVM** (`/dev/kvm`), kernel `CONFIG_NET_SCH_NETEM`+`_INGRESS`, `CAP_SYS_ADMIN`+
  `CAP_NET_ADMIN`, iptables, and CNI plugins (`bridge`,`static`,`firewall`,`tc-redirect-tap`) —
  auto-downloaded to `~/.talos/cni`. macOS requires Apple Silicon.
- Builds a bridge `10.5.0.1` with a **built-in load balancer** on `10.5.0.1` for the K8s API; nodes at
  `10.5.0.2+`. Supports Talos node-lifecycle (real VMs). QEMU-only: `--presets`, `--schematic-id`
  (Image Factory), `--omni-api-endpoint` (connect to Omni — [[CONCEPT-TALOS_OMNI]]).

**Key flags** (`talosctl cluster create`, v1.13 defaults):

- Topology: `--controlplanes` (1), `--workers`, `--with-init-node`.
- Versions: `--kubernetes-version` (default **1.36.0**), `--talos-version` (**v1.13.0**),
  `--install-image`.
- Network: `--cidr` (10.5.0.0/24), `--control-plane-port` (6443), `--use-vip`, `--kubeprism-port`
  (7445), `--dns-domain`, `--wireguard-cidr`.
- Resources (QEMU): `--cpus`/`--memory` (2.0 / 2GiB), `--disk` (6144MB), `--extra-disks`,
  `--user-volumes`.
- Config: `--config-patch[-control-plane|-worker]`, `--custom-cni-url`, `--registry-mirror`,
  `--with-firewall`. Encryption: `--encrypt-state`, `--encrypt-ephemeral`,
  `--disk-encryption-key-types` (uuid, kms — [[CONCEPT-TALOS_DISK_ENCRYPTION]]).

**Multiple clusters / teardown:** each needs a unique `--name` (default `talos-default`) and `--cidr`;
switch with `--context`; destroy with `talosctl cluster destroy [--name …]`. Set
`--kubernetes-version` from the Talos version's supported window ([[CONCEPT-TALOS_K8S_MATRIX]]).

## References

- `siderolabs/docs` `.../local-platforms/{docker,qemu}.mdx` (@59a5195); `talosctl cluster create` CLI
  reference (@v1.13.6). Provisioning [[CONCEPT-TALOS_PROVISIONING]]; talosctl workflow
  [[CONCEPT-TALOS_TALOSCTL_WORKFLOW]]; matrix [[CONCEPT-TALOS_K8S_MATRIX]].
