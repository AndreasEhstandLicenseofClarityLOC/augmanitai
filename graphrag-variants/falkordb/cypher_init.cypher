-- FalkorDB Cypher Initialization Script for AUGMANITAI
-- This script initializes the FalkorDB graph database with AUGMANITAI concepts
-- and relationships, enabling Cypher-based graph pattern matching and analysis.
--
-- Framework: AUGMANITAI
-- Author: Andreas Ehstand (ORCID 0009-0006-3773-7796)
-- License: CC BY-NC-ND 4.0

-- ============================================================================
-- 1. CREATE CONSTRAINT DEFINITIONS
-- ============================================================================

-- Constraint: Node IDs are unique
CREATE CONSTRAINT ON (n:Concept)
  ASSERT n.entity_id IS UNIQUE;

CREATE CONSTRAINT ON (n:Concept)
  ASSERT n.abbreviation IS UNIQUE;

-- ============================================================================
-- 2. CREATE LINGUISTIC DYNAMICS CONCEPTS
-- ============================================================================

CREATE (sle:Concept {
  entity_id: 'sle',
  label: 'Symbiotic Linguistic Evolution',
  abbreviation: 'SLE',
  domain: 'linguistic_dynamics',
  definition: 'Linguistic co-evolution enabling shared understanding and communicative adaptation',
  degree: 4,
  pagerank_score: 0.0847,
  centrality_betweenness: 0.087,
  concept_type: 'core'
});

CREATE (dsm:Concept {
  entity_id: 'dsm',
  label: 'Domain-Specific Metalanguage',
  abbreviation: 'DSM',
  domain: 'linguistic_dynamics',
  definition: 'Specialized vocabulary and professional dialects for precise abstraction',
  degree: 4,
  pagerank_score: 0.0756,
  centrality_betweenness: 0.045,
  concept_type: 'core'
});

CREATE (sds:Concept {
  entity_id: 'sds',
  label: 'Semantic Drift Sensitivity',
  abbreviation: 'SDS',
  domain: 'linguistic_dynamics',
  definition: 'Detection and tracking of semantic meaning evolution and connotation changes',
  degree: 3,
  pagerank_score: 0.0615,
  centrality_betweenness: 0.032,
  concept_type: 'core'
});

CREATE (ape:Concept {
  entity_id: 'ape',
  label: 'Adaptive Protocol Evolution',
  abbreviation: 'APE',
  domain: 'linguistic_dynamics',
  definition: 'Implicit feedback-driven refinement of interaction protocols',
  degree: 3,
  pagerank_score: 0.0534,
  centrality_betweenness: 0.028,
  concept_type: 'core'
});

-- ============================================================================
-- 3. CREATE META-COGNITIVE CONCEPTS
-- ============================================================================

CREATE (ccr:Concept {
  entity_id: 'ccr',
  label: 'Context-Cognition Resonance',
  abbreviation: 'CCR',
  domain: 'meta_cognitive',
  definition: 'Emergent alignment between contextual understanding and cognitive frameworks',
  degree: 6,
  pagerank_score: 0.0805,
  centrality_betweenness: 0.134,
  concept_type: 'hub'
});

CREATE (mca:Concept {
  entity_id: 'mca',
  label: 'Mutual Context Awareness',
  abbreviation: 'MCA',
  domain: 'meta_cognitive',
  definition: 'Shared understanding of discussion boundaries and narrative continuity',
  degree: 7,
  pagerank_score: 0.0834,
  centrality_betweenness: 0.098,
  concept_type: 'hub'
});

CREATE (cie:Concept {
  entity_id: 'cie',
  label: 'Cognitive Intimacy Exchange',
  abbreviation: 'CIE',
  domain: 'meta_cognitive',
  definition: 'Progressive deepening of intellectual vulnerability and abstract thought sharing',
  degree: 5,
  pagerank_score: 0.0692,
  centrality_betweenness: 0.067,
  concept_type: 'core'
});

