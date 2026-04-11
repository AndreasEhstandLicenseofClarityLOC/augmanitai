# Provenance Stack — Structural Demonstration

> **Scope note.** This directory is a **structural demonstration only**.
> AUGMANITAI is a manually curated terminology **dataset** (1000 terms across
> 16 domains), not an AI system, not a trained model, and not a certified
> product. Nothing in this folder or its subdirectories asserts ISO
> certification, EU AI Act conformity, notified-body approval, or regulatory
> endorsement. The files here show *example shapes* that a downstream
> operator could use when attaching provenance metadata to **their own**
> artifacts — they are not operational credentials, SBOMs, or manifests.
>
> Descriptive linguistic research, not normative (§1). Non-peer-reviewed
> working-paper (§11). ISO-inspired, not ISO-certified (§16). Restricted
> applications per §20. See `DISCLAIMER.md` in the repository root.

## What is in this folder

The provenance stack demonstrates three complementary open standards for
documenting the origin and composition of a digital artifact:

1. **C2PA 2.1** (Coalition for Content Provenance & Authenticity) —
   cryptographically signed content credentials that bind provenance
   metadata to an artifact's hash.
2. **AI SBOM** — Software Bill of Materials in SPDX 3.0 and CycloneDX 1.6
   format. For a dataset like AUGMANITAI, the SBOM inventories packages,
   licenses, and the relationships between the compendium and its
   derived serializations (ontology, TBX).
3. **W3C VC 2.0** — Verifiable Credentials, a standard for cryptographically
   signed machine-readable claims about a subject.

Each subdirectory has its own `README.md` with a local scope note.

## Directory Structure

```
provenance/
├── README.md                             [this file — structural demo]
│
├── c2pa/
│   ├── README.md                         [C2PA structural demo]
│   ├── c2pa-manifest-template.json       [dataset manifest, humanEdited]
│   └── training-mining-assertion.json    [no-training declaration]
│
├── ai-sbom/
│   ├── README.md                         [SBOM structural demo]
│   ├── ai-sbom-spdx.json                 [SPDX 3.0 dataset SBOM]
│   ├── ai-sbom-cyclonedx.json            [CycloneDX 1.6 dataset BOM]
│   └── sbom-generator.py                 [downstream operator demo script]
│
└── w3c-vc/
    ├── README.md                         [W3C VC structural demo]
    ├── augmanitai-verifiable-credential.json  [fictional citation VC]
    ├── credential-issuer.json            [fictional self-sovereign issuer]
    └── proof-template.json               [proof-shape demonstrations]
```

## What these files describe

### Dataset-level (AUGMANITAI itself)

The C2PA manifest, the two SBOM files, and the example verifiable
credential describe the **AUGMANITAI dataset**. They declare:

- The compendium's three artifacts (compendium, OWL/SKOS ontology, TBX
  export) and their CC BY-NC-ND 4.0 licensing.
- That AUGMANITAI was **manually curated** by a single author — no
  training, no inference, no ML pipeline.
- That AUGMANITAI is **informed by** ISO 704, ISO 1087, and ISO 30042
  (ISO-inspired, not ISO-certified — §16).
- That AUGMANITAI makes no claim of ISO certification, EU AI Act
  conformity, regulatory endorsement, or diagnostic / medical / HR /
  credit / surveillance applicability (§20).

Each of these files carries an explicit `doesNotClaim` or `_note`
section listing things that are **not** being asserted.

### Downstream-operator shapes

The `sbom-generator.py` script and some of the W3C VC proof templates
are **starter shapes for downstream operators** who want to attach
provenance to **their own** AI systems. Running them does not produce a
regulatory-compliant artifact for AUGMANITAI itself, and the generator
uses a fictional example system (`EXAMPLE_SYSTEM`) as placeholder input.

## What this folder does NOT do

- It does **not** operate a live C2PA signing service, a live SBOM
  registry, or a live W3C VC issuer.
- It does **not** contain real cryptographic signatures, real content
  hashes, or real revocation status lists. All such fields are
  placeholder strings.
- It does **not** assert that AUGMANITAI or any downstream system is
  "compliant" with any regulation.
- It does **not** contain Article or Annex mappings. AUGMANITAI is not
  an AI system in the sense of EU Regulation 2024/1689 and does not
  carry the obligations of one.
- It does **not** represent any affiliation with, endorsement from, or
  working relationship with notified bodies, the European Commission,
  the European AI Office, or any national competent authority.

## How a downstream operator could use this material

If you are building an AI system and want to attach provenance to
**your** artifact (not to AUGMANITAI), you would:

1. **SBOM.** Use `ai-sbom/sbom-generator.py` or the format docs to emit
   an SPDX 3.0 or CycloneDX 1.6 BOM describing **your own** components,
   your own training data (if any), and your own dependencies. Cite
   AUGMANITAI as an *input* using the CC BY-NC-ND 4.0 attribution in
   `ai-sbom/ai-sbom-spdx.json`.
2. **C2PA.** Use `c2pa/c2pa-manifest-template.json` as a starting
   skeleton. Compute your own content hash, sign with your own key,
   publish your own verification method. Do **not** reuse AUGMANITAI's
   identifiers as if they were your own.
3. **W3C VC.** Stand up your own issuer DID and key material. Author a
   credential whose subject is your system. If you cite AUGMANITAI
   terminology, attribute it via the format in
   `w3c-vc/augmanitai-verifiable-credential.json → licenses.attribution`.

The files in this folder are skeletons. Filling them in is the downstream
operator's responsibility, and any regulatory obligations that apply to
the downstream system are the downstream operator's obligations — not
AUGMANITAI's.

## Standards bodies referenced (no affiliation implied)

The following standards are *referenced* by this folder for format
interoperability. Their mention does **not** imply that AUGMANITAI is
certified against them, audited against them, or endorsed by the
organisations that maintain them.

- **ISO** (International Organization for Standardization) — ISO 704,
  ISO 1087, ISO 30042 (TBX).
- **W3C** (World Wide Web Consortium) — Verifiable Credentials Data
  Model 2.0, JSON-LD 1.1, SKOS.
- **C2PA** (Coalition for Content Provenance and Authenticity) —
  C2PA Technical Specification 2.1.
- **Linux Foundation** — SPDX 3.0.
- **OWASP** — CycloneDX 1.6.

## License & disclaimer

- **Code / templates** in this folder: Apache-2.0
- **Data** (the AUGMANITAI compendium): CC BY-NC-ND 4.0
- **Ethical Disclaimer**: see `DISCLAIMER.md` §1, §11, §16, §20 in the
  repository root. §20 prohibits use of AUGMANITAI as a diagnostic,
  medical, psychological, legal, HR, credit-scoring, insurance,
  surveillance, or profiling mechanism.

## Contact

Andreas Ehstand — ORCID [0009-0006-3773-7796](https://orcid.org/0009-0006-3773-7796)
DOI: [10.5281/zenodo.19481331](https://doi.org/10.5281/zenodo.19481331)
