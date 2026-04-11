# W3C Verifiable Credentials — Structural Demonstration

> **Scope note.** This directory is a **structural demonstration only**.
> AUGMANITAI is a manually curated terminology **dataset** (1000 terms
> across 16 domains), not an AI system, not a certified product, and not
> the subject of any live credentialing authority. The files in this
> folder are *example shapes* showing how a downstream operator could
> issue a verifiable credential referencing AUGMANITAI terminology. They
> are not operational credentials. The "issuer", the signature, the
> revocation status list, and all quality numbers are literal
> placeholders.
>
> Descriptive linguistic research, not normative (§1). Longitudinal n=1
> priority deposit, non-peer-reviewed per §11. ISO-inspired, not ISO-certified (§16). Restricted
> applications per §20. See `DISCLAIMER.md` in the repository root.

## What a Verifiable Credential is (briefly)

The **W3C Verifiable Credentials Data Model** is a standard for
cryptographically signed, machine-readable claims made by an *issuer*
about a *subject*. A VC typically contains:

- `@context` — JSON-LD context(s)
- `issuer` — who is making the claim
- `credentialSubject` — what is being claimed, about what
- `proof` — a cryptographic signature binding the credential to the issuer

In production, VCs are used for things like academic credentials, trade
documents, and supply-chain attestations. They rely on a live issuer, a
published verification key, and (usually) a revocation status list.

## What this folder contains

### `augmanitai-verifiable-credential.json`
A demo VC of type `AugmanitaiTerminologyCitationCredential`. The subject
is the AUGMANITAI dataset (v1.0), and the body contains:

- `terminologyMetrics` — the 1000 terms, the 16 domains, the ISO
  standards the dataset was *informed by* (`isoCertified: false`), and
  the two languages (English primary, German complete).
- `restrictedApplications` — a direct reference to §20.
- `limitations` — a short list covering §1, §11, §16, and §20.
- `doesNotClaim` — an explicit list of things the credential does **not**
  assert (diagnostic / medical validity, legal or HR applicability, ISO
  certification, EU AI Act conformity, regulatory endorsement).

The `proof.signatureValue` is the literal string
`PLACEHOLDER-NOT-A-REAL-SIGNATURE`. The `credentialStatus.id` is the
literal string `urn:placeholder:not-operational`.

### `credential-issuer.json`
A demo issuer profile describing the **fictional** self-sovereign
attestation authority `urn:augmanitai:issuer:terminology-reference`. It
contains:

- A contact (the author, via ORCID)
- A list of credential *types* the fictional issuer could emit
- A `trustFramework: "None — self-sovereign author attestation only"`
- A `doesNotClaim` section listing what the issuer does **not** assert
  (ISO certification, EU AI Act conformity, endorsement by any
  regulatory body, diagnostic/medical/…/profiling use)

There is no live endpoint, no DID document, no published verification
key, and no credential registry. Nothing in this file should be read as
a claim of authority.

## What this folder does NOT do

- It does **not** operate a live issuer. The "issuer" ID is a URN, not a
  resolvable endpoint.
- It does **not** bind a real signature to the credential payload.
- It does **not** maintain a revocation status list.
- It does **not** assert ISO certification, EU AI Act conformity, or any
  form of regulatory endorsement.
- It does **not** assert that the quality metrics in the example
  credential are measured values. They are not.
- It does **not** imply that downstream systems using AUGMANITAI
  terminology inherit any form of compliance status from AUGMANITAI.

## How a downstream operator could use this

If you want to issue your *own* verifiable credential that cites
AUGMANITAI as a terminology source, you would:

1. Stand up your own issuer (your own DID / key material / endpoint).
2. Author a VC whose `credentialSubject` describes **your** system or
   content — not AUGMANITAI.
3. Cite AUGMANITAI using the attribution format in
   `augmanitai-verifiable-credential.json` → `licenses.attribution`
   (CC BY-NC-ND 4.0, DOI, author, ORCID).
4. Sign the VC with your own key and publish your verification method.

The files here are skeleton shapes, not a ready-made credential chain.

## License & disclaimer

- **Code / templates** (this directory): Apache-2.0
- **Data** (the AUGMANITAI compendium): CC BY-NC-ND 4.0
- **Ethical Disclaimer**: see `DISCLAIMER.md` §1, §11, §16, §20 in the
  repository root.

## Contact

Andreas Ehstand — ORCID [0009-0006-3773-7796](https://orcid.org/0009-0006-3773-7796)
DOI: [10.5281/zenodo.19481331](https://doi.org/10.5281/zenodo.19481331)
