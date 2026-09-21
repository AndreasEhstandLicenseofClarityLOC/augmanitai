# Working with the public AUGMANITAI lexicon

**AI-generated technical guide to an existing public resource by Andreas Ehstand.**

The archived lexicon contains 101 entries with German and English names and definitions. It offers proposed vocabulary for describing human–AI interaction. This guide explains how to find an entry and keep its identity and source clear.

## Start with the versioned source

- [Published archive — DOI 10.5281/zenodo.22228966](https://doi.org/10.5281/zenodo.22228966)
- [Download the JSON](https://zenodo.org/api/records/22228966/files/terms.json/content)
- [Source README and scope](https://zenodo.org/api/records/22228966/files/README.md/content)
- Author: [Andreas Ehstand, ORCID 0009-0006-3773-7796](https://orcid.org/0009-0006-3773-7796)

The checked snapshot has 101 unique `aug_id` values, 101 German names and definitions, and 101 English names and definitions. The source labels 12 entries `phenomenology-core` and 89 `phenomenology-extension`. Those are collection labels, not quality scores or evidence of empirical validation.

## Look up a term by its identifier

This Python example uses the standard library and reads the public archive. It neither changes the source nor sends private input to a service.

```python
import json
from urllib.request import urlopen

SOURCE = "https://zenodo.org/api/records/22228966/files/terms.json/content"
with urlopen(SOURCE, timeout=30) as response:
    lexicon = json.load(response)

terms = lexicon["terms"]
by_id = {term["aug_id"]: term for term in terms}
if len(by_id) != len(terms):
    raise ValueError("Duplicate term identifiers in this source")

term = by_id["AUG-2010"]
print(term["aug_id"], term["name_de"], term["name_en"], sep=" | ")
print(term["definition_en"])
```

The selected entry is `AUG-2010`: **VERTRAUENSSCHLEIFE / Trust Loop**. The definition comes directly from the archived source when the example runs.

## Keep interpretation separate from retrieval

Finding a matching label does not show that an observed interaction fits its definition. Read the entry's context, boundaries and examples before applying it. A name is a descriptive proposal; it does not establish a new discovery, diagnosis or validated psychological construct.

The `querverweise` field is source text rather than a declared array of identifiers. Check whether a referenced ID is present in the selected archive before constructing links. A missing target can be outside this public selection; do not invent its definition.

For citation, retain both the term ID and the archive DOI. The JSON's source block contains an old prepublication DOI placeholder; the published repository record above supplies the actual citation identifier. A live page can change independently of this archived snapshot.

The source declares **CC BY-NC-ND 4.0**. Public availability does not grant unrestricted adaptation, commercial redistribution or any extra rights through this guide. Consult the source licence for a proposed use.

Checked on 21 September 2026. These checks concern fields, identifiers and availability, not scientific validation or widespread adoption.

[Nine research and creative reading paths](COLLABORATION.md) · [Research index](README.md)
