#!/usr/bin/env python3
"""
AI Software Bill of Materials (SBOM) Generator — STRUCTURAL DEMONSTRATION ONLY.

This script is a structural demonstration of how a downstream operator could
generate SPDX 3.0 and CycloneDX 1.6 SBOMs for a hypothetical AI system that
USES AUGMANITAI terminology. AUGMANITAI itself is a manually curated
terminology DATASET, not a trained model or AI system. Running this script
does NOT produce a regulatory-compliant SBOM and does NOT assert any ISO
certification, EU AI Act conformity, or performance metrics for AUGMANITAI.

Descriptive linguistic research, not normative (§1). Longitudinal n=1
priority deposit, non-peer-reviewed per §11. ISO-inspired, not ISO-certified (§16). Restricted
applications per §20. See DISCLAIMER.md in the repository root.

Usage:
    python3 sbom-generator.py --system "EXAMPLE_SYSTEM" --version "1.0" --format spdx --output sbom.json
    python3 sbom-generator.py --system "EXAMPLE_SYSTEM" --version "1.0" --format cyclonedx --output sbom-cdx.json

Author: AUGMANITAI SBOM Module (demonstration code)
License: Apache-2.0 (code) / CC BY-NC-ND 4.0 (data outputs)
"""

import json
import hashlib
import uuid
from datetime import datetime, timezone
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from pathlib import Path
import argparse


@dataclass
class TrainingDataSource:
    """Training data source descriptor"""
    name: str
    count: int
    format: str
    category: str
    temporal_range: str
    license: str


@dataclass
class PerformanceMetric:
    """AI system performance metric"""
    metric_name: str
    metric_value: float
    metric_unit: str
    evaluation_date: str
    evaluation_method: str


@dataclass
class RiskItem:
    """Risk assessment item"""
    risk_id: str
    risk_name: str
    risk_severity: str
    risk_likelihood: str
    mitigation: str


