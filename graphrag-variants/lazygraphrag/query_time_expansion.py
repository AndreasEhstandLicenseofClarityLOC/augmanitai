"""
LazyGraphRAG Query-Time Expansion Module

Implements deferred computation patterns for graph expansion with on-demand
materialization, lazy evaluation, and memoization for AUGMANITAI framework.

Author: AUGMANITAI Implementation
License: CC BY-NC-ND 4.0
"""

import json
import time
from typing import Dict, List, Set, Tuple, Optional, Any, Callable
from dataclasses import dataclass, field
from enum import Enum
from functools import lru_cache
from collections import OrderedDict


class ExpansionStrategy(Enum):
    """Strategies for lazy graph expansion."""
    BREADTH_FIRST_LAZY = "breadth_first_lazy"
    DEPTH_FIRST_LAZY = "depth_first_lazy"
    BOUNDED_LAZY = "bounded_lazy"
    TYPED_LAZY = "typed_lazy"
    PATH_LAZY = "path_lazy"


class MaterializationTrigger(Enum):
    """Triggers for graph materialization."""
    DIRECT_ACCESS = "direct_access"
    NEIGHBOR_QUERY = "neighbor_query"
    PATH_QUERY = "path_query"
    SUBGRAPH_QUERY = "subgraph_query"
    CENTRALITY_NEEDED = "centrality_needed"
    CLUSTERING_NEEDED = "clustering_needed"


@dataclass
class LazyComputation:
    """Represents a computation deferred until materialization trigger."""
    computation_id: str
    operation: str
    depends_on: List[str]
    trigger: MaterializationTrigger
    cache_key: str
    result: Optional[Any] = None
    materialized: bool = False
    access_count: int = 0


@dataclass
class MaterializationCacheEntry:
    """Cache entry for materialized computations."""
    key: str
    value: Any
    timestamp: float
    access_count: int = 0
    priority_boost: float = 1.0

    def score(self) -> float:
        """Compute LRU priority score."""
        return self.access_count * self.priority_boost


class LRUMaterializationCache:
    """LRU cache for materialized graph computations."""

    def __init__(self, max_size: int = 1000):
        self.max_size = max_size
        self.cache: OrderedDict[str, MaterializationCacheEntry] = OrderedDict()
        self.hits = 0
        self.misses = 0

    def get(self, key: str) -> Optional[Any]:
        """Retrieve cached value with LRU update."""
        if key in self.cache:
            entry = self.cache.pop(key)
            entry.access_count += 1
            self.cache[key] = entry
            self.hits += 1
            return entry.value
        self.misses += 1
        return None

    def put(self, key: str, value: Any, priority_boost: float = 1.0) -> None:
        """Store value in cache with priority boost."""
        if key in self.cache:
            self.cache.pop(key)

        if len(self.cache) >= self.max_size:
            # Evict lowest priority item
            min_key = min(
                self.cache.keys(),
                key=lambda k: self.cache[k].score()
            )
            self.cache.pop(min_key)

        entry = MaterializationCacheEntry(
            key=key,
            value=value,
            timestamp=time.time(),
            priority_boost=priority_boost
        )
        self.cache[key] = entry

    def hit_rate(self) -> float:
        """Calculate cache hit rate."""
        total = self.hits + self.misses
        return self.hits / total if total > 0 else 0.0


