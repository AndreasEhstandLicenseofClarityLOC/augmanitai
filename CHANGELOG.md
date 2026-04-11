# Changelog

All notable changes to this repository are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). AUGMANITAI uses a terminology-adapted [Semantic Versioning](governance/VERSIONING.md):

- **MAJOR** — term removal, term rename, incompatible definition change
- **MINOR** — new terms, new relations, new format serializations (additive only)
- **PATCH** — typographical fixes, metadata corrections, non-semantic refinements

---

## [Unreleased]

### Added
- GitHub repository scaffolding for the 1000-Term Compendium.
- `DISCLAIMER.md` — bilingual (DE/EN) Ethical Disclaimer §1–§20, applied to the entire repository.
- Governance, licensing, issue templates, PR template, Code of Conduct, CLA, DCO, Security policy.
- Protocol adapters: MCP, A2A, ANP, AG-UI.
- Provenance: C2PA, AI-SBOM (SPDX 3.0 + CycloneDX 1.6 ML-BOM), W3C VC 2.0 — with generic EXAMPLE_SYSTEM demo.
- Well-known discovery: `llms.txt` pointing to the canonical Zenodo DOI.
- GraphRAG variants: Microsoft, LlamaIndex, LangGraph, HippoRAG, LazyGraphRAG, FalkorDB.
- Demo swarms: LangGraph, CrewAI, AutoGen reference examples with mock LLMs.

### Notes
- This repository contains a non-peer-reviewed longitudinal n=1 terminological priority deposit (§11; see METHODOLOGY.md §2.0).
- Framework is ISO-inspired, not ISO-certified (§16).
- Restricted applications per §20: no diagnostic, medical, HR, credit-scoring, surveillance, or profiling use.

## [1.1.0] — 2026-04

### Added
- OntoLex-Lemon serialization.
- SKOS-XL extended labels.
- SHACL validation shapes (terms + relations).
- TBX (ISO 30042:2019) export.
- JSON-LD 1.1 context and frame.

### Fixed
- Missing `@prefix rdf:` declaration in SKOS-XL TTL (typographical).

### Unchanged
- All terms, definitions, and relations from v1.0.
- Licensing (CC BY-NC-ND 4.0).

## [1.0.0] — 2024

### Initial release
- 1000-Term Compendium.
- Core OWL ontology, SKOS concept scheme.
- Published on Zenodo: [10.5281/zenodo.19481331](https://doi.org/10.5281/zenodo.19481331).
- License: CC BY-NC-ND 4.0.
