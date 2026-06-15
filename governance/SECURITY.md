# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.x     | :white_check_mark: |
| < 1.0   | :x:                |

The current major version receives security and correctness updates. Older versions are archived on Zenodo (DOI 10.5281/zenodo.20161494) but do not receive patches.

## Reporting a Vulnerability

AUGMANITAI is primarily a terminology database, not a production software system, but the accompanying tooling (Python package, MCP server, REST API, JSON-LD generators) can process untrusted input and therefore has a security surface.

If you discover a security issue, please report it privately. Do NOT open a public issue for security problems.

**Preferred channel:** private security advisory via GitHub Security Advisories (once the repository is public).

**Alternative channel:** encrypted email to the maintainer. Request the current PGP key fingerprint through the repository issue tracker (for a non-sensitive preliminary contact), then send the vulnerability details encrypted.

Please include:

1. A clear description of the vulnerability.
2. Steps to reproduce (proof of concept if available).
3. The affected version(s).
4. Your assessment of impact (data integrity, denial of service, information disclosure, etc.).
5. Any suggested mitigation.

## Response Timeline

- **Acknowledgment:** within 72 hours of receipt.
- **Triage and severity assessment:** within 7 days.
- **Coordinated disclosure plan:** within 14 days.
- **Patch release:** depending on severity, typically within 30 days for high-severity issues.

## Scope

**In scope:**

- Python package (`augmanitai-python/`)
- NPM package (`augmanitai-npm/`)
- MCP server (`protocols/mcp/`)
- REST API mock (`api-mock/`)
- FastAPI/Gradio/HuggingFace Space deployment configurations
- JSON-LD, SPARQL, SHACL, and TBX generators and validators
- CI/CD configurations

**Out of scope:**

- Third-party dependencies (report to upstream)
- Issues in demo code that is clearly marked as non-production
- Theoretical attacks without a practical exploit
- Social engineering attacks on maintainers
- Content of the terminology definitions themselves (these are editorial, not security matters — use normal Issues)

## Safe Harbor

The AUGMANITAI project supports good-faith security research. If you make a good-faith effort to comply with this policy during your security research, we will consider your research to be authorized, we will work with you to understand and resolve the issue quickly, and we will not recommend or pursue legal action related to your research.

## Disclosure Policy

After a patch is released, we will:

1. Publish a security advisory describing the issue and the fix.
2. Credit the reporter (unless they request anonymity).
3. Request a CVE identifier if the issue warrants one.

## Contact

**Maintainer:** Andreas Ehstand (ORCID [0009-0006-3773-7796](https://orcid.org/0009-0006-3773-7796))
**Preferred channel:** private [GitHub Security Advisory](https://github.com/AndreasEhstandLicenseofClarityLOC/augmanitai/security/advisories) (do not open a public issue).
**Fallback channel:** `augmanitai [at] gmail [dot] com` — please use the subject line `AUGMANITAI SECURITY` and request the PGP key fingerprint in a first non-sensitive message before sending details.
**Provider information:** see [`IMPRESSUM.md`](../IMPRESSUM.md) in the repository root.

---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](../DISCLAIMER.md)).*
