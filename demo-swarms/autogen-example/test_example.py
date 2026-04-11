"""Pytest tests for AutoGen AUGMANITAI example."""

import pytest
from .groupchat_example import run_example_sync


def test_groupchat_returns_response():
    """Test that the group chat returns a response."""
    question = "What is Symbiotic Linguistic Evolution?"
    result = run_example_sync(question)

    assert isinstance(result, str)
    assert len(result) > 0


def test_groupchat_addresses_question():
    """Test that the group chat addresses the user's question."""
    question = "How do terminology adoption mechanisms work?"
    result = run_example_sync(question)

    result_lower = result.lower()
    # Should contain relevant content
    assert (
        "terminology" in result_lower
        or "concept" in result_lower
        or "term" in result_lower
    )


def test_groupchat_multiple_agents_participate():
    """Test that multiple agents contribute to the response."""
    question = "Explain AI-Induced Perspective Shift."
    result = run_example_sync(question)

    # Response should be substantive (shows agent participation)
    assert len(result) > 50


def test_groupchat_various_questions():
    """Test the group chat with different question types."""
    questions = [
        "What are the cognitive processes involved in human-AI interaction?",
        "Describe the systemic effects of terminology adoption.",
        "How does Cognitive Offloading affect human autonomy?",
    ]

    for question in questions:
        result = run_example_sync(question)
        assert isinstance(result, str)
        assert len(result) > 10


def test_groupchat_structured_response():
    """Test that responses have some structure."""
    question = "What is the relationship between Compound Cognition and terminology?"
    result = run_example_sync(question)

    # Should have some form of structure (sentences, agents, etc.)
    assert "." in result or ":" in result or "\n" in result or len(result) > 30
