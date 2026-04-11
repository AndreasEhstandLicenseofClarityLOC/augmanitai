"""
LangGraph State Schema for AUGMANITAI
Defines the state types and transitions for multi-agent workflows
"""

from typing import List, Dict, Any, Optional, Set
from dataclasses import dataclass, field
from enum import Enum


class ConceptType(Enum):
    """Types of concepts in AUGMANITAI"""
    CORE_CONCEPT = "Core Concept"
    PHENOMENON = "Phenomenon"
    PRACTICE = "Practice"
    FRAMEWORK = "Framework"
    CAPABILITY = "Capability"
    PROCESS = "Process"
    CHALLENGE = "Challenge"
    MECHANISM = "Mechanism"
    METHODOLOGY = "Methodology"
    PATTERN = "Pattern"
    CONSTRAINT = "Constraint"


class RelationshipType(Enum):
    """Types of relationships in AUGMANITAI"""
    ENABLES = "ENABLES"
    DEPENDS_ON = "DEPENDS_ON"
    PRECEDES = "PRECEDES"
    GENERATES = "GENERATES"
    FACILITATES = "FACILITATES"
    ENHANCES = "ENHANCES"
    REQUIRES = "REQUIRES"
    SUPPORTS = "SUPPORTS"
    CONTRIBUTES_TO = "CONTRIBUTES_TO"
    CAUSES = "CAUSES"
    CRITICAL_FOR = "CRITICAL_FOR"
    AMPLIFIES = "AMPLIFIES"
    IMPLEMENTS = "IMPLEMENTS"
    OPTIMIZES = "OPTIMIZES"
    SHAPES = "SHAPES"
    INITIATES = "INITIATES"
    ESTABLISHES = "ESTABLISHES"
    MITIGATED_BY = "MITIGATED_BY"
    CHALLENGES = "CHALLENGES"
    CONSTRAINS = "CONSTRAINS"
    COMPLICATES = "COMPLICATES"
    PREDICTS = "PREDICTS"
    ACCELERATES = "ACCELERATES"
    GUIDES = "GUIDES"
    INFORMS = "INFORMS"
    STRUCTURES = "STRUCTURES"
    OPERATIONALIZES = "OPERATIONALIZES"
    ERODES = "ERODES"
    IMPAIRS = "IMPAIRS"
    DISRUPTS = "DISRUPTS"
    GROUNDS = "GROUNDS"
    LEADS_TO = "LEADS_TO"
    REFINES = "REFINES"


class Domain(Enum):
    """Domains in AUGMANITAI"""
    LINGUISTIC_DYNAMICS = "linguistic_dynamics"
    META_COGNITIVE = "meta_cognitive"
    KNOWLEDGE_SYNTHESIS = "knowledge_synthesis"
    INTERACTION_DYNAMICS = "interaction_dynamics"
    ORGANIZATIONAL = "organizational"


@dataclass
class Concept:
    """Represents a concept in the AUGMANITAI framework"""
    id: str
    label: str
    type: ConceptType
    domain: Domain
    degree: int
    definition: str
    abbreviation: str
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Relationship:
    """Represents a relationship between concepts"""
    source_id: str
    target_id: str
    relationship_type: RelationshipType
    strength: float
    description: Optional[str] = None
    properties: Dict[str, Any] = field(default_factory=dict)


@dataclass
class QueryState:
    """State for a query execution in the graph"""
    query_id: str
    query_text: str
    query_type: str  # entity, neighborhood, subgraph, path, domain
    start_node: Optional[str] = None
    end_node: Optional[str] = None
    max_depth: int = 2
    filters: Dict[str, Any] = field(default_factory=dict)
    results: List[Dict[str, Any]] = field(default_factory=list)
    visited_nodes: Set[str] = field(default_factory=set)
    status: str = "pending"  # pending, processing, completed, error
    error_message: Optional[str] = None


@dataclass
class ReasoningState:
    """State for reasoning and synthesis across the graph"""
    reasoning_id: str
    query: str
    current_node: str
    visited_nodes: Set[str] = field(default_factory=set)
    path: List[str] = field(default_factory=list)
    relationships_traversed: List[Relationship] = field(default_factory=list)
    findings: List[Dict[str, Any]] = field(default_factory=list)
    confidence_score: float = 0.0
    status: str = "pending"  # pending, reasoning, reasoning_complete, error


@dataclass
class AggregationState:
    """State for aggregating results from multiple agents"""
    aggregation_id: str
    query: str
    agent_results: List[Dict[str, Any]] = field(default_factory=list)
    aggregated_findings: List[Dict[str, Any]] = field(default_factory=list)
    consensus_score: float = 0.0
    contradictions: List[Dict[str, Any]] = field(default_factory=list)
    final_answer: Optional[str] = None
    status: str = "pending"  # pending, aggregating, complete


