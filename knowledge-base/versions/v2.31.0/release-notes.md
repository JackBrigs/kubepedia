---
project: kubespray
kubespray_version: v2.31.0
git_commit: 1c9add4
source_type: release
source_url: https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.31.0
retrieved_at: 2026-07-14
topics:
  - release
  - versions
  - breaking-changes
reliability: authoritative
---

# GitHub Release Kubespray v2.31.0

- **Тег:** `v2.31.0` (commit `1c9add4`)
- **Дата тега:** 2026-04-24 (по git)
- **Предыдущая версия:** v2.30.0
- **Тип:** минорный релиз с крупными breaking changes (Kubernetes 1.35, удаление ряда аддонов, отказ от cgroup v1 по умолчанию).
- **Источник:** https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.31.0

## ⚠️ Breaking changes и удаления (action required)

1. **Kubernetes 1.35 по умолчанию; cgroup v1 больше не поддерживается по умолчанию.** Для узлов на cgroup v1 нужно явно задать `kubelet_fail_cgroup_v1: false`.
   - Проверено по коду: `roles/kubespray_defaults/defaults/main/main.yml:21` — `kubelet_fail_cgroup_v1: true`.
2. **Удалена поддержка ingress-nginx** (проект выведен из поддержки upstream). Роль `ingress_controller/ingress_nginx`, переменные `ingress_nginx_*`, тег `ingress-nginx` и `docs/ingress/ingress_nginx.md` удалены.
3. **Удалён аддон Kubernetes Dashboard** (upstream архивирован). Роль, переменные и тег `dashboard` удалены.
4. **Удалён Netchecker.** Роль, переменные `deploy_netchecker` и тег `netchecker` удалены.
5. **Переименована переменная bastion:** `ssh_bastion_confing__name` → `ssh_bastion_config_name`.
   - Проверено: новое имя в `roles/bastion-ssh-config/`, старое отсутствует.
6. **Шаблоны kubeadm — только v1beta4;** поддержка v1beta3 удалена.
   - Проверено: в `roles/kubernetes/control-plane/templates/` остался только `kubeadm-config.v1beta4.yaml.j2`.
7. **Роль валидации инвентаря прерывает плейбук при обнаружении удалённых/устаревших переменных** — устаревшие конфиги нужно вычистить перед обновлением.
8. Удалена поддержка terraform-провайдера Nifcloud; удалена документация RHEL 8.

## Заметные новые возможности

- Kubernetes v1.35.4 по умолчанию.
- Настраиваемый путь статических подов: `kubelet_static_pod_path`.
- Структурированная AuthenticationConfiguration для kube-apiserver (`kube_apiserver_use_authentication_config_file`, `kube_apiserver_authentication_config_*`).
- Кастомизация имени сервиса CoreDNS: `coredns_svc_name`.
- Поддержка Fedora 41 и 42.
- Cilium: обновление apiVersion ресурсов до v2.
- Ansible обновлён до 11.13.0 (ansible-core 2.18; требование `>=2.18.0,<2.19.0`, Python 3.11–3.13).
- OpenStack CCM обновлён до v1.35.0.

## Версии компонентов (по релизу)

Все сверены с разрешёнными из кода тега ([[versions/v2.31.0/components|components]]) — расхождений нет.

| Компонент | Версия | в v2.30.0 было |
|---|---|---|
| Kubernetes | 1.35.4 | 1.34.3 |
| etcd | 3.6.10 | 3.5.26 |
| containerd | 2.2.3 | 2.2.1 |
| runc | 1.4.2 | 1.3.4 |
| CRI-O | 1.35.0 | 1.34.4 |
| cni-plugins | 1.9.1 | 1.8.0 |
| Cilium | 1.19.3 | 1.18.6 |
| CoreDNS | 1.12.4 | 1.12.1 |
| Helm | 3.18.4 | 3.18.4 |
| MetalLB | 0.13.9 | 0.13.9 |
| cert-manager | 1.15.3 | 1.15.3 |
| metrics-server | 0.8.1 | 0.8.0 |
| kube-vip | 1.0.3 | 1.0.3 |
| Gateway API | 1.5.1 | 1.4.1 |
| Calico *(не индексируется)* | 3.31.5 | 3.30.6 |
| Docker | 28.3 | — |

## Примечания

- Детальное сравнение с предыдущей версией: [[diffs/v2.30.0__v2.31.0|Отчёт сравнения v2.30.0 → v2.31.0]] (этап 8).
- Дата на странице релиза GitHub в извлечённом виде отображалась как «April 25»; авторитетная дата тега по git — 2026-04-24.

---

Связанные срезы: [[versions/v2.31.0/components|Компоненты]] · [[versions/v2.31.0/variables/k8s-cluster|Переменные ядра]] · [[versions/v2.31.0/docs/upgrades|Дайджест: обновление]]

Назад: [[versions/v2.31.0/README|Срез v2.31.0]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
