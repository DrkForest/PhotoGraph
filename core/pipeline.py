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