import matplotlib.pyplot as plt
import networkx as nx


class GraphVisualizer:

    def visualize(self, graph: nx.DiGraph):

        pos = nx.spring_layout(graph, seed=42)

        plt.figure(figsize=(12, 7))

        nx.draw_networkx_nodes(
            graph,
            pos,
            node_size=900,
            node_color="lightgray"
        )

        edge_colors = []

        for u, v, data in graph.edges(data=True):

            if data["type"] == "conflict":
                edge_colors.append("red")
            elif data["type"] == "redundant":
                edge_colors.append("blue")
            elif data["type"] == "supports":
                edge_colors.append("green")
            else:
                edge_colors.append("gray")

        nx.draw_networkx_edges(
            graph,
            pos,
            edge_color=edge_colors,
            width=2
        )

        # LABELS
        labels = {
            node: f"{node}:{graph.nodes[node]['type']}"
            for node in graph.nodes()
        }

        nx.draw_networkx_labels(
            graph,
            pos,
            labels,
            font_size=9
        )

        plt.title("Prompt Optimization Graph IR")
        plt.axis("off")
        plt.show()