"""
LangGraph Subgraph Composition for AUGMANITAI
Defines composite graphs and workflow orchestration patterns
"""

from typing import Dict, List, Any, Optional, Callable
from dataclasses import dataclass
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


@dataclass
class SubgraphComposition:
    """Represents a composition of multiple subgraphs"""
    name: str
    description: str
    nodes: List[str]
    edges: List[tuple]
    entry_point: str
    exit_points: List[str]
    state_type: str


class CompositionBuilder:
    """Builder for creating subgraph compositions"""

    def __init__(self):
        """Initialize composition builder"""
        self.compositions: Dict[str, SubgraphComposition] = {}

    def add_composition(
        self,
        name: str,
        description: str,
        nodes: List[str],
        edges: List[tuple],
        entry_point: str,
        exit_points: List[str],
        state_type: str,
    ) -> None:
        """Add a composition definition"""
        self.compositions[name] = SubgraphComposition(
            name=name,
            description=description,
            nodes=nodes,
            edges=edges,
            entry_point=entry_point,
            exit_points=exit_points,
            state_type=state_type,
        )

    def build_standard_compositions(self) -> None:
        """Build standard workflow compositions"""

        # Simple Query Composition
        self.add_composition(
            name="simple_query",
            description="Single-node query execution",
            nodes=["query"],
            edges=[],
            entry_point="query",
            exit_points=["query"],
            state_type="query",
        )

        # Entity Analysis Composition
        self.add_composition(
            name="entity_analysis",
            description="Query entity, reason about it, then aggregate",
            nodes=["query", "reasoning", "aggregation"],
            edges=[("query", "reasoning"), ("reasoning", "aggregation")],
            entry_point="query",
            exit_points=["aggregation"],
            state_type="query",
        )

        # Subgraph Discovery Composition
        self.add_composition(
            name="subgraph_discovery",
            description="Traverse subgraph, analyze structure, synthesize findings",
            nodes=["traversal", "analysis", "synthesis"],
            edges=[("traversal", "analysis"), ("analysis", "synthesis")],
            entry_point="traversal",
            exit_points=["synthesis"],
            state_type="traversal",
        )

        # Validation Composition
        self.add_composition(
            name="graph_validation",
            description="Validate entities and relationships",
            nodes=["validation", "analysis"],
            edges=[("validation", "analysis")],
            entry_point="validation",
            exit_points=["analysis"],
            state_type="validation",
        )

        # Full Knowledge Synthesis Composition
        self.add_composition(
            name="knowledge_synthesis",
            description="Complete workflow: query -> reason -> analyze -> synthesize",
            nodes=[
                "query",
                "reasoning",
                "traversal",
                "analysis",
                "synthesis",
                "aggregation",
            ],
            edges=[
                ("query", "reasoning"),
                ("query", "traversal"),
                ("reasoning", "analysis"),
                ("traversal", "analysis"),
                ("analysis", "synthesis"),
                ("synthesis", "aggregation"),
            ],
            entry_point="query",
            exit_points=["aggregation"],
            state_type="query",
        )

    def export_compositions(self, output_path: str) -> None:
        """Export all compositions to JSON"""
        compositions_data = {
            "compositions": [
                {
                    "name": comp.name,
                    "description": comp.description,
                    "nodes": comp.nodes,
                    "edges": [
                        {"from": e[0], "to": e[1]} for e in comp.edges
                    ],
                    "entry_point": comp.entry_point,
                    "exit_points": comp.exit_points,
                    "state_type": comp.state_type,
                }
                for comp in self.compositions.values()
            ]
        }

        with open(output_path, "w") as f:
            json.dump(compositions_data, f, indent=2)


class ParallelComposition:
    """Manages parallel execution of multiple subgraphs"""

    def __init__(self, name: str, subgraphs: List[str]):
        """Initialize parallel composition"""
        self.name = name
        self.subgraphs = subgraphs
        self.results: Dict[str, Any] = {}

    def execute(self, states: Dict[str, Any]) -> Dict[str, Any]:
        """Execute subgraphs in parallel and aggregate"""
        # In actual implementation, this would use concurrent execution
        results = {}
        for subgraph_name, state in states.items():
            # Simulate execution
            results[subgraph_name] = f"Executed {subgraph_name}"
        return results


class ConditionalComposition:
    """Manages conditional execution based on state"""

    def __init__(
        self,
        name: str,
        condition_fn: Callable[[Any], bool],
        true_path: List[str],
        false_path: List[str],
    ):
        """Initialize conditional composition"""
        self.name = name
        self.condition_fn = condition_fn
        self.true_path = true_path
        self.false_path = false_path

    def evaluate(self, state: Any) -> List[str]:
        """Evaluate condition and return execution path"""
        if self.condition_fn(state):
            return self.true_path
        return self.false_path