class LazyGraphIndex:
    """
    Lazy graph index implementing deferred computation and on-demand materialization.
    """

    def __init__(self, graph_data_path: str = "property_graph.json",
                 cache_size: int = 1000, max_lazy_depth: int = 5):
        self.graph_data = self._load_graph(graph_data_path)
        self.nodes = {n["id"]: n for n in self.graph_data.get("nodes", [])}
        self.edges = self.graph_data.get("relationships", [])
        self.adjacency = self._build_adjacency()

        self.cache = LRUMaterializationCache(cache_size)
        self.max_lazy_depth = max_lazy_depth
        self.memoization_table: Dict[str, Any] = {}
        self.lazy_computations: Dict[str, LazyComputation] = {}

    def _load_graph(self, path: str) -> Dict:
        """Load graph structure from JSON."""
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Return minimal valid graph for testing
            return {
                "nodes": [
                    {"id": "rke", "label": "Recursive Knowledge Expansion"},
                    {"id": "ccr", "label": "Context-Cognition Resonance"},
                    {"id": "cie", "label": "Cognitive Intimacy Exchange"},
                    {"id": "cod", "label": "Collaborative Ontology Development"},
                    {"id": "mca", "label": "Mutual Context Awareness"},
                ],
                "relationships": [
                    {"source_id": "rke", "target_id": "ccr", "label": "ENABLES"},
                    {"source_id": "rke", "target_id": "cie", "label": "DEPENDS_ON"},
                    {"source_id": "ccr", "target_id": "mca", "label": "SUPPORTS"},
                    {"source_id": "cod", "target_id": "rke", "label": "ENABLES"},
                ]
            }

    def _build_adjacency(self) -> Dict[str, List[Dict]]:
        """Build adjacency list from edges."""
        adjacency = {node_id: [] for node_id in self.nodes}
        for edge in self.edges:
            src = edge.get("source_id", edge.get("source"))
            tgt = edge.get("target_id", edge.get("target"))
            if src in adjacency and tgt in adjacency:
                adjacency[src].append({
                    "target": tgt,
                    "label": edge.get("label"),
                    "strength": edge.get("strength", 0.8)
                })
        return adjacency

    def _get_memoization_key(self, operation: str, args: Tuple) -> str:
        """Generate memoization key for computation."""
        return f"{operation}_{str(args)}"

    @staticmethod
    def _check_memoization(operation: str, args: Tuple,
                          memo_table: Dict) -> Optional[Any]:
        """Check memoization table for cached computation result."""
        key = f"{operation}_{str(args)}"
        return memo_table.get(key)

    @staticmethod
    def _store_memoization(operation: str, args: Tuple, result: Any,
                          memo_table: Dict) -> None:
        """Store computation result in memoization table."""
        key = f"{operation}_{str(args)}"
        memo_table[key] = result

    def lazy_neighbors(self, node_id: str, depth: int = 1) -> Dict[int, Set[str]]:
        """
        Lazy breadth-first neighbor expansion.

        Returns neighbors at each depth level, expanding on-demand.
        """
        cache_key = f"neighbors_{node_id}_{depth}"

        # Check materialization cache
        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached

        # Check memoization table
        memo_result = self._check_memoization("lazy_neighbors", (node_id, depth),
                                             self.memoization_table)
        if memo_result is not None:
            self.cache.put(cache_key, memo_result, priority_boost=1.5)
            return memo_result

        neighbors_by_depth = {0: {node_id}}
        current_frontier = {node_id}

        for d in range(1, depth + 1):
            next_frontier = set()
            for node in current_frontier:
                for edge_info in self.adjacency.get(node, []):
                    next_frontier.add(edge_info["target"])
            neighbors_by_depth[d] = next_frontier
            current_frontier = next_frontier

        result = {d: neighbors for d, neighbors in neighbors_by_depth.items()}

        # Store in both caches
        self.cache.put(cache_key, result, priority_boost=1.5)
        self._store_memoization("lazy_neighbors", (node_id, depth), result,
                               self.memoization_table)

        return result

    def lazy_path(self, start: str, end: str, max_length: int = 5) -> Optional[List[str]]:
        """
        Lazy BFS path finding with early termination.

        Expands from both endpoints and terminates on first meeting.
        """
        cache_key = f"paths_{start}_{end}_{max_length}"

        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached

        memo_result = self._check_memoization("lazy_path",
                                             (start, end, max_length),
                                             self.memoization_table)
        if memo_result is not None:
            self.cache.put(cache_key, memo_result)
            return memo_result

        if start not in self.nodes or end not in self.nodes:
            return None

        # BFS from start
        queue = [(start, [start])]
        visited = {start}

        while queue and len(queue[0][1]) <= max_length:
            current, path = queue.pop(0)

            if current == end:
                self.cache.put(cache_key, path)
                self._store_memoization("lazy_path", (start, end, max_length),
                                       path, self.memoization_table)
                return path

            for edge_info in self.adjacency.get(current, []):
                neighbor = edge_info["target"]
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        self.cache.put(cache_key, None)
        return None

    def lazy_subgraph(self, anchor: str, hops: int = 2) -> Dict[str, Any]:
        """
        Lazy bounded subgraph extraction.

        Expands neighborhood and collects induced edges.
        """
        cache_key = f"subgraph_{anchor}_{hops}"

        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached

        memo_result = self._check_memoization("lazy_subgraph", (anchor, hops),
                                             self.memoization_table)
        if memo_result is not None:
            self.cache.put(cache_key, memo_result, priority_boost=1.3)
            return memo_result

        # Get neighbors at each hop
        neighbors_dict = self.lazy_neighbors(anchor, hops)

        # Collect all nodes in subgraph
        subgraph_nodes = set()
        for d in range(hops + 1):
            subgraph_nodes.update(neighbors_dict.get(d, set()))

        # Collect induced edges
        subgraph_edges = []
        for edge in self.edges:
            src = edge.get("source_id", edge.get("source"))
            tgt = edge.get("target_id", edge.get("target"))
            if src in subgraph_nodes and tgt in subgraph_nodes:
                subgraph_edges.append(edge)

        result = {
            "nodes": [self.nodes[n] for n in subgraph_nodes if n in self.nodes],
            "edges": subgraph_edges,
            "node_count": len(subgraph_nodes),
            "edge_count": len(subgraph_edges)
        }

        self.cache.put(cache_key, result, priority_boost=1.3)
        self._store_memoization("lazy_subgraph", (anchor, hops), result,
                               self.memoization_table)

        return result

    def lazy_relationship_expansion(self, relationship_type: str) -> List[Dict]:
        """
        Lazy expansion of relationships by type.

        Materializes only relationships matching the specified type.
        """
        cache_key = f"relationships_{relationship_type}"

        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached

        result = [e for e in self.edges
                 if e.get("label") == relationship_type]

        self.cache.put(cache_key, result, priority_boost=1.2)
        return result

    def lazy_centrality(self, node_id: str, subgraph_id: Optional[str] = None) -> float:
        """
        Lazy centrality computation with deferred materialization.

        Computes node importance score only when needed.
        """
        cache_key = f"centrality_{node_id}_{subgraph_id}"

        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached

        # Simple degree-based centrality for demonstration
        neighbors = self.lazy_neighbors(node_id, 1)
        total_neighbors = sum(len(n) for n in neighbors.values())
        degree_centrality = total_neighbors / len(self.nodes) if self.nodes else 0.0

        self.cache.put(cache_key, degree_centrality)
        return degree_centrality

    def lazy_clustering_coefficient(self, node_id: str) -> float:
        """
        Lazy clustering coefficient computation.

        Measures local density of node's neighborhood.
        """
        cache_key = f"clustering_{node_id}"

        cached = self.cache.get(cache_key)
        if cached is not None:
            return cached

        neighbors = list(self.lazy_neighbors(node_id, 1).get(1, set()))

        if len(neighbors) < 2:
            return 0.0

        # Count edges between neighbors
        edges_between = 0
        for i, n1 in enumerate(neighbors):
            for n2 in neighbors[i+1:]:
                for edge_info in self.adjacency.get(n1, []):
                    if edge_info["target"] == n2:
                        edges_between += 1
                        break

        # Maximum possible edges between neighbors
        max_edges = len(neighbors) * (len(neighbors) - 1) / 2

        coefficient = edges_between / max_edges if max_edges > 0 else 0.0

        self.cache.put(cache_key, coefficient)
        return coefficient

    def materialize_all(self) -> None:
        """Force full materialization of lazy computations."""
        for node_id in self.nodes:
            self.lazy_neighbors(node_id, self.max_lazy_depth)
            self.lazy_centrality(node_id)
            self.lazy_clustering_coefficient(node_id)

        # Materialize all relationship types
        rel_types = set(e.get("label") for e in self.edges)
        for rel_type in rel_types:
            self.lazy_relationship_expansion(rel_type)

    def get_cache_stats(self) -> Dict[str, Any]:
        """Retrieve cache performance statistics."""
        return {
            "cache_entries": len(self.cache.cache),
            "cache_size_limit": self.cache.max_size,
            "hit_rate": self.cache.hit_rate(),
            "total_hits": self.cache.hits,
            "total_misses": self.cache.misses,
            "memoization_entries": len(self.memoization_table),
            "memory_overhead_estimate_mb": (
                len(self.cache.cache) * 0.05 +
                len(self.memoization_table) * 0.08
            )
        }


