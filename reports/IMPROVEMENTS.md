# Improvement backlog (сгенерировано `scripts/learn.py`)
_Дата: 2026-07-20. Петля обратной связи: сигналы из базы + git. Перегенерируется; правьте не файл, а базу._

## P0 — риски корректности (уроки этой сессии, автоматизированы)

### Операционные доки БЕЗ явного impact/простоя (9 сигналов)

**Нет раздела impact/disruption (runbook/upgrade):**
- `UPGRADE-V2_28_0__V2_28_1` → `kb/kubespray/releases/upgrade-2.28.0-to-2.28.1.md`
- `PRACTICE-HARDENING` → `kb/kubespray/operations/hardening.md`
- `PRACTICE-INTEGRATION` → `kb/kubespray/guides/integration.md`
- `PRACTICE-CERTIFICATE_EXPIRY` → `kb/kubespray/guides/certificate-expiry.md`
- `PRACTICE-KATA_CONTAINERS` → `kb/kubespray/guides/kata-containers.md`
- `PRACTICE-MIRROR` → `kb/kubespray/guides/mirror.md`
- `PRACTICE-CLUSTER_HARDENING` → `kb/kubespray/guides/cluster-hardening.md`
- `PRACTICE-ANSIBLE` → `kb/kubespray/guides/ansible.md`
- `PRACTICE-BACKUP_DR` → `kb/kubespray/guides/backup-disaster-recovery.md`

### Механизм не подкреплён исходником Kubespray (4)
_Док описывает cluster.yml/scale.yml/cilium/kubespray, но в `sources` нет `type: code` на роль/плейбук → риск выдуманной переменной/механизма (как `cilium_upgrade_compatibility`)._
- `PRACTICE-MONITORING_BASELINE` → `kb/kubespray/operations/monitoring-baseline.md`
- `PRACTICE-RBAC_LEAST_PRIVILEGE` → `kb/kubespray/operations/rbac-least-privilege.md`
- `UPGRADE-ARGOCD_2_11_TO_2_14` → `kb/components/argocd/argocd-upgrade-2.11-to-2.14.md`
- `UPGRADE-CILIUM_1_15_TO_1_19` → `kb/components/cilium/cilium-upgrade-1.15-to-1.19.md`

## P1 — свежесть и полнота
### Протухший verified_at (>180д): 0

### Тонкие доки (<900 симв.): 5
- 801c `UPGRADE-V2_28_0__V2_28_1` → `kb/kubespray/releases/upgrade-2.28.0-to-2.28.1.md`
- 828c `PRACTICE-CERT_MANAGER_SETUP` → `kb/kubespray/guides/cert-manager-setup.md`
- 851c `PRACTICE-CNI_GENERIC_PLUGIN` → `kb/kubespray/guides/cni-generic-plugin.md`
- 871c `UPGRADE-V2_27_0__V2_27_1` → `kb/kubespray/releases/upgrade-2.27.0-to-2.27.1.md`
- 872c `PRACTICE-ARCHITECTURE_COMPATIBILITY` → `kb/kubespray/guides/architecture-compatibility.md`

## P2 — недавно исправленное (проверить соседей на тот же класс ошибки): 3
_После правки одного дока тот же промах часто есть в соседних (Cilium→add-nodes)._
- 8401bd8 Аудит не-сетевых раннбуков по источникам: явный impact в etcd-restore и remove-node
- 59fd9f9 Аудит 'rolling/non-disruptive' по источникам Kubespray: правка add-nodes
- e6da74e Cilium upgrade: исправлено по факту исходников Kubespray (прод-критично)

## Темы твоих вопросов (346 реплик; агрегат, без сырого текста)
_Частые темы = где база активнее всего проверяется/дёргается — кандидаты на углубление._
`версии`×27, `продолжаем`×20, `cilium`×18, `можно`×18, `kubespray`×17, `добавь`×15, `продолжим`×14, `после`×13, `переменные`×13, `только`×12, `добавить`×12, `базу`×12, `kubernetes`×12, `какой`×11, `проекта`×10, `теперь`×10, `план`×9, `etcd`×9, `вообще`×9, `будет`×9
