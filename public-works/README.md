# AUGMANITAI — Selected Public Works

AI-generated catalogue documentation and descriptive metadata, compiled from Andreas Ehstand’s public project materials.

**Three entrances into Andreas Ehstand's public work: concepts as visual art, AI-generated films, and interaction among people, software agents and machines.**

This catalogue makes the published AUGMANITAI link catalogue readable as structured records. Each row describes a public collection or research page. It contains three records, with English titles and descriptions, source links, topics and attribution.

## Explore

| Public resource | Description |
|---|---|
| [Concepts and visual art](https://augmanitai.com/en/kunst) | A public collection exploring concepts through visual art, with links to related works. |
| [Signature Films](https://augmanitai.com/en/kino) | A collection of AI-generated short films on themes in Andreas Ehstand's work. |
| [SWAMANITAI](https://augmanitai.com/en/swamanitai) | A research perspective on interaction in mixed teams of people, software agents and machines. |

## Files and structure

- [works.jsonl](works.jsonl): exactly three JSON records, one per public resource.
- [works.jsonld](works.jsonld): the original catalogue's Schema.org representation, with the same three resources plus author and collection records.
- [LICENSE.md](LICENSE.md): licence scope for this metadata package.

JSONL fields: `id`, `title`, `description`, `resource_type`, `source_url`, `source_languages`, `keywords`, `author`, `author_url`, `source_snapshot_date`, `metadata_generated_by_ai`, `metadata_license` and `linked_work_rights`.

## Origin and AI disclosure

**AI-generated catalogue descriptions, metadata and catalogue documentation, compiled from public project materials. The JSONL records explicitly carry `metadata_generated_by_ai: true`.** Titles and descriptions are taken from the existing public catalogue. Converting them to JSONL adds a convenient data format without adding new work entries.

The source catalogue records its public-page snapshot as **15 September 2026**. These records describe collection-level entrances, not individual films, images or experiments. The linked pages may subsequently change.

The referenced Signature Films are AI-generated, including depicted people. The original media are available at the linked source pages; this repository contains metadata only.

## Intended use and scope

Use the records for discovery, attribution and source navigation. The selection is a small, author-specific view of a wider body of work. It is not exhaustive or representative of the AI-art field. SWAMANITAI is described as a research perspective; the records do not establish a deployed robotics system, model performance, peer review or priority of invention. No model weights, benchmarks, training examples, private correspondence or original media files are included.

## Attribution and rights

Author: **Andreas Ehstand** · [Public author page](https://augmanitai.com/en/autor/).

Catalogue text, catalogue documentation, JSON-LD and JSONL metadata are distributed under [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/), following the source catalogue's licence. This licence applies only to the files in this package. It does not relicense linked artworks, films, source pages or third-party material. Their own terms remain applicable; a link grants no additional rights to the linked work.

Source catalogue: *AUGMANITAI: Selected Public Works — Thoughts, Images, Moving Works, and Interaction*, [Zenodo, version 1.0.0](https://doi.org/10.5281/zenodo.22763843), 15 September 2026. This package is a format adaptation with new catalogue documentation and a JSONL representation. The collection identifier and citation are preserved in `works.jsonld`.
