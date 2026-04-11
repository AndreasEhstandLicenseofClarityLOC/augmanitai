#!/usr/bin/env python3
"""
A2A ↔ ANP Protocol Bridge
Translates A2A task messages to ANP DID-wrapped messages and vice versa

Author: Andreas Ehstand
License: CC BY-NC-ND 4.0
"""

import json
import uuid
from datetime import datetime
from typing import Dict, Any, Optional
from hashlib import sha256
import base64


class A2AtoANPBridge:
    """Bridge translating A2A ↔ ANP (W3C Decentralized) protocol"""

    def __init__(
        self,
        agent_did: str = "did:web:augmanitai.local",
        agent_name: str = "AUGMANITAI"
    ):
        """
        Initialize bridge

        Args:
            agent_did: DID of the agent (default: AUGMANITAI DID)
            agent_name: Display name of agent
        """
        self.agent_did = agent_did
        self.agent_name = agent_name

    def a2a_to_anp(
        self,
        a2a_request: Dict[str, Any],
        source_did: str = "did:web:client.local"
    ) -> Dict[str, Any]:
        """
        Convert A2A task request to ANP P2P message with DID wrapping

        Args:
            a2a_request: A2A TaskRequest message
            source_did: DID of requesting agent

        Returns:
            ANP P2P message with verifiable credentials
        """
        # Create ANP message wrapper
        anp_message = {
            "@context": [
                "https://www.w3.org/ns/did/v1",
                "https://w3id.org/security/suites/jws-2020/v1"
            ],
            "type": "AgentMessage",
            "id": f"urn:uuid:{uuid.uuid4()}",
            "from": {
                "did": source_did,
                "agentId": a2a_request.get("sourceAgent", {}).get("agentId")
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
            "capabilities": self._extract_capabilities(a2a_request),
            "proof": self._generate_proof(a2a_request, source_did)
        }

        return anp_message

    def anp_to_a2a(
        self,
        anp_message: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Convert ANP P2P message to A2A task response

        Args:
            anp_message: ANP message with verifiable credentials

        Returns:
            A2A TaskResponse message
        """
        # Extract original A2A request from payload
        original_request = anp_message.get("payload", {}).get("a2aRequest", {})

        # Verify proof
        verified = self._verify_proof(anp_message)

        # Build A2A response
        a2a_response = {
            "@context": "https://google.github.io/A2A/v1/schema/task-response.jsonld",
            "type": "TaskResponse",
            "id": str(uuid.uuid4()),
            "requestId": original_request.get("id"),
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "version": "1.0",
            "sourceAgent": {
                "agentId": "augmanitai",
                "name": self.agent_name
            },
            "targetAgent": {
                "agentId": anp_message.get("from", {}).get("agentId")
            },
            "status": "success",
            "result": {
                "action": original_request.get("task", {}).get("action"),
                "artifacts": []
            },
            "metadata": {
                "anpVerified": verified,
                "anpSourceDid": anp_message.get("from", {}).get("did"),
                "anpMessageId": anp_message.get("id")
            }
        }

        return a2a_response

    def _extract_capabilities(self, a2a_request: Dict[str, Any]) -> list:
        """Extract agent capabilities needed for action"""
        action = a2a_request.get("task", {}).get("action")

        capability_map = {
            "term_lookup": ["read:terms", "public:augmanitai"],
            "term_search": ["read:terms", "search:full-text"],
            "term_relate": ["read:terms", "compute:relationships"],
            "term_validate_drift": ["read:terms", "analyze:semantics"],
            "list_domains": ["read:terms", "browse:domains"]
        }

        return capability_map.get(action, ["read:terms"])

    def _generate_proof(
        self,
        a2a_request: Dict[str, Any],
        source_did: str
    ) -> Dict[str, Any]:
        """
        Generate cryptographic proof for ANP message

        Args:
            a2a_request: Original A2A request
            source_did: Source agent DID

        Returns:
            Proof object (placeholder implementation)
        """
        # Create deterministic hash of message content
        content_hash = sha256(
            json.dumps(a2a_request, sort_keys=True).encode()
        ).hexdigest()

        proof = {
            "type": "DataIntegrityProof",
            "cryptosuite": "ed25519-rdfc-2022",
            "created": datetime.utcnow().isoformat() + "Z",
            "verificationMethod": f"{source_did}#key-1",
            "proofPurpose": "assertionMethod",
            "contentHash": content_hash,
            "proofValue": base64.b64encode(
                f"placeholder-signature-for-{content_hash}".encode()
            ).decode()
        }

        return proof

    def _verify_proof(self, anp_message: Dict[str, Any]) -> bool:
        """
        Verify ANP message proof (placeholder implementation)

        Args:
            anp_message: ANP message with proof

        Returns:
            True if proof verification succeeds
        """
        proof = anp_message.get("proof", {})

        # In production, verify actual cryptographic signature
        # For now, just check proof structure exists
        return (
            proof.get("type") == "DataIntegrityProof" and
            proof.get("verificationMethod") and
            proof.get("proofValue")
        )

    def wrap_credential(
        self,
        term_data: Dict[str, Any],
        issuer_did: str = "did:web:augmanitai.local"
    ) -> Dict[str, Any]:
        """
        Wrap term data in verifiable credential

        Args:
            term_data: AUGMANITAI term definition
            issuer_did: DID of issuer (default: AUGMANITAI)

        Returns:
            Verifiable Credential 2.0 format
        """
        vc = {
            "@context": [
                "https://www.w3.org/ns/credentials/v2",
                "https://www.w3.org/ns/credentials/examples/v2"
            ],
            "type": [
                "VerifiableCredential",
                "AugmanitaiTermCredential"
            ],
            "issuer": {
                "id": issuer_did,
                "name": "AUGMANITAI"
            },
            "issuanceDate": datetime.utcnow().isoformat() + "Z",
            "expirationDate": None,
            "credentialSubject": {
                "id": f"{issuer_did}#{term_data.get('id')}",
                "termId": term_data.get("id"),
                "abbreviation": term_data.get("abbreviation"),
                "nameEn": term_data.get("name_en"),
                "nameDe": term_data.get("name_de"),
                "definitionEn": term_data.get("definition_en"),
                "definitionDe": term_data.get("definition_de"),
                "domain": term_data.get("domain"),
                "examples": term_data.get("examples", [])
            },
            "proof": {
                "type": "DataIntegrityProof",
                "cryptosuite": "ed25519-rdfc-2022",
                "created": datetime.utcnow().isoformat() + "Z",
                "verificationMethod": f"{issuer_did}#key-1",
                "proofValue": base64.b64encode(
                    f"vc-proof-{term_data.get('id')}".encode()
                ).decode()
            }
        }

        return vc

    def extract_credential_subject(self, vc: Dict[str, Any]) -> Dict[str, Any]:
        """Extract term data from verifiable credential"""
        subject = vc.get("credentialSubject", {})

        return {
            "id": subject.get("termId"),
            "name_en": subject.get("nameEn"),
            "name_de": subject.get("nameDe"),
            "abbreviation": subject.get("abbreviation"),
            "definition_en": subject.get("definitionEn"),
            "definition_de": subject.get("definitionDe"),
            "domain": subject.get("domain"),
            "examples": subject.get("examples", [])
        }


# Example usage
if __name__ == "__main__":
    bridge = A2AtoANPBridge()

    print("=" * 70)
    print("A2A → ANP Translation Example")
    print("=" * 70)

    # Example A2A request
    a2a_request = {
        "type": "TaskRequest",
        "id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "sourceAgent": {
            "agentId": "client-agent-001",
            "name": "Client Agent"
        },
        "task": {
            "action": "term_lookup",
            "parameters": {"term_id": "sle-001"}
        }
    }

    print("\n1. Original A2A TaskRequest:")
    print(json.dumps(a2a_request, indent=2))

    # Convert to ANP
    anp_message = bridge.a2a_to_anp(
        a2a_request,
        source_did="did:web:client.local"
    )

    print("\n2. Converted to ANP P2P Message:")
    print(json.dumps(anp_message, indent=2))

    # Example term data wrapped in VC
    print("\n" + "=" * 70)
    print("Term Verifiable Credential Example")
    print("=" * 70)

    term_data = {
        "id": "sle-001",
        "abbreviation": "SLE",
        "name_en": "Symbiotic Linguistic Evolution",
        "name_de": "Symbiotische linguistische Entwicklung",
        "definition_en": "The process by which human language and AI-generated language patterns co-evolve...",
        "definition_de": "Der Prozess, durch den sich menschliche Sprache und KI-generierte Sprachmuster co-entwickeln...",
        "domain": "linguistic_dynamics",
        "examples": [
            "Users adopt AI-suggested phrasings",
            "Anthropomorphic language patterns emerge"
        ]
    }

    vc = bridge.wrap_credential(term_data)
    print("\nVerifiable Credential:")
    print(json.dumps(vc, indent=2))

    # Extract from VC
    extracted = bridge.extract_credential_subject(vc)
    print("\nExtracted from VC:")
    print(json.dumps(extracted, indent=2))

    print("\n" + "=" * 70)
    print("Bridge Translation Complete")
    print("=" * 70)
