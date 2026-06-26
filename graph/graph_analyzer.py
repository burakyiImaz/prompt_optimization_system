import networkx as nx


class GraphAnalyzer:

    def analyze(self, graph: nx.DiGraph):

        analysis = {}

        conflict_nodes = set()

        for u, v, data in graph.edges(data=True):
            if data.get("type") == "conflict":
                conflict_nodes.add(u)
                conflict_nodes.add(v)

        analysis["conflict_nodes"] = conflict_nodes

        centrality = nx.degree_centrality(graph)
        analysis["centrality"] = centrality

        analysis["sorted_importance"] = sorted(
            centrality.items(),
            key=lambda x: x[1],
            reverse=True
        )

        redundancy_pairs = []

        for u, v, data in graph.edges(data=True):
            if data.get("type") == "redundant":
                redundancy_pairs.append((u, v))

        analysis["redundancy_pairs"] = redundancy_pairs

        risk_scores = {}

        for node in graph.nodes():
            risk = 0

            for u, v, data in graph.edges(data=True):
                if v == node and data.get("type") == "conflict":
                    risk += 2

                if v == node and data.get("type") == "redundant":
                    risk += 1

            risk_scores[node] = risk

        analysis["risk_scores"] = risk_scores

        return analysis