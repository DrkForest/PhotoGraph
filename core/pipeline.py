from core.image.scanner import scan_folder
from core.image.thumbnail import create_thumbnail
from core.clip.batch import generate_embeddings
from core.faiss.index import build_index
from core.faiss.search import search_similar
from core.graph.builder import build_graph
from core.graph.layout import build_layout

from core.models.photo import Photo

import numpy as np


def process_folder(folder):

    # IMAGE SCAN
    images = scan_folder(
        folder
    )

    photos = [
        Photo(
            image=image
        )
        for image in images
    ]


    # THUMBNAILS
    for photo in photos:

        photo.thumbnail = create_thumbnail(
            photo.image
        )


    # CLIP
    photos = generate_embeddings(
        photos
    )


    # FAISS
    index, photo_list = build_index(
        photos
    )

    vectors = np.stack(
        [
            photo.embedding
            for photo in photos
        ]
    ).astype("float32")


    similar = search_similar(
        index,
        vectors,
        photo_list
    )

    print("\n\n=== TEST AFTER SEARCH ===")
    print(f"Similar entries: {len(similar)}")

    for image, neighbours in similar.items():
        print(
            image.name,
            "->",
            len(neighbours),
            "neighbours"
        )

    print("=== END TEST ===\n\n")


    # TEMPORARY GRAPH ANALYSIS
    import networkx as nx

    graph_debug = nx.Graph()

    for image, neighbours in similar.items():

        graph_debug.add_node(image)

        for neighbour, score in neighbours:

            graph_debug.add_edge(
                image,
                neighbour.image,
                weight=score
            )

    components = list(
        nx.connected_components(graph_debug)
    )

    components.sort(
        key=len,
        reverse=True
    )

    print("\n=== GRAPH ANALYSIS ===")
    print(f"Nodes: {graph_debug.number_of_nodes()}")
    print(f"Edges: {graph_debug.number_of_edges()}")
    print(f"Components: {len(components)}")

    print("Component sizes:")

    for i, component in enumerate(components, 1):
        print(
            f"  {i}: {len(component)} photos"
        )

    isolated = list(
        nx.isolates(graph_debug)
    )

    print(f"Isolated: {len(isolated)}")


    # GRAPH
    graph = build_graph(
        similar
    )

    positions = build_layout(
        graph
    )


    return {
        "photos": photos,
        "similar": similar,
        "graph": graph,
        "positions": positions,
    }