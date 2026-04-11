# Contributing to AUGMANITAI

Thank you for your interest in contributing to AUGMANITAI. This document describes how contributions are accepted and reviewed.

> **Precondition.** Every contributor is bound by the project's **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](DISCLAIMER.md)). By opening an issue or submitting a pull request you acknowledge that AUGMANITAI is descriptive linguistic-terminological research, a non-peer-reviewed longitudinal n=1 terminological priority deposit, 18+ only, and subject to the §20 restricted-applications clause. Contributions that reframe or repurpose the vocabulary for diagnostic, medical, HR screening, credit scoring, insurance, military/intel classification, surveillance, or profiling use will be rejected on sight.

Before contributing, please read:
- [Ethical Disclaimer §1–§20](DISCLAIMER.md) — mandatory
- [Code of Conduct](governance/CODE_OF_CONDUCT.md)
- [Governance and Maintainers](governance/MAINTAINERS.md)
- [Versioning Policy](governance/VERSIONING.md)
- [Release Policy](governance/RELEASE-POLICY.md)
- [Security Policy](governance/SECURITY.md)

## Types of contributions

AUGMANITAI is curated terminology work, not a commons of editable definitions. Different contribution types are handled differently.

### 1. Term proposals

New terms are the most carefully governed contribution. Use the [Term Proposal issue form](.github/ISSUE_TEMPLATE/term_proposal.yml).

Every term proposal must include:

- **Term name** in a well-formed form (no whitespace ambiguity, no unexplained acronyms)
- **Genus** — the superordinate concept (ISO 704-informed)
- **Differentia** — what distinguishes this term from its siblings (ISO 704-informed)
- **At least three characteristics** in the format "attribute : value"
- **At least two attestation sources** (published papers, standards, documented usage)
- **Proposed relations** to existing terms (`broader`, `narrower`, `related`)
- **A concrete usage example** in natural language

Term proposals that do not meet all six requirements will be closed with a request for revision.

Term proposals are reviewed by the maintainer. Acceptance is a MINOR version bump. Rejection is always explained.

### 2. Format extensions and serializations

Adding a new machine-readable serialization (e.g., a new JSON-LD profile, a new SHACL shape graph, a new export format) is welcomed. Open an issue first to discuss scope.

Requirements:
- The extension must be standards-based (ISO, W3C, OASIS, IETF, ECMA, or equivalent).
- It must be additive — no existing file may change semantics as a result.
- It must include a README in its own subdirectory explaining usage.
- It must include at least one validation test or parse check.

### 3. Tooling, scripts, demos

Code contributions (protocol servers, converters, validators, demo swarms) use pull requests.

Requirements:
- Signed-off commits ([Developer Certificate of Origin](governance/DCO.md)): `git commit -s -m "..."`.
- Passes existing tests (if any) and does not introduce regressions.
- Apache 2.0 licensed by default (see `licensing/LICENSE-code-apache`).
- No new runtime dependencies without discussion in an issue.
- PII-clean: no personal identifiers, API keys, tokens, or third-party data in the diff.

### 4. Documentation improvements

Fixes to typos, clarifications, better examples, translations of READMEs — very welcome. These are usually merged quickly.

### 5. Bug reports and feature requests

Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.yml) or [Feature Request](.github/ISSUE_TEMPLATE/feature_request.yml) issue forms.

## Pull request process

1. **Fork** the repository and create a feature branch (`git checkout -b feature/my-change`).
2. **Sign off** every commit: `git commit -s -m "Short description"`. This is a mandatory Developer Certificate of Origin acknowledgement.
3. **Keep changes focused** — one PR, one concern. Larger PRs will be asked to split.
4. **Update the CHANGELOG** under the `## [Unreleased]` section.
5. **Update documentation** — if behavior or files change, update the relevant README.
6. **Run validation** — for TTL/JSON-LD changes, run `riot --validate` or `rdflib` parse. For Python, run any present tests.
7. **Open a pull request** using the [PR template](.github/PULL_REQUEST_TEMPLATE.md).

### Review and merge

- All PRs are reviewed by the maintainer (Andreas Ehstand) until domain stewards are appointed.
- Reviews focus on: correctness, terminological rigor, standards compliance, test coverage, license hygiene.
- Merged PRs are squash-merged by default; exceptions for multi-commit sequences that are individually meaningful.

## Contributor License Agreement

For substantive contributions (more than a few lines, or any new file beyond trivial edits), a signed [Contributor License Agreement](governance/CLA.md) is required. For contributions on behalf of an organization, the [Corporate CLA](governance/CLA-entity.md) is required.

The CLAs grant the same dual license that governs the repository (CC BY-NC-ND 4.0 for data, Apache 2.0 for code) and include a patent non-assertion.

## Code of Conduct

All interaction — issues, pull requests, discussions — is governed by the [Code of Conduct](governance/CODE_OF_CONDUCT.md), which adapts Contributor Covenant 2.1 with an added academic-misconduct clause (plagiarism, fabrication, attribution violations are grounds for immediate ban).

## Questions

For questions that are not bugs or feature requests, open a GitHub Discussion (if enabled) or reach the maintainer via [ORCID](https://orcid.org/0009-0006-3773-7796).
