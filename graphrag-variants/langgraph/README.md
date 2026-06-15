# LangGraph: AUGMANITAI Workflow Graphs

This directory contains a complete LangGraph implementation for AUGMANITAI, enabling multi-agent reasoning workflows with state persistence, checkpointing, and complex graph orchestration.

## Files

- **state_schema.py**: Type definitions for all workflow states (Query, Reasoning, Aggregation, Traversal, Validation, Analysis, Synthesis). Includes enums for concept types, relationship types, and domains. Provides factory methods and state transition rules.
- **graph_definition.py**: Core agents (QueryAgent, ReasoningAgent, AggregationAgent) and GraphDefinition class defining nodes, edges, and routing logic. Implements actual graph processing.
- **checkpoint_schema.json**: Schema for state persistence and recovery. Defines checkpoint structure for each state type, recovery procedures, validation rules, and monitoring metrics.
- **subgraph_compose.py**: Composition builder for creating complex workflows from subgraphs. Implements parallel, conditional, and loop compositions with orchestration logic.
- **README.md**: This documentation file.

## Architecture

### State Types

LangGraph uses 7 distinct state types for different workflow phases:

1. **QueryState**: Represents a graph query (entity, neighborhood, subgraph, path, domain)
2. **ReasoningState**: Represents reasoning about connections between concepts
3. **AggregationState**: Aggregates results from multiple agents
4. **GraphTraversalState**: Tracks traversal of subgraphs using BFS/DFS
5. **ValidationState**: Validates entities and relationships against schema
6. **AnalysisState**: Analyzes structural properties (centrality, distribution, metrics)
7. **SynthesisState**: Synthesizes insights across concepts

### Agents

Each agent implements specialized operations:

- **QueryAgent**: Executes queries (entity lookup, neighborhood, subgraph, path finding, domain filtering)
- **ReasoningAgent**: Reasons about concept relationships and generates findings
- **AggregationAgent**: Aggregates findings and synthesizes consensus answers

### Workflow Patterns

#### Simple Query
```
Query Node → Result
```

#### Entity Analysis
```
Query → Reasoning → Aggregation
```

#### Full Knowledge Synthesis
```
Query ─┐
       ├→ Reasoning ─┐
Traversal ─┤         ├→ Analysis → Synthesis → Aggregation
       └→ ────┘
```

## State Transitions

Valid state transitions follow a directed acyclic graph:

- `query` → `reasoning` or `error`
- `reasoning` → `aggregation` or `error`
- `aggregation` → `validation`, `analysis`, `synthesis`, or `complete`
- `traversal` → `analysis`, `synthesis`, or `complete`
- `validation` → `analysis` or `complete`
- `analysis` → `synthesis` or `complete`
- `synthesis` → `complete`

## Checkpoint Management

### Checkpoint Structure

Each state type has a checkpoint configuration:

```python
{
    "query_id": "q_001",
    "query_text": "Find concepts in knowledge_synthesis",
    "status": "completed",
    "results": [...],
    "visited_nodes": {...},
    "timestamp": "2026-04-10T10:30:00Z"
}
```

### Recovery Procedures

- **Query Recovery**: Resume from latest checkpoint with retry limit of 3
- **Reasoning Recovery**: Resume with visited nodes preserved, retry limit of 2
- **Aggregation Recovery**: Replay agent results, retry limit of 1

### Validation

Checkpoints validate:

- Schema compliance for state fields
- Data type correctness
- Field completeness for critical fields
- Timestamp validity
- State consistency (e.g., visited nodes are subset of all nodes)

## Compositions

### Standard Compositions

1. **simple_query**: Single-node query execution
2. **entity_analysis**: Query → Reason → Aggregate
3. **subgraph_discovery**: Traversal → Analysis → Synthesis
4. **graph_validation**: Validation → Analysis
5. **knowledge_synthesis**: Full multi-agent workflow

### Composition Types

#### Sequential Composition
Nodes execute in topologically sorted order:
```python
comp = SubgraphComposition(
    nodes=["query", "reasoning", "aggregation"],
    edges=[("query", "reasoning"), ("reasoning", "aggregation")]
)
```

