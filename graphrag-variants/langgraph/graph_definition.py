"""
LangGraph Graph Definition for AUGMANITAI
Defines the multi-agent workflow graph with nodes, edges, and conditional routing
"""

from typing import Dict, Any, List, Optional
import json
from pathlib import Path

from state_schema import (
    QueryState,
    ReasoningState,
    AggregationState,
    GraphTraversalState,
    ValidationState,
    AnalysisState,
    SynthesisState,
    StateTransitions,
)


class AUGMANITAIGraphAgent:
    """Base agent for AUGMANITAI graph operations"""

    def __init__(self, data_dir: str = "."):
        """Initialize agent with property graph data"""
        self.data_dir = Path(data_dir)
        self.property_graph = self._load_property_graph()
        self.schema = self._load_schema()

    def _load_property_graph(self) -> Dict[str, Any]:
        """Load property graph"""
        graph_path = self.data_dir / "property_graph.json"
        if not graph_path.exists():
            return {"nodes": [], "relationships": []}
        with open(graph_path) as f:
            return json.load(f)

    def _load_schema(self) -> Dict[str, Any]:
        """Load schema"""
        schema_path = self.data_dir / "schema.json"
        if not schema_path.exists():
            return {"schema": {}}
        with open(schema_path) as f:
            return json.load(f)


class QueryAgent(AUGMANITAIGraphAgent):
    """Agent for executing queries on the graph"""

    def execute_query(self, state: QueryState) -> QueryState:
        """Execute a query and populate results"""
        state.status = "processing"

        try:
            if state.query_type == "entity":
                self._query_entity(state)
            elif state.query_type == "neighborhood":
                self._query_neighborhood(state)
            elif state.query_type == "subgraph":
                self._query_subgraph(state)
            elif state.query_type == "path":
                self._query_path(state)
            elif state.query_type == "domain":
                self._query_domain(state)
            else:
                state.error_message = f"Unknown query type: {state.query_type}"
                state.status = "error"
                return state

            state.status = "completed"
        except Exception as e:
            state.status = "error"
            state.error_message = str(e)

        return state

    def _query_entity(self, state: QueryState) -> None:
        """Query a single entity"""
        if not state.start_node:
            state.error_message = "Entity query requires start_node"
            return

        for node in self.property_graph.get("nodes", []):
            if node["id"] == state.start_node:
                state.results.append({
                    "node": node,
                    "incoming": self._get_incoming_relationships(state.start_node),
                    "outgoing": self._get_outgoing_relationships(state.start_node),
                })
                state.visited_nodes.add(state.start_node)
                return

        state.error_message = f"Node {state.start_node} not found"

    def _query_neighborhood(self, state: QueryState) -> None:
        """Query neighborhood of a node"""
        if not state.start_node:
            state.error_message = "Neighborhood query requires start_node"
            return

        neighbors = {
            "center": state.start_node,
            "outgoing": self._get_outgoing_relationships(state.start_node),
            "incoming": self._get_incoming_relationships(state.start_node),
        }

        state.results.append(neighbors)
        state.visited_nodes.add(state.start_node)

    def _query_subgraph(self, state: QueryState) -> None:
        """Query subgraph via BFS"""
        if not state.start_node:
            state.error_message = "Subgraph query requires start_node"
            return

        visited = {state.start_node}
        queue = [(state.start_node, 0)]
        nodes = {}
        edges = []

        while queue:
            current, depth = queue.pop(0)

            if depth >= state.max_depth:
                continue

            # Find node details
            for node in self.property_graph.get("nodes", []):
                if node["id"] == current and current not in nodes:
                    nodes[current] = node

            # Find relationships
            for rel in self.property_graph.get("relationships", []):
                if rel["source_id"] == current:
                    edges.append(rel)
                    if rel["target_id"] not in visited:
                        visited.add(rel["target_id"])
                        queue.append((rel["target_id"], depth + 1))

                elif rel["target_id"] == current:
                    edges.append(rel)
                    if rel["source_id"] not in visited:
                        visited.add(rel["source_id"])
                        queue.append((rel["source_id"], depth + 1))

        state.results.append({
            "start": state.start_node,
            "depth": state.max_depth,
            "nodes": nodes,
            "edges": edges,
        })
        state.visited_nodes = visited

    def _query_path(self, state: QueryState) -> None:
        """Find path between two nodes"""
        if not state.start_node or not state.end_node:
            state.error_message = "Path query requires start_node and end_node"
            return

        from collections import deque

        visited = {state.start_node}
        queue = deque([(state.start_node, [state.start_node])])
        found_paths = []

        while queue:
            current, path = queue.popleft()

            if current == state.end_node:
                found_paths.append(path)
                continue

            if len(path) > state.max_depth + 1:
                continue

            for rel in self.property_graph.get("relationships", []):
                next_node = None
                if rel["source_id"] == current:
                    next_node = rel["target_id"]
                elif rel["target_id"] == current:
                    next_node = rel["source_id"]

                if next_node and next_node not in visited:
                    visited.add(next_node)
                    queue.append((next_node, path + [next_node]))

        state.results.append({
            "start": state.start_node,
            "end": state.end_node,
            "paths": found_paths,
        })
        state.visited_nodes = visited

    def _query_domain(self, state: QueryState) -> None:
        """Query entities in a domain"""
        domain = state.filters.get("domain")
        if not domain:
            state.error_message = "Domain query requires domain filter"
            return

        domain_entities = []
        for node in self.property_graph.get("nodes", []):
            if node.get("properties", {}).get("domain") == domain:
                domain_entities.append(node)
                state.visited_nodes.add(node["id"])

        state.results.append({
            "domain": domain,
            "entities": domain_entities,
        })

    def _get_outgoing_relationships(self, node_id: str) -> List[Dict]:
        """Get outgoing relationships from a node"""
        rels = []
        for rel in self.property_graph.get("relationships", []):
            if rel["source_id"] == node_id:
                rels.append(rel)
        return rels

    def _get_incoming_relationships(self, node_id: str) -> List[Dict]:
        """Get incoming relationships to a node"""
        rels = []
        for rel in self.property_graph.get("relationships", []):
            if rel["target_id"] == node_id:
                rels.append(rel)
        return rels


