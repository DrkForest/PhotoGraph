import networkx as nx


MIN_SIMILARITY = 0.70
WEIGHT_POWER = 2.5


def build_layout(graph):

    if not graph.nodes:
        return {}

    layout_graph = graph.copy()

    # Transform similarity into stronger nonlinear attraction.
    for u, v, data in layout_graph.edges(data=True):

        similarity = data.get("weight", 0.0)

        normalized = max(
            0.0,
            (similarity - MIN_SIMILARITY)
            / (1.0 - MIN_SIMILARITY)
        )

        data["weight"] = normalized ** WEIGHT_POWER

    components = list(nx.connected_components(layout_graph))

    positions = {}

    component_offset_x = 0

    for component in components:

        subgraph = layout_graph.subgraph(component)

        local_positions = nx.spring_layout(
            subgraph,
            seed=42,
            weight="weight",
            k=1.5,
            iterations=300,
        )

        for node, pos in local_positions.items():

            x, y = pos

            positions[node] = (
                x + component_offset_x,
                y,
            )

        component_offset_x += 3.0

    return positions