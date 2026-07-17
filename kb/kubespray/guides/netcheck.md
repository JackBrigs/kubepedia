---
id: PRACTICE-NETCHECK
type: best_practice
title: Network Checker application (netchecker) in Kubespray
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - netchecker
tags:
  - networking
  - diagnostics
  - dns
sources:
  - type: docs
    path: docs/advanced/netcheck.md
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/docs/advanced/netcheck.md
    note: "Deploying and using the k8s-netchecker connectivity checker"
relations:
  - type: see_also
    target: CONCEPT-COMPONENT_VERSION_SELECTION
---

# Network Checker application (netchecker) in Kubespray

## Summary
Kubespray can optionally deploy the Network Checker application (`mirantis/k8s-netchecker`) to verify pod-to-pod connectivity via cluster IP and DNS resolution across the cluster. It runs a server plus agents that periodically probe connectivity; results are read on demand via an HTTP endpoint. Deployment is opt-in and off by default.

## Context
Applies when you want an in-cluster connectivity/DNS diagnostic. Enabled with `deploy_netchecker` (defaults to false). The app pulls a 3rd-party image (`mirantis/k8s-netchecker`), which matters for air-gapped mirrors. Agents cover both standard and host-network pods; check history lives in the agents' application logs. Kubespray only deploys the app — it does not invoke the checks.

## Implementation
Enable with `deploy_netchecker: true`. Related variables:
```yaml
netchecker_port: 31081
agent_report_interval: 15
netcheck_namespace: default
```

Get the cluster-wide connectivity report from any node:
```shell
curl http://localhost:31081/api/v1/connectivity_check
```

DNS caveat: the app verifies FQDN resolution built only from `netcheck_namespace` + `dns_domain`, e.g. `netchecker-service.default.svc.cluster.local`. If you deploy to a non-default namespace, also adjust the `searchdomains` var so the resulting search-domain records include that namespace, for example:
```yaml
search: foospace.cluster.local default.cluster.local ...
nameserver: ...
```

## References
- docs/advanced/netcheck.md (tag v2.31.0 1c9add4)
