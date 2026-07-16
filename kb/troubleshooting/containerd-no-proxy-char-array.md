---
id: TROUBLE-CONTAINERD_NO_PROXY_CHAR_ARRAY
type: troubleshooting
title: "containerd NO_PROXY rendered as a character array behind a proxy"
status: active
kubespray_version: ">=v2.29.0 <=v2.30.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: verified
aliases:
  - no-proxy-char-array
  - containerd-http-proxy-conf
tags:
  - containerd
  - proxy
  - no-proxy
sources:
  - type: github_pr
    url: https://github.com/kubernetes-sigs/kubespray/pull/12981
    note: "Master fix: replaces the custom Jinja loop with flatten + join and uses run_once"
  - type: github_pr
    url: https://github.com/kubernetes-sigs/kubespray/pull/13110
    note: "Backport to release-2.29 (v2.29.2)"
  - type: github_issue
    url: https://github.com/kubernetes-sigs/kubespray/issues/12977
    note: "Original issue report"
relations: []
---

# containerd NO_PROXY rendered as a character array behind a proxy

## Summary
With a proxy configured (`http_proxy`/`https_proxy` + `additional_no_proxy`), the file `/etc/systemd/system/containerd.service.d/http-proxy.conf` is generated incorrectly: `NO_PROXY` is emitted as a list of individual characters (`['1','7','2','.',...]`) instead of a comma-separated string. The proxy for containerd is configured wrongly, breaking clusters running behind a proxy / in air-gapped environments. Fixed in v2.29.2 and v2.31.0; workaround is to set `no_proxy` manually as a correct comma-separated string.

## Problem
The `no_proxy` value ends up rendered as a character array, e.g.:

```
"NO_PROXY=['1', '7', '2', '.', '3', '1', '.', '1', '3', '2', '.', '8', '8', ...]"
```

instead of the expected:

```
"NO_PROXY=172.31.132.88,...,svc,svc.cluster.local"
```

Because the malformed value is written into the containerd systemd drop-in unit, proxying for containerd is misconfigured.

## Context
- Affected Kubespray versions: v2.29.0, v2.29.1, v2.30.0.
- Fixed versions: v2.29.2 (release-2.29 backport) and v2.31.0 (master).
- Not fixed in v2.30.0 — the master fix #12981 was merged after the v2.30.0 tag (2026-01-30) and there is no backport to release-2.30.
- Trigger conditions: a proxy is configured and the effective `no_proxy` is assembled by Kubespray; whether it manifests depends on the native-Jinja templating of the Ansible version in use (reporter reproduced it on v2.30 with ansible-core 2.17.5; v2.29.1 requires Ansible >= 2.17.3, which matches the conditions).

## Diagnostics
- Inspect the generated drop-in: `cat /etc/systemd/system/containerd.service.d/http-proxy.conf` — a broken `NO_PROXY=['1','7','2',...]` value confirms the issue.
- Check the tag code: in v2.29.1 and v2.30.0 the vulnerable implementation is `roles/network_facts/tasks/no_proxy.yml` — `no_proxy_prepare: >-` folded scalar with `{%- for item in (groups[cluster_or_control_plane] + ...) | unique -%}` and `delegate_to: localhost`. The template `roles/container-engine/containerd/templates/http-proxy.conf.j2` substitutes `NO_PROXY={{ no_proxy }}` directly, so a malformed value flows into the unit file.

## Known Issues
- Root cause: `no_proxy` is built by a custom Jinja loop in `roles/network_facts/tasks/no_proxy.yml` (fact `no_proxy_prepare`, folded scalar `>-` with a `for item in ...` loop, then `delegate_to: localhost`). Under the native-Jinja templating of newer Ansible versions the result is in some cases interpreted as an iterable string (a character array) rather than a single string. Per the fix author, the problem appears "starting from version 2.29" due to a change in Ansible templating.
- Fix: PR #12981 (merged to master) removed the custom Jinja loop, replacing it with `flatten` + `join` filters and switching to `run_once` instead of delegating to localhost. Backport to release-2.29: PR #13110. Original issue: #12977. In v2.31.0 `no_proxy.yml` was removed and the logic moved to `roles/network_facts/tasks/main.yaml` with `flatten`+`join`, i.e. fixed there.
- Workaround (before upgrading): set `no_proxy` manually to a correct comma-separated string.

## References
- https://github.com/kubernetes-sigs/kubespray/pull/12981
- https://github.com/kubernetes-sigs/kubespray/pull/13110
- https://github.com/kubernetes-sigs/kubespray/issues/12977
- Migrated from Kubepedia 0.1.0 cache: containerd-no-proxy-char-array-v2.29.1.md, containerd-no-proxy-char-array-v2.30.0.md
