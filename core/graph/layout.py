import networkx as nx


def build_layout(graph):

    return nx.spring_layout(
        graph,
        seed=42,
        weight="weight",
        iterations=150
    )