# AUGMANITAI

> A terminology framework for human–AI interaction. 1000 curated terms, informed by ISO 704 / ISO 1087 / ISO 30042 (ISO-inspired, not ISO-certified), Semantic Web native.

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.19481331-blue)](https://doi.org/10.5281/zenodo.19481331)
[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
[![License: Apache 2.0](https://img.shields.io/badge/Code%20License-Apache%202.0-green)](https://www.apache.org/licenses/LICENSE-2.0)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0006--3773--7796-A6CE39?logo=orcid)](https://orcid.org/0009-0006-3773-7796)

**Author:** Andreas Ehstand
**Concept DOI:** [10.5281/zenodo.19481331](https://doi.org/10.5281/zenodo.19481331)
**Status:** Priority-establishing terminological deposit. The 1000-Term Compendium is the curated output of a **longitudinal n=1 observation** of daily human–LLM interaction over approximately nine months, published as a timestamped Zenodo record with Semantic Web format extensions, validation shapes, and reference infrastructure. This is **not** a peer-reviewed publication and does not target one; see [METHODOLOGY.md §2.0](METHODOLOGY.md#20-study-design-longitudinal-n1) and [§11](METHODOLOGY.md#11-what-peer-review-would-add--and-why-this-work-does-not-target-it) for the design rationale.

---

## ⚠️ Ethical Disclaimer (§1–§20) — please read before use

AUGMANITAI is **purely descriptive linguistic-terminological research** into phenomena observable at the human–AI interface. It is **not normative**, makes **no recommendations for action**, and is **not a diagnostic, medical, psychological, legal, or screening instrument**.

- **§1 Descriptive, not normative.** Naming a phenomenon is not an endorsement, recommendation, or evaluation of the described behavior.
- **§11 Independent research.** No external funding, no sponsorship, **longitudinal n=1 terminological priority deposit (non-peer-reviewed per §11).**
- **§13 No efficacy claims.** Not a substitute for professional advice (medical, psychological, legal, financial).
- **§7 18+ only.** The contents are intended exclusively for adult users.
- **§16 ISO-inspired, not ISO-certified.** The framework is informed by ISO 704 / ISO 1087 / ISO 30042; it is not an ISO-certified deliverable.
- **§20 Restricted application.** The terms, definitions, and descriptions **must not be used as** diagnostic labels, medical classification, psychological screening, legal categorization, military or intelligence classification, HR screening, credit scoring, insurance assessment, state surveillance systems, or profiling mechanisms.

The full bilingual §1–§20 disclaimer is in [**DISCLAIMER.md**](DISCLAIMER.md) and applies to every file, every term, and every serialization in this repository.

The disclaimer is complemented by two transparency documents that every reviewer, replicator, or critic is expected to read:

- [**METHODOLOGY.md**](METHODOLOGY.md) — how the 1000 terms were elicited, selected, annotated, and validated. Documents the **longitudinal n=1 design** of the observation window, the scope boundaries of a single-observer deposit (B1–B10), the three origin categories of the terms (imported / re-formulated / newly introduced), model- and language-coverage constraints, and the circularity risk inherent to any published terminology.
- [**DUAL_USE_STATEMENT.md**](DUAL_USE_STATEMENT.md) — foreseeable misuse vectors (jailbreak engineering, clinical misuse, HR/credit/insurance profiling, surveillance, disinformation seeding, training-data contamination, reflexive self-misuse), how §20 mitigates each, and which residual risks remain.

**Fictional examples only.** Where definitions in this repository are illustrated by examples of human–LLM interaction, the examples are either fully synthetic or de-identified paraphrases of public discussion. No private chat logs, correspondence, or re-identifiable third parties appear in any term, definition, example, or serialization. See [METHODOLOGY.md §5](METHODOLOGY.md#5-fictional-and-synthetic-examples-only).

**Note on the word "phenomenology".** Where this repository uses the word *phenomenology* or *phenomenal*, it means *observable regularities that can be named and described*. It does **not** invoke the Husserlian, Merleau-Pontian, or broader continental-philosophical tradition of phenomenology. No claims from that tradition are transferred to AUGMANITAI. See [METHODOLOGY.md §7](METHODOLOGY.md#7-use-of-phenomenology).

License: CC BY-NC-ND 4.0 (data) · Apache-2.0 (code). Jurisdiction: Munich, Germany.

---

## What AUGMANITAI is

AUGMANITAI is a structured terminology for phenomena that arise at the interface between humans and large language models. The core deliverable is the **1000-Term Compendium**: a curated set of terms, each with definition, genus/differentia structure, characteristics, and relations — published under a permanent DOI and formalized as an RDF knowledge graph.

The compendium is the curated output of a **longitudinal n=1 observation** conducted by a single observer over approximately nine months of daily, extended human–LLM interaction. It is a timestamped case record, comparable in form to a longitudinal case report or a qualitative single-subject study, transposed onto the human–LLM interaction domain.

**What is claimed and what is not.** AUGMANITAI v1.0 claims priority on the **schema as a whole** — the selection, definition, relation structure, and W3C-native serialization, deposited on Zenodo with a cryptographically anchored timestamp. It does **not** claim invention of every individual term: some are drawn from existing literature, some are re-formulations of terms already in use, and some are labels newly introduced by the curator where no existing term fit. The three origin categories are described in [METHODOLOGY.md §3](METHODOLOGY.md#3-selection-and-inclusion-criteria). A reader who identifies prior art for any term is welcome — the correct response is attribution, not rebuttal.

The framework is intended as a research instrument. It is not a product, not a methodology, and not a manifesto. Terms are tools for observation.

## What is in this repository

| Directory | Contents |
|---|---|
| [`ontology/`](ontology/) | Core OWL ontology, SKOS concept scheme, OntoLex-Lemon, SKOS-XL, JSON-LD context, SHACL shapes, TBX export |
| [`protocols/`](protocols/) | MCP, A2A, ANP, and AG-UI protocol adapters for agent integration |
| [`provenance/`](provenance/) | C2PA manifests, AI-SBOM (SPDX 3.0 + CycloneDX 1.6 ML-BOM), W3C Verifiable Credentials 2.0 |
| [`well-known/`](well-known/) | `llms.txt` — LLM discoverability pointer to the canonical Zenodo DOI |
| [`graphrag-variants/`](graphrag-variants/) | GraphRAG integration examples (Microsoft, LlamaIndex, LangGraph, HippoRAG, LazyGraphRAG, FalkorDB) |
| [`demo-swarms/`](demo-swarms/) | Reference multi-agent examples (LangGraph, CrewAI, AutoGen) with mock LLMs |
| [`governance/`](governance/) | Code of Conduct, CLA, DCO, Security, Maintainers, Roadmap, Versioning |
| [`licensing/`](licensing/) | Dual-license files (CC BY-NC-ND 4.0 for data, Apache 2.0 for code), SPDX, PATENT, TRADEMARK, NOTICE |

## Quick start

### Load the ontology

```bash
# Apache Jena
riot --validate ontology/augmanitai-ontology.ttl

# rdflib (Python)
python3 -c "import rdflib; g=rdflib.Graph(); g.parse('ontology/augmanitai-ontology.ttl'); print(len(g), 'triples')"
```

### Validate data with SHACL

```bash
pip install pyshacl
pyshacl -s ontology/validation/shacl-shapes/term-shapes.ttl \
        -d ontology/augmanitai-ontology.ttl
```

### Explore with GraphRAG

See [`graphrag-variants/`](graphrag-variants/) for six integration examples with mock LLMs that run offline.

## Standards the framework is informed by

Per §16 of the Ethical Disclaimer, AUGMANITAI is **ISO-inspired, not ISO-certified**. The table below lists the standards whose principles informed the methodology; it does not assert certification, conformance, or official approval by any standards body.

| Standard | Role |
|---|---|
| ISO 704:2022 | Terminology work — principles and methods (informed by) |
| ISO 1087:2019 | Terminology work — vocabulary (informed by) |
| ISO 30042:2019 | TermBase eXchange (TBX) serialization (informed by) |
| W3C SKOS | Concept scheme |
| W3C SKOS-XL | Extended labels with per-label provenance |
| W3C OntoLex-Lemon | Lexical layer |
| W3C SHACL | Validation shapes |
| W3C JSON-LD 1.1 | Web-native serialization |
| W3C Verifiable Credentials 2.0 | Content provenance |
| SPDX 3.0 AI Profile | Bill of materials |
| C2PA 2.0 | Content credentials |

## Licensing

AUGMANITAI uses a **dual-license model**. The two licenses cover disjoint sets of files — there are no mixed-license files in this repository.

**Data layer — [CC BY-NC-ND 4.0](licensing/LICENSE-data):**

- `.ttl`, `.rdf`, `.owl`, `.nt`, `.nq` (RDF serializations)
- `.jsonld`, `.json-ld` (JSON-LD 1.1)
- `.tbx` (TermBase eXchange)
- `.csv`, `.tsv` files containing terminology or definitional content
- `.md` files whose primary content is terminological or definitional (this README, `DISCLAIMER.md`, `METHODOLOGY.md`, `DUAL_USE_STATEMENT.md`, `CHANGELOG.md`, files under `governance/`, `licensing/`, `provenance/`, `well-known/`)
- `CITATION.cff`, `.zenodo.json`

**Code layer — [Apache License 2.0](licensing/LICENSE-code-apache):**

- `.py`, `.js`, `.ts`, `.sh` (scripts, demos, tooling, protocol servers)
- `.yml`, `.yaml` (CI workflows, GitHub Actions)
- Dockerfiles, Makefiles, shell configuration

**SPDX expression:** `CC-BY-NC-ND-4.0 AND Apache-2.0`

**No mixed works.** The repository deliberately avoids files that combine terminological content (which is *data* and non-derivable) with executable logic (which is *code* and permissively licensable). A Python script that *loads* an ontology is Apache-2.0; the ontology it loads is CC BY-NC-ND 4.0. A demo that embeds term definitions inline must either split into two files or be treated as a data file.

**Contribution implications.**

- A pull request against any file in the data layer constitutes a *derivative work* under CC BY-NC-ND 4.0 and is **not accepted** under the ND (no-derivatives) clause. Term proposals instead use the [Term Proposal issue form](.github/ISSUE_TEMPLATE/term_proposal.yml); the maintainer incorporates accepted proposals by authoring new files under the curator's license.
- A pull request against any file in the code layer is accepted under the [Developer Certificate of Origin](governance/DCO.md) (`git commit -s`) and becomes licensed under Apache-2.0.
- Larger code contributions may require a [Contributor License Agreement](governance/CLA.md).

See [`licensing/`](licensing/) for the full policy, patent non-assertion, trademark guidance, and third-party attributions.

For **commercial licensing inquiries** regarding the data layer, contact the author via ORCID.

## Citation

```bibtex
@dataset{ehstand_augmanitai,
  author       = {Ehstand, Andreas},
  title        = {AUGMANITAI: 1000-Term Compendium},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.19481331},
  url          = {https://doi.org/10.5281/zenodo.19481331}
}
```

A machine-readable citation is available in [`CITATION.cff`](CITATION.cff).

## Contributing

AUGMANITAI is curated terminology work, not an open commons of editable definitions. All contributors acknowledge and accept the Ethical Disclaimer ([`DISCLAIMER.md`](DISCLAIMER.md), §1–§20) as a precondition of contribution. Contributions are welcome but governed:

- **Term proposals** use the [Term Proposal issue form](.github/ISSUE_TEMPLATE/term_proposal.yml) and follow an ISO 704-informed structure (genus, differentia, at least three characteristics, at least two attestation sources).
- **Format and tooling contributions** use standard pull requests and require a signed [Developer Certificate of Origin](governance/DCO.md) (`git commit -s`).
- **Larger contributions** may require a [Contributor License Agreement](governance/CLA.md).

All contributors agree to the [Code of Conduct](governance/CODE_OF_CONDUCT.md).

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## Security

Vulnerabilities and security concerns: see [SECURITY.md](governance/SECURITY.md). Do not report security issues via public GitHub issues.

## Governance

- **Maintainer:** Andreas Ehstand (BDFL during research preview phase)
- **Roadmap:** [governance/ROADMAP.md](governance/ROADMAP.md)
- **Versioning:** [governance/VERSIONING.md](governance/VERSIONING.md) (SemVer adapted for terminology)
- **Release policy:** [governance/RELEASE-POLICY.md](governance/RELEASE-POLICY.md)

## Legal

- [**IMPRESSUM**](IMPRESSUM.md) — Anbieter-Angaben gemäß § 5 TMG / provider information per § 5 German Telemedia Act
- [**DISCLAIMER.md**](DISCLAIMER.md) — Ethical Disclaimer §1–§20 (bilingual DE/EN)
- [**LICENSE**](LICENSE) — CC BY-NC-ND 4.0 (data) · Apache-2.0 (code); see [`licensing/LICENSE-summary.md`](licensing/LICENSE-summary.md)

## Related work

- [Zenodo record](https://doi.org/10.5281/zenodo.19481331) — canonical published version with DOI
- [ORCID profile](https://orcid.org/0009-0006-3773-7796) — author identity

## Acknowledgements

Built on the shoulders of ISO, W3C, DCMI, PROV-O, schema.org, SPDX, C2PA, Wikidata, the MCP/A2A/ANP/AG-UI communities, and the Contributor Covenant. Full attributions in [licensing/NOTICE](licensing/NOTICE).

## Ecosystem

AUGMANITAI is the foundation of the MANITAI framework ecosystem:

- **[NEOMANITAI](https://github.com/AndreasEhstandLicenseofClarityLOC/neomanitai-terms)** — 6182 terms across 54 domains, extending the 1000-term core
- **[PERMANITAI](https://github.com/AndreasEhstandLicenseofClarityLOC/permanitai-framework)** — Universal Performance Factor Analysis for Intelligent Entities, transferring sports science Leistungsfaktorenanalyse to AI models, agents, robots, drones, hybrid systems, business teams, world-class performers, and managers
- **ROBMANITAI** — 750 robotics-specific terms (subsumed by PERMANITAI)
