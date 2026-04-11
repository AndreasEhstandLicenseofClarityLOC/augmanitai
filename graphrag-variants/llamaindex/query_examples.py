"""
LlamaIndex Query Examples for AUGMANITAI PropertyGraphStore
Demonstrates subgraph retrieval, entity traversal, and relationship queries
"""

import json
from typing import List, Dict, Set, Tuple
from pathlib import Path


class AUGMANITAIQueryEngine:
    """Query engine for AUGMANITAI PropertyGraphStore index"""

    def __init__(self, data_dir: str = "."):
        """Initialize query engine"""
        self.data_dir = Path(data_dir)
        self.property_graph = self._load_property_graph()
        self.triples = self._load_triples()
        self.schema = self._load_schema()

    def _load_property_graph(self) -> Dict:
        """Load property graph data"""
        with open(self.data_dir / "property_graph.json") as f:
            return json.load(f)

    def _load_triples(self) -> List[Dict]:
        """Load triple data"""
        with open(self.data_dir / "kg_triples.json") as f:
            return json.load(f).get("triples", [])

    def _load_schema(self) -> Dict:
        """Load schema"""
        with open(self.data_dir / "schema.json") as f:
            return json.load(f)

    def query_entity(self, entity_id: str) -> Dict:
        """Query details of a single entity"""
        for node in self.property_graph.get("nodes", []):
            if node["id"] == entity_id:
                return {
                    "entity": node,
                    "relationships_outgoing": self.query_outgoing_relationships(entity_id),
                    "relationships_incoming": self.query_incoming_relationships(entity_id),
                }
        return {"error": f"Entity {entity_id} not found"}

    def query_outgoing_relationships(self, source_id: str) -> List[Dict]:
        """Query relationships where source_id is the source"""
        results = []
        for rel in self.property_graph.get("relationships", []):
            if rel["source_id"] == source_id:
                results.append(rel)
        return results

    def query_incoming_relationships(self, target_id: str) -> List[Dict]:
        """Query relationships where target_id is the target"""
        results = []
        for rel in self.property_graph.get("relationships", []):
            if rel["target_id"] == target_id:
                results.append(rel)
        return results

    def query_neighbors_by_relationship_type(
        self, entity_id: str, relationship_type: str
    ) -> Dict:
        """Query neighbors connected by a specific relationship type"""
        neighbors = {
            "outgoing": [],
            "incoming": [],
        }

        for rel in self.property_graph.get("relationships", []):
            if rel["source_id"] == entity_id and rel["label"] == relationship_type:
                neighbors["outgoing"].append(
                    {
                        "target": rel["target_id"],
                        "strength": rel["properties"]["strength"],
                    }
                )
            elif rel["target_id"] == entity_id and rel["label"] == relationship_type:
                neighbors["incoming"].append(
                    {
                        "source": rel["source_id"],
                        "strength": rel["properties"]["strength"],
                    }
                )

        return neighbors

    def query_subgraph_bfs(
        self, start_id: str, max_depth: int = 2
    ) -> Dict:
        """Query subgraph using breadth-first search"""
        visited = {start_id}
        queue = [(start_id, 0)]
        nodes = {start_id: None}
        edges = []

        while queue:
            current_id, depth = queue.pop(0)

            if depth >= max_depth:
                continue

            # Find all relationships from current node
            for rel in self.property_graph.get("relationships", []):
                if rel["source_id"] == current_id:
                    target_id = rel["target_id"]
                    edges.append(rel)

                    if target_id not in visited:
                        visited.add(target_id)
                        nodes[target_id] = None
                        queue.append((target_id, depth + 1))

                elif rel["target_id"] == current_id:
                    source_id = rel["source_id"]
                    edges.append(rel)

                    if source_id not in visited:
                        visited.add(source_id)
                        nodes[source_id] = None
                        queue.append((source_id, depth + 1))

        # Collect node details
        for node in self.property_graph.get("nodes", []):
            if node["id"] in nodes:
                nodes[node["id"]] = node

        return {
            "start_id": start_id,
            "depth": max_depth,
            "nodes": nodes,
            "edges": edges,
            "node_count": len(nodes),
            "edge_count": len(edges),
        }

    def query_domain_entities(self, domain: str) -> Dict:
        """Query all entities in a specific domain"""
        entities = []
        for node in self.property_graph.get("nodes", []):
            if node["properties"].get("domain") == domain:
                entities.append(node)
        return {
            "domain": domain,
            "count": len(entities),
            "entities": entities,
        }

    def query_high_degree_nodes(self, threshold: int = 10) -> List[Dict]:
        """Query nodes with degree >= threshold"""
        high_degree = []
        for node in self.property_graph.get("nodes", []):
            degree = node["properties"].get("degree", 0)
            if degree >= threshold:
                high_degree.append(node)
        high_degree.sort(key=lambda x: x["properties"].get("degree", 0), reverse=True)
        return high_degree

    def query_strongest_relationships(self, min_strength: float = 0.9) -> List[Dict]:
        """Query relationships with strength >= threshold"""
        strong_rels = []
        for rel in self.property_graph.get("relationships", []):
            strength = rel["properties"].get("strength", 0.0)
            if strength >= min_strength:
                strong_rels.append(rel)
        strong_rels.sort(
            key=lambda x: x["properties"].get("strength", 0.0), reverse=True
        )
        return strong_rels

    def query_relationship_type_distribution(self) -> Dict:
        """Query distribution of relationship types"""
        distribution = {}
        for rel in self.property_graph.get("relationships", []):
            rel_type = rel["label"]
            distribution[rel_type] = distribution.get(rel_type, 0) + 1
        return dict(sorted(distribution.items(), key=lambda x: x[1], reverse=True))

    def query_entity_type_distribution(self) -> Dict:
        """Query distribution of entity types"""
        distribution = {}
        for node in self.property_graph.get("nodes", []):
            entity_type = node["properties"].get("type", "Unknown")
            distribution[entity_type] = distribution.get(entity_type, 0) + 1
        return dict(sorted(distribution.items(), key=lambda x: x[1], reverse=True))

    def query_shortest_path(self, start_id: str, end_id: str) -> Dict:
        """Find shortest path between two nodes"""
        from collections import deque

        visited = {start_id}
        queue = deque([(start_id, [start_id])])
        shortest_path = None

        while queue:
            current_id, path = queue.popleft()

            if current_id == end_id:
                shortest_path = path
                break

            # Explore neighbors (both directions)
            for rel in self.property_graph.get("relationships", []):
                next_id = None
                if rel["source_id"] == current_id:
                    next_id = rel["target_id"]
                elif rel["target_id"] == current_id:
                    next_id = rel["source_id"]

                if next_id and next_id not in visited:
                    visited.add(next_id)
                    queue.append((next_id, path + [next_id]))

        return {
            "start": start_id,
            "end": end_id,
            "path": shortest_path,
            "distance": len(shortest_path) - 1 if shortest_path else None,
        }

    def query_symmetric_relationships(self) -> List[Tuple[str, str]]:
        """Find pairs of entities with bidirectional relationships"""
        symmetric = []
        rels_dict = {}

        for rel in self.property_graph.get("relationships", []):
            key = (rel["source_id"], rel["target_id"], rel["label"])
            rels_dict[key] = True

        for rel in self.property_graph.get("relationships", []):
            reverse_key = (rel["target_id"], rel["source_id"], rel["label"])
            if reverse_key in rels_dict:
                pair = tuple(sorted([rel["source_id"], rel["target_id"]]))
                if pair not in symmetric:
                    symmetric.append(pair)

        return symmetric


