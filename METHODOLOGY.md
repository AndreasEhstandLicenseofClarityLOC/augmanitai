# METHODOLOGY

> **Scope.** This document describes the methodological choices behind the AUGMANITAI 1000-Term Compendium. It is intended to make the framework legible for reviewers, replicators, and critics. Reading this document does not require agreement with the choices; the document's purpose is to make the choices *visible and criticizable*.
>
> **Status per §11 of [DISCLAIMER.md](DISCLAIMER.md).** AUGMANITAI is a non-peer-reviewed, longitudinal n=1 terminological priority deposit. Nothing in this document claims the authority of a peer-reviewed publication, and the artefact is not designed to target one. The scope boundaries listed in §10 are the boundaries of an n=1 longitudinal deposit — they are not defects of a larger study that this is trying to be.
>
> **Scope per §1 of [DISCLAIMER.md](DISCLAIMER.md).** The framework is descriptive, not normative. Methodological choices describe *how the terminology was constructed*, not *how LLMs should be built, used, or regulated*.

---

## 1. Research question and deliverable

AUGMANITAI asks a single, narrow question:

> *Can the recurring, linguistically isolable phenomena at the human–LLM interface be organized into a coherent controlled vocabulary with genus/differentia structure, explicit semantic relations, and a formal serialization — drawing on existing literature where terminology already exists, and introducing new labels only where needed?*

The deliverable is a controlled vocabulary — not a theory, not a model of cognition, not a safety framework, not an evaluation benchmark. The deliverable is a curated list of 1000 terms with definitions, characteristics, and semantic relations, formalized as an RDF knowledge graph.

What AUGMANITAI is therefore **not**:

- an empirical study of LLM capabilities
- an evaluation benchmark
- a dataset for training or fine-tuning
- a diagnostic or screening instrument (see §20 of [DISCLAIMER.md](DISCLAIMER.md))
- a theory of mind, cognition, or consciousness — in machines or humans
- a replacement for peer-reviewed literature
- **a claim of invention for every single term it lists** — see §2

## Scope: what is and is not claimed

AUGMANITAI v1.0 makes a narrow, defensible set of claims. It is important to state them as clearly as the limitations, so that readers and critics can engage with the right object.

**What AUGMANITAI v1.0 claims:**

1. **A coherent schema of 1000 terms** describing phenomena at the human–LLM interface, organized in a genus/differentia structure with explicit semantic relations (broader/narrower, related, associative).
2. **A formal serialization** of that schema in W3C-native formats (SKOS, SKOS-XL, OntoLex-Lemon, JSON-LD 1.1, SHACL, TBX) with a validated structural layer.
3. **A timestamped priority deposit** of the schema on Zenodo under DOI 10.5281/zenodo.20161494, dated to the public release. The timestamp is cryptographically anchored by Zenodo (CERN) and mirrored in this repository.
4. **A dual-language documentation layer** (German / English) with an explicit ethical framework ([DISCLAIMER.md](DISCLAIMER.md) §1–§20), a methodological disclosure (this document), and a dual-use statement ([DUAL_USE_STATEMENT.md](DUAL_USE_STATEMENT.md)).
5. **Integration with existing vocabularies and standards.** Where terms or concepts already exist in the literature (in linguistics, HCI, AI safety, philosophy, cognitive science, or standards bodies), AUGMANITAI incorporates them in its schema with appropriate attribution and re-expresses them in the genus/differentia form the schema requires.

**What AUGMANITAI v1.0 explicitly does not claim:**

