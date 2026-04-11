# SKOS-XL Extended Labels for AUGMANITAI

## Overview

This directory contains the AUGMANITAI terminology enhanced with SKOS-XL (Simple Knowledge Organization System - Reification Module for Labels), providing rich lexical metadata for terminology management systems, controlled vocabularies, and linked data applications.

## Files

### augmanitai-skos-xl.ttl
Complete SKOS-XL representation of all 25 AUGMANITAI core terms with:
- **Primary Labels**: skosxl:prefLabel for canonical English designations
- **Alternative Labels**: skosxl:altLabel for synonyms and variants (2-3 per term)
- **Hidden Labels**: skosxl:hiddenLabel for non-display retrieval (German translations)
- **Label Provenance**: dct:created, dct:creator, dct:language metadata
- **Label Relations**: skosxl:labelRelation to connect semantically related labels
- **ISO 704 Alignment**: All labels meet ISO 704 terminology principles

## SKOS-XL Structure

### Label Reification

SKOS-XL reifies labels as first-class objects, enabling rich metadata:

```turtle
# Simple SKOS (labels as strings)
aug:SLE skos:prefLabel "Symbiotic Linguistic Evolution"@en .

# SKOS-XL (labels as objects with metadata)
aug:SLE skosxl:prefLabel aug:SLE_prefLabel .

aug:SLE_prefLabel a skosxl:Label ;
    skosxl:literalForm "Symbiotic Linguistic Evolution"@en ;
    dct:created "2024-01-15"^^xsd:date ;
    dct:creator "Andreas Ehstand" ;
    dct:language "en" ;
    rdfs:comment "Primary English designation"@en .
```

### Label Types

1. **Preferred Labels** (skosxl:prefLabel)
   - One per term in primary language (English)
   - Used as canonical form in documentation and systems
   - Contains creation date and creator attribution
   - Includes rdfs:comment describing usage context

2. **Alternative Labels** (skosxl:altLabel)
   - 2-3 synonyms per term
   - Represent different perspectives on the concept
   - Include semantic rationale (e.g., "emphasizing iterative process")
   - Enable discovery through varied terminology

3. **Hidden Labels** (skosxl:hiddenLabel)
   - Non-display labels enabling multilingual retrieval
   - German translations of English terms
   - Marked as hidden to avoid duplicate display
   - Enable cross-language querying

## Label Coverage

All 25 AUGMANITAI terms have:

| Term | Abbreviation | Preferred Label | Alternatives | Coverage |
|------|--------------|-----------------|---------------|----------|
| SLE | SLE | Symbiotic Linguistic Evolution | 2 + German | 3 forms |
| RKE | RKE | Recursive Knowledge Expansion | 3 | 3 forms |
| SSP | SSP | Semantic System Programming | 2 | 2 forms |
| CIR | CIR | Corpus Infiltration Rate | 1 | 1 form |
| SRTL | SRTL | Self-Reinforcing Term Loop | 2 | 2 forms |
| AIPS | AIPS | AI-Induced Perspective Shift | 1 | 1 form |
| CLR | CLR | Cognitive Legacy Rate | 1 | 1 form |
| CC | CC | Compound Cognition | 2 | 2 forms |
| TI | TI | Thought Inheritance | 2 | 2 forms |
| TEA | TEA | Training Echo Amplification | 1 | 1 form |
| TC | TC | Terminological Colonization | 2 | 2 forms |
| SM | SM | Semantic Moat | 1 | 1 form |
| LFMA | LFMA | Lexical First-Mover Advantage | 1 | 1 form |
| VLI | VLI | Vocabulary Lock-In | 1 | 1 form |
| DA | DA | Definitional Authority | 1 | 1 form |
| SAT | SAT | Silent Authority Transfer | 2 | 2 forms |
| IC | IC | Invisible Consulting | 1 | 1 form |
| SG | SG | Semantic Gravity | 1 | 1 form |
| CO | CO | Cognitive Offloading | 1 | 1 form |
| SEA | SEA | Stochastic Exposure Advantage | 1 | 1 form |
| MLA | MLA | Model Leap Amplification | 1 | 1 form |
| CAE | CAE | Cohort Attrition Effect | 1 | 1 form |
| CS | CS | Compression Signatures | 1 | 1 form |
| LOC | LOC | License of Clarity | 2 | 2 forms |
| HDAR | HDAR | Human-Data Authority Recursion | 1 | 1 form |

