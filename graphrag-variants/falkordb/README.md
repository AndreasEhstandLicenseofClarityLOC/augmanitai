# FalkorDB: Cypher-Based GraphRAG Variant

This directory contains a FalkorDB implementation for AUGMANITAI, a native graph database variant using Cypher for declarative graph pattern matching and querying.

## Overview

FalkorDB is a graph database optimized for pattern matching and complex graph traversal queries. This variant provides:

- **Native Graph Storage**: Nodes and relationships stored as first-class database objects
- **Cypher Query Language**: Declarative pattern matching for graph analysis
- **Constraint Enforcement**: Unique constraints and validation rules
- **Index Support**: Performance optimization through strategic indexing
- **Atomic Transactions**: ACID compliance for graph operations

## Files

- **cypher_init.cypher**: DDL/DML script to initialize all 25 AUGMANITAI concepts and 51 relationships in FalkorDB with constraints and indices.
- **query_examples.cypher**: 40+ representative Cypher queries demonstrating pattern matching, traversal, aggregation, and analytical patterns.
- **README.md**: This documentation file.

## Initialization

### Database Setup

```bash
# Connect to FalkorDB instance
falkordb-cli

# Load initialization script
SOURCE cypher_init.cypher

# Verify successful initialization
MATCH (c:Concept) RETURN COUNT(c) AS concept_count;
-- Expected result: 25
```

### Graph Structure

The initialized graph contains:

- **25 Concept Nodes** across 5 domains:
  - Linguistic Dynamics: SLE, DSM, SDS, APE (4 concepts)
  - Meta-Cognitive Processes: CCR, MCA, CIE, AIR, HCF, HRM, IKF, MAE (8 concepts)
  - Knowledge Synthesis: RKE, TEA, ECV, PDT, COD, TCI, RAS, QAM (8 concepts)
  - Interaction Dynamics: PLP, TCT, CSF, CDQ (4 concepts)
  - Organizational Context: AIF, ARS (2 concepts)

- **51 Relationships** with typed edges:
  - ENABLES: 12 relationships (enablement dependencies)
  - SUPPORTS: 11 relationships (foundational support)
  - DEPENDS_ON: 5 relationships (prerequisite dependencies)
  - CHALLENGES: 4 relationships (risk/challenge relationships)
  - ENHANCES: 3 relationships (improvement relationships)
  - COMPLICATES/IMPAIRS: 3 relationships (negative effects)
  - DISRUPTS: 2 relationships (severe impact)
  - Additional: PRECEDES, REQUIRES, SHAPES, IMPLEMENTS, etc.

Each relationship has a `strength` property (0.72-0.96) indicating relationship importance.

### Node Properties

Each Concept node contains:

```
{
  entity_id: 'sle',               // Unique identifier
  label: 'Symbiotic...',          // Full concept name
  abbreviation: 'SLE',            // 3-letter abbreviation
  domain: 'linguistic_dynamics',  // Domain classification
  definition: 'Linguistic...',    // Concept definition
  degree: 4,                      // Number of relationships
  pagerank_score: 0.0847,         // Global importance score
  centrality_betweenness: 0.087,  // Betweenness centrality
  concept_type: 'core'            // hub, core, or risk
}
```

## Cypher Query Patterns

### 1. Basic Entity Lookups

**Find specific concept:**
```cypher
MATCH (c:Concept {entity_id: 'rke'})
RETURN c.label, c.domain, c.definition;
```

**Find concepts in domain:**
```cypher
MATCH (c:Concept {domain: 'knowledge_synthesis'})
RETURN c.abbreviation, c.pagerank_score
ORDER BY c.pagerank_score DESC;
```

**Find hub concepts:**
```cypher
MATCH (c:Concept {concept_type: 'hub'})
RETURN c.label, c.degree
ORDER BY c.degree DESC;
```

### 2. Relationship Traversal

**Find outgoing relationships:**
```cypher
MATCH (rke:Concept {entity_id: 'rke'})-[r:ENABLES]->(target:Concept)
RETURN target.label, r.strength
ORDER BY r.strength DESC;
```

**Find incoming relationships:**
```cypher
MATCH (source:Concept)-[r:ENABLES]->(rke:Concept {entity_id: 'rke'})
RETURN source.label, r.strength;
```

**Find all relationship types:**
```cypher
MATCH (a:Concept)-[r]->(b:Concept)
RETURN DISTINCT type(r) AS relationship_type;
```

### 3. Neighborhood Analysis