1. **It does not claim invention of every term.** Some terms are drawn from existing literature or from community discourse and are included in the schema because the schema needed a label for the phenomenon. Others are newly introduced labels for phenomena that the curator could not find a shared name for in the sources scanned. The repository does not mark which terms fall into which category at the term level, because in practice the boundary is fuzzy — a term can be a minor re-formulation of an existing concept, a synthesis of multiple existing concepts, or a genuinely new label. **The priority deposit covers the schema as a whole, not each individual term.**
2. **It does not claim exhaustiveness.** The scan of existing literature was thorough but not systematic in the Cochrane-review sense. A prior term that the curator did not encounter is possible and will be acknowledged and attributed if brought to the curator's attention.
3. **It does not claim peer-reviewed status.** See §11. AUGMANITAI is a terminological priority deposit, not a peer-reviewed publication, and does not target peer review as its validation mechanism.
4. **It does not claim cross-cultural or cross-linguistic universality.** See the language-coverage limitation in §2 below.
5. **It does not claim predictive, diagnostic, or operational value.** See §20 of [DISCLAIMER.md](DISCLAIMER.md).

This separation is important: critics who attack AUGMANITAI for "inventing terms that already exist" are attacking a claim the repository does not make. Critics who point out that a specific term has prior art are engaging with the object correctly — the correct response to such a pointer is attribution, not rebuttal.

## 2. Study design and observational sources

### 2.0 Study design: longitudinal n=1

AUGMANITAI v1.0 is the terminological output of a **longitudinal single-subject observation** (n=1) conducted by the curator over approximately nine months of daily, extended use of production LLM systems. The design is not an experimental study with a hypothesis and a control group. It is a systematic, time-extended case record, comparable in form to a longitudinal case report, a single-subject behavioural study, or an autoethnographic observation log — transposed onto the human–LLM interaction domain.

The n=1 design is **the design**, not a defect of a larger study. It is disclosed here so that readers can calibrate their expectations accordingly:

- **What an n=1 longitudinal design can deliver:** dense, time-indexed observation of recurring phenomena in a single observer's interaction stream; stable naming of phenomena that appear across many sessions; a curated vocabulary that makes those phenomena discussable.
- **What an n=1 longitudinal design cannot deliver:** population-level frequency, inter-observer reliability, generalisation to other users, or predictive validity. These are out of scope by design, not by oversight.

Readers familiar with single-subject methodology in behavioural science (e.g. ABAB designs), clinical case reports, or qualitative autoethnography will recognise the form. Readers expecting a hypothesis-testing study with a sample size will not find one, and should not read AUGMANITAI as if it were one.

### 2.1 Observational sources

Terms were elicited from direct observation of human–LLM interactions over the n=1 observation window. The sources are heterogeneous by design:

| Source type | Description |
|---|---|
| First-person interaction logs | Daily extended use of production LLM systems (Claude, Gemini, Grok) across approximately nine months of the observation window. |
| Literature scan | Published academic work on human–AI interaction, RLHF, constitutional AI, alignment, HCI, and linguistic terminology methodology (ISO 704, ISO 1087, ISO 30042). |
| Standards documents | W3C, ISO, DCMI, C2PA, SPDX, W3C VC documentation for methodological framing. |
| Community discourse | Public technical discussions (blog posts, conference talks, public forum threads) that named phenomena without formal definition. |

### 2.2 Model coverage (scope boundary)

The first-person observation window is dominated by three vendor families (Anthropic Claude, Google Gemini, xAI Grok). Open-weights families (Llama, Mistral, Qwen, DeepSeek, Kimi) are under-represented in the first-person logs. This is a property of the n=1 observer's working setup, not a defect of the deposit. An independent follow-up on a broader model mix would address it (see §10, row B2).

### 2.3 Language coverage (scope boundary)

First-person observations are predominantly German and English — the working languages of the n=1 observer. Phenomena that emerge only in other languages or only in specific cultural framings are therefore likely under-represented. The term labels are provided with `@de` and `@en` language tags via SKOS-XL, but the *elicitation* process was not cross-linguistic (see §10, row B3).

## 3. Selection and inclusion criteria

A term was included in the compendium if **all** of the following conditions were satisfied:

