---
id: TROUBLE-ENVOY_XDS_CONTROLLER
type: troubleshooting
title: "envoy-xds-controller: Envoy not receiving config — CRD errors, node-id mismatch, ADS connection, dex"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=0.17.1"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - envoy xds no config
  - envoy node id mismatch
  - exc crd invalid
  - envoy ads not connecting
  - envoy-xds-controller
tags: [troubleshooting, networking, envoy, xds]
sources:
  - type: external
    path: kaasops envoy-xds-controller
    url: https://github.com/kaasops/envoy-xds-controller
    note: "serves Envoy xDS/ADS from CRDs; Envoy node-id must match the controller's config; data-plane image user-supplied"
relations:
  - type: see_also
    target: CONCEPT-ADDON_ENVOY_XDS_CONTROLLER
  - type: see_also
    target: CONCEPT-CILIUM_ENVOY
---

# envoy-xds-controller: Envoy not receiving config — CRD errors, node-id mismatch, ADS connection, dex

## Summary

The kaasops envoy-xds-controller (exc) serves **Envoy xDS/ADS** config built from Kubernetes CRDs. When
an Envoy has no listeners/routes, it's usually an **invalid CRD** the controller rejected, an Envoy
**node-id** that doesn't match any controller config, or the Envoy's **ADS connection** to the controller
failing. App `v0.17.1`; the Envoy data-plane image is **user-supplied**.

## Problem

- Envoy comes up but serves nothing (no listeners), or `503`/`no healthy upstream`; the controller logs
  reject a CRD, or the Envoy logs can't reach the xDS server.

## Context

- envoy-xds-controller `0.17.1` ([[CONCEPT-ADDON_ENVOY_XDS_CONTROLLER]]); related to Envoy control-plane
  concepts ([[CONCEPT-CILIUM_ENVOY]] covers Envoy internals). Runs in multiple envs (exc/exc-stage/
  exc-test), each paired with dex for the UI.
- **CRD invalid:** a bad VirtualService/Listener/Cluster CRD is dropped by the controller, so that config
  never reaches Envoy.
- **node-id mismatch:** Envoy identifies with a **node id/cluster**; the controller only sends config
  matching a known node — a mismatched `--service-node` gets an empty snapshot.
- **ADS connection:** Envoy's xDS cluster must point at the controller's gRPC service; wrong address/TLS
  → Envoy never fetches config.
- **dex/UI:** the management UI auth via dex is separate from data-plane config — UI login issues don't
  affect Envoy config and vice-versa.

## Diagnostics

```bash
kubectl -n <ns> logs deploy/envoy-xds-controller | tail          # CRD validation / snapshot errors
kubectl -n <ns> get virtualservice,listener,cluster,route 2>/dev/null
kubectl -n <ns> exec <envoy-pod> -- curl -s localhost:19000/config_dump | head   # what Envoy actually has
kubectl -n <ns> exec <envoy-pod> -- curl -s localhost:19000/server_info
```

## Known Issues

- **CRD invalid — fix:** `describe` the rejected CRD; correct the schema/reference so the controller
  includes it in the snapshot.
- **node-id — fix:** align Envoy's `--service-node`/`--service-cluster` with the controller's expected
  node id.
- **ADS — fix:** point Envoy's bootstrap xDS cluster at the controller's gRPC endpoint (address + TLS);
  confirm `config_dump` starts populating.
- **Data-plane image — fix:** supply a compatible Envoy image (not pinned by the chart).

## References

- kaasops envoy-xds-controller. Addon [[CONCEPT-ADDON_ENVOY_XDS_CONTROLLER]]; Envoy internals
  [[CONCEPT-CILIUM_ENVOY]].
