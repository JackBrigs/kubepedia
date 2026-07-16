---
id: CONCEPT-CILIUM_HUBBLE
type: concept
title: "Cilium Hubble observability in Kubespray"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - hubble
  - cilium observability
  - cilium_enable_hubble
  - hubble ui
  - hubble metrics
tags:
  - cilium
  - hubble
  - observability
  - networking
sources:
  - type: code
    path: roles/network_plugin/cilium/defaults/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/network_plugin/cilium/defaults/main.yml
    note: "cilium_enable_hubble / _ui / _metrics / hubble_metrics defaults (tag v2.31.0)"
relations:
  - type: see_also
    target: COMPONENT-CILIUM
  - type: see_also
    target: CONCEPT-CILIUM_DATAPATH
  - type: see_also
    target: TROUBLE-CILIUM_CONFIG_VALIDATION
---

# Cilium Hubble observability in Kubespray

## Summary

**Hubble** is Cilium's network-observability layer (flow visibility, service maps,
metrics). It is **off by default** in Kubespray; enabling it turns on the Hubble server,
optionally the UI and Prometheus metrics. Useful for debugging connectivity/policy — you
see allowed/denied flows without tcpdump.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0`, `kube_network_plugin: cilium`.
- Defaults (`cilium/defaults/main.yml`):
  - `cilium_enable_hubble: false` — master switch (Hubble server/Relay).
  - `cilium_enable_hubble_ui: "{{ cilium_enable_hubble }}"` — UI follows the master switch
    by default.
  - `cilium_enable_hubble_metrics: false` — expose Hubble Prometheus metrics.
  - `cilium_hubble_metrics: []` — which metric sets to export (e.g. `dns`, `drop`,
    `flow`, `http`); empty means none even if metrics are "enabled".
  - `cilium_hubble_install: false` — install the Hubble components.

## Implementation

- Set `cilium_enable_hubble: true` to deploy Hubble; the UI comes along unless you set
  `cilium_enable_hubble_ui: false`.
- For metrics: set `cilium_enable_hubble_metrics: true` **and** populate
  `cilium_hubble_metrics` with the metric sets you want — one without the other yields no
  useful data.
- `cilium_hubble_event_buffer_capacity`, if set, must be a **power of two minus one**
  (`2^n − 1`) — an invalid value fails the Cilium preflight
  ([[TROUBLE-CILIUM_CONFIG_VALIDATION]]).
- Observe flows with the `hubble` CLI / UI (allowed vs dropped, by identity/policy) — the
  fastest way to see *why* Cilium dropped a connection.

## Compatibility

- Hubble adds agents/relay + (optional) UI pods — modest overhead; enable where you need
  observability rather than everywhere by default.
- Hubble metrics integrate with the cluster Prometheus stack; scrape ports must be
  reachable (Cilium metrics ports — [[TROUBLE-FIREWALL_PORTS_BLOCKED]]).
- Hubble reflects the datapath it observes ([[CONCEPT-CILIUM_DATAPATH]]); it is a
  read-only observability layer, not a policy control.

## References

- `cilium/defaults/main.yml` (Hubble knobs) at tag `v2.31.0`. Component:
  [[COMPONENT-CILIUM]]; datapath: [[CONCEPT-CILIUM_DATAPATH]].
