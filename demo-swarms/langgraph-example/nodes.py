"""Node functions for LangGraph AUGMANITAI example."""

from typing import List, Dict, Any
from augmanitai.core import AugmanitaiDB
from .state import AugmanitaiState


class SimpleLLM:
    """Offline mock LLM for demonstration."""

    def __call__(self, prompt: str) -> str:
        """Return a canned response."""
        if "extract" in prompt.lower() or "term" in prompt.lower():
            return "SLE, RKE, Compound Cognition"
        return "No additional insights."


# Initialize database and LLM
db = AugmanitaiDB()
llm = SimpleLLM()


def query_parser(state: AugmanitaiState) -> AugmanitaiState:
    """
    Node 1: Parse the user query and extract term names.

    Uses the mock LLM to identify which AUGMANITAI terms are relevant to the
    user's question.
    """
    prompt = f"""
Given this research question, identify which terminology from a Human-AI
interaction database would be most relevant:

Question: {state['query']}

List term names separated by commas (e.g., "Term A, Term B, Term C").
    """.strip()

    response = llm(prompt)
    terms = [t.strip() for t in response.split(",")]

    return {
        **state,
        "query_terms": terms,
    }


def term_retriever(state: AugmanitaiState) -> AugmanitaiState:
    """
    Node 2: Retrieve term definitions from AUGMANITAI.

    For each extracted term, search the database and retrieve its full
    definition and examples.
    """
    retrieved = []

    for term_name in state["query_terms"]:
        # Search by name
        results = db.search(term_name, limit=1)
        if results:
            term, score = results[0]
            retrieved.append(
                {
                    "name": term.name_en,
                    "abbreviation": term.abbreviation,
                    "definition": term.definition_en,
                    "examples": term.examples,
                    "domain": term.domain,
                }
            )

    return {
        **state,
        "retrieved_terms": retrieved,
    }


def response_composer(state: AugmanitaiState) -> AugmanitaiState:
    """
    Node 3: Compose a structured response.

    Formats the retrieved terms into a clear, readable answer to the original
    research question.
    """
    if not state["retrieved_terms"]:
        response = (
            "No AUGMANITAI terms were found matching the query. "
            "The database may not contain terminology relevant to this topic."
        )
    else:
        lines = [f"Research Query: {state['query']}", "", "Relevant Terminology:"]
        for term in state["retrieved_terms"]:
            lines.append(f"\n{term['name']} ({term['abbreviation']})")
            lines.append(f"  Domain: {term['domain']}")
            lines.append(f"  Definition: {term['definition']}")
            if term["examples"]:
                lines.append(f"  Examples:")
                for ex in term["examples"][:2]:
                    lines.append(f"    - {ex}")

        response = "\n".join(lines)

    return {
        **state,
        "response": response,
    }