CREATE (air:Concept {
  entity_id: 'air',
  label: 'AI Intent Recognition',
  abbreviation: 'AIR',
  domain: 'meta_cognitive',
  definition: 'Inference of human goals, values, and constraints through dialogue analysis',
  degree: 4,
  pagerank_score: 0.0721,
  centrality_betweenness: 0.058,
  concept_type: 'core'
});

CREATE (hcf:Concept {
  entity_id: 'hcf',
  label: 'Human Cognitive Fatigue',
  abbreviation: 'HCF',
  domain: 'meta_cognitive',
  definition: 'Degradation of human cognitive performance and reasoning quality',
  degree: 3,
  pagerank_score: 0.0487,
  centrality_betweenness: 0.021,
  concept_type: 'risk'
});

CREATE (hrm:Concept {
  entity_id: 'hrm',
  label: 'Human Relevance Mapping',
  abbreviation: 'HRM',
  domain: 'meta_cognitive',
  definition: 'Recognition of value connections and importance assessment',
  degree: 3,
  pagerank_score: 0.0461,
  centrality_betweenness: 0.019,
  concept_type: 'core'
});

CREATE (ikf:Concept {
  entity_id: 'ikf',
  label: 'Implicit Knowledge Frames',
  abbreviation: 'IKF',
  domain: 'meta_cognitive',
  definition: 'Background assumptions and cultural references shaping interpretation',
  degree: 3,
  pagerank_score: 0.0598,
  centrality_betweenness: 0.034,
  concept_type: 'core'
});

CREATE (mae:Concept {
  entity_id: 'mae',
  label: 'Multimodal Alignment Engine',
  abbreviation: 'MAE',
  domain: 'meta_cognitive',
  definition: 'Integration and synthesis across modalities for coherent understanding',
  degree: 3,
  pagerank_score: 0.0502,
  centrality_betweenness: 0.024,
  concept_type: 'core'
});

-- ============================================================================
-- 4. CREATE KNOWLEDGE SYNTHESIS CONCEPTS
-- ============================================================================

CREATE (rke:Concept {
  entity_id: 'rke',
  label: 'Recursive Knowledge Expansion',
  abbreviation: 'RKE',
  domain: 'knowledge_synthesis',
  definition: 'Iterative deepening and cumulative understanding through multi-turn refinement',
  degree: 5,
  pagerank_score: 0.0923,
  centrality_betweenness: 0.156,
  concept_type: 'hub'
});

CREATE (tea:Concept {
  entity_id: 'tea',
  label: 'Temporal Episodic Anchoring',
  abbreviation: 'TEA',
  domain: 'knowledge_synthesis',
  definition: 'Temporal marking and decision anchoring with retrospective reference points',
  degree: 3,
  pagerank_score: 0.0421,
  centrality_betweenness: 0.018,
  concept_type: 'core'
});

CREATE (ecv:Concept {
  entity_id: 'ecv',
  label: 'Epistemic Confidence Variance',
  abbreviation: 'ECV',
  domain: 'knowledge_synthesis',
  definition: 'Variance between confidence and validity in knowledge assertions',
  degree: 2,
  pagerank_score: 0.0542,
  centrality_betweenness: 0.015,
  concept_type: 'risk'
});

CREATE (pdt:Concept {
  entity_id: 'pdt',
  label: 'Probabilistic Decision Transparency',
  abbreviation: 'PDT',
  domain: 'knowledge_synthesis',
  definition: 'Explicit articulation of reasoning branches and decision confidence weights',
  degree: 3,
  pagerank_score: 0.0687,
  centrality_betweenness: 0.042,
  concept_type: 'core'
});

CREATE (cod:Concept {
  entity_id: 'cod',
  label: 'Collaborative Ontology Development',
  abbreviation: 'COD',
  domain: 'knowledge_synthesis',
  definition: 'Joint framework creation and co-constructed shared knowledge structures',
  degree: 5,
  pagerank_score: 0.0845,
  centrality_betweenness: 0.123,
  concept_type: 'hub'
});

