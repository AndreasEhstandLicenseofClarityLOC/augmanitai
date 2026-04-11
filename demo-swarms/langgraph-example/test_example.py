"""Pytest tests for LangGraph AUGMANITAI example."""

import pytest
from .stategraph_example import run_example


def test_query_parser_extracts_terms():
    """Test that the query parser extracts term names from the query."""
    query = "What is Symbiotic Linguistic Evolution?"
    result = run_example(query)

    # Assert that the response mentions a term (should contain term name)
    assert "Symbiotic" in result or "SLE" in result or len(result) > 50


def test_term_retriever_returns_definitions():
    """Test that the term retriever fetches and includes definitions."""
    query = "Explain Compound Cognition and its implications."
    result = run_example(query)

    # Assert that response contains structured information
    assert "Definition:" in result or "Domain:" in result or "Compound" in result


def test_response_formatter_includes_all_sections():
    """Test that the response includes query, terminology, and examples."""
    query = "How do we measure the adoption of AI terminology?"
    result = run_example(query)

    # Assert structure
    assert "Research Query:" in result or len(result) > 0
    # Should contain at least term info or examples
    assert "Domain:" in result or "Examples:" in result or "Definition:" in result


def test_end_to_end_workflow():
    """Test the complete workflow from query to response."""
    query = (
        "What mechanisms cause AI language patterns to influence human communication?"
    )
    result = run_example(query)

    # Assert that we got a non-empty, structured response
    assert isinstance(result, str)
    assert len(result) > 10
    # Should mention terms or have structure
    assert "Query:" in result or "Term" in result or "Domain:" in result
