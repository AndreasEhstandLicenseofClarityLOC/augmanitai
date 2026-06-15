# AUGMANITAI Versioning Policy

AUGMANITAI uses Semantic Versioning 2.0.0 (https://semver.org/), **adapted for a terminology database**. This document explains what MAJOR, MINOR, and PATCH mean specifically for a project whose primary artifact is a curated vocabulary rather than executable software.

## Version Format

`MAJOR.MINOR.PATCH` (e.g., `1.2.3`)

Optional suffixes: `-alpha.N`, `-beta.N`, `-rc.N` for pre-releases; `+BUILD` for build metadata.

## Scope of Versioning

A single version number covers the entire release of:

1. **Terminology data** — the JSON/RDF/SKOS/TBX/JSON-LD exports of terms and relations.
2. **Code** — the Python package, NPM package, MCP server, API mock, helpers.
3. **Protocols** — the exposed MCP/A2A/ANP/AG-UI interfaces.
4. **Documentation** — the handbook, term pages, API reference.

Sub-components may have their own internal versions for debugging purposes, but the *published* version is the compendium version.

## MAJOR (X.y.z)

A MAJOR version increment signals a **breaking change** for consumers. For AUGMANITAI, this includes any of:

### Terminology breaking changes
- Removing a term from the compendium
- Renaming a term ID (the short abbreviation, e.g., `SLE`)
- Changing a term's URI (the permanent identifier, e.g., `https://augmanitai.org/term/sle`)
- Changing a term's `@type` or ontology class in a way that breaks downstream SPARQL queries
- Incompatible narrowing or broadening of a term's definition that would invalidate prior usage
- Removing or renaming a relation type in the relation vocabulary
- Removing or renaming a domain/collection

### Code breaking changes
- Removing or renaming a public Python/JS API function, class, or parameter
- Changing a function's required argument types
- Changing the default behavior of a function in a way existing callers would not expect
- Dropping support for a Python or Node.js version

### Schema breaking changes
- Changing the JSON Schema of `terms.json` in a non-additive way
- Changing the TTL structure of `augmanitai-ontology.ttl` in a way that breaks consumers
- Changing the SHACL shapes to reject previously-valid data

### Migration support
MAJOR releases ship with a `MIGRATION.md` that documents every breaking change and provides copy-pasteable fixes where possible.

Terms removed in a MAJOR release are never reused: their IDs are permanently retired and their URIs resolve to a tombstone with a `prov:invalidatedAtTime` timestamp and a pointer to the replacement (if any).

## MINOR (x.Y.z)

A MINOR version increment signals **backward-compatible additions**. For AUGMANITAI, this includes:

- Adding a new term
- Adding a new relation type
- Adding a new domain/collection
- Adding a new translation for an existing term
- Adding a new example to a term
- Adding a new optional field to the term schema (with a sensible default)
- Adding a new public API function
- Adding a new optional parameter to an existing function
- New supported export formats (e.g., adding a new serialization)
- New supported protocols (e.g., adding A2A was a MINOR increment when MCP was already present)

**Constraint:** a MINOR release must not change the meaning of any existing term or API in a way that existing consumers would notice.

## PATCH (x.y.Z)

A PATCH version increment signals **fixes that do not change meaning**. For AUGMANITAI, this includes:

- Typo fixes in definitions or examples
- Clarification wording that does not change the semantic scope
- Fixing a broken cross-reference
- Fixing a bug in the Python/NPM package
- Fixing a broken export generator
- Fixing documentation
- Correcting a translation
- Re-running export generators to regenerate derived files

**Constraint:** a PATCH release must not add or remove any term, field, or API. If you find yourself adding something in what you thought was a PATCH, it is actually a MINOR.

## Pre-releases

- `1.2.0-alpha.1` — early experimentation; expect bugs and further breaking changes
- `1.2.0-beta.1` — feature-complete, testing; expect bug fixes only
- `1.2.0-rc.1` — release candidate; expect no further changes unless blocking bugs found

Pre-releases may be published on Zenodo as separate DOI entries (each Zenodo upload gets its own DOI; the "concept DOI" is the version-independent one).

## DOI Policy

- The **concept DOI** (10.5281/zenodo.20161494) always resolves to the latest version.
- Each published version gets its own **version DOI** for citation permanence.
- Pre-releases get their own version DOIs but are not promoted to the concept DOI until the final release.

Citations should cite the version DOI for reproducibility and the concept DOI for "latest" references.

## Deprecation Policy

Before removing a term or API in a MAJOR release, it must be deprecated in at least one prior MINOR release.

A deprecated term:
- Remains in the compendium and resolvable via its URI
- Gains a `skos:deprecated true` annotation
- Gains a `dct:isReplacedBy` link to the replacement (if any)
- Triggers a deprecation warning in the Python/NPM packages when looked up

A deprecated API function:
- Remains callable
- Emits a `DeprecationWarning` with the target removal version and the migration path
- Is marked `@deprecated` in its docstring

## Version Communication

Each release is accompanied by:

1. A `CHANGELOG.md` entry (Keep a Changelog format)
2. A git tag (`v1.2.3`) signed with the maintainer's GPG key or Sigstore
3. A GitHub/GitLab Release
4. A Zenodo upload with full metadata
5. An announcement on the project's official channels
6. For MAJOR releases: a `MIGRATION.md` and a retrospective blog post

## Example Scenarios

| Change                                                        | Version bump |
| ------------------------------------------------------------- | ------------ |
| Add new term "Context Collapse"                               | MINOR        |
| Fix a typo in the definition of SLE                           | PATCH        |
| Add Chinese translation for RKE                               | MINOR        |
| Rename term `SSP` to `SEMPROG`                                | MAJOR        |
| Remove the experimental `AIPS-v2` term                        | MAJOR        |
| Add new relation type `aug:derives-from`                      | MINOR        |
| Tighten the SHACL shape to require `dct:created` on all terms | MAJOR (if existing data would fail) / PATCH (if it already passes) |
| Add a new `list_terms_by_year()` API function                 | MINOR        |
| Change default return type of `lookup()` from dict to dataclass | MAJOR      |
| Speed up `search()` with a better index (same results)        | PATCH        |


---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](../DISCLAIMER.md)) and the repository licenses ([`LICENSE`](../LICENSE)). Contact and provider: [`IMPRESSUM.md`](../IMPRESSUM.md).*
