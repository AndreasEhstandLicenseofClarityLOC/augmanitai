#!/usr/bin/env python3
"""
ANP ↔ MCP Protocol Bridge
Translates ANP DID-wrapped messages back to MCP tool calls

Author: Andreas Ehstand
License: CC BY-NC-ND 4.0
"""

import json
import uuid
from datetime import datetime
from typing import Dict, Any, Optional


class ANPtoMCPBridge:
    """Bridge translating ANP ↔ MCP protocol"""

    # ANP action → MCP tool mapping
    ANP_ACTION_TO_MCP_TOOL = {
        "term_lookup": "lookup_term",
        "term_search": "search_terms",
        "term_relate": "get_related",
        "list_domains": "list_domains"
    }

    # MCP tool → ANP action mapping
    MCP_TOOL_TO_ANP_ACTION = {v: k for k, v in ANP_ACTION_TO_MCP_TOOL.items()}

    # Parameter mapping: ANP → MCP
    ANP_PARAM_TO_MCP = {
        "term_lookup": {
            "term_id": "term_id"
        },
        "term_search": {
            "query": "query",
            "limit": "limit"
        },
        "term_relate": {
            "term_id": "term_id"
        },
        "list_domains": {}
    }

    # Parameter mapping: MCP → ANP
    MCP_PARAM_TO_ANP = {
        "lookup_term": {
            "term_id": "term_id"
        },
        "search_terms": {
            "query": "query",
            "limit": "limit"
        },
        "get_related": {
            "term_id": "term_id"
        },
        "list_domains": {}
    }

    def __init__(self, agent_did: str = "did:web:augmanitai.local"):
        """
        Initialize bridge

        Args:
            agent_did: DID of AUGMANITAI agent
        """
        self.agent_did = agent_did

    def anp_to_mcp(self, anp_message: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert ANP message to MCP tool call

        Args:
            anp_message: ANP P2P message

        Returns:
            MCP tool call structure
        """
        # Extract A2A request from ANP payload
        a2a_request = anp_message.get("payload", {}).get("a2aRequest", {})
        a2a_task = a2a_request.get("task", {})
        action = a2a_task.get("action")

        # Map action to MCP tool
        mcp_tool = self.ANP_ACTION_TO_MCP_TOOL.get(action)
        if not mcp_tool:
            raise ValueError(f"Unknown ANP action: {action}")

        # Map parameters
        param_mapping = self.ANP_PARAM_TO_MCP.get(action, {})
        mcp_params = {}
        for anp_key, mcp_key in param_mapping.items():
            if anp_key in a2a_task.get("parameters", {}):
                mcp_params[mcp_key] = a2a_task["parameters"][anp_key]

        # Build MCP tool call
        mcp_call = {
            "tool": mcp_tool,
            "parameters": mcp_params,
            "metadata": {
                "source_did": anp_message.get("from", {}).get("did"),
                "anp_message_id": anp_message.get("id"),
                "anp_verified": self._verify_anp_proof(anp_message),
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
        }

        return mcp_call

    def mcp_to_anp(
        self,
        mcp_tool: str,
        mcp_params: Dict[str, Any],
        source_did: str = "did:web:client.local"
    ) -> Dict[str, Any]:
        """
        Convert MCP tool call to ANP message

        Args:
            mcp_tool: MCP tool name
            mcp_params: MCP tool parameters
            source_did: DID of requesting agent

        Returns:
            ANP P2P message
        """
        # Map MCP tool to ANP action
        action = self.MCP_TOOL_TO_ANP_ACTION.get(mcp_tool)
        if not action:
            raise ValueError(f"Unknown MCP tool: {mcp_tool}")

        # Map parameters
        param_mapping = self.MCP_PARAM_TO_ANP.get(mcp_tool, {})
        anp_params = {}
        for mcp_key, anp_key in param_mapping.items():
            if mcp_key in mcp_params:
                anp_params[anp_key] = mcp_params[mcp_key]

        # Create A2A request
        a2a_request = {
            "@context": "https://google.github.io/A2A/v1/schema/task-request.jsonld",
            "type": "TaskRequest",
            "id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "version": "1.0",
            "sourceAgent": {
                "agentId": "anp-bridge",
                "name": "ANP Bridge"
            },
            "targetAgent": {
                "agentId": "augmanitai"
            },
            "task": {
                "action": action,
                "parameters": anp_params
            }
        }

        # Wrap in ANP message
        anp_message = {
            "@context": [
                "https://www.w3.org/ns/did/v1",
                "https://w3id.org/security/suites/jws-2020/v1"
            ],
            "type": "AgentMessage",
            "id": f"urn:uuid:{uuid.uuid4()}",
            "from": {
                "did": source_did,
                "agentId": "anp-bridge"
            },
            "to": {
                "did": self.agent_did,
                "agentId": "augmanitai"
            },
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "messageType": "taskRequest",
            "payload": {
                "a2aRequest": a2a_request
            },
            "capabilities": self._extract_capabilities(action),
            "proof": self._create_proof(source_did)
        }

        return anp_message

    def _extract_capabilities(self, action: str) -> list:
        """Extract required capabilities for ANP action"""
        capability_map = {
            "term_lookup": ["read:terms", "public:augmanitai"],
            "term_search": ["read:terms", "search:full-text"],
            "term_relate": ["read:terms", "compute:relationships"],
            "list_domains": ["read:terms", "browse:domains"]
        }

        return capability_map.get(action, ["read:terms"])

    def _create_proof(self, did: str) -> Dict[str, Any]:
        """Create placeholder cryptographic proof"""
        return {
            "type": "DataIntegrityProof",
            "cryptosuite": "ed25519-rdfc-2022",
            "created": datetime.utcnow().isoformat() + "Z",
            "verificationMethod": f"{did}#key-1",
            "proofPurpose": "assertionMethod",
            "proofValue": "placeholder-proof-signature"
        }

    def _verify_anp_proof(self, anp_message: Dict[str, Any]) -> bool:
        """Verify ANP message proof (placeholder)"""
        proof = anp_message.get("proof", {})
        return (
            proof.get("type") == "DataIntegrityProof" and
            proof.get("verificationMethod") and
            proof.get("proofValue")
        )

    def extract_did_document(
        self,
        anp_message: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """
        Extract DID document reference from ANP message

        Args:
            anp_message: ANP message

        Returns:
            DID document or None
        """
        from_did = anp_message.get("from", {}).get("did")

        if not from_did:
            return None

        # Placeholder: in production, would resolve DID document
        return {
            "@context": "https://www.w3.org/ns/did/v1",
            "id": from_did,
            "type": ["Agent"],
            "verificationMethod": [
                {
                    "id": f"{from_did}#key-1",
                    "type": "JsonWebKey2020",
                    "controller": from_did
                }
            ]
        }

    def validate_anp_message(self, anp_message: Dict[str, Any]) -> bool:
        """
        Validate ANP message structure

        Args:
            anp_message: ANP message to validate

        Returns:
            True if valid, False otherwise
        """
        required_fields = ["type", "from", "to", "payload"]

        for field in required_fields:
            if field not in anp_message:
                return False

        # Validate structure
        if anp_message.get("type") != "AgentMessage":
            return False

        if not anp_message.get("from", {}).get("did"):
            return False

        if not anp_message.get("to", {}).get("did"):
            return False

        if not anp_message.get("payload", {}).get("a2aRequest"):
            return False

        return True


# Example usage
if __name__ == "__main__":
    bridge = ANPtoMCPBridge()

    print("=" * 70)
    print("ANP → MCP Translation Example")
    print("=" * 70)

    # Example ANP message
    anp_message = {
        "@context": [
            "https://www.w3.org/ns/did/v1",
            "https://w3id.org/security/suites/jws-2020/v1"
        ],
        "type": "AgentMessage",
        "id": f"urn:uuid:{uuid.uuid4()}",
        "from": {
            "did": "did:web:client.local",
            "agentId": "client-agent"
        },
        "to": {
            "did": "did:web:augmanitai.local",
            "agentId": "augmanitai"
        },
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "messageType": "taskRequest",
        "payload": {
            "a2aRequest": {
                "type": "TaskRequest",
                "id": str(uuid.uuid4()),
                "task": {
                    "action": "term_search",
                    "parameters": {
                        "query": "semantic drift",
                        "limit": 5
                    }
                }
            }
        },
        "capabilities": ["read:terms", "search:full-text"],
        "proof": {
            "type": "DataIntegrityProof",
            "verificationMethod": "did:web:client.local#key-1",
            "proofValue": "placeholder-proof"
        }
    }

    print("\n1. ANP P2P Message:")
    print(json.dumps(anp_message, indent=2)[:500] + "...")

    # Validate
    is_valid = bridge.validate_anp_message(anp_message)
    print(f"\n2. Message Valid: {is_valid}")

    # Convert to MCP
    mcp_call = bridge.anp_to_mcp(anp_message)
    print("\n3. Converted to MCP Tool Call:")
    print(json.dumps(mcp_call, indent=2))

    # Reverse: MCP → ANP
    print("\n" + "=" * 70)
    print("MCP → ANP Translation Example")
    print("=" * 70)

    anp_from_mcp = bridge.mcp_to_anp(
        mcp_tool="search_terms",
        mcp_params={"query": "recursive knowledge", "limit": 10},
        source_did="did:web:client.local"
    )

    print("\nANP Message Created from MCP Call:")
    print(json.dumps(anp_from_mcp, indent=2)[:500] + "...")

    print("\n" + "=" * 70)
    print("Bridge Translation Complete")
    print("=" * 70)
