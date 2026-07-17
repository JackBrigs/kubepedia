---
id: TROUBLE-K8S_CERTS_RENEW_BROKEN_SCRIPT
type: troubleshooting
title: "control-plane: k8s-certs-renew script broken by bad quoting"
status: active
kubespray_version: ">=v2.29.0 <=v2.29.1"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - k8s-certs-renew-broken-script
tags:
  - troubleshooting
sources:
  - type: pull_request
    url: https://github.com/kubernetes-sigs/kubespray/pull/12876
    note: "fix merged in v2.30.0 (PR #12876)"
  - type: code
    path: roles/kubernetes/control-plane/templates/k8s-certs-renew.sh.j2
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.30.0/roles/kubernetes/control-plane/templates/k8s-certs-renew.sh.j2
    note: "fixed file"
relations:
  - type: see_also
    target: CONCEPT-CLUSTER_PKI
---

# control-plane: k8s-certs-renew script broken by bad quoting

## Summary

The generated certificate-renewal helper script failed because an improperly quoted variable assignment was interpreted by the shell as a command. Fixed in **v2.30.0** (PR #12876).

## Problem

In `k8s-certs-renew.sh.j2` an unquoted assignment made the shell try to execute it as a command; the variable was unused, so the fix simply removed the line. The broken line could make the renew timer/script error out.

## Context

- Affected Kubespray: `>=v2.29.0 <=v2.29.1`. Fixed in: `v2.30.0`.
- Confirmed via the merged PR #12876 and the tag code.

## Diagnostics

```bash
systemctl status k8s-certs-renew.service --no-pager   # errored?
journalctl -u k8s-certs-renew.service -n 30 --no-pager
```

## Known Issues

Root cause fixed by PR #12876 (in `roles/kubernetes/control-plane/templates/k8s-certs-renew.sh.j2`). Workaround before upgrading: renew certs manually with `kubeadm certs renew all` (see PRACTICE-CERTIFICATE_EXPIRY). The
durable fix is to upgrade to `v2.30.0` or later.

## References

- PR https://github.com/kubernetes-sigs/kubespray/pull/12876 — fixed in `v2.30.0`.
- `roles/kubernetes/control-plane/templates/k8s-certs-renew.sh.j2`.