1. **Phenomenal isolability.** The phenomenon could be described without reference to a specific model version, specific prompt, or specific user.
2. **Recurrent observability.** The phenomenon appeared across at least two different vendor families in the first-person logs, was documented in independent community discourse, or was established in the prior literature.
3. **Genus/differentia definability.** The phenomenon could be given a definition of the form *"X is a Y that differs from Z in the following way"* — i.e., it fit the ISO-704-informed definition schema.
4. **Non-prescriptive formulation.** The definition did not require a value judgement about the phenomenon being good, bad, safe, or unsafe.
5. **Schema fit.** The term could be placed into the broader/narrower/related relation network of the existing schema without forcing an inconsistency.

### Origin categories (non-exclusive)

Within the set of included terms, the curator distinguishes three origin categories. The boundary between them is fuzzy and the repository does not mark the category at the term level:

- **Imported.** The term already existed in the literature (linguistics, HCI, AI-safety research, philosophy, cognitive science, standards bodies) with a recognisable definition. AUGMANITAI includes it to avoid gratuitous neologism and re-expresses it in the schema's genus/differentia form. Where the source is known, it is acknowledged in the term's `dct:source` or `skos:note` field.
- **Re-formulated.** A phenomenon was named in the literature under a term that was polysemous, product-specific, or embedded in a theoretical framework the schema does not adopt. AUGMANITAI assigns a sharper label and cross-references the original term.
- **Newly introduced.** A phenomenon was observed repeatedly in the first-person logs or in community discourse but could not be matched to an existing term in the sources scanned. AUGMANITAI introduces a new label.

**The priority deposit (see §11) covers the coherent schema as a whole — the selection, definition, relation structure, and serialization — not each individual term.** A contributor or critic who identifies prior art for a term marked as "newly introduced" is welcomed; the correct response is attribution.

A term was *excluded* if it required a normative stance, if it referred to a specific vendor's product behaviour, or if it collapsed multiple distinguishable phenomena into one label (lumping).

## 4. Annotation process and single-observer reflexivity

**n=1 single-observer design.** All 1000 terms were proposed, defined, structured, and classified by the single observer of the longitudinal observation window (Andreas Ehstand). This is the design of the study, not a shortfall against a larger study. The curator is simultaneously the observer, the annotator, and the curator of the resulting schema. Within the n=1 frame this is not a limitation; it is what n=1 means.

**What that implies about scope of claims.** An n=1 schema makes strictly limited claims:

- It can name phenomena that the single observer encountered repeatedly across sessions and systems.
- It can give those phenomena definitions that are stable across the observation window.
- It cannot claim inter-observer agreement, population frequency, or predictive value. Any such claim would exceed the n=1 design and is explicitly not made here (see §20 of [DISCLAIMER.md](DISCLAIMER.md) and the claim list in the "Scope" section above).

**Reflexivity and known single-observer effects.** n=1 designs in qualitative and single-subject research are expected to disclose the observer effects that shape the record. The curator names three such effects explicitly so that readers can weigh them:

- **Selection bias.** The observer's interests, blind spots, and preferred framings shape which phenomena are named and which are ignored.
- **Definition drift.** Without a second observer challenging definitions, borderline cases may be absorbed into existing terms rather than generating new ones.
- **Lumping/splitting as curator judgement.** The granularity at which phenomena are separated is a judgement call the single curator made; readers who disagree with a specific split are invited to propose alternatives via the contribution path.

**Triangulation inside the n=1 frame.** Because inter-observer reliability is not available by design, the compendium uses *source triangulation* as its internal cross-check: a term was only accepted if the phenomenon it named was observable across more than one vendor family in the first-person logs, was documented in independent community discourse, or was established in the prior literature (see §3, criterion 2). Triangulation does not replace inter-rater reliability — it is a different instrument — but it reduces the risk that the schema reflects a single-session artefact.

**Relationship to multi-annotator work.** A multi-annotator study — distinct from AUGMANITAI v1.0 — could be conducted later by independent researchers using the schema as a given. That would be a *separate* study, with its own design, ethics, and authorship, not a continuation of this one. See §8 for the replication path.