@dataclass
class GraphTraversalState:
    """State for graph traversal operations"""
    traversal_id: str
    start_node: str
    strategy: str  # bfs, dfs, weighted
    max_hops: int = 5
    current_frontier: Set[str] = field(default_factory=set)
    explored: Set[str] = field(default_factory=set)
    discovered_paths: List[List[str]] = field(default_factory=list)
    discovered_subgraphs: List[Dict[str, Any]] = field(default_factory=list)
    status: str = "pending"  # pending, traversing, complete


@dataclass
class ValidationState:
    """State for validating graph consistency and schema compliance"""
    validation_id: str
    entities_to_validate: List[Concept] = field(default_factory=list)
    relationships_to_validate: List[Relationship] = field(default_factory=list)
    validation_results: Dict[str, Any] = field(default_factory=dict)
    schema_violations: List[Dict[str, Any]] = field(default_factory=list)
    is_valid: bool = False
    status: str = "pending"  # pending, validating, complete


@dataclass
class AnalysisState:
    """State for analyzing structural properties of the graph"""
    analysis_id: str
    metrics_requested: List[str] = field(default_factory=list)
    graph_metrics: Dict[str, float] = field(default_factory=dict)
    node_centrality: Dict[str, float] = field(default_factory=dict)
    relationship_distribution: Dict[str, int] = field(default_factory=dict)
    domain_analysis: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    anomalies_detected: List[Dict[str, Any]] = field(default_factory=list)
    status: str = "pending"  # pending, analyzing, complete


@dataclass
class SynthesisState:
    """State for synthesizing insights across the graph"""
    synthesis_id: str
    focus_nodes: Set[str] = field(default_factory=set)
    related_concepts: List[Concept] = field(default_factory=list)
    connecting_relationships: List[Relationship] = field(default_factory=list)
    synthesis_findings: List[Dict[str, Any]] = field(default_factory=list)
    conceptual_frameworks: List[Dict[str, Any]] = field(default_factory=list)
    emergent_patterns: List[str] = field(default_factory=list)
    status: str = "pending"  # pending, synthesizing, complete


# Convenience type for any state
StateType = Union[
    QueryState,
    ReasoningState,
    AggregationState,
    GraphTraversalState,
    ValidationState,
    AnalysisState,
    SynthesisState,
]


from typing import Union


# State configuration for LangGraph
class StateConfig:
    """Configuration for state management in LangGraph"""

    @staticmethod
    def get_state_schema() -> Dict[str, type]:
        """Returns the state schema for all node types"""
        return {
            "query": QueryState,
            "reasoning": ReasoningState,
            "aggregation": AggregationState,
            "traversal": GraphTraversalState,
            "validation": ValidationState,
            "analysis": AnalysisState,
            "synthesis": SynthesisState,
        }

    @staticmethod
    def create_query_state(
        query_id: str,
        query_text: str,
        query_type: str,
        **kwargs
    ) -> QueryState:
        """Factory method for creating QueryState"""
        return QueryState(
            query_id=query_id,
            query_text=query_text,
            query_type=query_type,
            **kwargs
        )

    @staticmethod
    def create_reasoning_state(
        reasoning_id: str,
        query: str,
        current_node: str,
        **kwargs
    ) -> ReasoningState:
        """Factory method for creating ReasoningState"""
        return ReasoningState(
            reasoning_id=reasoning_id,
            query=query,
            current_node=current_node,
            **kwargs
        )

    @staticmethod
    def create_aggregation_state(
        aggregation_id: str,
        query: str,
        **kwargs
    ) -> AggregationState:
        """Factory method for creating AggregationState"""
        return AggregationState(
            aggregation_id=aggregation_id,
            query=query,
            **kwargs
        )

    @staticmethod
    def create_traversal_state(
        traversal_id: str,
        start_node: str,
        strategy: str = "bfs",
        **kwargs
    ) -> GraphTraversalState:
        """Factory method for creating GraphTraversalState"""
        return GraphTraversalState(
            traversal_id=traversal_id,
            start_node=start_node,
            strategy=strategy,
            **kwargs
        )


# Example state transitions
class StateTransitions:
    """Defines valid state transitions for the workflow"""

    TRANSITIONS = {
        "query": ["reasoning", "error"],
        "reasoning": ["aggregation", "error"],
        "aggregation": ["validation", "analysis", "synthesis", "complete"],
        "traversal": ["analysis", "synthesis", "complete"],
        "validation": ["analysis", "complete"],
        "analysis": ["synthesis", "complete"],
        "synthesis": ["complete"],
    }

    @staticmethod
    def is_valid_transition(from_state: str, to_state: str) -> bool:
        """Check if a state transition is valid"""
        if from_state not in StateTransitions.TRANSITIONS:
            return False
        return to_state in StateTransitions.TRANSITIONS[from_state]
