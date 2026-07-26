import networkx as nx


def build_graph(similar):

    graph = nx.Graph()

    for image_path, neighbours in similar.items():

        graph.add_node(
            image_path
        )

        for photo, score in neighbours:

            graph.add_node(
                photo.image
            )

            graph.add_edge(
                image_path,
                photo.image,
                weight=score
            )

    return graph