**Total: 25 preferred labels + 45 alternative labels = 70 lexical forms**

## Metadata Properties

### Label Creation and Attribution
```turtle
dct:created "2024-01-15"^^xsd:date ;
dct:creator "Andreas Ehstand" ;
```
Enables tracking of label origin and authorship.

### Language Specification
```turtle
dct:language "en" ;
```
Explicit language tagging for multilingual systems.

### Version Relations
```turtle
dct:isVersionOf "Symbiotic Linguistic Evolution"@en ;
```
Tracks variant forms and their relationships to canonical expressions.

### Usage Comments
```turtle
rdfs:comment "Primary English designation; use for formal terminology systems"@en .
```
Provides context for when and how to use each label variant.

### Label Relations
```turtle
skosxl:labelRelation aug:SLE_prefLabel ;
```
Connects semantically related labels and variants.

## Use Cases

### 1. Terminology Management Systems (TMS)

```sparql
# Query all alternative labels for a term
PREFIX skosxl: <http://www.w3.org/2008/05/skos-xl#>
PREFIX aug: <https://augmanitai.org/term/>

SELECT ?term ?altLabel
WHERE {
  ?term skosxl:altLabel ?label .
  ?label skosxl:literalForm ?altLabel .
}
```

### 2. Multilingual Discovery

```sparql
# Find German hidden labels for English retrieval
PREFIX skosxl: <http://www.w3.org/2008/05/skos-xl#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX aug: <https://augmanitai.org/term/>

SELECT ?term ?english ?german
WHERE {
  ?term skosxl:prefLabel ?enLabel ;
        skosxl:hiddenLabel ?deLabel .
  ?enLabel skosxl:literalForm ?english ; dct:language "en" .
  ?deLabel skosxl:literalForm ?german ; dct:language "de" .
}
```

### 3. Provenance and Attribution

```sparql
# Find all labels created by specific creator with dates
PREFIX skosxl: <http://www.w3.org/2008/05/skos-xl#>
PREFIX dct: <http://purl.org/dc/terms/>

SELECT ?term ?form ?created ?creator
WHERE {
  ?term skosxl:prefLabel|skosxl:altLabel ?label .
  ?label skosxl:literalForm ?form ;
         dct:created ?created ;
         dct:creator ?creator .
}
ORDER BY ?created
```

### 4. Label Variant Expansion

```sparql
# Get all label forms for a term with their rationales
PREFIX skosxl: <http://www.w3.org/2008/05/skos-xl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX aug: <https://augmanitai.org/term/>

SELECT ?form ?comment
WHERE {
  aug:SLE skosxl:prefLabel|skosxl:altLabel ?label .
  ?label skosxl:literalForm ?form ;
         rdfs:comment ?comment .
}
```

## Integration with SKOS

SKOS-XL complements and extends SKOS by:
- Replacing simple string labels (skos:prefLabel) with rich objects (skosxl:prefLabel)
- Enabling metadata attached to specific label forms
- Preserving backward compatibility with SKOS systems
- Providing fine-grained control over label variants

```turtle
# SKOS-XL augments SKOS
aug:SLE skosxl:prefLabel aug:SLE_prefLabel ;        # Rich SKOS-XL
        skos:prefLabel "Symbiotic Linguistic Evolution"@en .  # SKOS fallback
```

## Standards Compliance

### W3C Recommendations
- **SKOS** (Simple Knowledge Organization System): https://www.w3.org/2004/02/skos/
- **SKOS-XL**: https://www.w3.org/2008/05/skos-xl#
- **RDF 1.1**: https://www.w3.org/RDF/
- **RDFS**: https://www.w3.org/TR/rdf-schema/

