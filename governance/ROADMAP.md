# AUGMANITAI Public Roadmap

*Last updated: 2026-04-10. This roadmap is a living document. Dates are targets, not commitments.*

## Vision

AUGMANITAI aims to become the authoritative, interoperable, ISO-aligned terminology reference for human-AI interaction phenomena, consumable by both humans (researchers, practitioners) and machines (LLMs, agent frameworks, knowledge graphs, RAG systems).

## Current Version

**v1.0** — Initial compendium release
- ~120 terms across 6 domains (Meta-Cognitive, Compound Cognition, Multi-Agent/Swarm, Collective Intelligence, Prompt-Ontology Bridge, Infrastructure)
- DOI-published on Zenodo (10.5281/zenodo.19481331)
- CC BY-NC-ND 4.0 for data, Apache 2.0 for code
- Informed by ISO 704 / 1087 / 30042 (ISO-inspired, not ISO-certified — §16)
- Python package, NPM package, MCP server, REST API, SPARQL endpoint
- EN/DE primary; ZH/HI/AR stub translations for 25 core terms

## v1.1 — Consolidation (target: Q3 2026)

**Theme:** Depth over breadth. Fix, validate, harden.

- [ ] SHACL-complete validation of all existing terms (zero violations)
- [ ] Full German translations for all 120 terms (currently partial)
- [ ] API rate limiting and auth on reference deployment
- [ ] Integration tests for MCP + A2A + ANP + AG-UI protocol bridges
- [ ] GraphRAG benchmark published with baseline scores
- [ ] Test coverage ≥ 90% for augmanitai-python
- [ ] Documentation site (mdBook or Docusaurus) with cross-linked term pages

**Release cadence:** patch releases as needed; one minor release at quarter end.

## v1.2 — Community (target: Q4 2026)

**Theme:** Open the doors. Enable contribution.

- [ ] First external contributor term proposal accepted
- [ ] At least 1 domain steward appointed
- [ ] CLA-assistant or DCO bot integrated for PR workflow
- [ ] Public discussion forum (GitHub Discussions or Matrix)
- [ ] Quarterly term proposal review cycle established
- [ ] Translations: full ZH, HI, AR coverage for core 25 terms
- [ ] Accessibility review of explorer HTML (WCAG 2.1 AA)
- [ ] First independent citation of the deposit by an external author (peer-reviewed or not — observed, not pursued)

## v2.0 — Expansion (target: Q2 2027)

**Theme:** Breadth. Multilingual. Canonical.

- [ ] 250+ terms total
- [ ] 5 new domains (e.g., Memory, Persona, Deception, Alignment-Failure, Meta-Learning)
- [ ] Full translations: EN/DE/ZH/HI/AR/ES/FR/JA/KO/PT
- [ ] Wikidata integration: every term has a Q-id and bidirectional sitelinks
- [ ] OntoLex-Lemon export becomes canonical lexical representation
- [ ] Second priority deposit on Zenodo covering the v2.0 schema expansion
- [ ] Migration path from v1.x: semver-major breaking changes clearly documented

**Breaking changes expected in v2.0:** URI scheme finalization, relation vocabulary consolidation, deprecation of any v1.x experimental terms.

## v3.0 — Federation (target: 2028)

**Theme:** Beyond one repository.

- [ ] Federated term authority model: multiple institutional publishers cross-reference under a shared schema
- [ ] Semantic Web Triple Store hosting (public SPARQL endpoint)
- [ ] Official translations maintained by native-speaker committees
- [ ] Terminology citation patterns adopted by at least 3 independent downstream projects as voluntary reference (AUGMANITAI remains a descriptive dataset — §1, §11, §16, §20; no regulatory claim)
- [ ] Formal standardization submission (ISO, W3C CG, or similar)

## Beyond v3 — Speculative

- Living terminology with versioned drift tracking (an official "this term has changed" alerting system)
- Integration with W3C Decentralized Identifiers for term authorship provenance
- Automated term drift detection across LLM outputs (operationalized CIR metric)
- Voluntary uptake of AUGMANITAI terminology as a shared reference vocabulary in independent AI transparency and auditability discussions (AUGMANITAI itself remains a descriptive dataset with no regulatory status — §1, §16)

## Non-Goals

These are explicitly NOT on the roadmap, by design:

- Becoming a general AI ethics framework (we are terminology, not philosophy)
- Building our own LLM (we describe phenomena in LLMs, we don't train them)
- Commercial SaaS offering (licensing is NC; commercial use requires a separate agreement)
- Replacing existing terminology standards (we complement ISO, W3C, Wikidata)

## How to Influence This Roadmap

- Open an issue with the `roadmap` label
- Propose a new milestone via Discussion
- Submit term proposals — volume and quality will influence prioritization
- Sponsor a domain steward role (see `GOVERNANCE.md`)
