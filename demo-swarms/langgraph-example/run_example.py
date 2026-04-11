"""CLI runner for LangGraph AUGMANITAI example."""

from stategraph_example import run_example


if __name__ == "__main__":
    # Example research questions
    queries = [
        "How do AI systems influence human language adoption and terminology usage?",
        "What is Compound Cognition and how does it relate to AI interaction?",
        "Explain the concept of Semantic System Programming.",
    ]

    for i, query in enumerate(queries, 1):
        print(f"\n{'=' * 70}")
        print(f"Query {i}:")
        print(f"{'=' * 70}")
        print(f"{query}\n")

        result = run_example(query)
        print(result)
