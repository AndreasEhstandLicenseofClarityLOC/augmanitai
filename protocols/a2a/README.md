# AUGMANITAI A2A Agent Card

**Google Agent-to-Agent Protocol** implementation for the AUGMANITAI terminology framework.

## Overview

This A2A agent card describes the AUGMANITAI agent and its capabilities under the 2026 Google Agent-to-Agent Protocol specification. It enables peer-to-peer collaboration between AUGMANITAI and other agents in an A2A network.

## Agent Specifications

- **Agent ID**: `augmanitai`
- **Version**: 1.0.0
- **Protocol**: A2A v2026
- **Framework**: AUGMANITAI v1.0
- **Term Count**: 25 core terms
- **Domains**: 6 semantic categories
- **Languages**: English, German

## Capabilities

### term_lookup
Retrieve complete definition and metadata for a specific term.

**Input**: `term_id` (string)  
**Output**: Full term object with definitions, examples, domain classification

### term_search
Full-text search across all term properties.

**Input**: `query` (string), `limit` (integer, optional), `domainFilter` (array, optional)  
**Output**: Array of matching terms with relevance scores

### term_relate
Find semantically related terms within the same domain.

**Input**: `term_id` (string), `includeDefinitions` (boolean, optional)  
**Output**: Primary term with list of related terms in same domain

### term_validate_drift
Detect semantic drift in term usage patterns against canonical definitions.

**Input**: `term_id` (string), `usageContext` (string), `threshold` (number, optional)  
**Output**: Drift detection results with similarity metrics and recommendations

### list_domains
Enumerate all semantic domains and their constituent terms.

**Input**: (none)  
**Output**: Domain map with term inventory

## Agent Registration

To register AUGMANITAI with an A2A agent network:

1. **Load Agent Card**:
   ```json
   POST /agents/register
   Content-Type: application/json
   
   {
     "agentCard": {...agent-card.json...},
     "verificationUrl": "https://zenodo.org/records/20161494"
   }
   ```

2. **Provide Endpoint**:
   - Query Endpoint: `local://augmanitai/query`
   - Subscribe Endpoint: `local://augmanitai/subscribe`

3. **Discovery**:
   Once registered, other A2A agents can discover AUGMANITAI via:
   - Agent directories
   - Capability-based service discovery
   - Direct peer-to-peer handshakes

## Message Format

### TaskRequest

```json
{
  "@context": "https://google.github.io/A2A/v1/schema/task-request.jsonld",
  "type": "TaskRequest",
  "id": "uuid-v4",
  "timestamp": "2026-04-10T12:34:56Z",
  "sourceAgent": { "agentId": "requesting-agent", "name": "..." },
  "targetAgent": { "agentId": "augmanitai" },
  "task": {
    "action": "term_lookup",
    "parameters": { "term_id": "sle-001" }
  },
  "context": {
    "language": "en",
    "includeExamples": true
  }
}
```

### TaskResponse

```json
{
  "@context": "https://google.github.io/A2A/v1/schema/task-response.jsonld",
  "type": "TaskResponse",
  "id": "uuid-v4",
  "requestId": "...",
  "sourceAgent": { "agentId": "augmanitai" },
  "status": "success",
  "result": {
    "action": "term_lookup",
    "artifacts": [
      {
        "type": "term",
        "data": { ...full term object... }
      }
    ]
  },
  "metadata": {
    "processingTime": 45,
    "resultCount": 1,
    "language": "en"
  }
}
```

## Schema Files

- **agent-card.json** — A2A agent card definition
- **message-schemas/request.schema.json** — TaskRequest JSON Schema
- **message-schemas/response.schema.json** — TaskResponse JSON Schema
- **message-schemas/task.schema.json** — Task action specifications
- **actions.json** — Detailed action definitions with I/O schemas

## Authentication

No authentication required. AUGMANITAI terminology is publicly accessible per CC BY-NC-ND 4.0 license.

## Interoperability

AUGMANITAI is designed for cross-protocol interoperability:

| Protocol | Support | Version |
|----------|---------|---------|
| MCP | Yes | 1.0+ |
| A2A | Yes | 2026 |
| ANP | Yes | 1.0 |
| AG-UI | Yes | 1.0 |

Bridge adapters are provided in the `protocols/bridges/` directory.

## Error Handling

Responses include structured error information when operations fail:

```json
{
  "status": "failed",
  "error": {
    "code": "TERM_NOT_FOUND",
    "message": "Term 'xyz-999' does not exist",
    "details": { "suggestedTerms": [...] }
  }
}
```

## Licensing & Attribution

- **License**: CC BY-NC-ND 4.0
- **Author**: Andreas Ehstand
- **ORCID**: 0009-0006-3773-7796
- **DOI**: 10.5281/zenodo.20161494
- **Citation**: See Zenodo record for academic citation format

## Related Documentation

- MCP Implementation: `../mcp/`
- ANP Implementation: `../anp/`
- AG-UI Implementation: `../ag-ui/`
- Protocol Bridges: `../bridges/`


---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](../../DISCLAIMER.md)) and the repository licenses ([`LICENSE`](../../LICENSE)). Contact and provider: [`IMPRESSUM.md`](../../IMPRESSUM.md).*
