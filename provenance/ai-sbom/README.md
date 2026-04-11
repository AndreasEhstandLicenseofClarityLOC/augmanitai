# AI-SBOM for AUGMANITAI — Structural Demonstration

> **Scope note.** This directory is a **structural demonstration only**.
> AUGMANITAI is a manually curated terminology **dataset** (1000 terms
> across 16 domains), not an AI system and not a trained model. The SBOMs
> in this folder describe the dataset's files and licenses for
> supply-chain transparency; they do **not** assert any ISO certification,
> EU AI Act conformity, notified-body approval, or ML performance metrics
> for AUGMANITAI. The generator script (`sbom-generator.py`) is a
> demonstration of how a downstream operator could emit SPDX or CycloneDX
> SBOMs for **their own** AI system — not for AUGMANITAI.
>
> Descriptive linguistic research, not normative (§1). Longitudinal n=1
> priority deposit, non-peer-reviewed per §11. ISO-inspired, not ISO-certified (§16). Restricted
> applications per §20. See `DISCLAIMER.md` in the repository root.

## What an SBOM is (briefly)

A **Software Bill of Materials** is a machine-readable inventory of the
parts that make up a software or data artifact. Two widely used formats:

- **SPDX 3.0** (ISO/IEC 5962:2021) — Linux Foundation format. Version 3.0
  introduces an optional "AI Profile" for describing model components.
- **CycloneDX 1.6** — OWASP format. Version 1.6 introduces an optional
  "ML-BOM" profile for describing model components and training data.

For a *dataset* like AUGMANITAI the interesting fields are the package
list, license concluded, copyright text, DOI, and the relationships
between the compendium and its derived serializations (ontology, TBX).

## What this folder contains

### `ai-sbom-spdx.json`
An SPDX 3.0 SBOM **for the AUGMANITAI dataset itself**. Three packages:

1. `SPDXRef-Package-Compendium` — the 1000-term compendium
2. `SPDXRef-Package-Ontology` — OWL / RDF Turtle serialization
3. `SPDXRef-Package-TBX-Export` — TBX file (informed by ISO 30042)

All three carry `packageLicenseConcluded: CC-BY-NC-ND-4.0`. A `doesNotClaim`
block lists what the SBOM does **not** assert (AI system status, ISO
certification, EU AI Act conformity, performance metrics, regulatory
endorsement).

### `ai-sbom-cyclonedx.json`
A CycloneDX 1.6 BOM covering the same three data components, with a
`dependencies` graph linking the compendium to its serializations. Same
`doesNotClaim` treatment.

### `sbom-generator.py`
A demonstration Python script that emits SPDX or CycloneDX SBOMs for a
**fictional downstream AI system** (`EXAMPLE_SYSTEM`). It is intended as
starter code for downstream operators who want to describe their own
system; running it does **not** produce a regulatory-compliant SBOM and
does not assert anything about AUGMANITAI itself. The script's header
docstring makes this explicit.

Example (fictional):

```bash
python3 sbom-generator.py \
    --system "EXAMPLE_SYSTEM" \
    --version "1.0" \
    --format spdx \
    --output example-sbom.json
```

## What this folder does NOT do

- It does **not** contain a real AI model, trained weights, or inference
  pipeline. AUGMANITAI has none of these.
- It does **not** contain real training data. The compendium was written
  by the author through reading and manual drafting, not by training.
- It does **not** claim any quality metric, performance number, or
  accuracy figure. Any numbers that appear in the generator's fictional
  example output are literal placeholders.
- It does **not** imply that downstream systems using AUGMANITAI inherit
  any form of compliance status.

## License & disclaimer

- **Code** (`sbom-generator.py`, templates): Apache-2.0
- **Data** (the AUGMANITAI compendium): CC BY-NC-ND 4.0
- **Ethical Disclaimer**: see `DISCLAIMER.md` §1, §11, §16, §20 in the
  repository root.

## Contact

Andreas Ehstand — ORCID [0009-0006-3773-7796](https://orcid.org/0009-0006-3773-7796)
DOI: [10.5281/zenodo.19481331](https://doi.org/10.5281/zenodo.19481331)
