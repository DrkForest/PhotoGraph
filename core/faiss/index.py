import faiss
import numpy as np


def build_index(embeddings: dict):

    images = list(embeddings.keys())

    vectors = np.stack(
        list(embeddings.values())
    ).astype("float32")

    index = faiss.IndexFlatIP(
        vectors.shape[1]
    )

    index.add(vectors)

    return index, images