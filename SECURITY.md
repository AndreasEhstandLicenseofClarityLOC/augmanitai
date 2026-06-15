# Security Policy

## Scope

AUGMANITAI is primarily a terminology database, but the accompanying tooling (Python package,
MCP server, protocol adapters, JSON-LD / SHACL / TBX generators and validators) can process
untrusted input and therefore has a security surface.

**In scope:** the MCP server (`protocols/mcp/`), protocol bridges (`protocols/bridges/`),
ontology/provenance generators and validators, and any CI/CD configuration.

**Out of scope:** third-party dependencies (report upstream), clearly-marked non-production demo
code, theoretical attacks without a practical exploit, social engineering, and the editorial content
of the terminology definitions themselves (use normal Issues for those).

## Reporting a Vulnerability — responsible disclosure

Please report security issues **privately**. Do **not** open a public GitHub issue for a
security problem.

- **Preferred channel:** private [GitHub Security Advisory](https://github.com/AndreasEhstandLicenseofClarityLOC/augmanitai/security/advisories)
  for this repository.
- **Fallback channel:** email **ehstand.schule@gmail.com** with the subject line
  `AUGMANITAI SECURITY`. For sensitive details, send a first non-sensitive message and request a
  PGP key fingerprint before transmitting the full report.

Please include: a clear description, steps to reproduce (PoC if available), affected version(s),
your impact assessment, and any suggested mitigation.

## Response timeline (best effort, single-maintainer project)

- Acknowledgment: within 72 hours.
- Triage & severity assessment: within 7 days.
- Coordinated disclosure plan: within 14 days.
- Patch: depending on severity, typically within 30 days for high-severity issues.

## Safe Harbor

This project supports good-faith security research. If you make a good-faith effort to comply with
this policy, we will consider your research authorized, work with you to resolve the issue, and will
not pursue legal action related to that research.

## Disclosure

After a fix is released we will publish an advisory, credit the reporter (unless anonymity is
requested), and request a CVE if warranted.

## Contact

- **Maintainer:** Andreas Ehstand (ORCID [0009-0006-3773-7796](https://orcid.org/0009-0006-3773-7796))
- **Security email:** ehstand.schule@gmail.com (subject `AUGMANITAI SECURITY`)
- **Provider information:** see [`IMPRESSUM.md`](IMPRESSUM.md) in the repository root.

---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](DISCLAIMER.md)).*
