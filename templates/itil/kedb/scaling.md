# KEDB · scaling

_2 известных ошибок. Сгенерировано; не править руками._

### KEDB-163 · HorizontalPodAutoscaler not scaling (unknown / metrics unavailable)
- **Симптом:** `kubectl get hpa` shows `TARGETS: <unknown>/50%` and `REPLICAS` not changing; `kubectl describe hpa` shows `FailedGetResourceMetric` / `unable to get metrics` / `missing request for cpu`
- **Затронутые CIs:** autoscaling, hpa, metrics  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0`. CPU/memory HPAs use the **metrics.k8s.io** API served by **metrics-server** (`metrics_server_enabled`, off by default — ) · HPA utilization = usage ÷ **request**; without a request there's no denominator
- **Workaround / fix:** **metrics-server not installed** — enable it (`metrics_server_enabled: true`); no metrics API → every resource-metric HPA is `<unknown>` · **metrics-server can't scrape kubelet (`x509`)** — the classic Kubespray default: kubelet serving cert is self-signed and metrics-server needs `--kubelet-insecure-tls` (`metrics_server_kubelet_insecure_tls: true`, the default) or a rotated serving cert · **`missing request for cpu…
- **Источник:** `kb/troubleshooting/hpa-not-scaling.md`

### KEDB-164 · KEDA: ScaledObject not scaling / HPA stuck
- **Симптом:** Replicas stay flat despite load; or scale-to-zero never wakes on events · `ScaledObject` shows `Ready: False` / `Fallback` conditions · HPA exists but reports `unable to get external metric`
- **Затронутые CIs:** keda, autoscaling  ·  _>=2.17.0 <=2.20.1_
- **Root cause:** Applies to KEDA **2.17–2.20** (owner runs 2.17.2 — ). It drives a standard HPA — still applies
- **Workaround / fix:** **KEDA 2.17.2** has a Vault-credential path-traversal CVE (**CVE-2025-68476**, fixed 2.17.3) — relevant if using the Vault trigger-auth provider · KEDA follows an **N-2 Kubernetes** support policy (2.17 tested 1.30–1.32); running outside the tested window can cause metric-API oddities
- **Источник:** `kb/troubleshooting/keda-scaledobject-not-scaling.md`