## 5. Fictional and synthetic examples only

**No term in this repository is illustrated by a real, identified, or re-identifiable individual.** Where a term requires an illustrative example of human–LLM interaction, the example is either:

- fully synthetic (constructed by the annotator specifically for illustration), or
- a de-identified and re-framed paraphrase of a public, pre-existing discussion, with all identifying details removed.

No chat logs from private conversations have been published. No personal correspondence has been ingested. No third party's name, handle, or identifier appears in the term-level examples.

If any reader identifies content in the repository that they believe identifies a specific individual, they may report it via [governance/SECURITY.md](governance/SECURITY.md) and the content will be revised or removed.

## 6. Validation scope

**What has been validated.**

- Syntactic and structural validity of the RDF serializations (Turtle, JSON-LD 1.1) via `riot --validate` and `rdflib`.
- Conformance of term entries to the SHACL shapes in `ontology/validation/shacl-shapes/`.
- Internal consistency of the SKOS concept hierarchy (no `skos:broader` cycles).

**What has *not* been validated — because it is out of scope for an n=1 longitudinal deposit.**

- Inter-observer reliability (see §4 — not available by design in an n=1 study).
- Empirical frequency of the named phenomena in a controlled corpus.
- Predictive or diagnostic value in any downstream task (this is out of scope — see §20 of [DISCLAIMER.md](DISCLAIMER.md)).
- Cross-cultural or cross-linguistic stability of the phenomenal categories.

## 7. Use of "phenomenology"

The documentation occasionally uses the word *phenomenology* or *phenomenal* in the plain empirical sense of "observable regularities that can be named and described". **It does not invoke the Husserlian, Merleau-Pontian, or broader continental-philosophical tradition of phenomenology**, and no claims from that tradition are transferred to AUGMANITAI. Readers familiar with philosophical phenomenology should read the term as descriptive, not theoretically committed.

## 8. Reproducibility and replication

Full replication of AUGMANITAI v1.0 would require the original first-person observation logs, which are not published (they contain private interaction context and would violate §5 of this document). Replication is therefore *partial* and *prospective*: an independent group can:

1. Take the 1000-Term Compendium as given,
2. Conduct their own observation window on the same or different LLM families,
3. Attempt to re-derive the terms from scratch,
4. Compute the overlap with AUGMANITAI's terms as a rough external validity signal.

This is the replication path AUGMANITAI anticipates. It is not a substitute for the v2 multi-annotator revision described in §4.

## 9. Circularity risk (training-data contamination)

If LLM systems incorporate AUGMANITAI's terminology into their training data — either directly from the Zenodo record or indirectly via citations and discussion — and subsequently reproduce AUGMANITAI terms in their outputs, **this is not external validation of the terminology**. It is training-data contamination dressed as agreement.

Any future study that wants to measure the empirical uptake or validity of AUGMANITAI terms in LLM behaviour must control for this contamination explicitly — for example, by comparing models trained before and after the Zenodo publication date (2026), or by using held-out phenomena that were never published.

## 10. Scope boundaries of an n=1 longitudinal deposit

The entries below are not defects of a larger study that AUGMANITAI v1.0 fails to be. They are the **scope boundaries** of the n=1 longitudinal design described in §2.0 and §4. They are listed here so that readers can see, in one place, exactly what the compendium does and does not cover — and so that anyone conducting a separate study can see where an independent investigation would pick up.

