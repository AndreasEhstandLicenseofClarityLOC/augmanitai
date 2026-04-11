# JSON-LD @context and Frame Documents for AUGMANITAI

## Overview

This directory contains JSON-LD context and frame documents for representing AUGMANITAI terminology in JSON-LD format, enabling Linked Data applications, semantic web frameworks, and modern JavaScript-based systems to work with AUGMANITAI concepts using familiar JSON structures.

## Files

### augmanitai-context.jsonld
Reusable JSON-LD @context defining namespace prefixes, property mappings, and type coercions:
- **Namespace Declarations**: Maps all ontology, vocabulary, and standard namespaces to IRIs
- **Property Mappings**: Defines how JSON properties correspond to RDF properties
- **Language Containers**: Enables multilingual property values
- **Type Coercions**: Specifies datatypes for dates, identifiers, and relationships
- **Vocabulary Prefixes**: Supports both expanded IRIs and compact prefixes

### augmanitai-frame.jsonld
JSON-LD Frame document for consistent document structure:
- **Frame Template**: Defines expected shape of term documents
- **Property Ordering**: Specifies canonical property sequence
- **Nested Objects**: Shows structure for complex properties (labels, relationships)
- **Type Specification**: Indicates expected types for properties
- **Shape Consistency**: Ensures all term documents have uniform structure

### example-sle.jsonld
Complete worked example showing full JSON-LD representation of SLE (Symbiotic Linguistic Evolution):
- **Context Inclusion**: References augmanitai-context.jsonld
- **Full Term Data**: Demonstrates all properties and multilingual fields
- **Label Variants**: Shows SKOS-XL label objects with metadata
- **Relationships**: Includes broader, narrower, related, and causal relationships
- **Multilingual Coverage**: English and German definitions and labels
- **Real Property Values**: Uses actual SLE term data

## JSON-LD Context Structure

### Namespace Declarations

```json
{
  "@context": {
    "aug": "https://augmanitai.org/term/",
    "augont": "https://augmanitai.org/ontology#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dct": "http://purl.org/dc/terms/",
    ...
  }
}
```

### Property Mappings

```json
{
  "@context": {
    "term": {
      "@id": "skos:prefLabel",
      "@language": "en"
    },
    "definition": {
      "@id": "skos:definition",
      "@language": "en",
      "@container": "@language"
    },
    "created": {
      "@id": "dct:created",
      "@type": "xsd:date"
    }
  }
}
```

### Language Containers

```json
{
  "definition": {
    "en": "English definition...",
    "de": "German definition...",
    "zh": "Chinese definition..."
  }
}
```

Serializes to RDF with language tags:
```turtle
aug:SLE skos:definition "English definition..."@en ;
        skos:definition "German definition..."@de ;
        skos:definition "Chinese definition..."@zh .
```

## Usage Patterns

### 1. Expanding Compact IRIs

Use the context to expand compact identifiers:

```javascript
// With augmanitai-context.jsonld
const doc = {
  "@context": "augmanitai-context.jsonld",
  "id": "aug:SLE",
  "type": "augont:Term"
};

// Expands to:
{
  "@id": "https://augmanitai.org/term/SLE",
  "@type": "https://augmanitai.org/ontology#Term"
}
```

### 2. Framing Documents

Use augmanitai-frame.jsonld to structure data consistently:

```javascript
// Raw RDF data
{
  "@id": "aug:SLE",
  "skos:prefLabel": "Symbiotic Linguistic Evolution",
  "skos:definition": {...},
  ...
}

// After framing with augmanitai-frame.jsonld
{
  "@context": "augmanitai-context.jsonld",
  "id": "aug:SLE",
  "term": "Symbiotic Linguistic Evolution",
  "definition": {...},
  ...
}
```

### 3. Multilingual Access

Access definitions in specific languages:

```javascript
const sle = {
  "definition": {
    "en": "...",
    "de": "..."
  }
};

// Access English definition
const enDef = sle.definition.en;
const deDef = sle.definition.de;
```

### 4. Compacting RDF Triples

Convert RDF/Turtle to compact JSON-LD:

```turtle
# RDF/Turtle
aug:SLE skos:prefLabel "Symbiotic Linguistic Evolution"@en ;
        skos:definition "The process..."@en ;
        dct:created "2024-01-15"^^xsd:date ;
        dct:domain "linguistic_dynamics" .
```

