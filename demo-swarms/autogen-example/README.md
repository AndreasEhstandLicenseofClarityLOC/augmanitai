# AutoGen RoundRobinGroupChat AUGMANITAI Example

A Microsoft AutoGen example demonstrating collaborative terminology research using RoundRobinGroupChat.

## Architecture

Three agents collaborate in a round-robin discussion to answer research questions:

1. **Query Analyzer** — Breaks down questions into key concepts and identifies relevant domains
2. **Terminology Expert** — Searches and retrieves AUGMANITAI definitions and examples
3. **Synthesis Officer** — Integrates findings into coherent, structured responses

## Communication Pattern

The `RoundRobinGroupChat` cycles through agents in sequence:
- Agent 1 responds to the initial message
- Agent 2 responds to Agent 1
- Agent 3 responds to Agent 2
- Cycle repeats up to max_turns (continues until conversation terminates)

Each agent sees the full conversation history and can reference previous contributions.

## Files

- `agents.py` — AssistantAgent definitions with system prompts
- `tools.py` — AUGMANITAI lookup tools for agents
- `mock_client.py` — Mock ChatCompletionClient for offline execution
- `groupchat_example.py` — RoundRobinGroupChat orchestration
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

To extend this example:

- Replace `MockChatCompletionClient` with real client (e.g., Azure OpenAI, Claude)
- Add function calling so agents can invoke AUGMANITAI tool methods directly
- Implement custom termination conditions (e.g., consensus reached, max turns)
- Add agent reflection: agents review peer responses and refine understanding
- Create specialized group chats for different task types
- Integrate human-in-the-loop review between agent turns

## Key Learning Points

- **Round-robin conversation**: How agents with distinct expertise can collaborate iteratively
- **Group chat state management**: Conversation history tracking and context propagation
- **System prompts for specialization**: Role-specific instructions guide agent behavior
- **Async/await patterns**: AutoGen's async architecture for scalable multi-agent workflows
- **Mock clients for development**: Testing group chat logic without API costs or latency


---

*Bound by the **Ethical Disclaimer §1–§20** ([`DISCLAIMER.md`](../../DISCLAIMER.md)) and the repository licenses ([`LICENSE`](../../LICENSE)). Contact and provider: [`IMPRESSUM.md`](../../IMPRESSUM.md).*
