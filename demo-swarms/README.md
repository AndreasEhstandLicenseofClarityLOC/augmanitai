# AUGMANITAI Integration Examples for Python Agent Frameworks

This directory contains three complete, runnable examples demonstrating how to integrate the AUGMANITAI terminology database into popular Python multi-agent frameworks. All examples run entirely offline with no API calls required.

## Overview

| Example | Framework | Pattern | Key Feature | Lines of Code |
|---------|-----------|---------|-------------|---------------|
| [langgraph-example](./langgraph-example) | LangGraph >= 0.2 | StateGraph with 3 sequential nodes | Typed state, linear workflow | ~250 |
| [crewai-example](./crewai-example) | CrewAI >= 0.70 | Multi-agent crew with sequential tasks | Role-based agents, structured tasks | ~280 |
| [autogen-example](./autogen-example) | AutoGen >= 0.4 | RoundRobinGroupChat with 3 agents | Asynchronous group conversation | ~300 |

## Quick Start

Each example follows the same structure:

```bash
cd <example-directory>
pip install -r requirements.txt
python run_example.py
```

To run tests:

```bash
pytest test_example.py -v
```

## Common Pattern

All three examples solve the same problem: **collaborative terminology research and explanation**.

### User Input
```
"How do AI systems influence human language adoption and terminology usage?"
```

### Workflow

1. **Query Analysis** — Extract key concepts and research domains from the question
2. **Terminology Lookup** — Search AUGMANITAI database for relevant definitions
3. **Response Composition** — Format findings into a structured, readable answer

### Example Output

```
Research Query: How do AI systems influence human language adoption?

Relevant Terminology:

Symbiotic Linguistic Evolution (SLE)
  Domain: linguistic_dynamics
  Definition: The process by which human language and AI-generated language patterns 
  co-evolve through repeated interaction...
  
Compound Cognition (CC)
  Domain: cognitive_processes
  Definition: The cognitive state wherein an individual's thinking process 
  incorporates internalized AI-generated conceptual structures...
```

## Framework Comparison

### LangGraph Example

Best for: **Beginners learning agent workflows**

- Uses typed `StateGraph` for explicit state management
- Linear 3-node pipeline: query_parser → term_retriever → response_composer
- Simplest mental model, explicit data flow
- Good foundation before exploring more complex patterns

### CrewAI Example

Best for: **Complex multi-agent scenarios with specialized roles**

- Three agents with distinct roles, goals, and backstories
- Sequential task execution with output chaining
- Built-in abstractions for common patterns (roles, tasks, crews)
- Scales well to 5+ agents with different expertise areas

### AutoGen Example

Best for: **Research-grade multi-agent systems with rich interactions**

- Asynchronous round-robin group chat (agents can interrupt/respond to each other)
- Agents see full conversation history and build on prior contributions
- Most flexible interaction model, closest to human team dynamics
- Production-ready with enterprise features (logging, monitoring)

## AUGMANITAI Integration Points

Each example integrates the AUGMANITAI database via:

1. **Database Import** — `from augmanitai.core import AugmanitaiDB`
2. **Term Lookup** — `db.search(query)` and `db.get_term(term_id)`
3. **Structured Access** — Terms have `name`, `definition`, `domain`, `examples`
4. **Offline Operation** — All data embedded, no external requests

### Core AUGMANITAI API Used

- `AugmanitaiDB.search(query, domain=None, threshold=0.3, limit=None)` — Fuzzy search for terms
- `AugmanitaiDB.get_term(term_id)` — Retrieve specific term by ID
- `AugmanitaiDB.get_domain(domain)` — Get all terms in a domain
- `AugmanitaiDB.get_related_terms(term_id, direction="both")` — Find connected terms

## File Structure

