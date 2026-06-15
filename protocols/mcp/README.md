# AUGMANITAI MCP Server

**Model Context Protocol** implementation for the AUGMANITAI academic terminology framework.

## Overview

This MCP server exposes the AUGMANITAI term database (25 core terms describing human-AI interaction phenomena) through the Model Context Protocol, enabling any MCP-compatible client to query, search, and navigate the terminology.

## Features

- **lookup_term**: Retrieve specific term definitions by ID or abbreviation
- **search_terms**: Full-text search across term names, definitions, and domains
- **get_related**: Find semantically related terms within the same domain
- **list_domains**: Explore all semantic domains and their contents

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Starting the Server

```bash
python server.py
```

The server will load the AUGMANITAI terms database and await MCP client connections.

### MCP Client Integration

Configure your MCP client to connect to this server:

```json
{
  "mcpServers": {
    "augmanitai": {
      "command": "python",
      "args": ["/path/to/server.py"]
    }
  }
}
```

## API Reference

### lookup_term(term_id: str) -> str

Retrieve a specific term by its ID (e.g., 'sle-001') or abbreviation (e.g., 'SLE').

**Response**: Complete term object including:
- Multilingual names (EN/DE)
- Full definitions (EN/DE)
- Semantic domain classification
- Usage examples
- ISO standard alignment

### search_terms(query: str) -> str

Search terms using full-text matching across:
- Term names (English and German)
- Definitions (English and German)
- Abbreviations
- Semantic domains

**Response**: JSON array of matching term objects.

### get_related(term_id: str) -> str

Return the specified term plus all related terms within its semantic domain.

**Response**: Object containing:
- Primary term
- Domain classification
- Count and list of related terms

### list_domains() -> str

Enumerate all semantic domains and their constituent terms.

**Response**: Object with:
- Mapping of domain names to term lists
- Total domain count
- Total term count

## Term Database

- **Location**: `../../augmanitai-python/augmanitai/data/terms.json`
- **Term Count**: 25 core terms
- **Domains**: 6 semantic categories
  - linguistic_dynamics
  - knowledge_extraction
  - cognitive_processes
  - measurement_metrics
  - systemic_effects
  - terminological_phenomena
- **Languages**: English, German
- **ISO Compliance**: ISO 704, ISO 1087, ISO 30042

## Author

Andreas Ehstand  
ORCID: 0009-0006-3773-7796  
DOI: 10.5281/zenodo.20161494  

## License

CC BY-NC-ND 4.0 — AUGMANITAI terminology framework  
Non-commercial use only. No derivative works permitted without explicit attribution.

## Architecture

```
server.py
├── MCP Server Core
├── Term Database Loader (terms.json)
├── Search Index (in-memory)
├── Tool Handlers
│   ├── lookup_term()
│   ├── search_terms()
│   ├── get_related()
│   └── list_domains()
└── JSON Schema Validation
```

## Schema Files

- `manifest.json` — MCP server metadata and tool registry
- `tool-schemas.json` — JSON Schema definitions for all tool inputs/outputs

## Error Handling

All tool responses include graceful error messages when:
- Term ID not found (returns `{"error": "..."}`)
- Invalid search query
- Malformed request parameters

JSON Schema validation ensures request integrity before processing.


---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](../../DISCLAIMER.md)) and the repository licenses ([`LICENSE`](../../LICENSE)). Contact and provider: [`IMPRESSUM.md`](../../IMPRESSUM.md).*
