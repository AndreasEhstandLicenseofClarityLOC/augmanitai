#!/usr/bin/env python3
"""
AUGMANITAI MCP Server
Model Context Protocol implementation for AUGMANITAI term database
Author: Andreas Ehstand
License: CC BY-NC-ND 4.0
"""

import json
import os
from typing import Any, Callable
from mcp.server import Server
from mcp.types import Tool, TextContent, ToolCall, ToolResult

# Initialize MCP server
server = Server(name="augmanitai")

# Load terms database
TERMS_DB_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../augmanitai-python/augmanitai/data/terms.json"
)

def load_terms() -> dict:
    """Load AUGMANITAI terms from JSON database"""
    with open(TERMS_DB_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

TERMS = load_terms()
TERM_MAP = {term["id"]: term for term in TERMS["terms"]}
ABBREV_MAP = {term["abbreviation"]: term for term in TERMS["terms"]}

# Define MCP tools
@server.call_tool()
async def lookup_term(term_id: str) -> str:
    """
    Look up a specific AUGMANITAI term by ID or abbreviation

    Args:
        term_id: Term ID (e.g., 'sle-001') or abbreviation (e.g., 'SLE')

    Returns:
        JSON-formatted term definition with all metadata
    """
    # Try direct ID lookup
    if term_id in TERM_MAP:
        term = TERM_MAP[term_id]
        return json.dumps(term, ensure_ascii=False, indent=2)

    # Try abbreviation lookup
    if term_id.upper() in ABBREV_MAP:
        term = ABBREV_MAP[term_id.upper()]
        return json.dumps(term, ensure_ascii=False, indent=2)

    return json.dumps({"error": f"Term '{term_id}' not found"}, ensure_ascii=False)


@server.call_tool()
async def search_terms(query: str) -> str:
    """
    Search AUGMANITAI terms by name, definition, or domain

    Args:
        query: Search term (case-insensitive, full-text on name and definition)

    Returns:
        JSON array of matching terms
    """
    query_lower = query.lower()
    results = []

    for term in TERMS["terms"]:
        # Search in name (EN/DE), definition (EN/DE), abbreviation, domain
        if (query_lower in term.get("name_en", "").lower() or
            query_lower in term.get("name_de", "").lower() or
            query_lower in term.get("definition_en", "").lower() or
            query_lower in term.get("definition_de", "").lower() or
            query_lower in term.get("abbreviation", "").lower() or
            query_lower in term.get("domain", "").lower()):
            results.append(term)

    return json.dumps(results, ensure_ascii=False, indent=2)


@server.call_tool()
async def get_related(term_id: str) -> str:
    """
    Get related terms by domain and semantic similarity

    Args:
        term_id: Term ID or abbreviation (e.g., 'SLE')

    Returns:
        JSON object with primary term and related terms in same domain
    """
    # Resolve term
    term = None
    if term_id in TERM_MAP:
        term = TERM_MAP[term_id]
    elif term_id.upper() in ABBREV_MAP:
        term = ABBREV_MAP[term_id.upper()]

    if not term:
        return json.dumps({"error": f"Term '{term_id}' not found"}, ensure_ascii=False)

    # Find related terms in same domain
    domain = term.get("domain", "")
    related = [t for t in TERMS["terms"]
               if t.get("domain") == domain and t["id"] != term["id"]]

    result = {
        "primary": term,
        "domain": domain,
        "related_count": len(related),
        "related_terms": related
    }

    return json.dumps(result, ensure_ascii=False, indent=2)


@server.call_tool()
async def list_domains() -> str:
    """
    List all AUGMANITAI domains and term counts

    Returns:
        JSON object mapping domains to term lists
    """
    domains = {}

    for term in TERMS["terms"]:
        domain = term.get("domain", "unclassified")
        if domain not in domains:
            domains[domain] = []
        domains[domain].append({
            "id": term["id"],
            "abbreviation": term.get("abbreviation"),
            "name_en": term.get("name_en")
        })

    result = {
        "domains": domains,
        "total_domains": len(domains),
        "total_terms": len(TERMS["terms"])
    }

    return json.dumps(result, ensure_ascii=False, indent=2)


# Register tools with server
server.add_tool(
    Tool(
        name="lookup_term",
        description="Look up a specific AUGMANITAI term by ID or abbreviation",
        inputSchema={
            "type": "object",
            "properties": {
                "term_id": {
                    "type": "string",
                    "description": "Term ID (e.g., 'sle-001') or abbreviation (e.g., 'SLE')"
                }
            },
            "required": ["term_id"]
        }
    )
)

server.add_tool(
    Tool(
        name="search_terms",
        description="Search AUGMANITAI terms by name, definition, or domain",
        inputSchema={
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search term (case-insensitive, full-text)"
                }
            },
            "required": ["query"]
        }
    )
)

server.add_tool(
    Tool(
        name="get_related",
        description="Get related terms by domain and semantic similarity",
        inputSchema={
            "type": "object",
            "properties": {
                "term_id": {
                    "type": "string",
                    "description": "Term ID or abbreviation"
                }
            },
            "required": ["term_id"]
        }
    )
)

server.add_tool(
    Tool(
        name="list_domains",
        description="List all AUGMANITAI domains and term counts",
        inputSchema={
            "type": "object",
            "properties": {}
        }
    )
)


if __name__ == "__main__":
    import asyncio

    async def main():
        print("Starting AUGMANITAI MCP Server...")
        print(f"Loaded {len(TERMS['terms'])} terms from database")
        print(f"Available domains: {len(set(t.get('domain') for t in TERMS['terms']))}")

        # Run server
        async with server:
            print("Server running. Use MCP client to connect.")
            await asyncio.Event().wait()

    asyncio.run(main())