| # | Scope boundary | Why it is out of scope for this deposit | How an independent study could address it |
|---|---|---|---|
| B1 | No inter-observer reliability | n=1 design by construction (see §4) | Independent multi-annotator study using the schema as given |
| B2 | Model coverage dominated by Claude / Gemini / Grok | These were the systems the single observer used daily | Broadened observation with open-weights families |
| B3 | Observation window predominantly DE/EN | Single observer's working languages | Cross-linguistic elicitation with other language pairs |
| B4 | No peer-review certification | Priority deposit, not a peer-reviewed publication (§11) | Independent submission by a third party, if desired |
| B5 | No preregistration of elicitation hypotheses | The design is descriptive, not hypothesis-testing | Pre-registered follow-up on specific sub-claims |
| B6 | No empirical frequency measurement | Out of scope for a case-style record | Corpus study as a separate follow-up |
| B7 | Philosophical term "phenomenology" may mislead | Terminological ambiguity in the general vocabulary | Disambiguation note (§7 above) |
| B8 | Potential circularity if LLMs re-emit the terms | Structural risk of any published terminology (§9) | Temporal pre/post-publication control by downstream studies |
| B9 | Lumping/splitting reflects one curator's judgement | n=1 design by construction (see §4) | Independent re-analysis of contested borders |
| B10 | No formal alignment against BFO / DOLCE / SUMO / CIDOC-CRM | Out of scope for v1.0 | Alignment paper as a separate follow-up |

The correct way to "remedy" any row above is not to fix AUGMANITAI v1.0, but to run the independent follow-up study it enables. That is the intended relationship between a priority deposit and the downstream research it makes possible.

## 11. What peer review would add — and why this work does not target it

AUGMANITAI v1.0 is a **priority-establishing terminological deposit**, not a peer-reviewed publication. The distinction matters for readers who want to know what the artefact is *for*.

**What a priority deposit is.** A priority deposit is a timestamped, cryptographically anchored public record that a particular schema, in a particular form, existed at a particular date. On Zenodo, CERN underwrites the timestamp. The purpose is to make the date of public availability verifiable — so that any later work in the same conceptual space can be compared against the deposit, not the other way around. The value of a priority deposit does not depend on peer review; it depends on the stability of the timestamp and the clarity of the deposited object.

**What peer review would add.** If AUGMANITAI were to enter a peer-review process at a venue familiar with terminology methodology (LREC, TKE, COLING) or human–AI interaction (CHI, CSCW, FAccT), the review would — if the process worked as intended — add:

1. An inter-annotator reliability study on a stratified sample (n ≥ 100 terms, k ≥ 2 independent annotators, Cohen's κ ≥ 0.6 as a minimum).
2. Cross-linguistic elicitation covering at least one non-Indo-European language.
3. An empirical frequency study against a controlled corpus of human–LLM interactions.
4. Pre-registration of hypotheses for any revision that expands the compendium.
5. A temporal pre/post-publication contamination control, as described in §9.
6. External challenge to the lumping/splitting decisions of the single annotator.

**Why v1.0 does not target peer review.** The purpose of AUGMANITAI v1.0 is to establish the date and form of the schema, not to argue its correctness in front of a peer-review committee. The curator considers the priority-deposit route adequate for the narrow question the compendium asks (see §1). Readers who want the items in the list above are invited to conduct them as independent studies — the replication path in §8 is designed to make that possible without the curator's participation. A future revision may or may not pursue a subset of those items; the decision is intentionally deferred.

**What this means for the reader.** AUGMANITAI v1.0 should be cited the way a timestamped dataset or a technical report is cited, not the way a peer-reviewed article is cited. A reader who requires peer-reviewed evidence for a claim should treat AUGMANITAI as a source of candidate terminology to test, not as a source of validated findings.

## 12. Contact and correction

Errors, misclassifications, missed sources, or overlooked prior terminology should be reported via GitHub issues on the dataset repository, or directly to the author via ORCID. Corrections will be versioned according to [governance/VERSIONING.md](governance/VERSIONING.md).

---

*This methodology document is part of the AUGMANITAI v1.0 release. It is licensed under CC BY-NC-ND 4.0 together with the rest of the data layer. See [README.md](README.md) and [DISCLAIMER.md](DISCLAIMER.md) for the full context.*
