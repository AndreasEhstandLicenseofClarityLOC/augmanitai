# Microsoft GraphRAG: AUGMANITAI Index

This directory contains a complete Microsoft GraphRAG (Community Summaries + Hierarchical Reports) implementation of the AUGMANITAI academic terminology framework.

## Files

- **entities.parquet.json**: Entity catalog with 25 core concepts. Each entity includes ID, name, type, description, text unit references, community assignments, and graph degree.
- **relationships.parquet.json**: Relationship catalog with 51 edges encoding dependencies, enables relationships, and critical causal patterns.
- **text_units.parquet.json**: Raw term definitions and explanatory text chunks for knowledge grounding.
- **communities.parquet.json**: Leiden clustering results producing 5 base communities + 3 hierarchical aggregations.
- **community_reports.parquet.json**: Comprehensive reports (300-600 words each) for each community with findings, rank scores, and synthesis.
- **hierarchical_reports.json**: Multi-level summaries (global, domain clusters, subclusters) showing how concepts organize at different levels.
- **settings.yaml**: Complete GraphRAG configuration template with all sections.
- **index_stats.json**: Indexing metadata, coverage analysis, and quality metrics.

## Framework Overview

AUGMANITAI comprises 25 concepts across 5 domains:

1. **Linguistic Dynamics** (4 concepts): How language evolves through human-AI interaction
2. **Meta-Cognitive Processes** (8 concepts): Dialogue quality, mutual understanding, self-awareness
3. **Knowledge Synthesis** (8 concepts): Knowledge acquisition, verification, collaborative reasoning
4. **Interaction Dynamics** (7 concepts): Dialogue structure, quality, conversational patterns
5. **Organizational Context** (3 concepts): Institutional adoption, risk management, governance

## Key Relationships

- Linguistic foundations (SLE, DSM) enable all higher-order collaboration
- Meta-cognitive alignment is a critical quality constraint
- Knowledge synthesis produces the intellectual output
- Interaction dynamics determine dialogue flow and quality
- Organizational context determines institutional impact

## Usage

This GraphRAG index supports three search patterns:

### Local Search
Query specific communities to understand focused topics:
```
Query: "How does dialogue quality improve?"
→ Returns entities from Interaction Dynamics community
```

### Global Search  
Query across the entire framework for comprehensive understanding:
```
Query: "What enables knowledge synthesis?"
→ Returns entities and relationships from Knowledge Synthesis community
   plus enabling relationships from other communities
```

### Drift Search
Track conceptual evolution and shifting relationships:
```
Query: "How does cognitive fatigue impact collaboration?"
→ Returns HCF and its cascading effects on related concepts
```

## Graph Statistics

- Entities: 25 (nodes)
- Relationships: 51 (edges)
- Communities: 5 base + 3 hierarchical
- Network Density: 0.174
- Average Degree: 4.08
- Modularity: 0.654 (high structure)

## Community Structures

**Base Communities:**
1. Linguistic Dynamics (4 entities)
2. Meta-Cognitive Processes (8 entities)
3. Knowledge Synthesis (8 entities)  
4. Interaction Dynamics (7 entities)
5. Organizational Context (3 entities)

**Hierarchical Integration:**
1. Linguistic-Cognitive Integration (merges 1+2)
2. Knowledge-Interaction Synthesis (merges 3+4)
3. Organizational Integration (augments with 5)

## Quality Metrics

- Relationship Coverage: 86%
- Semantic Coherence: 92%
- Community Quality: 88%
- Report Completeness: 95%

## Citation

This index implements the AUGMANITAI framework by Andreas Ehstand:
- ORCID: 0009-0006-3773-7796
- DOI: 10.5281/zenodo.19481331
- License: CC BY-NC-ND 4.0
- ISO Alignment: ISO 704, ISO 1087, ISO 30042

## Implementation Notes

This GraphRAG variant uses:
- **Community Detection**: Leiden algorithm (resolution=1.0)
- **Embeddings**: OpenAI text-embedding-3-small (1536-dim)
- **Chunk Size**: 1200 tokens with 100-token overlap
- **Report Length**: 300-600 words per community with structured findings

The index is optimized for both local exploration (understanding specific domains) and global synthesis (understanding how domains interact).
