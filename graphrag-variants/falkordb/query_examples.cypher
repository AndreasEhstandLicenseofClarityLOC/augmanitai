-- FalkorDB Cypher Query Examples for AUGMANITAI
--
-- This file contains representative Cypher queries for the AUGMANITAI graph,
-- demonstrating common patterns, analytical queries, and traversal patterns.
--
-- Framework: AUGMANITAI
-- License: CC BY-NC-ND 4.0

-- ============================================================================
-- 1. BASIC ENTITY LOOKUPS
-- ============================================================================

-- Query 1.1: Find a specific concept by entity ID
-- Expected result: Single node with RKE concept details
MATCH (c:Concept {entity_id: 'rke'})
RETURN c.label, c.domain, c.definition, c.pagerank_score;

-- Query 1.2: Find all concepts in a domain
-- Expected result: 4 concepts in linguistic_dynamics domain
MATCH (c:Concept {domain: 'linguistic_dynamics'})
RETURN c.abbreviation, c.label, c.pagerank_score
ORDER BY c.pagerank_score DESC;

-- Query 1.3: Find hub concepts by concept type
-- Expected result: High-degree nodes (RKE, CCR, COD, MCA)
MATCH (c:Concept {concept_type: 'hub'})
RETURN c.entity_id, c.label, c.degree, c.pagerank_score
ORDER BY c.degree DESC;

-- Query 1.4: Find risk concepts
-- Expected result: HCF, ARS, ECV (concepts representing risks or challenges)
MATCH (c:Concept {concept_type: 'risk'})
RETURN c.entity_id, c.label, c.domain, c.definition;

-- ============================================================================
-- 2. RELATIONSHIP TRAVERSAL
-- ============================================================================

-- Query 2.1: Find all concepts that RKE enables
-- Expected result: Concepts directly enabled by RKE (ENABLES relationship)
MATCH (rke:Concept {entity_id: 'rke'})-[r:ENABLES]->(target:Concept)
RETURN target.label, r.strength
ORDER BY r.strength DESC;

-- Query 2.2: Find all concepts that enable RKE
-- Expected result: Concepts with ENABLES relationship pointing to RKE
MATCH (source:Concept)-[r:ENABLES]->(rke:Concept {entity_id: 'rke'})
RETURN source.label, source.domain, r.strength
ORDER BY r.strength DESC;

-- Query 2.3: Find all relationships of a specific type
-- Expected result: All ENABLES relationships with strength scores
MATCH (a:Concept)-[r:ENABLES]->(b:Concept)
RETURN a.label, b.label, r.strength
ORDER BY r.strength DESC
LIMIT 10;

-- Query 2.4: Find bidirectional relationships
-- Expected result: Concept pairs with relationships in both directions
MATCH (a:Concept)-[r1]->(b:Concept)-[r2]->(a)
WHERE type(r1) <> type(r2)
RETURN a.label, type(r1), b.label, type(r2)
LIMIT 5;

-- ============================================================================
-- 3. NEIGHBORHOOD ANALYSIS
-- ============================================================================

-- Query 3.1: Find immediate neighbors of a concept
-- Expected result: All directly connected concepts (1 hop)
MATCH (c:Concept {entity_id: 'mca'})-[r]-(neighbor:Concept)
RETURN neighbor.label, neighbor.domain, type(r), r.strength
ORDER BY r.strength DESC;

-- Query 3.2: Find neighbors by relationship type
-- Expected result: Only concepts connected via SUPPORTS relationships
MATCH (c:Concept {entity_id: 'ccr'})-[r:SUPPORTS]->(neighbor:Concept)
RETURN neighbor.label, neighbor.pagerank_score, r.strength;

-- Query 3.3: Count neighbors per domain
-- Expected result: Distribution of neighbors across domains
MATCH (c:Concept {entity_id: 'mca'})-[r]-(neighbor:Concept)
RETURN neighbor.domain, COUNT(*) AS neighbor_count
ORDER BY neighbor_count DESC;

-- Query 3.4: Find concept with most outgoing relationships
-- Expected result: Concept with highest out-degree
MATCH (c:Concept)-[r]->()
RETURN c.entity_id, c.label, COUNT(r) AS outgoing_count
ORDER BY outgoing_count DESC
LIMIT 5;

-- ============================================================================
-- 4. PATH FINDING AND CONNECTIVITY
-- ============================================================================

-- Query 4.1: Find shortest path between two concepts
-- Expected result: Shortest path from SLE to RKE with relationship labels
MATCH path = shortestPath((sle:Concept {entity_id: 'sle'})-[*]-(rke:Concept {entity_id: 'rke'}))
RETURN [node in nodes(path) | node.label] AS path_nodes,
       [rel in relationships(path) | type(rel)] AS path_types;