**Immediate neighbors (1 hop):**
```cypher
MATCH (c:Concept {entity_id: 'mca'})-[r]-(neighbor:Concept)
RETURN neighbor.label, type(r), r.strength;
```

**Neighbors by relationship type:**
```cypher
MATCH (c:Concept {entity_id: 'ccr'})-[r:SUPPORTS]->(neighbor:Concept)
RETURN neighbor.label, neighbor.pagerank_score;
```

**Count neighbors per domain:**
```cypher
MATCH (c:Concept {entity_id: 'mca'})-[r]-(neighbor:Concept)
RETURN neighbor.domain, COUNT(*) AS count
ORDER BY count DESC;
```

### 4. Path Finding

**Shortest path:**
```cypher
MATCH path = shortestPath((sle:Concept {entity_id: 'sle'})-[*]-(rke:Concept {entity_id: 'rke'}))
RETURN [node in nodes(path) | node.label] AS path;
```

**Paths of specific length:**
```cypher
MATCH (a:Concept {entity_id: 'sle'})-[r1]->(b:Concept)-[r2]->(c:Concept)-[r3]->(d:Concept)
RETURN a.label, b.label, c.label, d.label;
```

**Paths with specific relationship types:**
```cypher
MATCH path = (start:Concept {entity_id: 'sle'})-[:ENABLES|SUPPORTS*1..3]-(end:Concept)
WHERE end.entity_id = 'rke'
RETURN [node in nodes(path) | node.label] AS path;
```

**Reachable within N hops:**
```cypher
MATCH (rke:Concept {entity_id: 'rke'})-[*1..2]->(reachable:Concept)
RETURN DISTINCT reachable.label;
```

### 5. Structural Analysis

**Hub concepts metrics:**
```cypher
MATCH (c:Concept {concept_type: 'hub'})
RETURN c.label, c.degree, c.centrality_betweenness, c.pagerank_score
ORDER BY c.pagerank_score DESC;
```

**Relationship strength aggregation:**
```cypher
MATCH (c:Concept)-[r]->()
RETURN c.label, SUM(r.strength) AS total_strength, COUNT(r) AS rel_count
ORDER BY total_strength DESC;
```

**Symmetric relationships:**
```cypher
MATCH (a:Concept)-[r1]->(b:Concept)<-[r2]-(a)
WHERE a.entity_id < b.entity_id
RETURN a.label, b.label, type(r1), type(r2);
```

### 6. Domain Analysis

**Intra-domain relationships:**
```cypher
MATCH (a:Concept {domain: 'linguistic_dynamics'})-[r]->(b:Concept {domain: 'linguistic_dynamics'})
RETURN a.label, type(r), b.label, r.strength;
```

**Inter-domain relationships:**
```cypher
MATCH (a:Concept)-[r]->(b:Concept)
WHERE a.domain <> b.domain
RETURN a.domain, type(r), b.domain, COUNT(*) AS connection_count
ORDER BY connection_count DESC;
```

**Domain influence patterns:**
```cypher
MATCH (a:Concept)-[r:ENABLES]->(b:Concept)
WHERE a.domain <> b.domain
RETURN a.domain AS source, b.domain AS target, COUNT(*) AS enable_count;
```

### 7. Advanced Analytics

**Bridge concepts (cross-domain connectors):**
```cypher
MATCH (c:Concept)-[r]->(neighbor:Concept)
WHERE c.domain <> neighbor.domain
WITH c, COUNT(DISTINCT neighbor.domain) AS domains, COUNT(r) AS rels
RETURN c.label, domains, rels
ORDER BY domains DESC;
```

**Relationship strength distribution:**
```cypher
MATCH ()-[r]->()
RETURN
  CASE
    WHEN r.strength >= 0.9 THEN 'Very Strong (0.9+)'
    WHEN r.strength >= 0.8 THEN 'Strong (0.8-0.9)'
    WHEN r.strength >= 0.7 THEN 'Moderate (0.7-0.8)'
    ELSE 'Weak (<0.7)'
  END AS category,
  COUNT(*) AS count;
```

**Impact scoring (ENABLES count):**
```cypher
MATCH (c:Concept)-[:ENABLES]->(target:Concept)
WITH c, COUNT(target) AS enables_count
RETURN c.label, enables_count
ORDER BY enables_count DESC;
```

### 8. Validation Queries

**Check constraint compliance:**
```cypher
-- Verify unique entity_id
MATCH (c1:Concept), (c2:Concept)
WHERE c1.entity_id = c2.entity_id AND c1 <> c2
RETURN COUNT(*) AS duplicates;
```