```json
// Compacted JSON-LD
{
  "@context": "augmanitai-context.jsonld",
  "@id": "aug:SLE",
  "term": "Symbiotic Linguistic Evolution",
  "definition": "The process...",
  "created": "2024-01-15",
  "domain": "linguistic_dynamics"
}
```

## Property Reference

### Core Term Properties

| JSON Property | RDF Property | Type | Container | Example |
|---------------|--------------|------|-----------|---------|
| id | @id | @id | - | "aug:SLE" |
| type | @type | - | - | "augont:Term" |
| term | skos:prefLabel | langString | en | "Symbiotic Linguistic Evolution" |
| abbreviation | augont:abbreviation | string | - | "SLE" |
| definition | skos:definition | langString | @language | {"en": "...", "de": "..."} |
| domain | dct:domain | string | - | "linguistic_dynamics" |
| iso704Characteristics | augont:iso704Characteristic | string | @set | ["characteristic1", "characteristic2"] |
| examples | augont:example | string | @list | ["example1", "example2"] |

### Label Properties

| JSON Property | RDF Property | Type | Container | Example |
|---------------|--------------|------|-----------|---------|
| prefLabel | skos:prefLabel | langString | @language | {"en": "..."} |
| altLabel | skos:altLabel | langString | @language | {"en": ["alt1", "alt2"]} |
| hiddenLabel | skos:hiddenLabel | langString | @language | {"de": ["..."]} |
| skosxlPrefLabel | skosxl:prefLabel | object | - | {...label object...} |
| skosxlAltLabel | skosxl:altLabel | object | @set | [{...}, {...}] |
| skosxlHiddenLabel | skosxl:hiddenLabel | object | @set | [{...}, {...}] |

### Relationship Properties

| JSON Property | RDF Property | Target | Container |
|---------------|--------------|--------|-----------|
| broaderTerms | skos:broader | @id | @set |
| narrowerTerms | skos:narrower | @id | @set |
| relatedTerms | skos:related | @id | @set |
| relatedTo | augont:relatedTo | @id | - |
| partOf | augont:partOf | @id | - |
| hasPart | augont:hasPart | @id | - |
| hasChild | augont:hasChild | @id | - |
| enables | augont:enables | @id | - |
| causesDirectly | augont:causesDirectly | @id | @set |
| causesIndirectly | augont:causesIndirectly | @id | @set |
| equivalentTo | augont:equivalentTo | @id | - |
| contradicts | augont:contradicts | @id | - |

### Metadata Properties

| JSON Property | RDF Property | Type | Datatype |
|---------------|--------------|------|----------|
| created | dct:created | literal | xsd:date |
| creator | dct:creator | literal | string |
| license | dct:license | @id | - |
| modified | dct:modified | literal | xsd:dateTime |
| language | dct:language | literal | string |
| label | rdfs:label | literal | string |
| comment | rdfs:comment | literal | string |
| seeAlso | rdfs:seeAlso | @id | - |

## Context Sections

### Core Namespaces
```json
{
  "@context": {
    "@vocab": "https://augmanitai.org/ontology#",
    "@base": "https://augmanitai.org/",
    "aug": "https://augmanitai.org/term/",
    ...
  }
}
```

### Identifier Mappings
```json
{
  "id": "@id",
  "type": "@type",
  "context": "@context"
}
```

### Language-Tagged Containers
```json
{
  "definitions": {
    "@id": "skos:definition",
    "@container": "@language"
  }
}
```

### Set Containers
```json
{
  "broaderTerms": {
    "@id": "skos:broader",
    "@type": "@id",
    "@container": "@set"
  }
}
```

### List Containers
```json
{
  "examples": {
    "@id": "augont:example",
    "@container": "@list"
  }
}
```

### Type Coercions
```json
{
  "created": {
    "@id": "dct:created",
    "@type": "xsd:date"
  }
}
```

## Integration Examples

### Web Application Usage

```javascript
// Load AUGMANITAI term with context
async function loadTerm(termId) {
  const doc = {
    "@context": "https://augmanitai.org/ontology/augmanitai-context.jsonld",
    "@id": `aug:${termId}`
  };

  const response = await fetch('/api/terms/' + termId);
  const term = await response.json();

  // Automatically compacted with context
  return term;
}

// Usage
const sle = await loadTerm('SLE');
console.log(sle.term);           // "Symbiotic Linguistic Evolution"
console.log(sle.definition.en);  // English definition
console.log(sle.definition.de);  // German definition
```

