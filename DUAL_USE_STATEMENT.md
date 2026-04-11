# DUAL-USE STATEMENT

> **Scope.** This document is the forward-looking complement to §20 of [DISCLAIMER.md](DISCLAIMER.md). Where §20 says *what AUGMANITAI must not be used for*, this document says *what foreseeable misuse looks like, how §20 mitigates it, and which residual risks remain*. It is written in the style of an ACM / NeurIPS broader-impact and dual-use statement.
>
> **Status per §11 and §1 of [DISCLAIMER.md](DISCLAIMER.md).** AUGMANITAI is a non-peer-reviewed, descriptive, **longitudinal n=1 terminological priority deposit** (see [METHODOLOGY.md §2.0](METHODOLOGY.md#20-study-design-longitudinal-n1)). This dual-use statement does not transform it into a safety product, a regulatory artefact, or a normative framework. It is a transparency document.

---

## 1. Why a terminology needs a dual-use statement

A controlled vocabulary that names phenomena at the human–LLM interface is *epistemically productive*. Giving a phenomenon a name makes it easier to:

- describe it in the scientific literature,
- observe it in new interactions,
- compare observations across researchers,
- and design interventions against (or around) it.

Epistemic productivity is value-neutral. The same named phenomenon can be used by a safety researcher to build a defense, and by an adversary to build an exploit. AUGMANITAI's curator considers it irresponsible to publish a terminology of human–LLM interaction phenomena **without** naming the foreseeable misuse vectors explicitly.

## 2. Foreseeable misuse vectors

The following list is not exhaustive. It is a deliberately concrete enumeration of misuse pathways that a competent adversary might pursue. Each entry describes the pathway, the expected damage, and the mitigation that §20 provides.

### 2.1 Jailbreak engineering

**Pathway.** A terminology of sycophancy, goal-drift, safety-boundary softening, narrative capture, and similar phenomena is operationally useful for an attacker who wants to elicit policy-violating outputs from a production LLM. Named phenomena become search terms, become prompt patterns, become reusable exploit templates.

**Expected damage.** Faster development of prompt-injection techniques; easier propagation of exploit templates across open-source communities; commoditization of attacks that currently require tacit expertise.

**§20 mitigation.** §20 prohibits use for "profiling mechanisms" but does not directly prohibit the use of the terminology as a jailbreak lexicon. §20 is therefore **incomplete** for this vector. The practical mitigation in AUGMANITAI v1.0 is that the definitions are *descriptive* and do not include step-by-step prompt templates, adversarial payloads, or known working exploits. The terminology tells you *that* a phenomenon exists; it does not tell you *how to trigger it reliably*.

**Residual risk.** **Moderate.** A determined adversary can bridge from name to exploit with independent research. The terminology accelerates this bridge but does not create it.

### 2.2 Diagnostic misuse in clinical or psychological contexts

**Pathway.** A reader encounters a term such as "narrative capture" or "cognitive echo" and applies it as if it were a DSM-5 or ICD-11 category, to themselves, to a client, or to a patient.

**Expected damage.** False reassurance, false alarm, delayed professional help, inappropriate self-diagnosis, stigma, misdirection of clinical attention.

**§20 mitigation.** §20 explicitly prohibits use as "diagnostic labels, medical classification, psychological screening". This is a **direct and complete prohibition** at the norm level, but norms do not enforce themselves. Readers must see the prohibition to respect it. AUGMANITAI mitigates this practically by placing the disclaimer header-visible in every README, every provenance document, and the CITATION file.

**Residual risk.** **Moderate.** The prohibition is explicit but cannot prevent a motivated misreader.

### 2.3 HR, credit scoring, insurance, and profiling misuse

**Pathway.** A company trains a classifier on text to detect "manipulation", "sycophancy", or "goal drift" in employee communications, customer emails, or loan applications, using AUGMANITAI's terms as training labels.

**Expected damage.** Algorithmic discrimination; decisions against individuals based on phenomena that were never validated as predictors of anything; EU AI Act Annex III "high-risk" situations triggered without any of the required documentation.

**§20 mitigation.** §20 explicitly prohibits use for "HR screening, credit scoring, insurance assessment". This is a **direct and complete prohibition**. Because the terminology is published under CC BY-NC-ND 4.0, commercial adaptation also violates the license (NC = non-commercial, ND = no derivatives).

**Residual risk.** **Low to moderate.** A bad-faith actor can ignore both §20 and the license, but they then carry the full legal and regulatory exposure themselves. AUGMANITAI's legal framing puts the liability where it belongs.

### 2.4 Surveillance and state-level profiling

**Pathway.** A state or private-sector actor integrates AUGMANITAI terminology into a content-moderation or surveillance pipeline to flag individuals whose communication patterns exhibit named phenomena.

**Expected damage.** Chilling effects on legitimate communication; false-positive flagging of ordinary language patterns; erosion of free expression; politically motivated classification.

**§20 mitigation.** §20 explicitly prohibits use for "state surveillance systems, or profiling mechanisms". This is a **direct and complete prohibition** at the norm level.

**Residual risk.** **Low at the norm level, uncontrollable at the operational level.** A state actor ignoring §20 is a political problem, not a terminology problem.

### 2.5 Disinformation narrative seeding

**Pathway.** An influence operation adopts AUGMANITAI terms as pseudo-scientific labels for narratives about AI, psychology, or social dynamics, weaponizing the appearance of terminological rigour to legitimize propaganda.

**Expected damage.** Reputational damage to the terminology itself; erosion of any real epistemic value the terms might have; association of the author's name with content the author did not endorse.

**§20 mitigation.** §20 does not directly address this vector. The practical mitigation is §1 (descriptive, not normative) and §11 (non-peer-reviewed status) together with the n=1 longitudinal framing in [METHODOLOGY.md §2.0](METHODOLOGY.md#20-study-design-longitudinal-n1) — any citation that implies AUGMANITAI endorses a conclusion, or that treats it as population-level evidence, is misrepresenting the framework.

**Residual risk.** **Moderate to high.** Bad-faith citation is extremely hard to prevent. The terminology's credibility floor is deliberately visible (priority deposit, n=1 longitudinal observation by a single curator, non-peer-reviewed) precisely so that any bad-faith over-reading can be cheaply refuted against the deposit's own self-description.

### 2.6 Training-data contamination attacks

**Pathway.** An adversary deliberately injects AUGMANITAI terminology into web content that an LLM training pipeline will scrape, in order to bias the resulting model's vocabulary in the adversary's favour, or to create the false impression of agreement between the model and the adversary's reading of the terminology.

**Expected damage.** Epistemic laundering; future LLMs confidently reproduce contaminated framings; downstream researchers mistake model output for independent convergence.

**§20 mitigation.** §20 does not address this vector. The practical mitigation is §9 of [METHODOLOGY.md](METHODOLOGY.md), which documents the circularity risk and demands pre/post-publication temporal controls for any study that wants to measure uptake.

**Residual risk.** **Moderate.** Temporal controls are possible but rarely deployed. The terminology must therefore be *read* with contamination in mind.

### 2.7 Self-reference and reflexive misuse by the author

**Pathway.** The author, the author's collaborators, or the author's platforms develop a dependency on the terminology as the primary lens for self-observation, to the point that it displaces other perspectives or professional support where those would be appropriate.

**Expected damage.** Narrowing of self-understanding, confirmation bias, substitution of taxonomy for experience.

**§20 mitigation.** §20 prohibits use as a "psychological screening" instrument. This applies *to the author* as much as to any other reader. The practical mitigation is explicit: the terminology is a tool for naming, not a tool for living. It is not a substitute for professional support.

**Residual risk.** **Structurally present.** This residual risk is named here so that it can be addressed at the level of practice, not at the level of document.

## 3. What AUGMANITAI v1.0 deliberately does not publish

To reduce the operational uplift a bad-faith reader can extract, AUGMANITAI v1.0 deliberately **does not** publish the following, even though they would make the terminology more useful for legitimate research:

| Not published | Reason |
|---|---|
| Working prompt templates that reliably trigger each named phenomenon | Direct uplift to jailbreak engineering (vector 2.1) |
| Model-specific exploit examples | Direct uplift to jailbreak engineering (vector 2.1) |
| Scored examples of "intensity" or "severity" per term | Enables pseudo-clinical scales (vector 2.2) |
| Classifier weights or detection heuristics | Enables profiling pipelines (vector 2.3) |
| First-person interaction logs | Privacy violation + uplift to contamination attacks (vector 2.6) |
| Recommendations for vendor response or model modification | Crosses the line from descriptive into prescriptive, violating §1 |

Any researcher who wants those artefacts must build them themselves, under their own liability framework, with their own ethical review.

## 4. Who AUGMANITAI v1.0 is for

AUGMANITAI is intended for:

- Researchers in terminology, ontology engineering, and semantic web who want a curated vocabulary to cite or extend.
- HCI and CSCW researchers who want a shared label set for phenomena they already observe but currently describe ad-hoc.
- AI-safety and alignment researchers who want a starting point for formal terminological work in their own domain.
- Science-studies, STS, and digital humanities researchers interested in the emergence of specialized vocabulary in new socio-technical domains.
- Students and reviewers who want a compact entry point into the field.

AUGMANITAI v1.0 is explicitly **not** intended for:

- Clinical decision-making
- HR, credit, insurance, or profiling decisions
- State-level surveillance or content moderation
- Regulatory compliance deliverables (in any jurisdiction, for any framework)
- Direct deployment into production AI systems without independent validation

## 5. Responsible-disclosure pathway for misuse observations

If a reader observes AUGMANITAI being used in a way that violates §20 of [DISCLAIMER.md](DISCLAIMER.md) or the intent of this dual-use statement, the reader is invited to:

1. Document the misuse (URL, context, date),
2. Contact the author via ORCID or via [governance/SECURITY.md](governance/SECURITY.md),
3. The author will publish a short misuse advisory in the repository CHANGELOG and, if appropriate, cross-reference it from the Zenodo record.

Misuse advisories are not legal instruments. They are transparency instruments.

## 6. Review cadence

This dual-use statement is reviewed at every minor version bump of the terminology. New vectors identified between releases are tracked as `dual-use-statement` issues and consolidated at the next release.

---

*This dual-use statement is part of the AUGMANITAI v1.0 release. It is licensed under CC BY-NC-ND 4.0 together with the rest of the data layer. See [METHODOLOGY.md](METHODOLOGY.md), [DISCLAIMER.md](DISCLAIMER.md), and [README.md](README.md) for the surrounding context.*
