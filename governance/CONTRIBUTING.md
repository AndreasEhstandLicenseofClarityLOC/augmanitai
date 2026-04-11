# Contributing to AUGMANITAI

Thank you for your interest in contributing to AUGMANITAI, an open-source terminology database designed to advance academic precision through harmonized terminology across disciplines and languages.

## How to Contribute

AUGMANITAI welcomes contributions in the form of term proposals, definition refinements, domain expertise validation, and translations. All contributions must follow this process.

## Code of Conduct

All contributors are expected to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). We are committed to providing a welcoming and harassment-free environment for everyone.

## Contribution Types

### 1. Term Proposals

Term proposals are the primary contribution type. Each proposal must follow ISO 704 terminology standards and include specific structured information.

#### Requirements for Term Proposals:

- **Term ID**: Unique identifier in format `[DOMAIN]-[NUMBER]` (e.g., `LING-0042`)
- **Language**: English and/or German (with full definitions in both)
- **Genus**: The broader category to which the term belongs
- **Differentia**: The distinguishing characteristics that set this term apart from related terms
- **Definitions**: 
  - English definition (2-4 sentences, precise and accessible)
  - German definition (functional equivalent, not literal translation)
- **ISO 704 Characteristics** (minimum 3 required):
  - Preciseness: Free from ambiguity in the specific context
  - Conciseness: Expressed in the shortest possible form without loss of precision
  - Consistency: Used uniformly throughout all relevant contexts
  - Distinctiveness: Clearly differentiated from related terms
  - Appropriateness: Follows conventions of standard terminology formation
  - Plurilinguality: Capable of parallel representation in multiple languages
  - Recognition: Accepted and used within the relevant domain community
  - Clarity: Expressed in clear, unambiguous language free of metaphor or ambiguity

- **First Attestation Source**: The earliest documented use of the term in academic literature
  - Format: Author (Year). *Publication*. DOI/URL
  - Required verification that the source supports the proposed definition

- **Related Existing Terms**: Links to 2-5 existing AUGMANITAI terms that share semantic proximity
  - Use term IDs from the database
  - Specify relationship type: broader, narrower, related, synonym, antonym

- **Domain**: Primary classification (e.g., Linguistics, Epistemology, Cognitive Science)

#### Submission Process:

1. Fill out the [Term Proposal Issue Template](.github/ISSUE_TEMPLATE/term_proposal.yml)
2. Provide all required fields with clear, complete information
3. Wait for review by domain experts
4. Address feedback through discussion in the GitHub issue
5. Once approved, maintainers integrate into the database

### 2. Definition Refinements

Proposed changes to existing term definitions must:
- Maintain ISO 704 compliance
- Include rationale for the change
- Reference new source material if applicable
- Preserve backward compatibility (no removal of definitions unless critical)

### 3. Documentation Improvements

- Typo fixes and clarity improvements
- Translation improvements
- Style guide adherence
- Examples and clarifications

### 4. Translations

Propose translations of existing terms to additional languages following the same ISO 704 standards applied for English and German.

## Licensing & Legal

### Developer Certificate of Origin (DCO)

AUGMANITAI uses the Developer Certificate of Origin v1.1. By contributing, you agree to the DCO. See [DCO.md](DCO.md) for full text.

To sign your commits:

```bash
git commit -s -m "Add term proposal for EPIST-0145"
```

The `-s` flag adds:
```
Signed-off-by: Your Name <your.email@example.com>
```

### Contributor License Agreement (CLA)

Before your first contribution is merged, you must sign our Contributor License Agreement. Choose one:
- [Individual CLA](CLA.md) — for individual contributors
- [Entity CLA](CLA-entity.md) — for contributions made on behalf of an organization

The CLA grants AUGMANITAI the necessary rights to distribute your contributions while you retain copyright ownership.

## Review Process

