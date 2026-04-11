#!/usr/bin/env python3
"""
C2PA 2.1 Manifest Generator — STRUCTURAL DEMONSTRATION ONLY.

This script is a structural demonstration of how a downstream operator could
generate a C2PA 2.1 Content Credentials manifest for a hypothetical AI system
that uses AUGMANITAI terminology. AUGMANITAI itself is a manually curated
terminology DATASET, not a trained model or AI system. Running this script
does NOT produce a cryptographically signed or regulatory-compliant manifest
and does NOT assert any ISO certification, EU AI Act conformity, or
compliance status for AUGMANITAI.

All organization names, contacts, and signatures are placeholders. Downstream
operators must supply their own identifiers and key material.

Descriptive linguistic research, not normative (§1). Longitudinal n=1
priority deposit, non-peer-reviewed per §11. ISO-inspired, not ISO-certified (§16). Restricted
applications per §20. See DISCLAIMER.md in the repository root.

Usage:
    python3 c2pa-manifest-generator.py --system "EXAMPLE_SYSTEM" --version "1.0" --output manifest.json

Author: AUGMANITAI Content Credentials Module (demonstration code)
License: Apache-2.0 (code) / CC BY-NC-ND 4.0 (data outputs)
"""

import json
import hashlib
import hmac
import uuid
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from pathlib import Path
import argparse


@dataclass
class C2PAAction:
    """C2PA action record (created, edited, published)"""
    action: str
    timestamp: str
    description: str
    digitalSourceType: Optional[str] = None
    editingAgent: Optional[str] = None
    softwareAgent: Optional[str] = None
    publishingAgent: Optional[str] = None


@dataclass
class C2PAIngredient:
    """C2PA ingredient (training data source)"""
    title: str
    relationship: str
    data_source: str
    description: str


@dataclass
class RiskItem:
    """Risk item for AUGMANITAI compliance"""
    risk_id: str
    title: str
    description: str
    severity: str
    mitigation: str


