---
project: kubespray
kubespray_version: v2.30.0
git_commit: f4ccdb5
source_type: release
source_url: https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.30.0
retrieved_at: 2026-07-14
topics:
  - release
  - versions
  - breaking-changes
reliability: authoritative
---

# GitHub Release Kubespray v2.30.0

- **Тег:** `v2.30.0` (commit `f4ccdb5`)
- **Дата тега:** 2026-01-30 (по git)
- **Предыдущая версия:** v2.29.1
- **Тип:** минорный релиз (обновление Kubernetes до 1.34.x, ряд breaking changes).
- **Источник:** https://github.com/kubernetes-sigs/kubespray/releases/tag/v2.30.0

## ⚠️ Breaking changes и предупреждения об обновлении

1. **Cilium: `k8sServiceHost` / `k8sServicePort` теперь берутся из `kube_apiserver_global_endpoint`**, а не автоопределяются. Требуется убедиться, что этот endpoint корректно настроен и доступен со всех узлов.
   - Проверено по коду: `roles/network_plugin/cilium/templates/values.yaml.j2:10-11` — `k8sServiceHost: "{{ kube_apiserver_global_endpoint | urlsplit('hostname') }}"`, `k8sServicePort: "{{ ... | urlsplit('port') }}"`.
2. **Добавление control plane узла «в начало» списка `kube_control_plane` явно не поддерживается** — новый control plane нужно размещать в конце группы.
3. **`containerd_discard_unpacked_layers`** теперь применяется только к containerd < 2.1 (во избежание предупреждений нового Transfer Service).
4. **Удалены переменные:**
   - `etcd_cert_dir_mode` — удалена, режим каталога всегда `0700`. Проверено по коду: в `roles/` переменная отсутствует.
   - `runtime_engine` и `runtime_root` — удалены из конфигурации containerd (по заметкам релиза). Замечание по коду: ссылки на `runtime.engine`/`runtime.root` сохранились только в легаси-шаблоне `roles/container-engine/containerd/templates/config-v1.toml.j2` (для containerd < 2.0), в основном пути конфигурации их нет.

## Устаревшие / выводимые из поддержки компоненты

- **Ingress NGINX** — v2.30.0 последняя версия с его поддержкой; удаление запланировано в будущих релизах.
- **Kubernetes Dashboard** — последняя версия с поддержкой; удаление запланировано.

## Версии компонентов (по релизу)

Все сверены с разрешёнными из кода тега ([[versions/v2.30.0/components|components]]) — расхождений нет.

| Компонент | Версия | в v2.29.1 было |
|---|---|---|
| Kubernetes | 1.34.3 | 1.33.7 |
| etcd | 3.5.26 | 3.5.25 |
| containerd | 2.2.1 | 2.1.5 |
| CRI-O | 1.34.4 | 1.33.7 |
| cni-plugins | 1.8.0 | 1.8.0 |
| Cilium | 1.18.6 | 1.18.4 |
| CoreDNS | 1.12.1 | 1.12.0 |
| Helm | 3.18.4 | 3.18.4 |
| MetalLB | 0.13.9 | 0.13.9 |
| cert-manager | 1.15.3 | 1.15.3 |
| ingress-nginx | 1.13.3 | 1.13.3 |
| Calico | 3.30.6 | 3.30.5 (не индексируется) |
| Flannel | 0.27.3 | 0.27.3 (не индексируется) |

## Заметные изменения и исправления

- Экспериментальная поддержка RockyLinux 10.
- Поддержка Kubernetes v1.34.x.
- Gateway API обновлён до 1.4.x (в коде тега `gateway_api_version` = 1.4.1).
- kube-vip обновлён до v1.0.3.
- Исправления Calico RBAC для Kubernetes 1.33+.
- Исправлен рендеринг `loadBalancer.mode` для Cilium (см. troubleshooting v2.29.1 — этот фикс вошёл ещё в v2.29.1, здесь в составе базовой линии).
- Исправлено автоматическое обновление сертификатов через systemd timer.

## Примечания

- Детальное сравнение с предыдущей версией: [[diffs/v2.29.1__v2.30.0|Отчёт сравнения v2.29.1 → v2.30.0]] (этап 8).
- Дата на странице релиза GitHub в извлечённом виде отображалась как «January 29»; авторитетная дата тега по git — 2026-01-30.

---

Связанные срезы: [[versions/v2.30.0/components|Компоненты]] · [[versions/v2.30.0/variables/cni|Переменные CNI]] · [[versions/v2.30.0/docs/upgrades|Дайджест: обновление]]

Назад: [[versions/v2.30.0/README|Срез v2.30.0]] · [[INDEX|Kubespray Encyclopedia — INDEX]]
