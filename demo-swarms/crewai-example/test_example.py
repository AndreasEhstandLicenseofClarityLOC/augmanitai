"""Pytest tests for CrewAI AUGMANITAI example."""

import pytest
from .crew_example import run_augmanitai_crew


def test_crew_returns_non_empty_response():
    """Test that the crew returns a response."""
    question = "What is terminology adoption in human-AI interaction?"
    result = run_augmanitai_crew(question)

    assert isinstance(result, str)
    assert len(result) > 0


def test_crew_mentions_augmanitai_concepts():
    """Test that the crew's response includes AUGMANITAI terminology."""
    question = "Explain how AI influences language patterns."
    result = run_augmanitai_crew(question)

    # Should mention cognitive or linguistic concepts
    result_lower = result.lower()
    assert (
        "term" in result_lower
        or "definition" in result_lower
        or "concept" in result_lower
    )


def test_crew_addresses_user_question():
    """Test that the response addresses the user's original question."""
    question = "How do recursive knowledge cycles work?"
    result = run_augmanitai_crew(question)

    # Response should be substantial
    assert len(result) > 50
    # Should have some structure (multiple sentences or lines)
    assert "\n" in result or "." in result


def test_crew_with_different_questions():
    """Test the crew with multiple different questions."""
    questions = [
        "What is Semantic System Programming?",
        "How does cognitive offloading affect learning?",
        "Explain Terminological Colonization.",
    ]

    for question in questions:
        result = run_augmanitai_crew(question)
        assert isinstance(result, str)
        assert len(result) > 10
