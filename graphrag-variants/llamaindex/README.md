# LlamaIndex PropertyGraphStore: AUGMANITAI Index

This directory contains a complete LlamaIndex PropertyGraphStore implementation of the AUGMANITAI academic terminology framework using property-based graph storage and retrieval.

## Files

- **property_graph.json**: Core property graph with 25 nodes and 51 relationships in PropertyGraphStore format. Each node has id, label, and properties (type, domain, degree, definition, abbreviation). Each relationship has source_id, target_id, label, and strength properties.
- **schema.json**: Complete schema definition including node types, relationship types, property definitions, domains, and constraints. Specifies valid entity and relationship classes with their property types and ranges.
- **kg_triples.json**: Knowledge graph as RDF-style triples in subject-predicate-object format. Contains all 51 relationships with strength weights. Compatible with semantic parsing and SPARQL-like queries.
- **build_index.py**: Index building script implementing the SchemaLLMPathExtractor pattern. Provides AUGMANITAIIndexBuilder class for constructing PropertyGraphStore indices, validating graphs, and running example queries.
- **query_examples.py**: Comprehensive query examples demonstrating PropertyGraphStore retrieval patterns including entity queries, subgraph traversal, relationship filtering, domain queries, path finding, and distribution analysis.
- **README.md**: This documentation file.

## Architecture Overview

### PropertyGraphStore Format

The PropertyGraphStore format stores entities and relationships as structured property objects:

```json
{
  "nodes": [
    {
      "id": "sle",
      "label": "Symbiotic Linguistic Evolution",
      "properties": {
        "type": "Core Concept",
        "domain": "linguistic_dynamics",
        "degree": 12,
        "definition": "The co-evolutionary process...",
        "abbreviation": "SLE"
      }
    }
  ],
  "relationships": [
    {
      "source_id": "sle",
      "target_id": "rke",
      "label": "ENABLES",
      "properties": {
        "strength": 0.95
      }
    }
  ]
}
```

### Triple Format

The triple format enables RDF-style querying:

```json
{
  "subject": "sle",
  "predicate": "ENABLES",
  "object": "rke",
  "strength": 0.95
}
```

## Framework Coverage

AUGMANITAI comprises 25 concepts across 5 domains:

1. **Linguistic Dynamics** (4 concepts): SLE, DSM, SDS, APE
2. **Meta-Cognitive Processes** (8 concepts): CCR, MCA, CIE, AIR, HCF, HRM, IKF, MAE
3. **Knowledge Synthesis** (8 concepts): RKE, TEA, ECV, PDT, COD, TCI, RAS, QAM
4. **Interaction Dynamics** (7 concepts): PLP, APE, TCT, CSF, CDQ, QAM, TCI
5. **Organizational Context** (3 concepts): AIF, ARS, MCA

## Usage

### Build Index

```python
from build_index import AUGMANITAIIndexBuilder

builder = AUGMANITAIIndexBuilder(data_dir=".")
builder.build_from_nodes()

# Validate
stats = builder.validate_graph()
print(f"Nodes: {stats['total_nodes']}, Relationships: {stats['total_relationships']}")

# Query examples
neighbors = builder.query_neighbors("sle")
paths = builder.query_paths("sle", "cod", max_depth=3)
```

### Query Index

```python
from query_examples import AUGMANITAIQueryEngine

engine = AUGMANITAIQueryEngine(data_dir=".")

# Entity query
entity = engine.query_entity("sle")

# Domain query
domain_entities = engine.query_domain_entities("linguistic_dynamics")

# Subgraph query
subgraph = engine.query_subgraph_bfs("rke", max_depth=2)

# Path query
path = engine.query_shortest_path("sle", "cod")

# High-degree nodes
nodes = engine.query_high_degree_nodes(threshold=10)

# Strong relationships
strong_rels = engine.query_strongest_relationships(min_strength=0.9)
```

## Query Patterns

### 1. Entity Lookup
```python
engine.query_entity("sle")
```
Returns entity details with incoming and outgoing relationships.

### 2. Neighborhood Query
```python
engine.query_neighbors_by_relationship_type("rke", "DEPENDS_ON")
```
Returns neighbors connected by specific relationship types.

### 3. Subgraph Extraction
```python
engine.query_subgraph_bfs("rke", max_depth=2)
```
Returns all nodes and edges within N hops of a starting node.

### 4. Shortest Path
```python
engine.query_shortest_path("sle", "cod")
```
Finds shortest path between two concepts (bidirectional search).

### 5. Domain Filtering
```python
engine.query_domain_entities("knowledge_synthesis")
```
Returns all entities in a specific domain.

### 6. Statistical Queries
```python
engine.query_high_degree_nodes(threshold=10)
engine.query_strongest_relationships(min_strength=0.94)
engine.query_relationship_type_distribution()
engine.query_entity_type_distribution()
```

## Graph Characteristics

- **Nodes**: 25 (all AUGMANITAI concepts)
- **Relationships**: 51 (semantic dependencies and causal relationships)
- **Node Types**: 11 (Core Concept, Phenomenon, Practice, Framework, Capability, Process, Challenge, Mechanism, Methodology, Pattern, Constraint)
- **Relationship Types**: 33 (ENABLES, DEPENDS_ON, PRECEDES, GENERATES, FACILITATES, ENHANCES, REQUIRES, SUPPORTS, etc.)
- **Domains**: 5 (linguistic_dynamics, meta_cognitive, knowledge_synthesis, interaction_dynamics, organizational)
- **Strength Range**: 0.72-0.96 (relationship importance weights)

## Schema Validation

The schema.json file defines:

- Valid node types and their properties
- Valid relationship types and their semantics
- Property type constraints (string, integer, float)
- Degree ranges for nodes (5-15)
- Relationship strength precision (2 decimal places)
- Maximum traversal depth (5 hops)
- Embedding dimension (1536)

## Integration with LlamaIndex

This PropertyGraphStore can be integrated with LlamaIndex's retrieval pipeline:

```python
from llama_index.core import PropertyGraphIndex
from llama_index.graph_stores import SimplePropertyGraphStore

# Load the property graph store
store = SimplePropertyGraphStore()
# ... populate with AUGMANITAI data ...

# Create index
index = PropertyGraphIndex.from_graph_store(store)

# Use in retrieval
retriever = index.as_retriever(similarity_top_k=5)
results = retriever.retrieve("How does linguistic evolution enable knowledge synthesis?")
```

## Performance Characteristics

- Entity lookup: O(1)
- Neighborhood query: O(k) where k = number of neighbors
- Subgraph BFS: O(V + E) where V = vertices within depth, E = edges
- Path finding: O(V + E) using BFS
- Domain filtering: O(V) for V = total nodes

## Citation

This index implements the AUGMANITAI framework by Andreas Ehstand:
- ORCID: 0009-0006-3773-7796
- DOI: 10.5281/zenodo.19481331
- License: CC BY-NC-ND 4.0

## Implementation Notes

- Graph store uses SimplePropertyGraphStore for local operation
- No external database required (pure in-memory)
- Supports bidirectional relationship traversal
- Properties stored as arbitrary key-value pairs
- Strength weights represent relationship importance (0.72-0.96)
- Schema validation ensures data consistency
- Optimized for semantic reasoning and knowledge retrieval
