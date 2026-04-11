"""CrewAI tools wrapping AUGMANITAI lookup for agents."""

from typing import List, Dict, Any, Optional
from augmanitai.core import AugmanitaiDB


class AugmanitaiTool:
    """Tool wrapper for AUGMANITAI term lookup."""

    def __init__(self):
        """Initialize with AUGMANITAI database."""
        self.db = AugmanitaiDB()

    def search_terms(
        self, query: str, domain: Optional[str] = None, limit: int = 5
    ) -> List[Dict[str, Any]]:
        """
        Search AUGMANITAI for terminology matching a query.

        Args:
            query: Search query string
            domain: Optional domain to filter by
            limit: Maximum number of results

        Returns:
            List of matching terms with their definitions
        """
        results = self.db.search(query, domain=domain, threshold=0.3, limit=limit)

        formatted = []
        for term, score in results:
            formatted.append(
                {
                    "name": term.name_en,
                    "abbreviation": term.abbreviation,
                    "definition": term.definition_en,
                    "domain": term.domain,
                    "examples": term.examples,
                    "relevance_score": round(score, 3),
                }
            )

        return formatted

    def get_related_terms(self, term_id: str) -> List[Dict[str, Any]]:
        """
        Get terms related to a given term.

        Args:
            term_id: The AUGMANITAI term ID

        Returns:
            List of related terms
        """
        related = self.db.get_related_terms(term_id)

        return [
            {
                "related_term": term.name_en,
                "relation_type": rel_type,
                "relation_description": description,
            }
            for term, rel_type, description in related
        ]

    def get_domain_terms(self, domain: str) -> List[Dict[str, str]]:
        """
        Get all terms in a specific domain.

        Args:
            domain: Domain name (e.g., 'cognitive_processes')

        Returns:
            List of terms in that domain
        """
        terms = self.db.get_domain(domain)
        return [
            {"name": t.name_en, "abbreviation": t.abbreviation, "id": t.id}
            for t in terms
        ]