# Example queries
def run_example_queries():
    """Run example queries and print results"""
    engine = AUGMANITAIQueryEngine(".")

    print("=" * 80)
    print("AUGMANITAI PropertyGraphStore Query Examples")
    print("=" * 80)

    # Query 1: Single entity
    print("\n1. Entity Query (sle):")
    result = engine.query_entity("sle")
    print(f"   Entity: {result['entity']['label']}")
    print(f"   Outgoing relationships: {len(result['relationships_outgoing'])}")
    print(f"   Incoming relationships: {len(result['relationships_incoming'])}")

    # Query 2: Domain entities
    print("\n2. Domain Query (linguistic_dynamics):")
    result = engine.query_domain_entities("linguistic_dynamics")
    print(f"   Found {result['count']} entities in domain")
    for entity in result["entities"]:
        print(f"     - {entity['label']}")

    # Query 3: High degree nodes
    print("\n3. High-Degree Nodes (degree >= 12):")
    nodes = engine.query_high_degree_nodes(threshold=12)
    for node in nodes:
        print(f"   {node['label']}: degree {node['properties']['degree']}")

    # Query 4: Strong relationships
    print("\n4. Strongest Relationships (strength >= 0.94):")
    rels = engine.query_strongest_relationships(min_strength=0.94)
    for rel in rels[:5]:
        print(f"   {rel['source_id']} --{rel['label']}--> {rel['target_id']} ({rel['properties']['strength']})")

    # Query 5: Relationship type distribution
    print("\n5. Relationship Type Distribution:")
    dist = engine.query_relationship_type_distribution()
    for rel_type, count in list(dist.items())[:5]:
        print(f"   {rel_type}: {count}")

    # Query 6: Entity type distribution
    print("\n6. Entity Type Distribution:")
    dist = engine.query_entity_type_distribution()
    for entity_type, count in dist.items():
        print(f"   {entity_type}: {count}")

    # Query 7: Subgraph
    print("\n7. Subgraph Query (starting from 'rke', depth=2):")
    subgraph = engine.query_subgraph_bfs("rke", max_depth=2)
    print(f"   Nodes: {subgraph['node_count']}")
    print(f"   Edges: {subgraph['edge_count']}")

    # Query 8: Shortest path
    print("\n8. Shortest Path Query (sle -> cod):")
    path = engine.query_shortest_path("sle", "cod")
    if path["path"]:
        print(f"   Path: {' -> '.join(path['path'])}")
        print(f"   Distance: {path['distance']} hops")

    # Query 9: Neighbors by relationship type
    print("\n9. Neighbors by Relationship Type (rke + DEPENDS_ON):")
    neighbors = engine.query_neighbors_by_relationship_type("rke", "DEPENDS_ON")
    print(f"   Outgoing: {neighbors['outgoing']}")
    print(f"   Incoming: {neighbors['incoming']}")

    # Query 10: Symmetric relationships
    print("\n10. Symmetric Relationships:")
    symmetric = engine.query_symmetric_relationships()
    print(f"   Found {len(symmetric)} symmetric pairs")
    for pair in symmetric[:3]:
        print(f"     {pair[0]} <-> {pair[1]}")


if __name__ == "__main__":
    run_example_queries()
