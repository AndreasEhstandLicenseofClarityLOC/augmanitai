"""CLI runner for AutoGen AUGMANITAI example."""

from groupchat_example import run_example_sync


if __name__ == "__main__":
    # Example research questions
    queries = [
        "How do AI systems influence human terminology adoption?",
        "Explain the mechanisms of Semantic System Programming.",
        "What are the long-term cognitive effects of AI-induced language patterns?",
    ]

    for i, query in enumerate(queries, 1):
        print(f"\n{'=' * 70}")
        print(f"Question {i}: {query}")
        print(f"{'=' * 70}\n")

        response = run_example_sync(query)
        print(response)
        print("\n")
