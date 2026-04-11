"""CLI runner for CrewAI AUGMANITAI example."""

from crew_example import run_augmanitai_crew


if __name__ == "__main__":
    # Example research questions
    queries = [
        "How do AI systems influence the way humans adopt and use new terminology?",
        "What mechanisms cause terminology to become dominant in a field?",
        "Explain the relationship between cognitive structures and linguistic patterns in human-AI interaction.",
    ]

    for i, query in enumerate(queries, 1):
        print(f"\n{'=' * 70}")
        print(f"Question {i}: {query}")
        print(f"{'=' * 70}\n")

        response = run_augmanitai_crew(query)
        print(response)
        print("\n")
