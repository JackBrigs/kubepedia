---
id: CONFIG-PROXY
type: configuration
title: "HTTP(S) proxy configuration in Kubespray"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - http_proxy
  - https_proxy
  - no_proxy
  - additional_no_proxy
  - corporate proxy kubespray
  - proxy behind firewall
tags:
  - operations
  - proxy
  - networking
  - configuration
sources:
  - type: code
    path: roles/kubespray_defaults/defaults/main/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubespray_defaults/defaults/main/main.yml
    note: "proxy_env / no_proxy assembly, https_proxy_cert_file (tag v2.31.0)"
  - type: code
    path: inventory/sample/group_vars/all/all.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/inventory/sample/group_vars/all/all.yml
    note: "http_proxy/https_proxy/additional_no_proxy/skip_http_proxy_on_os_packages knobs (tag v2.31.0)"
relations:
  - type: see_also
    target: TROUBLE-CONTAINERD_NO_PROXY_CHAR_ARRAY
  - type: see_also
    target: CONCEPT-SAMPLE_INVENTORY_LAYOUT
  - type: see_also
    target: PRACTICE-OFFLINE_ENVIRONMENT
---

# HTTP(S) proxy configuration in Kubespray

## Summary

Behind a corporate/egress proxy, set `http_proxy`/`https_proxy` in inventory and Kubespray
propagates them to package managers, the container runtime, and downloads. Critically,
Kubespray **auto-builds `no_proxy`** with the cluster-internal addresses so in-cluster
traffic isn't sent to the proxy — you extend it with `additional_no_proxy` rather than
overriding it.

## Configuration

Set in `group_vars/all/all.yml` (see [[CONCEPT-SAMPLE_INVENTORY_LAYOUT]]):

| Variable | Purpose |
|----------|---------|
| `http_proxy` / `https_proxy` | the proxy URLs (empty by default) |
| `https_proxy_cert_file` | custom CA cert for the HTTPS proxy (sets `SSL_CERT_FILE`) |
| `no_proxy` | **auto-composed** by Kubespray with cluster-internal addresses — do not blindly override |
| `additional_no_proxy` | **your** extra no-proxy entries (internal registries, mirrors, DNS names) — the safe way to extend |
| `skip_http_proxy_on_os_packages` | `true` to *not* proxy OS package repos (internal repos) |

- Kubespray combines these into `proxy_env` (`HTTP_PROXY`/`HTTPS_PROXY`/`NO_PROXY` +
  lowercase, plus `SSL_CERT_FILE` when a proxy CA is set) and applies it to tasks, the
  container runtime, and downloads.
- The auto-built `no_proxy` covers cluster-internal targets (nodes, service/pod networks,
  cluster domain, localhost) so API/etcd/pod traffic bypasses the proxy — extend it, don't
  replace it.

## Compatibility

- Applies to Kubespray `v2.29.0`–`v2.31.0`.
- **Add internal endpoints to `additional_no_proxy`**: private registries, package
  mirrors, and any DNS name that must not go through the proxy — otherwise pulls/updates
  route to the proxy and fail.
- **Debian/Ubuntu:** apt honours `no_proxy` differently — the sample notes you may need to
  set `no_proxy` explicitly for apt to reach an internal source; check the OS caveat.
- A malformed `no_proxy` can render into containerd's config incorrectly — see
  [[TROUBLE-CONTAINERD_NO_PROXY_CHAR_ARRAY]].
- Combine with offline mirrors for fully air-gapped installs
  ([[PRACTICE-OFFLINE_ENVIRONMENT]]) — proxy and offline are different strategies; pick per
  environment.

## References

- `proxy_env` / `no_proxy` assembly and `https_proxy_cert_file` in `main.yml`; proxy knobs
  in `group_vars/all/all.yml` at tag `v2.31.0`. Offline: [[PRACTICE-OFFLINE_ENVIRONMENT]].