class SBOMGenerator:
    """Generate SBOM documents for AI systems"""

    def __init__(self, system_name: str, system_version: str, organization: str):
        """Initialize SBOM generator"""
        self.system_name = system_name
        self.system_version = system_version
        self.organization = organization
        self.timestamp = datetime.now(timezone.utc).isoformat()
        self.uuid = str(uuid.uuid4())

    def _calculate_hash(self, content: str) -> str:
        """Calculate SHA-256 hash"""
        return hashlib.sha256(content.encode()).hexdigest()

    def generate_spdx_3_0(
        self,
        description: str,
        components: Dict[str, Any],
        training_data: List[TrainingDataSource],
        metrics: List[PerformanceMetric],
        risks: List[RiskItem]
    ) -> Dict[str, Any]:
        """Generate SPDX 3.0 AI Profile SBOM"""

        packages = []
        for comp_id, comp_data in components.items():
            package = {
                "SPDXID": f"SPDXRef-Package-{comp_id}",
                "name": comp_data["name"],
                "downloadLocation": comp_data.get("downloadLocation", "NOASSERTION"),
                "filesAnalyzed": False,
                "packageVersion": self.system_version,
                "packageLicenseConcluded": comp_data.get("license", "NOASSERTION"),
                "packageLicenseDeclared": comp_data.get("license", "NOASSERTION"),
                "packageCopyrightText": f"Copyright {datetime.now().year} {self.organization}",
                "description": comp_data.get("description", "")
            }
            packages.append(package)

        # Build relationships
        relationships = [
            {
                "spdxElementId": "SPDXRef-DOCUMENT",
                "relationshipType": "DESCRIBES",
                "relatedSpdxElement": "SPDXRef-Package-Core"
            }
        ]

        # Add training data sources
        training_data_obj = {
            "sources": len(training_data),
            "documents": sum(s.count for s in training_data),
            "temporal_range": self.system_version,
            "categories": list(set(s.category for s in training_data))
        }

        # Convert metrics
        metrics_list = [
            {
                "metric_name": m.metric_name,
                "metric_value": m.metric_value,
                "metric_unit": m.metric_unit,
                "evaluation_date": m.evaluation_date,
                "evaluation_method": m.evaluation_method
            }
            for m in metrics
        ]

        # Convert risks
        risks_list = [
            {
                "risk_id": r.risk_id,
                "risk_name": r.risk_name,
                "risk_severity": r.risk_severity,
                "risk_likelihood": r.risk_likelihood,
                "mitigation": r.mitigation
            }
            for r in risks
        ]

        sbom = {
            "spdxVersion": "SPDX-3.0.0",
            "dataLicense": "CC0-1.0",
            "SPDXID": "SPDXRef-DOCUMENT",
            "name": f"{self.system_name} AI Software Bill of Materials",
            "documentNamespace": f"https://sbom.example.com/{self.system_name.lower()}/spdx-3.0/{self.uuid}",
            "creationInfo": {
                "created": self.timestamp,
                "creators": [f"Tool: AUGMANITAI-SBOM-Generator-1.0", f"Organization: {self.organization}"],
                "licenseListVersion": "3.21"
            },
            "packages": packages,
            "relationships": relationships,
            "ai_profile_extensions": {
                "ai_system_type": "AugmantaiCompliantSystem",
                "system_description": description,
                "training_data_inventory": training_data_obj,
                "evaluation_metrics": metrics_list,
                "risk_management": risks_list
            }
        }

        return sbom

    def generate_cyclonedx_1_6(
        self,
        description: str,
        components: Dict[str, Any],
        training_data: List[TrainingDataSource],
        metrics: List[PerformanceMetric],
        risks: List[RiskItem]
    ) -> Dict[str, Any]:
        """Generate CycloneDX 1.6 ML-BOM SBOM"""

        # Build components array
        components_array = []
        for comp_id, comp_data in components.items():
            component = {
                "bom-ref": f"pkg:generic/{comp_id.lower()}@{self.system_version}",
                "type": comp_data.get("type", "library"),
                "name": comp_data["name"],
                "version": self.system_version,
                "scope": comp_data.get("scope", "required"),
                "description": comp_data.get("description", ""),
                "licenses": [
                    {
                        "license": {
                            "id": comp_data.get("license", "NOASSERTION")
                        }
                    }
                ]
            }
            components_array.append(component)

        # Build dependencies
        dependencies = [
            {
                "ref": f"pkg:generic/{self.system_name.lower()}@{self.system_version}",
                "dependsOn": [f"pkg:generic/{comp_id.lower()}@{self.system_version}" for comp_id in components.keys()]
            }
        ]

        sbom = {
            "bomFormat": "CycloneDX",
            "specVersion": "1.6",
            "serialNumber": f"urn:uuid:{self.uuid}",
            "version": 1,
            "metadata": {
                "timestamp": self.timestamp,
                "tools": [
                    {
                        "vendor": self.organization,
                        "name": "AUGMANITAI-SBOM-Generator",
                        "version": "1.0"
                    }
                ],
                "component": {
                    "bom-ref": f"pkg:generic/{self.system_name.lower()}@{self.system_version}",
                    "type": "application",
                    "name": self.system_name,
                    "version": self.system_version,
                    "description": description,
                    "supplier": {
                        "name": self.organization
                    }
                }
            },
            "components": components_array,
            "dependencies": dependencies,
            "ml_profile_extensions": {
                "model_information": {
                    "model_name": self.system_name,
                    "model_version": self.system_version,
                    "model_type": "FictionalExampleSystem",
                    "purpose": "Fictional example AI system for structural demonstration only — NOT a regulatory conformance claim for AUGMANITAI (dataset, §1/§11/§16/§20 of DISCLAIMER.md)"
                },
                "training_data": {
                    "dataset_name": f"{self.system_name} Training Corpus (fictional)",
                    "dataset_size": sum(s.count for s in training_data),
                    "data_sources": len(training_data),
                    "preprocessing_applied": "Fictional placeholder values; AUGMANITAI itself is manually curated, not trained"
                },
                "performance_metrics": [
                    {
                        "metric_name": m.metric_name,
                        "metric_value": m.metric_value,
                        "metric_unit": m.metric_unit,
                        "measurement_date": m.evaluation_date,
                        "measurement_method": m.evaluation_method
                    }
                    for m in metrics
                ],
                "risk_management": [
                    {
                        "risk_id": r.risk_id,
                        "risk_name": r.risk_name,
                        "risk_severity": r.risk_severity,
                        "risk_likelihood": r.risk_likelihood,
                        "mitigation": r.mitigation
                    }
                    for r in risks
                ]
            }
        }

        return sbom

    def save_sbom(self, sbom: Dict[str, Any], output_path: str) -> None:
        """Save SBOM to JSON file"""
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w') as f:
            json.dump(sbom, f, indent=2)
        print(f"SBOM saved to: {output_file}")


