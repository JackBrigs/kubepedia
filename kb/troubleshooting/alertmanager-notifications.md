---
id: TROUBLE-ALERTMANAGER_NOTIFICATIONS
type: troubleshooting
title: "Alertmanager: alerts not notifying / silences not silencing / config not reloading / duplicate pages (HA)"
status: active
kubespray_version: null
kubernetes_version: ">=1.29 <=1.35"
component_version: ">=0.25.0"
verified_at: "2026-07-19"
confidence: confirmed
aliases:
  - alertmanager not sending notifications
  - alertmanager silence not working
  - alertmanager config not reloading
  - duplicate alerts ha alertmanager
  - amtool config check
  - alertmanager route continue
tags:
  - troubleshooting
  - observability
  - alerting
  - alertmanager
sources:
  - type: external
    path: Alertmanager configuration / HA
    url: https://prometheus.io/docs/alerting/latest/configuration/
    note: "route matchers, group_by/group_wait/repeat_interval, inhibition; HA gossip on :9094"
relations:
  - type: see_also
    target: CONCEPT-ADDON_ALERTMANAGER
  - type: see_also
    target: CONCEPT-OBSERVABILITY_STACK
  - type: see_also
    target: TROUBLE-PROMETHEUS_TARGET_DOWN
---

# Alertmanager: alerts not notifying / silences not silencing / config not reloading / duplicate pages (HA)

## Summary

The four operational failures every Alertmanager operator hits, none of which are a "crash": an alert
**fires in Prometheus but no notification arrives**; a **silence doesn't silence**; an **edited config
has no effect**; or an **HA pair pages twice**. Each is a config/labels/topology subtlety, not a broken
pod — so the pod is `Running` and the logs look clean while alerts misbehave.

## Problem

- Prometheus shows an alert `FIRING`, but **no email/Slack/PagerDuty** notification is delivered.
- A **silence** is created but the alert **still notifies**.
- You edit the Alertmanager config, but behaviour **doesn't change**.
- With 2+ replicas, a single alert **notifies twice** (duplicate pages).

## Context

- Applies to Alertmanager `>=0.25.0` (the addon chart, [[CONCEPT-ADDON_ALERTMANAGER]]); part of the
  observability stack ([[CONCEPT-OBSERVABILITY_STACK]]).
- **Routing tree:** an alert walks the `route` tree; the **first matching** route wins unless
  `continue: true`. A too-greedy top route or a receiver with **no notifier configured** (a "null"
  receiver) silently swallows alerts.
- **Grouping/timing:** `group_wait`, `group_interval`, `repeat_interval` **delay** and **batch**
  notifications by design — "nothing arrived yet" is often just `group_wait`. `repeat_interval`
  controls re-notification of a still-firing alert.
- **Silences match on labels:** a silence is a set of **label matchers**; if they don't **exactly**
  match the alert's labels (typo, missing label, regex vs equality), it won't silence.
- **Config reload:** Alertmanager reloads on `SIGHUP` / `POST /-/reload` / config-file change picked up
  by a **config-reloader sidecar**. If the reloader isn't watching the right Secret/ConfigMap, your
  edit never loads.
- **HA:** replicas form a gossip **cluster** on port **9094** and de-duplicate notifications among
  themselves. If they **can't cluster** (blocked gossip port, wrong `--cluster.peer`, single-replica
  each behind separate services), each replica notifies independently → duplicates.

## Diagnostics

```bash
# is the config valid and what's actually loaded?
kubectl -n <ns> exec <am-pod> -- amtool check-config /etc/alertmanager/alertmanager.yml
kubectl -n <ns> exec <am-pod> -- wget -qO- localhost:9093/api/v2/status | head    # config hash, cluster peers
# does the alert reach AM, and which route/receiver?
kubectl -n <ns> exec <am-pod> -- amtool alert query           # alerts AM currently holds
kubectl -n <ns> exec <am-pod> -- amtool config routes test <label=value>...   # which receiver a labelset hits
# silences
kubectl -n <ns> exec <am-pod> -- amtool silence query
# HA: are peers clustered?
kubectl -n <ns> exec <am-pod> -- wget -qO- localhost:9093/api/v2/status | grep -A5 cluster
```

## Known Issues

- **No notification — fix:** run `amtool config routes test` with the alert's labels to see the actual
  receiver; confirm that receiver has a real notifier (not a null receiver) and that a parent route
  isn't catching it first without `continue`. Account for `group_wait`/`repeat_interval` before
  declaring it lost. Check receiver auth/TLS (SMTP creds, Slack webhook URL, proxy).
- **Silence not silencing — fix:** copy the alert's exact labels (`amtool alert query`) into the
  silence matchers; watch equality vs regex and missing labels. Confirm the silence hasn't **expired**
  and you created it on the **same** AM cluster that notifies.
- **Config not reloading — fix:** verify the config-reloader sidecar watches the Secret/ConfigMap you
  edited (`amtool check-config` inside the pod shows what's loaded); trigger `POST /-/reload` or restart
  the pod to confirm; ensure the chart mounts your config, not a default.
- **Duplicate pages (HA) — fix:** open the gossip port **9094/tcp+udp** between replicas, set correct
  `--cluster.peer`/`--cluster.listen-address`, and confirm `/api/v2/status` lists all peers. Clustered
  replicas de-dup; unclustered ones each page.
- **Stale appVersion CVE:** the chart may pin `image.tag` 0.25.0 (a High XSS) — override upward
  ([[CONCEPT-ADDON_ALERTMANAGER]]); unrelated to notification behaviour but worth fixing while here.

## References

- Upstream Alertmanager configuration + HA. Addon [[CONCEPT-ADDON_ALERTMANAGER]]; stack
  [[CONCEPT-OBSERVABILITY_STACK]]; scrape-side [[TROUBLE-PROMETHEUS_TARGET_DOWN]].