class ReasoningAgent(AUGMANITAIGraphAgent):
    """Agent for reasoning about graph connections"""

    def reason_about_concepts(self, state: ReasoningState) -> ReasoningState:
        """Reason about relationships between concepts"""
        state.status = "reasoning"

        try:
            # Find direct relationships
            for rel in self.property_graph.get("relationships", []):
                if rel["source_id"] == state.current_node or rel["target_id"] == state.current_node:
                    state.relationships_traversed.append(rel)

            # Generate findings
            state.findings.append({
                "node": state.current_node,
                "connected_count": len(state.relationships_traversed),
                "strongest_relationships": sorted(
                    state.relationships_traversed,
                    key=lambda x: x["properties"].get("strength", 0),
                    reverse=True
                )[:3],
            })

            state.confidence_score = min(
                1.0,
                len(state.relationships_traversed) / 10.0
            )
            state.status = "reasoning_complete"

        except Exception as e:
            state.status = "error"
            state.error_message = str(e)

        return state


class AggregationAgent(AUGMANITAIGraphAgent):
    """Agent for aggregating results from multiple sources"""

    def aggregate_results(self, state: AggregationState) -> AggregationState:
        """Aggregate and synthesize findings"""
        state.status = "aggregating"

        try:
            # Aggregate findings
            for agent_result in state.agent_results:
                if "findings" in agent_result:
                    state.aggregated_findings.extend(agent_result["findings"])

            # Calculate consensus
            state.consensus_score = sum(
                r.get("confidence_score", 0.5) for r in state.agent_results
            ) / max(1, len(state.agent_results))

            state.final_answer = self._synthesize_findings(
                state.aggregated_findings
            )
            state.status = "complete"

        except Exception as e:
            state.status = "error"
            state.error_message = str(e)

        return state

    def _synthesize_findings(self, findings: List[Dict[str, Any]]) -> str:
        """Synthesize findings into a cohesive answer"""
        if not findings:
            return "No findings to synthesize"

        summary_parts = []
        for finding in findings[:3]:  # Limit to top 3
            if "node" in finding:
                summary_parts.append(
                    f"Concept {finding['node']}: {finding.get('connected_count', 0)} connections"
                )

        return "; ".join(summary_parts) if summary_parts else "Analysis complete"


class GraphDefinition:
    """Defines the LangGraph workflow for AUGMANITAI"""

    def __init__(self, data_dir: str = "."):
        """Initialize graph definition"""
        self.query_agent = QueryAgent(data_dir)
        self.reasoning_agent = ReasoningAgent(data_dir)
        self.aggregation_agent = AggregationAgent(data_dir)

    def get_node_definitions(self) -> Dict[str, callable]:
        """Returns node processing functions"""
        return {
            "query": self._node_query,
            "reasoning": self._node_reasoning,
            "aggregation": self._node_aggregation,
            "traversal": self._node_traversal,
            "analysis": self._node_analysis,
            "synthesis": self._node_synthesis,
            "validation": self._node_validation,
        }

    def get_edge_definitions(self) -> Dict[str, callable]:
        """Returns edge routing functions"""
        return {
            "query_to_next": self._edge_query_to_next,
            "reasoning_to_aggregation": self._edge_reasoning_to_aggregation,
            "aggregation_to_final": self._edge_aggregation_to_final,
        }

    def _node_query(self, state: QueryState) -> QueryState:
        """Query node processor"""
        return self.query_agent.execute_query(state)

    def _node_reasoning(self, state: ReasoningState) -> ReasoningState:
        """Reasoning node processor"""
        return self.reasoning_agent.reason_about_concepts(state)

    def _node_aggregation(self, state: AggregationState) -> AggregationState:
        """Aggregation node processor"""
        return self.aggregation_agent.aggregate_results(state)

    def _node_traversal(self, state: GraphTraversalState) -> GraphTraversalState:
        """Traversal node processor"""
        state.status = "traversing"
        # Traversal logic would go here
        state.status = "complete"
        return state

    def _node_analysis(self, state: AnalysisState) -> AnalysisState:
        """Analysis node processor"""
        state.status = "analyzing"
        # Analysis logic would go here
        state.status = "complete"
        return state

    def _node_synthesis(self, state: SynthesisState) -> SynthesisState:
        """Synthesis node processor"""
        state.status = "synthesizing"
        # Synthesis logic would go here
        state.status = "complete"
        return state

    def _node_validation(self, state: ValidationState) -> ValidationState:
        """Validation node processor"""
        state.status = "validating"
        state.is_valid = True  # Assume valid for now
        state.status = "complete"
        return state

    def _edge_query_to_next(self, state: QueryState) -> str:
        """Route from query node"""
        if state.status == "error":
            return "error"
        return "reasoning"

    def _edge_reasoning_to_aggregation(self, state: ReasoningState) -> str:
        """Route from reasoning node"""
        if state.status == "error":
            return "error"
        return "aggregation"

    def _edge_aggregation_to_final(self, state: AggregationState) -> str:
        """Route from aggregation node"""
        if state.status == "error":
            return "error"
        return "complete"
