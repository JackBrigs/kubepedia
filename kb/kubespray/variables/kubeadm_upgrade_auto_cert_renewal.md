---
id: VARIABLE-KUBEADM_UPGRADE_AUTO_CERT_RENEWAL
type: variable
title: kubeadm_upgrade_auto_cert_renewal
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - kubeadm_upgrade_auto_cert_renewal
tags:
  - kubeadm
  - upgrade
  - certificates
sources:
  - type: code
    path: roles/kubernetes/control-plane/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/defaults/main/main.yml
    note: "Defines kubeadm_upgrade_auto_cert_renewal: true"
relations: []
---

# kubeadm_upgrade_auto_cert_renewal

## Summary
Controls whether kubeadm automatically renews all certificates during a control-plane upgrade. Default is `true`; set to `false` to upgrade the cluster without renewing certificates.

## Implementation
Defined in `roles/kubernetes/control-plane/defaults/main/main.yml` as:

```yaml
kubeadm_upgrade_auto_cert_renewal: true
```

The value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0 (line 241 in v2.29.0/v2.29.1, line 244 in v2.30.0/v2.31.0).

## Compatibility
Applies to Kubespray v2.29.0 through v2.31.0. Consumed during control-plane upgrade tasks in the kubernetes control-plane role.

## References
- roles/kubernetes/control-plane/defaults/main/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
