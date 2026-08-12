import networkx as nx


def build_layout(graph):

    if not graph.nodes:
        return {}

    return nx.spring_layout(
        graph,
        seed=42,
        weight="weight",
        k=1.5,
        iterations=300
    )