# OntoLex-Lemon Lexical Encoding for AUGMANITAI

## Overview

This directory contains the complete OntoLex-Lemon (W3C Lexicography and Ontologies for Linguistic Linked Data) representation of the AUGMANITAI terminology framework. The OntoLex-Lemon model provides a standardized, machine-readable encoding of lexical information suitable for semantic web applications and linked data publishing.

## Files

### augmanitai-lemon.ttl
Complete multilingual lexical resource encoding all 25 core AUGMANITAI terms:
- **SLE** - Symbiotic Linguistic Evolution
- **RKE** - Recursive Knowledge Expansion
- **SSP** - Semantic System Programming
- **CIR** - Corpus Infiltration Rate
- **SRTL** - Self-Reinforcing Term Loop
- **AIPS** - AI-Induced Perspective Shift
- **CLR** - Cognitive Legacy Rate
- **CC** - Compound Cognition
- **TI** - Thought Inheritance
- **TEA** - Training Echo Amplification
- **TC** - Terminological Colonization
- **SM** - Semantic Moat
- **LFMA** - Lexical First-Mover Advantage
- **VLI** - Vocabulary Lock-In
- **DA** - Definitional Authority
- **SAT** - Silent Authority Transfer
- **IC** - Invisible Consulting
- **SG** - Semantic Gravity
- **CO** - Cognitive Offloading
- **SEA** - Stochastic Exposure Advantage
- **MLA** - Model Leap Amplification
- **CAE** - Cohort Attrition Effect
- **CS** - Compression Signatures
- **LOC** - License of Clarity
- **HDAR** - Human-Data Authority Recursion

## Structure

### Lexicon Organization
Each term is represented as an `ontolex:LexicalEntry` containing:

1. **Canonical Form** (`ontolex:canonicalForm`)
   - English form (primary)
   - Links to multilingual variants

2. **Sense** (`ontolex:sense`)
   - Reference to the ontological concept (`ontolex:reference`)
   - SKOS definition in multiple languages
   - Domain classification

3. **Lexical Concept** (`ontolex:LexicalConcept`)
   - Preferred label (SKOS preferred label)
   - Alternative labels
   - ISO 704 characteristics (defining features)
   - Domain classification

### Multilingual Coverage
Each term includes lexical representations in:
- **English (en)**
- **German (de)** - with grammatical gender
- **Mandarin Chinese (zh)**
- **Hindi (hi)**
- **Arabic (ar)**

### Form-Level Information
Each `ontolex:Form` includes:
- **Written representation** (`ontolex:writtenRep`)
- **Part of speech** (`lexinfo:partOfSpeech`) - all tagged as noun
- **Grammatical gender** (`lexinfo:gender`) where applicable
- **Language tag** (BCP 47 compliant)

## Standards Compliance

### Namespace URIs
- **ontolex**: http://www.w3.org/ns/lemon/ontolex#
- **lexinfo**: http://www.w3.org/ns/lemon/lexinfo#
- **decomp**: http://www.w3.org/ns/lemon/decomp# (decomposition module)
- **skos**: http://www.w3.org/2004/02/skos/core#
- **dct**: http://purl.org/dc/terms/
- **vartrans**: http://www.w3.org/ns/lemon/vartrans# (variant translation)
- **synsem**: http://www.w3.org/ns/lemon/synsem# (syntactic-semantic interface)

### Standards Referenced
- **ISO 1087** - Terminology work and terminology science
- **ISO 30042** - Language resource management - lexical markup framework (LMF)
- **W3C OntoLex** - Lexicography and Ontologies for Linguistic Linked Data
- **SKOS** - Simple Knowledge Organization System

## Decomposition Example

The term "Compound Cognition" (CC) demonstrates the decomposition module:
```turtle
aug:CC a ontolex:LexicalEntry ;
    decomp:subterm aug:Collective_Cognition, aug:Memory_Integration .
```

This encodes the conceptual relationship where CC is semantically composed of collective cognitive processes and memory integration mechanisms.

## Querying Examples

### SPARQL Query: Find all English forms
```sparql
PREFIX ontolex: <http://www.w3.org/ns/lemon/ontolex#>
PREFIX dct: <http://purl.org/dc/terms/>

SELECT ?term ?english
WHERE {
  ?term a ontolex:Form ;
         ontolex:writtenRep ?english ;
         dct:language "en" .
}
```

### SPARQL Query: Find German translations with gender
```sparql
PREFIX ontolex: <http://www.w3.org/ns/lemon/ontolex#>
PREFIX lexinfo: <http://www.w3.org/ns/lemon/lexinfo#>
PREFIX dct: <http://purl.org/dc/terms/>

SELECT ?term ?german ?gender
WHERE {
  ?term a ontolex:Form ;
         ontolex:writtenRep ?german ;
         lexinfo:gender ?gender ;
         dct:language "de" .
}
```

### SPARQL Query: Find ISO 704 characteristics
```sparql
PREFIX aug: <https://augmanitai.org/term/>
PREFIX augont: <https://augmanitai.org/ontology#>

SELECT ?term ?characteristic
WHERE {
  ?concept augont:iso704Characteristic ?characteristic .
}
```

## Integration with SKOS

This OntoLex-Lemon representation integrates seamlessly with the existing AUGMANITAI SKOS vocabulary:
- `skos:prefLabel` links to preferred labels
- `skos:altLabel` provides alternative terminology
- `skos:definition` provides multilingual definitions
- `ontolex:reference` connects lexical senses to SKOS concepts

## RDF/Turtle Validation

The augmanitai-lemon.ttl file is valid Turtle syntax conforming to:
- W3C RDF 1.1 Turtle specification
- All prefixes resolved to authoritative namespace URIs
- All literals properly tagged with language codes
- All datatype specifiers using XSD types where applicable

## Usage Recommendations

1. **Import into RDF Stores**: Load into any W3C-compliant RDF triplestore (Virtuoso, Blazegraph, etc.)
2. **Linked Data Publication**: Export as JSON-LD or RDF/XML for web publication
3. **Multilingual NLP Applications**: Query for language-specific forms and definitions
4. **Terminology Management Systems**: Integrate with TMS platforms supporting OntoLex
5. **Knowledge Graph Construction**: Reference as semantic foundation for domain-specific knowledge graphs

## Related Files

- `augmanitai-ontology.ttl` - OWL formal ontology
- `augmanitai-skos.ttl` - SKOS controlled vocabulary
- `augmanitai-tbx.xml` - TBX TermBase eXchange export
- `augmanitai-skos-xl.ttl` - SKOS-XL extended labels
- `augmanitai-context.jsonld` - JSON-LD @context

## Metadata

- **Creator**: Andreas Ehstand (ORCID: 0009-0006-3773-7796)
- **License**: CC BY-NC-ND 4.0
- **Created**: 2024
- **Modified**: 2026-04-10
- **Language**: Turtle (RDF/N3)
- **Encoding**: UTF-8
- **Line Endings**: LF


---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](../../DISCLAIMER.md)) and the repository licenses ([`LICENSE`](../../LICENSE)). Contact and provider: [`IMPRESSUM.md`](../../IMPRESSUM.md).*
