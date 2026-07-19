# KEDB · dns

_5 известных ошибок. Сгенерировано; не править руками._

### KEDB-058 · CoreDNS crashloop: 'Loop … detected'
- **Симптом:** The `forward . /etc/resolv.conf` in the Corefile inherits the node's resolv.conf; if that resolv.conf points at a resolver that loops back (e.g. 127.0.0.1 systemd-resolved stub, or the nodelocaldns/cluster IP), CoreDNS detects a query loop and exits
- **Затронутые CIs:** operations, dns  ·  _>=v2.29.0 <=v2.31.0_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0` clusters. This is a general Kubernetes/component operational issue (not tied to one Kubespray version); the relevant tunables are noted in Known Issues
- **Workaround / fix:** Point the node's upstream resolv.conf at a real external resolver (`upstream_dns_servers` / `resolvconf_mode`, see TAG-RESOLVCONF), or configure CoreDNS `forward` to a real upstream. Do not let the resolver chain loop back to CoreDNS
- **Источник:** `kb/troubleshooting/coredns-resolution-loop.md`

### KEDB-059 · CoreDNS: intermittent/slow DNS resolution in pods
- **Симптом:** Occasional `SERVFAIL`/timeouts; app retries succeed · ~5s latency on some external lookups · CoreDNS pods high CPU or `CrashLoopBackOff`
- **Затронутые CIs:** coredns, dns, networking  ·  _>=1.11.0 <=1.14.6_
- **Root cause:** Applies to CoreDNS **1.11–1.14.6** (base ≤1.12.4 — )
- **Workaround / fix:** On `systemd-resolved` nodes the upstream may be a stub (`127.0.0.53`) — ensure the real upstream nameservers are used, not just the stub
- **Источник:** `kb/troubleshooting/coredns-intermittent-dns.md`

### KEDB-060 · coredns: known CVEs by shipped version (osv.dev)
- **Симптом:** Each shipped coredns version carries the CVEs listed below (osv.dev returns only vulnerabilities that affect the queried version, so this is authoritative affectedness)
- **Затронутые CIs:** security, cve, coredns  ·  _>=v2.29.0 <=v2.31.0 / >=1.11.3 <=1.12.4_
- **Root cause:** | Component version | Kubespray | # CVEs | CVEs | |---|---|---|---| | 1.11.3 | v2.29.x (k8s 1.31/1.32) | 10 | CVE-2025-47950, CVE-2025-58063, CVE-2025-68151, CVE-2026-26017, CVE-2026-26018, CVE-2026-32934, CVE-2026-32936, CVE-2026-33190, CVE-2026-33489, CVE-2026-35579 | | 1.12.0 | v2.29.x (k8s 1.33) | 10 | CVE-2025-47950, CVE-2025-58063, CVE-2025-68151, CVE-2026-26017, CVE-2026-26018, CVE-2026-32934, CVE-2026-32936, …
- **Workaround / fix:** **CVE-2025-47950** [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H] — CoreDNS Vulnerable to DoQ Memory Exhaustion via Stream Amplification — fixed in: `1.12.2` · **CVE-2025-58063** [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:L/A:H] — CoreDNS: DNS Cache Pinning via etcd Lease ID Confusion — fixed in: `1.12.4` · **CVE-2025-68151** [CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:N/VI:N/VA:H/SC:N/SI:N/SA:N/E:U] — CoreDNS gRPC/HTTPS/HTTP…
- **Источник:** `kb/troubleshooting/coredns-known-cves.md`

### KEDB-061 · NodeLocal DNS: IPv6 nodelocaldns_ip not handled in config
- **Симптом:** The `nodelocaldns-config.yml.j2` template did not correctly handle an IPv6 `nodelocaldns_ip`; the fix renders it properly for IPv6
- **Затронутые CIs:** —  ·  _>=v2.29.0 <=v2.30.0_
- **Root cause:** Affected Kubespray: `>=v2.29.0 <=v2.30.0`. Fixed in: `v2.31.0` · Confirmed via the merged PR #13087 and the tag code
- **Workaround / fix:** Root cause fixed by PR #13087 (in `roles/kubernetes-apps/ansible/templates/nodelocaldns-config.yml.j2`). Workaround before upgrading: use an IPv4 `nodelocaldns_ip`, or upgrade to v2.31.0 for IPv6 support. The durable fix is to upgrade to `v2.31.0` or later
- **Источник:** `kb/troubleshooting/nodelocaldns-ipv6-ip-render.md`

### KEDB-062 · Pods can't resolve external DNS (upstream forwarding)
- **Симптом:** Cluster service names resolve, but external domains (e.g. `github.com`) return `SERVFAIL`/`NXDOMAIN`/timeout from inside pods; or **all** DNS fails if NodeLocal DNS is the sole resolver in the pod's `resolv.conf` and it's unhealthy
- **Затронутые CIs:** dns, coredns, nodelocaldns, networking  ·  _>=v2.29.0 <=v2.31.0 / >=1.31 <=1.35_
- **Root cause:** Applies to Kubespray `v2.29.0`–`v2.31.0`. Defaults: `dns_mode: coredns`, `enable_nodelocaldns: true`, `nodelocaldns_ip: 169.254.25.10`, `upstream_dns_servers: []`, `resolvconf_mode: host_resolvconf`, `ndots: 2` · With `upstream_dns_servers` **empty**, external queries are forwarded to the **host's** upstream nameservers (from `/etc/resolv.conf`). If the host can't resolve externally, neither can pods · Kubespray sets…
- **Workaround / fix:** **Set explicit upstreams:** define `upstream_dns_servers: [<ip>, <ip>]` (e.g. internal resolvers) instead of relying on the host's `/etc/resolv.conf`. Re-run so CoreDNS/ NodeLocal DNS pick it up · **Fix the host resolver:** if using the default (empty `upstream_dns_servers`), ensure each node's `/etc/resolv.conf` has a working nameserver; `resolvconf_mode` (`host_resolvconf`) governs how it's managed · **NodeLocal DN…
- **Источник:** `kb/troubleshooting/dns-external-resolution.md`

