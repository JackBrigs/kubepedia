# Проблемный слой апстрима — сводка

_Сгенерировано `kubepedia issues`. Числа — то, что объявил сам апстрим в заметках к релизам; это сырьё для документов базы, а не сами знания._

| Компонент | Репозиторий | Релизов | CVE | Ломающих | Дефектов | Источник |
|---|---|---:|---:|---:|---:|---|
| talos | `siderolabs/talos` | 136 | 3 | 0 | 3798 | GitHub Releases API |
| containerd | `containerd/containerd` | 170 | 30 | 11 | 2610 | GitHub Releases API |
| kube-ovn | `kubeovn/kube-ovn` | 143 | 15 | 0 | 1622 | GitHub Releases API |
| helm | `helm/helm` | 148 | 2 | 3 | 1597 | GitHub Releases API |
| cri-o | `cri-o/cri-o` | 207 | 11 | 2 | 840 | GitHub Releases API |
| azure-csi | `kubernetes-sigs/azuredisk-csi-driver` | 125 | 50 | 0 | 654 | GitHub Releases API |
| argo-cd | `argoproj/argo-cd` | 111 | 4 | 8 | 553 | клон: CHANGELOG |
| kubespray | `kubernetes-sigs/kubespray` | 51 | 3 | 31 | 457 | GitHub Releases API |
| envoy-gateway | `envoyproxy/gateway` | 50 | 12 | 52 | 446 | клон: release-notes/*.yaml |
| etcd | `etcd-io/etcd` | 147 | 32 | 218 | 420 | клон: CHANGELOG |
| youki | `youki-dev/youki` | 23 | 3 | 14 | 415 | GitHub Releases API |
| cert-manager | `cert-manager/cert-manager` | 140 | 49 | 24 | 360 | GitHub Releases API |
| kata-containers | `kata-containers/kata-containers` | 38 | 7 | 1 | 348 | GitHub Releases API |
| ingress-nginx | `kubernetes/ingress-nginx` | 69 | 9 | 0 | 321 | GitHub Releases API |
| skopeo | `containers/skopeo` | 37 | 7 | 0 | 223 | GitHub Releases API |
| consul-k8s | `hashicorp/consul-k8s` | 114 | 22 | 4 | 221 | клон: CHANGELOG |
| node-feature-discovery | `kubernetes-sigs/node-feature-discovery` | 40 | 0 | 0 | 191 | GitHub Releases API |
| kube-router | `cloudnativelabs/kube-router` | 33 | 1 | 2 | 180 | GitHub Releases API |
| cilium | `cilium/cilium` | 130 | 0 | 228 | 175 | клон: CHANGELOG |
| kube-vip | `kube-vip/kube-vip` | 37 | 0 | 9 | 146 | GitHub Releases API |
| crun | `containers/crun` | 67 | 7 | 0 | 135 | GitHub Releases API |
| runc | `opencontainers/runc` | 39 | 10 | 1 | 106 | GitHub Releases API |
| cinder-csi | `kubernetes/cloud-provider-openstack` | 41 | 4 | 6 | 96 | GitHub Releases API |
| cni-plugins | `containernetworking/plugins` | 24 | 1 | 2 | 89 | GitHub Releases API |
| flannel | `flannel-io/flannel` | 53 | 0 | 0 | 86 | GitHub Releases API |
| nerdctl | `containerd/nerdctl` | 44 | 19 | 0 | 82 | GitHub Releases API |
| gcp-pd-csi | `kubernetes-sigs/gcp-compute-persistent-disk-csi-driver` | 44 | 10 | 5 | 73 | GitHub Releases API |
| coredns | `coredns/coredns` | 18 | 2 | 0 | 49 | GitHub Releases API |
| calico | `projectcalico/calico` | 22 | 0 | 0 | 45 | GitHub Releases API |
| local-path-provisioner | `rancher/local-path-provisioner` | 11 | 0 | 0 | 34 | GitHub Releases API |
| scheduler-plugins | `kubernetes-sigs/scheduler-plugins` | 11 | 3 | 4 | 33 | GitHub Releases API |
| metrics-server | `kubernetes-sigs/metrics-server` | 14 | 2 | 1 | 21 | GitHub Releases API |
| snapshot-controller | `kubernetes-csi/external-snapshotter` | 12 | 0 | 1 | 20 | GitHub Releases API |
| nodelocaldns | `kubernetes/dns` | 8 | 3 | 0 | 14 | GitHub Releases API |
| multus | `k8snetworkplumbingwg/multus-cni` | 7 | 0 | 0 | 11 | GitHub Releases API |
| kyverno | `kyverno/kyverno` | 1 | 0 | 0 | 1 | клон: CHANGELOG |
| aws-ebs-csi | `kubernetes-sigs/aws-ebs-csi-driver` | 0 | 0 | 0 | 0 | GitHub Releases API |
| kubernetes | `kubernetes/kubernetes` | 0 | 0 | 0 | 0 | GitHub Releases API |
| metallb | `metallb/metallb` | 0 | 0 | 0 | 0 | GitHub Releases API |

**Всего уникальных CVE по всем компонентам: 218**

`CVE-1999-0524` `CVE-2018-25032` `CVE-2018-5702` `CVE-2019-11253` `CVE-2019-11254` `CVE-2019-11255` `CVE-2019-16276` `CVE-2019-16884` `CVE-2019-17596` `CVE-2019-18837` `CVE-2019-19921` `CVE-2019-5736` `CVE-2019-9512` `CVE-2019-9514` `CVE-2019-9515` `CVE-2019-9893` `CVE-2019-9946` `CVE-2020-0601` `CVE-2020-14040` `CVE-2020-28928` `CVE-2020-7919` `CVE-2020-9283` `CVE-2021-23820` `CVE-2021-28235` `CVE-2021-3121` `CVE-2021-32760` `CVE-2021-33910` `CVE-2021-3538` `CVE-2021-35942` `CVE-2021-36159` `CVE-2021-3711` `CVE-2021-38561` `CVE-2021-3995` `CVE-2021-3996` `CVE-2021-41190` `CVE-2021-43618` `CVE-2022-0778` `CVE-2022-1271` `CVE-2022-1708` `CVE-2022-1996` `CVE-2022-2097` `CVE-2022-21698` `CVE-2022-23525` `CVE-2022-23648` `CVE-2022-24769` `CVE-2022-24921` `CVE-2022-27191` `CVE-2022-27291` `CVE-2022-27650` `CVE-2022-27652` `CVE-2022-27664` `CVE-2022-2879` `CVE-2022-2880` `CVE-2022-28948` `CVE-2022-29526` `CVE-2022-2995` `CVE-2022-30065` `CVE-2022-32149` `CVE-2022-32190` `CVE-2022-3294` `CVE-2022-3358` `CVE-2022-39253` `CVE-2022-41715` `CVE-2022-41716` `CVE-2022-41717` `CVE-2022-41723` `CVE-2022-41724` `CVE-2022-4318` `CVE-2023-2253` `CVE-2023-2431` `CVE-2023-25173` `CVE-2023-25809` `CVE-2023-2650` `CVE-2023-27561` `CVE-2023-28642` `CVE-2023-28840` `CVE-2023-28841` `CVE-2023-28842` `CVE-2023-3676` `CVE-2023-39325` `CVE-2023-4448` `CVE-2023-44487` `CVE-2023-45142` `CVE-2023-45288` `CVE-2023-47108` `CVE-2023-48795` `CVE-2023-5363` `CVE-2023-5528` `CVE-2023-6476` `CVE-2024-21626` `CVE-2024-23650` `CVE-2024-23651` `CVE-2024-23652` `CVE-2024-23653` `CVE-2024-24783` `CVE-2024-24786` `CVE-2024-24789` `CVE-2024-24790` `CVE-2024-24791` `CVE-2024-25620` `CVE-2024-25621` `CVE-2024-26147` `CVE-2024-28180` `CVE-2024-3154` `CVE-2024-3177` `CVE-2024-34155` `CVE-2024-34156` `CVE-2024-34158` `CVE-2024-35255` `CVE-2024-3596` `CVE-2024-36118` `CVE-2024-3727` `CVE-2024-41110` `CVE-2024-45310` `CVE-2024-45336` `CVE-2024-45337` `CVE-2024-45338` `CVE-2024-45341` `CVE-2024-5154` `CVE-2024-5174` `CVE-2024-51744` `CVE-2024-5321` `CVE-2024-56171` `CVE-2024-6104` `CVE-2025-0426` `CVE-2025-0913` `CVE-2025-1097` `CVE-2025-1098` `CVE-2025-13281` `CVE-2025-1974` `CVE-2025-22866` `CVE-2025-22868` `CVE-2025-22869` `CVE-2025-22870` `CVE-2025-22871` `CVE-2025-22872` `CVE-2025-24030` `CVE-2025-24513` `CVE-2025-24514` `CVE-2025-24928` `CVE-2025-24965` `CVE-2025-25294` `CVE-2025-26519` `CVE-2025-27144` `CVE-2025-30157` `CVE-2025-30204` `CVE-2025-31133` `CVE-2025-32386` `CVE-2025-32387` `CVE-2025-35947` `CVE-2025-4563` `CVE-2025-4673` `CVE-2025-47906` `CVE-2025-47907` `CVE-2025-47912` `CVE-2025-47914` `CVE-2025-5187` `CVE-2025-52565` `CVE-2025-52881` `CVE-2025-53605` `CVE-2025-55198` `CVE-2025-55199` `CVE-2025-58058` `CVE-2025-58181` `CVE-2025-58183` `CVE-2025-58185` `CVE-2025-58186` `CVE-2025-58187` `CVE-2025-58188` `CVE-2025-61723` `CVE-2025-61724` `CVE-2025-61725` `CVE-2025-61726` `CVE-2025-61727` `CVE-2025-61729` `CVE-2025-61731` `CVE-2025-61732` `CVE-2025-62161` `CVE-2025-62596` `CVE-2025-64329` `CVE-2025-64527` `CVE-2025-64763` `CVE-2025-65637` `CVE-2025-66220` `CVE-2025-68121` `CVE-2026-22771` `CVE-2026-24051` `CVE-2026-24054` `CVE-2026-24834` `CVE-2026-25679` `CVE-2026-27145` `CVE-2026-29181` `CVE-2026-30892` `CVE-2026-31431` `CVE-2026-33186` `CVE-2026-33343` `CVE-2026-33413` `CVE-2026-34986` `CVE-2026-35469` `CVE-2026-39828` `CVE-2026-39835` `CVE-2026-39883` `CVE-2026-41326` `CVE-2026-41579` `CVE-2026-42504` `CVE-2026-42507` `CVE-2026-44210` `CVE-2026-46597` `CVE-2026-46598` `CVE-2026-46680` `CVE-2026-47243` `CVE-2026-47262` `CVE-2026-47766` `CVE-2026-47774` `CVE-2026-50195` `CVE-2026-53488` `CVE-2026-53489` `CVE-2026-53492`
