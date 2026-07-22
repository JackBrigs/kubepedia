---
id: TROUBLE-CONTAINERD_PROXY_NOT_REMOVED
type: troubleshooting
title: "Removing http_proxy from inventory does not disable the proxy — the containerd drop-in stays"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-22"
confidence: verified
aliases:
  - how to disable proxy for containerd kubespray
  - containerd still uses proxy after removing http_proxy
  - http-proxy.conf containerd.service.d
  - kubespray remove proxy settings
  - containerd ImagePullBackOff after disabling proxy
tags:
  - troubleshooting
  - containerd
  - proxy
  - container-runtime
sources:
  - type: code
    path: roles/container-engine/containerd/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.1/roles/container-engine/containerd/tasks/main.yml
    note: "'Containerd | Write containerd proxy drop-in' is gated on `when: http_proxy is defined or https_proxy is defined` — identical at v2.29.0, v2.29.1, v2.30.0, v2.31.0; there is no removal task"
  - type: code
    path: roles/reset/tasks/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/reset/tasks/main.yml
    note: "the only place in the tree that deletes containerd.service.d/http-proxy.conf (and the cri-o one) — i.e. a full cluster reset"
  - type: code
    path: roles/container-engine/containerd/templates/http-proxy.conf.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/container-engine/containerd/templates/http-proxy.conf.j2
    note: "renders [Service] Environment=HTTP_PROXY/HTTPS_PROXY/NO_PROXY from the inventory variables"
  - type: code
    path: roles/container-engine/meta/main.yml
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.29.1/roles/container-engine/meta/main.yml
    note: "container-engine/containerd carries tags 'container-engine' and 'containerd' — the run tags that reach this task"
relations:
  - type: see_also
    target: COMPONENT-CONTAINERD
  - type: see_also
    target: CONFIG-PROXY
  - type: see_also
    target: CONCEPT-DESTRUCTIVE_ACTIONS
  - type: see_also
    target: TAG-CONTAINERD
---

# Removing http_proxy from inventory does not disable the proxy — the containerd drop-in stays

## Summary

To put containerd behind a proxy you set `http_proxy`/`https_proxy` and Kubespray writes
`{{ containerd_systemd_dir }}/http-proxy.conf` (`/etc/systemd/system/containerd.service.d/http-proxy.conf`).
To turn it **off** operators remove those variables and re-run — and the run reports success
while the proxy is still in effect. The task that writes the drop-in is **conditional on the
variables being defined**, so removing them makes the task *skip*; nothing deletes the file.
Outside `reset.yml`, Kubespray never removes it.

## Problem

- `http_proxy`/`https_proxy` are gone from inventory, `cluster.yml` (or the `containerd`
  tag) ran green, but containerd still goes through the proxy.
- `systemctl show containerd -p Environment` still lists `HTTP_PROXY=…`/`HTTPS_PROXY=…`.
- Typical trigger for noticing: the proxy is decommissioned or firewalled, and image pulls
  start failing (`ImagePullBackOff`) on nodes that look otherwise healthy.
- Same shape for **cri-o** (`/etc/systemd/system/crio.service.d/http-proxy.conf`, same
  `when:`). **Docker differs** — its role does remove the drop-in, but only in a `rescue:`
  block when Docker fails to start, not as a normal path.

## Context

- Verified identical at **v2.29.0, v2.29.1, v2.30.0, v2.31.0**:

  ```yaml
  - name: Containerd | Write containerd proxy drop-in
    template:
      src: http-proxy.conf.j2
      dest: "{{ containerd_systemd_dir }}/http-proxy.conf"
    notify: Restart containerd
    when: http_proxy is defined or https_proxy is defined
  ```

- `roles/reset/tasks/main.yml` is the **only** file in the tree that deletes
  `containerd.service.d/http-proxy.conf` — that is a full cluster teardown, not an option
  for this.
- The variables may not live in the inventory repository at all: they are just as often
  passed as extra vars from the CI/AWX job template, or were set once during install and
  never version-controlled. In that case the drop-in on the node is the *only* remaining
  trace, and no future run will recreate it.
- Applies to the same class of Kubespray behaviour as
  [[CONCEPT-DESTRUCTIVE_ACTIONS]] read from the other side: the roles apply, they rarely
  un-apply.

## Diagnostics

- What the unit actually has (authoritative, includes drop-ins):
  `systemctl show containerd -p Environment`
- The file itself: `cat /etc/systemd/system/containerd.service.d/http-proxy.conf`
- Whether a proxy is still defined anywhere for the run: check inventory **and** the job's
  extra vars / survey (AWX: Job Template → Variables, plus Inventory/group variables held
  in the AWX UI rather than in git).
- Whether the node can reach registries without the proxy — test **before** removing it:
  `crictl pull <registry>/<image>:<tag>` on one node.

## Known Issues

- **Fix (per node, ordered).** Remove the source first so nothing re-creates the file, then
  delete it and reload the unit:
  1. drop `http_proxy`/`https_proxy`/`no_proxy` from inventory **and** from the job's extra
     vars;
  2. delete `/etc/systemd/system/containerd.service.d/http-proxy.conf`;
  3. `systemctl daemon-reload && systemctl restart containerd`;
  4. re-run Kubespray scoped to the runtime to converge the rest of the config (AWX: job
     tag `containerd`, Limit the host — see below).
- **Do it node by node.** The containerd role runs in `cluster.yml`'s first play
  (`hosts: k8s_cluster:etcd`) which has **no `serial`**, so an unlimited run restarts
  containerd on every node in parallel. Restarting containerd does not kill running
  containers (their shims are separate), but the node is briefly `NotReady` and starts no
  pods meanwhile.
- **Job tags:** `containerd` is the narrow tag, `container-engine` the broad one
  (`roles/container-engine/meta/main.yml`).
- **Order matters for connectivity.** If the proxy was the node's only route to the
  registries, removing it turns every *new* pull into `ImagePullBackOff` while already
  cached images keep working — the failure surfaces later, on the next new pod, not during
  the run. Verify direct pull access first.

## References

- `roles/container-engine/containerd/tasks/main.yml` + `templates/http-proxy.conf.j2` and
  `roles/container-engine/meta/main.yml` (tags) read at `v2.29.1`, condition re-checked at
  `v2.29.0`/`v2.30.0`/`v2.31.0`; `roles/reset/tasks/main.yml` (the only deletion);
  cri-o equivalent in `roles/container-engine/cri-o/tasks/main.yaml`; docker's
  `rescue:`-only cleanup in `roles/container-engine/docker/tasks/main.yml`.
  Runtime: [[COMPONENT-CONTAINERD]]; proxy configuration: [[CONFIG-PROXY]].