### ISO Standards
- **ISO 704:1987** - Terminology - Principles and methods
- **ISO 1087:1990** - Terminology - Vocabulary
- **ISO 12620:2009** - Terminology and other language and content resources - Specifications and requirements for a terminology resource management system
- **ISO 30042:2008** - Language resource management - TermBase eXchange (TBX)

### Language Tags
- **BCP 47**: All language tags conform to IETF BCP 47 standard
  - "en" - English
  - "de" - German
  - "zh" - Mandarin Chinese
  - "hi" - Hindi
  - "ar" - Arabic

## Querying Examples

### SPARQL Query: All Preferred Labels with Creation Dates
```sparql
PREFIX skosxl: <http://www.w3.org/2008/05/skos-xl#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?term ?label ?created
WHERE {
  ?term skosxl:prefLabel ?labelObj .
  ?labelObj skosxl:literalForm ?label ;
            dct:created ?created .
}
ORDER BY ?created
```

### SPARQL Query: Terms with Most Alternative Labels
```sparql
PREFIX skosxl: <http://www.w3.org/2008/05/skos-xl#>

SELECT ?term (COUNT(?altLabel) AS ?altCount)
WHERE {
  ?term skosxl:altLabel ?altLabel .
}
GROUP BY ?term
ORDER BY DESC(?altCount)
```

### SPARQL Query: Label Versions and Their Relationships
```sparql
PREFIX skosxl: <http://www.w3.org/2008/05/skos-xl#>
PREFIX dct: <http://purl.org/dc/terms/>

SELECT ?term ?version ?relatedForm
WHERE {
  ?term skosxl:altLabel ?versionLabel .
  ?versionLabel dct:isVersionOf ?originalForm ;
                skosxl:literalForm ?relatedForm .
}
```

## File Format

- **Serialization**: Turtle (RDF/N3)
- **Encoding**: UTF-8
- **Character Set**: Full Unicode support
- **Syntax**: Valid RDF/Turtle per W3C specification
- **Namespace Declarations**:
  - `aug`: https://augmanitai.org/term/
  - `augont`: https://augmanitai.org/ontology#
  - `skosxl`: http://www.w3.org/2008/05/skos-xl#
  - `skos`: http://www.w3.org/2004/02/skos/core#
  - `dct`: http://purl.org/dc/terms/
  - `rdfs`: http://www.w3.org/2000/01/rdf-schema#

## Related Files

- `../../ontology-core/augmanitai-skos.ttl` - SKOS core vocabulary
- `../../ontology-extensions/ontolex-lemon/augmanitai-lemon.ttl` - OntoLex-Lemon lexical encoding
- `../../ontology-extensions/json-ld/augmanitai-context.jsonld` - JSON-LD context

## Metadata

- **Creator**: Andreas Ehstand (ORCID: 0009-0006-3773-7796)
- **License**: CC BY-NC-ND 4.0
- **Format**: Turtle (RDF/N3)
- **Encoding**: UTF-8
- **Created**: 2024-01-15 (labels), ongoing expansion
- **Modified**: 2026-04-10
- **Standards**: W3C SKOS-XL, ISO 704, ISO 1087, ISO 12620

## Best Practices

1. **Label Maintenance**
   - Always provide dct:created and dct:creator for provenance
   - Use rdfs:comment to explain usage context
   - Keep alternative labels semantically related to preferred form

2. **Multilingual Extension**
   - Use skosxl:hiddenLabel for non-display language variants
   - Mark language explicitly with dct:language
   - Maintain 1:1 correspondence between languages in hiddenLabel

3. **Integration**
   - Combine with SKOS vocabulary for maximum compatibility
   - Include both skosxl: and skos: properties
   - Use labelRelation to document semantic connections

4. **Backward Compatibility**
   - Systems using only SKOS can fall back to skos:prefLabel
   - SKOS-XL extends rather than replaces SKOS
   - Both property types can coexist in RDF graph

## Notes

- SKOS-XL is a W3C recommendation extending SKOS Core
- Labels as objects enable rich metadata not possible with simple strings
- Hidden labels enable retrieval without adding visual clutter
- Label relations document semantic connections between variants
- Provenance metadata supports terminology lifecycle management
