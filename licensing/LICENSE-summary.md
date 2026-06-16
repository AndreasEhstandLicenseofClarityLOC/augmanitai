# AUGMANITAI Dual-License Summary

AUGMANITAI uses a **dual-license scheme** that separates the terminology data from the tooling code:

| Component | License | SPDX Identifier |
| --- | --- | --- |
| Terminology data (terms, relations, definitions, translations, ontology files) | Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International | `CC-BY-NC-ND-4.0` |
| Code (Python package, NPM package, MCP server, API, GraphRAG scripts, deployment configs) | Apache License 2.0 | `Apache-2.0` |
| Selected utility snippets (optional) | MIT License | `MIT` |

The combined SPDX expression for the project is:

    CC-BY-NC-ND-4.0 AND Apache-2.0

## Why Dual-License?

**The data** is scholarly output. It is the curated result of a longitudinal n=1 terminology observation and a priority-establishing deposit on Zenodo. CC BY-NC-ND 4.0 protects the editorial integrity of the compendium: others may cite and reference individual terms freely, but they cannot fork the compendium, relabel it, or commercialize derivatives without a separate agreement.

**The code** is infrastructure. It is the plumbing that makes the data queryable, validatable, and integrable into other systems. Apache 2.0 maximizes adoption: anyone — commercial or non-commercial — can build on the code without friction, which accelerates the reach of the data underneath.

This is the same pattern used by other data-centric open projects (Wikidata's code is Apache/GPL, the data itself is CC0; many academic datasets pair restrictive data licenses with permissive code licenses).

## What This Means for You

### If you are a researcher or academic
You can use AUGMANITAI freely for research, teaching, and publication:
- Cite individual terms in papers (with attribution)
- Build academic tools on top of AUGMANITAI code (Apache 2.0)
- Train research models on AUGMANITAI data (non-commercial AI training requires prior written permission)
- Publish results that reference AUGMANITAI terms

### If you are an open-source developer
You can integrate AUGMANITAI into your open-source projects:
- Use the Python/NPM packages under Apache 2.0
- Use the code freely; contribute improvements back
- Reference terms by URI in your own knowledge graph
- **Cannot** redistribute modified term definitions under the AUGMANITAI name

### If you are a commercial user
Most commercial uses of AUGMANITAI require a separate license:
- Using AUGMANITAI code in your product is permitted under Apache 2.0
- Using AUGMANITAI data in a commercial product is NOT permitted without a commercial license
- Commercial AI training on AUGMANITAI data is NOT permitted without a commercial license
- Please contact the author for commercial licensing terms (see below)

## How to Attribute

Every use of AUGMANITAI — commercial or non-commercial — must include attribution:

```
AUGMANITAI Terminology Compendium
by Andreas Ehstand (ORCID 0009-0006-3773-7796)
DOI: 10.5281/zenodo.20161494
Licensed under CC BY-NC-ND 4.0 (data) and Apache 2.0 (code)
https://doi.org/10.5281/zenodo.20161494
```

For academic citation, use the BibTeX entry shipped in the root of this repository (`CITATION.cff` and `references.bib`).

## Commercial Licensing

For commercial use of AUGMANITAI terminology data, please contact the author through the GitHub repository's security contact (see `../governance/SECURITY.md` for the current private contact channel). Commercial licensing negotiations will consider:

- The intended use case
- The scope of integration (lookup only vs. derivation)
- The commercial scale (internal tool vs. external product)
- Whether the licensing fee should be a one-time payment, an annual subscription, or a revenue share
- Whether the licensee is willing to contribute back improvements under the project's governance

There is no off-the-shelf commercial license schedule yet; each commercial inquiry is negotiated individually.

## License Compatibility Notes

- AUGMANITAI code (Apache 2.0) is compatible with GPLv3 (as a source), but NOT with GPLv2. If you are integrating into a GPLv2-only project, please contact us.
- AUGMANITAI data (CC BY-NC-ND 4.0) is NOT compatible with copyleft licenses like GPL or CC BY-SA for the purpose of combining into a derived dataset. You may however use both in the same project as independent components.
- The Creative Commons organization has stated that CC BY-NC-ND is NOT a "free cultural works" license. AUGMANITAI data is intentionally NOT a free cultural work — it is a curated scholarly reference, protected editorially.

## Provenance and Integrity

Every release of AUGMANITAI is:

- Published to Zenodo with a version-specific DOI (under the concept DOI 10.5281/zenodo.20161494)
- Git-tagged and GPG/Sigstore-signed
- Accompanied by an SPDX manifest and CycloneDX AI-SBOM (see `../provenance/ai-sbom/`)
- Covered by a C2PA content-credentials manifest (see `../provenance/c2pa/`)
- Asserted via W3C Verifiable Credentials (see `../provenance/w3c-vc/`)

These mechanisms allow downstream users to verify the integrity and authorship of the data they use.

## Questions?

See `../governance/CONTRIBUTING.md` and `../governance/GOVERNANCE.md` for general questions. For licensing-specific questions, open a GitHub Issue with the `licensing` label (for public questions) or use the private contact channel in `../governance/SECURITY.md` (for commercial inquiries or sensitive matters).


---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](../DISCLAIMER.md)) and the repository licenses ([`LICENSE`](../LICENSE)). Contact and provider: [`IMPRESSUM.md`](../IMPRESSUM.md).*