### RDF Conversion

```bash
# Convert Turtle to JSON-LD using context
rapper -i turtle augmanitai-skos.ttl \
  -o json-ld -c augmanitai-context.jsonld > augmanitai.jsonld
```

### SPARQL to JSON-LD

```sparql
# Query returns JSON-LD automatically with context
PREFIX augont: <https://augmanitai.org/ontology#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

CONSTRUCT {
  ?term skos:prefLabel ?label ;
        skos:definition ?def ;
        dct:domain ?domain .
}
WHERE {
  ?term augont:iso704Characteristic ?char ;
        skos:prefLabel ?label ;
        skos:definition ?def ;
        dct:domain ?domain .
}
```

## Standards Compliance

### W3C Recommendations
- **JSON-LD 1.1**: https://www.w3.org/TR/json-ld11/
- **JSON-LD Processing Algorithms and API**: https://www.w3.org/TR/json-ld11-api/
- **RDF 1.1**: https://www.w3.org/RDF/
- **SKOS**: https://www.w3.org/2004/02/skos/

### JSON-LD Features Used
- **@context**: Namespace and property definitions
- **@id**: Resource identifiers
- **@type**: Resource types
- **@language**: Language tags
- **@container**: Container types (@set, @list, @language, @id)
- **@vocab**: Default vocabulary
- **@base**: Base IRI resolution

## Context Usage Patterns

### Pattern 1: Direct Reference
```json
{
  "@context": "augmanitai-context.jsonld",
  "@id": "aug:SLE",
  "term": "Symbiotic Linguistic Evolution"
}
```

### Pattern 2: Embedded Context
```json
{
  "@context": {
    "@import": "augmanitai-context.jsonld",
    "customProp": "http://example.com/custom"
  },
  "@id": "aug:SLE"
}
```

### Pattern 3: Multiple Contexts
```json
{
  "@context": [
    "augmanitai-context.jsonld",
    "http://www.w3.org/ns/activitystreams",
    {"customProp": "..."}
  ]
}
```

### Pattern 4: Framing Application
```javascript
const jsonld = require('jsonld');

const doc = {...};
const frame = await jsonld.getDocument('augmanitai-frame.jsonld');
const framed = await jsonld.frame(doc, frame);
```

## File Format

- **Serialization**: JSON
- **Encoding**: UTF-8
- **JSON Schema**: Valid JSON-LD per W3C specification
- **Validation**: Can be validated against JSON-LD schema

## Related Files

- `../ontolex-lemon/augmanitai-lemon.ttl` - OntoLex-Lemon encoding
- `../skos-xl/augmanitai-skos-xl.ttl` - SKOS-XL labels
- `../../ontology-core/augmanitai-skos.ttl` - SKOS vocabulary
- `../../ontology-validation/shacl/term-shapes.ttl` - SHACL validation

## Metadata

- **Creator**: Andreas Ehstand (ORCID: 0009-0006-3773-7796)
- **License**: CC BY-NC-ND 4.0
- **Format**: JSON-LD 1.1
- **Encoding**: UTF-8
- **Created**: 2026-04-10
- **Standards**: W3C JSON-LD 1.1, RDF 1.1, SKOS

## Best Practices

1. **Context Reuse**
   - Use remote @context for consistency across projects
   - Cache context URIs for performance
   - Provide fallback contexts for offline use

2. **Framing**
   - Use frames for consistent document structure
   - Apply frames after compaction for uniform output
   - Maintain frame hierarchy for nested objects

3. **Multilingual Data**
   - Use @language containers for translated properties
   - Always include English as primary language
   - Specify language explicitly in labels

4. **IRI Management**
   - Use compact IRIs with namespace prefixes
   - Maintain consistent IRI patterns
   - Reference external vocabularies with full IRIs

5. **Type System**
   - Include @type for all resources
   - Use explicit type coercions for dates
   - Specify @id type for relationship properties

## Notes

- JSON-LD is fully compatible with RDF; documents can be converted bidirectionally
- Context is designed for both human-readable and machine-readable JSON
- Frame ensures consistent document structure across applications
- Example document demonstrates all major property types and containers
- Context supports both expanded and compacted JSON-LD forms


---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](../../DISCLAIMER.md)) and the repository licenses ([`LICENSE`](../../LICENSE)). Contact and provider: [`IMPRESSUM.md`](../../IMPRESSUM.md).*