#### Parallel Composition
Multiple subgraphs execute in parallel:
```python
ParallelComposition(
    name="parallel_analysis",
    subgraphs=["entity_analysis", "subgraph_discovery"]
)
```

#### Conditional Composition
Execution path depends on condition:
```python
ConditionalComposition(
    condition_fn=lambda s: s.confidence_score > 0.7,
    true_path=["synthesis"],
    false_path=["reasoning"]
)
```

#### Loop Composition
Iterative execution with termination condition:
```python
LoopComposition(
    body_nodes=["traversal"],
    condition_fn=lambda s: len(s.visited_nodes) < 20,
    max_iterations=5
)
```

## Usage Examples

### Define a Query State

```python
from state_schema import StateConfig

query_state = StateConfig.create_query_state(
    query_id="q_001",
    query_text="Find connections from RKE",
    query_type="neighborhood",
    start_node="rke"
)
```

### Build Graph Definition

```python
from graph_definition import GraphDefinition

graph = GraphDefinition(data_dir=".")
nodes = graph.get_node_definitions()
edges = graph.get_edge_definitions()

# Execute query
result_state = nodes["query"](query_state)
print(f"Query status: {result_state.status}")
print(f"Results: {result_state.results}")
```

### Create Orchestrator

```python
from subgraph_compose import create_standard_orchestrator

orchestrator = create_standard_orchestrator()

# Get execution plan
plan = orchestrator.get_execution_plan("knowledge_synthesis")
print(f"Execution order: {plan['execution_order']}")

# Export compositions
orchestrator.export_all_compositions(".")
```

### Register Custom Composition

```python
def should_continue(state):
    return len(state.visited_nodes) < 20

orchestrator.register_loop_composition(
    name="iterative_discovery",
    body_nodes=["traversal", "analysis"],
    condition_fn=should_continue,
    max_iterations=10
)
```

## Graph Characteristics

- **Nodes per graph**: 25 AUGMANITAI concepts
- **Relationships per graph**: 51 semantic dependencies
- **State types**: 7 distinct state classes
- **Standard compositions**: 5 pre-built workflows
- **Custom composition types**: 3 (parallel, conditional, loop)
- **Maximum workflow depth**: Typically 4-6 state transitions

## Performance Considerations

### State Transition Overhead
- Each state transition involves validation and serialization
- Checkpoint creation adds ~10-50ms per state
- Recovery from checkpoint ~5-20ms

### Parallelization
- Multiple agents can execute in parallel on independent queries
- No conflicts when agents operate on same graph (read-only)
- Aggregation phase must serialize for consensus

### Scalability
- Memory footprint scales with state history (checkpoint count)
- Graph operations are O(V+E) for vertices/edges visited
- Traversal algorithms (BFS/DFS) handle up to 5 hops efficiently

## Integration with LangChain/LangGraph

```python
from langchain.agents import AgentExecutor
from langgraph.graph import StateGraph

# Create state graph
sg = StateGraph(QueryState)

# Add nodes
sg.add_node("query", graph.nodes["query"])
sg.add_node("reasoning", graph.nodes["reasoning"])
sg.add_node("aggregation", graph.nodes["aggregation"])

# Add edges
sg.add_edge("query", "reasoning")
sg.add_edge("reasoning", "aggregation")
sg.set_entry_point("query")
sg.set_finish_point("aggregation")

# Compile and execute
runnable = sg.compile()
result = runnable.invoke({"query_text": "..."})
```

## Citation

This implementation uses the AUGMANITAI framework by Andreas Ehstand:
- ORCID: 0009-0006-3773-7796
- DOI: 10.5281/zenodo.20161494
- License: CC BY-NC-ND 4.0

## Implementation Notes

- States are immutable by design (dataclasses with frozen=True in production)
- Checkpoints include full state serialization for recovery
- Composition execution uses topological sorting for dependency ordering
- Agents implement the "node processor" pattern from LangGraph
- All state transitions validate against the transition DAG


---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](../../DISCLAIMER.md)) and the repository licenses ([`LICENSE`](../../LICENSE)). Contact and provider: [`IMPRESSUM.md`](../../IMPRESSUM.md).*
