# C2PA 2.1 Content Credentials — Structural Demonstration

> **Scope note.** This directory is a **structural demonstration only**.
> AUGMANITAI is a manually curated terminology **dataset** (1000 terms across
> 16 domains), not an AI system, not a trained model, and not a certified
> product. Nothing in this folder asserts ISO certification, EU AI Act
> conformity, notified-body approval, or regulatory endorsement. The files
> here show how a downstream operator *could* attach C2PA provenance
> metadata to a dataset artifact — nothing more.
>
> Descriptive linguistic research, not normative (§1). Non-peer-reviewed
> working-paper (§11). ISO-inspired, not ISO-certified (§16). Restricted
> applications per §20. See `DISCLAIMER.md` in the repository root.

## What C2PA is

The **Coalition for Content Provenance and Authenticity** (C2PA) is an open
technical specification for cryptographically binding provenance metadata
("content credentials") to a digital artifact. A C2PA manifest typically
records:

- Actions performed on the artifact (created, edited, published)
- Ingredients used to produce the artifact (source materials)
- Training & mining declarations (whether the artifact may be used for ML
  training, and under what license)
- A cryptographic signature linking the manifest to the artifact's hash

## What this folder contains

### `c2pa-manifest-template.json`
A **demo** C2PA 2.1 manifest for the AUGMANITAI dataset itself. It declares:

- `digitalSourceType: humanEdited` — the compendium was written by a single
  author, not generated or trained.
- `c2pa.training_mining`: the dataset was **not** produced by training and
  may not be mined for training without complying with CC BY-NC-ND 4.0 and
  §20 of the disclaimer.
- `does_not_claim`: an explicit list of things the manifest does **not**
  assert (AI system status, ISO certification, conformity with any
  regulation, performance metrics).

The signature and hash values are literal placeholder strings.

### `training-mining-assertion.json`
A standalone demo of the `c2pa.training_mining` assertion in isolation.
Declares:

- `claim_generator_trained: false` — AUGMANITAI is a terminology dataset.
- `training_method: "Manual curation by the single author"`.
- `training_data_mining_allowed: false` — CC BY-NC-ND 4.0 plus §20.
- A list of prohibited uses mirroring §20 of the disclaimer.

## What this folder does NOT do

- It does **not** generate a live, verifiable C2PA credential.
- It does **not** bind a real SHA-256 hash to a real artifact.
- It does **not** assert any relationship with C2PA, Adobe, the Content
  Authenticity Initiative, any notified body, or any regulator.
- It does **not** map AUGMANITAI onto any regulatory framework or article
  numbering.
- It does **not** imply that downstream systems using AUGMANITAI inherit
  any form of compliance status from AUGMANITAI.

## How a downstream operator could use this

If you are building an AI system and want to attach C2PA provenance to
**your** artifact (not to AUGMANITAI), you would:

1. Author your own manifest describing **your** system and **your** actions.
2. Compute a real content hash of your artifact and put it in
   `c2pa.core_properties.contentBinding.hash`.
3. Sign the manifest with your own key; publish your verification method.
4. If you **cite** AUGMANITAI as an input, attribute it per the
   `attribution_requirements` block in `training-mining-assertion.json`
   (CC BY-NC-ND 4.0, DOI, author, ORCID).

The templates in this folder are intended as a starting skeleton, not as a
ready-made compliance artifact.

## License & disclaimer

- **Code / templates** (this directory): Apache-2.0
- **Data** (the AUGMANITAI compendium itself): CC BY-NC-ND 4.0
- **Ethical Disclaimer**: see `DISCLAIMER.md` §1, §11, §16, §20 in the
  repository root.

## Contact

Andreas Ehstand — ORCID [0009-0006-3773-7796](https://orcid.org/0009-0006-3773-7796)
DOI: [10.5281/zenodo.19481331](https://doi.org/10.5281/zenodo.19481331)
