# AUGMANITAI Demo Examples — Testing Guide

This document provides instructions for running and testing the three AUGMANITAI integration examples.

## Prerequisites

Ensure AUGMANITAI is installed and accessible:

```bash
# From the AUGMANITAI Python package directory
pip install -e ../augmanitai-python
```

## Directory Structure

```
demo-swarms/
├── README.md                    # Overview and comparison
├── TESTING_GUIDE.md             # This file
│
├── langgraph-example/           # LangGraph StateGraph example
│   ├── state.py
│   ├── nodes.py
│   ├── stategraph_example.py
│   ├── test_example.py
│   ├── run_example.py
│   └── requirements.txt
│
├── crewai-example/              # CrewAI multi-agent example
│   ├── agents.py
│   ├── tasks.py
│   ├── tools.py
│   ├── mock_llm.py
│   ├── crew_example.py
│   ├── test_example.py
│   ├── run_example.py
│   └── requirements.txt
│
└── autogen-example/             # AutoGen RoundRobinGroupChat example
    ├── agents.py
    ├── tools.py
    ├── mock_client.py
    ├── groupchat_example.py
    ├── test_example.py
    ├── run_example.py
    └── requirements.txt
```

## Running the Examples

### Option 1: Run all examples sequentially

```bash
#!/bin/bash

cd ./demo-swarms

echo "Testing LangGraph example..."
cd langgraph-example
pip install -r requirements.txt
python run_example.py
pytest test_example.py -v

echo ""
echo "Testing CrewAI example..."
cd ../crewai-example
pip install -r requirements.txt
python run_example.py
pytest test_example.py -v

echo ""
echo "Testing AutoGen example..."
cd ../autogen-example
pip install -r requirements.txt
python run_example.py
pytest test_example.py -v
```

### Option 2: Test individual examples

#### LangGraph Example

```bash
cd ./demo-swarms/langgraph-example

# Install dependencies
pip install -r requirements.txt

# Run the example
python run_example.py

# Run tests
pytest test_example.py -v

# Run specific test
pytest test_example.py::test_query_parser_extracts_terms -v
```

#### CrewAI Example

```bash
cd ./demo-swarms/crewai-example

# Install dependencies
pip install -r requirements.txt

# Run the example
python run_example.py

# Run tests
pytest test_example.py -v

# Run specific test
pytest test_example.py::test_crew_returns_non_empty_response -v
```

#### AutoGen Example

```bash
cd ./demo-swarms/autogen-example

# Install dependencies
pip install -r requirements.txt

# Run the example
python run_example.py

# Run tests (tests are async)
pytest test_example.py -v

# Run with coverage
pytest test_example.py -v --cov=. --cov-report=html
```

## Expected Test Output

All tests should pass with output similar to:

```
test_example.py::test_query_parser_extracts_terms PASSED
test_example.py::test_term_retriever_returns_definitions PASSED
test_example.py::test_response_formatter_includes_all_sections PASSED
test_example.py::test_end_to_end_workflow PASSED

========================= 4 passed in 0.42s ==========================
```

## Test Descriptions

### LangGraph Tests (4 tests)

1. **test_query_parser_extracts_terms** — Verifies query parser identifies terminology
2. **test_term_retriever_returns_definitions** — Confirms database lookups work
3. **test_response_formatter_includes_all_sections** — Checks response structure
4. **test_end_to_end_workflow** — Full workflow from query to response

### CrewAI Tests (4 tests)

1. **test_crew_returns_non_empty_response** — Crew produces output
2. **test_crew_mentions_augmanitai_concepts** — Terminology is referenced
3. **test_crew_addresses_user_question** — Response relevance check
4. **test_crew_with_different_questions** — Multiple question handling

### AutoGen Tests (5 tests)

1. **test_groupchat_returns_response** — Group chat produces output
2. **test_groupchat_addresses_question** — Response is relevant
3. **test_groupchat_multiple_agents_participate** — Agent collaboration
4. **test_groupchat_various_questions** — Multiple question types
5. **test_groupchat_structured_response** — Response has structure

## Debugging

### Enable verbose output

**LangGraph:**
```python
# In stategraph_example.py, set debug mode
graph = build_graph()
graph.invoke(state, debug=True)
```

**CrewAI:**
```python
# In crew_example.py, set verbose
crew = Crew(
    agents=[...],
    tasks=[...],
    verbose=True  # Set to True
)
```

**AutoGen:**
```python
# In groupchat_example.py, add logging
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Common Issues

**Import Error: `No module named 'augmanitai'`**

Solution: Install the AUGMANITAI package
```bash
cd ./augmanitai-python
pip install -e .
```

**Missing dependencies**

Solution: Install framework dependencies
```bash
pip install -r requirements.txt
```

**Async/await issues in AutoGen**

AutoGen examples use async/await. Ensure you're using Python 3.8+:
```bash
python --version  # Should be 3.8 or higher
```

## Integration Testing

To verify AUGMANITAI integration across all frameworks:

```bash
# Test that AUGMANITAI database loads correctly
python -c "from augmanitai.core import AugmanitaiDB; db = AugmanitaiDB(); print(f'Loaded {len(db)} terms')"

# Test that each example can import its modules
python -c "from langgraph_example.stategraph_example import build_graph; print('LangGraph OK')"
python -c "from crewai_example.crew_example import run_augmanitai_crew; print('CrewAI OK')"
python -c "from autogen_example.groupchat_example import run_example_sync; print('AutoGen OK')"
```

## Performance Benchmarking

Each example includes timing information:

```bash
# Time the LangGraph example
time python langgraph-example/run_example.py

# Time the CrewAI example
time python crewai-example/run_example.py

# Time the AutoGen example
time python autogen-example/run_example.py
```

Expected runtime:
- LangGraph: < 1 second (simplest, fewest operations)
- CrewAI: 2-5 seconds (multiple agent tasks)
- AutoGen: 3-8 seconds (async round-robin conversation)

## Extending Tests

To add new tests:

1. Add test function to `test_example.py`
2. Test name must start with `test_`
3. Use `pytest.raises()` for expected exceptions
4. Run with `pytest test_example.py -v`

Example:
```python
def test_domain_filtering():
    """Test that searches can filter by domain."""
    result = run_example("What is cognitive offloading?")
    assert "cognitive" in result.lower()
```

## CI/CD Integration

To run tests in GitHub Actions or similar CI:

```yaml
name: Test AUGMANITAI Examples

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.9
      
      - name: Install AUGMANITAI
        run: |
          cd augmanitai-python
          pip install -e .
      
      - name: Test LangGraph
        run: |
          cd demo-swarms/langgraph-example
          pip install -r requirements.txt
          pytest test_example.py -v
      
      - name: Test CrewAI
        run: |
          cd demo-swarms/crewai-example
          pip install -r requirements.txt
          pytest test_example.py -v
      
      - name: Test AutoGen
        run: |
          cd demo-swarms/autogen-example
          pip install -r requirements.txt
          pytest test_example.py -v
```

## References

- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [CrewAI Docs](https://docs.crewai.com/)
- [AutoGen Docs](https://microsoft.github.io/autogen/)
- [Pytest Docs](https://docs.pytest.org/)

---

Built for AUGMANITAI by Andreas Ehstand