1. **Submission**: You open a GitHub issue using the appropriate template (term proposal, feature request, or bug report)
2. **Initial Triage** (1-3 business days): Maintainers review for completeness and basic compliance
3. **Domain Expert Review** (3-10 business days): Subject matter experts evaluate ISO 704 compliance and semantic soundness
4. **Community Discussion** (optional): Open discussion period for community feedback (typically 1 week)
5. **Resolution**: Maintainers make final decision and merge or request revisions
6. **Integration**: Approved contributions are merged into the main branch and included in the next release

## Style Guide

### Term Naming Conventions

- Use **English form** (nominalized where appropriate): "linguistic relativity" not "relativity of language"
- Avoid **abbreviations** in the term itself (acronyms only if standard in the field)
- Use **lowercase** for multi-word terms unless proper nouns are involved
- Prefer **singular** form for abstract concepts, **plural** for concrete countables

### Definition Writing

- **Opening**: Begin with the genus (broader category)
- **Differentia**: Specify what makes this term distinct
- **Scope Note**: Include context of use, domain restrictions, or important nuances
- **Examples**: Provide 1-2 clear domain-specific examples
- **Avoid**: Circular definitions, metaphorical language, undefined jargon

Example:
> **Term**: linguistic relativity  
> **Genus**: A principle of linguistic theory  
> **Differentia**: Proposing that the structure and vocabulary of a language influence the speaker's perception and categorization of experience  
> **Definition**: The hypothesis that the particular language a person speaks influences the way that person thinks about and perceives the world. Distinct from linguistic determinism in allowing language to be one influence among many on cognition.

### References and Citations

- Use **full citations** with DOI or URL
- Include **retrieval date** for online sources without DOI
- Format: Author(s) (Year). *Title*. *Publication*. DOI

## Decision-Making Process

AUGMANITAI uses a **lazy consensus** model:

- **Lazy Consensus**: A decision is approved if no one objects within the decision period (typically 7 days)
- **Maintainer Authority**: For urgent decisions or when consensus cannot be reached, the project lead (Andreas Ehstand) makes the final decision
- **Escalation**: Significant disputes may be escalated to the Steering Committee (when established)

## Conflict Resolution

Disagreements about terms, definitions, or decisions are resolved through:

1. **Discussion**: Good-faith discussion in the relevant GitHub issue or discussion thread
2. **Mediation**: If discussion stalls, request a maintainer to facilitate resolution
3. **Escalation**: If mediation fails, escalate to the project lead
4. **Appeal**: Contributors may request review by the future Steering Committee

See [GOVERNANCE.md](GOVERNANCE.md) for full conflict resolution procedures.

## Community Standards

### Be Respectful

- Assume good intent
- Disagree on ideas, not people
- Respect different expertise and perspectives
- Use inclusive language

### Be Constructive

- Provide specific feedback with rationale
- Suggest improvements, not just problems
- Acknowledge good work and contributions

### Be Responsive

- Reply to feedback within reasonable timeframes
- Clarify misunderstandings promptly
- Accept that your idea may not be accepted

## Getting Help

- **Questions**: Use GitHub Discussions
- **Bug Reports**: Use the Bug Report issue template
- **Documentation**: See [GOVERNANCE.md](GOVERNANCE.md) and [README.md](README.md)
- **Direct Contact**: Reach out to maintainers for guidance

## Recognition

Contributors will be:
- Listed in [MAINTAINERS.md](MAINTAINERS.md) (significant contributions)
- Acknowledged in release notes
- Listed in the project README
- Credited in the NOTICE file for substantive contributions

## Licensing Your Contribution

By submitting a contribution, you license your work under the same license(s) as the project:
- **Data/Terminology**: CC BY-NC-ND 4.0
- **Code**: Apache License 2.0

See [licensing/LICENSE-summary.md](../licensing/LICENSE-summary.md) for details.

---

Thank you for contributing to AUGMANITAI. Your work advances academic terminology worldwide.


---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](../DISCLAIMER.md)) and the repository licenses ([`LICENSE`](../LICENSE)). Contact and provider: [`IMPRESSUM.md`](../IMPRESSUM.md).*
