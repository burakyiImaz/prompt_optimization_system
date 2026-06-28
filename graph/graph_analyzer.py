import networkx as nx


class GraphAnalyzer:

    def analyze(self, graph):

        analysis = {}


        conflict_nodes = set()

        for u, v, d in graph.edges(data=True):
            if d.get("type") == "conflict":
                conflict_nodes.add(u)
                conflict_nodes.add(v)

        analysis["conflict_nodes"] = conflict_nodes


        analysis["centrality"] = nx.degree_centrality(graph)

        analysis["pagerank"] = nx.pagerank(graph)


        risk = {}

        for node in graph.nodes():
            score = 0

            for u, v, d in graph.edges(data=True):

                if v == node and d.get("type") == "conflict":
                    score += 2

                if v == node and d.get("type") == "redundant":
                    score += 1

            risk[node] = score

        analysis["risk_scores"] = risk


        conflict_graph = nx.Graph()

        for u, v, d in graph.edges(data=True):
            if d.get("type") == "conflict":
                conflict_graph.add_edge(u, v)

        analysis["clusters"] = list(nx.connected_components(conflict_graph))

        return analysis