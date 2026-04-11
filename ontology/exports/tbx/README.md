# TBX TermBase eXchange Export for AUGMANITAI

## Overview

This directory contains the AUGMANITAI terminology database exported in ISO 30042 TBX-Core format, enabling integration with standard TermBase eXchange-compatible terminology management systems (TMS), translation memory systems, and localization platforms.

## Files

### augmanitai-tbx.xml
Complete TBX-Core 2 representation of all 25 AUGMANITAI core terms with:
- **Format**: ISO 30042 TBX-Core 2.0 XML schema
- **Encoding**: UTF-8 with XML declaration
- **Structure**: martif root element with teiHeader and text/body sections
- **Content**: 25 termEntry elements, one per AUGMANITAI term
- **Languages**: English (primary), German, and support for multilingual extensions

### convert_to_tbx.py
Python 3.7+ script for generating or regenerating the TBX export from source data:
- **Input**: augmanitai/data/terms.json and augmanitai_multilingual.json
- **Output**: augmanitai-tbx.xml with proper TBX-Core formatting
- **Usage**: `python convert_to_tbx.py /path/to/terms.json -m /path/to/multilingual.json -o output.xml`
- **Features**:
  - Automated TBX header generation with metadata
  - Language-specific term variants with grammatical tags
  - Domain classification preservation
  - License and provenance tracking
  - Pretty-printed XML output with proper indentation

## TBX-Core Structure

### Document Structure
```
martif (root, type="TBX-Core", xml:lang="en")
├── teiHeader (file metadata and encoding information)
│   ├── fileDesc (title, description, source)
│   ├── encodingDesc (format specification)
│   ├── profileDesc (language usage)
│   └── revisionDesc (version history)
└── text
    └── body
        └── termEntry (repeating, one per term)
```

### TermEntry Structure (per term)
Each termEntry contains:
- **id attribute**: Term abbreviation (SLE, RKE, SSP, etc.)
- **descrip type="definition"**: English definition with xml:lang="en"
- **descrip type="domain"**: Domain classification
- **admin type="license"**: License URI (CC BY-NC-ND 4.0)
- **langSet** (repeating, one per language):
  - **xml:lang**: Language code (en, de, zh, hi, ar)
  - **tig** (Term Information Group):
    - **term**: The term in the target language
    - **termNote type="partOfSpeech"**: All tagged as "noun"
    - **termNote type="grammaticalGender"**: For German forms (masculine, feminine, neuter)
    - **termNote type="abbreviation"**: Abbreviation (English langSet only)

## ISO Standards Compliance

### ISO 30042 (TBX - TermBase eXchange)
- Conformance to TBX-Core 2.0 profile
- Required mandatory elements: martif, teiHeader, text, body, termEntry, langSet, term
- Proper use of descrip and admin elements for metadata
- Valid encoding of multilingual term data

### ISO 704:1987 (Terminology Work - Principles and Methods)
- Each term includes definition meeting ISO 704 requirements
- Domain classification following ISO 704 Annex C principles
- Clear, unambiguous definitions suitable for standardization

### ISO 1087:1990 (Terminology - Vocabulary)
- Proper distinction between term, concept, and definition
- Relationships expressed through domain and classification metadata

## Import Recommendations

### TMS Platform Integration
1. **Trados Studio**: Import TBX-Core XML via File > Project > Create Project > Terms > Import TBX
2. **memoQ**: Tools > Resources > Manage > Create Terminology database from TBX
3. **Across**: Tools > Terminology Management > Import TBX file
4. **Wordfast**: TermBase > New > Import from TBX
5. **Lokalize**: Edit > Manage TBX Databases > Import

### Linked Data / RDF Integration
The TBX export can be converted to RDF/Turtle or linked data formats:
```sparql
# Extract term concepts for linked data publication
SELECT ?term ?definition ?domain
WHERE {
  ?term skos:definition ?definition ;
        dct:domain ?domain .
}
```

### Translation Memory Augmentation
Use TBX terms to populate translation memory (TM) with multilingual term pairs:
- English ⟷ German
- English ⟷ Mandarin Chinese
- English ⟷ Hindi
- English ⟷ Arabic

## Language Support

The augmanitai-tbx.xml file includes term forms for:

| Language | Code | Coverage |
|----------|------|----------|
| English | en | All 25 terms (primary) |
| German | de | All 25 terms (with grammatical gender) |
| Mandarin Chinese | zh | Support for future extension |
| Hindi | hi | Support for future extension |
| Arabic | ar | Support for future extension |

German grammatical gender is encoded in termNote[@type="grammaticalGender"] for all German forms.

## Generation and Maintenance

### Regenerating TBX Export

When source term data is updated, regenerate the TBX export:

```bash
cd /path/to/AUGMANITAI_BUILD/ontology-exports/tbx
python3 convert_to_tbx.py ../../augmanitai-python/augmanitai/data/terms.json \
  -m ../../augmanitai_multilingual.json \
  -o augmanitai-tbx.xml
```

### Validation

Validate TBX-Core conformance using:
1. XML Schema validation against TBX-Core 2.0 schema
2. Custom SHACL constraints (see ../shacl/)
3. TBX validator tools (e.g., TAUS TBX Checker)

## Related Files

- `convert_to_tbx.py` - TBX generation script
- `../shacl/term-shapes.ttl` - SHACL validation rules for TBX source data
- `../../augmanitai-python/augmanitai/data/terms.json` - Source term database
- `../../augmanitai_multilingual.json` - Multilingual extensions

## Metadata

- **Creator**: Andreas Ehstand (ORCID: 0009-0006-3773-7796)
- **License**: CC BY-NC-ND 4.0
- **Format Specification**: ISO 30042:2008 TBX-Core
- **Character Encoding**: UTF-8
- **Generated**: 2026-04-10
- **Last Modified**: 2026-04-10

## Standards References

- ISO 30042:2008 Language resource management - TermBase eXchange (TBX)
- ISO 30042:2008/Amd 1:2013 - Amendment 1
- ISO 704:1987 Terminology work - Principles and methods
- ISO 1087:1990 Terminology - Vocabulary
- W3C TBX: https://www.taus.net/standards/tbx

## Usage Examples

### Extracting English-German Term Pairs

```bash
xmllint --xpath '//langSet[@xml:lang="en"]/../langSet[@xml:lang="de"]' augmanitai-tbx.xml
```

### Finding Terms by Domain

```bash
xmllint --xpath '//termEntry[descrip[@type="domain"][contains(text(),"systemic_effects")]]/@id' augmanitai-tbx.xml
```

### Extracting All Definitions

```bash
xmllint --xpath '//descrip[@type="definition"]/text()' augmanitai-tbx.xml
```

## Notes

- TBX-Core 2.0 is compatible with TBX-Min and TBX-Full profiles
- The export uses martif[@type="TBX-Core"] to indicate strict TBX-Core compliance
- All term definitions are in English; multilingual definitions can be added via langSet/tig/descrip extensions
- License field universally set to CC BY-NC-ND 4.0 per AUGMANITAI project specification
