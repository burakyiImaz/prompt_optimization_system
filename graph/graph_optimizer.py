import networkx as nx


class GraphOptimizer:

    def optimize(self, graph: nx.DiGraph, analysis: dict):

        nodes_to_remove = set()

        for node in analysis.get("conflict_nodes", []):
            nodes_to_remove.add(node)

        risk_scores = analysis.get("risk_scores", {})

        for node, score in risk_scores.items():
            if score >= 2:
                nodes_to_remove.add(node)

        for node in nodes_to_remove:
            if graph.has_node(node):
                graph.remove_node(node)

        return graph