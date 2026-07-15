---
project: kubespray
kubespray_version: v2.27.0
git_commit: 9ec9b3a
source_type: code
source_path: roles/kubespray-defaults/defaults/main/download.yml
source_url: https://github.com/kubernetes-sigs/kubespray/tree/v2.27.0
retrieved_at: 2026-07-15
topics:
  - components
  - versions
reliability: authoritative
---

# Компоненты и их версии по умолчанию в Kubespray v2.27.0

Часть среза [[versions/v2.27.0/README|Срез v2.27.0]]. Источник истины — парный YAML-справочник [[versions/v2.27.0/components|components.yaml]] (там же дословные выражения и source_path каждого компонента).

## Сводная таблица

| Компонент | Версия по умолчанию | Переменная |
|---|---|---|
| Kubernetes | 1.31.4 | `kube_version` |
| kubeadm / kubectl / kubelet | 1.31.4 (= `kube_version`) | `kube_version` |
| etcd | 3.5.16 | `etcd_version` |
| pause (pod infra) | 3.10 | `pod_infra_version` |
| containerd | 1.7.24 | `containerd_version` |
| docker-containerd | 1.6.32 | `docker_containerd_version` |
| runc | 1.2.3 | `runc_version` |
| crictl | 1.31.1 | `crictl_version` |
| nerdctl | 1.7.7 | `nerdctl_version` |
| CRI-O | 1.31.0 | `crio_version` |
| cri-dockerd | 0.3.11 | `cri_dockerd_version` |
| skopeo | 1.16.1 | `skopeo_version` |
| crun | 1.17 | `crun_version` |
| youki | 0.4.1 | `youki_version` |
| gVisor | 20240305 | `gvisor_version` |
| Kata Containers | 3.1.3 | `kata_containers_version` |
| CNI plugins | 1.4.0 | `cni_version` |
| Cilium | 1.15.9 | `cilium_version` |
| cilium-cli | 0.16.0 | `cilium_cli_version` |
| Calico | 3.29.1 | `calico_version` |
| Flannel | 0.22.0 | `flannel_version` |
| Flannel CNI plugin | 1.1.2 | `flannel_cni_version` |
| Weave | 2.8.7 | `weave_version` |
| kube-ovn | 1.12.21 | `kube_ovn_version` |
| kube-router | 2.0.0 | `kube_router_version` |
| Multus | 4.1.0 | `multus_version` |
| CoreDNS | 1.11.3 | `coredns_version` |
| nodelocaldns | 1.22.28 | `nodelocaldns_version` |
| dns-autoscaler | 1.8.8 | `dnsautoscaler_version` |
| Helm | 3.16.4 | `helm_version` |
| yq | 4.42.1 | `yq_version` |
| krew | 0.4.4 | `krew_version` |
| metrics-server | 0.7.0 | `metrics_server_version` |
| ingress-nginx | 1.12.0 | `ingress_nginx_version` |
| cert-manager | 1.15.3 | `cert_manager_version` |
| Argo CD | 2.11.0 | `argocd_version` |
| MetalLB | 0.13.9 | `metallb_version` |
| local-path-provisioner | 0.0.24 | `local_path_provisioner_version` |
| local-volume-provisioner | 2.5.0 | `local_volume_provisioner_version` |
| node-feature-discovery | 0.16.4 | `node_feature_discovery_version` |
| snapshot-controller | 7.0.2 | `snapshot_controller_supported_versions` |
| scheduler-plugins | 0 (недоступен) | `scheduler_plugins_version` |
| registry | 2.8.1 | `registry_version` |
| netcheck | 1.2.2 | `netcheck_version` |
| kubernetes-dashboard | 2.7.0 | `dashboard_image_tag` |
| kube-vip | 0.8.0 | `kube_vip_image_tag` |
| cinder-csi-plugin | 1.30.0 | `cinder_csi_plugin_version` |
| aws-ebs-csi-plugin | 0.5.0 | `aws_ebs_csi_plugin_version` |
| gcp-pd-csi-plugin | 1.9.2 | `gcp_pd_csi_plugin_version` |
| azure-csi-plugin | 1.10.0 | `azure_csi_plugin_version` |
| cephfs-provisioner | 2.1.0-k8s1.11 | `cephfs_provisioner_version` |
| rbd-provisioner | 2.1.1-k8s1.11 | `rbd_provisioner_version` |

В отличие от v2.29.x, в v2.27.0 CNI-плагины (Calico, Flannel, Weave, kube-ovn, kube-router, Multus) задекларированы прямо в `roles/kubespray-defaults/defaults/main/download.yml` литералами и включены в справочник. CNI по умолчанию у проекта — Cilium.

## Как версии вычисляются

В v2.27.0 механизм проще, чем в v2.29.x: большинство версий заданы **прямыми литералами** в `roles/kubespray-defaults/defaults/main/download.yml`, например:

```
containerd_version: 1.7.24
cilium_version: "v1.15.9"
```

Механизм «первый ключ словаря контрольных сумм» (`(X_checksums | dict2items)[0].key`), характерный для v2.29.x, здесь ещё не используется.

Порядок разрешения версий, привязанных к Kubernetes:

1. `kube_version` = литерал **v1.31.4** (`roles/kubespray-defaults/defaults/main/main.yml`). Минимально допустимая `kube_version_min_required` = **v1.29.0**.
2. Из `kube_version` регэкспом вычисляется `kube_major_version` = **v1.31**.
3. Компоненты, привязанные к версии Kubernetes, выбираются из словарей `*_supported_versions` по ключу `kube_major_version`:
   - `etcd_version` = `etcd_supported_versions['v1.31']` → **v3.5.16**;
   - `pod_infra_version` = `pod_infra_supported_versions['v1.31']` → **3.10**;
   - `crictl_version` = `crictl_supported_versions['v1.31']` → **v1.31.1**;
   - `crio_version` = `crio_supported_versions['v1.31']` → **v1.31.0**;
   - `snapshot_controller` = `snapshot_controller_supported_versions['v1.31']` → **v7.0.2**;
   - `scheduler_plugins_version` = `scheduler_plugins_supported_versions['v1.31']` → **0** (сборка под 1.29–1.31 отсутствует, компонент фактически недоступен).
4. `coredns_version` выбирается тернарным условием по `kube_version`: `v1.11.3`, если `kube_version >= v1.30.5`, иначе `v1.11.1`; для v1.31.4 → **v1.11.3**.
5. Литералами заданы почти все остальные компоненты, включая CNI (Cilium 1.15.9, Calico 3.29.1 и др.), containerd 1.7.24, runc v1.2.3, Helm v3.16.4, addon-ы (metrics-server, ingress-nginx, cert-manager, MetalLB и т.д.).
6. Отдельно: `argocd_version` (**v2.11.0**) определён **не** в download.yml, а в `roles/kubernetes-apps/argocd/defaults/main.yml`.
