---
id: VARIABLE-CILIUM_CERTGEN_ARGS
type: variable
title: cilium_certgen_args
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - cilium_certgen_args
tags:
  - cilium
  - hubble
  - certificates
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "Argument mapping for the Cilium certgen job (Hubble CA and certs)"
relations: []
---

# cilium_certgen_args

## Summary
A dictionary of arguments passed to the Cilium certgen job, which generates the Hubble CA and server/relay certificates. It configures the namespace, CA reuse/generation, validity durations, and per-certificate common names and secret names.

## Implementation
Defined in `roles/network_plugin/cilium/defaults/main.yml` as a mapping. The default value is unchanged across v2.29.0, v2.29.1, v2.30.0, and v2.31.0:

```yaml
cilium_certgen_args:
  cilium-namespace: kube-system
  ca-reuse-secret: true
  ca-secret-name: hubble-ca-secret
  ca-generate: true
  ca-validity-duration: 94608000s
  hubble-server-cert-generate: true
  hubble-server-cert-common-name: '*.{{ cilium_cluster_name }}.hubble-grpc.cilium.io'
  hubble-server-cert-validity-duration: 94608000s
  hubble-server-cert-secret-name: hubble-server-certs
  hubble-relay-client-cert-generate: true
  hubble-relay-client-cert-common-name: '*.{{ cilium_cluster_name }}.hubble-grpc.cilium.io'
  hubble-relay-client-cert-validity-duration: 94608000s
  hubble-relay-client-cert-secret-name: hubble-relay-client-certs
  hubble-relay-server-cert-generate: false
```

## Compatibility
Kubespray >=v2.29.0 <=v2.31.0. Applies only when Cilium is the selected CNI (relevant to Hubble). References `cilium_cluster_name` in the certificate common names.

## References
- roles/network_plugin/cilium/defaults/main.yml
- Tags: v2.29.0 9991412, v2.29.1 0c6a295, v2.30.0 f4ccdb5, v2.31.0 1c9add4.