class LoopComposition:
    """Manages iterative execution of subgraphs"""

    def __init__(
        self,
        name: str,
        body_nodes: List[str],
        condition_fn: Callable[[Any], bool],
        max_iterations: int = 10,
    ):
        """Initialize loop composition"""
        self.name = name
        self.body_nodes = body_nodes
        self.condition_fn = condition_fn
        self.max_iterations = max_iterations
        self.iteration_count = 0

    def should_continue(self, state: Any) -> bool:
        """Check if loop should continue"""
        return (
            self.iteration_count < self.max_iterations
            and self.condition_fn(state)
        )

    def execute_iteration(self, state: Any) -> Any:
        """Execute one iteration of the loop"""
        self.iteration_count += 1
        return state


class CompositionOrchestrator:
    """Orchestrates execution of composite graphs"""

    def __init__(self):
        """Initialize orchestrator"""
        self.builder = CompositionBuilder()
        self.builder.build_standard_compositions()
        self.parallel_compositions: Dict[str, ParallelComposition] = {}
        self.conditional_compositions: Dict[str, ConditionalComposition] = {}
        self.loop_compositions: Dict[str, LoopComposition] = {}

    def register_parallel_composition(
        self,
        name: str,
        subgraphs: List[str],
    ) -> None:
        """Register a parallel composition"""
        self.parallel_compositions[name] = ParallelComposition(
            name, subgraphs
        )

    def register_conditional_composition(
        self,
        name: str,
        condition_fn: Callable[[Any], bool],
        true_path: List[str],
        false_path: List[str],
    ) -> None:
        """Register a conditional composition"""
        self.conditional_compositions[name] = ConditionalComposition(
            name, condition_fn, true_path, false_path
        )

    def register_loop_composition(
        self,
        name: str,
        body_nodes: List[str],
        condition_fn: Callable[[Any], bool],
        max_iterations: int = 10,
    ) -> None:
        """Register a loop composition"""
        self.loop_compositions[name] = LoopComposition(
            name, body_nodes, condition_fn, max_iterations
        )

    def get_execution_plan(self, composition_name: str) -> Dict[str, Any]:
        """Get execution plan for a composition"""
        if composition_name not in self.builder.compositions:
            return {"error": f"Unknown composition: {composition_name}"}

        comp = self.builder.compositions[composition_name]
        return {
            "name": comp.name,
            "description": comp.description,
            "execution_order": self._topological_sort(
                comp.nodes, comp.edges
            ),
            "entry_point": comp.entry_point,
            "exit_points": comp.exit_points,
            "node_count": len(comp.nodes),
            "edge_count": len(comp.edges),
        }

    def _topological_sort(
        self, nodes: List[str], edges: List[tuple]
    ) -> List[str]:
        """Topological sort of execution order"""
        from collections import defaultdict, deque

        in_degree = defaultdict(int)
        graph = defaultdict(list)

        for node in nodes:
            in_degree[node] = 0

        for src, dst in edges:
            graph[src].append(dst)
            in_degree[dst] += 1

        queue = deque([n for n in nodes if in_degree[n] == 0])
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in graph[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result if len(result) == len(nodes) else nodes

    def export_all_compositions(self, output_dir: str = ".") -> None:
        """Export all compositions"""
        output_path = Path(output_dir) / "compositions.json"
        self.builder.export_compositions(str(output_path))


# Create example compositions
def create_standard_orchestrator() -> CompositionOrchestrator:
    """Create orchestrator with standard compositions"""
    orchestrator = CompositionOrchestrator()

    # Register a parallel composition
    orchestrator.register_parallel_composition(
        "parallel_analysis",
        ["entity_analysis", "subgraph_discovery"],
    )

    # Register conditional composition
    def should_do_full_synthesis(state: Any) -> bool:
        return getattr(state, "confidence_score", 0) > 0.7

    orchestrator.register_conditional_composition(
        "confidence_based_routing",
        should_do_full_synthesis,
        true_path=["synthesis"],
        false_path=["reasoning"],
    )

    # Register loop composition
    def should_continue_traversal(state: Any) -> bool:
        visited = getattr(state, "visited_nodes", set())
        return len(visited) < 20

    orchestrator.register_loop_composition(
        "iterative_traversal",
        ["traversal"],
        should_continue_traversal,
        max_iterations=5,
    )

    return orchestrator


def main():
    """Main entry point"""
    orchestrator = create_standard_orchestrator()

    print("AUGMANITAI LangGraph Compositions")
    print("=" * 50)

    print("\nStandard Compositions:")
    for name in orchestrator.builder.compositions:
        plan = orchestrator.get_execution_plan(name)
        print(f"\n{name}:")
        print(f"  Description: {plan['description']}")
        print(f"  Nodes: {plan['node_count']}")
        print(f"  Execution order: {plan['execution_order']}")

    print("\n\nParallel Compositions:")
    for name, comp in orchestrator.parallel_compositions.items():
        print(f"\n{name}:")
        print(f"  Subgraphs: {comp.subgraphs}")

    print("\n\nConditional Compositions:")
    for name in orchestrator.conditional_compositions:
        print(f"\n{name}:")
        print(f"  Has true/false paths")

    print("\n\nLoop Compositions:")
    for name, comp in orchestrator.loop_compositions.items():
        print(f"\n{name}:")
        print(f"  Max iterations: {comp.max_iterations}")

    # Export
    orchestrator.export_all_compositions(".")
    print("\n\nCompositions exported to compositions.json")


if __name__ == "__main__":
    main()
