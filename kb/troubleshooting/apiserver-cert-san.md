---
id: TROUBLE-APISERVER_CERT_SAN
type: troubleshooting
title: "x509: certificate is valid for … not <address> (apiserver cert SAN)"
status: active
kubespray_version: ">=v2.29.0 <=v2.31.0"
kubernetes_version: ">=1.31 <=1.35"
component_version: null
verified_at: "2026-07-16"
confidence: confirmed
aliases:
  - x509 certificate is valid for
  - apiserver certificate SAN missing
  - certificate valid for not
  - supplementary_addresses_in_ssl_keys
  - kubectl x509 not valid for load balancer
  - apiserver cert does not include IP
tags:
  - troubleshooting
  - control-plane
  - certificates
  - apiserver
  - load-balancer
sources:
  - type: code
    path: roles/kubernetes/control-plane/tasks/kubeadm-setup.yml
    lines: "28-48"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/tasks/kubeadm-setup.yml
    note: "apiserver_sans composition (tag v2.31.0)"
  - type: code
    path: roles/kubernetes/control-plane/templates/kubeadm-config.v1beta4.yaml.j2
    lines: "352-355"
    url: https://github.com/kubernetes-sigs/kubespray/blob/v2.31.0/roles/kubernetes/control-plane/templates/kubeadm-config.v1beta4.yaml.j2
    note: "certSANs rendered from apiserver_sans (tag v2.31.0)"
relations:
  - type: see_also
    target: VARIABLE-SUPPLEMENTARY_ADDRESSES_IN_SSL_KEYS
  - type: see_also
    target: VARIABLE-APISERVER_LOADBALANCER_DOMAIN_NAME
  - type: see_also
    target: PRACTICE-CERTIFICATE_EXPIRY
---

# x509: certificate is valid for … not <address> (apiserver cert SAN)

## Summary

The kube-apiserver serving certificate is issued for a fixed list of names/IPs
(**certSANs**). Reach the API through an address **not** in that list — a new load
balancer, floating/VIP, public IP, or DNS name — and the TLS handshake fails with
`x509: certificate is valid for A, B, …, not <your address>`. The fix is to add the
address to **`supplementary_addresses_in_ssl_keys`** and **regenerate** the apiserver
certificate.

## Problem

`kubectl`, a load balancer health check, or an in-cluster client fails with:

```
x509: certificate is valid for kubernetes, kubernetes.default, …, 10.233.0.1,
<cp-node-ips>, not <the address you connected through>
```

Public API images/endpoints work from the control-plane nodes themselves but not via
the external endpoint.

## Context

- Applies to Kubespray `v2.29.0`–`v2.31.0` (kubeadm-issued apiserver cert).
- Kubespray builds `certSANs` from `apiserver_sans`
  (`roles/kubernetes/control-plane/tasks/kubeadm-setup.yml`), which **already** includes:
  `kubernetes[.default[.svc[.<dns_domain>]]]`, the API service IP (`kube_apiserver_ip`),
  `localhost`/`127.0.0.1`/`::1`, `apiserver_loadbalancer_domain_name`,
  `loadbalancer_apiserver.address`, `supplementary_addresses_in_ssl_keys`, and every
  control-plane node's `main_access_ip` / `main_ip` / default IPv4+IPv6 / hostname /
  FQDN / `kube_override_hostname`.
- So node IPs, hostnames, and a configured LB are covered automatically. The error
  appears for an endpoint **outside** that set — commonly an external LB VIP, a floating
  IP, a public DNS name, or a NAT address added after install.

## Diagnostics

- Read the error: it lists exactly which SANs the cert has — compare with the address
  you used.
- Inspect the live cert's SANs:
  `openssl x509 -in /etc/kubernetes/pki/apiserver.crt -noout -text | grep -A1 "Subject Alternative Name"`.
- Confirm the endpoint you're hitting (kubeconfig `server:` / LB target) and whether it
  is any of the auto-included values above.

## Known Issues

**Fix:**

1. Add the missing name/IP to **`supplementary_addresses_in_ssl_keys`** (a list) in
   inventory — e.g. the LB VIP, floating IP, or external DNS name. If the endpoint is a
   dedicated API LB, also set `apiserver_loadbalancer_domain_name` /
   `loadbalancer_apiserver`.
2. **Regenerate the apiserver certificate** — kubeadm does **not** add SANs to an
   existing cert. Remove the old `/etc/kubernetes/pki/apiserver.crt` and
   `apiserver.key` on each control-plane node, then re-run the control-plane role
   (`cluster.yml`, or the upgrade playbook) so kubeadm recreates the cert with the new
   SANs. `kubeadm certs renew apiserver` alone re-signs with the **same** SAN set and
   will **not** fix this. See [[PRACTICE-CERTIFICATE_EXPIRY]] for the renewal flow.
3. Restart kube-apiserver picks up the new cert (the role handles this on a full run).

**Gotchas:**

- Plan SANs **before** install when you know the external endpoint — adding them later
  forces a cert regeneration and apiserver restart.
- IPv6/dual-stack: include the IPv6 address too if clients reach the API over IPv6.
- Changing SANs does not change the CA — clients that already trust the cluster CA keep
  working once the leaf cert includes their address.

## References

- `apiserver_sans` (kubeadm-setup.yml:28-48) and `certSANs`
  (kubeadm-config template) at tag `v2.31.0`; knobs
  [[VARIABLE-SUPPLEMENTARY_ADDRESSES_IN_SSL_KEYS]],
  [[VARIABLE-APISERVER_LOADBALANCER_DOMAIN_NAME]].