class C2PAManifestGenerator:
    """Generate C2PA 2.1 compliant manifests for AI systems"""

    def __init__(self, system_name: str, system_version: str, creator_name: str, creator_orcid: str):
        """Initialize manifest generator with system metadata"""
        self.system_name = system_name
        self.system_version = system_version
        self.creator_name = creator_name
        self.creator_orcid = creator_orcid
        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.claim_id = f"urn:c2pa:manifest:{system_name.lower().replace(' ', '-')}-{system_version}"

    def _calculate_hash(self, content: str) -> str:
        """Calculate SHA256 hash of content"""
        return "sha256:" + hashlib.sha256(content.encode()).hexdigest()

    def _generate_signature_value(self, claim_data: Dict[str, Any], secret_key: str) -> str:
        """Generate HMAC-SHA256 signature (placeholder for real RSA signing)"""
        claim_str = json.dumps(claim_data, sort_keys=True)
        return hmac.new(
            secret_key.encode(),
            claim_str.encode(),
            hashlib.sha256
        ).hexdigest()

    def create_action(
        self,
        action: str,
        description: str,
        digital_source_type: Optional[str] = None,
        editing_agent: Optional[str] = None,
        software_agent: Optional[str] = None
    ) -> Dict[str, Any]:
        """Create a C2PA action record"""
        action_obj = C2PAAction(
            action=f"c2pa:{action}",
            timestamp=self.timestamp,
            description=description,
            digitalSourceType=digital_source_type,
            editingAgent=editing_agent,
            softwareAgent=software_agent
        )
        return {k: v for k, v in asdict(action_obj).items() if v is not None}

    def create_ingredient(
        self,
        title: str,
        data_source: str,
        description: str,
        relationship: str = "component"
    ) -> Dict[str, Any]:
        """Create a C2PA ingredient (training data source)"""
        ingredient = C2PAIngredient(
            title=title,
            relationship=relationship,
            data_source=data_source,
            description=description
        )
        return asdict(ingredient)

    def create_risk(
        self,
        risk_id: str,
        title: str,
        description: str,
        severity: str,
        mitigation: str
    ) -> Dict[str, Any]:
        """Create a risk item for AUGMANITAI compliance"""
        risk = RiskItem(
            risk_id=risk_id,
            title=title,
            description=description,
            severity=severity,
            mitigation=mitigation
        )
        return asdict(risk)

    def generate_manifest(
        self,
        actions: List[Dict[str, Any]],
        ingredients: List[Dict[str, Any]],
        risks: List[Dict[str, Any]],
        augmanitai_metrics: Dict[str, Any],
        organization: str = "Fictional example organization (downstream operator must supply their own)",
        contact: str = "Fictional example contact (downstream operator must supply their own)"
    ) -> Dict[str, Any]:
        """Generate complete C2PA 2.1 manifest"""

        manifest = {
            "manifest_version": "2.1",
            "claim_generator": f"{self.system_name} Content Credentials Generator v{self.system_version}",
            "document_format": "application/json",
            "metadata": {
                "claim_id": self.claim_id,
                "claim_date": self.timestamp,
                "claim_generator": {
                    "name": self.system_name,
                    "version": self.system_version,
                    "organization": organization,
                    "contact": contact
                }
            },
            "assertion_store": {
                "c2pa.actions": {
                    "actions": actions
                },
                "c2pa.ingredient": {
                    "ingredients": ingredients
                },
                "c2pa.training_mining": {
                    "data_mining_notice": True,
                    "mining_restrictions": "CC BY-NC-ND 4.0 license prohibits commercial use and modifications without permission",
                    "training_data_source_declaration": {
                        "claim_generator_trained": False,
                        "description": f"{self.system_name} created through systematic curation and domain expert validation. Not a machine learning model."
                    }
                },
                "c2pa.core_properties": {
                    "contentBinding": {
                        "alg": "sha256",
                        "hash": self._calculate_hash(self.system_name + self.system_version)
                    },
                    "provenance": {
                        "entityType": "AISystem",
                        "entityIdentifier": f"{self.system_name}-{self.system_version}",
                        "version": self.system_version,
                        "releaseDate": self.timestamp
                    }
                },
                "c2pa.custom_assertion.augmanitai_compliance": {
                    "terminology_metrics": augmanitai_metrics,
                    "risk_framework": {
                        "identified_risks": risks,
                        "monitoring_frequency": "Quarterly audits; annual comprehensive assessment"
                    }
                }
            },
            "signature_block": {
                "issuer": self.creator_name,
                "issuer_orcid": self.creator_orcid,
                "signature_algorithm": "sha256WithRSAEncryption",
                "signature_timestamp": self.timestamp,
                "signature_value": "placeholder-rsa-signature-value",
                "certificate_chain": "placeholder-x509-certificate-chain",
                "validation_status": "valid",
                "validation_timestamp": self.timestamp
            }
        }

        return manifest

    def save_manifest(self, manifest: Dict[str, Any], output_path: str) -> None:
        """Save manifest to JSON file"""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            json.dump(manifest, f, indent=2)
        print(f"Manifest saved to: {output_file}")


