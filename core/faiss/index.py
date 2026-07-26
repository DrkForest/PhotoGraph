import faiss
import numpy as np

from core.models.photo import Photo


def build_index(
    photos: list[Photo]
):

    vectors = np.stack(
        [
            photo.embedding
            for photo in photos
        ]
    ).astype("float32")


    index = faiss.IndexFlatIP(
        vectors.shape[1]
    )


    index.add(
        vectors
    )


    return index, photos