from core.image.scanner import scan_folder
from core.image.thumbnail import create_thumbnail
from core.clip.batch import generate_embeddings
from core.faiss.index import build_index
from core.faiss.search import search_similar

import numpy as np


def process_folder(folder):

    images = scan_folder(
        folder
    )

    thumbnails = []

    for image in images:

        thumbnail = create_thumbnail(image)
        thumbnails.append(thumbnail)

    embeddings = generate_embeddings(thumbnails)

    index, image_list = build_index(embeddings)

    vectors = np.stack(list(embeddings.values())).astype("float32")

    similar = search_similar(
        index,
        vectors,
        image_list
    )

    return {
        "images": images,
        "thumbnails": thumbnails,
        "embeddings": embeddings,
        "similar": similar,
    }