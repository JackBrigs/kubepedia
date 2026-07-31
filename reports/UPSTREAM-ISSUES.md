# Проблемный слой апстрима — сводка

_Сгенерировано `kubepedia issues`. Числа — то, что объявил сам апстрим в заметках к релизам; это сырьё для документов базы, а не сами знания._

| Компонент | Репозиторий | Релизов | CVE | Ломающих | Дефектов | Источник |
|---|---|---:|---:|---:|---:|---|
| envoy-gateway | `envoyproxy/gateway` | 50 | 12 | 52 | 446 | клон: release-notes/*.yaml |
| argo-cd | `argoproj/argo-cd` | 44 | 4 | 8 | 353 | клон: CHANGELOG |
| cilium | `cilium/cilium` | 82 | 0 | 228 | 110 | клон: CHANGELOG |
| consul-k8s | `hashicorp/consul-k8s` | 48 | 22 | 4 | 14 | клон: CHANGELOG |
| etcd | `etcd-io/etcd` | 55 | 32 | 218 | 1 | клон: CHANGELOG |
| kyverno | `kyverno/kyverno` | 1 | 0 | 0 | 1 | клон: CHANGELOG |
| aws-ebs-csi | `kubernetes-sigs/aws-ebs-csi-driver` | 0 | 0 | 0 | 0 | клона нет |
| azure-csi | `kubernetes-sigs/azuredisk-csi-driver` | 0 | 0 | 0 | 0 | клона нет |
| calico | `projectcalico/calico` | 0 | 0 | 0 | 0 | клона нет |
| cert-manager | `cert-manager/cert-manager` | 0 | 0 | 0 | 0 | клона нет |
| cinder-csi | `kubernetes/cloud-provider-openstack` | 0 | 0 | 0 | 0 | клона нет |
| cni-plugins | `containernetworking/plugins` | 0 | 0 | 0 | 0 | клона нет |
| containerd | `containerd/containerd` | 0 | 0 | 0 | 0 | клона нет |
| coredns | `coredns/coredns` | 0 | 0 | 0 | 0 | клона нет |
| cri-o | `cri-o/cri-o` | 0 | 0 | 0 | 0 | клона нет |
| crun | `containers/crun` | 0 | 0 | 0 | 0 | клона нет |
| flannel | `flannel-io/flannel` | 0 | 0 | 0 | 0 | клона нет |
| gcp-pd-csi | `kubernetes-sigs/gcp-compute-persistent-disk-csi-driver` | 0 | 0 | 0 | 0 | клона нет |
| helm | `helm/helm` | 0 | 0 | 0 | 0 | клона нет |
| ingress-nginx | `kubernetes/ingress-nginx` | 0 | 0 | 0 | 0 | клона нет |
| kata-containers | `kata-containers/kata-containers` | 0 | 0 | 0 | 0 | клона нет |
| kube-ovn | `kubeovn/kube-ovn` | 0 | 0 | 0 | 0 | клона нет |
| kube-router | `cloudnativelabs/kube-router` | 0 | 0 | 0 | 0 | клона нет |
| kube-vip | `kube-vip/kube-vip` | 0 | 0 | 0 | 0 | клона нет |
| kubernetes | `kubernetes/kubernetes` | 0 | 0 | 0 | 0 | клона нет |
| kubespray | `kubernetes-sigs/kubespray` | 0 | 0 | 0 | 0 | клона нет |
| local-path-provisioner | `rancher/local-path-provisioner` | 0 | 0 | 0 | 0 | клона нет |
| metallb | `metallb/metallb` | 0 | 0 | 0 | 0 | клона нет |
| metrics-server | `kubernetes-sigs/metrics-server` | 0 | 0 | 0 | 0 | клона нет |
| multus | `k8snetworkplumbingwg/multus-cni` | 0 | 0 | 0 | 0 | клона нет |
| nerdctl | `containerd/nerdctl` | 0 | 0 | 0 | 0 | клона нет |
| node-feature-discovery | `kubernetes-sigs/node-feature-discovery` | 0 | 0 | 0 | 0 | клона нет |
| nodelocaldns | `kubernetes/dns` | 0 | 0 | 0 | 0 | клона нет |
| runc | `opencontainers/runc` | 0 | 0 | 0 | 0 | клона нет |
| scheduler-plugins | `kubernetes-sigs/scheduler-plugins` | 0 | 0 | 0 | 0 | клона нет |
| skopeo | `containers/skopeo` | 0 | 0 | 0 | 0 | клона нет |
| snapshot-controller | `kubernetes-csi/external-snapshotter` | 0 | 0 | 0 | 0 | клона нет |
| talos | `siderolabs/talos` | 0 | 0 | 0 | 0 | клон есть, заметок к релизам не нашлось |
| youki | `youki-dev/youki` | 0 | 0 | 0 | 0 | клона нет |

**Всего уникальных CVE по всем компонентам: 66**

`CVE-2018-5702` `CVE-2019-11254` `CVE-2019-9893` `CVE-2020-14040` `CVE-2021-23820` `CVE-2021-28235` `CVE-2021-35942` `CVE-2021-36159` `CVE-2021-3711` `CVE-2021-38561` `CVE-2022-2097` `CVE-2022-27191` `CVE-2022-27291` `CVE-2022-28948` `CVE-2022-30065` `CVE-2022-41723` `CVE-2022-41724` `CVE-2023-2253` `CVE-2023-2650` `CVE-2023-44487` `CVE-2023-45288` `CVE-2023-47108` `CVE-2023-48795` `CVE-2024-23651` `CVE-2024-24786` `CVE-2024-24791` `CVE-2024-3596` `CVE-2024-36118` `CVE-2024-45337` `CVE-2024-45338` `CVE-2024-56171` `CVE-2025-0913` `CVE-2025-22869` `CVE-2025-22870` `CVE-2025-22872` `CVE-2025-24030` `CVE-2025-24928` `CVE-2025-25294` `CVE-2025-30157` `CVE-2025-30204` `CVE-2025-32386` `CVE-2025-32387` `CVE-2025-35947` `CVE-2025-47914` `CVE-2025-55198` `CVE-2025-55199` `CVE-2025-58058` `CVE-2025-58181` `CVE-2025-61726` `CVE-2025-61731` `CVE-2025-61732` `CVE-2025-64527` `CVE-2025-64763` `CVE-2025-66220` `CVE-2026-22771` `CVE-2026-24051` `CVE-2026-29181` `CVE-2026-33186` `CVE-2026-33343` `CVE-2026-33413` `CVE-2026-39828` `CVE-2026-39835` `CVE-2026-39883` `CVE-2026-46597` `CVE-2026-46598` `CVE-2026-47774`
