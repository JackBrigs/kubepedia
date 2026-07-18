# Upgrade & Change Report — inventory intake (demo)

`scripts/upgrade_report.py` is the first consumer **handle** over the Kubepedia KB:
given two Kubespray versions (and optionally your inventory) it emits a personalized,
source-linked upgrade report from the KDS docs.

## Try it

```bash
# full (unfiltered) report — Russian framing by default (the admin reads Russian)
.venv/bin/python scripts/upgrade_report.py --from v2.28.1 --to v2.31.0

# personalized to an inventory (this demo fixture)
.venv/bin/python scripts/upgrade_report.py --from v2.28.1 --to v2.31.0 \
    --inventory scripts/examples/sample-inventory -o report.md

# English framing
.venv/bin/python scripts/upgrade_report.py --from v2.28.1 --to v2.31.0 --lang en
```

**Language.** The report's own headers/labels/descriptions are **Russian by default**
(`--lang ru`), because the operator reading it is Russian-speaking. Verbatim excerpts
pulled from the KDS docs stay **English** (the KB's knowledge language) — the script is
deterministic and doesn't translate doc bodies; each quoted fact links to its source.
Use `--lang en` for a fully English report.

## What the intake reads

Point `--inventory` at a Kubespray inventory dir (or a single vars file). It scans
`*.yml`/`*.yaml` for the settings that decide relevance:

| Setting | Effect on the report |
|---|---|
| `kube_network_plugin` | keep only your CNI's notes; drop the other CNIs; link its deep version-jump doc (e.g. Cilium) |
| `container_manager` | keep your runtime (containerd/crio/docker); drop the others |
| `kube_proxy_mode` | shown in the profile |
| `kube_version` | shown in the profile |
| `cloud_provider` / `external_cloud_provider` | adds the external cloud-controller-manager section |
| `*_enabled` add-ons (`metallb_enabled`, `cert_manager_enabled`, `argocd_enabled`, …) | keep enabled add-ons; drop disabled ones; link deep docs (e.g. Argo CD) |

Anything not in your inventory is removed from the report and listed under
**"Filtered out"** for transparency.

`sample-inventory/` is a minimal fixture (Cilium + containerd + OpenStack cloud +
a few add-ons) so the personalization is visible end-to-end.
