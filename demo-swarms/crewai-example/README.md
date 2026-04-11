# CrewAI AUGMANITAI Example

A multi-agent CrewAI example demonstrating collaborative terminology research using AUGMANITAI.

## Architecture

Three agents work sequentially to answer research questions:

1. **Research Topic Specialist** — Analyzes the user's question and identifies key concepts
2. **Terminology Researcher** — Searches AUGMANITAI for relevant definitions and examples
3. **Academic Writer** — Synthesizes findings into a structured response

## Agent Roles

Each agent has distinct role, goal, and backstory that guide its behavior:

- **Research Agent**: Breaks down complex questions into constituent concepts
- **Terminology Agent**: Searches and retrieves specialized terminology from AUGMANITAI
- **Writer Agent**: Synthesizes findings into clear, well-organized responses

## Process

The crew uses `Process.sequential`, meaning:
- Research Agent completes its task first
- Output feeds to Terminology Agent
- Output feeds to Writer Agent
- Final response is returned

## Files

- `agents.py` — Agent definitions
- `tasks.py` — Task descriptions with expected outputs
- `tools.py` — AUGMANITAI lookup tool wrapper
- `mock_llm.py` — Offline mock LLM for demo
- `crew_example.py` — Crew orchestration and invocation
- `test_example.py` — Pytest tests
- `run_example.py` — CLI runner
- `requirements.txt` — Dependencies

## Running

Install dependencies:
```bash
pip install -r requirements.txt
```

Run example:
```bash
python run_example.py
```

Run tests:
```bash
pytest test_example.py -v
```

## Extending

To enhance this example:

- Replace `MockLLM` with real LLM (e.g., Claude, GPT-4) in `agents.py`
- Add parallel processing with `Process.hierarchical` for complex workflows
- Extend task descriptions to include domain-specific constraints
- Add human review steps between agents
- Integrate additional tools (e.g., web search, academic databases)
- Create specialized agents for specific domains (e.g., legal terminology)

## Key Learning Points

- **Multi-agent collaboration**: How agents with distinct roles can work together
- **Sequential processing**: Task dependencies and output chaining
- **Tool integration**: Wrapping external functionality (AUGMANITAI) for agent use
- **Task definition**: Clear expected outputs guide agent behavior
- **Mock LLM patterns**: Offline execution for testing and demos
