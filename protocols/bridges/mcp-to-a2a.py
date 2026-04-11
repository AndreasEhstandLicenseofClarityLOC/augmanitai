#!/usr/bin/env python3
"""
MCP ↔ A2A Protocol Bridge
Translates MCP tool calls to A2A task messages and vice versa

Author: Andreas Ehstand
License: CC BY-NC-ND 4.0
"""

import json
import uuid
from datetime import datetime
from typing import Dict, Any, Optional
from dataclasses import dataclass, asdict


@dataclass
class MCPToolCall:
    """MCP tool invocation"""
    tool_name: str
    parameters: Dict[str, Any]


@dataclass
class A2ATaskRequest:
    """A2A task request message"""
    id: str
    timestamp: str
    source_agent_id: str
    target_agent_id: str
    action: str
    parameters: Dict[str, Any]
    context: Optional[Dict[str, Any]] = None


class MCPtoA2ABridge:
    """Bridge translating MCP ↔ A2A protocol"""

    # MCP tool → A2A action mapping
    MCP_TO_A2A_ACTION_MAP = {
        "lookup_term": "term_lookup",
        "search_terms": "term_search",
        "get_related": "term_relate",
        "list_domains": "list_domains",
    }

    # A2A action → MCP tool mapping
    A2A_TO_MCP_TOOL_MAP = {v: k for k, v in MCP_TO_A2A_ACTION_MAP.items()}

    # Parameter mapping: MCP → A2A
    MCP_PARAM_TO_A2A = {
        "lookup_term": {
            "term_id": "term_id",
        },
        "search_terms": {
            "query": "query",
            "limit": "limit",
        },
        "get_related": {
            "term_id": "term_id",
        },
        "list_domains": {},
    }

    # Parameter mapping: A2A → MCP
    A2A_PARAM_TO_MCP = {
        "term_lookup": {
            "term_id": "term_id",
        },
        "term_search": {
            "query": "query",
            "limit": "limit",
        },
        "term_relate": {
            "term_id": "term_id",
        },
        "list_domains": {},
    }

    def __init__(self, source_agent: str = "mcp-client", target_agent: str = "augmanitai"):
        """
        Initialize bridge

        Args:
            source_agent: ID of calling MCP agent
            target_agent: ID of target A2A agent (default: augmanitai)
        """
        self.source_agent = source_agent
        self.target_agent = target_agent

    def mcp_to_a2a(
        self,
        tool_call: MCPToolCall,
        language: str = "en",
        include_examples: bool = True
    ) -> Dict[str, Any]:
        """
        Convert MCP tool call to A2A task request

        Args:
            tool_call: MCP tool invocation
            language: Preferred response language (en/de)
            include_examples: Include usage examples in responses

        Returns:
            A2A TaskRequest as JSON-serializable dict
        """
        # Map MCP tool to A2A action
        action = self.MCP_TO_A2A_ACTION_MAP.get(tool_call.tool_name)
        if not action:
            raise ValueError(f"Unknown MCP tool: {tool_call.tool_name}")

        # Map parameters
        param_mapping = self.MCP_PARAM_TO_A2A.get(tool_call.tool_name, {})
        a2a_params = {}
        for mcp_key, a2a_key in param_mapping.items():
            if mcp_key in tool_call.parameters:
                a2a_params[a2a_key] = tool_call.parameters[mcp_key]

        # Create A2A task request
        request = {
            "@context": "https://google.github.io/A2A/v1/schema/task-request.jsonld",
            "type": "TaskRequest",
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "version": "1.0",
            "sourceAgent": {
                "agentId": self.source_agent,
                "name": "MCP Client"
            },
            "targetAgent": {
                "agentId": self.target_agent,
                "name": "AUGMANITAI"
            },
            "task": {
                "action": action,
                "parameters": a2a_params
            },
            "context": {
                "language": language,
                "includeExamples": include_examples
            }
        }

        return request

    def a2a_to_mcp(
        self,
        a2a_response: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Convert A2A task response to MCP tool result

        Args:
            a2a_response: A2A TaskResponse message

        Returns:
            MCP tool result as JSON-serializable dict
        """
        # Extract action from response
        action = a2a_response.get("result", {}).get("action")
        mcp_tool = self.A2A_TO_MCP_TOOL_MAP.get(action)

        if not mcp_tool:
            raise ValueError(f"Unknown A2A action: {action}")

        # Extract status and artifacts
        status = a2a_response.get("status", "unknown")

        if status == "success":
            # Extract artifact data
            artifacts = a2a_response.get("result", {}).get("artifacts", [])
            tool_result = {
                "success": True,
                "tool": mcp_tool,
                "status": status,
                "data": self._extract_artifact_data(artifacts)
            }
        elif status == "failed":
            # Handle error
            error = a2a_response.get("error", {})
            tool_result = {
                "success": False,
                "tool": mcp_tool,
                "status": status,
                "error": {
                    "code": error.get("code"),
                    "message": error.get("message")
                }
            }
        else:
            tool_result = {
                "success": False,
                "tool": mcp_tool,
                "status": status,
                "error": {"message": "Unknown response status"}
            }

        # Add metadata
        metadata = a2a_response.get("metadata", {})
        tool_result["metadata"] = {
            "processingTime": metadata.get("processingTime"),
            "resultCount": metadata.get("resultCount"),
            "language": metadata.get("language")
        }

        return tool_result

    def _extract_artifact_data(self, artifacts: list) -> Any:
        """Extract data from A2A artifacts"""
        if not artifacts:
            return None

        if len(artifacts) == 1:
            return artifacts[0].get("data")

        return [artifact.get("data") for artifact in artifacts]

    def bridge_request(self, tool_call: MCPToolCall, **context_opts) -> Dict[str, Any]:
        """
        Single-call bridge: MCP tool → A2A request

        Args:
            tool_call: MCP tool invocation
            **context_opts: Additional context (language, include_examples, etc.)

        Returns:
            A2A TaskRequest as dict
        """
        return self.mcp_to_a2a(tool_call, **context_opts)

    def bridge_response(self, a2a_response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Single-call bridge: A2A response → MCP result

        Args:
            a2a_response: A2A TaskResponse message

        Returns:
            MCP tool result as dict
        """
        return self.a2a_to_mcp(a2a_response)


# Example usage
if __name__ == "__main__":
    # Initialize bridge
    bridge = MCPtoA2ABridge(source_agent="mcp-client-001")

    # Example 1: Translate MCP tool call to A2A request
    print("=" * 60)
    print("MCP → A2A Translation Example")
    print("=" * 60)

    tool_call = MCPToolCall(
        tool_name="lookup_term",
        parameters={"term_id": "sle-001"}
    )

    a2a_request = bridge.mcp_to_a2a(tool_call, language="en")
    print("\nMCP Tool Call:")
    print(json.dumps(asdict(tool_call), indent=2))

    print("\nConverted to A2A TaskRequest:")
    print(json.dumps(a2a_request, indent=2))

    # Example 2: Translate A2A response back to MCP
    print("\n" + "=" * 60)
    print("A2A → MCP Translation Example")
    print("=" * 60)

    a2a_response = {
        "type": "TaskResponse",
        "id": str(uuid.uuid4()),
        "requestId": a2a_request["id"],
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "sourceAgent": {"agentId": "augmanitai"},
        "status": "success",
        "result": {
            "action": "term_lookup",
            "artifacts": [
                {
                    "type": "term",
                    "data": {
                        "id": "sle-001",
                        "name_en": "Symbiotic Linguistic Evolution",
                        "abbreviation": "SLE",
                        "definition_en": "The process by which human language and AI-generated language patterns co-evolve..."
                    }
                }
            ]
        },
        "metadata": {
            "processingTime": 45,
            "resultCount": 1,
            "language": "en"
        }
    }

    print("\nA2A TaskResponse:")
    print(json.dumps(a2a_response, indent=2))

    mcp_result = bridge.a2a_to_mcp(a2a_response)
    print("\nConverted to MCP Result:")
    print(json.dumps(mcp_result, indent=2))

    print("\n" + "=" * 60)
    print("Bridge Translation Complete")
    print("=" * 60)