def create_example_sbom_spdx() -> Dict[str, Any]:
    """Generate SPDX SBOM for fictional generic EXAMPLE_SYSTEM.

    NOTE: Fictional demonstration only. Not a real system, not a real
    organization. See DISCLAIMER.md (§1, §20) — this structure must not be
    used as a template for §20-restricted applications (diagnostic, medical,
    HR screening, credit scoring, insurance assessment, surveillance, or
    profiling).
    """
    generator = SBOMGenerator(
        system_name="EXAMPLE_SYSTEM",
        system_version="1.0",
        organization="Example Organization (fictional)"
    )

    components = {
        "example-model": {
            "name": "EXAMPLE_SYSTEM ML Model",
            "description": "Fictional generic ML model for demonstration",
            "license": "Example-License",
            "downloadLocation": "Internal"
        },
        "example-data": {
            "name": "EXAMPLE_SYSTEM Training Data",
            "description": "Synthetic example dataset (fictional)",
            "license": "Example-License"
        },
        "augmanitai-terms": {
            "name": "AUGMANITAI Terminology",
            "description": "Descriptive terminology reference only",
            "license": "CC-BY-NC-ND-4.0",
            "downloadLocation": "https://zenodo.org/records/19481331"
        }
    }

    training_data = [
        TrainingDataSource(
            name="Synthetic Example Dataset",
            count=1000,
            format="Synthetic benchmark",
            category="Example",
            temporal_range="N/A (synthetic)",
            license="Example-License"
        )
    ]

    metrics = [
        PerformanceMetric(
            metric_name="Example Metric",
            metric_value=0.0,
            metric_unit="placeholder",
            evaluation_date="2026-01-01",
            evaluation_method="Placeholder — fictional demonstration"
        )
    ]

    risks = [
        RiskItem(
            risk_id="EXAMPLE-001",
            risk_name="Training Data Bias (illustrative)",
            risk_severity="Medium",
            risk_likelihood="Medium",
            mitigation="Placeholder — consult domain expertise"
        )
    ]

    return generator.generate_spdx_3_0(
        description="EXAMPLE_SYSTEM v1.0 — fictional generic SBOM demonstration (see DISCLAIMER.md §1, §20)",
        components=components,
        training_data=training_data,
        metrics=metrics,
        risks=risks
    )


def create_example_sbom_cyclonedx() -> Dict[str, Any]:
    """Generate CycloneDX SBOM for fictional generic EXAMPLE_SYSTEM.

    NOTE: Fictional demonstration only. See DISCLAIMER.md (§1, §20).
    """
    generator = SBOMGenerator(
        system_name="EXAMPLE_SYSTEM",
        system_version="1.0",
        organization="Example Organization (fictional)"
    )

    components = {
        "example-model": {
            "name": "EXAMPLE_SYSTEM ML Model",
            "description": "Fictional generic ML model",
            "type": "application",
            "license": "Example-License"
        },
        "example-data": {
            "name": "Synthetic Example Dataset",
            "type": "library",
            "license": "Example-License"
        },
        "augmanitai": {
            "name": "AUGMANITAI Terminology",
            "type": "library",
            "license": "CC-BY-NC-ND-4.0"
        }
    }

    training_data = [
        TrainingDataSource(
            name="Synthetic Example",
            count=1000,
            format="Synthetic",
            category="Example",
            temporal_range="N/A",
            license="Example-License"
        )
    ]

    metrics = [
        PerformanceMetric(
            metric_name="Example Metric",
            metric_value=0.0,
            metric_unit="placeholder",
            evaluation_date="2026-01-01",
            evaluation_method="Placeholder"
        )
    ]

    risks = [
        RiskItem(
            risk_id="EXAMPLE-001",
            risk_name="Illustrative bias placeholder",
            risk_severity="Medium",
            risk_likelihood="Medium",
            mitigation="Placeholder"
        )
    ]

    return generator.generate_cyclonedx_1_6(
        description="EXAMPLE_SYSTEM v1.0 — fictional CycloneDX demonstration (see DISCLAIMER.md §1, §20)",
        components=components,
        training_data=training_data,
        metrics=metrics,
        risks=risks
    )


def main():
    """CLI interface"""
    parser = argparse.ArgumentParser(description="AI SBOM Generator for AUGMANITAI Systems")
    parser.add_argument("--system", default="AUGMANITAI", help="System name")
    parser.add_argument("--version", default="1.0", help="System version")
    parser.add_argument("--format", choices=["spdx", "cyclonedx", "both"], default="both", help="SBOM format")
    parser.add_argument("--output", help="Output file path")
    parser.add_argument("--example", action="store_true", help="Generate fictional generic EXAMPLE_SYSTEM SBOM")

    args = parser.parse_args()

    if args.example:
        # Generate SPDX
        if args.format in ["spdx", "both"]:
            sbom = create_example_sbom_spdx()
            output = args.output or "example-sbom-spdx.json"
            generator = SBOMGenerator("EXAMPLE_SYSTEM", "1.0", "Example Organization (fictional)")
            generator.save_sbom(sbom, output)

        # Generate CycloneDX
        if args.format in ["cyclonedx", "both"]:
            sbom = create_example_sbom_cyclonedx()
            output = args.output or "example-sbom-cyclonedx.json"
            generator = SBOMGenerator("EXAMPLE_SYSTEM", "1.0", "Example Organization (fictional)")
            generator.save_sbom(sbom, output)

        print("Example SBOMs generated successfully")
    else:
        print(f"SBOM generation for {args.system} v{args.version} in {args.format} format")
        print("Populate with your system data and run again")


if __name__ == "__main__":
    main()