CREATE (tci:Concept {
  entity_id: 'tci',
  label: 'Temporal Cognitive Integration',
  abbreviation: 'TCI',
  domain: 'knowledge_synthesis',
  definition: 'Synthesis across time scales for coherent temporal understanding',
  degree: 3,
  pagerank_score: 0.0625,
  centrality_betweenness: 0.038,
  concept_type: 'core'
});

CREATE (ras:Concept {
  entity_id: 'ras',
  label: 'Reasoning Artifact Symbiosis',
  abbreviation: 'RAS',
  domain: 'knowledge_synthesis',
  definition: 'Co-production of cognitive scaffolding and externalized thinking artifacts',
  degree: 4,
  pagerank_score: 0.0791,
  centrality_betweenness: 0.056,
  concept_type: 'core'
});

CREATE (qam:Concept {
  entity_id: 'qam',
  label: 'Query-Answer Morphodynamics',
  abbreviation: 'QAM',
  domain: 'knowledge_synthesis',
  definition: 'Dialogue shape-shifting and mutual influence in question-answer dynamics',
  degree: 3,
  pagerank_score: 0.0643,
  centrality_betweenness: 0.031,
  concept_type: 'core'
});

-- ============================================================================
-- 5. CREATE INTERACTION DYNAMICS CONCEPTS
-- ============================================================================

CREATE (plp:Concept {
  entity_id: 'plp',
  label: 'Prompt-Level Personality',
  abbreviation: 'PLP',
  domain: 'interaction_dynamics',
  definition: 'Emergent persona and conversation voice in interaction sessions',
  degree: 4,
  pagerank_score: 0.0568,
  centrality_betweenness: 0.041,
  concept_type: 'core'
});

CREATE (tct:Concept {
  entity_id: 'tct',
  label: 'Threshold-Crossing Transformation',
  abbreviation: 'TCT',
  domain: 'interaction_dynamics',
  definition: 'Qualitative shifts and phase transitions in interaction quality',
  degree: 4,
  pagerank_score: 0.0654,
  centrality_betweenness: 0.049,
  concept_type: 'core'
});

CREATE (csf:Concept {
  entity_id: 'csf',
  label: 'Contextual Sensemaking Framework',
  abbreviation: 'CSF',
  domain: 'interaction_dynamics',
  definition: 'Organizing responses for narrative coherence and meaning construction',
  degree: 4,
  pagerank_score: 0.0678,
  centrality_betweenness: 0.052,
  concept_type: 'core'
});

CREATE (cdq:Concept {
  entity_id: 'cdq',
  label: 'Convergent-Divergent Questioning',
  abbreviation: 'CDQ',
  domain: 'interaction_dynamics',
  definition: 'Question pattern alternation for focused exploration and scope modulation',
  degree: 3,
  pagerank_score: 0.0712,
  centrality_betweenness: 0.044,
  concept_type: 'core'
});

-- ============================================================================
-- 6. CREATE ORGANIZATIONAL CONTEXT CONCEPTS
-- ============================================================================

CREATE (aif:Concept {
  entity_id: 'aif',
  label: 'AI Institutional Fluency',
  abbreviation: 'AIF',
  domain: 'organizational',
  definition: 'Operating within organizational norms and institutional integration',
  degree: 2,
  pagerank_score: 0.0612,
  centrality_betweenness: 0.035,
  concept_type: 'core'
});

CREATE (ars:Concept {
  entity_id: 'ars',
  label: 'Asymmetric Risk Sharing',
  abbreviation: 'ARS',
  domain: 'organizational',
  definition: 'Imbalanced accountability structures and responsibility asymmetry',
  degree: 2,
  pagerank_score: 0.0388,
  centrality_betweenness: 0.012,
  concept_type: 'risk'
});

-- ============================================================================
-- 7. CREATE LINGUISTIC RELATIONSHIPS
-- ============================================================================

