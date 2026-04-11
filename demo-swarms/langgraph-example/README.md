# LangGraph AUGMANITAI Example

A simple 3-node LangGraph StateGraph that demonstrates AUGMANITAI term lookup in a structured workflow.

## Architecture

The workflow follows a linear pipeline pattern:

1. **query_parser** — Extracts relevant AUGMANITAI term names from the user's question using a mock LLM
2. **term_retriever** — Searches the AUGMANITAI database for full definitions, examples, and domain classification
3. **response_composer** — Formats the results into a structured, readable response

## State Schema

The `AugmanitaiState` TypedDict tracks:

- `query`: User's research question
- `query_terms`: Extracted term names (output of parser)
- `retrieved_terms`: Full term records from the database (output of retriever)
- `response`: Final formatted response (output of composer)

## Files

- `state.py` — State TypedDict definition
- `nodes.py` — Node function implementations and mock LLM
- `stategraph_example.py` — Graph construction and invocation
- `test_example.py` — Pytest tests
- `run_example.py` — CLI runner for manual testing
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

To extend this example:

- Replace the `SimpleLLM` class in `nodes.py` with a real LLM (e.g., Anthropic's Claude)
- Add conditional branching in the graph (e.g., add nodes to handle ambiguous queries)
- Enhance the response composer to format results as JSON, markdown tables, or other formats
- Add error handling nodes for queries that return no results

## Key Learning Points

- **StateGraph structure**: How to define a typed state and linear workflow
- **Offline integration**: Mock LLM for demonstration without API keys
- **Multi-step reasoning**: Separating parsing, retrieval, and formatting concerns
- **AUGMANITAI API**: Using `AugmanitaiDB.search()` for terminology lookup
