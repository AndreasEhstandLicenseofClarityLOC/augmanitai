"""
LangGraph StateGraph example for AUGMANITAI term lookup.

Demonstrates a simple 3-node workflow:
1. query_parser: Extract relevant term names from user question
2. term_retriever: Look up definitions in AUGMANITAI
3. response_composer: Format a structured response
"""

from langgraph.graph import StateGraph, END
from .state import AugmanitaiState
from .nodes import query_parser, term_retriever, response_composer


def build_graph():
    """Construct the StateGraph."""
    graph = StateGraph(AugmanitaiState)

    # Add nodes
    graph.add_node("query_parser", query_parser)
    graph.add_node("term_retriever", term_retriever)
    graph.add_node("response_composer", response_composer)

    # Define edges
    graph.add_edge("query_parser", "term_retriever")
    graph.add_edge("term_retriever", "response_composer")
    graph.add_edge("response_composer", END)

    # Set entry point
    graph.set_entry_point("query_parser")

    return graph.compile()


def run_example(query: str) -> str:
    """
    Run the workflow on a query.

    Args:
        query: User's research question

    Returns:
        Final formatted response with AUGMANITAI terminology
    """
    graph = build_graph()

    initial_state: AugmanitaiState = {
        "query": query,
        "query_terms": [],
        "retrieved_terms": [],
        "response": "",
    }

    final_state = graph.invoke(initial_state)
    return final_state["response"]


if __name__ == "__main__":
    # Example usage
    question = (
        "How do AI systems influence human language adoption and terminology usage?"
    )
    result = run_example(question)
    print(result)