**Find orphaned concepts:**
```cypher
MATCH (c:Concept)
WHERE NOT ((c)-[]-())
RETURN c.label;
```

**Verify relationship strength ranges:**
```cypher
MATCH ()-[r]->()
WHERE r.strength < 0 OR r.strength > 1
RETURN COUNT(*) AS invalid;
```

### 9. Graph Statistics

**Overall metrics:**
```cypher
MATCH (c:Concept)
WITH COUNT(c) AS nodes
MATCH ()-[r]->()
WITH nodes, COUNT(r) AS edges
RETURN nodes, edges,
       toFloat(edges) / nodes AS avg_degree,
       toFloat(edges) / (nodes * (nodes - 1)) AS density;
```

**Domain distribution:**
```cypher
MATCH (c:Concept)
RETURN c.domain, COUNT(*) AS count
ORDER BY count DESC;
```

**Concept type distribution:**
```cypher
MATCH (c:Concept)
RETURN c.concept_type, COUNT(*) AS count;
```

**Relationship type distribution:**
```cypher
MATCH ()-[r]->()
RETURN type(r) AS type, COUNT(*) AS count, AVG(r.strength) AS avg_strength
ORDER BY count DESC;
```

## Performance Optimization

### Indices

The initialization script creates indices on:
- `:Concept(domain)` - Fast domain filtering
- `:Concept(concept_type)` - Fast type-based queries
- `:Concept(pagerank_score)` - Fast ranking queries

### Query Optimization Tips

1. **Use WHERE clauses early**: Filter nodes before traversal
   ```cypher
   MATCH (c:Concept) WHERE c.domain = 'knowledge_synthesis'
   MATCH (c)-[r]->(neighbor:Concept)
   ```

2. **Limit result sets**: Use LIMIT to reduce output
   ```cypher
   MATCH (c:Concept)
   ORDER BY c.pagerank_score DESC
   LIMIT 10
   ```

3. **Aggregate in queries**: Use COUNT, SUM, AVG for statistics
   ```cypher
   MATCH (c:Concept)-[r]->()
   RETURN c.label, COUNT(r) AS rel_count
   ```

4. **Use relationship type filters**: Reduce traversal scope
   ```cypher
   MATCH (c:Concept)-[:ENABLES|SUPPORTS]->(target:Concept)
   ```

## Query Execution Statistics

Expected execution characteristics for standard queries:

| Query Type | Typical Time | Notes |
|-----------|------------|-------|
| Single entity lookup | <1ms | Indexed by entity_id |
| Domain filtering | 1-2ms | Indexed by domain |
| Single hop traversal | 2-5ms | Degree-dependent |
| Path finding (2-3 hops) | 5-15ms | BFS expansion |
| Full graph analysis | 50-100ms | Aggregation over all nodes |

## Transaction Support

FalkorDB supports ACID transactions for all queries:

```cypher
BEGIN;
MATCH (c:Concept {entity_id: 'sle'})
SET c.pagerank_score = 0.0850;
COMMIT;
```

## Constraints

The database enforces:

1. **Unique entity_id**: Each concept has unique identifier
2. **Unique abbreviation**: Each concept has unique 3-letter code
3. **Property types**: Strength values are floats (0-1)
4. **Relationship validity**: Only valid relationship types allowed

## Integration with GraphRAG

FalkorDB can integrate as a backing store for GraphRAG:

```python
from falkordb import FalkorDB

# Connect to database
db = FalkorDB(host='localhost', port=6379)

# Execute query
result = db.query("""
  MATCH (c:Concept {entity_id: 'rke'})-[r:ENABLES]->(target:Concept)
  RETURN target.label, r.strength
""")

# Process results
for row in result:
    print(f"{row['target.label']}: {row['r.strength']}")
```

## AUGMANITAI Concepts in FalkorDB

All 25 AUGMANITAI concepts are modeled as Concept nodes with full properties, enabling:

- Domain-based filtering and analysis
- Relationship strength modeling
- Centrality metrics tracking
- PageRank-based importance ranking
- Cross-domain pattern discovery

## Citation

This implementation uses the AUGMANITAI framework by Andreas Ehstand:
- ORCID: 0009-0006-3773-7796
- DOI: 10.5281/zenodo.19481331
- License: CC BY-NC-ND 4.0

## Implementation Notes

- All relationships are directional (labeled edges)
- Self-referential relationships are excluded
- Relationship strength is normalized (0.72-0.96)
- Centrality metrics computed during initialization
- Graph is fully connected with no isolated nodes
