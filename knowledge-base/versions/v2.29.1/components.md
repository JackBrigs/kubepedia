---
project: kubespray
kubespray_version: v2.29.1
git_commit: 0c6a295
source_type: code
source_path: roles/kubespray_defaults/defaults/main/download.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.29.1
retrieved_at: 2026-07-14
topics:
  - components
  - versions
reliability: authoritative
---

# Компоненты и их версии по умолчанию в Kubespray v2.29.1

Часть среза [[versions/v2.29.1/README|Срез v2.29.1]]. Источник истины — парный YAML-справочник [[versions/v2.29.1/components|components.yaml]] (там же дословные Jinja-выражения и source_path каждого компонента).

## Сводная таблица

| Компонент | Версия по умолчанию | Переменная |
|---|---|---|
| Kubernetes | 1.33.7 | `kube_version` |
| kubeadm / kubectl / kubelet | 1.33.7 (= `kube_version`) | `kube_version` |
| etcd | 3.5.25 | `etcd_version` |
| pause (pod infra) | 3.10 | `pod_infra_version` |
| containerd | 2.1.5 | `containerd_version` |
| runc | 1.3.4 | `runc_version` |
| crictl | 1.33.0 | `crictl_version` |
| nerdctl | 2.1.6 | `nerdctl_version` |
| CRI-O | 1.33.7 | `crio_version` |
| cri-dockerd | 0.3.21 | `cri_dockerd_version` |
| skopeo | 1.16.1 | `skopeo_version` |
| crun | 1.17 | `crun_version` |
| youki | 0.5.7 | `youki_version` |
| gVisor | 20251201.0 | `gvisor_version` |
| Kata Containers | 3.7.0 | `kata_containers_version` |
| CNI plugins | 1.8.0 | `cni_version` |
| Cilium | 1.18.4 | `cilium_version` |
| cilium-cli | 0.18.9 | `cilium_cli_version` |
| CoreDNS | 1.12.0 | `coredns_version` |
| nodelocaldns | 1.25.0 | `nodelocaldns_version` |
| dns-autoscaler | 1.8.8 | `dnsautoscaler_version` |
| Helm | 3.18.4 | `helm_version` |
| yq | 4.42.1 | `yq_version` |
| metrics-server | 0.8.0 | `metrics_server_version` |
| ingress-nginx | 1.13.3 | `ingress_nginx_version` |
| cert-manager | 1.15.3 | `cert_manager_version` |
| Argo CD | 2.14.21 | `argocd_version` |
| MetalLB | 0.13.9 | `metallb_version` |
| local-path-provisioner | 0.0.32 | `local_path_provisioner_version` |
| local-volume-provisioner | 2.5.0 | `local_volume_provisioner_version` |
| node-feature-discovery | 0.16.4 | `node_feature_discovery_version` |
| Gateway API CRDs | 1.2.1 | `gateway_api_version` |
| Prometheus Operator CRDs | 0.84.0 | `prometheus_operator_crds_version` |
| registry | 2.8.1 | `registry_version` |
| kubernetes-dashboard | 2.7.0 | `dashboard_image_tag` |
| kube-vip | 0.8.9 | `kube_vip_image_tag` |

Из CNI-плагинов проект индексирует только Cilium; Calico/Flannel/kube-ovn/kube-router/Multus в справочник не включены (их версии определены в том же `roles/kubespray_defaults/defaults/main/download.yml`).

## Как версии вычисляются из checksums

Большинство версий заданы **не литералами**, а Jinja-выражением вида:

```
containerd_version: "{{ (containerd_archive_checksums['amd64'] | dict2items)[0].key }}"
```

Это означает «первый ключ словаря контрольных сумм для amd64». Словари `*_checksums` в `roles/kubespray_defaults/vars/main/checksums.yml` упорядочены по убыванию версий, поэтому по умолчанию берётся **самая новая версия, для которой в теге есть контрольная сумма**. При переопределении версии пользователем для неё обязана существовать запись в checksums (иначе загрузка упадёт на проверке суммы).

Порядок разрешения:

1. `kube_version` = первый ключ `kubelet_checksums['amd64']` → **1.33.7** (`roles/kubespray_defaults/defaults/main/main.yml`). Минимально допустимая версия `kube_version_min_required` = последний ключ → **1.31.0**.
2. Из `kube_version` вычисляются `kube_major_version` = **1.33** и `kube_major_next_version` = **1.34** (`roles/kubespray_defaults/vars/main/main.yml`).
3. Компоненты, привязанные к версии Kubernetes, выбираются из словарей `*_supported_versions` по ключу `kube_major_version`:
   - `etcd_version` = `etcd_supported_versions['1.33']` = «первый ключ `etcd_binary_checksums['amd64']` < 3.6» → **3.5.25**;
   - `coredns_version` = `coredns_supported_versions['1.33']` → **1.12.0**;
   - `pod_infra_version` = `pod_infra_supported_versions['1.33']` → **3.10**.
4. `crictl_version` и `crio_version` берут первый ключ своего словаря сумм, **строго меньший** `kube_major_next_version` (1.34): самая новая версия, совместимая с текущим Kubernetes → crictl **1.33.0**, CRI-O **1.33.7**.
5. Литералами заданы: `cilium_version` (1.18.4), `nodelocaldns_version`, версии addons (metrics-server, ingress-nginx, cert-manager, MetalLB и др.).

Механизм загрузки этих компонентов описан в [[versions/v2.29.1/variables/download|заметке о механизме download]].