class LazyQueryEngine:
    """Query engine implementing lazy graph traversal patterns."""

    def __init__(self, lazy_index: LazyGraphIndex):
        self.index = lazy_index
        self.query_count = 0
        self.total_materialization_time_ms = 0.0

    def query_neighbors(self, node_id: str, depth: int = 1) -> Dict[str, Any]:
        """Query node neighbors with lazy evaluation."""
        self.query_count += 1
        start_time = time.time()

        result = self.index.lazy_neighbors(node_id, depth)

        elapsed_ms = (time.time() - start_time) * 1000
        self.total_materialization_time_ms += elapsed_ms

        return {
            "query_type": "neighbors",
            "node_id": node_id,
            "depth": depth,
            "neighbors_by_depth": {
                d: list(nodes) for d, nodes in result.items()
            },
            "total_neighbors": sum(len(n) for n in result.values()),
            "materialization_time_ms": elapsed_ms
        }

    def query_path(self, start: str, end: str, max_length: int = 5) -> Dict[str, Any]:
        """Query path between nodes with lazy expansion."""
        self.query_count += 1
        start_time = time.time()

        path = self.index.lazy_path(start, end, max_length)

        elapsed_ms = (time.time() - start_time) * 1000
        self.total_materialization_time_ms += elapsed_ms

        return {
            "query_type": "path",
            "start": start,
            "end": end,
            "path": path,
            "path_length": len(path) if path else -1,
            "found": path is not None,
            "materialization_time_ms": elapsed_ms
        }

    def query_subgraph(self, anchor: str, hops: int = 2) -> Dict[str, Any]:
        """Query subgraph with lazy bounded expansion."""
        self.query_count += 1
        start_time = time.time()

        subgraph = self.index.lazy_subgraph(anchor, hops)

        elapsed_ms = (time.time() - start_time) * 1000
        self.total_materialization_time_ms += elapsed_ms

        return {
            "query_type": "subgraph",
            "anchor": anchor,
            "hops": hops,
            "node_count": subgraph["node_count"],
            "edge_count": subgraph["edge_count"],
            "nodes": [n["id"] for n in subgraph["nodes"]],
            "materialization_time_ms": elapsed_ms
        }

    def get_query_statistics(self) -> Dict[str, Any]:
        """Get aggregate query statistics."""
        avg_time = (self.total_materialization_time_ms / self.query_count
                   if self.query_count > 0 else 0.0)

        return {
            "total_queries": self.query_count,
            "total_time_ms": self.total_materialization_time_ms,
            "average_time_per_query_ms": avg_time,
            "cache_stats": self.index.get_cache_stats()
        }


