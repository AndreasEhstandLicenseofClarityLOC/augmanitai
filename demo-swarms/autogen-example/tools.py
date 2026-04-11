"""Tools for AutoGen agents to access AUGMANITAI."""

from typing import List, Dict, Any
from augmanitai.core import AugmanitaiDB
from autogen_core.models import FunctionCall


class AugmanitaiToolset:
    """Collection of tools for AUGMANITAI access."""

    def __init__(self):
        """Initialize with AUGMANITAI database."""
        self.db = AugmanitaiDB()

    def search_terminology(self, query: str, limit: int = 3) -> Dict[str, Any]:
        """
        Search for AUGMANITAI terms matching a query.

        Args:
            query: Search query
            limit: Maximum number of results

        Returns:
            Dictionary with search results
        """
        results = self.db.search(query, threshold=0.3, limit=limit)

        terms = []
        for term, score in results:
            terms.append(
                {
                    "id": term.id,
                    "name": term.name_en,
                    "abbreviation": term.abbreviation,
                    "definition": term.definition_en,
                    "domain": term.domain,
                    "relevance": round(score, 2),
                }
            )

        return {
            "query": query,
            "results_count": len(terms),
            "terms": terms,
        }

    def get_term_details(self, term_id: str) -> Dict[str, Any]:
        """
        Get full details for a specific term.

        Args:
            term_id: AUGMANITAI term ID

        Returns:
            Complete term information
        """
        term = self.db.get_term(term_id)

        if not term:
            return {"error": f"Term {term_id} not found"}

        return {
            "id": term.id,
            "name_en": term.name_en,
            "name_de": term.name_de,
            "abbreviation": term.abbreviation,
            "definition_en": term.definition_en,
            "definition_de": term.definition_de,
            "domain": term.domain,
            "examples": term.examples,
        }

    def get_domain_overview(self, domain: str) -> Dict[str, Any]:
        """
        Get all terms in a domain with brief summaries.

        Args:
            domain: Domain name

        Returns:
            Overview of domain terms
        """
        terms = self.db.get_domain(domain)

        return {
            "domain": domain,
            "term_count": len(terms),
            "terms": [
                {
                    "id": t.id,
                    "name": t.name_en,
                    "abbreviation": t.abbreviation,
                }
                for t in terms[:5]  # Limit to 5 for brevity
            ],
        }

    def get_related_terminology(self, term_id: str) -> Dict[str, Any]:
        """
        Get terms related to a specific term.

        Args:
            term_id: AUGMANITAI term ID

        Returns:
            Related terms and their relationships
        """
        related = self.db.get_related_terms(term_id)

        return {
            "term_id": term_id,
            "related_terms": [
                {
                    "related_to": term.name_en,
                    "relationship": rel_type,
                    "description": description,
                }
                for term, rel_type, description in related
            ],
        }

    def get_all_domains(self) -> Dict[str, Any]:
        """
        Get list of all available domains.

        Returns:
            Dictionary with domain names and term counts
        """
        domains = {}
        for domain in self.db.domains:
            terms = self.db.get_domain(domain)
            domains[domain] = len(terms)

        return {
            "total_domains": len(domains),
            "domains": domains,
        }
