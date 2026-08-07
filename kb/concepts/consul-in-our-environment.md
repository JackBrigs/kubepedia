---
id: CONCEPT-CONSUL_LOCAL
type: concept
title: "Consul here: front hosts are servers, everything else is a client, one DC per site"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: "1.19.2, 1.21.1"
verified_at: "2026-08-07"
confidence: verified
aliases:
  - consul
  - consul maint
  - вывод ноды из consul
  - consul maintenance
  - нода не в каталоге consul
  - consul_envoy_gateway
  - prepared query consul
  - consul датацентр
tags:
  - consul
  - discovery
  - operations
  - maintenance
  - dns
sources:
  - type: doc
    path: ~/Desktop/work/playbook/docs/consul.md
    note: "наша топология: серверы на front, клиенты везде; API 8500, DNS 8600; теги и prepared query; добавление DC"
  - type: measurement
    path: sc-ams1-cons-prod-kube-node4, sc-ams1-cons-test-kube-master1
    note: "consul 1.21.1, конфиг /etc/consul.d/, ACL enabled с default_policy=allow, DC consult; сервис consult-envoy-gateway на 443"
  - type: doc
    path: ~/Desktop/work/playbook/consul-reg-services.yml
    note: "регистрация сервисов идёт PUT на /v1/agent/service/register через ansible.builtin.uri"
relations:
  - type: see_also
    target: CONCEPT-LOCAL_SOURCES
  - type: see_also
    target: PRACTICE-ANSIBLE_ROLE_RULES
  - type: see_also
    target: PRACTICE-RUNBOOK_NODE_MAINTENANCE
---

## Summary

Consul is the discovery layer these clusters depend on: services register with the
local agent, health checks decide whether they stay in DNS, and clients resolve
services without knowing which host runs them. Kubernetes nodes participate as
consul **clients** — which means a node can be perfectly healthy to Kubernetes and
simultaneously invisible, or wrongly visible, to everything that resolves through
consul.

## Context

**Topology.** Front hosts run consul in server mode; everything else — Kubernetes
nodes, www, ceph, vault, clickhouse — runs as a client. A datacenter has exactly one
leader, elected among the servers; the leader accepts all writes.

**Two interfaces.** The HTTP API on **8500** is used to register services on the
local node; DNS on **8600** resolves them. DNS queries for the `.consul` zone are
forwarded to `127.0.0.1:8600` by dnsmasq or unbound.

**Identifiers.** `service_id` must be unique; `service_name` need not be — several
instances sharing a name is exactly what gives round-robin through DNS.

**Cross-DC routing.** A name ending in `.consul` is resolved within the local
datacenter. A name containing `.query` uses a prepared query: the local DC first,
then a fallback to another DC over the WAN interface. This is how geo-failover is
built, and chains of arbitrary length between datacenters are possible.

**Verified on the running fleet (2026-08-07):** consul 1.21.1 on the newer hosts and
1.19.2 on older ones, configuration in `/etc/consul.d/` (not `/etc/consul.json` as
the team document still says), datacenter `consult`, ACL enabled with
`default_policy = allow` — so the local API answers without a token.

## Implementation

**Registration is an API call, not a config file.** Services are registered by
`PUT /v1/agent/service/register` against the local agent — the pattern used
throughout the playbook repository via `ansible.builtin.uri`. A registration carries
its own health checks; a failing check removes the service from DNS answers while
leaving it registered.

**Maintenance mode is the supported way to take a node out.**

```
PUT /v1/agent/maintenance?enable=true&reason=<текст>
PUT /v1/agent/maintenance?enable=false
```

Every service on the node is marked `critical` and disappears from DNS and load
balancing; the registration itself survives, so nothing needs re-registering on the
way back. The flag shows up as a check with `CheckID = _node_maintenance` — that is
the reliable way to confirm the state actually reached the catalog.

Reading current state:

```bash
consul maint                                # что сейчас в обслуживании
consul members                              # состав DC
consul catalog services                     # какие сервисы известны
consul catalog nodes -service=<имя>         # кто отдаёт конкретный сервис
```

## Known Issues

**Kubernetes health and consul health are independent.** A node can be `Ready` in
Kubernetes and absent from the consul catalog, or `NotReady` while consul still
advertises its services. Neither system knows about the other. Taking a node out for
maintenance therefore requires two separate actions, and the consul one is the one
that gets forgotten.

**A reinstalled node loses its agent silently.** Observed on a gateway node: the
systemd unit remained while the binary and `/etc/consul.d/` were gone, and the node
vanished from the catalog. Nothing in Kubernetes reports this. Check
`GET /v1/agent/self`, not the presence of `/usr/bin/consul`.

**Not every node runs consul.** In one test cluster only the control-plane nodes and
the gateway nodes carry an agent; plain workers have no unit at all. Any automation
that touches consul must tolerate hosts without it instead of failing on them.

**The team document has drifted.** `docs/consul.md` describes `/etc/consul.json` and
a `server: true/false` key in it; the running fleet uses `/etc/consul.d/consul.hcl`
with `server = false`. Treat the document as authoritative for intent and topology,
and the running hosts as authoritative for paths.

**`default_policy = allow` is why nothing asks for a token.** This is a property of
the current configuration, not a guarantee. Automation should not assume it
permanently.

## References

- `playbook/docs/consul.md` — topology, DC/query mechanics, procedure for adding a DC
- `playbook/consul-reg-services.yml` — registration through the HTTP API
- `playbook/update-opcache.yml` — existing example of wrapping work in maintenance mode
- HashiCorp API documentation for `/v1/agent/maintenance` and `/v1/health/node/<node>`