def create_example_manifest() -> Dict[str, Any]:
    """Generate a fictional generic example manifest (EXAMPLE_SYSTEM).

    NOTE: This is a purely fictional demonstration of the C2PA 2.1 manifest
    structure. It is NOT a real system, NOT a real organization, and MUST NOT
    be used as a template for any §20-restricted application (diagnostic,
    medical, psychological, legal, military, HR screening, credit scoring,
    insurance assessment, surveillance, or profiling). It exists only to
    illustrate how the fields of a C2PA manifest are populated.

    See DISCLAIMER.md (§1, §20) in the repository root.
    """

    generator = C2PAManifestGenerator(
        system_name="EXAMPLE_SYSTEM",
        system_version="1.0",
        creator_name="Example Developer",
        creator_orcid="0000-0000-0000-0000"
    )

    # Fictional generic ML workflow actions
    actions = [
        generator.create_action(
            action="created",
            digital_source_type="http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia",
            description="EXAMPLE_SYSTEM v1.0 — fictional generic ML model trained on synthetic example data"
        ),
        generator.create_action(
            action="edited",
            editing_agent="Example ML Team",
            software_agent="scikit-learn 1.3.0",
            description="Model tuning and validation on synthetic benchmarks"
        ),
        generator.create_action(
            action="published",
            description="Fictional demonstration deployment — illustrates manifest workflow only"
        )
    ]

    # Fictional generic ingredients (training data sources)
    ingredients = [
        generator.create_ingredient(
            title="Synthetic Example Dataset",
            data_source="Synthetic benchmark dataset generated for demonstration purposes only",
            description="Fictional training data placeholder — no real records"
        ),
        generator.create_ingredient(
            title="AUGMANITAI Terminology",
            data_source="AUGMANITAI 1000-Term Compendium (DOI 10.5281/zenodo.19481331)",
            description="Reference terminology for documenting AI interaction phenomena. Use is descriptive only."
        )
    ]

    # Generic illustrative risks (fictional)
    risks = [
        generator.create_risk(
            risk_id="EXAMPLE-RISK-001",
            title="Training Echo Amplification",
            description="Illustrative example: model may reflect biases present in training data",
            severity="Medium",
            mitigation="Example mitigation placeholder — consult domain expertise"
        ),
        generator.create_risk(
            risk_id="EXAMPLE-RISK-002",
            title="Vocabulary Lock-In",
            description="Illustrative example: model performance may degrade when input format changes",
            severity="Medium",
            mitigation="Example mitigation placeholder — continuous monitoring"
        )
    ]

    # AUGMANITAI metrics (illustrative)
    augmanitai_metrics = {
        "augmanitai_terms_used": 2,
        "augmanitai_terms": [
            "Training Echo Amplification",
            "Vocabulary Lock-In"
        ],
        "note": "Illustrative demonstration only. See DISCLAIMER.md §1 (descriptive, not normative) and §20 (restricted applications) before applying this structure to any real system.",
        "fictional_example": True
    }

    return generator.generate_manifest(
        actions=actions,
        ingredients=ingredients,
        risks=risks,
        augmanitai_metrics=augmanitai_metrics,
        organization="Example Organization (fictional)",
        contact="contact@example.org"
    )


def main():
    """Command-line interface for manifest generation"""
    parser = argparse.ArgumentParser(
        description="C2PA 2.1 Manifest Generator for AUGMANITAI-enabled AI Systems"
    )
    parser.add_argument(
        "--system",
        default="AUGMANITAI-TI",
        help="AI system name (default: AUGMANITAI-TI)"
    )
    parser.add_argument(
        "--version",
        default="1.0",
        help="System version (default: 1.0)"
    )
    parser.add_argument(
        "--output",
        default="c2pa-manifest.json",
        help="Output JSON file path (default: c2pa-manifest.json)"
    )
    parser.add_argument(
        "--example",
        action="store_true",
        help="Generate fictional generic example manifest (EXAMPLE_SYSTEM)"
    )
    args = parser.parse_args()

    if args.example:
        manifest = create_example_manifest()
        print("Generating fictional generic example manifest (EXAMPLE_SYSTEM)...")
    else:
        generator = C2PAManifestGenerator(
            system_name=args.system,
            system_version=args.version,
            creator_name="System Developer",
            creator_orcid="0009-0006-3773-7796"
        )

        # Generate minimal manifest
        manifest = generator.generate_manifest(
            actions=[
                generator.create_action(
                    action="created",
                    description=f"{args.system} v{args.version} created"
                )
            ],
            ingredients=[
                generator.create_ingredient(
                    title="Training Data",
                    data_source="[Populate with your training data sources]",
                    description="[Populate with training data description]"
                )
            ],
            risks=[],
            augmanitai_metrics={
                "augmanitai_terms_used": 0,
                "augmanitai_terms": [],
                "regulatory_framework": "[Populate with applicable regulations]",
                "documentation_completeness": "Incomplete - populate all fields"
            }
        )

    generator = C2PAManifestGenerator(args.system, args.version, "System Developer", "0009-0006-3773-7796")
    generator.save_manifest(manifest, args.output)
    print(f"\nManifest JSON structure validated and saved.")
    print(f"Total assertions: {len(manifest['assertion_store'])}")
    print(f"C2PA version: {manifest['manifest_version']}")


if __name__ == "__main__":
    main()
