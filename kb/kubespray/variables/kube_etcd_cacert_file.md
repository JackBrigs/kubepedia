---
id: VARIABLE-KUBE_ETCD_CACERT_FILE
type: variable
title: kube_etcd_cacert_file
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kube_etcd_cacert_file
tags:
  - etcd
  - certificates
  - control-plane
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "etcd CA certificate filename; default ca.pem"
relations: []
---

# kube_etcd_cacert_file

## Summary
The filename of the etcd CA certificate referenced by the control plane and CNI plugins. Default in the defaults files: `ca.pem`. Note: at runtime the preinstall role overrides the fact to `etcd/ca.crt` (see below), so the effective value during a run is `etcd/ca.crt`.

## Implementation
Declared as `kube_etcd_cacert_file: ca.pem` in several defaults: `roles/kubernetes/control-plane/defaults/main/main.yml`, `roles/network_plugin/calico_defaults/defaults/main.yml`, and `roles/network_plugin/cilium/defaults/main.yml`. It is rendered as the etcd `caFile` in the kubeadm config templates (`kubeadm-config.v1beta3.yaml.j2` through v2.30.0, `kubeadm-config.v1beta4.yaml.j2`) and used by Calico/Cilium install tasks. However, `roles/kubernetes/preinstall/tasks/0020-set_facts.yml` sets the fact `kube_etcd_cacert_file: "etcd/ca.crt"`, which takes precedence at runtime. This behavior (default `ca.pem`, preinstall override `etcd/ca.crt`) is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0.

## Compatibility
Available in Kubespray v2.29.0 through v2.31.0. Related: `etcd_cert_dir`, `kube_etcd_cert_file`, `kube_etcd_key_file`.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- roles/kubernetes/preinstall/tasks/0020-set_facts.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