-- Query 4.2: Find all paths of length exactly 3
-- Expected result: All 3-hop paths between specified concepts
MATCH (a:Concept {entity_id: 'sle'})-[r1]->(b:Concept)-[r2]->(c:Concept)-[r3]->(d:Concept)
RETURN a.label, b.label, c.label, d.label, type(r1), type(r2), type(r3)
LIMIT 10;

-- Query 4.3: Find paths with specific relationship types
-- Expected result: Paths that only use ENABLES and SUPPORTS relationships
MATCH path = (start:Concept {entity_id: 'sle'})-[:ENABLES|SUPPORTS*1..3]-(end:Concept)
WHERE end.entity_id = 'rke'
RETURN [node in nodes(path) | node.entity_id] AS path,
       length(path) AS path_length;

-- Query 4.4: Find concepts reachable from a source within N hops
-- Expected result: All concepts reachable from RKE within 2 hops
MATCH (rke:Concept {entity_id: 'rke'})-[*1..2]->(reachable:Concept)
RETURN DISTINCT reachable.label, reachable.domain
ORDER BY reachable.label;

-- ============================================================================
-- 5. STRUCTURAL ANALYSIS
-- ============================================================================

-- Query 5.1: Find all hub concepts and their metrics
-- Expected result: Central nodes with high betweenness and degree
MATCH (c:Concept {concept_type: 'hub'})
RETURN c.label, c.degree, c.centrality_betweenness, c.pagerank_score
ORDER BY c.pagerank_score DESC;

-- Query 5.2: Calculate total relationship strength from each concept
-- Expected result: Concepts ranked by total outgoing relationship strength
MATCH (c:Concept)-[r]->()
RETURN c.label, SUM(r.strength) AS total_strength, COUNT(r) AS relationship_count
ORDER BY total_strength DESC
LIMIT 10;

-- Query 5.3: Find concepts with symmetric relationships
-- Expected result: Concept pairs with bidirectional connections
MATCH (a:Concept)-[r1]->(b:Concept)<-[r2]-(a)
WHERE a.entity_id < b.entity_id
RETURN a.label, type(r1), b.label, type(r2), r1.strength, r2.strength;

-- Query 5.4: Identify strongly connected components
-- Expected result: Groups of mutually reachable concepts
MATCH (a:Concept)-[*2..4]->(b:Concept)
WHERE a.entity_id = 'mca' OR b.entity_id = 'mca'
RETURN COUNT(DISTINCT a) AS component_size;

-- ============================================================================
-- 6. DOMAIN-SPECIFIC ANALYSIS
-- ============================================================================

-- Query 6.1: Find all intra-domain relationships
-- Expected result: Relationships within linguistic_dynamics domain
MATCH (a:Concept {domain: 'linguistic_dynamics'})-[r]->(b:Concept {domain: 'linguistic_dynamics'})
RETURN a.label, type(r), b.label, r.strength
ORDER BY r.strength DESC;

-- Query 6.2: Find inter-domain relationships
-- Expected result: Connections between different domains
MATCH (a:Concept)-[r]->(b:Concept)
WHERE a.domain <> b.domain
RETURN a.domain, type(r), b.domain, COUNT(*) AS connection_count
ORDER BY connection_count DESC;

-- Query 6.3: Find domain influence patterns
-- Expected result: Which domains influence which other domains
MATCH (a:Concept)-[r:ENABLES]->(b:Concept)
WHERE a.domain <> b.domain
RETURN a.domain AS source_domain, b.domain AS target_domain, COUNT(*) AS enable_count
ORDER BY enable_count DESC;

-- Query 6.4: Analyze domain PageRank distribution
-- Expected result: Average PageRank score by domain
MATCH (c:Concept)
RETURN c.domain, AVG(c.pagerank_score) AS avg_pagerank, COUNT(*) AS concept_count
ORDER BY avg_pagerank DESC;

-- ============================================================================
-- 7. COMPLEX ANALYTICAL PATTERNS
-- ============================================================================

-- Query 7.1: Find concepts that form bridges between domains
-- Expected result: Concepts with high cross-domain connectivity
MATCH (c:Concept)-[r]->(neighbor:Concept)
WHERE c.domain <> neighbor.domain
WITH c, COUNT(DISTINCT neighbor.domain) AS domain_connections, COUNT(r) AS total_connections
RETURN c.label, c.domain, domain_connections, total_connections
ORDER BY domain_connections DESC, total_connections DESC;

