"""
LlamaIndex PropertyGraphStore Index Builder for AUGMANITAI
Implements SchemaLLMPathExtractor pattern for knowledge graph construction
"""

import json
import os
from typing import List, Dict, Any
from pathlib import Path

from llama_index.core import Document
from llama_index.core.schema import PropertyGraphNode, PropertyGraphRelationship
from llama_index.graph_stores import SimplePropertyGraphStore
from llama_index.llm.openai import OpenAI


class AUGMANITAIIndexBuilder:
    """Builder for AUGMANITAI PropertyGraphStore index"""

    def __init__(self, data_dir: str = "."):
        """Initialize the index builder with data directory"""
        self.data_dir = Path(data_dir)
        self.property_graph_store = SimplePropertyGraphStore()
        self.llm = OpenAI(model="gpt-4-turbo", temperature=0.7)
        self.schema = self._load_schema()
        self.nodes_data = self._load_json("property_graph.json")
        self.triples_data = self._load_json("kg_triples.json")

    def _load_schema(self) -> Dict[str, Any]:
        """Load schema definition"""
        schema_path = self.data_dir / "schema.json"
        with open(schema_path, "r") as f:
            return json.load(f)

    def _load_json(self, filename: str) -> Dict[str, Any]:
        """Load JSON file"""
        filepath = self.data_dir / filename
        with open(filepath, "r") as f:
            return json.load(f)

    def build_from_nodes(self) -> None:
        """Build index from nodes and relationships in property_graph.json"""
        print("Building PropertyGraphStore from nodes...")

        # Add all nodes to the graph store
        for node in self.nodes_data.get("nodes", []):
            pg_node = PropertyGraphNode(
                id_=node["id"],
                label=node["label"],
                properties=node.get("properties", {}),
            )
            self.property_graph_store.add_node(pg_node)
            print(f"Added node: {node['id']} ({node['label']})")

        # Add all relationships to the graph store
        for rel in self.nodes_data.get("relationships", []):
            pg_rel = PropertyGraphRelationship(
                source_id=rel["source_id"],
                target_id=rel["target_id"],
                label=rel["label"],
                properties=rel.get("properties", {}),
            )
            self.property_graph_store.add_relationship(pg_rel)
            print(f"Added relationship: {rel['source_id']} --{rel['label']}--> {rel['target_id']}")

    def build_from_triples(self) -> None:
        """Build index from triples in kg_triples.json"""
        print("\nBuilding PropertyGraphStore from triples...")

        triples = self.triples_data.get("triples", [])
        for triple in triples:
            # Ensure source and target nodes exist
            source_id = triple["subject"]
            target_id = triple["object"]

            # Add relationship
            pg_rel = PropertyGraphRelationship(
                source_id=source_id,
                target_id=target_id,
                label=triple["predicate"],
                properties={"strength": triple.get("strength", 0.8)},
            )
            self.property_graph_store.add_relationship(pg_rel)

        print(f"Added {len(triples)} triple relationships")

    def validate_graph(self) -> Dict[str, Any]:
        """Validate the constructed graph"""
        stats = {
            "total_nodes": len(self.property_graph_store.data["nodes"]),
            "total_relationships": len(self.property_graph_store.data["relationships"]),
            "node_ids": list(self.property_graph_store.data["nodes"].keys()),
            "relationship_types": set(),
        }

        for rel in self.property_graph_store.data["relationships"].values():
            for r in rel:
                stats["relationship_types"].add(r.label)

        stats["relationship_types"] = sorted(list(stats["relationship_types"]))
        return stats

    def query_neighbors(self, node_id: str, max_depth: int = 2) -> Dict[str, Any]:
        """Query immediate neighbors of a node"""
        result = {
            "node_id": node_id,
            "neighbors": [],
            "depth": max_depth,
        }

        # Get neighbors from property graph store
        if node_id in self.property_graph_store.data["relationships"]:
            for rel in self.property_graph_store.data["relationships"][node_id]:
                result["neighbors"].append(
                    {
                        "target": rel.target_id,
                        "relationship": rel.label,
                        "strength": rel.properties.get("strength", 0.0),
                    }
                )

        return result

    def query_paths(
        self, start_id: str, end_id: str, max_depth: int = 3
    ) -> List[List[str]]:
        """Find paths between two nodes (simple BFS)"""
        paths = []
        visited = set()
        queue = [(start_id, [start_id])]

        while queue:
            current, path = queue.pop(0)

            if len(path) > max_depth + 1:
                continue

            if current == end_id:
                paths.append(path)
                continue

            if current in visited:
                continue

            visited.add(current)

            # Explore neighbors
            if current in self.property_graph_store.data["relationships"]:
                for rel in self.property_graph_store.data["relationships"][current]:
                    if rel.target_id not in visited:
                        queue.append((rel.target_id, path + [rel.target_id]))

        return paths

    def export_stats(self, output_path: str = "build_stats.json") -> None:
        """Export index building statistics"""
        stats = self.validate_graph()
        stats["paths_example"] = {
            "sle_to_cod": self.query_paths("sle", "cod", max_depth=3),
            "rke_to_pdt": self.query_paths("rke", "pdt", max_depth=3),
        }
        stats["neighbors_example"] = {
            "sle": self.query_neighbors("sle"),
            "rke": self.query_neighbors("rke"),
            "cod": self.query_neighbors("cod"),
        }

        with open(output_path, "w") as f:
            json.dump(stats, f, indent=2)

        print(f"\nExported stats to {output_path}")


def main():
    """Main entry point for index building"""
    # Initialize builder
    builder = AUGMANITAIIndexBuilder(data_dir=".")

    # Build from nodes and relationships
    builder.build_from_nodes()

    # Validate the graph
    print("\nValidating graph...")
    validation = builder.validate_graph()
    print(f"Graph has {validation['total_nodes']} nodes and {validation['total_relationships']} relationships")
    print(f"Relationship types: {len(validation['relationship_types'])}")

    # Example queries
    print("\nExample neighbor query (sle):")
    print(json.dumps(builder.query_neighbors("sle"), indent=2))

    print("\nExample path query (sle -> cod):")
    paths = builder.query_paths("sle", "cod", max_depth=3)
    for i, path in enumerate(paths):
        print(f"  Path {i+1}: {' -> '.join(path)}")

    # Export statistics
    builder.export_stats()

    print("\nIndex build complete!")


if __name__ == "__main__":
    main()