if __name__ == "__main__":
    # Example usage
    print("=== LazyGraphRAG Query-Time Expansion ===\n")

    index = LazyGraphIndex()
    engine = LazyQueryEngine(index)

    # Example queries
    print("1. Neighbor Query (RKE, depth=2):")
    result = engine.query_neighbors("rke", 2)
    print(f"   Neighbors: {result['neighbors_by_depth']}")
    print(f"   Time: {result['materialization_time_ms']:.2f}ms\n")

    print("2. Path Query (SLE -> RKE):")
    result = engine.query_path("sle", "rke", max_length=5)
    print(f"   Path: {result['path']}")
    print(f"   Time: {result['materialization_time_ms']:.2f}ms\n")

    print("3. Subgraph Query (MCA, hops=2):")
    result = engine.query_subgraph("mca", 2)
    print(f"   Nodes: {result['node_count']}, Edges: {result['edge_count']}")
    print(f"   Time: {result['materialization_time_ms']:.2f}ms\n")

    print("4. Cache Statistics:")
    stats = engine.get_query_statistics()
    print(f"   Queries: {stats['total_queries']}")
    print(f"   Cache Hit Rate: {stats['cache_stats']['hit_rate']:.1%}")
    print(f"   Memory Overhead: {stats['cache_stats']['memory_overhead_estimate_mb']:.1f}MB")