-- SLE relationships
CREATE (sle)-[:ENABLES {strength: 0.92}]->(cod);
CREATE (sle)-[:ENABLES {strength: 0.88}]->(rke);
CREATE (sle)-[:SUPPORTS {strength: 0.85}]->(dsm);
CREATE (sle)-[:PRECEDES {strength: 0.80}]->(ape);

-- DSM relationships
CREATE (dsm)-[:ENABLES {strength: 0.89}]->(cod);
CREATE (dsm)-[:SUPPORTS {strength: 0.86}]->(mca);
CREATE (dsm)-[:DEPENDS_ON {strength: 0.91}]->(sle);

-- SDS relationships
CREATE (sds)-[:CHALLENGES {strength: 0.78}]->(ccr);
CREATE (sds)-[:IMPAIRS {strength: 0.74}]->(mca);
CREATE (sds)-[:SUPPORTS {strength: 0.82}]->(ikf);

-- APE relationships
CREATE (ape)-[:ENABLES {strength: 0.85}]->(tct);
CREATE (ape)-[:SUPPORTS {strength: 0.80}]->(csf);
CREATE (ape)-[:DEPENDS_ON {strength: 0.88}]->(sle);

-- ============================================================================
-- 8. CREATE COGNITIVE RELATIONSHIPS
-- ============================================================================

-- CCR relationships
CREATE (ccr)-[:SUPPORTS {strength: 0.93}]->(mca);
CREATE (ccr)-[:ENABLES {strength: 0.90}]->(cie);
CREATE (ccr)-[:DEPENDS_ON {strength: 0.92}]->(csf);

-- MCA relationships
CREATE (mca)-[:SUPPORTS {strength: 0.94}]->(tea);
CREATE (mca)-[:ENABLES {strength: 0.89}]->(air);
CREATE (mca)-[:CHALLENGES {strength: 0.76}]->(hcf);

-- CIE relationships
CREATE (cie)-[:ENABLES {strength: 0.87}]->(rke);
CREATE (cie)-[:SUPPORTS {strength: 0.85}]->(tct);
CREATE (cie)-[:DISRUPTS {strength: 0.72}]->(hcf);

-- AIR relationships
CREATE (air)-[:SUPPORTS {strength: 0.88}]->(pdt);
CREATE (air)-[:ENABLES {strength: 0.86}]->(aif);

-- IKF relationships
CREATE (ikf)-[:CHALLENGES {strength: 0.77}]->(mca);
CREATE (ikf)-[:COMPLICATES {strength: 0.79}]->(air);

-- MAE relationships
CREATE (mae)-[:ENABLES {strength: 0.84}]->(ccr);
CREATE (mae)-[:ENHANCES {strength: 0.83}]->(ras);

-- ============================================================================
-- 9. CREATE KNOWLEDGE SYNTHESIS RELATIONSHIPS
-- ============================================================================

-- RKE relationships
CREATE (rke)-[:DEPENDS_ON {strength: 0.96}]->(ccr);
CREATE (rke)-[:ENABLES {strength: 0.91}]->(tea);
CREATE (rke)-[:REQUIRES {strength: 0.89}]->(cod);
CREATE (rke)-[:SUPPORTS {strength: 0.87}]->(qam);

-- TEA relationships
CREATE (tea)-[:SUPPORTS {strength: 0.90}]->(tci);
CREATE (tea)-[:ENABLES {strength: 0.86}]->(ras);

-- ECV relationships
CREATE (ecv)-[:CHALLENGES {strength: 0.75}]->(pdt);
CREATE (ecv)-[:IMPAIRS {strength: 0.73}]->(rke);

-- PDT relationships
CREATE (pdt)-[:SUPPORTS {strength: 0.91}]->(ras);
CREATE (pdt)-[:DEPENDS_ON {strength: 0.92}]->(air);

