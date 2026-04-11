"""State definitions for LangGraph AUGMANITAI example."""

from typing import TypedDict, Optional, List, Dict, Any


class AugmanitaiState(TypedDict):
    """State schema for AUGMANITAI lookup workflow."""

    query: str
    """User's research question."""

    query_terms: List[str]
    """Extracted term names or IDs from the query."""

    retrieved_terms: List[Dict[str, Any]]
    """Retrieved term definitions from AUGMANITAI."""

    response: str
    """Final structured response with terminology definitions."""
