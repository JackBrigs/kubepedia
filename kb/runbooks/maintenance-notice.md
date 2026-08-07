---
id: PRACTICE-MAINTENANCE_NOTICE
type: best_practice
title: "Maintenance notice: restate what the provider announced, not what it might cause"
status: active
kubespray_version: ">=v2.27.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-08-07"
confidence: confirmed
aliases:
  - maintenance
  - создай maintenance
  - шаблон maintenance
  - работы провайдера
  - окно обслуживания
  - планові роботи датацентра
  - maintenance notice template
  - action required maintenance
tags:
  - runbook
  - operations
  - maintenance
  - datacenter
sources:
  - type: measurement
    path: IO-6117, AMS94, 2026-08-13
    note: "уведомление провайдера: две ноды k8s из двенадцати хостов; LACP проверен на месте (aggi, 802.3ad, два порта up)"
relations:
  - type: see_also
    target: PRACTICE-RUNBOOK_NODE_MAINTENANCE
  - type: see_also
    target: PRACTICE-RUNBOOK_ORDER_NODES
---

## Summary

A maintenance notice records what the provider announced and which of our machines
it touches. It is not an impact analysis and not a place for predictions. The single
most common way to spoil it is to mix verified facts with reasonable-sounding
consequences — the reader then cannot tell which is which, and neither can the
person who wrote it a week later.

## Context

Applies to datacenter or provider maintenance windows affecting hosts we own.
The input is the provider's notice; the only research needed is mapping the listed
hosts to our clusters and confirming any prerequisite the notice demands.

## Implementation

**Template:**

```markdown
# Ресурсы

- <имя ноды>
- <имя ноды>

# Описание работ

- Работы провайдера <ID> на <что затрагивается> площадки <площадка>
- Окно: <дата>, <время> (Кипр)

# Возможное влияние

- <дословно из уведомления>
- <дословно из уведомления>
```

**Rules per section:**

- **Ресурсы** — host names only. No addresses, roles, cluster names or hardware.
  Hosts from the provider's list that are not ours are omitted entirely.
- **Описание работ** — the provider's identifier, what is being worked on, and the
  window. Times are converted to **Cyprus local time**, since that is where the
  team reads them; the provider states UTC.
- **Возможное влияние** — only what the notice itself states. Consequences we infer
  (pods rescheduling, workloads failing, capacity loss) do not belong here.

**What is researched but not written into the document:** which clusters the hosts
belong to, and whether any prerequisite the notice demands is actually satisfied —
for example "ensure LACP aggregation is configured", checkable via
`/proc/net/bonding/*`. Report those findings in the reply; the maintenance document
stays as above.

## Known Issues

**Do not narrate consequences.** "Pods will migrate", "GPU pods will go Pending",
"capacity drops by 13%" are all plausible and all invented at the moment of
writing. The provider announced a network event, not an outcome for our workloads.
If the consequence matters, it belongs in a separate assessment addressed to whoever
decides on the window.

**Do not carry over findings from unrelated checks.** Hardware details discovered
while looking at a node — GPU models, disk layout, kernel version — are not part of
a maintenance notice, however interesting.

**Keep the provider's own wording for impact.** Rephrasing "risk of private network
unavailability for up to one hour in the worst case" into something sharper changes
a stated risk into a promise.

## References

- Provider maintenance notice — the only source for the work description and impact
- `/proc/net/bonding/*` — verifying LACP prerequisites before confirming a window
- Inventory repository — mapping the announced host list to our clusters