-- COD relationships
CREATE (cod)-[:ENABLES {strength: 0.93}]->(rke);
CREATE (cod)-[:SUPPORTS {strength: 0.88}]->(csf);
CREATE (cod)-[:REQUIRES {strength: 0.90}]->(dsm);

-- TCI relationships
CREATE (tci)-[:SUPPORTS {strength: 0.89}]->(ras);
CREATE (tci)-[:ENABLES {strength: 0.87}]->(mae);

-- RAS relationships
CREATE (ras)-[:SUPPORTS {strength: 0.92}]->(rke);
CREATE (ras)-[:ENABLES {strength: 0.89}]->(cod);

-- QAM relationships
CREATE (qam)-[:SHAPES {strength: 0.86}]->(rke);
CREATE (qam)-[:SUPPORTS {strength: 0.85}]->(csf);

-- ============================================================================
-- 10. CREATE INTERACTION DYNAMICS RELATIONSHIPS
-- ============================================================================

-- PLP relationships
CREATE (plp)-[:DEPENDS_ON {strength: 0.87}]->(sle);
CREATE (plp)-[:ENABLES {strength: 0.84}]->(cie);
CREATE (plp)-[:SUPPORTS {strength: 0.82}]->(tct);

-- TCT relationships
CREATE (tct)-[:REQUIRES {strength: 0.88}]->(csf);
CREATE (tct)-[:ENABLES {strength: 0.85}]->(ccr);

-- CSF relationships
CREATE (csf)-[:SUPPORTS {strength: 0.91}]->(hrm);
CREATE (csf)-[:ENABLES {strength: 0.88}]->(mca);

-- CDQ relationships
CREATE (cdq)-[:IMPLEMENTS {strength: 0.89}]->(tct);
CREATE (cdq)-[:SHAPES {strength: 0.87}]->(rke);

-- ============================================================================
-- 11. CREATE ORGANIZATIONAL RELATIONSHIPS
-- ============================================================================

-- AIF relationships
CREATE (aif)-[:CHALLENGES {strength: 0.75}]->(mca);
CREATE (aif)-[:ENABLES {strength: 0.82}]->(ars);

-- ARS relationships
CREATE (ars)-[:COMPLICATES {strength: 0.78}]->(air);
CREATE (ars)-[:IMPAIRS {strength: 0.76}]->(pdt);

-- ============================================================================
-- 12. CREATE CROSS-DOMAIN RELATIONSHIPS
-- ============================================================================

-- Connect linguistic to knowledge synthesis
CREATE (sle)-[:ENABLES {strength: 0.86}]->(rke);
CREATE (ape)-[:SUPPORTS {strength: 0.83}]->(qam);

-- Connect meta-cognitive to interaction
CREATE (ccr)-[:SUPPORTS {strength: 0.89}]->(tct);
CREATE (mca)-[:ENABLES {strength: 0.87}]->(csf);

-- Connect knowledge synthesis to interaction
CREATE (cod)-[:SUPPORTS {strength: 0.88}]->(csf);
CREATE (ras)-[:ENABLES {strength: 0.85}]->(cdq);

-- ============================================================================
-- 13. CREATE INDICES FOR QUERY OPTIMIZATION
-- ============================================================================

CREATE INDEX ON :Concept(domain);
CREATE INDEX ON :Concept(concept_type);
CREATE INDEX ON :Concept(pagerank_score);

-- ============================================================================
-- 14. VERIFICATION QUERIES
-- ============================================================================

-- Verify all 25 concepts created
-- MATCH (c:Concept) RETURN COUNT(c) AS concept_count;

-- Verify all relationships created
-- MATCH ()-[r]->() RETURN COUNT(r) AS relationship_count;

-- Verify constraints
-- MATCH (c1:Concept {entity_id: 'rke'}), (c2:Concept {entity_id: 'ccr'})
-- WHERE (c1)-[:ENABLES|DEPENDS_ON|SUPPORTS]-(c2)
-- RETURN c1.label, c2.label;