-- Query 7.2: Analyze relationship strength distribution
-- Expected result: Histogram of relationship strengths
MATCH ()-[r]->()
RETURN
  CASE
    WHEN r.strength >= 0.9 THEN 'Very Strong (0.9+)'
    WHEN r.strength >= 0.8 THEN 'Strong (0.8-0.9)'
    WHEN r.strength >= 0.7 THEN 'Moderate (0.7-0.8)'
    ELSE 'Weak (<0.7)'
  END AS strength_category,
  COUNT(*) AS count
ORDER BY strength_category DESC;

-- Query 7.3: Find enabling chains (transitive ENABLES relationships)
-- Expected result: Multi-hop ENABLES paths
MATCH path = (a:Concept)-[:ENABLES*2..3]->(b:Concept)
WHERE a.entity_id = 'sle'
RETURN [node in nodes(path) | node.label] AS concept_chain,
       length(path) AS chain_length;

-- Query 7.4: Calculate impact scores (outgoing ENABLES count)
-- Expected result: Concepts that enable many others (high impact)
MATCH (c:Concept)-[:ENABLES]->(target:Concept)
WITH c, COUNT(target) AS enables_count
RETURN c.label, enables_count, c.concept_type
ORDER BY enables_count DESC
LIMIT 10;

-- ============================================================================
-- 8. VALIDATION AND CONSISTENCY CHECKS
-- ============================================================================

-- Query 8.1: Verify uniqueness constraints
-- Expected result: Should return 0 if entity_id is unique
MATCH (c1:Concept), (c2:Concept)
WHERE c1.entity_id = c2.entity_id AND c1 <> c2
RETURN COUNT(*) AS duplicate_count;

-- Query 8.2: Find orphaned concepts (no relationships)
-- Expected result: Should be empty for well-formed graph
MATCH (c:Concept)
WHERE NOT ((c)-[r]-())
RETURN c.label, c.entity_id;

-- Query 8.3: Verify relationship strength ranges
-- Expected result: All relationships have strength between 0 and 1
MATCH ()-[r]->()
WHERE r.strength < 0 OR r.strength > 1
RETURN COUNT(*) AS invalid_strength_count;

-- Query 8.4: Check for self-referential relationships
-- Expected result: Should be empty (no concept enables itself)
MATCH (c:Concept)-[r]->(c)
RETURN c.label, type(r);

-- ============================================================================
-- 9. AGGREGATION AND STATISTICS
-- ============================================================================

-- Query 9.1: Overall graph statistics
-- Expected result: Node count, edge count, average degree
MATCH (c:Concept)
WITH COUNT(c) AS node_count
MATCH ()-[r]->()
WITH node_count, COUNT(r) AS edge_count
RETURN node_count, edge_count,
       toFloat(edge_count) / node_count AS average_degree,
       toFloat(edge_count) / (node_count * (node_count - 1)) AS network_density;

-- Query 9.2: Concept metrics summary
-- Expected result: Min, max, average for key metrics
MATCH (c:Concept)
RETURN
  MIN(c.degree) AS min_degree,
  MAX(c.degree) AS max_degree,
  AVG(c.degree) AS avg_degree,
  MIN(c.pagerank_score) AS min_pagerank,
  MAX(c.pagerank_score) AS max_pagerank,
  AVG(c.pagerank_score) AS avg_pagerank;

-- Query 9.3: Relationship type distribution
-- Expected result: Count of each relationship type
MATCH ()-[r]->()
RETURN type(r) AS relationship_type, COUNT(*) AS count, AVG(r.strength) AS avg_strength
ORDER BY count DESC;

-- Query 9.4: Concept type distribution
-- Expected result: Count of each concept type
MATCH (c:Concept)
RETURN c.concept_type, COUNT(*) AS count
ORDER BY count DESC;

-- ============================================================================
-- 10. QUERY OPTIMIZATION PATTERNS
-- ============================================================================

-- Query 10.1: Use index for domain filtering
-- Expected result: Fast lookup of concepts in a specific domain
MATCH (c:Concept)
WHERE c.domain = 'knowledge_synthesis'
RETURN c.entity_id, c.label
LIMIT 10;

-- Query 10.2: Filter by multiple attributes
-- Expected result: Hub concepts in meta_cognitive domain
MATCH (c:Concept)
WHERE c.domain = 'meta_cognitive' AND c.concept_type = 'hub'
RETURN c.label, c.degree, c.pagerank_score;

-- Query 10.3: Limit result set early
-- Expected result: Only top 5 concepts by PageRank
MATCH (c:Concept)
RETURN c.label, c.pagerank_score
ORDER BY c.pagerank_score DESC
LIMIT 5;

-- Query 10.4: Use aggregation for counting
-- Expected result: Efficient counting with GROUP BY
MATCH (c:Concept)-[r:ENABLES]->(target:Concept)
RETURN c.label, COUNT(target) AS enables_count
ORDER BY enables_count DESC
LIMIT 5;
