---
id: TROUBLE-CLOCK_SKEW_TLS
type: troubleshooting
title: "x509 / TLS errors from node clock skew"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: null
component_version: null
verified_at: "2026-07-16"
confidence: probable
aliases:
  - clock-skew-tls-errors
tags:
  - troubleshooting
  - operations
  - security
sources:
  - type: docs
    url: https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/
    note: "kubeadm troubleshooting"
relations:
  - type: see_also
    target: PRACTICE-CERTIFICATE_EXPIRY
---

# x509 / TLS errors from node clock skew

## Summary

Components fail with `x509: certificate has expired or is not yet valid` even though certs are valid — the node clock is wrong.

## Problem

TLS validates certificate NotBefore/NotAfter against the local clock. A node with significant clock skew (NTP not running/synced) rejects otherwise-valid certificates and can fail kubeadm join / API access.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` clusters. This is a general Kubernetes/component operational issue (not tied to one Kubespray version); the relevant tunables are noted in Known Issues.

## Diagnostics

```bash
timedatectl                          # NTP synchronized? clock correct?
date -u
journalctl -u chronyd -u systemd-timesyncd -n 20 --no-pager 2>/dev/null
```

## Known Issues

Enable/verify NTP (`ntp_enabled`, see the ntp run-tag/variables) and let clocks sync; then retry. Certificate expiry itself is covered by PRACTICE-CERTIFICATE_EXPIRY.

## References

- https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/ — kubeadm troubleshooting (verified behavior, 2026-07-16).
