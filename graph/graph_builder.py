import networkx as nx
from itertools import combinations
from optimizer.conflict_resolver import ConflictResolver


class GraphBuilder:

    def __init__(self):
        self.conflict_resolver = ConflictResolver()

    def build(self, rules):

        G = nx.DiGraph()

        for r in rules:
            G.add_node(r.id, text=r.text, type=r.rule_type)


        conflicts = self.conflict_resolver.detect_conflicts(rules)

        for c in conflicts:
            G.add_edge(c["rule_1"], c["rule_2"], type="conflict")


        for r1, r2 in combinations(rules, 2):
            if r1.text.lower() == r2.text.lower():
                G.add_edge(r1.id, r2.id, type="redundant")


        for r1, r2 in combinations(rules, 2):

            if r1.rule_type == "instruction" and r2.rule_type == "constraint":
                G.add_edge(r2.id, r1.id, type="controls")

            if r1.rule_type == r2.rule_type:
                G.add_edge(r1.id, r2.id, type="related")

        return Gc