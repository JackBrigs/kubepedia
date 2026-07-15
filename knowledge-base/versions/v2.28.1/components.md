---
project: kubespray
kubespray_version: v2.28.1
git_commit: a20891a
source_type: code
source_path: roles/kubespray_defaults/defaults/main/download.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.28.1
retrieved_at: 2026-07-15
topics:
  - components
  - versions
reliability: authoritative
---

# Компоненты и их версии по умолчанию в Kubespray v2.28.1

Часть среза [[versions/v2.28.1/README|Срез v2.28.1]]. Источник истины — парный YAML-справочник [[versions/v2.28.1/components|components.yaml]] (там же дословные Jinja-выражения и source_path каждого компонента).

## Сводная таблица

| Компонент | Версия по умолчанию | Переменная |
|---|---|---|
| Kubernetes | 1.32.8 | `kube_version` |
| kubeadm / kubectl / kubelet | 1.32.8 (= `kube_version`) | `kube_version` |
| etcd | 3.5.22 | `etcd_version` |
| pause (pod infra) | 3.10 | `pod_infra_version` |
| containerd | 2.0.6 | `containerd_version` |
| docker-containerd | 1.6.32 | `docker_containerd_version` |
| runc | 1.2.6 | `runc_version` |
| crictl | 1.32.0 | `crictl_version` |
| nerdctl | 2.0.5 | `nerdctl_version` |
| CRI-O | 1.32.0 | `crio_version` |
| cri-dockerd | 0.3.18 | `cri_dockerd_version` |
| skopeo | 1.16.1 | `skopeo_version` |
| crun | 1.17 | `crun_version` |
| youki | 0.5.5 | `youki_version` |
| gVisor | 20250820.0 | `gvisor_version` |
| Kata Containers | 3.7.0 | `kata_containers_version` |
| CNI plugins | 1.4.1 | `cni_version` |
| Cilium | 1.17.7 | `cilium_version` |
| cilium-cli | 0.18.6 | `cilium_cli_version` |
| Calico | 3.29.5 | `calico_version` |
| Flannel | 0.22.0 (cni-plugin 1.1.2) | `flannel_version` |
| Weave | 2.8.7 | `weave_version` |
| kube-ovn | 1.12.21 | `kube_ovn_version` |
| kube-router | 2.1.1 | `kube_router_version` |
| Multus | 4.1.0 | `multus_version` |
| CoreDNS | 1.11.3 | `coredns_version` |
| nodelocaldns | 1.25.0 | `nodelocaldns_version` |
| dns-autoscaler | 1.8.8 | `dnsautoscaler_version` |
| Helm | 3.16.4 | `helm_version` |
| yq | 4.42.1 | `yq_version` |
| metrics-server | 0.7.0 | `metrics_server_version` |
| ingress-nginx | 1.12.1 | `ingress_nginx_version` |
| cert-manager | 1.15.3 | `cert_manager_version` |
| Argo CD | 2.14.5 | `argocd_version` |
| MetalLB | 0.13.9 | `metallb_version` |
| local-path-provisioner | 0.0.24 | `local_path_provisioner_version` |
| local-volume-provisioner | 2.5.0 | `local_volume_provisioner_version` |
| node-feature-discovery | 0.16.4 | `node_feature_discovery_version` |
| Gateway API CRDs | 1.2.1 | `gateway_api_version` |
| registry | 2.8.1 | `registry_version` |
| kubernetes-dashboard | 2.7.0 | `dashboard_image_tag` |
| kube-vip | 0.8.9 | `kube_vip_image_tag` |

В отличие от более поздних срезов, в v2.28.1 в справочник включены все CNI-плагины (Calico/Flannel/Weave/kube-ovn/kube-router/Multus), поскольку задача среза — полный перечень значимых компонентов. Их версии определены в том же `roles/kubespray_defaults/defaults/main/download.yml`.

## Как версии вычисляются из checksums

Часть версий заданы **не литералами**, а Jinja-выражением вида:

```
containerd_version: "{{ (containerd_archive_checksums['amd64'] | dict2items)[0].key }}"
```

Это означает «первый ключ словаря контрольных сумм для amd64». Словари `*_checksums` в `roles/kubespray_defaults/vars/main/checksums.yml` упорядочены по убыванию версий, поэтому по умолчанию берётся **самая новая версия, для которой в теге есть контрольная сумма**. При переопределении версии пользователем для неё обязана существовать запись в checksums (иначе загрузка упадёт на проверке суммы).

Порядок разрешения:

1. `kube_version` = первый ключ `kubelet_checksums['amd64']` → **1.32.8** (`roles/kubespray_defaults/defaults/main/main.yml`). Минимально допустимая версия `kube_version_min_required` = последний ключ → **1.30.0**.
2. Из `kube_version` вычисляется `kube_major_version` = **1.32** (`roles/kubespray_defaults/defaults/main/download.yml`).
3. Компоненты, привязанные к версии Kubernetes, выбираются из словарей `*_supported_versions` по ключу `kube_major_version`. **Важно:** в v2.28.1 эти словари объявлены прямо в `download.yml` (а не в `vars/main/main.yml`, как в поздних тегах):
   - `etcd_version` = `etcd_supported_versions['1.32']` → **3.5.22**. В v2.28.1 значения `etcd_supported_versions` заданы не литералом, а выражением `(etcd_binary_checksums['amd64'].keys() | select('version', '3.6', '<'))[0]` — наибольшая версия etcd < 3.6 из checksums (в v2.28.0 было литеральное 3.5.16);
   - `crictl_version` = `crictl_supported_versions['1.32']` → **1.32.0**;
   - `crio_version` = `crio_supported_versions['1.32']` → **1.32.0**;
   - `pod_infra_version` = `pod_infra_supported_versions['1.32']` → **3.10**.
4. `coredns_version` задан тернарным выражением: **1.11.3** при `kube_version >= 1.30.5`, иначе 1.11.1 → для 1.32.8 это **1.11.3**.
5. Литералами заданы: `cilium_version` (1.17.7), `nodelocaldns_version`, версии CNI (flannel/weave/kube-ovn/kube-router/multus) и addons (metrics-server 0.7.0, ingress-nginx 1.12.1, cert-manager 1.15.3, MetalLB 0.13.9, local-path-provisioner 0.0.24 и др.).
6. `argocd_version` в v2.28.1 резолвится выражением `(argocd_install_checksums.no_arch | dict2items)[0].key` → **2.14.5** в `roles/kubespray_defaults/defaults/main/download.yml` (манифест ставится через `downloads.argocd_install` с `argocd_install_url` и `argocd_install_checksum`); в `roles/kubernetes-apps/argocd/defaults/main.yml` остаётся `argocd_version: 2.14.5` как fallback.
