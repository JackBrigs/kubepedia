---
id: PRACTICE-PROXY
type: best_practice
title: Kubespray environment proxy configuration (http_proxy, no_proxy)
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - Environment proxy
tags:
  - proxy
  - networking
sources:
  - type: docs
    path: docs/advanced/proxy.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/advanced/proxy.md
    note: "Configuring HTTP/HTTPS proxy, custom CA, and no_proxy generation for cluster nodes"
relations: []
---

# Kubespray environment proxy configuration (http_proxy, no_proxy)

## Summary
Kubespray configures an environment proxy for cluster nodes via `http_proxy`/`https_proxy`. When set, all nodes and the loadbalancer are automatically excluded from the proxy through a generated `no_proxy` variable (built in `roles/kubespray_defaults/tasks/no_proxy.yml`). You can extend, fully override, or narrow that exclusion list.

## Context
Applies when deploying behind a corporate proxy. Involves inventory variables `http_proxy`, `https_proxy`, `https_proxy_cert_file`, `no_proxy`, `additional_no_proxy`, and `no_proxy_exclude_workers`. The auto-generated `no_proxy` covers all cluster nodes and the loadbalancer unless overridden.

## Implementation
### Set the proxy
- `http_proxy: "http://example.proxy.tld:port"`
- `https_proxy: "http://example.proxy.tld:port"`

### Custom CA
- `https_proxy_cert_file: /path/to/host/custom/ca.crt` — the CA must already be present on each target node.

### no_proxy handling
- Default: `no_proxy` is generated automatically to exclude all nodes and the loadbalancer.
- Add extra exclusions to the generated list: `additional_no_proxy: "additional_host1,additional_host2"`.
- Fully override generation: set `no_proxy: "node1,node1_ip,node2,node2_ip,...additional_host"` — when set explicitly, no node or loadbalancer addresses are auto-added.
- Exclude workers from `no_proxy`: `no_proxy_exclude_workers: true`. By default workers are in `no_proxy`, so adding/removing workers restarts the docker engine on all nodes (all pods restart). Setting this to `true` includes only control plane nodes in `no_proxy`, avoiding that churn.

## References
- docs/advanced/proxy.md (tag v2.31.0 1c9add4)