```
demo-swarms/
├── README.md (this file)
│
├── langgraph-example/
│   ├── state.py                 # State TypedDict
│   ├── nodes.py                 # Node implementations
│   ├── stategraph_example.py    # Graph construction
│   ├── test_example.py          # Tests
│   ├── run_example.py           # CLI runner
│   ├── requirements.txt
│   └── README.md
│
├── crewai-example/
│   ├── tools.py                 # AUGMANITAI tool wrapper
│   ├── agents.py                # Agent definitions
│   ├── tasks.py                 # Task definitions
│   ├── mock_llm.py              # Offline LLM mock
│   ├── crew_example.py          # Crew orchestration
│   ├── test_example.py          # Tests
│   ├── run_example.py           # CLI runner
│   ├── requirements.txt
│   └── README.md
│
└── autogen-example/
    ├── agents.py                 # AssistantAgent definitions
    ├── tools.py                  # AUGMANITAI toolset
    ├── mock_client.py            # Mock ChatCompletionClient
    ├── groupchat_example.py      # RoundRobinGroupChat setup
    ├── test_example.py           # Tests
    ├── run_example.py            # CLI runner
    ├── requirements.txt
    └── README.md
```

## Extending the Examples

### Add a Real LLM

Replace the mock LLM with Claude, GPT-4, or another provider:

**LangGraph:**
```python
from anthropic import Anthropic

client = Anthropic()

def query_parser(state: AugmanitaiState) -> AugmanitaiState:
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=200,
        messages=[{"role": "user", "content": f"Extract terms from: {state['query']}"}]
    )
    # Parse response...
```

**CrewAI:**
```python
from crewai import Agent

agent = Agent(
    role="Terminology Researcher",
    goal="Find AUGMANITAI terms",
    model="gpt-4",  # or "claude-3-5-sonnet-20241022"
    tools=tools,
)
```

**AutoGen:**
```python
from autogen_core.models import ChatCompletionClient
from autogen_agentchat.agents import AssistantAgent

client = ChatCompletionClient(
    model_id="gpt-4",
    api_key="YOUR_API_KEY"
)
```

### Add Parallel Processing

**LangGraph:** Add parallel branches with `graph.add_edge(start, ["branch1", "branch2"])`

**CrewAI:** Switch to hierarchical process: `process=Process.hierarchical`

**AutoGen:** Use `SelectorGroupChat` for tournament-style agent competition

### Add Persistence

Save agent interactions to database:

```python
# Log all agent decisions
with open("augmanitai_interactions.jsonl", "w") as f:
    f.write(json.dumps({"query": q, "response": r}))
```

### Add Human Review

Insert human feedback loop between agent steps:

```python
# LangGraph: Add conditional edge with human input
graph.add_conditional_edges(
    "term_retriever",
    lambda x: "human_review" if x["retrieved_terms"] else "response_composer"
)
```

## Testing

All three examples include pytest tests that verify:
- Agents process queries without errors
- AUGMANITAI terms are retrieved correctly
- Responses contain expected structure (definitions, domains, examples)
- End-to-end workflow completes successfully

Run tests from each directory:

```bash
pytest test_example.py -v
```

## Learning Progression

**Recommended order for learning:**

1. Start with **LangGraph** — Understand basic agent workflow and state management
2. Move to **CrewAI** — Learn role-based agent specialization and task sequencing
3. Explore **AutoGen** — Understand asynchronous group dynamics and advanced patterns

## Citation

If you use these examples in research or publications, please cite AUGMANITAI:

```bibtex
@software{ehstand2025augmanitai,
  author = {Ehstand, Andreas},
  title = {AUGMANITAI: Academic Terminology Database for Human-AI Interaction},
  year = {2025},
  doi = {10.5281/zenodo.20161494},
  url = {https://zenodo.org/record/20161494}
}
```

AUGMANITAI is published under CC BY-NC-ND 4.0 license.

## References

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [AUGMANITAI Database](https://zenodo.org/record/20161494)

## Support

For questions about AUGMANITAI integration:
1. Check the framework-specific README in each example directory
2. Review the docstrings in `agents.py`, `nodes.py`, and `tools.py`
3. Run the examples with `--verbose` flags to see agent behavior
4. Modify the mock LLM responses to understand agent reasoning

---

Built with AUGMANITAI by Andreas Ehstand (ORCID 0009-0006-3773-7796)


---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](../DISCLAIMER.md)) and the repository licenses ([`LICENSE`](../LICENSE)). Contact and provider: [`IMPRESSUM.md`](../IMPRESSUM.md).*
